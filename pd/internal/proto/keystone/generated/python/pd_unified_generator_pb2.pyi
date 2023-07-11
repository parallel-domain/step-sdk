import pd_types_pb2 as _pd_types_pb2
import pd_distributions_pb2 as _pd_distributions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

ANIMAL: AgentType
BLOCKED_LANE: ObstacleType
CROSSTRAFFIC: ObstacleType
DESCRIPTOR: _descriptor.FileDescriptor
DRIVE: Gear
DRONE: AgentType
EDGESTOPPER: PedestrianBehavior
EGO: SpecialAgentTag
END_OF_LANE: ObstacleType
FORWARD_AGENT: ObstacleType
JAYWALKER: PedestrianBehavior
LANE_CLOSURE: ObstacleType
LINEAR_MOVER: ObstacleType
MERGE: ObstacleType
NEUTRAL: Gear
NORMAL: PedestrianBehavior
ONCOMING_AGENT: ObstacleType
PARKED: Gear
PARKED_VEHICLE: AgentType
PATH_END: ObstacleType
PEDESTRIAN: AgentType
REVERSE: Gear
REVERSE_DISTANCE: ObstacleType
ROUTE_LENGTH: ObstacleType
STAR: SpecialAgentTag
STATIC: PedestrianBehavior
STATIC_OBJECT: AgentType
STOP_LINE: ObstacleType
TRAILER_VEHICLE: AgentType
UNSPECIFIED: AgentType
VEHICLE: AgentType

class AbsolutePositionRequest(_message.Message):
    __slots__ = ["lane_id", "position", "resolve_z", "rotation"]
    LANE_ID_FIELD_NUMBER: ClassVar[int]
    POSITION_FIELD_NUMBER: ClassVar[int]
    RESOLVE_Z_FIELD_NUMBER: ClassVar[int]
    ROTATION_FIELD_NUMBER: ClassVar[int]
    lane_id: int
    position: _pd_types_pb2.Float3
    resolve_z: bool
    rotation: _pd_types_pb2.Float3x3
    def __init__(self, position: Optional[Union[_pd_types_pb2.Float3, Mapping]] = ..., rotation: Optional[Union[_pd_types_pb2.Float3x3, Mapping]] = ..., lane_id: Optional[int] = ..., resolve_z: bool = ...) -> None: ...

class AgentSpawnData(_message.Message):
    __slots__ = ["tags"]
    TAGS_FIELD_NUMBER: ClassVar[int]
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, tags: Optional[Iterable[str]] = ...) -> None: ...

class AtomicGeneratorParameters(_message.Message):
    __slots__ = ["debris", "drone", "ego_agent", "parked_vehicles", "pedestrian", "random_pedestrian", "static_agent", "traffic", "vehicle"]
    DEBRIS_FIELD_NUMBER: ClassVar[int]
    DRONE_FIELD_NUMBER: ClassVar[int]
    EGO_AGENT_FIELD_NUMBER: ClassVar[int]
    PARKED_VEHICLES_FIELD_NUMBER: ClassVar[int]
    PEDESTRIAN_FIELD_NUMBER: ClassVar[int]
    RANDOM_PEDESTRIAN_FIELD_NUMBER: ClassVar[int]
    STATIC_AGENT_FIELD_NUMBER: ClassVar[int]
    TRAFFIC_FIELD_NUMBER: ClassVar[int]
    VEHICLE_FIELD_NUMBER: ClassVar[int]
    debris: DebrisGeneratorParameters
    drone: DroneGeneratorParameters
    ego_agent: EgoAgentGeneratorParameters
    parked_vehicles: ParkedVehicleGeneratorParameters
    pedestrian: PedestrianGeneratorParameters
    random_pedestrian: RandomPedestrianGeneratorParameters
    static_agent: StaticAgentGeneratorParameters
    traffic: TrafficGeneratorParameters
    vehicle: VehicleGeneratorParameters
    def __init__(self, ego_agent: Optional[Union[EgoAgentGeneratorParameters, Mapping]] = ..., vehicle: Optional[Union[VehicleGeneratorParameters, Mapping]] = ..., traffic: Optional[Union[TrafficGeneratorParameters, Mapping]] = ..., parked_vehicles: Optional[Union[ParkedVehicleGeneratorParameters, Mapping]] = ..., static_agent: Optional[Union[StaticAgentGeneratorParameters, Mapping]] = ..., debris: Optional[Union[DebrisGeneratorParameters, Mapping]] = ..., pedestrian: Optional[Union[PedestrianGeneratorParameters, Mapping]] = ..., random_pedestrian: Optional[Union[RandomPedestrianGeneratorParameters, Mapping]] = ..., drone: Optional[Union[DroneGeneratorParameters, Mapping]] = ...) -> None: ...

class CenterSpreadConfig(_message.Message):
    __slots__ = ["center", "spread"]
    CENTER_FIELD_NUMBER: ClassVar[int]
    SPREAD_FIELD_NUMBER: ClassVar[int]
    center: float
    spread: float
    def __init__(self, center: Optional[float] = ..., spread: Optional[float] = ...) -> None: ...

class CenterSpreadConfigInt(_message.Message):
    __slots__ = ["center", "spread"]
    CENTER_FIELD_NUMBER: ClassVar[int]
    SPREAD_FIELD_NUMBER: ClassVar[int]
    center: int
    spread: int
    def __init__(self, center: Optional[int] = ..., spread: Optional[int] = ...) -> None: ...

class CenterSpreadProbabilityConfig(_message.Message):
    __slots__ = ["center", "probability", "spread"]
    CENTER_FIELD_NUMBER: ClassVar[int]
    PROBABILITY_FIELD_NUMBER: ClassVar[int]
    SPREAD_FIELD_NUMBER: ClassVar[int]
    center: float
    probability: float
    spread: float
    def __init__(self, probability: Optional[float] = ..., center: Optional[float] = ..., spread: Optional[float] = ...) -> None: ...

class DebrisGeneratorParameters(_message.Message):
    __slots__ = ["agent_spawn_data", "asset_distribution", "debris_asset_remove_tag", "debris_asset_tag", "debris_center_bias", "max_debris_distance", "min_debris_distance", "position_request", "spawn_probability"]
    class AssetDistributionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: float
        def __init__(self, key: Optional[str] = ..., value: Optional[float] = ...) -> None: ...
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    ASSET_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    DEBRIS_ASSET_REMOVE_TAG_FIELD_NUMBER: ClassVar[int]
    DEBRIS_ASSET_TAG_FIELD_NUMBER: ClassVar[int]
    DEBRIS_CENTER_BIAS_FIELD_NUMBER: ClassVar[int]
    MAX_DEBRIS_DISTANCE_FIELD_NUMBER: ClassVar[int]
    MIN_DEBRIS_DISTANCE_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    SPAWN_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    asset_distribution: _containers.ScalarMap[str, float]
    debris_asset_remove_tag: str
    debris_asset_tag: str
    debris_center_bias: float
    max_debris_distance: float
    min_debris_distance: float
    position_request: PositionRequest
    spawn_probability: float
    def __init__(self, spawn_probability: Optional[float] = ..., debris_center_bias: Optional[float] = ..., min_debris_distance: Optional[float] = ..., max_debris_distance: Optional[float] = ..., debris_asset_tag: Optional[str] = ..., debris_asset_remove_tag: Optional[str] = ..., position_request: Optional[Union[PositionRequest, Mapping]] = ..., asset_distribution: Optional[Mapping[str, float]] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ...) -> None: ...

class DecorationData(_message.Message):
    __slots__ = ["decoration_preset"]
    DECORATION_PRESET_FIELD_NUMBER: ClassVar[int]
    decoration_preset: DecorationPreset
    def __init__(self, decoration_preset: Optional[Union[DecorationPreset, Mapping]] = ...) -> None: ...

class DecorationPreset(_message.Message):
    __slots__ = ["preset_name", "variant"]
    PRESET_NAME_FIELD_NUMBER: ClassVar[int]
    VARIANT_FIELD_NUMBER: ClassVar[int]
    preset_name: str
    variant: int
    def __init__(self, preset_name: Optional[str] = ..., variant: Optional[int] = ...) -> None: ...

class DefaultAtomicGeneratorParameters(_message.Message):
    __slots__ = ["vehicle_distribution"]
    class VehicleDistributionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.VehicleCategoryWeight
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.VehicleCategoryWeight, Mapping]] = ...) -> None: ...
    VEHICLE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    vehicle_distribution: _containers.MessageMap[str, _pd_distributions_pb2.VehicleCategoryWeight]
    def __init__(self, vehicle_distribution: Optional[Mapping[str, _pd_distributions_pb2.VehicleCategoryWeight]] = ...) -> None: ...

class DroneGeneratorParameters(_message.Message):
    __slots__ = ["drone_spawn_data", "position_request"]
    DRONE_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    drone_spawn_data: DroneSpawnData
    position_request: PositionRequest
    def __init__(self, position_request: Optional[Union[PositionRequest, Mapping]] = ..., drone_spawn_data: Optional[Union[DroneSpawnData, Mapping]] = ...) -> None: ...

class DroneSpawnData(_message.Message):
    __slots__ = ["agent_spawn_data", "ascend_probability", "flight_path_dir", "ground_asset_height_offset", "ground_asset_probability", "ground_assets", "height_offset"]
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    ASCEND_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    FLIGHT_PATH_DIR_FIELD_NUMBER: ClassVar[int]
    GROUND_ASSETS_FIELD_NUMBER: ClassVar[int]
    GROUND_ASSET_HEIGHT_OFFSET_FIELD_NUMBER: ClassVar[int]
    GROUND_ASSET_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    HEIGHT_OFFSET_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    ascend_probability: float
    flight_path_dir: str
    ground_asset_height_offset: _pd_distributions_pb2.ContinousUniformDistribution
    ground_asset_probability: float
    ground_assets: _containers.RepeatedScalarFieldContainer[str]
    height_offset: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, ascend_probability: Optional[float] = ..., ground_asset_probability: Optional[float] = ..., ground_assets: Optional[Iterable[str]] = ..., flight_path_dir: Optional[str] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ..., height_offset: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., ground_asset_height_offset: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...

class EgoAgentGeneratorParameters(_message.Message):
    __slots__ = ["agent_type", "drone_spawn_data", "ego_model", "pedestrian_spawn_data", "position_request", "vehicle_spawn_data"]
    AGENT_TYPE_FIELD_NUMBER: ClassVar[int]
    DRONE_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    EGO_MODEL_FIELD_NUMBER: ClassVar[int]
    PEDESTRIAN_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    VEHICLE_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    agent_type: AgentType
    drone_spawn_data: DroneSpawnData
    ego_model: str
    pedestrian_spawn_data: PedestrianSpawnData
    position_request: PositionRequest
    vehicle_spawn_data: VehicleSpawnData
    def __init__(self, agent_type: Optional[Union[AgentType, str]] = ..., ego_model: Optional[str] = ..., position_request: Optional[Union[PositionRequest, Mapping]] = ..., vehicle_spawn_data: Optional[Union[VehicleSpawnData, Mapping]] = ..., pedestrian_spawn_data: Optional[Union[PedestrianSpawnData, Mapping]] = ..., drone_spawn_data: Optional[Union[DroneSpawnData, Mapping]] = ...) -> None: ...

class EnvironmentParameters(_message.Message):
    __slots__ = ["crosswalk_sign_spawn_probability", "marker_data_map", "parking_space_data", "region", "sign_spawn_probability"]
    class MarkerDataMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: RoadMarkingData
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[RoadMarkingData, Mapping]] = ...) -> None: ...
    CROSSWALK_SIGN_SPAWN_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    MARKER_DATA_MAP_FIELD_NUMBER: ClassVar[int]
    PARKING_SPACE_DATA_FIELD_NUMBER: ClassVar[int]
    REGION_FIELD_NUMBER: ClassVar[int]
    SIGN_SPAWN_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    crosswalk_sign_spawn_probability: CenterSpreadConfig
    marker_data_map: _containers.MessageMap[str, RoadMarkingData]
    parking_space_data: ParkingSpaceData
    region: _pd_distributions_pb2.EnumDistribution
    sign_spawn_probability: CenterSpreadConfig
    def __init__(self, sign_spawn_probability: Optional[Union[CenterSpreadConfig, Mapping]] = ..., crosswalk_sign_spawn_probability: Optional[Union[CenterSpreadConfig, Mapping]] = ..., marker_data_map: Optional[Mapping[str, RoadMarkingData]] = ..., region: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., parking_space_data: Optional[Union[ParkingSpaceData, Mapping]] = ...) -> None: ...

class FloatArray(_message.Message):
    __slots__ = ["data"]
    DATA_FIELD_NUMBER: ClassVar[int]
    data: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, data: Optional[Iterable[float]] = ...) -> None: ...

class JunctionSpawnPolicy(_message.Message):
    __slots__ = ["distance_to_junction"]
    DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    distance_to_junction: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, distance_to_junction: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...

class LaneCurvatureSpawnPolicy(_message.Message):
    __slots__ = ["curvature_bounds", "min_section_length"]
    CURVATURE_BOUNDS_FIELD_NUMBER: ClassVar[int]
    MIN_SECTION_LENGTH_FIELD_NUMBER: ClassVar[int]
    curvature_bounds: MinMaxConfigFloat
    min_section_length: float
    def __init__(self, curvature_bounds: Optional[Union[MinMaxConfigFloat, Mapping]] = ..., min_section_length: Optional[float] = ...) -> None: ...

class LaneSpawnPolicy(_message.Message):
    __slots__ = ["bicycles_only_in_bike_lanes", "lane_decoration_distribution", "lane_type", "lateral_offset", "min_length_behind", "min_num_lanes_in_opposite_direction", "min_num_lanes_in_same_direction", "min_path_length", "nearby_asset_policy", "on_road_parking_angle_distribution", "position_of_interest_policy", "road_type"]
    BICYCLES_ONLY_IN_BIKE_LANES_FIELD_NUMBER: ClassVar[int]
    LANE_DECORATION_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    LANE_TYPE_FIELD_NUMBER: ClassVar[int]
    LATERAL_OFFSET_FIELD_NUMBER: ClassVar[int]
    MIN_LENGTH_BEHIND_FIELD_NUMBER: ClassVar[int]
    MIN_NUM_LANES_IN_OPPOSITE_DIRECTION_FIELD_NUMBER: ClassVar[int]
    MIN_NUM_LANES_IN_SAME_DIRECTION_FIELD_NUMBER: ClassVar[int]
    MIN_PATH_LENGTH_FIELD_NUMBER: ClassVar[int]
    NEARBY_ASSET_POLICY_FIELD_NUMBER: ClassVar[int]
    ON_ROAD_PARKING_ANGLE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    POSITION_OF_INTEREST_POLICY_FIELD_NUMBER: ClassVar[int]
    ROAD_TYPE_FIELD_NUMBER: ClassVar[int]
    bicycles_only_in_bike_lanes: bool
    lane_decoration_distribution: _pd_distributions_pb2.EnumDistribution
    lane_type: _pd_distributions_pb2.EnumDistribution
    lateral_offset: CenterSpreadConfig
    min_length_behind: CenterSpreadConfig
    min_num_lanes_in_opposite_direction: int
    min_num_lanes_in_same_direction: int
    min_path_length: CenterSpreadConfig
    nearby_asset_policy: NearbyAssetPolicy
    on_road_parking_angle_distribution: _pd_distributions_pb2.EnumDistribution
    position_of_interest_policy: _containers.RepeatedCompositeFieldContainer[PositionOfInterestPolicy]
    road_type: _pd_distributions_pb2.EnumDistribution
    def __init__(self, min_num_lanes_in_same_direction: Optional[int] = ..., lane_type: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., min_num_lanes_in_opposite_direction: Optional[int] = ..., lateral_offset: Optional[Union[CenterSpreadConfig, Mapping]] = ..., bicycles_only_in_bike_lanes: bool = ..., nearby_asset_policy: Optional[Union[NearbyAssetPolicy, Mapping]] = ..., road_type: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., position_of_interest_policy: Optional[Iterable[Union[PositionOfInterestPolicy, Mapping]]] = ..., min_path_length: Optional[Union[CenterSpreadConfig, Mapping]] = ..., min_length_behind: Optional[Union[CenterSpreadConfig, Mapping]] = ..., on_road_parking_angle_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., lane_decoration_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ...) -> None: ...

class LocationRelativePositionRequest(_message.Message):
    __slots__ = ["agent_tags", "lane_spawn_policy", "max_spawn_radius"]
    AGENT_TAGS_FIELD_NUMBER: ClassVar[int]
    LANE_SPAWN_POLICY_FIELD_NUMBER: ClassVar[int]
    MAX_SPAWN_RADIUS_FIELD_NUMBER: ClassVar[int]
    agent_tags: _containers.RepeatedScalarFieldContainer[str]
    lane_spawn_policy: LaneSpawnPolicy
    max_spawn_radius: float
    def __init__(self, agent_tags: Optional[Iterable[str]] = ..., max_spawn_radius: Optional[float] = ..., lane_spawn_policy: Optional[Union[LaneSpawnPolicy, Mapping]] = ...) -> None: ...

class MinMaxConfigFloat(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: ClassVar[int]
    MIN_FIELD_NUMBER: ClassVar[int]
    max: float
    min: float
    def __init__(self, min: Optional[float] = ..., max: Optional[float] = ...) -> None: ...

class MinMaxConfigInt(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: ClassVar[int]
    MIN_FIELD_NUMBER: ClassVar[int]
    max: int
    min: int
    def __init__(self, min: Optional[int] = ..., max: Optional[int] = ...) -> None: ...

class NearbyAssetPolicy(_message.Message):
    __slots__ = ["asset_tags", "num_assets", "search_radius"]
    ASSET_TAGS_FIELD_NUMBER: ClassVar[int]
    NUM_ASSETS_FIELD_NUMBER: ClassVar[int]
    SEARCH_RADIUS_FIELD_NUMBER: ClassVar[int]
    asset_tags: _containers.RepeatedScalarFieldContainer[str]
    num_assets: MinMaxConfigInt
    search_radius: CenterSpreadConfig
    def __init__(self, search_radius: Optional[Union[CenterSpreadConfig, Mapping]] = ..., num_assets: Optional[Union[MinMaxConfigInt, Mapping]] = ..., asset_tags: Optional[Iterable[str]] = ...) -> None: ...

class ObjectDecorationParams(_message.Message):
    __slots__ = ["decorate_chance", "preset_distribution"]
    DECORATE_CHANCE_FIELD_NUMBER: ClassVar[int]
    PRESET_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    decorate_chance: float
    preset_distribution: _pd_distributions_pb2.EnumDistribution
    def __init__(self, decorate_chance: Optional[float] = ..., preset_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ...) -> None: ...

class ObjectDecorations(_message.Message):
    __slots__ = ["decoration_data", "object_id"]
    DECORATION_DATA_FIELD_NUMBER: ClassVar[int]
    OBJECT_ID_FIELD_NUMBER: ClassVar[int]
    decoration_data: DecorationData
    object_id: int
    def __init__(self, object_id: Optional[int] = ..., decoration_data: Optional[Union[DecorationData, Mapping]] = ...) -> None: ...

class ParkedVehicleGeneratorParameters(_message.Message):
    __slots__ = ["agent_spawn_data", "position_request", "spawn_probability", "vehicle_distribution"]
    class VehicleDistributionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.VehicleCategoryWeight
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.VehicleCategoryWeight, Mapping]] = ...) -> None: ...
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    SPAWN_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    VEHICLE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    position_request: PositionRequest
    spawn_probability: CenterSpreadConfig
    vehicle_distribution: _containers.MessageMap[str, _pd_distributions_pb2.VehicleCategoryWeight]
    def __init__(self, position_request: Optional[Union[PositionRequest, Mapping]] = ..., spawn_probability: Optional[Union[CenterSpreadConfig, Mapping]] = ..., vehicle_distribution: Optional[Mapping[str, _pd_distributions_pb2.VehicleCategoryWeight]] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ...) -> None: ...

class ParkingSpaceData(_message.Message):
    __slots__ = ["delineation_color", "delineation_wear_amount", "global_parking_decal_wear", "lot_parking_delineation_type", "parking_lot_angle_distribution", "parking_space_decoration", "parking_space_grunge_amount", "parking_space_material", "parking_space_tint", "street_parking_angle_zero_override", "street_parking_delineation_type"]
    DELINEATION_COLOR_FIELD_NUMBER: ClassVar[int]
    DELINEATION_WEAR_AMOUNT_FIELD_NUMBER: ClassVar[int]
    GLOBAL_PARKING_DECAL_WEAR_FIELD_NUMBER: ClassVar[int]
    LOT_PARKING_DELINEATION_TYPE_FIELD_NUMBER: ClassVar[int]
    PARKING_LOT_ANGLE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    PARKING_SPACE_DECORATION_FIELD_NUMBER: ClassVar[int]
    PARKING_SPACE_GRUNGE_AMOUNT_FIELD_NUMBER: ClassVar[int]
    PARKING_SPACE_MATERIAL_FIELD_NUMBER: ClassVar[int]
    PARKING_SPACE_TINT_FIELD_NUMBER: ClassVar[int]
    STREET_PARKING_ANGLE_ZERO_OVERRIDE_FIELD_NUMBER: ClassVar[int]
    STREET_PARKING_DELINEATION_TYPE_FIELD_NUMBER: ClassVar[int]
    delineation_color: _containers.RepeatedCompositeFieldContainer[_pd_types_pb2.Float3]
    delineation_wear_amount: CenterSpreadConfig
    global_parking_decal_wear: CenterSpreadConfig
    lot_parking_delineation_type: _pd_distributions_pb2.EnumDistribution
    parking_lot_angle_distribution: _pd_distributions_pb2.EnumDistribution
    parking_space_decoration: ObjectDecorationParams
    parking_space_grunge_amount: CenterSpreadConfig
    parking_space_material: _pd_distributions_pb2.EnumDistribution
    parking_space_tint: _containers.RepeatedCompositeFieldContainer[_pd_types_pb2.Float3]
    street_parking_angle_zero_override: _pd_distributions_pb2.EnumDistribution
    street_parking_delineation_type: _pd_distributions_pb2.EnumDistribution
    def __init__(self, parking_lot_angle_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., lot_parking_delineation_type: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., street_parking_delineation_type: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., street_parking_angle_zero_override: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., delineation_color: Optional[Iterable[Union[_pd_types_pb2.Float3, Mapping]]] = ..., delineation_wear_amount: Optional[Union[CenterSpreadConfig, Mapping]] = ..., parking_space_material: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., parking_space_tint: Optional[Iterable[Union[_pd_types_pb2.Float3, Mapping]]] = ..., parking_space_grunge_amount: Optional[Union[CenterSpreadConfig, Mapping]] = ..., global_parking_decal_wear: Optional[Union[CenterSpreadConfig, Mapping]] = ..., parking_space_decoration: Optional[Union[ObjectDecorationParams, Mapping]] = ...) -> None: ...

class ParkingTypeDistribution(_message.Message):
    __slots__ = ["forward", "parallel", "reverse"]
    FORWARD_FIELD_NUMBER: ClassVar[int]
    PARALLEL_FIELD_NUMBER: ClassVar[int]
    REVERSE_FIELD_NUMBER: ClassVar[int]
    forward: float
    parallel: float
    reverse: float
    def __init__(self, forward: Optional[float] = ..., reverse: Optional[float] = ..., parallel: Optional[float] = ...) -> None: ...

class PathTimeRelativePositionRequest(_message.Message):
    __slots__ = ["agent_tags", "incident_angle", "time_along_path", "time_to_path"]
    AGENT_TAGS_FIELD_NUMBER: ClassVar[int]
    INCIDENT_ANGLE_FIELD_NUMBER: ClassVar[int]
    TIME_ALONG_PATH_FIELD_NUMBER: ClassVar[int]
    TIME_TO_PATH_FIELD_NUMBER: ClassVar[int]
    agent_tags: _containers.RepeatedScalarFieldContainer[str]
    incident_angle: _pd_distributions_pb2.ContinousUniformDistribution
    time_along_path: _pd_distributions_pb2.ContinousUniformDistribution
    time_to_path: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, agent_tags: Optional[Iterable[str]] = ..., time_to_path: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., time_along_path: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., incident_angle: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...

class PedestrianGeneratorParameters(_message.Message):
    __slots__ = ["ped_spawn_data", "position_request"]
    PED_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    ped_spawn_data: PedestrianSpawnData
    position_request: PositionRequest
    def __init__(self, position_request: Optional[Union[PositionRequest, Mapping]] = ..., ped_spawn_data: Optional[Union[PedestrianSpawnData, Mapping]] = ...) -> None: ...

class PedestrianSpawnData(_message.Message):
    __slots__ = ["agent_spawn_data", "asset_name", "check_occupancy", "jaywalker_ego_fwd_offset", "orient_to_velocity", "ped_behavior", "pedestrian_color_override_probability", "pedestrian_color_override_rgb", "pedestrians_dynamic_pathing", "speed"]
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    ASSET_NAME_FIELD_NUMBER: ClassVar[int]
    CHECK_OCCUPANCY_FIELD_NUMBER: ClassVar[int]
    JAYWALKER_EGO_FWD_OFFSET_FIELD_NUMBER: ClassVar[int]
    ORIENT_TO_VELOCITY_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANS_DYNAMIC_PATHING_FIELD_NUMBER: ClassVar[int]
    PEDESTRIAN_COLOR_OVERRIDE_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    PEDESTRIAN_COLOR_OVERRIDE_RGB_FIELD_NUMBER: ClassVar[int]
    PED_BEHAVIOR_FIELD_NUMBER: ClassVar[int]
    SPEED_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    asset_name: str
    check_occupancy: bool
    jaywalker_ego_fwd_offset: float
    orient_to_velocity: bool
    ped_behavior: PedestrianBehavior
    pedestrian_color_override_probability: CenterSpreadConfig
    pedestrian_color_override_rgb: _pd_types_pb2.Float3
    pedestrians_dynamic_pathing: bool
    speed: float
    def __init__(self, pedestrian_color_override_probability: Optional[Union[CenterSpreadConfig, Mapping]] = ..., pedestrian_color_override_rgb: Optional[Union[_pd_types_pb2.Float3, Mapping]] = ..., pedestrians_dynamic_pathing: bool = ..., orient_to_velocity: bool = ..., check_occupancy: bool = ..., jaywalker_ego_fwd_offset: Optional[float] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ..., ped_behavior: Optional[Union[PedestrianBehavior, str]] = ..., asset_name: Optional[str] = ..., speed: Optional[float] = ...) -> None: ...

class PositionOfInterestPolicy(_message.Message):
    __slots__ = ["junction_spawn_policy", "lane_curvature_spawn_policy"]
    JUNCTION_SPAWN_POLICY_FIELD_NUMBER: ClassVar[int]
    LANE_CURVATURE_SPAWN_POLICY_FIELD_NUMBER: ClassVar[int]
    junction_spawn_policy: JunctionSpawnPolicy
    lane_curvature_spawn_policy: LaneCurvatureSpawnPolicy
    def __init__(self, lane_curvature_spawn_policy: Optional[Union[LaneCurvatureSpawnPolicy, Mapping]] = ..., junction_spawn_policy: Optional[Union[JunctionSpawnPolicy, Mapping]] = ...) -> None: ...

class PositionRequest(_message.Message):
    __slots__ = ["absolute_position_request", "lane_spawn_policy", "lateral_offset", "location_relative_position_request", "longitudinal_offset", "path_time_relative_position_request", "road_pitch_position_request", "yaw_offset"]
    ABSOLUTE_POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    LANE_SPAWN_POLICY_FIELD_NUMBER: ClassVar[int]
    LATERAL_OFFSET_FIELD_NUMBER: ClassVar[int]
    LOCATION_RELATIVE_POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    LONGITUDINAL_OFFSET_FIELD_NUMBER: ClassVar[int]
    PATH_TIME_RELATIVE_POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    ROAD_PITCH_POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    YAW_OFFSET_FIELD_NUMBER: ClassVar[int]
    absolute_position_request: AbsolutePositionRequest
    lane_spawn_policy: LaneSpawnPolicy
    lateral_offset: CenterSpreadConfig
    location_relative_position_request: LocationRelativePositionRequest
    longitudinal_offset: CenterSpreadConfig
    path_time_relative_position_request: PathTimeRelativePositionRequest
    road_pitch_position_request: RoadPitchPositionRequest
    yaw_offset: CenterSpreadConfig
    def __init__(self, longitudinal_offset: Optional[Union[CenterSpreadConfig, Mapping]] = ..., lateral_offset: Optional[Union[CenterSpreadConfig, Mapping]] = ..., yaw_offset: Optional[Union[CenterSpreadConfig, Mapping]] = ..., absolute_position_request: Optional[Union[AbsolutePositionRequest, Mapping]] = ..., path_time_relative_position_request: Optional[Union[PathTimeRelativePositionRequest, Mapping]] = ..., location_relative_position_request: Optional[Union[LocationRelativePositionRequest, Mapping]] = ..., lane_spawn_policy: Optional[Union[LaneSpawnPolicy, Mapping]] = ..., road_pitch_position_request: Optional[Union[RoadPitchPositionRequest, Mapping]] = ...) -> None: ...

class RandomPedestrianGeneratorParameters(_message.Message):
    __slots__ = ["min_radius_between_pedestrians", "num_of_pedestrians_range", "ped_spawn_data", "position_request", "speed_range"]
    MIN_RADIUS_BETWEEN_PEDESTRIANS_FIELD_NUMBER: ClassVar[int]
    NUM_OF_PEDESTRIANS_RANGE_FIELD_NUMBER: ClassVar[int]
    PED_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    SPEED_RANGE_FIELD_NUMBER: ClassVar[int]
    min_radius_between_pedestrians: float
    num_of_pedestrians_range: MinMaxConfigInt
    ped_spawn_data: PedestrianSpawnData
    position_request: PositionRequest
    speed_range: MinMaxConfigFloat
    def __init__(self, speed_range: Optional[Union[MinMaxConfigFloat, Mapping]] = ..., position_request: Optional[Union[PositionRequest, Mapping]] = ..., num_of_pedestrians_range: Optional[Union[MinMaxConfigInt, Mapping]] = ..., min_radius_between_pedestrians: Optional[float] = ..., ped_spawn_data: Optional[Union[PedestrianSpawnData, Mapping]] = ...) -> None: ...

class RoadMarkingData(_message.Message):
    __slots__ = ["marker_types", "override_colors", "preset_colors", "use_preset", "wear"]
    MARKER_TYPES_FIELD_NUMBER: ClassVar[int]
    OVERRIDE_COLORS_FIELD_NUMBER: ClassVar[int]
    PRESET_COLORS_FIELD_NUMBER: ClassVar[int]
    USE_PRESET_FIELD_NUMBER: ClassVar[int]
    WEAR_FIELD_NUMBER: ClassVar[int]
    marker_types: _containers.RepeatedScalarFieldContainer[str]
    override_colors: _containers.RepeatedCompositeFieldContainer[FloatArray]
    preset_colors: _containers.RepeatedScalarFieldContainer[str]
    use_preset: bool
    wear: CenterSpreadConfig
    def __init__(self, use_preset: bool = ..., override_colors: Optional[Iterable[Union[FloatArray, Mapping]]] = ..., preset_colors: Optional[Iterable[str]] = ..., marker_types: Optional[Iterable[str]] = ..., wear: Optional[Union[CenterSpreadConfig, Mapping]] = ...) -> None: ...

class RoadPitchPositionRequest(_message.Message):
    __slots__ = ["bin_pitch_points", "bin_width", "lane_spawn_policy", "road_pitch"]
    BIN_PITCH_POINTS_FIELD_NUMBER: ClassVar[int]
    BIN_WIDTH_FIELD_NUMBER: ClassVar[int]
    LANE_SPAWN_POLICY_FIELD_NUMBER: ClassVar[int]
    ROAD_PITCH_FIELD_NUMBER: ClassVar[int]
    bin_pitch_points: bool
    bin_width: float
    lane_spawn_policy: LaneSpawnPolicy
    road_pitch: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, road_pitch: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., lane_spawn_policy: Optional[Union[LaneSpawnPolicy, Mapping]] = ..., bin_pitch_points: bool = ..., bin_width: Optional[float] = ...) -> None: ...

class SignalLightDistribution(_message.Message):
    __slots__ = ["green", "red", "yellow"]
    GREEN_FIELD_NUMBER: ClassVar[int]
    RED_FIELD_NUMBER: ClassVar[int]
    YELLOW_FIELD_NUMBER: ClassVar[int]
    green: float
    red: float
    yellow: float
    def __init__(self, green: Optional[float] = ..., red: Optional[float] = ..., yellow: Optional[float] = ...) -> None: ...

class StaticAgentGeneratorParameters(_message.Message):
    __slots__ = ["agent_spawn_data", "model", "position_request"]
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    MODEL_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    model: str
    position_request: PositionRequest
    def __init__(self, position_request: Optional[Union[PositionRequest, Mapping]] = ..., model: Optional[str] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ...) -> None: ...

class TrafficGeneratorParameters(_message.Message):
    __slots__ = ["position_request", "spawn_probability", "start_separation_time_map", "target_separation_time_map", "vehicle_distribution", "vehicle_spawn_data"]
    class StartSeparationTimeMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.ContinousUniformDistribution
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...
    class TargetSeparationTimeMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.ContinousUniformDistribution
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...
    class VehicleDistributionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.VehicleCategoryWeight
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.VehicleCategoryWeight, Mapping]] = ...) -> None: ...
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    SPAWN_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    START_SEPARATION_TIME_MAP_FIELD_NUMBER: ClassVar[int]
    TARGET_SEPARATION_TIME_MAP_FIELD_NUMBER: ClassVar[int]
    VEHICLE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    VEHICLE_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    position_request: PositionRequest
    spawn_probability: float
    start_separation_time_map: _containers.MessageMap[str, _pd_distributions_pb2.ContinousUniformDistribution]
    target_separation_time_map: _containers.MessageMap[str, _pd_distributions_pb2.ContinousUniformDistribution]
    vehicle_distribution: _containers.MessageMap[str, _pd_distributions_pb2.VehicleCategoryWeight]
    vehicle_spawn_data: VehicleSpawnData
    def __init__(self, position_request: Optional[Union[PositionRequest, Mapping]] = ..., spawn_probability: Optional[float] = ..., vehicle_spawn_data: Optional[Union[VehicleSpawnData, Mapping]] = ..., vehicle_distribution: Optional[Mapping[str, _pd_distributions_pb2.VehicleCategoryWeight]] = ..., start_separation_time_map: Optional[Mapping[str, _pd_distributions_pb2.ContinousUniformDistribution]] = ..., target_separation_time_map: Optional[Mapping[str, _pd_distributions_pb2.ContinousUniformDistribution]] = ...) -> None: ...

class TurnTypeDistribution(_message.Message):
    __slots__ = ["left", "right", "straight"]
    LEFT_FIELD_NUMBER: ClassVar[int]
    RIGHT_FIELD_NUMBER: ClassVar[int]
    STRAIGHT_FIELD_NUMBER: ClassVar[int]
    left: float
    right: float
    straight: float
    def __init__(self, straight: Optional[float] = ..., left: Optional[float] = ..., right: Optional[float] = ...) -> None: ...

class UnifiedGeneratorParameters(_message.Message):
    __slots__ = ["atomics", "default_params", "environment_params", "use_merge_batches"]
    ATOMICS_FIELD_NUMBER: ClassVar[int]
    DEFAULT_PARAMS_FIELD_NUMBER: ClassVar[int]
    ENVIRONMENT_PARAMS_FIELD_NUMBER: ClassVar[int]
    USE_MERGE_BATCHES_FIELD_NUMBER: ClassVar[int]
    atomics: _containers.RepeatedCompositeFieldContainer[AtomicGeneratorParameters]
    default_params: DefaultAtomicGeneratorParameters
    environment_params: EnvironmentParameters
    use_merge_batches: bool
    def __init__(self, atomics: Optional[Iterable[Union[AtomicGeneratorParameters, Mapping]]] = ..., use_merge_batches: bool = ..., default_params: Optional[Union[DefaultAtomicGeneratorParameters, Mapping]] = ..., environment_params: Optional[Union[EnvironmentParameters, Mapping]] = ...) -> None: ...

class VehicleBehavior(_message.Message):
    __slots__ = ["enable_dynamic_lane_selection", "ignore_obstacle_types", "ignore_speed_limit", "lane_change_cooldown", "lane_change_probability", "lane_drift_amplitude", "lane_drift_scale", "lane_offset", "parking_scenario_goal", "parking_scenario_time", "start_gear", "start_separation_time", "start_speed", "target_separation_time", "target_speed", "vehicle_aggression"]
    ENABLE_DYNAMIC_LANE_SELECTION_FIELD_NUMBER: ClassVar[int]
    IGNORE_OBSTACLE_TYPES_FIELD_NUMBER: ClassVar[int]
    IGNORE_SPEED_LIMIT_FIELD_NUMBER: ClassVar[int]
    LANE_CHANGE_COOLDOWN_FIELD_NUMBER: ClassVar[int]
    LANE_CHANGE_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    LANE_DRIFT_AMPLITUDE_FIELD_NUMBER: ClassVar[int]
    LANE_DRIFT_SCALE_FIELD_NUMBER: ClassVar[int]
    LANE_OFFSET_FIELD_NUMBER: ClassVar[int]
    PARKING_SCENARIO_GOAL_FIELD_NUMBER: ClassVar[int]
    PARKING_SCENARIO_TIME_FIELD_NUMBER: ClassVar[int]
    START_GEAR_FIELD_NUMBER: ClassVar[int]
    START_SEPARATION_TIME_FIELD_NUMBER: ClassVar[int]
    START_SPEED_FIELD_NUMBER: ClassVar[int]
    TARGET_SEPARATION_TIME_FIELD_NUMBER: ClassVar[int]
    TARGET_SPEED_FIELD_NUMBER: ClassVar[int]
    VEHICLE_AGGRESSION_FIELD_NUMBER: ClassVar[int]
    enable_dynamic_lane_selection: bool
    ignore_obstacle_types: _containers.RepeatedScalarFieldContainer[ObstacleType]
    ignore_speed_limit: bool
    lane_change_cooldown: _pd_distributions_pb2.ContinousUniformDistribution
    lane_change_probability: _pd_distributions_pb2.ContinousUniformDistribution
    lane_drift_amplitude: _pd_distributions_pb2.ContinousUniformDistribution
    lane_drift_scale: _pd_distributions_pb2.ContinousUniformDistribution
    lane_offset: _pd_distributions_pb2.ContinousUniformDistribution
    parking_scenario_goal: PositionRequest
    parking_scenario_time: _pd_distributions_pb2.ContinousUniformDistribution
    start_gear: Gear
    start_separation_time: _pd_distributions_pb2.ContinousUniformDistribution
    start_speed: _pd_distributions_pb2.ContinousUniformDistribution
    target_separation_time: _pd_distributions_pb2.ContinousUniformDistribution
    target_speed: _pd_distributions_pb2.ContinousUniformDistribution
    vehicle_aggression: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, start_speed: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., target_speed: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., ignore_speed_limit: bool = ..., lane_offset: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., lane_drift_scale: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., lane_drift_amplitude: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., lane_change_probability: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., lane_change_cooldown: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., enable_dynamic_lane_selection: bool = ..., start_gear: Optional[Union[Gear, str]] = ..., start_separation_time: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., target_separation_time: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., vehicle_aggression: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., ignore_obstacle_types: Optional[Iterable[Union[ObstacleType, str]]] = ..., parking_scenario_goal: Optional[Union[PositionRequest, Mapping]] = ..., parking_scenario_time: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ...) -> None: ...

class VehicleGeneratorParameters(_message.Message):
    __slots__ = ["model", "position_request", "vehicle_spawn_data"]
    MODEL_FIELD_NUMBER: ClassVar[int]
    POSITION_REQUEST_FIELD_NUMBER: ClassVar[int]
    VEHICLE_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    model: str
    position_request: PositionRequest
    vehicle_spawn_data: VehicleSpawnData
    def __init__(self, model: Optional[str] = ..., position_request: Optional[Union[PositionRequest, Mapping]] = ..., vehicle_spawn_data: Optional[Union[VehicleSpawnData, Mapping]] = ...) -> None: ...

class VehiclePeripheral(_message.Message):
    __slots__ = ["disable_accessories", "disable_occupants", "emergency_light_probability", "randomize_vehicle_parts", "spawn_trailer_probability", "trailer_initial_yaw"]
    DISABLE_ACCESSORIES_FIELD_NUMBER: ClassVar[int]
    DISABLE_OCCUPANTS_FIELD_NUMBER: ClassVar[int]
    EMERGENCY_LIGHT_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    RANDOMIZE_VEHICLE_PARTS_FIELD_NUMBER: ClassVar[int]
    SPAWN_TRAILER_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    TRAILER_INITIAL_YAW_FIELD_NUMBER: ClassVar[int]
    disable_accessories: bool
    disable_occupants: bool
    emergency_light_probability: float
    randomize_vehicle_parts: bool
    spawn_trailer_probability: float
    trailer_initial_yaw: _pd_distributions_pb2.ContinousUniformDistribution
    def __init__(self, spawn_trailer_probability: Optional[float] = ..., trailer_initial_yaw: Optional[Union[_pd_distributions_pb2.ContinousUniformDistribution, Mapping]] = ..., disable_occupants: bool = ..., disable_accessories: bool = ..., randomize_vehicle_parts: bool = ..., emergency_light_probability: Optional[float] = ...) -> None: ...

class VehicleSpawnData(_message.Message):
    __slots__ = ["agent_spawn_data", "vehicle_behavior", "vehicle_peripheral"]
    AGENT_SPAWN_DATA_FIELD_NUMBER: ClassVar[int]
    VEHICLE_BEHAVIOR_FIELD_NUMBER: ClassVar[int]
    VEHICLE_PERIPHERAL_FIELD_NUMBER: ClassVar[int]
    agent_spawn_data: AgentSpawnData
    vehicle_behavior: VehicleBehavior
    vehicle_peripheral: VehiclePeripheral
    def __init__(self, vehicle_behavior: Optional[Union[VehicleBehavior, Mapping]] = ..., vehicle_peripheral: Optional[Union[VehiclePeripheral, Mapping]] = ..., agent_spawn_data: Optional[Union[AgentSpawnData, Mapping]] = ...) -> None: ...

class AgentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class ObstacleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Gear(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class PedestrianBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SpecialAgentTag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
