import threading
import time
from queue import Queue
from typing import List
import logging

import flatbuffers
import pytest
import zmq
import numpy as np

import pd.state
from pd.internal.fb.generated.python import pdMessage, pdReturnSystemInfo, pdLoadLocation, pdReturnRuntimeInfo, \
    pdIgState, pdUpdateState, pdReturnSensorData, pdQuerySensorData, pdReturnScenarioData, pdSubmitScenarioGenConfig, \
    pdReturnStateData, pdRaycastHit, pdFloat3, pdRaycastHits, pdRaycastQuery, pdConfigLabelEngine, \
    pdReturnLabelEngineAnnotationStatus, pdQueryLabelEngineAnnotationStatus, pdReturnLabelEngineAnnotationData, \
    pdLabelData, pdRequestLabelEngineAnnotationData, pdUpdateLabelEngineAnnotationData
from pd.internal.fb.generated.python.pdBufferType import pdBufferType
from pd.internal.fb.generated.python.pdIgStateType import pdIgStateType
from pd.internal.fb.generated.python.pdMessageType import pdMessageType
from pd.internal.fb.generated.python.pdResponseCode import pdResponseCode
from pd.internal.fb.generated.python.pdRuntimeInfo import pdRuntimeInfo
from pd.label_engine import DataType
from pd.session.session import BaseSession, StepIgSession, PdMessageMixin, RuntimeState, SimSession, LabelEngineSession
from pd.session.transport import get_zmq_context
from pd.core.errors import PdError
from pd.sim import Raycast
from pd.state import bytes_to_state, SensorBuffer, state_to_bytes

logger = logging.getLogger(__name__)


class TestBaseSession:
    def test_base_session_init_tcp(self):
        BaseSession(
            request_addr='tcp://hostname:1234'
        )

    def test_base_session_init_ssl(self):
        BaseSession(
            request_addr='ssl://hostname:1234', client_cert_file='/path/to/file'
        )

    def test_base_session_init_fails_on_unknown_protocol(self):
        with pytest.raises(PdError, match=r'.*Invalid request address.*'):
            BaseSession(
                request_addr='udp://hostname:1234'
            )

    def test_base_session_init_fails_on_missing_port(self):
        with pytest.raises(PdError, match=r'.*Invalid request address.*'):
            BaseSession(
                request_addr='tcp://hostname'
            )

    def test_base_session_init_fails_on_missing_ssl_cert(self):
        with pytest.raises(PdError, match=r'.*certificate path missing.*'):
            BaseSession(
                request_addr='ssl://hostname:1234'
            )

    def test_base_session_init_fails_on_state_not_tcp(self):
        with pytest.raises(PdError, match=r'.*Invalid state address.*'):
            BaseSession(
                request_addr='ssl://hostname:1234', state_addr='ssl://hostname:1234',
                client_cert_file='/path/to/file'
            )

class PdMessageZmqServerStub:
    """
    A zmq server that sinks all pd messages it receives
    """
    def __init__(self):
        self._thread = None
        self._exit = False
        self._address_queue = Queue()
        self.responses = []  # response messages to be returned by server
        self.requests: List[pdMessage.pdMessage] = []  # request messages received by server

    def __enter__(self):
        self._thread = threading.Thread(
            target=self._worker
        )
        self._thread.start()

    def __exit__(self, *args):
        if self._thread:
            self._exit = True
            self._thread.join()
            self._thread = None

    @property
    def address(self) -> str:
        if not self._thread:
            raise ValueError("Server stub context has not started. Address is only available after context has started.")
        return self._address_queue.get(timeout=1)

    def _worker(self):
        logger.info(f"{id(self)} Starting worker")
        context = get_zmq_context()
        self._socket = context.socket(zmq.REP)
        self._socket.bind("tcp://127.0.0.1:0")
        endpoint = self._socket.getsockopt(zmq.LAST_ENDPOINT).decode()
        logger.info(f"{id(self)} Server endpoint {endpoint}")
        self._address_queue.put(endpoint)
        timeout_time = time.time() + 10.0  # timeout (in secs) for if test crashed
        while True:
            if self._exit:
                logger.info(f"{id(self)} PdMessageZmqServerStub received exit request, exiting")
                break
            if time.time() > timeout_time:
                logger.info(f"{id(self)} PdMessageZmqServerStub worker timed out")
                break
            logger.info(f"{id(self)} Waiting for msg")
            try:
                message_bytes = self._socket.recv(flags=zmq.NOBLOCK)
            except zmq.Again:
                time.sleep(0.1)
                continue
            pd_msg = pdMessage.pdMessage.GetRootAspdMessage(message_bytes, 0)
            logger.info(f"{id(self)} Received msg {pd_msg.MessageType()}")
            self.requests.append(pd_msg)

            logger.info(f"{id(self)} Sending msg")
            try:
                message = self.responses.pop(0)
            except IndexError:
                logger.error(f"{id(self)} Server has no messages to respond with")
                raise
            self._socket.send(message, flags=zmq.NOBLOCK)
        self._socket.disconnect(endpoint)
        logger.info(f"{id(self)} Exiting worker exit={self._exit} # responses remaining={len(self.responses)}")


@pytest.fixture
def builder():
    return flatbuffers.Builder(65536)


class TestStepIgSession:
    @pytest.fixture
    def server_and_session(self, builder):
        """
        Returns a tuple containing server stub and ig session
        """
        # Add the system info msg by default to all responses list
        build_string = builder.CreateString("test")
        pdReturnSystemInfo.pdReturnSystemInfoStart(builder)
        pdReturnSystemInfo.pdReturnSystemInfoAddVersionMajor(builder, 1)
        pdReturnSystemInfo.pdReturnSystemInfoAddVersionMinor(builder, 2)
        pdReturnSystemInfo.pdReturnSystemInfoAddVersionPatch(builder, 3)
        pdReturnSystemInfo.pdReturnSystemInfoAddVersionBuild(builder, build_string)
        msg_bytes = pdReturnSystemInfo.pdReturnSystemInfoEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnSystemInfo)
        builder.Finish(msg)
        request_bytes = builder.Output()

        server = PdMessageZmqServerStub()
        server.responses.append(request_bytes)
        with server:
            session = StepIgSession(request_addr=server.address)
            session.transport.timeout_recv_ms = 1000  # fail quickly
            with session:
                yield server, session

        server.__exit__()  # force exit server in case test crashed
        assert len(server.responses) == 0, "not all responses were consumed"

    def test_system_info(self, server_and_session):
        server, session = server_and_session

        system_info = session.system_info
        assert system_info
        assert system_info.version.major == 1
        assert system_info.version.minor == 2
        assert system_info.version.patch == 3
        assert system_info.version.build == "test"

    def test_system_info_raises_error_on_error_response(self, builder):
        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdQuerySystemInfo, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()

        server = PdMessageZmqServerStub()
        server.responses.append(request_bytes)
        with server:
            session = StepIgSession(request_addr=server.address)
            session.transport.timeout_recv_ms = 1000  # fail quickly
            with pytest.raises(PdError, match=r'.*error ack.*'):
                with session:
                    # Query system info is called automatically by session
                    # We don't need to do anything here
                    pass

    def test_query_runtime_state(self, builder, server_and_session):
        server, session = server_and_session

        pdIgState.pdIgStateStart(builder)
        pdIgState.pdIgStateAddIgState(builder, pdIgStateType.IgState_Loaded)
        ig_state_fb = pdIgState.pdIgStateEnd(builder)
        pdReturnRuntimeInfo.pdReturnRuntimeInfoStart(builder)
        pdReturnRuntimeInfo.pdReturnRuntimeInfoAddInfo(builder, ig_state_fb)
        pdReturnRuntimeInfo.pdReturnRuntimeInfoAddInfoType(builder, pdRuntimeInfo.pdIgState)
        msg_bytes = pdReturnRuntimeInfo.pdReturnRuntimeInfoEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnRuntimeInfo)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        runtime_state = session.query_runtime_state()
        assert runtime_state == RuntimeState.Loaded

    def test_query_runtime_state_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdQueryRuntimeInfo, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.query_runtime_state()

    def test_load_location(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdLoadLocation, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        session.load_location("test_location", "test_lighting")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdLoadLocation
        request_msg = pdLoadLocation.pdLoadLocation()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.LocationName().decode() == "test_location"
        assert request_msg.TimeOfDay().decode() == "test_lighting"

    def test_load_location_with_scene_name(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdLoadLocation, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        session.load_location("test_location", "test_lighting", "scene_abc")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdLoadLocation
        request_msg = pdLoadLocation.pdLoadLocation()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.LocationName().decode() == "test_location"
        assert request_msg.TimeOfDay().decode() == "test_lighting"
        assert request_msg.SceneName().decode() == "scene_abc"

    def test_load_location_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdLoadLocation, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.load_location("test_location", "test_lighting")

    def test_update_state(self, builder, server_and_session, helpers):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateState, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        state = pd.state.State(
            simulation_time_sec=0.123,
            world_info=pd.state.WorldInfo(),
            agents=[]
        )
        session.update_state(state)
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateState
        request_msg = pdUpdateState.pdUpdateState()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        sim_state_bytes = request_msg.SimStateAsNumpy().tobytes()
        sim_state = bytes_to_state(sim_state_bytes)
        assert helpers.fisclose(sim_state.simulation_time_sec, 0.123)

    def test_update_state_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateState, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            state = pd.state.State(
                simulation_time_sec=0.123,
                world_info=pd.state.WorldInfo(),
                agents=[]
            )
            session.update_state(state)

    def test_query_sensor_data(self, builder, server_and_session):
        server, session = server_and_session

        image_bytes = bytes([42, 60, 170, 89, 25, 156])
        pdReturnSensorData.pdReturnSensorDataStartDataVector(builder, len(image_bytes))
        builder.head = builder.head - len(image_bytes)
        builder.Bytes[builder.head : (builder.head + len(image_bytes))] = image_bytes
        image_bytes_fb = builder.EndVector(len(image_bytes))

        pdReturnSensorData.pdReturnSensorDataStart(builder)
        pdReturnSensorData.pdReturnSensorDataAddWidth(builder, 3)
        pdReturnSensorData.pdReturnSensorDataAddHeight(builder, 2)
        pdReturnSensorData.pdReturnSensorDataAddChannel(builder, 1)
        pdReturnSensorData.pdReturnSensorDataAddData(builder, image_bytes_fb)
        msg_bytes = pdReturnSensorData.pdReturnSensorDataEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnSensorData)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        sensor_data = session.query_sensor_data(agent_id=123, sensor_name="test", buffer=SensorBuffer.DEPTH)

        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQuerySensorData
        request_msg = pdQuerySensorData.pdQuerySensorData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.SensorName().decode() == "test"
        assert request_msg.BufferType() == pdBufferType.Buffer_Depth
        assert request_msg.AgentId() == 123

        assert sensor_data
        assert sensor_data.width == 3
        assert sensor_data.height == 2
        assert sensor_data.data.shape == (2, 3, 1)
        data = sensor_data.data.squeeze()
        assert np.array_equal(data, np.array([[42, 60, 170], [89, 25, 156]]))

    def test_query_sensor_data_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdQuerySensorData, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.query_sensor_data(agent_id=123, sensor_name="test", buffer=SensorBuffer.DEPTH)


class TestSimSession:
    @pytest.fixture
    def server_and_session(self, builder):
        """
        Returns a tuple containing server stub and sim session
        """
        server = PdMessageZmqServerStub()
        with server:
            session = SimSession(request_addr=server.address)
            session.transport.timeout_recv_ms = 1000  # fail quickly
            with session:
                yield server, session

        server.__exit__()  # force exit server in case test crashed
        assert len(server.responses) == 0, "not all responses were consumed"

    def test_load_scenario_generation(self, builder, server_and_session):
        server, session = server_and_session

        location_name_fb = builder.CreateString("test_location")

        pdReturnScenarioData.pdReturnScenarioDataStart(builder)
        pdReturnScenarioData.pdReturnScenarioDataAddEgoId(builder, 1234)
        pdReturnScenarioData.pdReturnScenarioDataAddLocationName(builder, location_name_fb)
        msg_bytes = pdReturnScenarioData.pdReturnScenarioDataEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnScenarioData)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        location, ego_id = session.load_scenario_generation(scenario_gen="test scenario string", location_index=42)
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdSubmitScenarioGenConfig
        request_msg = pdSubmitScenarioGenConfig.pdSubmitScenarioGenConfig()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.LocationIndex() == 42
        assert request_msg.BuildSimState().decode() == "test scenario string"

        assert location == "test_location"
        assert ego_id == 1234

    def test_load_scenario_generation_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdSubmitScenarioGenConfig, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.load_scenario_generation(scenario_gen="test scenario string", location_index=42)

    def test_query_state_data(self, builder, server_and_session, helpers):
        server, session = server_and_session

        state = pd.state.State(
            simulation_time_sec=0.456,
            world_info=pd.state.WorldInfo(),
            agents=[]
        )
        state_bytes = state_to_bytes(state)
        pdReturnStateData.pdReturnStateDataStartStateDataVector(builder, len(state_bytes))
        builder.head = builder.head - len(state_bytes)
        builder.Bytes[builder.head : (builder.head + len(state_bytes))] = state_bytes
        state_bytes_fb = builder.EndVector(len(state_bytes))

        pdReturnStateData.pdReturnStateDataStart(builder)
        pdReturnStateData.pdReturnStateDataAddStateData(builder, state_bytes_fb)
        msg_bytes = pdReturnStateData.pdReturnStateDataEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnStateData)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        response_state = session.query_state_data()
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryStateData

        assert helpers.fisclose(response_state.simulation_time_sec, 0.456)

    def test_query_state_data_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdQueryStateData, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.query_state_data()

    def test_raycast(self, builder, server_and_session, helpers):
        server, session = server_and_session

        locations = [(0.11, 0.12, 0.13), (0.21, 0.22, 0.23)]
        normals = [(0.31, 0.32, 0.33), (0.41, 0.42, 0.43)]
        flags = [7, 8]
        pdRaycastHit.pdRaycastHitStartLocationsVector(builder, len(locations))
        for location in reversed(locations):
            pdFloat3.CreatepdFloat3(builder, *location)
        locations_vector_fb = builder.EndVector(len(locations))
        pdRaycastHit.pdRaycastHitStartNormalsVector(builder, len(normals))
        for normal in reversed(normals):
            pdFloat3.CreatepdFloat3(builder, *normal)
        normals_vector_fb = builder.EndVector(len(normals))
        pdRaycastHit.pdRaycastHitStartFlagsVector(builder, len(flags))
        for flag in reversed(flags):
            builder.PrependUint64(flag)
        flag_vector_fb = builder.EndVector(len(flags))
        pdRaycastHit.pdRaycastHitStart(builder)
        pdRaycastHit.pdRaycastHitAddLocations(builder, locations_vector_fb)
        pdRaycastHit.pdRaycastHitAddNormals(builder, normals_vector_fb)
        pdRaycastHit.pdRaycastHitAddFlags(builder, flag_vector_fb)
        raycast_hit_fb = pdRaycastHit.pdRaycastHitEnd(builder)

        pdRaycastHits.pdRaycastHitsStartHitsVector(builder, 1)
        builder.PrependUOffsetTRelative(raycast_hit_fb)
        hits_vec_fb = builder.EndVector(1)
        pdRaycastHits.pdRaycastHitsStart(builder)
        pdRaycastHits.pdRaycastHitsAddHits(builder, hits_vec_fb)
        msg_bytes = pdRaycastHits.pdRaycastHitsEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdRaycastHits)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        requests = [
            Raycast(origin=(0.1, 0.2, 0.3), direction=(0.4, 0.5, 0.6), max_distance=0.78),
            Raycast(origin=(1.1, 1.2, 1.3), direction=(1.4, 1.5, 1.6), max_distance=1.78),
        ]
        raycast_hits = session.raycast(requests)
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRaycastQuery
        request_msg = pdRaycastQuery.pdRaycastQuery()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.StartLength() == 2
        starts = [request_msg.Start(0), request_msg.Start(1)]
        assert np.allclose((starts[0].X(), starts[0].Y(), starts[0].Z()), (0.1, 0.2, 0.3))
        assert np.allclose((starts[1].X(), starts[1].Y(), starts[1].Z()), (1.1, 1.2, 1.3))
        assert request_msg.DirectionLength() == 2
        directions = [request_msg.Direction(0), request_msg.Direction(1)]
        assert np.allclose((directions[0].X(), directions[0].Y(), directions[0].Z()), (0.4, 0.5, 0.6))
        assert np.allclose((directions[1].X(), directions[1].Y(), directions[1].Z()), (1.4, 1.5, 1.6))
        assert request_msg.DistanceLength() == 2
        assert helpers.fisclose(request_msg.Distance(0), 0.78)
        assert helpers.fisclose(request_msg.Distance(1), 1.78)

        assert len(raycast_hits) == 1
        assert len(raycast_hits[0]) == 2
        assert np.allclose(raycast_hits[0][0].position, (0.11, 0.12, 0.13))
        assert np.allclose(raycast_hits[0][1].position, (0.21, 0.22, 0.23))
        assert np.allclose(raycast_hits[0][0].normal, (0.31, 0.32, 0.33))
        assert np.allclose(raycast_hits[0][1].normal, (0.41, 0.42, 0.43))
        assert raycast_hits[0][0].surface_flag == 7
        assert raycast_hits[0][1].surface_flag == 8

    def test_raycast_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdRaycastQuery, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.raycast([])


class TestLabelEngineSession:
    @pytest.fixture
    def server_and_session(self, builder):
        """
        Returns a tuple containing server stub and sim session
        """
        server = PdMessageZmqServerStub()
        logger.info(f"server id = {id(server)}")
        with server:
            session = LabelEngineSession(request_addr=server.address)
            session.transport.timeout_recv_ms = 1000  # fail quickly
            with session:
                yield server, session

        server.__exit__()  # force exit server in case test crashed
        assert len(server.responses) == 0, "not all responses were consumed"

    def test_configure(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdConfigLabelEngine, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        session.configure(scene_name="scene abc", config="test pipeline json")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdConfigLabelEngine
        request_msg = pdConfigLabelEngine.pdConfigLabelEngine()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Config().decode() == "test pipeline json"
        assert request_msg.SceneName().decode() == "scene abc"

    def test_configure_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdConfigLabelEngine, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.configure(scene_name="scene abc", config="test pipeline json")

    @staticmethod
    def _add_response_for_query_annotation_status(builder, server, resp_status: bool):
        pdReturnLabelEngineAnnotationStatus.pdReturnLabelEngineAnnotationStatusStart(builder)
        pdReturnLabelEngineAnnotationStatus.pdReturnLabelEngineAnnotationStatusAddStatus(builder, resp_status)
        msg_bytes = pdReturnLabelEngineAnnotationStatus.pdReturnLabelEngineAnnotationStatusEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnLabelEngineAnnotationStatus)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

    def test_query_annotation_status(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_query_annotation_status(builder, server, True)

        status = session.query_annotation_status(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryLabelEngineAnnotationStatus
        request_msg = pdQueryLabelEngineAnnotationStatus.pdQueryLabelEngineAnnotationStatus()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.SensorsLength() == 1
        assert request_msg.Sensors(0).decode() == "testsensor-123"
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.SceneName().decode() == "scene abc"

        assert status is True

    def test_query_annotation_status_no_timestamp(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_query_annotation_status(builder, server, True)

        status = session.query_annotation_status(scene_name="scene abc", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryLabelEngineAnnotationStatus
        request_msg = pdQueryLabelEngineAnnotationStatus.pdQueryLabelEngineAnnotationStatus()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.SensorsLength() == 1
        assert request_msg.Sensors(0).decode() == "testsensor-123"
        assert request_msg.Label().decode() == "data_stream_xyz"

        assert status is True

    def test_query_annotation_status_no_sensor(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_query_annotation_status(builder, server, True)

        status = session.query_annotation_status(scene_name="scene abc", timestamp="000123", label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryLabelEngineAnnotationStatus
        request_msg = pdQueryLabelEngineAnnotationStatus.pdQueryLabelEngineAnnotationStatus()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.SensorsLength() == 0
        assert request_msg.Label().decode() == "data_stream_xyz"

        assert status is True

    def test_query_annotation_status_no_timestamp_or_sensor(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_query_annotation_status(builder, server, True)

        status = session.query_annotation_status(scene_name="scene abc", label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryLabelEngineAnnotationStatus
        request_msg = pdQueryLabelEngineAnnotationStatus.pdQueryLabelEngineAnnotationStatus()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.SensorsLength() == 0
        assert request_msg.Label().decode() == "data_stream_xyz"

        assert status is True

    def test_query_annotation_status_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdQueryLabelEngineAnnotationStatus, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.query_annotation_status(scene_name="scene abc", label="data_stream_xyz")

    def test_query_annotation_status_sensor_name_with_hyphen(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_query_annotation_status(builder, server, True)

        status = session.query_annotation_status(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "test-sensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdQueryLabelEngineAnnotationStatus
        request_msg = pdQueryLabelEngineAnnotationStatus.pdQueryLabelEngineAnnotationStatus()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Sensors(0).decode() == "test-sensor-123"

        assert status is True

    @staticmethod
    def _add_response_for_request_annotation_data(builder, server, timestamp, sensor,data):
        label_data_fbs = []

        label_data_bytes = data.encode()
        sensor_fb = builder.CreateString(sensor) if sensor else None
        timestamp_fb = builder.CreateString(timestamp) if timestamp else None
        pdLabelData.pdLabelDataStartLabelDataVector(builder, len(label_data_bytes))
        builder.head = builder.head - len(label_data_bytes)
        builder.Bytes[builder.head : (builder.head + len(label_data_bytes))] = label_data_bytes
        label_data_bytes_fb = builder.EndVector(len(label_data_bytes))
        pdLabelData.pdLabelDataStart(builder)
        if sensor_fb:
            pdLabelData.pdLabelDataAddSensor(builder, sensor_fb)
        if timestamp_fb:
            pdLabelData.pdLabelDataAddTimestamp(builder, timestamp_fb)
        pdLabelData.pdLabelDataAddLabelData(builder, label_data_bytes_fb)
        label_data_fbs.append(pdLabelData.pdLabelDataEnd(builder))

        pdReturnLabelEngineAnnotationData.pdReturnLabelEngineAnnotationDataStartLabelDataVector(builder, len(label_data_fbs))
        for label_data_fb in reversed(label_data_fbs):
            builder.PrependUOffsetTRelative(label_data_fb)
        label_data_fb_vec = builder.EndVector(len(label_data_fbs))
        pdReturnLabelEngineAnnotationData.pdReturnLabelEngineAnnotationDataStart(builder)
        pdReturnLabelEngineAnnotationData.pdReturnLabelEngineAnnotationDataAddLabelData(builder, label_data_fb_vec)
        msg_bytes = pdReturnLabelEngineAnnotationStatus.pdReturnLabelEngineAnnotationStatusEnd(builder)

        msg = PdMessageMixin._build_pd_message(builder, msg_bytes, pdMessageType.pdReturnLabelEngineAnnotationData)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

    def test_request_annotation_data(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_request_annotation_data(builder, server, "000123", "testsensor-123", "test label data 1")

        label_data = session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRequestLabelEngineAnnotationData
        request_msg = pdRequestLabelEngineAnnotationData.pdRequestLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.SensorsLength() == 1
        assert request_msg.Sensors(0).decode() == "testsensor-123"
        assert request_msg.SceneName().decode() == "scene abc"

        assert label_data.timestamp == "000123"
        assert label_data.label == "data_stream_xyz"
        assert label_data.sensor_id_and_name == (123, "testsensor")
        assert label_data.data.decode() == "test label data 1"

    def test_request_annotation_data_no_sensor(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_request_annotation_data(builder, server, "000123", None, "test label data 1")

        label_data = session.request_annotation_data(scene_name="scene abc", timestamp="000123", label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRequestLabelEngineAnnotationData
        request_msg = pdRequestLabelEngineAnnotationData.pdRequestLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.SensorsLength() == 0

        assert label_data.timestamp == "000123"
        assert label_data.label == "data_stream_xyz"
        assert label_data.sensor_id_and_name is None
        assert label_data.data.decode() == "test label data 1"

    def test_request_annotation_data_no_timestamp(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_request_annotation_data(builder, server, None, "testsensor-123", "test label data 1")

        label_data = session.request_annotation_data(scene_name="scene abc", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRequestLabelEngineAnnotationData
        request_msg = pdRequestLabelEngineAnnotationData.pdRequestLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.SensorsLength() == 1
        assert request_msg.Sensors(0).decode() == "testsensor-123"

        assert label_data.timestamp is None
        assert label_data.label == "data_stream_xyz"
        assert label_data.sensor_id_and_name == (123, "testsensor")
        assert label_data.data.decode() == "test label data 1"

    def test_request_annotation_data_no_sensor_or_timestamp(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_request_annotation_data(builder, server, None, None, "test label data 1")

        label_data = session.request_annotation_data(scene_name="scene abc", label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRequestLabelEngineAnnotationData
        request_msg = pdRequestLabelEngineAnnotationData.pdRequestLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.SensorsLength() == 0
        assert request_msg.Label().decode() == "data_stream_xyz"

        assert label_data.timestamp is None
        assert label_data.label == "data_stream_xyz"
        assert label_data.sensor_id_and_name is None
        assert label_data.data.decode() == "test label data 1"

    def test_request_annotation_data_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdRequestLabelEngineAnnotationData, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            session.request_annotation_data(scene_name="scene abc", timestamp="000123", label="data_stream_xyz")

    def test_request_annotation_data_raises_error_on_mismatch_response(self, builder, server_and_session):
        server, session = server_and_session

        self._add_response_for_request_annotation_data(builder, server, "000123", "anothersensor-123", "test label data 1")
        with pytest.raises(PdError, match=r'.*Expecting sensor*'):
            session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")

        self._add_response_for_request_annotation_data(builder, server, "000123", None, "test label data 1")
        with pytest.raises(PdError, match=r'.*Expecting sensor*'):
            session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")

        self._add_response_for_request_annotation_data(builder, server, "000124", "testsensor-123", "test label data 1")
        with pytest.raises(PdError, match=r'.*Expecting timestamp*'):
            session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")

        self._add_response_for_request_annotation_data(builder, server, None, "anothersensor-123", "test label data 1")
        with pytest.raises(PdError, match=r'.*Expecting timestamp*'):
            session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "testsensor"), label="data_stream_xyz")

    def test_request_annotation_data_sensor_name_with_hyphen(self, builder, server_and_session):
        server, session = server_and_session
        self._add_response_for_request_annotation_data(builder, server, "000123", "test-sensor-123", "test label data 1")

        label_data = session.request_annotation_data(scene_name="scene abc", timestamp="000123", sensor_id_and_name=(123, "test-sensor"), label="data_stream_xyz")
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdRequestLabelEngineAnnotationData
        request_msg = pdRequestLabelEngineAnnotationData.pdRequestLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Sensors(0).decode() == "test-sensor-123"

        assert label_data.sensor_id_and_name == (123, "test-sensor")
        assert label_data.data.decode() == "test label data 1"

    def test_update_annotation_data(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        data_bytes = "test annotation data".encode()
        session.update_annotation_data(
            scene_name="scene abc",
            label="data_stream_xyz",
            timestamp="000123",
            sensor_id_and_name=(123, "testsensor"),
            data_type=DataType.Annotation,
            data=data_bytes
        )
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateLabelEngineAnnotationData
        request_msg = pdUpdateLabelEngineAnnotationData.pdUpdateLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.Sensor().decode() == "testsensor-123"
        assert request_msg.DataType() == DataType.Annotation
        assert request_msg.LabelDataAsNumpy().tobytes().decode() == "test annotation data"
        assert request_msg.SceneName().decode() == "scene abc"

    def test_update_annotation_data_no_sensor(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        data_bytes = "test annotation data".encode()
        session.update_annotation_data(
            scene_name="scene abc",
            label="data_stream_xyz",
            timestamp="000123",
            sensor_id_and_name=None,
            data_type=DataType.Annotation,
            data=data_bytes
        )
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateLabelEngineAnnotationData
        request_msg = pdUpdateLabelEngineAnnotationData.pdUpdateLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Timestamp().decode() == "000123"
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert not request_msg.Sensor()
        assert request_msg.DataType() == DataType.Annotation
        assert request_msg.LabelDataAsNumpy().tobytes().decode() == "test annotation data"

    def test_update_annotation_data_no_timestamp(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        data_bytes = "test annotation data".encode()
        session.update_annotation_data(
            scene_name="scene abc",
            label="data_stream_xyz",
            timestamp=None,
            sensor_id_and_name=(123, "testsensor"),
            data_type=DataType.Annotation,
            data=data_bytes
        )
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateLabelEngineAnnotationData
        request_msg = pdUpdateLabelEngineAnnotationData.pdUpdateLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert request_msg.Sensor().decode() == "testsensor-123"
        assert request_msg.DataType() == DataType.Annotation
        assert request_msg.LabelDataAsNumpy().tobytes().decode() == "test annotation data"

    def test_update_annotation_data_no_sensor_no_timestamp(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        data_bytes = "test annotation data".encode()
        session.update_annotation_data(
            scene_name="scene abc",
            label="data_stream_xyz",
            timestamp=None,
            sensor_id_and_name=None,
            data_type=DataType.Annotation,
            data=data_bytes
        )
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateLabelEngineAnnotationData
        request_msg = pdUpdateLabelEngineAnnotationData.pdUpdateLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert not request_msg.Timestamp()
        assert request_msg.Label().decode() == "data_stream_xyz"
        assert not request_msg.Sensor()
        assert request_msg.DataType() == DataType.Annotation
        assert request_msg.LabelDataAsNumpy().tobytes().decode() == "test annotation data"

    def test_update_annotation_data_raises_error_on_error_response(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "error ack", pdResponseCode.SERVER_ERROR)
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        with pytest.raises(PdError, match=r'.*error ack*'):
            data_bytes = "test annotation data".encode()
            session.update_annotation_data(
                scene_name="scene abc",
                timestamp="000123",
                label="data_stream_xyz",
                sensor_id_and_name=(123, "testsensor"),
                data_type=42,
                data=data_bytes
            )

    def test_update_annotation_data_sensor_name_with_hyphen(self, builder, server_and_session):
        server, session = server_and_session

        msg = PdMessageMixin._build_ack_message(builder, pdMessageType.pdUpdateLabelEngineAnnotationData, "ack")
        builder.Finish(msg)
        request_bytes = builder.Output()
        server.responses.append(request_bytes)

        data_bytes = "test annotation data".encode()
        session.update_annotation_data(
            scene_name="scene abc",
            label="data_stream_xyz",
            timestamp="000123",
            sensor_id_and_name=(123, "test-sensor"),
            data_type=DataType.Annotation,
            data=data_bytes
        )
        request_pd_msg = server.requests[-1]
        assert request_pd_msg.MessageType() == pdMessageType.pdUpdateLabelEngineAnnotationData
        request_msg = pdUpdateLabelEngineAnnotationData.pdUpdateLabelEngineAnnotationData()
        request_msg.Init(request_pd_msg.Message().Bytes, request_pd_msg.Message().Pos)
        assert request_msg.Sensor().decode() == "test-sensor-123"
