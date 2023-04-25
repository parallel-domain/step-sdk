from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_sim_state_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_sim_state_pb2.BuildSimState)
class BuildSimState(ProtoMessageClass):
    _proto_message = pd_sim_state_pb2.BuildSimState

    def __init__(self, *, proto: Optional[pd_sim_state_pb2.BuildSimState]=None, code_build_artifact_uid: Optional[str]=None, locations: Optional[List[_pd_scenario_pb2.ScenarioLocation]]=None, name: Optional[str]=None, output_artifact_uid: Optional[str]=None, scenario_gen: Optional[_pd_scenario_pb2.ScenarioGenConfig]=None, sensor_rig: Optional[_pd_sensor_pb2.SensorRigConfig]=None):
        if proto is None:
            proto = pd_sim_state_pb2.BuildSimState()
        self.proto = proto
        self._locations = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.locations], attr_name='locations', list_owner=proto)
        self._scenario_gen = get_wrapper(proto_type=proto.scenario_gen.__class__)(proto=proto.scenario_gen)
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if locations is not None:
            self.locations = locations
        if name is not None:
            self.name = name
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if scenario_gen is not None:
            self.scenario_gen = scenario_gen
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig

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
    def scenario_gen(self) -> _pd_scenario_pb2.ScenarioGenConfig:
        return self._scenario_gen

    @scenario_gen.setter
    def scenario_gen(self, value: _pd_scenario_pb2.ScenarioGenConfig):
        self._scenario_gen.proto.CopyFrom(value.proto)

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self._sensor_rig.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_sim_state_pb2.MergeSimState)
class MergeSimState(ProtoMessageClass):
    _proto_message = pd_sim_state_pb2.MergeSimState

    def __init__(self, *, proto: Optional[pd_sim_state_pb2.MergeSimState]=None, first_input_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None, second_input_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_sim_state_pb2.MergeSimState()
        self.proto = proto
        if first_input_artifact_uid is not None:
            self.first_input_artifact_uid = first_input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if second_input_artifact_uid is not None:
            self.second_input_artifact_uid = second_input_artifact_uid

    @property
    def first_input_artifact_uid(self) -> str:
        return self.proto.first_input_artifact_uid

    @first_input_artifact_uid.setter
    def first_input_artifact_uid(self, value: str):
        self.proto.first_input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def second_input_artifact_uid(self) -> str:
        return self.proto.second_input_artifact_uid

    @second_input_artifact_uid.setter
    def second_input_artifact_uid(self, value: str):
        self.proto.second_input_artifact_uid = value

@register_wrapper(proto_type=pd_sim_state_pb2.ProcessSimState)
class ProcessSimState(ProtoMessageClass):
    _proto_message = pd_sim_state_pb2.ProcessSimState

    def __init__(self, *, proto: Optional[pd_sim_state_pb2.ProcessSimState]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, code_build_artifact_uid: Optional[str]=None, input_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None, param_artifact_uid: Optional[str]=None, params: Optional[ProcessSimStateParams]=None):
        if proto is None:
            proto = pd_sim_state_pb2.ProcessSimState()
        self.proto = proto
        self._params = get_wrapper(proto_type=proto.params.__class__)(proto=proto.params)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if param_artifact_uid is not None:
            self.param_artifact_uid = param_artifact_uid
        if params is not None:
            self.params = params

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

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
        self._params.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_sim_state_pb2.ProcessSimStateParams)
class ProcessSimStateParams(ProtoMessageClass):
    _proto_message = pd_sim_state_pb2.ProcessSimStateParams

    def __init__(self, *, proto: Optional[pd_sim_state_pb2.ProcessSimStateParams]=None, capture_all_frames: Optional[bool]=None, cull_agents: Optional[List[int]]=None, fog_intensity: Optional[float]=None, headlights: Optional[bool]=None, override_fog_intensity: Optional[bool]=None, override_headlights: Optional[bool]=None, override_rain_intensity: Optional[bool]=None, override_sensor_rig: Optional[bool]=None, override_streetlights: Optional[bool]=None, override_time_of_day: Optional[bool]=None, override_wetness: Optional[bool]=None, rain_intensity: Optional[float]=None, sensor_rig: Optional[_pd_sensor_pb2.SensorRigConfig]=None, streetlights: Optional[float]=None, time_of_day: Optional[str]=None, wetness: Optional[float]=None):
        if proto is None:
            proto = pd_sim_state_pb2.ProcessSimStateParams()
        self.proto = proto
        self._cull_agents = ProtoListWrapper(container=[int(v) for v in proto.cull_agents], attr_name='cull_agents', list_owner=proto)
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        if capture_all_frames is not None:
            self.capture_all_frames = capture_all_frames
        if cull_agents is not None:
            self.cull_agents = cull_agents
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if headlights is not None:
            self.headlights = headlights
        if override_fog_intensity is not None:
            self.override_fog_intensity = override_fog_intensity
        if override_headlights is not None:
            self.override_headlights = override_headlights
        if override_rain_intensity is not None:
            self.override_rain_intensity = override_rain_intensity
        if override_sensor_rig is not None:
            self.override_sensor_rig = override_sensor_rig
        if override_streetlights is not None:
            self.override_streetlights = override_streetlights
        if override_time_of_day is not None:
            self.override_time_of_day = override_time_of_day
        if override_wetness is not None:
            self.override_wetness = override_wetness
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig
        if streetlights is not None:
            self.streetlights = streetlights
        if time_of_day is not None:
            self.time_of_day = time_of_day
        if wetness is not None:
            self.wetness = wetness

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

    @property
    def fog_intensity(self) -> float:
        return self.proto.fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: float):
        self.proto.fog_intensity = value

    @property
    def headlights(self) -> bool:
        return self.proto.headlights

    @headlights.setter
    def headlights(self, value: bool):
        self.proto.headlights = value

    @property
    def override_fog_intensity(self) -> bool:
        return self.proto.override_fog_intensity

    @override_fog_intensity.setter
    def override_fog_intensity(self, value: bool):
        self.proto.override_fog_intensity = value

    @property
    def override_headlights(self) -> bool:
        return self.proto.override_headlights

    @override_headlights.setter
    def override_headlights(self, value: bool):
        self.proto.override_headlights = value

    @property
    def override_rain_intensity(self) -> bool:
        return self.proto.override_rain_intensity

    @override_rain_intensity.setter
    def override_rain_intensity(self, value: bool):
        self.proto.override_rain_intensity = value

    @property
    def override_sensor_rig(self) -> bool:
        return self.proto.override_sensor_rig

    @override_sensor_rig.setter
    def override_sensor_rig(self, value: bool):
        self.proto.override_sensor_rig = value

    @property
    def override_streetlights(self) -> bool:
        return self.proto.override_streetlights

    @override_streetlights.setter
    def override_streetlights(self, value: bool):
        self.proto.override_streetlights = value

    @property
    def override_time_of_day(self) -> bool:
        return self.proto.override_time_of_day

    @override_time_of_day.setter
    def override_time_of_day(self, value: bool):
        self.proto.override_time_of_day = value

    @property
    def override_wetness(self) -> bool:
        return self.proto.override_wetness

    @override_wetness.setter
    def override_wetness(self, value: bool):
        self.proto.override_wetness = value

    @property
    def rain_intensity(self) -> float:
        return self.proto.rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: float):
        self.proto.rain_intensity = value

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self._sensor_rig.proto.CopyFrom(value.proto)

    @property
    def streetlights(self) -> float:
        return self.proto.streetlights

    @streetlights.setter
    def streetlights(self, value: float):
        self.proto.streetlights = value

    @property
    def time_of_day(self) -> str:
        return self.proto.time_of_day

    @time_of_day.setter
    def time_of_day(self, value: str):
        self.proto.time_of_day = value

    @property
    def wetness(self) -> float:
        return self.proto.wetness

    @wetness.setter
    def wetness(self, value: float):
        self.proto.wetness = value

@register_wrapper(proto_type=pd_sim_state_pb2.SimStateCull)
class SimStateCull(ProtoMessageClass):
    _proto_message = pd_sim_state_pb2.SimStateCull

    def __init__(self, *, proto: Optional[pd_sim_state_pb2.SimStateCull]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, capture_frame_window: Optional[int]=None, code_build_artifact_uid: Optional[str]=None, input_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None, trailing_frame_window: Optional[int]=None):
        if proto is None:
            proto = pd_sim_state_pb2.SimStateCull()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if capture_frame_window is not None:
            self.capture_frame_window = capture_frame_window
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if trailing_frame_window is not None:
            self.trailing_frame_window = trailing_frame_window

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def capture_frame_window(self) -> int:
        return self.proto.capture_frame_window

    @capture_frame_window.setter
    def capture_frame_window(self, value: int):
        self.proto.capture_frame_window = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

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
    def trailing_frame_window(self) -> int:
        return self.proto.trailing_frame_window

    @trailing_frame_window.setter
    def trailing_frame_window(self, value: int):
        self.proto.trailing_frame_window = value