from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class AABB(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: ClassVar[int]
    MIN_FIELD_NUMBER: ClassVar[int]
    max: Point_ENU
    min: Point_ENU
    def __init__(self, min: Optional[Union[Point_ENU, Mapping]] = ..., max: Optional[Union[Point_ENU, Mapping]] = ...) -> None: ...

class Area(_message.Message):
    __slots__ = ["edges", "floors", "height", "id", "type", "user_data"]
    class AreaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BUILDING_APARTMENT: Area.AreaType
    BUILDING_COMMERCIAL: Area.AreaType
    BUILDING_GARAGE: Area.AreaType
    BUILDING_GAS: Area.AreaType
    BUILDING_HOUSE: Area.AreaType
    BUILDING_INDUSTRIAL: Area.AreaType
    BUILDING_OFFICE: Area.AreaType
    BUILDING_PARKING: Area.AreaType
    BUILDING_RESIDENTIAL: Area.AreaType
    BUILDING_RETAIL: Area.AreaType
    BUILDING_SCHOOL: Area.AreaType
    BUILDING_UNCLASSIFIED: Area.AreaType
    BUILDING_WAREHOUSE: Area.AreaType
    CONSTRUCTION: Area.AreaType
    EDGES_FIELD_NUMBER: ClassVar[int]
    EMPTY_LOT: Area.AreaType
    FLOORS_FIELD_NUMBER: ClassVar[int]
    HEIGHT_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    PARK: Area.AreaType
    PARKING_LOT: Area.AreaType
    PARKING_SPACE: Area.AreaType
    POWER: Area.AreaType
    RAIL: Area.AreaType
    SIDEWALK: Area.AreaType
    SPEEDBUMP: Area.AreaType
    TYPE_FIELD_NUMBER: ClassVar[int]
    UNCLASSIFIED: Area.AreaType
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    WATER: Area.AreaType
    YARD: Area.AreaType
    ZONE_BROWN: Area.AreaType
    ZONE_COMMERCIAL: Area.AreaType
    ZONE_GREEN: Area.AreaType
    ZONE_INDUSTRIAL: Area.AreaType
    ZONE_RESIDENTIAL: Area.AreaType
    ZONE_RETAIL: Area.AreaType
    ZONE_WATER: Area.AreaType
    edges: _containers.RepeatedScalarFieldContainer[int]
    floors: int
    height: float
    id: int
    type: Area.AreaType
    user_data: str
    def __init__(self, id: Optional[int] = ..., type: Optional[Union[Area.AreaType, str]] = ..., edges: Optional[Iterable[int]] = ..., height: Optional[float] = ..., floors: Optional[int] = ..., user_data: Optional[str] = ...) -> None: ...

class Edge(_message.Message):
    __slots__ = ["id", "open", "points", "user_data"]
    ID_FIELD_NUMBER: ClassVar[int]
    OPEN_FIELD_NUMBER: ClassVar[int]
    POINTS_FIELD_NUMBER: ClassVar[int]
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    id: int
    open: bool
    points: _containers.RepeatedCompositeFieldContainer[Point_ENU]
    user_data: str
    def __init__(self, id: Optional[int] = ..., open: bool = ..., points: Optional[Iterable[Union[Point_ENU, Mapping]]] = ..., user_data: Optional[str] = ...) -> None: ...

class Info(_message.Message):
    __slots__ = ["audit", "name", "origin"]
    AUDIT_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    audit: str
    name: str
    origin: Point_LLA
    def __init__(self, name: Optional[str] = ..., origin: Optional[Union[Point_LLA, Mapping]] = ..., audit: Optional[str] = ...) -> None: ...

class Junction(_message.Message):
    __slots__ = ["corners", "crosswalk_lanes", "id", "lane_segments", "road_segments", "signaled_intersection", "signed_intersection", "user_data"]
    CORNERS_FIELD_NUMBER: ClassVar[int]
    CROSSWALK_LANES_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    LANE_SEGMENTS_FIELD_NUMBER: ClassVar[int]
    ROAD_SEGMENTS_FIELD_NUMBER: ClassVar[int]
    SIGNALED_INTERSECTION_FIELD_NUMBER: ClassVar[int]
    SIGNED_INTERSECTION_FIELD_NUMBER: ClassVar[int]
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    corners: _containers.RepeatedScalarFieldContainer[int]
    crosswalk_lanes: _containers.RepeatedScalarFieldContainer[int]
    id: int
    lane_segments: _containers.RepeatedScalarFieldContainer[int]
    road_segments: _containers.RepeatedScalarFieldContainer[int]
    signaled_intersection: int
    signed_intersection: int
    user_data: str
    def __init__(self, id: Optional[int] = ..., lane_segments: Optional[Iterable[int]] = ..., road_segments: Optional[Iterable[int]] = ..., signaled_intersection: Optional[int] = ..., user_data: Optional[str] = ..., corners: Optional[Iterable[int]] = ..., crosswalk_lanes: Optional[Iterable[int]] = ..., signed_intersection: Optional[int] = ...) -> None: ...

class LaneSegment(_message.Message):
    __slots__ = ["compass_angle", "direction", "id", "left_edge", "left_neighbor", "predecessors", "reference_line", "right_edge", "right_neighbor", "road", "successors", "turn_angle", "turn_type", "type", "user_data"]
    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class LaneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class TurnType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BACKWARD: LaneSegment.Direction
    BIDIRECTIONAL: LaneSegment.Direction
    BIKING: LaneSegment.LaneType
    COMPASS_ANGLE_FIELD_NUMBER: ClassVar[int]
    CROSSWALK: LaneSegment.LaneType
    DIRECTION_FIELD_NUMBER: ClassVar[int]
    DRIVABLE: LaneSegment.LaneType
    FORWARD: LaneSegment.Direction
    ID_FIELD_NUMBER: ClassVar[int]
    LEFT: LaneSegment.TurnType
    LEFT_EDGE_FIELD_NUMBER: ClassVar[int]
    LEFT_NEIGHBOR_FIELD_NUMBER: ClassVar[int]
    NON_DRIVABLE: LaneSegment.LaneType
    PARKING: LaneSegment.LaneType
    PARKING_AISLE: LaneSegment.LaneType
    PARKING_SPACE: LaneSegment.LaneType
    PREDECESSORS_FIELD_NUMBER: ClassVar[int]
    REFERENCE_LINE_FIELD_NUMBER: ClassVar[int]
    RESTRICTED: LaneSegment.LaneType
    RIGHT: LaneSegment.TurnType
    RIGHT_EDGE_FIELD_NUMBER: ClassVar[int]
    RIGHT_NEIGHBOR_FIELD_NUMBER: ClassVar[int]
    ROAD_FIELD_NUMBER: ClassVar[int]
    SHOULDER: LaneSegment.LaneType
    SIDEWALK: LaneSegment.LaneType
    SLIGHT_LEFT: LaneSegment.TurnType
    SLIGHT_RIGHT: LaneSegment.TurnType
    STRAIGHT: LaneSegment.TurnType
    SUCCESSORS_FIELD_NUMBER: ClassVar[int]
    TURN_ANGLE_FIELD_NUMBER: ClassVar[int]
    TURN_TYPE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    UNDEFINED_DIR: LaneSegment.Direction
    UNDEFINED_LANE: LaneSegment.LaneType
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    U_TURN: LaneSegment.TurnType
    compass_angle: float
    direction: LaneSegment.Direction
    id: int
    left_edge: int
    left_neighbor: int
    predecessors: _containers.RepeatedScalarFieldContainer[int]
    reference_line: int
    right_edge: int
    right_neighbor: int
    road: int
    successors: _containers.RepeatedScalarFieldContainer[int]
    turn_angle: float
    turn_type: LaneSegment.TurnType
    type: LaneSegment.LaneType
    user_data: str
    def __init__(self, id: Optional[int] = ..., type: Optional[Union[LaneSegment.LaneType, str]] = ..., direction: Optional[Union[LaneSegment.Direction, str]] = ..., road: Optional[int] = ..., left_edge: Optional[int] = ..., right_edge: Optional[int] = ..., reference_line: Optional[int] = ..., predecessors: Optional[Iterable[int]] = ..., successors: Optional[Iterable[int]] = ..., left_neighbor: Optional[int] = ..., right_neighbor: Optional[int] = ..., compass_angle: Optional[float] = ..., turn_angle: Optional[float] = ..., turn_type: Optional[Union[LaneSegment.TurnType, str]] = ..., user_data: Optional[str] = ...) -> None: ...

class Object(_message.Message):
    __slots__ = ["bounding_box", "exclusion_radius", "id", "orientation", "origin", "prop_data", "traffic_light_data", "traffic_sign_data", "user_data"]
    BOUNDING_BOX_FIELD_NUMBER: ClassVar[int]
    EXCLUSION_RADIUS_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    ORIENTATION_FIELD_NUMBER: ClassVar[int]
    ORIGIN_FIELD_NUMBER: ClassVar[int]
    PROP_DATA_FIELD_NUMBER: ClassVar[int]
    TRAFFIC_LIGHT_DATA_FIELD_NUMBER: ClassVar[int]
    TRAFFIC_SIGN_DATA_FIELD_NUMBER: ClassVar[int]
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    bounding_box: AABB
    exclusion_radius: float
    id: int
    orientation: Quaternion
    origin: Point_ENU
    prop_data: PropData
    traffic_light_data: TrafficLightData
    traffic_sign_data: TrafficSignData
    user_data: str
    def __init__(self, id: Optional[int] = ..., orientation: Optional[Union[Quaternion, Mapping]] = ..., origin: Optional[Union[Point_ENU, Mapping]] = ..., bounding_box: Optional[Union[AABB, Mapping]] = ..., traffic_sign_data: Optional[Union[TrafficSignData, Mapping]] = ..., traffic_light_data: Optional[Union[TrafficLightData, Mapping]] = ..., prop_data: Optional[Union[PropData, Mapping]] = ..., exclusion_radius: Optional[float] = ..., user_data: Optional[str] = ...) -> None: ...

class Phase(_message.Message):
    __slots__ = ["controlled_lanes", "id", "phase_timing"]
    CONTROLLED_LANES_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    PHASE_TIMING_FIELD_NUMBER: ClassVar[int]
    controlled_lanes: _containers.RepeatedScalarFieldContainer[int]
    id: int
    phase_timing: _containers.RepeatedCompositeFieldContainer[SignalOnset]
    def __init__(self, id: Optional[int] = ..., phase_timing: Optional[Iterable[Union[SignalOnset, Mapping]]] = ..., controlled_lanes: Optional[Iterable[int]] = ...) -> None: ...

class Point_ECEF(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...) -> None: ...

class Point_ENU(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...) -> None: ...

class Point_LLA(_message.Message):
    __slots__ = ["alt", "lat", "lon"]
    ALT_FIELD_NUMBER: ClassVar[int]
    LAT_FIELD_NUMBER: ClassVar[int]
    LON_FIELD_NUMBER: ClassVar[int]
    alt: float
    lat: float
    lon: float
    def __init__(self, lat: Optional[float] = ..., lon: Optional[float] = ..., alt: Optional[float] = ...) -> None: ...

class PropData(_message.Message):
    __slots__ = ["asset_name", "type"]
    class PropType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASSET_NAME_FIELD_NUMBER: ClassVar[int]
    BARRIER: PropData.PropType
    BUILDING: PropData.PropType
    HARDSCAPE: PropData.PropType
    OTHER: PropData.PropType
    POLE: PropData.PropType
    TERRAIN_NATURAL: PropData.PropType
    TYPE_FIELD_NUMBER: ClassVar[int]
    VEGETATION_HIGH: PropData.PropType
    VEGETATION_LOW: PropData.PropType
    VEHICLE: PropData.PropType
    asset_name: str
    type: PropData.PropType
    def __init__(self, type: Optional[Union[PropData.PropType, str]] = ..., asset_name: Optional[str] = ...) -> None: ...

class Quaternion(_message.Message):
    __slots__ = ["w", "x", "y", "z"]
    W_FIELD_NUMBER: ClassVar[int]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    w: float
    x: float
    y: float
    z: float
    def __init__(self, w: Optional[float] = ..., x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...) -> None: ...

class RoadMarking(_message.Message):
    __slots__ = ["color", "dash_length", "dash_separation", "edge_id", "id", "is_stopline", "type", "width"]
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BLUE: RoadMarking.Color
    BOTTS_DOTS: RoadMarking.Type
    COLOR_FIELD_NUMBER: ClassVar[int]
    DASHED: RoadMarking.Type
    DASHED_DASHED: RoadMarking.Type
    DASHED_SOLID: RoadMarking.Type
    DASH_LENGTH_FIELD_NUMBER: ClassVar[int]
    DASH_SEPARATION_FIELD_NUMBER: ClassVar[int]
    EDGE_ID_FIELD_NUMBER: ClassVar[int]
    GREEN: RoadMarking.Color
    ID_FIELD_NUMBER: ClassVar[int]
    IS_STOPLINE_FIELD_NUMBER: ClassVar[int]
    NO_PAINT: RoadMarking.Type
    RED: RoadMarking.Color
    SOLID: RoadMarking.Type
    SOLID_DASHED: RoadMarking.Type
    SOLID_SOLID: RoadMarking.Type
    TYPE_FIELD_NUMBER: ClassVar[int]
    WHITE: RoadMarking.Color
    WIDTH_FIELD_NUMBER: ClassVar[int]
    YELLOW: RoadMarking.Color
    color: RoadMarking.Color
    dash_length: float
    dash_separation: float
    edge_id: int
    id: int
    is_stopline: bool
    type: RoadMarking.Type
    width: float
    def __init__(self, id: Optional[int] = ..., edge_id: Optional[int] = ..., width: Optional[float] = ..., type: Optional[Union[RoadMarking.Type, str]] = ..., color: Optional[Union[RoadMarking.Color, str]] = ..., dash_length: Optional[float] = ..., dash_separation: Optional[float] = ..., is_stopline: bool = ...) -> None: ...

class RoadSegment(_message.Message):
    __slots__ = ["ground_type", "id", "junction_id", "lane_segments", "name", "predecessors", "reference_line", "speed_limit", "successors", "type", "user_data"]
    class GroundType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class RoadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BRIDGE: RoadSegment.GroundType
    DRIVEWAY: RoadSegment.RoadType
    DRIVEWAY_PARKING_ENTRY: RoadSegment.RoadType
    GROUND: RoadSegment.GroundType
    GROUND_TYPE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    JUNCTION_ID_FIELD_NUMBER: ClassVar[int]
    LANE_SEGMENTS_FIELD_NUMBER: ClassVar[int]
    MOTORWAY: RoadSegment.RoadType
    MOTORWAY_LINK: RoadSegment.RoadType
    NAME_FIELD_NUMBER: ClassVar[int]
    PARKING_AISLE: RoadSegment.RoadType
    PREDECESSORS_FIELD_NUMBER: ClassVar[int]
    PRIMARY: RoadSegment.RoadType
    PRIMARY_LINK: RoadSegment.RoadType
    REFERENCE_LINE_FIELD_NUMBER: ClassVar[int]
    RESIDENTIAL: RoadSegment.RoadType
    SECONDARY: RoadSegment.RoadType
    SECONDARY_LINK: RoadSegment.RoadType
    SERVICE: RoadSegment.RoadType
    SPEED_LIMIT_FIELD_NUMBER: ClassVar[int]
    SUCCESSORS_FIELD_NUMBER: ClassVar[int]
    TERTIARY: RoadSegment.RoadType
    TERTIARY_LINK: RoadSegment.RoadType
    TRUNK: RoadSegment.RoadType
    TRUNK_LINK: RoadSegment.RoadType
    TUNNEL: RoadSegment.GroundType
    TYPE_FIELD_NUMBER: ClassVar[int]
    UNCLASSIFIED: RoadSegment.RoadType
    USER_DATA_FIELD_NUMBER: ClassVar[int]
    ground_type: RoadSegment.GroundType
    id: int
    junction_id: int
    lane_segments: _containers.RepeatedScalarFieldContainer[int]
    name: str
    predecessors: _containers.RepeatedScalarFieldContainer[int]
    reference_line: int
    speed_limit: SpeedLimit
    successors: _containers.RepeatedScalarFieldContainer[int]
    type: RoadSegment.RoadType
    user_data: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., predecessors: Optional[Iterable[int]] = ..., successors: Optional[Iterable[int]] = ..., lane_segments: Optional[Iterable[int]] = ..., reference_line: Optional[int] = ..., type: Optional[Union[RoadSegment.RoadType, str]] = ..., ground_type: Optional[Union[RoadSegment.GroundType, str]] = ..., speed_limit: Optional[Union[SpeedLimit, Mapping]] = ..., junction_id: Optional[int] = ..., user_data: Optional[str] = ...) -> None: ...

class SignalOnset(_message.Message):
    __slots__ = ["logical_state", "onset", "signal_state"]
    class LogicalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class SignalState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    LOGICAL_STATE_FIELD_NUMBER: ClassVar[int]
    ONSET_FIELD_NUMBER: ClassVar[int]
    SIGNAL_STATE_FIELD_NUMBER: ClassVar[int]
    green: SignalOnset.SignalState
    green_flashing: SignalOnset.LogicalState
    green_solid: SignalOnset.LogicalState
    inactive: SignalOnset.LogicalState
    logical_state: SignalOnset.LogicalState
    onset: float
    red: SignalOnset.SignalState
    red_flashing: SignalOnset.LogicalState
    red_solid: SignalOnset.LogicalState
    signal_state: SignalOnset.SignalState
    yellow: SignalOnset.SignalState
    yellow_flashing: SignalOnset.LogicalState
    yellow_solid: SignalOnset.LogicalState
    def __init__(self, onset: Optional[float] = ..., signal_state: Optional[Union[SignalOnset.SignalState, str]] = ..., logical_state: Optional[Union[SignalOnset.LogicalState, str]] = ...) -> None: ...

class SignaledIntersection(_message.Message):
    __slots__ = ["cycle_time", "id", "junction", "phase_timings"]
    CYCLE_TIME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    JUNCTION_FIELD_NUMBER: ClassVar[int]
    PHASE_TIMINGS_FIELD_NUMBER: ClassVar[int]
    cycle_time: float
    id: int
    junction: int
    phase_timings: _containers.RepeatedCompositeFieldContainer[Phase]
    def __init__(self, id: Optional[int] = ..., junction: Optional[int] = ..., phase_timings: Optional[Iterable[Union[Phase, Mapping]]] = ..., cycle_time: Optional[float] = ...) -> None: ...

class SignedIntersection(_message.Message):
    __slots__ = ["id", "junction", "stop_sign_lane_ids", "yield_sign_lane_ids"]
    ID_FIELD_NUMBER: ClassVar[int]
    JUNCTION_FIELD_NUMBER: ClassVar[int]
    STOP_SIGN_LANE_IDS_FIELD_NUMBER: ClassVar[int]
    YIELD_SIGN_LANE_IDS_FIELD_NUMBER: ClassVar[int]
    id: int
    junction: int
    stop_sign_lane_ids: _containers.RepeatedScalarFieldContainer[int]
    yield_sign_lane_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, id: Optional[int] = ..., junction: Optional[int] = ..., stop_sign_lane_ids: Optional[Iterable[int]] = ..., yield_sign_lane_ids: Optional[Iterable[int]] = ...) -> None: ...

class SpeedLimit(_message.Message):
    __slots__ = ["speed", "units"]
    class SpeedUnits(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    KILOMETERS_PER_HOUR: SpeedLimit.SpeedUnits
    MILES_PER_HOUR: SpeedLimit.SpeedUnits
    SPEED_FIELD_NUMBER: ClassVar[int]
    UNITS_FIELD_NUMBER: ClassVar[int]
    speed: int
    units: SpeedLimit.SpeedUnits
    def __init__(self, speed: Optional[int] = ..., units: Optional[Union[SpeedLimit.SpeedUnits, str]] = ...) -> None: ...

class TrafficLightBulb(_message.Message):
    __slots__ = ["color", "is_flashing", "phase_id", "shape"]
    class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Shape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ARROW_DOWN: TrafficLightBulb.Shape
    ARROW_LEFT: TrafficLightBulb.Shape
    ARROW_LEFT_DIAGONAL: TrafficLightBulb.Shape
    ARROW_RIGHT: TrafficLightBulb.Shape
    ARROW_RIGHT_DIAGONAL: TrafficLightBulb.Shape
    ARROW_UP: TrafficLightBulb.Shape
    BICYCLE: TrafficLightBulb.Shape
    CIRCLE: TrafficLightBulb.Shape
    COLOR_FIELD_NUMBER: ClassVar[int]
    DONT_WALK: TrafficLightBulb.Shape
    GREEN: TrafficLightBulb.Color
    IS_FLASHING_FIELD_NUMBER: ClassVar[int]
    NUMBER: TrafficLightBulb.Shape
    PHASE_ID_FIELD_NUMBER: ClassVar[int]
    RED: TrafficLightBulb.Color
    SHAPE_FIELD_NUMBER: ClassVar[int]
    U_TURN: TrafficLightBulb.Shape
    WALK: TrafficLightBulb.Shape
    YELLOW: TrafficLightBulb.Color
    color: TrafficLightBulb.Color
    is_flashing: bool
    phase_id: int
    shape: TrafficLightBulb.Shape
    def __init__(self, shape: Optional[Union[TrafficLightBulb.Shape, str]] = ..., color: Optional[Union[TrafficLightBulb.Color, str]] = ..., phase_id: Optional[int] = ..., is_flashing: bool = ...) -> None: ...

class TrafficLightData(_message.Message):
    __slots__ = ["asset_name", "bulbs", "signaled_intersection_id"]
    ASSET_NAME_FIELD_NUMBER: ClassVar[int]
    BULBS_FIELD_NUMBER: ClassVar[int]
    SIGNALED_INTERSECTION_ID_FIELD_NUMBER: ClassVar[int]
    asset_name: str
    bulbs: _containers.RepeatedCompositeFieldContainer[TrafficLightBulb]
    signaled_intersection_id: int
    def __init__(self, signaled_intersection_id: Optional[int] = ..., bulbs: Optional[Iterable[Union[TrafficLightBulb, Mapping]]] = ..., asset_name: Optional[str] = ...) -> None: ...

class TrafficSignData(_message.Message):
    __slots__ = ["asset_name", "face_text", "face_value", "sign_code", "type"]
    class SignType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ASSET_NAME_FIELD_NUMBER: ClassVar[int]
    BICYCLE_FACILITIES: TrafficSignData.SignType
    CULTURAL_INTEREST_ACCOMMODATION_SERVICES: TrafficSignData.SignType
    CULTURAL_INTEREST_GENERAL_INFORMATION: TrafficSignData.SignType
    CULTURAL_INTEREST_LAND_RECREATION: TrafficSignData.SignType
    CULTURAL_INTEREST_TRAVELER_SERVICES: TrafficSignData.SignType
    CULTURAL_INTEREST_WATER_RECREATION: TrafficSignData.SignType
    CULTURAL_INTEREST_WINTER_RECREATION: TrafficSignData.SignType
    EMERGENCY_MANAGEMENT_CIVIL_DEFENSE: TrafficSignData.SignType
    FACE_TEXT_FIELD_NUMBER: ClassVar[int]
    FACE_VALUE_FIELD_NUMBER: ClassVar[int]
    GUIDE_BICYCLE: TrafficSignData.SignType
    GUIDE_CROSSOVER_FREEWAY_ENTRANCE: TrafficSignData.SignType
    GUIDE_DESTINATION: TrafficSignData.SignType
    GUIDE_DISTANCE: TrafficSignData.SignType
    GUIDE_EXPRESSWAY_AND_FREEWAY: TrafficSignData.SignType
    GUIDE_GENERAL_INFORMATION: TrafficSignData.SignType
    GUIDE_GENERAL_SERVICES: TrafficSignData.SignType
    GUIDE_PARKING: TrafficSignData.SignType
    GUIDE_RECREATIONAL: TrafficSignData.SignType
    GUIDE_RECREATIONAL_AND_CULTURAL_INTEREST: TrafficSignData.SignType
    GUIDE_REFERENCE_LOCATION_MILEPOSTS: TrafficSignData.SignType
    GUIDE_REST_AREA: TrafficSignData.SignType
    GUIDE_SCENIC: TrafficSignData.SignType
    GUIDE_STREET_NAME: TrafficSignData.SignType
    GUIDE_WEIGH_STATION: TrafficSignData.SignType
    GUIDE_WORK_ZONE_INFORMATION: TrafficSignData.SignType
    MARKER_ADVANCE_TURN_AUXILLARIES: TrafficSignData.SignType
    MARKER_ALTERNATIVE_ROUTE_SIGNS: TrafficSignData.SignType
    MARKER_CARDINAL_DIRECTIONAL_AUXILLARIES: TrafficSignData.SignType
    MARKER_DIRECTIONAL_ARROW_AUXILLARIES: TrafficSignData.SignType
    MARKER_DIRECTIONAL_ARROW_AUXILLARIES_BICYCLE: TrafficSignData.SignType
    MARKER_JUNCTION_SIGNS: TrafficSignData.SignType
    MARKER_ROUTE_MARKERS: TrafficSignData.SignType
    OBJECT_MARKER: TrafficSignData.SignType
    REGULATORY_MOVEMENT_REGULATION: TrafficSignData.SignType
    REGULATORY_ONE_WAY_DIVIDED_HIGHWAY_ROUNDABOUT: TrafficSignData.SignType
    REGULATORY_PARKING_PROHIBITION_EMERGENCY_RESTRICTION_RAIL: TrafficSignData.SignType
    REGULATORY_PARKING_REGULATION: TrafficSignData.SignType
    REGULATORY_PEDESTRIAN_BICYCLE_EQUESTRIAN: TrafficSignData.SignType
    REGULATORY_RAILROAD_AND_LIGHT_RAIL: TrafficSignData.SignType
    REGULATORY_ROAD_CLOSURE: TrafficSignData.SignType
    REGULATORY_SEATBELT_CRASH_CLEARANCE_HEADLIGHT_USE: TrafficSignData.SignType
    REGULATORY_SELECTIVE_EXCLUSION: TrafficSignData.SignType
    REGULATORY_SPEED_REGULATION: TrafficSignData.SignType
    REGULATORY_STOP_YIELD_PEDESTRIAN_CROSSING: TrafficSignData.SignType
    REGULATORY_TRAFFIC_SIGNAL: TrafficSignData.SignType
    REGULATORY_TRUCK_ROUTE: TrafficSignData.SignType
    REGULATORY_TURN_AND_LANE_USE: TrafficSignData.SignType
    REGULATORY_WEIGHT_LIMIT: TrafficSignData.SignType
    REGULATORY_WEIGH_STATION: TrafficSignData.SignType
    SCHOOL: TrafficSignData.SignType
    SIGN_CODE_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    WARNING_ADVANCE_TRAFFIC_CONTROL: TrafficSignData.SignType
    WARNING_ADVANCE_WARNING_CROSSING: TrafficSignData.SignType
    WARNING_ADVISORY_SPEED: TrafficSignData.SignType
    WARNING_BLASTING: TrafficSignData.SignType
    WARNING_DEAD_END_NO_OUTLET_NO_PASSING: TrafficSignData.SignType
    WARNING_DIVIDED_HIGHWAY: TrafficSignData.SignType
    WARNING_DOUBLE_REVERSE_CURVE: TrafficSignData.SignType
    WARNING_HILL: TrafficSignData.SignType
    WARNING_INTERSECTION: TrafficSignData.SignType
    WARNING_LANE_TRANSITION: TrafficSignData.SignType
    WARNING_LOW_CLEARANCE: TrafficSignData.SignType
    WARNING_MERGE_AND_LANE_TRANSITION: TrafficSignData.SignType
    WARNING_NO_TRAFFIC_SIGNS: TrafficSignData.SignType
    WARNING_PAVEMENT_CONDITION: TrafficSignData.SignType
    WARNING_PLAYGROUND: TrafficSignData.SignType
    WARNING_RAILROAD_AND_LIGHT_RAIL: TrafficSignData.SignType
    WARNING_ROAD_WORK: TrafficSignData.SignType
    WARNING_SLOW_TRAFFIC: TrafficSignData.SignType
    WARNING_SPEED_HUMP: TrafficSignData.SignType
    WARNING_SUPPLEMENTAL_PLAQUES: TrafficSignData.SignType
    WARNING_TURN_AND_CURVE: TrafficSignData.SignType
    WARNING_WIDTH_RESTRICTION: TrafficSignData.SignType
    WARNING_WORK_ZONE: TrafficSignData.SignType
    WARNING_YELLOW_TRAP: TrafficSignData.SignType
    asset_name: str
    face_text: str
    face_value: int
    sign_code: str
    type: TrafficSignData.SignType
    def __init__(self, type: Optional[Union[TrafficSignData.SignType, str]] = ..., sign_code: Optional[str] = ..., face_value: Optional[int] = ..., face_text: Optional[str] = ..., asset_name: Optional[str] = ...) -> None: ...

class UniversalMap(_message.Message):
    __slots__ = ["areas", "edges", "info", "junctions", "lane_segments", "objects", "road_markings", "road_segments", "signaled_intersections", "signed_intersections", "zone_grid"]
    class AreasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: Area
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[Area, Mapping]] = ...) -> None: ...
    class EdgesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: Edge
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[Edge, Mapping]] = ...) -> None: ...
    class JunctionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: Junction
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[Junction, Mapping]] = ...) -> None: ...
    class LaneSegmentsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: LaneSegment
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[LaneSegment, Mapping]] = ...) -> None: ...
    class ObjectsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: Object
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[Object, Mapping]] = ...) -> None: ...
    class RoadMarkingsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: RoadMarking
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[RoadMarking, Mapping]] = ...) -> None: ...
    class RoadSegmentsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: RoadSegment
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[RoadSegment, Mapping]] = ...) -> None: ...
    class SignaledIntersectionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: SignaledIntersection
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[SignaledIntersection, Mapping]] = ...) -> None: ...
    class SignedIntersectionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: int
        value: SignedIntersection
        def __init__(self, key: Optional[int] = ..., value: Optional[Union[SignedIntersection, Mapping]] = ...) -> None: ...
    AREAS_FIELD_NUMBER: ClassVar[int]
    EDGES_FIELD_NUMBER: ClassVar[int]
    INFO_FIELD_NUMBER: ClassVar[int]
    JUNCTIONS_FIELD_NUMBER: ClassVar[int]
    LANE_SEGMENTS_FIELD_NUMBER: ClassVar[int]
    OBJECTS_FIELD_NUMBER: ClassVar[int]
    ROAD_MARKINGS_FIELD_NUMBER: ClassVar[int]
    ROAD_SEGMENTS_FIELD_NUMBER: ClassVar[int]
    SIGNALED_INTERSECTIONS_FIELD_NUMBER: ClassVar[int]
    SIGNED_INTERSECTIONS_FIELD_NUMBER: ClassVar[int]
    ZONE_GRID_FIELD_NUMBER: ClassVar[int]
    areas: _containers.MessageMap[int, Area]
    edges: _containers.MessageMap[int, Edge]
    info: Info
    junctions: _containers.MessageMap[int, Junction]
    lane_segments: _containers.MessageMap[int, LaneSegment]
    objects: _containers.MessageMap[int, Object]
    road_markings: _containers.MessageMap[int, RoadMarking]
    road_segments: _containers.MessageMap[int, RoadSegment]
    signaled_intersections: _containers.MessageMap[int, SignaledIntersection]
    signed_intersections: _containers.MessageMap[int, SignedIntersection]
    zone_grid: ZoneGrid
    def __init__(self, info: Optional[Union[Info, Mapping]] = ..., road_segments: Optional[Mapping[int, RoadSegment]] = ..., lane_segments: Optional[Mapping[int, LaneSegment]] = ..., areas: Optional[Mapping[int, Area]] = ..., objects: Optional[Mapping[int, Object]] = ..., edges: Optional[Mapping[int, Edge]] = ..., junctions: Optional[Mapping[int, Junction]] = ..., road_markings: Optional[Mapping[int, RoadMarking]] = ..., signaled_intersections: Optional[Mapping[int, SignaledIntersection]] = ..., signed_intersections: Optional[Mapping[int, SignedIntersection]] = ..., zone_grid: Optional[Union[ZoneGrid, Mapping]] = ...) -> None: ...

class ZoneGrid(_message.Message):
    __slots__ = ["bound_NE", "bound_SW", "lat_samples", "lon_samples", "points"]
    class ZoneType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOUND_NE_FIELD_NUMBER: ClassVar[int]
    BOUND_SW_FIELD_NUMBER: ClassVar[int]
    BROWN: ZoneGrid.ZoneType
    COMMERCIAL: ZoneGrid.ZoneType
    GREEN: ZoneGrid.ZoneType
    INDUSTRIAL: ZoneGrid.ZoneType
    LAT_SAMPLES_FIELD_NUMBER: ClassVar[int]
    LON_SAMPLES_FIELD_NUMBER: ClassVar[int]
    PARKING: ZoneGrid.ZoneType
    POINTS_FIELD_NUMBER: ClassVar[int]
    RESIDENTIAL: ZoneGrid.ZoneType
    RETAIL: ZoneGrid.ZoneType
    UNCLASSIFIED: ZoneGrid.ZoneType
    WATER: ZoneGrid.ZoneType
    bound_NE: Point_ENU
    bound_SW: Point_ENU
    lat_samples: int
    lon_samples: int
    points: _containers.RepeatedScalarFieldContainer[ZoneGrid.ZoneType]
    def __init__(self, bound_NE: Optional[Union[Point_ENU, Mapping]] = ..., bound_SW: Optional[Union[Point_ENU, Mapping]] = ..., lat_samples: Optional[int] = ..., lon_samples: Optional[int] = ..., points: Optional[Iterable[Union[ZoneGrid.ZoneType, str]]] = ...) -> None: ...
