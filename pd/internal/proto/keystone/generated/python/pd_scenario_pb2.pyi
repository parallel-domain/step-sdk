import pd_environments_pb2 as _pd_environments_pb2
import pd_spawn_pb2 as _pd_spawn_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AgentTag(_message.Message):
    __slots__ = ["agent_id", "tags"]
    AGENT_ID_FIELD_NUMBER: ClassVar[int]
    TAGS_FIELD_NUMBER: ClassVar[int]
    agent_id: int
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, agent_id: Optional[int] = ..., tags: Optional[Iterable[str]] = ...) -> None: ...

class LinearMover(_message.Message):
    __slots__ = ["agent_id", "model", "orient_to_velocity", "origin", "rotation", "velocity_keys"]
    AGENT_ID_FIELD_NUMBER: ClassVar[int]
    MODEL_FIELD_NUMBER: ClassVar[int]
    ORIENT_TO_VELOCITY_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    ROTATION_FIELD_NUMBER: ClassVar[int]
    VELOCITY_KEYS_FIELD_NUMBER: ClassVar[int]
    agent_id: int
    model: str
    orient_to_velocity: bool
    origin: _containers.RepeatedScalarFieldContainer[float]
    rotation: _containers.RepeatedScalarFieldContainer[float]
    velocity_keys: _containers.RepeatedCompositeFieldContainer[VelocityKey]
    def __init__(self, agent_id: Optional[int] = ..., model: Optional[str] = ..., orient_to_velocity: bool = ..., origin: Optional[Iterable[float]] = ..., rotation: Optional[Iterable[float]] = ..., velocity_keys: Optional[Iterable[Union[VelocityKey, Mapping]]] = ...) -> None: ...

class ScenarioDefinition(_message.Message):
    __slots__ = ["agent_tags", "anti_aliasing", "config_blob", "current_time", "fog_intensity", "headlights", "lighting", "linear_movers", "name", "num_frames", "output_frame_skip", "performance_feature", "rain_intensity", "sensors", "sim_update_time", "skip_frames", "street_lights", "vehicles", "wetness", "world"]
    class PerformanceFeature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AGENT_TAGS_FIELD_NUMBER: ClassVar[int]
    ANTI_ALIASING_FIELD_NUMBER: ClassVar[int]
    CONFIG_BLOB_FIELD_NUMBER: ClassVar[int]
    CURRENT_TIME_FIELD_NUMBER: ClassVar[int]
    FOG_INTENSITY_FIELD_NUMBER: ClassVar[int]
    HEADLIGHTS_FIELD_NUMBER: ClassVar[int]
    HighFidelityMode: ScenarioDefinition.PerformanceFeature
    LIGHTING_FIELD_NUMBER: ClassVar[int]
    LINEAR_MOVERS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    NUM_FRAMES_FIELD_NUMBER: ClassVar[int]
    OUTPUT_FRAME_SKIP_FIELD_NUMBER: ClassVar[int]
    PERFORMANCE_FEATURE_FIELD_NUMBER: ClassVar[int]
    PerformanceMode: ScenarioDefinition.PerformanceFeature
    RAIN_INTENSITY_FIELD_NUMBER: ClassVar[int]
    SENSORS_FIELD_NUMBER: ClassVar[int]
    SIM_UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
    SKIP_FRAMES_FIELD_NUMBER: ClassVar[int]
    STREET_LIGHTS_FIELD_NUMBER: ClassVar[int]
    VEHICLES_FIELD_NUMBER: ClassVar[int]
    WETNESS_FIELD_NUMBER: ClassVar[int]
    WORLD_FIELD_NUMBER: ClassVar[int]
    agent_tags: _containers.RepeatedCompositeFieldContainer[AgentTag]
    anti_aliasing: int
    config_blob: str
    current_time: float
    fog_intensity: float
    headlights: bool
    lighting: str
    linear_movers: _containers.RepeatedCompositeFieldContainer[LinearMover]
    name: str
    num_frames: int
    output_frame_skip: int
    performance_feature: ScenarioDefinition.PerformanceFeature
    rain_intensity: float
    sensors: _containers.RepeatedCompositeFieldContainer[Sensor]
    sim_update_time: float
    skip_frames: int
    street_lights: float
    vehicles: _containers.RepeatedCompositeFieldContainer[Vehicle]
    wetness: float
    world: str
    def __init__(self, name: Optional[str] = ..., num_frames: Optional[int] = ..., skip_frames: Optional[int] = ..., current_time: Optional[float] = ..., sim_update_time: Optional[float] = ..., output_frame_skip: Optional[int] = ..., world: Optional[str] = ..., lighting: Optional[str] = ..., fog_intensity: Optional[float] = ..., rain_intensity: Optional[float] = ..., wetness: Optional[float] = ..., street_lights: Optional[float] = ..., headlights: bool = ..., linear_movers: Optional[Iterable[Union[LinearMover, Mapping]]] = ..., vehicles: Optional[Iterable[Union[Vehicle, Mapping]]] = ..., sensors: Optional[Iterable[Union[Sensor, Mapping]]] = ..., performance_feature: Optional[Union[ScenarioDefinition.PerformanceFeature, str]] = ..., anti_aliasing: Optional[int] = ..., config_blob: Optional[str] = ..., agent_tags: Optional[Iterable[Union[AgentTag, Mapping]]] = ...) -> None: ...

class ScenarioGenConfig(_message.Message):
    __slots__ = ["batch_size", "check_offroad_vehicles", "end_skip_frames", "environment", "merge_batches", "num_frames", "output_offset", "scenario_seed", "sim_capture_rate", "sim_settle_frames", "sim_terminate_on_collision_within_radius_m", "sim_terminate_on_drone_flight_path_end", "sim_terminate_on_pedestrian_collision_within_radius_m", "sim_update_time", "spawn_config", "start_skip_frames"]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    CHECK_OFFROAD_VEHICLES_FIELD_NUMBER: ClassVar[int]
    END_SKIP_FRAMES_FIELD_NUMBER: ClassVar[int]
    ENVIRONMENT_FIELD_NUMBER: ClassVar[int]
    MERGE_BATCHES_FIELD_NUMBER: ClassVar[int]
    NUM_FRAMES_FIELD_NUMBER: ClassVar[int]
    OUTPUT_OFFSET_FIELD_NUMBER: ClassVar[int]
    SCENARIO_SEED_FIELD_NUMBER: ClassVar[int]
    SIM_CAPTURE_RATE_FIELD_NUMBER: ClassVar[int]
    SIM_SETTLE_FRAMES_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_COLLISION_WITHIN_RADIUS_M_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_DRONE_FLIGHT_PATH_END_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_PEDESTRIAN_COLLISION_WITHIN_RADIUS_M_FIELD_NUMBER: ClassVar[int]
    SIM_UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
    SPAWN_CONFIG_FIELD_NUMBER: ClassVar[int]
    START_SKIP_FRAMES_FIELD_NUMBER: ClassVar[int]
    batch_size: int
    check_offroad_vehicles: bool
    end_skip_frames: int
    environment: _pd_environments_pb2.EnvironmentDefinition
    merge_batches: bool
    num_frames: int
    output_offset: int
    scenario_seed: int
    sim_capture_rate: int
    sim_settle_frames: int
    sim_terminate_on_collision_within_radius_m: float
    sim_terminate_on_drone_flight_path_end: bool
    sim_terminate_on_pedestrian_collision_within_radius_m: float
    sim_update_time: float
    spawn_config: _pd_spawn_pb2.SpawnConfig
    start_skip_frames: int
    def __init__(self, num_frames: Optional[int] = ..., sim_settle_frames: Optional[int] = ..., start_skip_frames: Optional[int] = ..., end_skip_frames: Optional[int] = ..., sim_capture_rate: Optional[int] = ..., sim_update_time: Optional[float] = ..., scenario_seed: Optional[int] = ..., output_offset: Optional[int] = ..., merge_batches: bool = ..., batch_size: Optional[int] = ..., environment: Optional[Union[_pd_environments_pb2.EnvironmentDefinition, Mapping]] = ..., spawn_config: Optional[Union[_pd_spawn_pb2.SpawnConfig, Mapping]] = ..., sim_terminate_on_collision_within_radius_m: Optional[float] = ..., sim_terminate_on_pedestrian_collision_within_radius_m: Optional[float] = ..., check_offroad_vehicles: bool = ..., sim_terminate_on_drone_flight_path_end: bool = ...) -> None: ...

class ScenarioLocation(_message.Message):
    __slots__ = ["generator_config", "location", "location_guid", "num_retries", "num_scenarios"]
    GENERATOR_CONFIG_FIELD_NUMBER: ClassVar[int]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    LOCATION_GUID_FIELD_NUMBER: ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: ClassVar[int]
    NUM_SCENARIOS_FIELD_NUMBER: ClassVar[int]
    generator_config: _pd_spawn_pb2.GeneratorConfig
    location: str
    location_guid: str
    num_retries: int
    num_scenarios: int
    def __init__(self, location: Optional[str] = ..., location_guid: Optional[str] = ..., num_scenarios: Optional[int] = ..., num_retries: Optional[int] = ..., generator_config: Optional[Union[_pd_spawn_pb2.GeneratorConfig, Mapping]] = ...) -> None: ...

class Sensor(_message.Message):
    __slots__ = ["agent_id", "origin", "rotation"]
    AGENT_ID_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    ROTATION_FIELD_NUMBER: ClassVar[int]
    agent_id: int
    origin: _containers.RepeatedScalarFieldContainer[float]
    rotation: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, agent_id: Optional[int] = ..., origin: Optional[Iterable[float]] = ..., rotation: Optional[Iterable[float]] = ...) -> None: ...

class Vehicle(_message.Message):
    __slots__ = ["agent_id", "aggression", "brake_until_time", "color", "constant_accelerate", "enable_merge_detection", "ignore_obstacles", "ignore_speed_limit", "lane_drift_amp", "lane_drift_scale", "lane_offset", "lane_path", "lane_shift_amount", "lane_shift_speed", "lane_shift_time", "position", "sensors", "target_separation", "target_velocity", "vehicle_actor", "vehicle_type", "velocity"]
    AGENT_ID_FIELD_NUMBER: ClassVar[int]
    AGGRESSION_FIELD_NUMBER: ClassVar[int]
    BRAKE_UNTIL_TIME_FIELD_NUMBER: ClassVar[int]
    COLOR_FIELD_NUMBER: ClassVar[int]
    CONSTANT_ACCELERATE_FIELD_NUMBER: ClassVar[int]
    ENABLE_MERGE_DETECTION_FIELD_NUMBER: ClassVar[int]
    IGNORE_OBSTACLES_FIELD_NUMBER: ClassVar[int]
    IGNORE_SPEED_LIMIT_FIELD_NUMBER: ClassVar[int]
    LANE_DRIFT_AMP_FIELD_NUMBER: ClassVar[int]
    LANE_DRIFT_SCALE_FIELD_NUMBER: ClassVar[int]
    LANE_OFFSET_FIELD_NUMBER: ClassVar[int]
    LANE_PATH_FIELD_NUMBER: ClassVar[int]
    LANE_SHIFT_AMOUNT_FIELD_NUMBER: ClassVar[int]
    LANE_SHIFT_SPEED_FIELD_NUMBER: ClassVar[int]
    LANE_SHIFT_TIME_FIELD_NUMBER: ClassVar[int]
    POSITION_FIELD_NUMBER: ClassVar[int]
    SENSORS_FIELD_NUMBER: ClassVar[int]
    TARGET_SEPARATION_FIELD_NUMBER: ClassVar[int]
    TARGET_VELOCITY_FIELD_NUMBER: ClassVar[int]
    VEHICLE_ACTOR_FIELD_NUMBER: ClassVar[int]
    VEHICLE_TYPE_FIELD_NUMBER: ClassVar[int]
    VELOCITY_FIELD_NUMBER: ClassVar[int]
    agent_id: int
    aggression: float
    brake_until_time: float
    color: str
    constant_accelerate: float
    enable_merge_detection: bool
    ignore_obstacles: bool
    ignore_speed_limit: bool
    lane_drift_amp: float
    lane_drift_scale: float
    lane_offset: float
    lane_path: _containers.RepeatedScalarFieldContainer[int]
    lane_shift_amount: float
    lane_shift_speed: float
    lane_shift_time: float
    position: _containers.RepeatedScalarFieldContainer[float]
    sensors: bool
    target_separation: float
    target_velocity: float
    vehicle_actor: str
    vehicle_type: str
    velocity: float
    def __init__(self, agent_id: Optional[int] = ..., sensors: bool = ..., color: Optional[str] = ..., vehicle_actor: Optional[str] = ..., vehicle_type: Optional[str] = ..., position: Optional[Iterable[float]] = ..., velocity: Optional[float] = ..., lane_path: Optional[Iterable[int]] = ..., target_velocity: Optional[float] = ..., target_separation: Optional[float] = ..., aggression: Optional[float] = ..., lane_drift_amp: Optional[float] = ..., lane_drift_scale: Optional[float] = ..., lane_offset: Optional[float] = ..., lane_shift_amount: Optional[float] = ..., lane_shift_speed: Optional[float] = ..., lane_shift_time: Optional[float] = ..., brake_until_time: Optional[float] = ..., constant_accelerate: Optional[float] = ..., enable_merge_detection: bool = ..., ignore_obstacles: bool = ..., ignore_speed_limit: bool = ...) -> None: ...

class VelocityKey(_message.Message):
    __slots__ = ["t", "velocity"]
    T_FIELD_NUMBER: ClassVar[int]
    VELOCITY_FIELD_NUMBER: ClassVar[int]
    t: float
    velocity: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, t: Optional[float] = ..., velocity: Optional[Iterable[float]] = ...) -> None: ...
