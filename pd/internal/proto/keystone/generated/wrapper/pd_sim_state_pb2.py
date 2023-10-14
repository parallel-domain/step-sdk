from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_sim_state_pb2
)
from . import (
    pd_sensor_pb2 as _pd_sensor_pb2,
    pd_scenario_pb2 as _pd_scenario_pb2
)


@register_wrapper(proto_type=pd_sim_state_pb2.BuildSimState)
class BuildSimState(ProtoMessageClass):
    """
    Args:
        name: :attr:`name`
        output_artifact_uid: :attr:`output_artifact_uid`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        locations: :attr:`locations`
        scenario_gen: :attr:`scenario_gen`
        sensor_rig: :attr:`sensor_rig`
    Attributes:
        name: Human readable name for this job
        output_artifact_uid: Output artifact for build results
        code_build_artifact_uid: Set the tag/uid of the code build ECR image to use in the build and finalize steps.
        locations: Location definitions for this scenario batch
        scenario_gen: Scenario batch configuration parameters
        sensor_rig: Sensor rig definition for scenario"""

    _proto_message = pd_sim_state_pb2.BuildSimState

    def __init__(
        self,
        *,
        proto: Optional[pd_sim_state_pb2.BuildSimState] = None,
        name: str = None,
        output_artifact_uid: str = None,
        code_build_artifact_uid: str = None,
        locations: List[_pd_scenario_pb2.ScenarioLocation] = None,
        scenario_gen: _pd_scenario_pb2.ScenarioGenConfig = None,
        sensor_rig: _pd_sensor_pb2.SensorRigConfig = None,
    ):
        if proto is None:
            proto = pd_sim_state_pb2.BuildSimState()
        self.proto = proto
        self._locations = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.locations],
            attr_name="locations",
            list_owner=self,
        )
        self._scenario_gen = get_wrapper(proto_type=proto.scenario_gen.__class__)(proto=proto.scenario_gen)
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        if name is not None:
            self.name = name
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if locations is not None:
            self.locations = locations
        if scenario_gen is not None:
            self.scenario_gen = scenario_gen
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig

    @property
    def name(self) -> str:
        return self.proto.name

    @name.setter
    def name(self, value: str):
        self.proto.name = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def locations(self) -> List[_pd_scenario_pb2.ScenarioLocation]:
        return self._locations

    @locations.setter
    def locations(self, value: List[_pd_scenario_pb2.ScenarioLocation]):
        self._locations.clear()
        for v in value:
            self._locations.append(v)

    @property
    def scenario_gen(self) -> _pd_scenario_pb2.ScenarioGenConfig:
        return self._scenario_gen

    @scenario_gen.setter
    def scenario_gen(self, value: _pd_scenario_pb2.ScenarioGenConfig):
        self.proto.scenario_gen.CopyFrom(value.proto)

        self._scenario_gen = value
        self._scenario_gen._update_proto_references(self.proto.scenario_gen)

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self.proto.sensor_rig.CopyFrom(value.proto)

        self._sensor_rig = value
        self._sensor_rig._update_proto_references(self.proto.sensor_rig)

    def _update_proto_references(self, proto: pd_sim_state_pb2.BuildSimState):
        self.proto = proto
        for i, v in enumerate(self.locations):
            v._update_proto_references(self.proto.locations[i])
        self._scenario_gen._update_proto_references(proto.scenario_gen)
        self._sensor_rig._update_proto_references(proto.sensor_rig)


@register_wrapper(proto_type=pd_sim_state_pb2.SimStateCull)
class SimStateCull(ProtoMessageClass):
    """
    Args:
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        artifact_key: :attr:`artifact_key`
        capture_frame_window: :attr:`capture_frame_window`
        batch_size: :attr:`batch_size`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        trailing_frame_window: :attr:`trailing_frame_window`
    Attributes:
        input_artifact_uid: Inptu artifact for sim state data
        output_artifact_uid: Output artifact for processed sim state data
        artifact_key: Human readable name for this job
        capture_frame_window: Number of frames to retain prior to capture frame
        batch_size: Number of scenarios to process per pod
        code_build_artifact_uid: Set the tag/uid of the code build ECR image to use.
        trailing_frame_window: Number of frames to trail the sim to retain lidar quality"""

    _proto_message = pd_sim_state_pb2.SimStateCull

    def __init__(
        self,
        *,
        proto: Optional[pd_sim_state_pb2.SimStateCull] = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        artifact_key: str = None,
        capture_frame_window: int = None,
        batch_size: int = None,
        code_build_artifact_uid: str = None,
        trailing_frame_window: int = None,
    ):
        if proto is None:
            proto = pd_sim_state_pb2.SimStateCull()
        self.proto = proto
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if capture_frame_window is not None:
            self.capture_frame_window = capture_frame_window
        if batch_size is not None:
            self.batch_size = batch_size
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if trailing_frame_window is not None:
            self.trailing_frame_window = trailing_frame_window

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def capture_frame_window(self) -> int:
        return self.proto.capture_frame_window

    @capture_frame_window.setter
    def capture_frame_window(self, value: int):
        self.proto.capture_frame_window = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def trailing_frame_window(self) -> int:
        return self.proto.trailing_frame_window

    @trailing_frame_window.setter
    def trailing_frame_window(self, value: int):
        self.proto.trailing_frame_window = value

    def _update_proto_references(self, proto: pd_sim_state_pb2.SimStateCull):
        self.proto = proto


@register_wrapper(proto_type=pd_sim_state_pb2.ProcessSimStateParams)
class ProcessSimStateParams(ProtoMessageClass):
    """
    Args:
        override_time_of_day: :attr:`override_time_of_day`
        time_of_day: :attr:`time_of_day`
        override_sensor_rig: :attr:`override_sensor_rig`
        sensor_rig: :attr:`sensor_rig`
        override_wetness: :attr:`override_wetness`
        wetness: :attr:`wetness`
        override_rain_intensity: :attr:`override_rain_intensity`
        rain_intensity: :attr:`rain_intensity`
        override_fog_intensity: :attr:`override_fog_intensity`
        fog_intensity: :attr:`fog_intensity`
        override_streetlights: :attr:`override_streetlights`
        streetlights: :attr:`streetlights`
        override_headlights: :attr:`override_headlights`
        headlights: :attr:`headlights`
        capture_all_frames: :attr:`capture_all_frames`
        cull_agents: :attr:`cull_agents`
    Attributes:
        override_time_of_day:
        time_of_day:
        override_sensor_rig:
        sensor_rig:
        override_wetness:
        wetness:
        override_rain_intensity:
        rain_intensity:
        override_fog_intensity:
        fog_intensity:
        override_streetlights:
        streetlights:
        override_headlights:
        headlights:
        capture_all_frames:
        cull_agents:"""

    _proto_message = pd_sim_state_pb2.ProcessSimStateParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sim_state_pb2.ProcessSimStateParams] = None,
        override_time_of_day: bool = None,
        time_of_day: str = None,
        override_sensor_rig: bool = None,
        sensor_rig: _pd_sensor_pb2.SensorRigConfig = None,
        override_wetness: bool = None,
        wetness: float = None,
        override_rain_intensity: bool = None,
        rain_intensity: float = None,
        override_fog_intensity: bool = None,
        fog_intensity: float = None,
        override_streetlights: bool = None,
        streetlights: float = None,
        override_headlights: bool = None,
        headlights: bool = None,
        capture_all_frames: bool = None,
        cull_agents: List[int] = None,
    ):
        if proto is None:
            proto = pd_sim_state_pb2.ProcessSimStateParams()
        self.proto = proto
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        if override_time_of_day is not None:
            self.override_time_of_day = override_time_of_day
        if time_of_day is not None:
            self.time_of_day = time_of_day
        if override_sensor_rig is not None:
            self.override_sensor_rig = override_sensor_rig
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig
        if override_wetness is not None:
            self.override_wetness = override_wetness
        if wetness is not None:
            self.wetness = wetness
        if override_rain_intensity is not None:
            self.override_rain_intensity = override_rain_intensity
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if override_fog_intensity is not None:
            self.override_fog_intensity = override_fog_intensity
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if override_streetlights is not None:
            self.override_streetlights = override_streetlights
        if streetlights is not None:
            self.streetlights = streetlights
        if override_headlights is not None:
            self.override_headlights = override_headlights
        if headlights is not None:
            self.headlights = headlights
        if capture_all_frames is not None:
            self.capture_all_frames = capture_all_frames
        self._cull_agents = ProtoListWrapper(
            container=[int(v) for v in proto.cull_agents], attr_name="cull_agents", list_owner=self
        )
        if cull_agents is not None:
            self.cull_agents = cull_agents

    @property
    def override_time_of_day(self) -> bool:
        return self.proto.override_time_of_day

    @override_time_of_day.setter
    def override_time_of_day(self, value: bool):
        self.proto.override_time_of_day = value

    @property
    def time_of_day(self) -> str:
        return self.proto.time_of_day

    @time_of_day.setter
    def time_of_day(self, value: str):
        self.proto.time_of_day = value

    @property
    def override_sensor_rig(self) -> bool:
        return self.proto.override_sensor_rig

    @override_sensor_rig.setter
    def override_sensor_rig(self, value: bool):
        self.proto.override_sensor_rig = value

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self.proto.sensor_rig.CopyFrom(value.proto)

        self._sensor_rig = value
        self._sensor_rig._update_proto_references(self.proto.sensor_rig)

    @property
    def override_wetness(self) -> bool:
        return self.proto.override_wetness

    @override_wetness.setter
    def override_wetness(self, value: bool):
        self.proto.override_wetness = value

    @property
    def wetness(self) -> float:
        return self.proto.wetness

    @wetness.setter
    def wetness(self, value: float):
        self.proto.wetness = value

    @property
    def override_rain_intensity(self) -> bool:
        return self.proto.override_rain_intensity

    @override_rain_intensity.setter
    def override_rain_intensity(self, value: bool):
        self.proto.override_rain_intensity = value

    @property
    def rain_intensity(self) -> float:
        return self.proto.rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: float):
        self.proto.rain_intensity = value

    @property
    def override_fog_intensity(self) -> bool:
        return self.proto.override_fog_intensity

    @override_fog_intensity.setter
    def override_fog_intensity(self, value: bool):
        self.proto.override_fog_intensity = value

    @property
    def fog_intensity(self) -> float:
        return self.proto.fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: float):
        self.proto.fog_intensity = value

    @property
    def override_streetlights(self) -> bool:
        return self.proto.override_streetlights

    @override_streetlights.setter
    def override_streetlights(self, value: bool):
        self.proto.override_streetlights = value

    @property
    def streetlights(self) -> float:
        return self.proto.streetlights

    @streetlights.setter
    def streetlights(self, value: float):
        self.proto.streetlights = value

    @property
    def override_headlights(self) -> bool:
        return self.proto.override_headlights

    @override_headlights.setter
    def override_headlights(self, value: bool):
        self.proto.override_headlights = value

    @property
    def headlights(self) -> bool:
        return self.proto.headlights

    @headlights.setter
    def headlights(self, value: bool):
        self.proto.headlights = value

    @property
    def capture_all_frames(self) -> bool:
        return self.proto.capture_all_frames

    @capture_all_frames.setter
    def capture_all_frames(self, value: bool):
        self.proto.capture_all_frames = value

    @property
    def cull_agents(self) -> List[int]:
        return self._cull_agents

    @cull_agents.setter
    def cull_agents(self, value: List[int]):
        self._cull_agents.clear()
        for v in value:
            self._cull_agents.append(v)

    def _update_proto_references(self, proto: pd_sim_state_pb2.ProcessSimStateParams):
        self.proto = proto
        self._sensor_rig._update_proto_references(proto.sensor_rig)


@register_wrapper(proto_type=pd_sim_state_pb2.ProcessSimState)
class ProcessSimState(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        param_artifact_uid: :attr:`param_artifact_uid`
        params: :attr:`params`
        batch_size: :attr:`batch_size`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
    Attributes:
        artifact_key:
        input_artifact_uid:
        output_artifact_uid:
        param_artifact_uid:
        params:
        batch_size:
        code_build_artifact_uid: Set the tag/uid of the code build ECR image to use."""

    _proto_message = pd_sim_state_pb2.ProcessSimState

    def __init__(
        self,
        *,
        proto: Optional[pd_sim_state_pb2.ProcessSimState] = None,
        artifact_key: str = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        param_artifact_uid: str = None,
        params: ProcessSimStateParams = None,
        batch_size: int = None,
        code_build_artifact_uid: str = None,
    ):
        if proto is None:
            proto = pd_sim_state_pb2.ProcessSimState()
        self.proto = proto
        self._params = get_wrapper(proto_type=proto.params.__class__)(proto=proto.params)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if param_artifact_uid is not None:
            self.param_artifact_uid = param_artifact_uid
        if params is not None:
            self.params = params
        if batch_size is not None:
            self.batch_size = batch_size
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def param_artifact_uid(self) -> str:
        return self.proto.param_artifact_uid

    @param_artifact_uid.setter
    def param_artifact_uid(self, value: str):
        self.proto.param_artifact_uid = value

    @property
    def params(self) -> ProcessSimStateParams:
        return self._params

    @params.setter
    def params(self, value: ProcessSimStateParams):
        self.proto.params.CopyFrom(value.proto)

        self._params = value
        self._params._update_proto_references(self.proto.params)

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    def _update_proto_references(self, proto: pd_sim_state_pb2.ProcessSimState):
        self.proto = proto
        self._params._update_proto_references(proto.params)


@register_wrapper(proto_type=pd_sim_state_pb2.MergeSimState)
class MergeSimState(ProtoMessageClass):
    """
    Args:
        first_input_artifact_uid: :attr:`first_input_artifact_uid`
        second_input_artifact_uid: :attr:`second_input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
    Attributes:
        first_input_artifact_uid:
        second_input_artifact_uid:
        output_artifact_uid:"""

    _proto_message = pd_sim_state_pb2.MergeSimState

    def __init__(
        self,
        *,
        proto: Optional[pd_sim_state_pb2.MergeSimState] = None,
        first_input_artifact_uid: str = None,
        second_input_artifact_uid: str = None,
        output_artifact_uid: str = None,
    ):
        if proto is None:
            proto = pd_sim_state_pb2.MergeSimState()
        self.proto = proto
        if first_input_artifact_uid is not None:
            self.first_input_artifact_uid = first_input_artifact_uid
        if second_input_artifact_uid is not None:
            self.second_input_artifact_uid = second_input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def first_input_artifact_uid(self) -> str:
        return self.proto.first_input_artifact_uid

    @first_input_artifact_uid.setter
    def first_input_artifact_uid(self, value: str):
        self.proto.first_input_artifact_uid = value

    @property
    def second_input_artifact_uid(self) -> str:
        return self.proto.second_input_artifact_uid

    @second_input_artifact_uid.setter
    def second_input_artifact_uid(self, value: str):
        self.proto.second_input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    def _update_proto_references(self, proto: pd_sim_state_pb2.MergeSimState):
        self.proto = proto
