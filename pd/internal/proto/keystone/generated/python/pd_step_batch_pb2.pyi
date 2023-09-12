from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationOverride(_message.Message):
    __slots__ = ["location", "location_uuid"]
    LOCATION_FIELD_NUMBER: ClassVar[int]
    LOCATION_UUID_FIELD_NUMBER: ClassVar[int]
    location: str
    location_uuid: str
    def __init__(self, location: Optional[str] = ..., location_uuid: Optional[str] = ...) -> None: ...

class StepBatch(_message.Message):
    __slots__ = ["batch_size", "check_offroad_vehicles", "end_skip_frames", "generate_name", "location_overrides", "merge_batches", "module_name", "name", "num_frames", "num_retries", "num_scenarios", "org", "output_artifact_uid", "output_offset", "scenario_container", "scenario_seed", "sim_capture_rate", "sim_settle_frames", "sim_terminate_on_collision_within_radius_m", "sim_terminate_on_drone_flight_path_end", "sim_terminate_on_pedestrian_collision_within_radius_m", "sim_update_time", "start_skip_frames"]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    CHECK_OFFROAD_VEHICLES_FIELD_NUMBER: ClassVar[int]
    END_SKIP_FRAMES_FIELD_NUMBER: ClassVar[int]
    GENERATE_NAME_FIELD_NUMBER: ClassVar[int]
    LOCATION_OVERRIDES_FIELD_NUMBER: ClassVar[int]
    MERGE_BATCHES_FIELD_NUMBER: ClassVar[int]
    MODULE_NAME_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    NUM_FRAMES_FIELD_NUMBER: ClassVar[int]
    NUM_RETRIES_FIELD_NUMBER: ClassVar[int]
    NUM_SCENARIOS_FIELD_NUMBER: ClassVar[int]
    ORG_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_OFFSET_FIELD_NUMBER: ClassVar[int]
    SCENARIO_CONTAINER_FIELD_NUMBER: ClassVar[int]
    SCENARIO_SEED_FIELD_NUMBER: ClassVar[int]
    SIM_CAPTURE_RATE_FIELD_NUMBER: ClassVar[int]
    SIM_SETTLE_FRAMES_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_COLLISION_WITHIN_RADIUS_M_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_DRONE_FLIGHT_PATH_END_FIELD_NUMBER: ClassVar[int]
    SIM_TERMINATE_ON_PEDESTRIAN_COLLISION_WITHIN_RADIUS_M_FIELD_NUMBER: ClassVar[int]
    SIM_UPDATE_TIME_FIELD_NUMBER: ClassVar[int]
    START_SKIP_FRAMES_FIELD_NUMBER: ClassVar[int]
    batch_size: int
    check_offroad_vehicles: bool
    end_skip_frames: int
    generate_name: str
    location_overrides: _containers.RepeatedCompositeFieldContainer[LocationOverride]
    merge_batches: bool
    module_name: str
    name: str
    num_frames: int
    num_retries: int
    num_scenarios: int
    org: str
    output_artifact_uid: str
    output_offset: int
    scenario_container: str
    scenario_seed: int
    sim_capture_rate: int
    sim_settle_frames: int
    sim_terminate_on_collision_within_radius_m: float
    sim_terminate_on_drone_flight_path_end: bool
    sim_terminate_on_pedestrian_collision_within_radius_m: float
    sim_update_time: float
    start_skip_frames: int
    def __init__(self, name: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., scenario_container: Optional[str] = ..., module_name: Optional[str] = ..., generate_name: Optional[str] = ..., org: Optional[str] = ..., num_scenarios: Optional[int] = ..., scenario_seed: Optional[int] = ..., batch_size: Optional[int] = ..., output_offset: Optional[int] = ..., merge_batches: bool = ..., num_frames: Optional[int] = ..., sim_settle_frames: Optional[int] = ..., start_skip_frames: Optional[int] = ..., end_skip_frames: Optional[int] = ..., sim_capture_rate: Optional[int] = ..., sim_update_time: Optional[float] = ..., num_retries: Optional[int] = ..., sim_terminate_on_collision_within_radius_m: Optional[float] = ..., sim_terminate_on_pedestrian_collision_within_radius_m: Optional[float] = ..., check_offroad_vehicles: bool = ..., sim_terminate_on_drone_flight_path_end: bool = ..., location_overrides: Optional[Iterable[Union[LocationOverride, Mapping]]] = ...) -> None: ...
