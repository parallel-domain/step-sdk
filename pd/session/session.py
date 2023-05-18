# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utilities to communicate with Parallel Domain's servers

You can use the :class:`StepIgSession` context manager to establish a Step session in a Pythonic way.
Or you can use the :func:`create_step_ig_session` function while exploring our API in a terminal environment.
Same applies for :class:`StreamIgSession` and :func:`create_stream_ig_session`.
"""

import logging
import re
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional, Union, List, Tuple

import flatbuffers
import numpy as np

import pd.core.errors
from pd.core.errors import PdError
from pd.internal.fb.generated.python import (
    pdAck,
    pdEnableStateStream,
    pdIgState,
    pdIgStateType,
    pdLoadLocation,
    pdMessage,
    pdQueryRuntimeInfo,
    pdQuerySensorData,
    pdQueryStateData,
    pdQuerySystemInfo,
    pdReturnLidarSensorData,
    pdReturnRuntimeInfo,
    pdReturnScenarioData,
    pdReturnSensorData,
    pdReturnStateData,
    pdReturnSystemInfo,
    pdRuntimeInfo,
    pdRuntimeInfoType,
    pdSetCaptureParameters,
    pdSetGlobalParams,
    pdSubmitScenarioConfig,
    pdSubmitScenarioGenConfig,
    pdUpdateState,
    pdResponseCode,
    pdRaycastQuery,
    pdRaycastHits,
    pdFloat3
)
from pd.internal.fb.generated.python.pdMessageType import pdMessageType
from pd.internal.fb.generated.python.pdPerformanceFeature import pdPerformanceFeature
from pd.session.transport import TlsProxyForZmqTransport, ZmqTransport
from pd.state.sensor import LidarSensorData, SensorBuffer, SensorData
from pd.state.serialize import state_to_bytes, bytes_to_state
from pd.state.state import State
from pd.sim.sim import Raycast, RaycastHit

logger = logging.getLogger(__name__)


_SERVER_URL_REGEX = r"(?P<protocol>tcp|ssl)://(?P<hostname>\S+):(?P<port>\d+)"


def is_server_url(url: str) -> bool:
    """
    Returns :obj:`True` if given url is a valid address for a Step server

    Args:
        url: The url to check

    Returns:
        `True` if given url is a valid address for a Step server
    """
    return re.match(_SERVER_URL_REGEX, url) is not None


@dataclass(frozen=True)
class Version:
    """
    Semantic version

    See `Semantic Versioning 2.0.0 <https://semver.org/>`_
    """

    major: int
    minor: int
    patch: int
    build: str


@dataclass(frozen=True)
class SystemInfo:
    """
    Server information

    Provides system information about the server.
    """

    version: Version
    """Server API version"""


class RuntimeState(Enum):
    """
    Enumerates runtime states of the server
    """

    Disconnected = auto()
    """Not connected to any clients"""

    Connected = auto()
    """Connected to a client, is idle"""

    Backing = auto()
    """Unloading a map"""

    Loading = auto()
    """Loading a map"""

    Loaded = auto()
    """Finished loading a map, is idle"""

    Capturing = auto()
    """Capturing"""

    Finishing = auto()
    """Finishing"""


class PdMessageMixin:
    @staticmethod
    def _build_pd_message(builder, msg, msg_type):
        pdMessage.pdMessageStart(builder)
        pdMessage.pdMessageAddMessageType(builder, msg_type)
        pdMessage.pdMessageAddMessage(builder, msg)
        msg = pdMessage.pdMessageEnd(builder)
        return msg

    @classmethod
    def _consume_ack(cls, resp_bytes: bytes):
        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdAck:
            cls._raise_error_for_ack(ack_msg)
        else:
            cls._raise_error_for_unknown_message()

    @staticmethod
    def _raise_error_for_ack(ack_msg):
        ack = pdAck.pdAck()
        ack.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
        response = ack.Response().decode()
        code = ack.Code()
        logger.debug(f"Ack response: {response}")
        if code == pdResponseCode.pdResponseCode.CONFIG_ERROR:
            raise PdError(
                f"Given configuration is invalid. "
                f"Reason: {response}"
            )
        elif code == pdResponseCode.pdResponseCode.SERVER_ERROR:
            raise PdError(
                f"Server experienced an error. "
                f"Reason: {response}"
            )
        elif code == pdResponseCode.pdResponseCode.UNHANDLED_MESSAGE_TYPE:
            raise PdError(
                f"Server couldn't handle this request. "
                f"Reason: {response}"
            )
        elif code != pdResponseCode.pdResponseCode.OK:
            raise PdError(
                f"Error occurred while processing the request. "
                f"Reason: {response}"
            )

    @staticmethod
    def _raise_error_for_unknown_message():
        raise PdError(
            "Server sent an unexpected response. "
            "Please contact support@paralleldomain.com for support."
        )


class IgSession(PdMessageMixin):
    """
    Base class for communication with Step IG and Stream IG servers
    """

    def __init__(self, request_addr: str, state_addr: Optional[str] = None, client_cert_file: Optional[str] = None):
        """
        Args:
            request_addr: Address for request socket.
            state_addr: Address for state socket.
                        If :obj:`None`, uses request socket for :class:`~pd.state.State` messages.
            client_cert_file: Path to credentials file for SSL/TLS protocol
        """
        if not request_addr:
            raise PdError("request_addr is required.")
        addr_re = re.compile(_SERVER_URL_REGEX)
        request_addr_match = addr_re.match(request_addr)
        if not request_addr_match:
            raise pd.core.errors.PdError(
                f"Invalid request address provided: {request_addr}. "
                "Must be of the form tcp://hostname:port or ssl://hostname:port"
            )
        if request_addr_match.group("protocol") == "ssl" and not client_cert_file:
            raise pd.core.errors.PdError("TLS certificate path missing: required when using ssl protocol")
        if state_addr:
            state_addr_match = addr_re.match(state_addr)
            if not state_addr_match or state_addr_match.group("protocol") != "tcp":
                raise pd.core.errors.PdError(
                    f"Invalid state address provided: {state_addr}. " "Must be of the form tcp://hostname:port"
                )

        if request_addr_match.group("protocol") == "ssl":
            hostname = request_addr_match.group("hostname")
            port = int(request_addr_match.group("port"))
            self.transport = TlsProxyForZmqTransport(hostname, port, client_cert_file)
        else:
            self.transport = ZmqTransport(request_addr, state_addr)
        self.stream_addr = state_addr
        self._system_info = None

    def __enter__(self):
        self.transport.__enter__()

        # Query system info from server
        self._system_info = self._query_system_info()

        return self

    def __exit__(self, *args):
        return self.transport.__exit__(*args)

    @property
    def system_info(self) -> SystemInfo:
        """
        System information about the server

        Returns:
            System info
        """
        return self._system_info

    def load_default_location(self):
        """
        Load a default map
        """
        self.load_location(
            location_name="Test_SF_6thAndMission_small", time_of_day="LS_sky_noon_mostlySunny_1250_HDS025"
        )

    def load_location(self, location_name: str, time_of_day: str):
        """
        Load a new map

        Args:
            location_name: Name of the location to load
            time_of_day: Name of the time of day setting to load
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_location(builder, location_name, time_of_day)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())
        self._consume_ack(resp_bytes)

    def _update_state(self, state: State, step_mode=False):
        self._update_state_bytes(state_to_bytes(state), step_mode)

    def _update_state_bytes(self, state_bytes, step_mode=False):
        builder = flatbuffers.Builder(1024 + len(state_bytes))
        msg = self._build_pd_update_state(builder, state_bytes, step_mode)
        builder.Finish(msg)
        self.transport.send_state_msg(builder.Output())

        if step_mode:
            self._consume_ack(self.transport.receive_state_msg())

    def query_sensor_data(
        self, agent_id: int, sensor_name: str, buffer: SensorBuffer
    ) -> Optional[Union[SensorData, LidarSensorData]]:
        """
        Query server for sensor data

        Args:
            agent_id: Agent's unique identifier
            sensor_name: Name of the sensor
            buffer: Type of sensor data to fetch

        Returns:
            Sensor data returned from backend
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_query_sensor_data(builder, agent_id, sensor_name, buffer)

        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdReturnSensorData:
            return_msg = pdReturnSensorData.pdReturnSensorData()
            return_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            width, height = return_msg.Width(), return_msg.Height()
            data = return_msg.DataAsNumpy()
            if width > 0 and height > 0:
                data = data.reshape((height, width, -1))
            else:
                raise PdError(f"Failed to retrieve sensor data for sensor '{sensor_name}' attached to agent {agent_id}")
            sensor_data = SensorData(width=width, height=height, data=data)
            return sensor_data

        elif msg_type == pdMessageType.pdReturnLidarSensorData:
            return_msg = pdReturnLidarSensorData.pdReturnLidarSensorData()
            return_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            num_points, point_size = return_msg.NumPoints(), return_msg.PointSize()

            data_bytes = return_msg.DataAsNumpy().tobytes()
            data = np.frombuffer(data_bytes, dtype=np.float32)
            num_values_per_point = point_size // np.dtype(np.float32).itemsize
            data = data.reshape((num_points, num_values_per_point))
            data = data[:, :3]

            sensor_data = LidarSensorData(num_points=num_points, data=data)
            return sensor_data

        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    def _set_global_params(self, use_zmq, performance_type):
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_set_global_params(builder, use_zmq, performance_type)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())
        self._consume_ack(resp_bytes)

    def _set_capture_parameters(self, agent_id, sensor_name, frame_rate, bit_rate):
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_set_capture_parameters(builder, agent_id, sensor_name, frame_rate, bit_rate)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())
        self._consume_ack(resp_bytes)

    def _enable_state_stream(self):
        """
        Instruct server to connect to client's state stream socket
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_enable_state_stream(builder, self.stream_addr)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())
        self._consume_ack(resp_bytes)

    def query_runtime_state(self) -> RuntimeState:
        """
        Query server for runtime state

        Returns:
            Server's runtime state
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_query_runtime_info(builder, pdRuntimeInfoType.pdRuntimeInfoType.RuntimeInfo_IgState)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdReturnRuntimeInfo:
            return_msg = pdReturnRuntimeInfo.pdReturnRuntimeInfo()
            return_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            info_type, info = return_msg.InfoType(), return_msg.Info()
            if info_type == pdRuntimeInfo.pdRuntimeInfo.pdIgState:
                ig_state = pdIgState.pdIgState()
                ig_state.Init(info.Bytes, info.Pos)
                lut = {
                    pdIgStateType.pdIgStateType.IgState_Disconnected: RuntimeState.Disconnected,
                    pdIgStateType.pdIgStateType.IgState_Connected: RuntimeState.Connected,
                    pdIgStateType.pdIgStateType.IgState_Backing: RuntimeState.Backing,
                    pdIgStateType.pdIgStateType.IgState_Loading: RuntimeState.Loading,
                    pdIgStateType.pdIgStateType.IgState_Loaded: RuntimeState.Loaded,
                    pdIgStateType.pdIgStateType.IgState_Capturing: RuntimeState.Capturing,
                    pdIgStateType.pdIgStateType.IgState_Finishing: RuntimeState.Finishing,
                }
                return lut[ig_state.IgState()]
            else:
                raise PdError("Invalid response received: unexpected runtime info type")
        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    def _query_system_info(self) -> SystemInfo:
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_query_system_info(builder)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdReturnSystemInfo:
            return_msg = pdReturnSystemInfo.pdReturnSystemInfo()
            return_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            return SystemInfo(
                version=Version(
                    major=int(return_msg.VersionMajor()),
                    minor=int(return_msg.VersionMinor()),
                    patch=int(return_msg.VersionPatch()),
                    build=return_msg.VersionBuild().decode("utf8", "replace"),
                )
            )
        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    @staticmethod
    def _build_pd_location(builder, location_name, time_of_day):
        name = builder.CreateString(location_name)
        tod = builder.CreateString(time_of_day)
        pdLoadLocation.pdLoadLocationStart(builder)
        pdLoadLocation.pdLoadLocationAddLocationName(builder, name)
        pdLoadLocation.pdLoadLocationAddTimeOfDay(builder, tod)
        load_msg = pdLoadLocation.pdLoadLocationEnd(builder)
        return IgSession._build_pd_message(builder, load_msg, pdMessageType.pdLoadLocation)

    @staticmethod
    def _build_pd_update_state(builder, state_bytes, step_mode):
        pdUpdateState.pdUpdateStateStartSimStateVector(builder, len(state_bytes))
        builder.head = builder.head - len(state_bytes)
        builder.Bytes[builder.head : (builder.head + len(state_bytes))] = state_bytes
        state_vec = builder.EndVector(len(state_bytes))
        pdUpdateState.pdUpdateStateStart(builder)
        pdUpdateState.pdUpdateStateAddSimState(builder, state_vec)
        pdUpdateState.pdUpdateStateAddStepMode(builder, step_mode)
        update_msg = pdUpdateState.pdUpdateStateEnd(builder)
        return IgSession._build_pd_message(builder, update_msg, pdMessageType.pdUpdateState)

    @staticmethod
    def _build_pd_query_sensor_data(builder, agent_id, sensor_name, buffer):
        sensor_str = builder.CreateString(sensor_name)
        pdQuerySensorData.pdQuerySensorDataStart(builder)
        pdQuerySensorData.pdQuerySensorDataAddAgentId(builder, agent_id)
        pdQuerySensorData.pdQuerySensorDataAddSensorName(builder, sensor_str)
        pdQuerySensorData.pdQuerySensorDataAddBufferType(builder, buffer)
        query_msg = pdQuerySensorData.pdQuerySensorDataEnd(builder)
        return IgSession._build_pd_message(builder, query_msg, pdMessageType.pdQuerySensorData)

    @staticmethod
    def _build_pd_set_global_params(builder, use_zmq, performance_type=pdPerformanceFeature.PerformanceMode):
        pdSetGlobalParams.pdSetGlobalParamsStart(builder)
        pdSetGlobalParams.pdSetGlobalParamsAddUseZmqStream(builder, use_zmq)
        pdSetGlobalParams.pdSetGlobalParamsAddPerformanceFeature(builder, int(performance_type))
        params_msg = pdSetGlobalParams.pdSetGlobalParamsEnd(builder)
        return IgSession._build_pd_message(builder, params_msg, pdMessageType.pdSetGlobalParams)

    @staticmethod
    def _build_pd_set_capture_parameters(builder, agent_id, sensor_name, frame_rate, bit_rate):
        sensor_str = builder.CreateString(sensor_name)
        pdSetCaptureParameters.pdSetCaptureParametersStart(builder)
        pdSetCaptureParameters.pdSetCaptureParametersAddAgentId(builder, agent_id)
        pdSetCaptureParameters.pdSetCaptureParametersAddSensorName(builder, sensor_str)
        pdSetCaptureParameters.pdSetCaptureParametersAddFrameRate(builder, frame_rate)
        pdSetCaptureParameters.pdSetCaptureParametersAddBitRate(builder, bit_rate)
        params_msg = pdSetCaptureParameters.pdSetCaptureParametersEnd(builder)
        return IgSession._build_pd_message(builder, params_msg, pdMessageType.pdSetCaptureParameters)

    @staticmethod
    def _build_pd_enable_state_stream(builder, _address):
        address = builder.CreateString(_address)
        pdEnableStateStream.pdEnableStateStreamStart(builder)
        pdEnableStateStream.pdEnableStateStreamAddAddress(builder, address)
        state_msg = pdEnableStateStream.pdEnableStateStreamEnd(builder)
        return IgSession._build_pd_message(builder, state_msg, pdMessageType.pdEnableStateStream)

    @staticmethod
    def _build_pd_query_system_info(builder):
        pdQuerySystemInfo.pdQuerySystemInfoStart(builder)
        system_info_msg = pdQuerySystemInfo.pdQuerySystemInfoEnd(builder)
        return IgSession._build_pd_message(builder, system_info_msg, pdMessageType.pdQuerySystemInfo)

    @staticmethod
    def _build_pd_query_runtime_info(builder, info_type: pdRuntimeInfoType):
        pdQueryRuntimeInfo.pdQueryRuntimeInfoStart(builder)
        pdQueryRuntimeInfo.pdQueryRuntimeInfoAddQueryInfo(builder, info_type)
        runtime_info_msg = pdQueryRuntimeInfo.pdQueryRuntimeInfoEnd(builder)
        return IgSession._build_pd_message(builder, runtime_info_msg, pdMessageType.pdQueryRuntimeInfo)


class StepIgSession(IgSession):
    """
    Enables communication with a Step server

    This class provides a simple interface for communication with Step servers.
    Each :class:`StepIgSession` object holds a persistent connection to a single Step server.
    It provides methods for managing the connection with the server, managing messaging
    with the API and updating :class:`~pd.state.State` information.
    This class implements Python context manager semantics and is meant to be used with a
    `with <https://docs.python.org/3/reference/compound_stmts.html#with>`_ statement as follows::

        with StepIgSession(...) as session:
            ...
    """

    def __init__(self, request_addr: str, client_cert_file: Optional[str] = None):
        """
        Args:
            request_addr: Address of the Step server including port in the form tcp://<hostname>:<port> or
                          ssl://<hostname>:<port>
            client_cert_file: Path to credentials file for SSL/TLS protocol
        """
        super().__init__(request_addr=request_addr, client_cert_file=client_cert_file)

    def __enter__(self):
        super().__enter__()
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def update_state(self, state: State):
        """
        Send a state update to the Step server

        Args:
            state: State to send to the server
        """
        self._update_state(state=state, step_mode=True)


class StreamIgSession(IgSession):
    """
    Enables communication with a Stream server

    This class provides a simple interface for communication with Stream servers.
    Each :class:`StreamIgSession` object holds a persistent connection to a single Stream server.
    It provides methods for managing the connection with the server, managing messaging
    with the API and updating :class:`~pd.state.State` information.
    This class implements Python context manager semantics and is meant to be used with a
    `with <https://docs.python.org/3/reference/compound_stmts.html#with>`_ statement as follows::

        with StreamIgSession(...) as session:
            ...
    """

    def __init__(self, request_addr: str, state_addr: str, use_zmq_stream: bool = True):
        """
        Args:
            request_addr: Address for request socket including port in the form tcp://<ip>:<port>.
            state_addr: Address for state socket including port in the form tcp://<ip>:<port>.
            use_zmq_stream: Whether to use zmq stream of webrtc stream
        """
        super().__init__(request_addr=request_addr, state_addr=state_addr)
        self.use_zmq_stream = use_zmq_stream

    def __enter__(self):
        super().__enter__()
        self._set_global_params(use_zmq=self.use_zmq_stream, performance_type=1)
        self._enable_state_stream()
        return self

    def __exit__(self, *args):
        return super().__exit__(*args)

    def update_state(self, state: State):
        """
        Send a state update to the Stream server

        Args:
            state: State to send to the server
        """
        self._update_state(state=state, step_mode=False)

    def set_capture_parameters(self, agent_id: int, sensor_name: str, frame_rate: int, bit_rate: int):
        """
        Set parameters for the video encoder on a per-sensor basis.

        Args:
            agent_id: Agent id of the sensor agent
            sensor_name: Name of the sensor
            frame_rate: Frame rate in Hz
            bit_rate: Bit rate in kbps
        """
        self._set_capture_parameters(agent_id, sensor_name, frame_rate, bit_rate)


class SimSession(PdMessageMixin):
    """
    Base class for communication with Step and Stream servers
    """

    def __init__(self, request_addr: str, client_cert_file: Optional[str] = None):
        """
        Args:
            request_addr: Address for request socket.
            client_cert_file: Path to credentials file for SSL/TLS protocol
        """
        if not request_addr:
            raise PdError("request_addr is required.")
        addr_re = re.compile(_SERVER_URL_REGEX)
        request_addr_match = addr_re.match(request_addr)
        if not request_addr_match:
            raise pd.core.errors.PdError(
                f"Invalid request address provided: {request_addr}. "
                "Must be of the form tcp://hostname:port or ssl://hostname:port"
            )
        if request_addr_match.group("protocol") == "ssl" and not client_cert_file:
            raise pd.core.errors.PdError("TLS certificate path missing: required when using ssl protocol")

        if request_addr_match.group("protocol") == "ssl":
            hostname = request_addr_match.group("hostname")
            port = int(request_addr_match.group("port"))
            self.transport = TlsProxyForZmqTransport(hostname, port, client_cert_file)
        else:
            self.transport = ZmqTransport(request_addr)

    def __enter__(self):
        self.transport.__enter__()
        return self

    def __exit__(self, *args):
        return self.transport.__exit__(*args)

    def load_scenario_generation(self, scenario_gen: str, location_index: int = 0) -> Tuple[str, int]:
        """
        Load a new Scenario Generation Config

        Args:
            scenario_gen: String representation of Scenario Generation Config JSON
            location_index: A single location at this index is selected from the Scenario Generation Config

        Return:
            Location and ego id
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_scenario_generation_configuration(builder, scenario_gen, location_index)
        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdReturnScenarioData:
            return_scenario_msg = pdReturnScenarioData.pdReturnScenarioData()
            return_scenario_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            location = return_scenario_msg.LocationName().decode()
            ego_id = return_scenario_msg.EgoId()
            return location, ego_id
        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    def query_state_data(self) -> State:
        """
        Query Sim for state data

        Returns:
            State data returned by Sim
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_query_state_data(builder)

        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdReturnStateData:
            return_state_msg = pdReturnStateData.pdReturnStateData()
            return_state_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            state_data = return_state_msg.StateDataAsNumpy().tobytes()

            return bytes_to_state(state_data)
        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    def raycast(self, requests: List[Raycast]) -> List[List[RaycastHit]]:
        """
        Cast a number of rays in the world and return their points of collisions against surfaces
        in the world.

        This function takes in a list of raycast requests. For each raycast request, it will return
        a list of hits.
        The list of hits (the inner list) will be in the order of increasing distance from the origin point
        for the given request.
        The list of responses (the outer list) will have a one-to-one correspondence with the list of requests.

        Args:
            requests: Any number of raycast requests

        Returns:
            Same number of responses as the number of requests.
            Each response is a list of hits.
        """
        builder = flatbuffers.Builder(1024)
        msg = self._build_pd_raycast(builder, requests)

        builder.Finish(msg)
        resp_bytes = self.transport.send_request_msg(builder.Output())

        ack_bytes = bytearray()
        ack_bytes.extend(resp_bytes)
        ack_msg = pdMessage.pdMessage.GetRootAspdMessage(ack_bytes, 0)
        msg_type = ack_msg.MessageType()

        if msg_type == pdMessageType.pdRaycastHits:
            return_msg = pdRaycastHits.pdRaycastHits()
            return_msg.Init(ack_msg.Message().Bytes, ack_msg.Message().Pos)
            hits_for_all_requests = []
            for i in range(return_msg.HitsLength()):
                hits_for_request = []
                hits_for_request_fb = return_msg.Hits(i)
                for j in range(hits_for_request_fb.LocationsLength()):
                    location_fb = hits_for_request_fb.Locations(j)
                    normal_fb = hits_for_request_fb.Normals(j)
                    flag = hits_for_request_fb.Flags(j)
                    hits_for_request.append(RaycastHit(
                        position=(location_fb.X(), location_fb.Y(), location_fb.Z()),
                        normal=(normal_fb.X(), normal_fb.Y(), normal_fb.Z()),
                        surface_flag=flag
                    ))
                hits_for_all_requests.append(hits_for_request)
            return hits_for_all_requests
        elif msg_type == pdMessageType.pdAck:
            self._raise_error_for_ack(ack_msg)
        else:
            self._raise_error_for_unknown_message()

    @staticmethod
    def _build_pd_scenario_generation_configuration(builder, scenario_gen_str: str, location_index: int):
        scenario_gen_fb_str = builder.CreateString(scenario_gen_str)
        pdSubmitScenarioGenConfig.pdSubmitScenarioGenConfigStart(builder)
        pdSubmitScenarioGenConfig.pdSubmitScenarioGenConfigAddBuildSimState(builder, scenario_gen_fb_str)
        pdSubmitScenarioGenConfig.pdSubmitScenarioGenConfigAddLocationIndex(builder, location_index)
        scenario_gen_msg = pdSubmitScenarioGenConfig.pdSubmitScenarioGenConfigEnd(builder)
        return SimSession._build_pd_message(builder, scenario_gen_msg, pdMessageType.pdSubmitScenarioGenConfig)

    @staticmethod
    def _build_pd_query_state_data(builder):
        pdQueryStateData.pdQueryStateDataStart(builder)
        query_msg = pdQueryStateData.pdQueryStateDataEnd(builder)
        return SimSession._build_pd_message(builder, query_msg, pdMessageType.pdQueryStateData)

    @staticmethod
    def _build_pd_raycast(builder, requests: List[Raycast]):
        pdRaycastQuery.pdRaycastQueryStartStartVector(builder, len(requests))
        for request in reversed(requests):
            pdFloat3.CreatepdFloat3(builder, *request.origin)
        start_vector_fb = builder.EndVector(len(requests))
        pdRaycastQuery.pdRaycastQueryStartDirectionVector(builder, len(requests))
        for request in reversed(requests):
            pdFloat3.CreatepdFloat3(builder, *request.direction)
        direction_vector_fb = builder.EndVector(len(requests))
        pdRaycastQuery.pdRaycastQueryStartDistanceVector(builder, len(requests))
        for request in reversed(requests):
            builder.PrependFloat32(request.max_distance)
        distance_vector_fb = builder.EndVector(len(requests))

        pdRaycastQuery.pdRaycastQueryStart(builder)
        pdRaycastQuery.pdRaycastQueryAddStart(builder, start_vector_fb)
        pdRaycastQuery.pdRaycastQueryAddDirection(builder, direction_vector_fb)
        pdRaycastQuery.pdRaycastQueryAddDistance(builder, distance_vector_fb)
        raycast_msg = pdRaycastQuery.pdRaycastQueryEnd(builder)
        return SimSession._build_pd_message(builder, raycast_msg, pdMessageType.pdRaycastQuery)



def create_step_ig_session(*args, **kwargs) -> StepIgSession:
    """
    Create and start a Step IG session
    This function makes it easier to work with a StepIgSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session = StepIgSession(*args, **kwargs)
    session.__enter__()
    return session


def stop_step_ig_session(session: StepIgSession):
    """
    Stop Step IG session
    This function makes it easier to work with a StepIgSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session.__exit__()


def create_stream_ig_session(*args, **kwargs) -> StreamIgSession:
    """
    Create and start a Stream IG session
    This function makes it easier to work with a StreamIgSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session = StreamIgSession(*args, **kwargs)
    session.__enter__()
    return session


def stop_stream_ig_session(session: StreamIgSession):
    """
    Stop Stream IG session
    This function makes it easier to work with a StreamIgSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session.__exit__()


def create_sim_session(*args, **kwargs) -> SimSession:
    """
    Create and start a Sim session
    This function makes it easier to work with a SimSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session = SimSession(*args, **kwargs)
    session.__enter__()
    return session


def stop_sim_session(session: SimSession):
    """
    Stop Sim session
    This function makes it easier to work with a SimSession in interactive shell by eliminating the
    need for a `with` block.
    """
    session.__exit__()


StepSession = StepIgSession
"""
Alias for :class:`StepIgSession` for backwards compatibility.
Use :class:`StepIgSession` instead.
"""

StreamSession = StreamIgSession
"""
Alias for :class:`StreamIgSession` for backwards compatibility.
Use :class:`StreamIgSession` instead.
"""

create_step_session = create_step_ig_session
"""
Alias for :func:`create_step_ig_session` for backwards compatibility.
Use :func:`create_step_ig_session` instead.
"""

stop_step_session = stop_step_ig_session
"""
Alias for :func:`stop_step_ig_session` for backwards compatibility.
Use :func:`stop_step_ig_session` instead.
"""

create_stream_session = create_stream_ig_session
"""
Alias for :func:`create_stream_ig_session` for backwards compatibility.
Use :func:`create_stream_ig_session` instead.
"""

stop_stream_session = stop_stream_ig_session
"""
Alias for :func:`stop_stream_ig_session` for backwards compatibility.
Use :func:`stop_stream_ig_session` instead.
"""
