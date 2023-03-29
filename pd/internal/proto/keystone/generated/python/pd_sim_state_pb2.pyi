import pd_sensor_pb2 as _pd_sensor_pb2
import pd_scenario_pb2 as _pd_scenario_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class BuildSimState(_message.Message):
    __slots__ = ["code_build_artifact_uid", "locations", "name", "output_artifact_uid", "scenario_gen", "sensor_rig"]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    LOCATIONS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    SCENARIO_GEN_FIELD_NUMBER: ClassVar[int]
    SENSOR_RIG_FIELD_NUMBER: ClassVar[int]
    code_build_artifact_uid: str
    locations: _containers.RepeatedCompositeFieldContainer[_pd_scenario_pb2.ScenarioLocation]
    name: str
    output_artifact_uid: str
    scenario_gen: _pd_scenario_pb2.ScenarioGenConfig
    sensor_rig: _pd_sensor_pb2.SensorRigConfig
    def __init__(self, name: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., locations: Optional[Iterable[Union[_pd_scenario_pb2.ScenarioLocation, Mapping]]] = ..., scenario_gen: Optional[Union[_pd_scenario_pb2.ScenarioGenConfig, Mapping]] = ..., sensor_rig: Optional[Union[_pd_sensor_pb2.SensorRigConfig, Mapping]] = ...) -> None: ...

class MergeSimState(_message.Message):
    __slots__ = ["first_input_artifact_uid", "output_artifact_uid", "second_input_artifact_uid"]
    FIRST_INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    SECOND_INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    first_input_artifact_uid: str
    output_artifact_uid: str
    second_input_artifact_uid: str
    def __init__(self, first_input_artifact_uid: Optional[str] = ..., second_input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ...) -> None: ...

class ProcessSimState(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "input_artifact_uid", "output_artifact_uid", "param_artifact_uid", "params"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    PARAMS_FIELD_NUMBER: ClassVar[int]
    PARAM_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    input_artifact_uid: str
    output_artifact_uid: str
    param_artifact_uid: str
    params: ProcessSimStateParams
    def __init__(self, artifact_key: Optional[str] = ..., input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., param_artifact_uid: Optional[str] = ..., params: Optional[Union[ProcessSimStateParams, Mapping]] = ..., batch_size: Optional[int] = ...) -> None: ...

class ProcessSimStateParams(_message.Message):
    __slots__ = ["capture_all_frames", "cull_agents", "fog_intensity", "headlights", "override_fog_intensity", "override_headlights", "override_rain_intensity", "override_sensor_rig", "override_streetlights", "override_time_of_day", "override_wetness", "rain_intensity", "sensor_rig", "streetlights", "time_of_day", "wetness"]
    CAPTURE_ALL_FRAMES_FIELD_NUMBER: ClassVar[int]
    CULL_AGENTS_FIELD_NUMBER: ClassVar[int]
    FOG_INTENSITY_FIELD_NUMBER: ClassVar[int]
    HEADLIGHTS_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_FOG_INTENSITY_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_HEADLIGHTS_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_RAIN_INTENSITY_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_SENSOR_RIG_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_STREETLIGHTS_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_TIME_OF_DAY_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_WETNESS_FIELD_NUMBER: ClassVar[int]
    RAIN_INTENSITY_FIELD_NUMBER: ClassVar[int]
    SENSOR_RIG_FIELD_NUMBER: ClassVar[int]
    STREETLIGHTS_FIELD_NUMBER: ClassVar[int]
    TIME_OF_DAY_FIELD_NUMBER: ClassVar[int]
    WETNESS_FIELD_NUMBER: ClassVar[int]
    capture_all_frames: bool
    cull_agents: _containers.RepeatedScalarFieldContainer[int]
    fog_intensity: float
    headlights: bool
    override_fog_intensity: bool
    override_headlights: bool
    override_rain_intensity: bool
    override_sensor_rig: bool
    override_streetlights: bool
    override_time_of_day: bool
    override_wetness: bool
    rain_intensity: float
    sensor_rig: _pd_sensor_pb2.SensorRigConfig
    streetlights: float
    time_of_day: str
    wetness: float
    def __init__(self, override_time_of_day: bool = ..., time_of_day: Optional[str] = ..., override_sensor_rig: bool = ..., sensor_rig: Optional[Union[_pd_sensor_pb2.SensorRigConfig, Mapping]] = ..., override_wetness: bool = ..., wetness: Optional[float] = ..., override_rain_intensity: bool = ..., rain_intensity: Optional[float] = ..., override_fog_intensity: bool = ..., fog_intensity: Optional[float] = ..., override_streetlights: bool = ..., streetlights: Optional[float] = ..., override_headlights: bool = ..., headlights: bool = ..., capture_all_frames: bool = ..., cull_agents: Optional[Iterable[int]] = ...) -> None: ...

class SimStateCull(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "capture_frame_window", "code_build_artifact_uid", "input_artifact_uid", "output_artifact_uid", "trailing_frame_window"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    CAPTURE_FRAME_WINDOW_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    TRAILING_FRAME_WINDOW_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    capture_frame_window: int
    code_build_artifact_uid: str
    input_artifact_uid: str
    output_artifact_uid: str
    trailing_frame_window: int
    def __init__(self, input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., artifact_key: Optional[str] = ..., capture_frame_window: Optional[int] = ..., batch_size: Optional[int] = ..., code_build_artifact_uid: Optional[str] = ..., trailing_frame_window: Optional[int] = ...) -> None: ...
