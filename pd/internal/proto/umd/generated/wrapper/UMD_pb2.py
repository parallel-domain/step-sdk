from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.umd.generated.python import UMD_pb2
from pd.internal.proto.umd.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.umd.generated.wrapper import UMD_pb2 as _UMD_pb2

@register_wrapper(proto_type=UMD_pb2.AABB)
class AABB(ProtoMessageClass):
    _proto_message = UMD_pb2.AABB

    def __init__(self, *, proto: Optional[UMD_pb2.AABB]=None, max: Optional[Point_ENU]=None, min: Optional[Point_ENU]=None):
        if proto is None:
            proto = UMD_pb2.AABB()
        self.proto = proto
        self._max = get_wrapper(proto_type=proto.max.__class__)(proto=proto.max)
        self._min = get_wrapper(proto_type=proto.min.__class__)(proto=proto.min)
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self) -> Point_ENU:
        return self._max

    @max.setter
    def max(self, value: Point_ENU):
        self.proto.max.CopyFrom(value.proto)
        
        self._max = value
        self._max._update_proto_references(self.proto.max)

    @property
    def min(self) -> Point_ENU:
        return self._min

    @min.setter
    def min(self, value: Point_ENU):
        self.proto.min.CopyFrom(value.proto)
        
        self._min = value
        self._min._update_proto_references(self.proto.min)

    def _update_proto_references(self, proto: UMD_pb2.AABB):
        self.proto = proto
        self._max._update_proto_references(proto.max)
        self._min._update_proto_references(proto.min)

@register_wrapper(proto_type=UMD_pb2.Area)
class Area(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.Area.AreaType)
    class AreaType(ProtoEnumClass):
        _proto_message = UMD_pb2.Area.AreaType
        BUILDING_APARTMENT: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_APARTMENT
        BUILDING_COMMERCIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_COMMERCIAL
        BUILDING_GARAGE: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_GARAGE
        BUILDING_GAS: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_GAS
        BUILDING_HOUSE: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_HOUSE
        BUILDING_INDUSTRIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_INDUSTRIAL
        BUILDING_OFFICE: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_OFFICE
        BUILDING_PARKING: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_PARKING
        BUILDING_RESIDENTIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_RESIDENTIAL
        BUILDING_RETAIL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_RETAIL
        BUILDING_SCHOOL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_SCHOOL
        BUILDING_UNCLASSIFIED: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_UNCLASSIFIED
        BUILDING_WAREHOUSE: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.BUILDING_WAREHOUSE
        CONSTRUCTION: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.CONSTRUCTION
        EMPTY_LOT: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.EMPTY_LOT
        PARK: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.PARK
        PARKING_LOT: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.PARKING_LOT
        POWER: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.POWER
        RAIL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.RAIL
        SPEEDBUMP: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.SPEEDBUMP
        YARD: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.YARD
        ZONE_BROWN: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_BROWN
        ZONE_COMMERCIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_COMMERCIAL
        ZONE_GREEN: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_GREEN
        ZONE_INDUSTRIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_INDUSTRIAL
        ZONE_RESIDENTIAL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_RESIDENTIAL
        ZONE_RETAIL: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_RETAIL
        ZONE_WATER: UMD_pb2.Area.AreaType = UMD_pb2.Area.AreaType.ZONE_WATER
    _proto_message = UMD_pb2.Area

    def __init__(self, *, proto: Optional[UMD_pb2.Area]=None, edges: Optional[List[int]]=None, floors: Optional[int]=None, height: Optional[float]=None, id: Optional[int]=None, type: Optional[Area.AreaType]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.Area()
        self.proto = proto
        self._edges = ProtoListWrapper(container=[int(v) for v in proto.edges], attr_name='edges', list_owner=self)
        if edges is not None:
            self.edges = edges
        if floors is not None:
            self.floors = floors
        if height is not None:
            self.height = height
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if user_data is not None:
            self.user_data = user_data

    @property
    def edges(self) -> List[int]:
        return self._edges

    @edges.setter
    def edges(self, value: List[int]):
        self._edges.clear()
        for v in value:
            self._edges.append(v)

    @property
    def floors(self) -> int:
        return self.proto.floors

    @floors.setter
    def floors(self, value: int):
        self.proto.floors = value

    @property
    def height(self) -> float:
        return self.proto.height

    @height.setter
    def height(self, value: float):
        self.proto.height = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Area):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.Edge)
class Edge(ProtoMessageClass):
    _proto_message = UMD_pb2.Edge

    def __init__(self, *, proto: Optional[UMD_pb2.Edge]=None, id: Optional[int]=None, open: Optional[bool]=None, points: Optional[List[Point_ENU]]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.Edge()
        self.proto = proto
        self._points = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.points], attr_name='points', list_owner=self)
        if id is not None:
            self.id = id
        if open is not None:
            self.open = open
        if points is not None:
            self.points = points
        if user_data is not None:
            self.user_data = user_data

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def open(self) -> bool:
        return self.proto.open

    @open.setter
    def open(self, value: bool):
        self.proto.open = value

    @property
    def points(self) -> List[Point_ENU]:
        return self._points

    @points.setter
    def points(self, value: List[Point_ENU]):
        self._points.clear()
        for v in value:
            self._points.append(v)

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Edge):
        self.proto = proto
        for i, v in enumerate(self.points):
            v._update_proto_references(self.proto.points[i])

@register_wrapper(proto_type=UMD_pb2.Info)
class Info(ProtoMessageClass):
    _proto_message = UMD_pb2.Info

    def __init__(self, *, proto: Optional[UMD_pb2.Info]=None, audit: Optional[str]=None, name: Optional[str]=None, origin: Optional[Point_LLA]=None):
        if proto is None:
            proto = UMD_pb2.Info()
        self.proto = proto
        self._origin = get_wrapper(proto_type=proto.origin.__class__)(proto=proto.origin)
        if audit is not None:
            self.audit = audit
        if name is not None:
            self.name = name
        if origin is not None:
            self.origin = origin

    @property
    def audit(self) -> str:
        return self.proto.audit

    @audit.setter
    def audit(self, value: str):
        self.proto.audit = value

    @property
    def name(self) -> str:
        return self.proto.name

    @name.setter
    def name(self, value: str):
        self.proto.name = value

    @property
    def origin(self) -> Point_LLA:
        return self._origin

    @origin.setter
    def origin(self, value: Point_LLA):
        self.proto.origin.CopyFrom(value.proto)
        
        self._origin = value
        self._origin._update_proto_references(self.proto.origin)

    def _update_proto_references(self, proto: UMD_pb2.Info):
        self.proto = proto
        self._origin._update_proto_references(proto.origin)

@register_wrapper(proto_type=UMD_pb2.Junction)
class Junction(ProtoMessageClass):
    _proto_message = UMD_pb2.Junction

    def __init__(self, *, proto: Optional[UMD_pb2.Junction]=None, corners: Optional[List[int]]=None, crosswalk_lanes: Optional[List[int]]=None, id: Optional[int]=None, lane_segments: Optional[List[int]]=None, road_segments: Optional[List[int]]=None, signaled_intersection: Optional[int]=None, signed_intersection: Optional[int]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.Junction()
        self.proto = proto
        self._corners = ProtoListWrapper(container=[int(v) for v in proto.corners], attr_name='corners', list_owner=self)
        self._crosswalk_lanes = ProtoListWrapper(container=[int(v) for v in proto.crosswalk_lanes], attr_name='crosswalk_lanes', list_owner=self)
        self._lane_segments = ProtoListWrapper(container=[int(v) for v in proto.lane_segments], attr_name='lane_segments', list_owner=self)
        self._road_segments = ProtoListWrapper(container=[int(v) for v in proto.road_segments], attr_name='road_segments', list_owner=self)
        if corners is not None:
            self.corners = corners
        if crosswalk_lanes is not None:
            self.crosswalk_lanes = crosswalk_lanes
        if id is not None:
            self.id = id
        if lane_segments is not None:
            self.lane_segments = lane_segments
        if road_segments is not None:
            self.road_segments = road_segments
        if signaled_intersection is not None:
            self.signaled_intersection = signaled_intersection
        if signed_intersection is not None:
            self.signed_intersection = signed_intersection
        if user_data is not None:
            self.user_data = user_data

    @property
    def corners(self) -> List[int]:
        return self._corners

    @corners.setter
    def corners(self, value: List[int]):
        self._corners.clear()
        for v in value:
            self._corners.append(v)

    @property
    def crosswalk_lanes(self) -> List[int]:
        return self._crosswalk_lanes

    @crosswalk_lanes.setter
    def crosswalk_lanes(self, value: List[int]):
        self._crosswalk_lanes.clear()
        for v in value:
            self._crosswalk_lanes.append(v)

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def lane_segments(self) -> List[int]:
        return self._lane_segments

    @lane_segments.setter
    def lane_segments(self, value: List[int]):
        self._lane_segments.clear()
        for v in value:
            self._lane_segments.append(v)

    @property
    def road_segments(self) -> List[int]:
        return self._road_segments

    @road_segments.setter
    def road_segments(self, value: List[int]):
        self._road_segments.clear()
        for v in value:
            self._road_segments.append(v)

    @property
    def signaled_intersection(self) -> int:
        return self.proto.signaled_intersection

    @signaled_intersection.setter
    def signaled_intersection(self, value: int):
        self.proto.signaled_intersection = value

    @property
    def signed_intersection(self) -> int:
        return self.proto.signed_intersection

    @signed_intersection.setter
    def signed_intersection(self, value: int):
        self.proto.signed_intersection = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Junction):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.LaneSegment)
class LaneSegment(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.LaneSegment.Direction)
    class Direction(ProtoEnumClass):
        _proto_message = UMD_pb2.LaneSegment.Direction
        BACKWARD: UMD_pb2.LaneSegment.Direction = UMD_pb2.LaneSegment.Direction.BACKWARD
        BIDIRECTIONAL: UMD_pb2.LaneSegment.Direction = UMD_pb2.LaneSegment.Direction.BIDIRECTIONAL
        FORWARD: UMD_pb2.LaneSegment.Direction = UMD_pb2.LaneSegment.Direction.FORWARD
        UNDEFINED_DIR: UMD_pb2.LaneSegment.Direction = UMD_pb2.LaneSegment.Direction.UNDEFINED_DIR

    @register_wrapper(proto_type=UMD_pb2.LaneSegment.LaneType)
    class LaneType(ProtoEnumClass):
        _proto_message = UMD_pb2.LaneSegment.LaneType
        PARKING_SPACE: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.PARKING_SPACE
        SIDEWALK: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.SIDEWALK
        BIKING: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.BIKING
        CROSSWALK: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.CROSSWALK
        DRIVABLE: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.DRIVABLE
        NON_DRIVABLE: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.NON_DRIVABLE
        RESTRICTED: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.RESTRICTED
        SHOULDER: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.SHOULDER
        UNDEFINED_LANE: UMD_pb2.LaneSegment.LaneType = UMD_pb2.LaneSegment.LaneType.UNDEFINED_LANE

    @register_wrapper(proto_type=UMD_pb2.LaneSegment.TurnType)
    class TurnType(ProtoEnumClass):
        _proto_message = UMD_pb2.LaneSegment.TurnType
        LEFT: UMD_pb2.LaneSegment.TurnType = UMD_pb2.LaneSegment.TurnType.LEFT
        RIGHT: UMD_pb2.LaneSegment.TurnType = UMD_pb2.LaneSegment.TurnType.RIGHT
        SLIGHT_LEFT: UMD_pb2.LaneSegment.TurnType = UMD_pb2.LaneSegment.TurnType.SLIGHT_LEFT
        SLIGHT_RIGHT: UMD_pb2.LaneSegment.TurnType = UMD_pb2.LaneSegment.TurnType.SLIGHT_RIGHT
        STRAIGHT: UMD_pb2.LaneSegment.TurnType = UMD_pb2.LaneSegment.TurnType.STRAIGHT
    _proto_message = UMD_pb2.LaneSegment

    def __init__(self, *, proto: Optional[UMD_pb2.LaneSegment]=None, compass_angle: Optional[float]=None, direction: Optional[LaneSegment.Direction]=None, id: Optional[int]=None, left_edge: Optional[int]=None, left_neighbor: Optional[int]=None, predecessors: Optional[List[int]]=None, reference_line: Optional[int]=None, right_edge: Optional[int]=None, right_neighbor: Optional[int]=None, road: Optional[int]=None, successors: Optional[List[int]]=None, turn_angle: Optional[float]=None, turn_type: Optional[LaneSegment.TurnType]=None, type: Optional[LaneSegment.LaneType]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.LaneSegment()
        self.proto = proto
        self._predecessors = ProtoListWrapper(container=[int(v) for v in proto.predecessors], attr_name='predecessors', list_owner=self)
        self._successors = ProtoListWrapper(container=[int(v) for v in proto.successors], attr_name='successors', list_owner=self)
        if compass_angle is not None:
            self.compass_angle = compass_angle
        if direction is not None:
            self.direction = direction
        if id is not None:
            self.id = id
        if left_edge is not None:
            self.left_edge = left_edge
        if left_neighbor is not None:
            self.left_neighbor = left_neighbor
        if predecessors is not None:
            self.predecessors = predecessors
        if reference_line is not None:
            self.reference_line = reference_line
        if right_edge is not None:
            self.right_edge = right_edge
        if right_neighbor is not None:
            self.right_neighbor = right_neighbor
        if road is not None:
            self.road = road
        if successors is not None:
            self.successors = successors
        if turn_angle is not None:
            self.turn_angle = turn_angle
        if turn_type is not None:
            self.turn_type = turn_type
        if type is not None:
            self.type = type
        if user_data is not None:
            self.user_data = user_data

    @property
    def compass_angle(self) -> float:
        return self.proto.compass_angle

    @compass_angle.setter
    def compass_angle(self, value: float):
        self.proto.compass_angle = value

    @property
    def direction(self) -> int:
        return self.proto.direction

    @direction.setter
    def direction(self, value: int):
        self.proto.direction = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def left_edge(self) -> int:
        return self.proto.left_edge

    @left_edge.setter
    def left_edge(self, value: int):
        self.proto.left_edge = value

    @property
    def left_neighbor(self) -> int:
        return self.proto.left_neighbor

    @left_neighbor.setter
    def left_neighbor(self, value: int):
        self.proto.left_neighbor = value

    @property
    def predecessors(self) -> List[int]:
        return self._predecessors

    @predecessors.setter
    def predecessors(self, value: List[int]):
        self._predecessors.clear()
        for v in value:
            self._predecessors.append(v)

    @property
    def reference_line(self) -> int:
        return self.proto.reference_line

    @reference_line.setter
    def reference_line(self, value: int):
        self.proto.reference_line = value

    @property
    def right_edge(self) -> int:
        return self.proto.right_edge

    @right_edge.setter
    def right_edge(self, value: int):
        self.proto.right_edge = value

    @property
    def right_neighbor(self) -> int:
        return self.proto.right_neighbor

    @right_neighbor.setter
    def right_neighbor(self, value: int):
        self.proto.right_neighbor = value

    @property
    def road(self) -> int:
        return self.proto.road

    @road.setter
    def road(self, value: int):
        self.proto.road = value

    @property
    def successors(self) -> List[int]:
        return self._successors

    @successors.setter
    def successors(self, value: List[int]):
        self._successors.clear()
        for v in value:
            self._successors.append(v)

    @property
    def turn_angle(self) -> float:
        return self.proto.turn_angle

    @turn_angle.setter
    def turn_angle(self, value: float):
        self.proto.turn_angle = value

    @property
    def turn_type(self) -> int:
        return self.proto.turn_type

    @turn_type.setter
    def turn_type(self, value: int):
        self.proto.turn_type = value

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.LaneSegment):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.Object)
class Object(ProtoMessageClass):
    _proto_message = UMD_pb2.Object

    def __init__(self, *, proto: Optional[UMD_pb2.Object]=None, bounding_box: Optional[AABB]=None, exclusion_radius: Optional[float]=None, id: Optional[int]=None, orientation: Optional[Quaternion]=None, origin: Optional[Point_ENU]=None, prop_data: Optional[PropData]=None, traffic_light_data: Optional[TrafficLightData]=None, traffic_sign_data: Optional[TrafficSignData]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.Object()
        self.proto = proto
        self._bounding_box = get_wrapper(proto_type=proto.bounding_box.__class__)(proto=proto.bounding_box)
        self._orientation = get_wrapper(proto_type=proto.orientation.__class__)(proto=proto.orientation)
        self._origin = get_wrapper(proto_type=proto.origin.__class__)(proto=proto.origin)
        self._prop_data = get_wrapper(proto_type=proto.prop_data.__class__)(proto=proto.prop_data)
        self._traffic_light_data = get_wrapper(proto_type=proto.traffic_light_data.__class__)(proto=proto.traffic_light_data)
        self._traffic_sign_data = get_wrapper(proto_type=proto.traffic_sign_data.__class__)(proto=proto.traffic_sign_data)
        if bounding_box is not None:
            self.bounding_box = bounding_box
        if exclusion_radius is not None:
            self.exclusion_radius = exclusion_radius
        if id is not None:
            self.id = id
        if orientation is not None:
            self.orientation = orientation
        if origin is not None:
            self.origin = origin
        if prop_data is not None:
            self.prop_data = prop_data
        if traffic_light_data is not None:
            self.traffic_light_data = traffic_light_data
        if traffic_sign_data is not None:
            self.traffic_sign_data = traffic_sign_data
        if user_data is not None:
            self.user_data = user_data

    @property
    def bounding_box(self) -> AABB:
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, value: AABB):
        self.proto.bounding_box.CopyFrom(value.proto)
        
        self._bounding_box = value
        self._bounding_box._update_proto_references(self.proto.bounding_box)

    @property
    def exclusion_radius(self) -> float:
        return self.proto.exclusion_radius

    @exclusion_radius.setter
    def exclusion_radius(self, value: float):
        self.proto.exclusion_radius = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def orientation(self) -> Quaternion:
        return self._orientation

    @orientation.setter
    def orientation(self, value: Quaternion):
        self.proto.orientation.CopyFrom(value.proto)
        
        self._orientation = value
        self._orientation._update_proto_references(self.proto.orientation)

    @property
    def origin(self) -> Point_ENU:
        return self._origin

    @origin.setter
    def origin(self, value: Point_ENU):
        self.proto.origin.CopyFrom(value.proto)
        
        self._origin = value
        self._origin._update_proto_references(self.proto.origin)

    @property
    def prop_data(self) -> PropData:
        return self._prop_data

    @prop_data.setter
    def prop_data(self, value: PropData):
        self.proto.prop_data.CopyFrom(value.proto)
        
        self._prop_data = value
        self._prop_data._update_proto_references(self.proto.prop_data)

    @property
    def traffic_light_data(self) -> TrafficLightData:
        return self._traffic_light_data

    @traffic_light_data.setter
    def traffic_light_data(self, value: TrafficLightData):
        self.proto.traffic_light_data.CopyFrom(value.proto)
        
        self._traffic_light_data = value
        self._traffic_light_data._update_proto_references(self.proto.traffic_light_data)

    @property
    def traffic_sign_data(self) -> TrafficSignData:
        return self._traffic_sign_data

    @traffic_sign_data.setter
    def traffic_sign_data(self, value: TrafficSignData):
        self.proto.traffic_sign_data.CopyFrom(value.proto)
        
        self._traffic_sign_data = value
        self._traffic_sign_data._update_proto_references(self.proto.traffic_sign_data)

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Object):
        self.proto = proto
        self._bounding_box._update_proto_references(proto.bounding_box)
        self._orientation._update_proto_references(proto.orientation)
        self._origin._update_proto_references(proto.origin)
        self._prop_data._update_proto_references(proto.prop_data)
        self._traffic_light_data._update_proto_references(proto.traffic_light_data)
        self._traffic_sign_data._update_proto_references(proto.traffic_sign_data)

@register_wrapper(proto_type=UMD_pb2.Phase)
class Phase(ProtoMessageClass):
    _proto_message = UMD_pb2.Phase

    def __init__(self, *, proto: Optional[UMD_pb2.Phase]=None, controlled_lanes: Optional[List[int]]=None, id: Optional[int]=None, phase_timing: Optional[List[SignalOnset]]=None):
        if proto is None:
            proto = UMD_pb2.Phase()
        self.proto = proto
        self._controlled_lanes = ProtoListWrapper(container=[int(v) for v in proto.controlled_lanes], attr_name='controlled_lanes', list_owner=self)
        self._phase_timing = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.phase_timing], attr_name='phase_timing', list_owner=self)
        if controlled_lanes is not None:
            self.controlled_lanes = controlled_lanes
        if id is not None:
            self.id = id
        if phase_timing is not None:
            self.phase_timing = phase_timing

    @property
    def controlled_lanes(self) -> List[int]:
        return self._controlled_lanes

    @controlled_lanes.setter
    def controlled_lanes(self, value: List[int]):
        self._controlled_lanes.clear()
        for v in value:
            self._controlled_lanes.append(v)

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def phase_timing(self) -> List[SignalOnset]:
        return self._phase_timing

    @phase_timing.setter
    def phase_timing(self, value: List[SignalOnset]):
        self._phase_timing.clear()
        for v in value:
            self._phase_timing.append(v)

    def _update_proto_references(self, proto: UMD_pb2.Phase):
        self.proto = proto
        for i, v in enumerate(self.phase_timing):
            v._update_proto_references(self.proto.phase_timing[i])

@register_wrapper(proto_type=UMD_pb2.Point_ECEF)
class Point_ECEF(ProtoMessageClass):
    _proto_message = UMD_pb2.Point_ECEF

    def __init__(self, *, proto: Optional[UMD_pb2.Point_ECEF]=None, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None):
        if proto is None:
            proto = UMD_pb2.Point_ECEF()
        self.proto = proto
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def x(self) -> float:
        return self.proto.x

    @x.setter
    def x(self, value: float):
        self.proto.x = value

    @property
    def y(self) -> float:
        return self.proto.y

    @y.setter
    def y(self, value: float):
        self.proto.y = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    def _update_proto_references(self, proto: UMD_pb2.Point_ECEF):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.Point_ENU)
class Point_ENU(ProtoMessageClass):
    _proto_message = UMD_pb2.Point_ENU

    def __init__(self, *, proto: Optional[UMD_pb2.Point_ENU]=None, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None):
        if proto is None:
            proto = UMD_pb2.Point_ENU()
        self.proto = proto
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def x(self) -> float:
        return self.proto.x

    @x.setter
    def x(self, value: float):
        self.proto.x = value

    @property
    def y(self) -> float:
        return self.proto.y

    @y.setter
    def y(self, value: float):
        self.proto.y = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    def _update_proto_references(self, proto: UMD_pb2.Point_ENU):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.Point_LLA)
class Point_LLA(ProtoMessageClass):
    _proto_message = UMD_pb2.Point_LLA

    def __init__(self, *, proto: Optional[UMD_pb2.Point_LLA]=None, alt: Optional[float]=None, lat: Optional[float]=None, lon: Optional[float]=None):
        if proto is None:
            proto = UMD_pb2.Point_LLA()
        self.proto = proto
        if alt is not None:
            self.alt = alt
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon

    @property
    def alt(self) -> float:
        return self.proto.alt

    @alt.setter
    def alt(self, value: float):
        self.proto.alt = value

    @property
    def lat(self) -> float:
        return self.proto.lat

    @lat.setter
    def lat(self, value: float):
        self.proto.lat = value

    @property
    def lon(self) -> float:
        return self.proto.lon

    @lon.setter
    def lon(self, value: float):
        self.proto.lon = value

    def _update_proto_references(self, proto: UMD_pb2.Point_LLA):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.PropData)
class PropData(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.PropData.PropType)
    class PropType(ProtoEnumClass):
        _proto_message = UMD_pb2.PropData.PropType
        BARRIER: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.BARRIER
        BUILDING: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.BUILDING
        HARDSCAPE: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.HARDSCAPE
        OTHER: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.OTHER
        POLE: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.POLE
        TERRAIN_NATURAL: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.TERRAIN_NATURAL
        VEGETATION_HIGH: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.VEGETATION_HIGH
        VEGETATION_LOW: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.VEGETATION_LOW
        VEHICLE: UMD_pb2.PropData.PropType = UMD_pb2.PropData.PropType.VEHICLE
    _proto_message = UMD_pb2.PropData

    def __init__(self, *, proto: Optional[UMD_pb2.PropData]=None, asset_name: Optional[str]=None, type: Optional[PropData.PropType]=None):
        if proto is None:
            proto = UMD_pb2.PropData()
        self.proto = proto
        if asset_name is not None:
            self.asset_name = asset_name
        if type is not None:
            self.type = type

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    def _update_proto_references(self, proto: UMD_pb2.PropData):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.Quaternion)
class Quaternion(ProtoMessageClass):
    _proto_message = UMD_pb2.Quaternion

    def __init__(self, *, proto: Optional[UMD_pb2.Quaternion]=None, w: Optional[float]=None, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None):
        if proto is None:
            proto = UMD_pb2.Quaternion()
        self.proto = proto
        if w is not None:
            self.w = w
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def w(self) -> float:
        return self.proto.w

    @w.setter
    def w(self, value: float):
        self.proto.w = value

    @property
    def x(self) -> float:
        return self.proto.x

    @x.setter
    def x(self, value: float):
        self.proto.x = value

    @property
    def y(self) -> float:
        return self.proto.y

    @y.setter
    def y(self, value: float):
        self.proto.y = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    def _update_proto_references(self, proto: UMD_pb2.Quaternion):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.RoadMarking)
class RoadMarking(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.RoadMarking.Color)
    class Color(ProtoEnumClass):
        _proto_message = UMD_pb2.RoadMarking.Color
        BLUE: UMD_pb2.RoadMarking.Color = UMD_pb2.RoadMarking.Color.BLUE
        WHITE: UMD_pb2.RoadMarking.Color = UMD_pb2.RoadMarking.Color.WHITE

    @register_wrapper(proto_type=UMD_pb2.RoadMarking.Type)
    class Type(ProtoEnumClass):
        _proto_message = UMD_pb2.RoadMarking.Type
        BOTTS_DOTS: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.BOTTS_DOTS
        DASHED: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.DASHED
        DASHED_DASHED: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.DASHED_DASHED
        DASHED_SOLID: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.DASHED_SOLID
        NO_PAINT: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.NO_PAINT
        SOLID: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.SOLID
        SOLID_DASHED: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.SOLID_DASHED
        SOLID_SOLID: UMD_pb2.RoadMarking.Type = UMD_pb2.RoadMarking.Type.SOLID_SOLID
    _proto_message = UMD_pb2.RoadMarking

    def __init__(self, *, proto: Optional[UMD_pb2.RoadMarking]=None, color: Optional[RoadMarking.Color]=None, dash_length: Optional[float]=None, dash_separation: Optional[float]=None, edge_id: Optional[int]=None, id: Optional[int]=None, is_stopline: Optional[bool]=None, type: Optional[RoadMarking.Type]=None, width: Optional[float]=None):
        if proto is None:
            proto = UMD_pb2.RoadMarking()
        self.proto = proto
        if color is not None:
            self.color = color
        if dash_length is not None:
            self.dash_length = dash_length
        if dash_separation is not None:
            self.dash_separation = dash_separation
        if edge_id is not None:
            self.edge_id = edge_id
        if id is not None:
            self.id = id
        if is_stopline is not None:
            self.is_stopline = is_stopline
        if type is not None:
            self.type = type
        if width is not None:
            self.width = width

    @property
    def color(self) -> int:
        return self.proto.color

    @color.setter
    def color(self, value: int):
        self.proto.color = value

    @property
    def dash_length(self) -> float:
        return self.proto.dash_length

    @dash_length.setter
    def dash_length(self, value: float):
        self.proto.dash_length = value

    @property
    def dash_separation(self) -> float:
        return self.proto.dash_separation

    @dash_separation.setter
    def dash_separation(self, value: float):
        self.proto.dash_separation = value

    @property
    def edge_id(self) -> int:
        return self.proto.edge_id

    @edge_id.setter
    def edge_id(self, value: int):
        self.proto.edge_id = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def is_stopline(self) -> bool:
        return self.proto.is_stopline

    @is_stopline.setter
    def is_stopline(self, value: bool):
        self.proto.is_stopline = value

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    @property
    def width(self) -> float:
        return self.proto.width

    @width.setter
    def width(self, value: float):
        self.proto.width = value

    def _update_proto_references(self, proto: UMD_pb2.RoadMarking):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.RoadSegment)
class RoadSegment(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.RoadSegment.GroundType)
    class GroundType(ProtoEnumClass):
        _proto_message = UMD_pb2.RoadSegment.GroundType
        BRIDGE: UMD_pb2.RoadSegment.GroundType = UMD_pb2.RoadSegment.GroundType.BRIDGE
        GROUND: UMD_pb2.RoadSegment.GroundType = UMD_pb2.RoadSegment.GroundType.GROUND
        TUNNEL: UMD_pb2.RoadSegment.GroundType = UMD_pb2.RoadSegment.GroundType.TUNNEL

    @register_wrapper(proto_type=UMD_pb2.RoadSegment.RoadType)
    class RoadType(ProtoEnumClass):
        _proto_message = UMD_pb2.RoadSegment.RoadType
        PARKING_AISLE: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.PARKING_AISLE
        DRIVEWAY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.DRIVEWAY
        DRIVEWAY_PARKING_ENTRY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.DRIVEWAY_PARKING_ENTRY
        MOTORWAY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.MOTORWAY
        MOTORWAY_LINK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.MOTORWAY_LINK
        PRIMARY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.PRIMARY
        PRIMARY_LINK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.PRIMARY_LINK
        SECONDARY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.SECONDARY
        SECONDARY_LINK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.SECONDARY_LINK
        SERVICE: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.SERVICE
        TERTIARY: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.TERTIARY
        TERTIARY_LINK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.TERTIARY_LINK
        TRUNK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.TRUNK
        TRUNK_LINK: UMD_pb2.RoadSegment.RoadType = UMD_pb2.RoadSegment.RoadType.TRUNK_LINK
    _proto_message = UMD_pb2.RoadSegment

    def __init__(self, *, proto: Optional[UMD_pb2.RoadSegment]=None, ground_type: Optional[RoadSegment.GroundType]=None, id: Optional[int]=None, junction_id: Optional[int]=None, lane_segments: Optional[List[int]]=None, name: Optional[str]=None, predecessors: Optional[List[int]]=None, reference_line: Optional[int]=None, speed_limit: Optional[SpeedLimit]=None, successors: Optional[List[int]]=None, type: Optional[RoadSegment.RoadType]=None, user_data: Optional[str]=None):
        if proto is None:
            proto = UMD_pb2.RoadSegment()
        self.proto = proto
        self._lane_segments = ProtoListWrapper(container=[int(v) for v in proto.lane_segments], attr_name='lane_segments', list_owner=self)
        self._predecessors = ProtoListWrapper(container=[int(v) for v in proto.predecessors], attr_name='predecessors', list_owner=self)
        self._speed_limit = get_wrapper(proto_type=proto.speed_limit.__class__)(proto=proto.speed_limit)
        self._successors = ProtoListWrapper(container=[int(v) for v in proto.successors], attr_name='successors', list_owner=self)
        if ground_type is not None:
            self.ground_type = ground_type
        if id is not None:
            self.id = id
        if junction_id is not None:
            self.junction_id = junction_id
        if lane_segments is not None:
            self.lane_segments = lane_segments
        if name is not None:
            self.name = name
        if predecessors is not None:
            self.predecessors = predecessors
        if reference_line is not None:
            self.reference_line = reference_line
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if successors is not None:
            self.successors = successors
        if type is not None:
            self.type = type
        if user_data is not None:
            self.user_data = user_data

    @property
    def ground_type(self) -> int:
        return self.proto.ground_type

    @ground_type.setter
    def ground_type(self, value: int):
        self.proto.ground_type = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def junction_id(self) -> int:
        return self.proto.junction_id

    @junction_id.setter
    def junction_id(self, value: int):
        self.proto.junction_id = value

    @property
    def lane_segments(self) -> List[int]:
        return self._lane_segments

    @lane_segments.setter
    def lane_segments(self, value: List[int]):
        self._lane_segments.clear()
        for v in value:
            self._lane_segments.append(v)

    @property
    def name(self) -> str:
        return self.proto.name

    @name.setter
    def name(self, value: str):
        self.proto.name = value

    @property
    def predecessors(self) -> List[int]:
        return self._predecessors

    @predecessors.setter
    def predecessors(self, value: List[int]):
        self._predecessors.clear()
        for v in value:
            self._predecessors.append(v)

    @property
    def reference_line(self) -> int:
        return self.proto.reference_line

    @reference_line.setter
    def reference_line(self, value: int):
        self.proto.reference_line = value

    @property
    def speed_limit(self) -> SpeedLimit:
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, value: SpeedLimit):
        self.proto.speed_limit.CopyFrom(value.proto)
        
        self._speed_limit = value
        self._speed_limit._update_proto_references(self.proto.speed_limit)

    @property
    def successors(self) -> List[int]:
        return self._successors

    @successors.setter
    def successors(self, value: List[int]):
        self._successors.clear()
        for v in value:
            self._successors.append(v)

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.RoadSegment):
        self.proto = proto
        self._speed_limit._update_proto_references(proto.speed_limit)

@register_wrapper(proto_type=UMD_pb2.SignalOnset)
class SignalOnset(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.SignalOnset.LogicalState)
    class LogicalState(ProtoEnumClass):
        _proto_message = UMD_pb2.SignalOnset.LogicalState

    @register_wrapper(proto_type=UMD_pb2.SignalOnset.SignalState)
    class SignalState(ProtoEnumClass):
        _proto_message = UMD_pb2.SignalOnset.SignalState
    _proto_message = UMD_pb2.SignalOnset

    def __init__(self, *, proto: Optional[UMD_pb2.SignalOnset]=None, green: Optional[SignalOnset.SignalState]=None, green_flashing: Optional[SignalOnset.LogicalState]=None, green_solid: Optional[SignalOnset.LogicalState]=None, inactive: Optional[SignalOnset.LogicalState]=None, logical_state: Optional[SignalOnset.LogicalState]=None, onset: Optional[float]=None, red: Optional[SignalOnset.SignalState]=None, red_flashing: Optional[SignalOnset.LogicalState]=None, red_solid: Optional[SignalOnset.LogicalState]=None, signal_state: Optional[SignalOnset.SignalState]=None, yellow: Optional[SignalOnset.SignalState]=None, yellow_flashing: Optional[SignalOnset.LogicalState]=None, yellow_solid: Optional[SignalOnset.LogicalState]=None):
        if proto is None:
            proto = UMD_pb2.SignalOnset()
        self.proto = proto
        if green is not None:
            self.green = green
        if green_flashing is not None:
            self.green_flashing = green_flashing
        if green_solid is not None:
            self.green_solid = green_solid
        if inactive is not None:
            self.inactive = inactive
        if logical_state is not None:
            self.logical_state = logical_state
        if onset is not None:
            self.onset = onset
        if red is not None:
            self.red = red
        if red_flashing is not None:
            self.red_flashing = red_flashing
        if red_solid is not None:
            self.red_solid = red_solid
        if signal_state is not None:
            self.signal_state = signal_state
        if yellow is not None:
            self.yellow = yellow
        if yellow_flashing is not None:
            self.yellow_flashing = yellow_flashing
        if yellow_solid is not None:
            self.yellow_solid = yellow_solid

    @property
    def green(self) -> int:
        return self.proto.green

    @green.setter
    def green(self, value: int):
        self.proto.green = value

    @property
    def green_flashing(self) -> int:
        return self.proto.green_flashing

    @green_flashing.setter
    def green_flashing(self, value: int):
        self.proto.green_flashing = value

    @property
    def green_solid(self) -> int:
        return self.proto.green_solid

    @green_solid.setter
    def green_solid(self, value: int):
        self.proto.green_solid = value

    @property
    def inactive(self) -> int:
        return self.proto.inactive

    @inactive.setter
    def inactive(self, value: int):
        self.proto.inactive = value

    @property
    def logical_state(self) -> int:
        return self.proto.logical_state

    @logical_state.setter
    def logical_state(self, value: int):
        self.proto.logical_state = value

    @property
    def onset(self) -> float:
        return self.proto.onset

    @onset.setter
    def onset(self, value: float):
        self.proto.onset = value

    @property
    def red(self) -> int:
        return self.proto.red

    @red.setter
    def red(self, value: int):
        self.proto.red = value

    @property
    def red_flashing(self) -> int:
        return self.proto.red_flashing

    @red_flashing.setter
    def red_flashing(self, value: int):
        self.proto.red_flashing = value

    @property
    def red_solid(self) -> int:
        return self.proto.red_solid

    @red_solid.setter
    def red_solid(self, value: int):
        self.proto.red_solid = value

    @property
    def signal_state(self) -> int:
        return self.proto.signal_state

    @signal_state.setter
    def signal_state(self, value: int):
        self.proto.signal_state = value

    @property
    def yellow(self) -> int:
        return self.proto.yellow

    @yellow.setter
    def yellow(self, value: int):
        self.proto.yellow = value

    @property
    def yellow_flashing(self) -> int:
        return self.proto.yellow_flashing

    @yellow_flashing.setter
    def yellow_flashing(self, value: int):
        self.proto.yellow_flashing = value

    @property
    def yellow_solid(self) -> int:
        return self.proto.yellow_solid

    @yellow_solid.setter
    def yellow_solid(self, value: int):
        self.proto.yellow_solid = value

    def _update_proto_references(self, proto: UMD_pb2.SignalOnset):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.SignaledIntersection)
class SignaledIntersection(ProtoMessageClass):
    _proto_message = UMD_pb2.SignaledIntersection

    def __init__(self, *, proto: Optional[UMD_pb2.SignaledIntersection]=None, cycle_time: Optional[float]=None, id: Optional[int]=None, junction: Optional[int]=None, phase_timings: Optional[List[Phase]]=None):
        if proto is None:
            proto = UMD_pb2.SignaledIntersection()
        self.proto = proto
        self._phase_timings = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.phase_timings], attr_name='phase_timings', list_owner=self)
        if cycle_time is not None:
            self.cycle_time = cycle_time
        if id is not None:
            self.id = id
        if junction is not None:
            self.junction = junction
        if phase_timings is not None:
            self.phase_timings = phase_timings

    @property
    def cycle_time(self) -> float:
        return self.proto.cycle_time

    @cycle_time.setter
    def cycle_time(self, value: float):
        self.proto.cycle_time = value

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def junction(self) -> int:
        return self.proto.junction

    @junction.setter
    def junction(self, value: int):
        self.proto.junction = value

    @property
    def phase_timings(self) -> List[Phase]:
        return self._phase_timings

    @phase_timings.setter
    def phase_timings(self, value: List[Phase]):
        self._phase_timings.clear()
        for v in value:
            self._phase_timings.append(v)

    def _update_proto_references(self, proto: UMD_pb2.SignaledIntersection):
        self.proto = proto
        for i, v in enumerate(self.phase_timings):
            v._update_proto_references(self.proto.phase_timings[i])

@register_wrapper(proto_type=UMD_pb2.SignedIntersection)
class SignedIntersection(ProtoMessageClass):
    _proto_message = UMD_pb2.SignedIntersection

    def __init__(self, *, proto: Optional[UMD_pb2.SignedIntersection]=None, id: Optional[int]=None, junction: Optional[int]=None, stop_sign_lane_ids: Optional[List[int]]=None, yield_sign_lane_ids: Optional[List[int]]=None):
        if proto is None:
            proto = UMD_pb2.SignedIntersection()
        self.proto = proto
        self._stop_sign_lane_ids = ProtoListWrapper(container=[int(v) for v in proto.stop_sign_lane_ids], attr_name='stop_sign_lane_ids', list_owner=self)
        self._yield_sign_lane_ids = ProtoListWrapper(container=[int(v) for v in proto.yield_sign_lane_ids], attr_name='yield_sign_lane_ids', list_owner=self)
        if id is not None:
            self.id = id
        if junction is not None:
            self.junction = junction
        if stop_sign_lane_ids is not None:
            self.stop_sign_lane_ids = stop_sign_lane_ids
        if yield_sign_lane_ids is not None:
            self.yield_sign_lane_ids = yield_sign_lane_ids

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def junction(self) -> int:
        return self.proto.junction

    @junction.setter
    def junction(self, value: int):
        self.proto.junction = value

    @property
    def stop_sign_lane_ids(self) -> List[int]:
        return self._stop_sign_lane_ids

    @stop_sign_lane_ids.setter
    def stop_sign_lane_ids(self, value: List[int]):
        self._stop_sign_lane_ids.clear()
        for v in value:
            self._stop_sign_lane_ids.append(v)

    @property
    def yield_sign_lane_ids(self) -> List[int]:
        return self._yield_sign_lane_ids

    @yield_sign_lane_ids.setter
    def yield_sign_lane_ids(self, value: List[int]):
        self._yield_sign_lane_ids.clear()
        for v in value:
            self._yield_sign_lane_ids.append(v)

    def _update_proto_references(self, proto: UMD_pb2.SignedIntersection):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.SpeedLimit)
class SpeedLimit(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.SpeedLimit.SpeedUnits)
    class SpeedUnits(ProtoEnumClass):
        _proto_message = UMD_pb2.SpeedLimit.SpeedUnits
        KILOMETERS_PER_HOUR: UMD_pb2.SpeedLimit.SpeedUnits = UMD_pb2.SpeedLimit.SpeedUnits.KILOMETERS_PER_HOUR
        MILES_PER_HOUR: UMD_pb2.SpeedLimit.SpeedUnits = UMD_pb2.SpeedLimit.SpeedUnits.MILES_PER_HOUR
    _proto_message = UMD_pb2.SpeedLimit

    def __init__(self, *, proto: Optional[UMD_pb2.SpeedLimit]=None, speed: Optional[int]=None, units: Optional[SpeedLimit.SpeedUnits]=None):
        if proto is None:
            proto = UMD_pb2.SpeedLimit()
        self.proto = proto
        if speed is not None:
            self.speed = speed
        if units is not None:
            self.units = units

    @property
    def speed(self) -> int:
        return self.proto.speed

    @speed.setter
    def speed(self, value: int):
        self.proto.speed = value

    @property
    def units(self) -> int:
        return self.proto.units

    @units.setter
    def units(self, value: int):
        self.proto.units = value

    def _update_proto_references(self, proto: UMD_pb2.SpeedLimit):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.TrafficLightBulb)
class TrafficLightBulb(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.TrafficLightBulb.Color)
    class Color(ProtoEnumClass):
        _proto_message = UMD_pb2.TrafficLightBulb.Color
        RED: UMD_pb2.TrafficLightBulb.Color = UMD_pb2.TrafficLightBulb.Color.RED
        YELLOW: UMD_pb2.TrafficLightBulb.Color = UMD_pb2.TrafficLightBulb.Color.YELLOW

    @register_wrapper(proto_type=UMD_pb2.TrafficLightBulb.Shape)
    class Shape(ProtoEnumClass):
        _proto_message = UMD_pb2.TrafficLightBulb.Shape
        U_TURN: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.U_TURN
        ARROW_DOWN: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_DOWN
        ARROW_LEFT: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_LEFT
        ARROW_LEFT_DIAGONAL: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_LEFT_DIAGONAL
        ARROW_RIGHT: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_RIGHT
        ARROW_RIGHT_DIAGONAL: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_RIGHT_DIAGONAL
        ARROW_UP: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.ARROW_UP
        BICYCLE: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.BICYCLE
        CIRCLE: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.CIRCLE
        DONT_WALK: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.DONT_WALK
        NUMBER: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.NUMBER
        WALK: UMD_pb2.TrafficLightBulb.Shape = UMD_pb2.TrafficLightBulb.Shape.WALK
    _proto_message = UMD_pb2.TrafficLightBulb

    def __init__(self, *, proto: Optional[UMD_pb2.TrafficLightBulb]=None, color: Optional[TrafficLightBulb.Color]=None, is_flashing: Optional[bool]=None, phase_id: Optional[int]=None, shape: Optional[TrafficLightBulb.Shape]=None):
        if proto is None:
            proto = UMD_pb2.TrafficLightBulb()
        self.proto = proto
        if color is not None:
            self.color = color
        if is_flashing is not None:
            self.is_flashing = is_flashing
        if phase_id is not None:
            self.phase_id = phase_id
        if shape is not None:
            self.shape = shape

    @property
    def color(self) -> int:
        return self.proto.color

    @color.setter
    def color(self, value: int):
        self.proto.color = value

    @property
    def is_flashing(self) -> bool:
        return self.proto.is_flashing

    @is_flashing.setter
    def is_flashing(self, value: bool):
        self.proto.is_flashing = value

    @property
    def phase_id(self) -> int:
        return self.proto.phase_id

    @phase_id.setter
    def phase_id(self, value: int):
        self.proto.phase_id = value

    @property
    def shape(self) -> int:
        return self.proto.shape

    @shape.setter
    def shape(self, value: int):
        self.proto.shape = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficLightBulb):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.TrafficLightData)
class TrafficLightData(ProtoMessageClass):
    _proto_message = UMD_pb2.TrafficLightData

    def __init__(self, *, proto: Optional[UMD_pb2.TrafficLightData]=None, asset_name: Optional[str]=None, bulbs: Optional[List[TrafficLightBulb]]=None, signaled_intersection_id: Optional[int]=None):
        if proto is None:
            proto = UMD_pb2.TrafficLightData()
        self.proto = proto
        self._bulbs = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.bulbs], attr_name='bulbs', list_owner=self)
        if asset_name is not None:
            self.asset_name = asset_name
        if bulbs is not None:
            self.bulbs = bulbs
        if signaled_intersection_id is not None:
            self.signaled_intersection_id = signaled_intersection_id

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    @property
    def bulbs(self) -> List[TrafficLightBulb]:
        return self._bulbs

    @bulbs.setter
    def bulbs(self, value: List[TrafficLightBulb]):
        self._bulbs.clear()
        for v in value:
            self._bulbs.append(v)

    @property
    def signaled_intersection_id(self) -> int:
        return self.proto.signaled_intersection_id

    @signaled_intersection_id.setter
    def signaled_intersection_id(self, value: int):
        self.proto.signaled_intersection_id = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficLightData):
        self.proto = proto
        for i, v in enumerate(self.bulbs):
            v._update_proto_references(self.proto.bulbs[i])

@register_wrapper(proto_type=UMD_pb2.TrafficSignData)
class TrafficSignData(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.TrafficSignData.SignType)
    class SignType(ProtoEnumClass):
        _proto_message = UMD_pb2.TrafficSignData.SignType
        BICYCLE_FACILITIES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.BICYCLE_FACILITIES
        CULTURAL_INTEREST_ACCOMMODATION_SERVICES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_ACCOMMODATION_SERVICES
        CULTURAL_INTEREST_GENERAL_INFORMATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_GENERAL_INFORMATION
        CULTURAL_INTEREST_LAND_RECREATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_LAND_RECREATION
        CULTURAL_INTEREST_TRAVELER_SERVICES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_TRAVELER_SERVICES
        CULTURAL_INTEREST_WATER_RECREATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_WATER_RECREATION
        CULTURAL_INTEREST_WINTER_RECREATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.CULTURAL_INTEREST_WINTER_RECREATION
        EMERGENCY_MANAGEMENT_CIVIL_DEFENSE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.EMERGENCY_MANAGEMENT_CIVIL_DEFENSE
        GUIDE_BICYCLE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_BICYCLE
        GUIDE_CROSSOVER_FREEWAY_ENTRANCE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_CROSSOVER_FREEWAY_ENTRANCE
        GUIDE_DESTINATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_DESTINATION
        GUIDE_DISTANCE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_DISTANCE
        GUIDE_EXPRESSWAY_AND_FREEWAY: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_EXPRESSWAY_AND_FREEWAY
        GUIDE_GENERAL_INFORMATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_GENERAL_INFORMATION
        GUIDE_GENERAL_SERVICES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_GENERAL_SERVICES
        GUIDE_PARKING: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_PARKING
        GUIDE_RECREATIONAL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_RECREATIONAL
        GUIDE_RECREATIONAL_AND_CULTURAL_INTEREST: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_RECREATIONAL_AND_CULTURAL_INTEREST
        GUIDE_REFERENCE_LOCATION_MILEPOSTS: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_REFERENCE_LOCATION_MILEPOSTS
        GUIDE_REST_AREA: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_REST_AREA
        GUIDE_SCENIC: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_SCENIC
        GUIDE_STREET_NAME: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_STREET_NAME
        GUIDE_WEIGH_STATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_WEIGH_STATION
        GUIDE_WORK_ZONE_INFORMATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.GUIDE_WORK_ZONE_INFORMATION
        MARKER_ADVANCE_TURN_AUXILLARIES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_ADVANCE_TURN_AUXILLARIES
        MARKER_ALTERNATIVE_ROUTE_SIGNS: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_ALTERNATIVE_ROUTE_SIGNS
        MARKER_CARDINAL_DIRECTIONAL_AUXILLARIES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_CARDINAL_DIRECTIONAL_AUXILLARIES
        MARKER_DIRECTIONAL_ARROW_AUXILLARIES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_DIRECTIONAL_ARROW_AUXILLARIES
        MARKER_DIRECTIONAL_ARROW_AUXILLARIES_BICYCLE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_DIRECTIONAL_ARROW_AUXILLARIES_BICYCLE
        MARKER_JUNCTION_SIGNS: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_JUNCTION_SIGNS
        MARKER_ROUTE_MARKERS: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.MARKER_ROUTE_MARKERS
        OBJECT_MARKER: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.OBJECT_MARKER
        REGULATORY_MOVEMENT_REGULATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_MOVEMENT_REGULATION
        REGULATORY_ONE_WAY_DIVIDED_HIGHWAY_ROUNDABOUT: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_ONE_WAY_DIVIDED_HIGHWAY_ROUNDABOUT
        REGULATORY_PARKING_PROHIBITION_EMERGENCY_RESTRICTION_RAIL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_PARKING_PROHIBITION_EMERGENCY_RESTRICTION_RAIL
        REGULATORY_PARKING_REGULATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_PARKING_REGULATION
        REGULATORY_PEDESTRIAN_BICYCLE_EQUESTRIAN: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_PEDESTRIAN_BICYCLE_EQUESTRIAN
        REGULATORY_RAILROAD_AND_LIGHT_RAIL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_RAILROAD_AND_LIGHT_RAIL
        REGULATORY_ROAD_CLOSURE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_ROAD_CLOSURE
        REGULATORY_SEATBELT_CRASH_CLEARANCE_HEADLIGHT_USE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_SEATBELT_CRASH_CLEARANCE_HEADLIGHT_USE
        REGULATORY_SELECTIVE_EXCLUSION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_SELECTIVE_EXCLUSION
        REGULATORY_SPEED_REGULATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_SPEED_REGULATION
        REGULATORY_STOP_YIELD_PEDESTRIAN_CROSSING: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_STOP_YIELD_PEDESTRIAN_CROSSING
        REGULATORY_TRAFFIC_SIGNAL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_TRAFFIC_SIGNAL
        REGULATORY_TRUCK_ROUTE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_TRUCK_ROUTE
        REGULATORY_TURN_AND_LANE_USE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_TURN_AND_LANE_USE
        REGULATORY_WEIGHT_LIMIT: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_WEIGHT_LIMIT
        REGULATORY_WEIGH_STATION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.REGULATORY_WEIGH_STATION
        SCHOOL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.SCHOOL
        WARNING_ADVANCE_TRAFFIC_CONTROL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_ADVANCE_TRAFFIC_CONTROL
        WARNING_ADVANCE_WARNING_CROSSING: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_ADVANCE_WARNING_CROSSING
        WARNING_ADVISORY_SPEED: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_ADVISORY_SPEED
        WARNING_BLASTING: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_BLASTING
        WARNING_DEAD_END_NO_OUTLET_NO_PASSING: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_DEAD_END_NO_OUTLET_NO_PASSING
        WARNING_DIVIDED_HIGHWAY: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_DIVIDED_HIGHWAY
        WARNING_DOUBLE_REVERSE_CURVE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_DOUBLE_REVERSE_CURVE
        WARNING_HILL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_HILL
        WARNING_INTERSECTION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_INTERSECTION
        WARNING_LANE_TRANSITION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_LANE_TRANSITION
        WARNING_LOW_CLEARANCE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_LOW_CLEARANCE
        WARNING_MERGE_AND_LANE_TRANSITION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_MERGE_AND_LANE_TRANSITION
        WARNING_NO_TRAFFIC_SIGNS: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_NO_TRAFFIC_SIGNS
        WARNING_PAVEMENT_CONDITION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_PAVEMENT_CONDITION
        WARNING_PLAYGROUND: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_PLAYGROUND
        WARNING_RAILROAD_AND_LIGHT_RAIL: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_RAILROAD_AND_LIGHT_RAIL
        WARNING_ROAD_WORK: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_ROAD_WORK
        WARNING_SLOW_TRAFFIC: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_SLOW_TRAFFIC
        WARNING_SPEED_HUMP: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_SPEED_HUMP
        WARNING_SUPPLEMENTAL_PLAQUES: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_SUPPLEMENTAL_PLAQUES
        WARNING_TURN_AND_CURVE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_TURN_AND_CURVE
        WARNING_WIDTH_RESTRICTION: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_WIDTH_RESTRICTION
        WARNING_WORK_ZONE: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_WORK_ZONE
        WARNING_YELLOW_TRAP: UMD_pb2.TrafficSignData.SignType = UMD_pb2.TrafficSignData.SignType.WARNING_YELLOW_TRAP
    _proto_message = UMD_pb2.TrafficSignData

    def __init__(self, *, proto: Optional[UMD_pb2.TrafficSignData]=None, asset_name: Optional[str]=None, face_text: Optional[str]=None, face_value: Optional[int]=None, sign_code: Optional[str]=None, type: Optional[TrafficSignData.SignType]=None):
        if proto is None:
            proto = UMD_pb2.TrafficSignData()
        self.proto = proto
        if asset_name is not None:
            self.asset_name = asset_name
        if face_text is not None:
            self.face_text = face_text
        if face_value is not None:
            self.face_value = face_value
        if sign_code is not None:
            self.sign_code = sign_code
        if type is not None:
            self.type = type

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    @property
    def face_text(self) -> str:
        return self.proto.face_text

    @face_text.setter
    def face_text(self, value: str):
        self.proto.face_text = value

    @property
    def face_value(self) -> int:
        return self.proto.face_value

    @face_value.setter
    def face_value(self, value: int):
        self.proto.face_value = value

    @property
    def sign_code(self) -> str:
        return self.proto.sign_code

    @sign_code.setter
    def sign_code(self, value: str):
        self.proto.sign_code = value

    @property
    def type(self) -> int:
        return self.proto.type

    @type.setter
    def type(self, value: int):
        self.proto.type = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficSignData):
        self.proto = proto

@register_wrapper(proto_type=UMD_pb2.UniversalMap)
class UniversalMap(ProtoMessageClass):
    _proto_message = UMD_pb2.UniversalMap

    def __init__(self, *, proto: Optional[UMD_pb2.UniversalMap]=None, areas: Optional[Dict[int, Area]]=None, edges: Optional[Dict[int, Edge]]=None, info: Optional[Info]=None, junctions: Optional[Dict[int, Junction]]=None, lane_segments: Optional[Dict[int, LaneSegment]]=None, objects: Optional[Dict[int, Object]]=None, road_markings: Optional[Dict[int, RoadMarking]]=None, road_segments: Optional[Dict[int, RoadSegment]]=None, signaled_intersections: Optional[Dict[int, SignaledIntersection]]=None, signed_intersections: Optional[Dict[int, SignedIntersection]]=None, zone_grid: Optional[ZoneGrid]=None):
        if proto is None:
            proto = UMD_pb2.UniversalMap()
        self.proto = proto
        self._areas = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.areas.items()}, attr_name='areas', dict_owner=self)
        self._edges = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.edges.items()}, attr_name='edges', dict_owner=self)
        self._info = get_wrapper(proto_type=proto.info.__class__)(proto=proto.info)
        self._junctions = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.junctions.items()}, attr_name='junctions', dict_owner=self)
        self._lane_segments = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.lane_segments.items()}, attr_name='lane_segments', dict_owner=self)
        self._objects = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.objects.items()}, attr_name='objects', dict_owner=self)
        self._road_markings = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.road_markings.items()}, attr_name='road_markings', dict_owner=self)
        self._road_segments = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.road_segments.items()}, attr_name='road_segments', dict_owner=self)
        self._signaled_intersections = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.signaled_intersections.items()}, attr_name='signaled_intersections', dict_owner=self)
        self._signed_intersections = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.signed_intersections.items()}, attr_name='signed_intersections', dict_owner=self)
        self._zone_grid = get_wrapper(proto_type=proto.zone_grid.__class__)(proto=proto.zone_grid)
        if areas is not None:
            self.areas = areas
        if edges is not None:
            self.edges = edges
        if info is not None:
            self.info = info
        if junctions is not None:
            self.junctions = junctions
        if lane_segments is not None:
            self.lane_segments = lane_segments
        if objects is not None:
            self.objects = objects
        if road_markings is not None:
            self.road_markings = road_markings
        if road_segments is not None:
            self.road_segments = road_segments
        if signaled_intersections is not None:
            self.signaled_intersections = signaled_intersections
        if signed_intersections is not None:
            self.signed_intersections = signed_intersections
        if zone_grid is not None:
            self.zone_grid = zone_grid

    @property
    def areas(self) -> Dict[int, Area]:
        return self._areas

    @areas.setter
    def areas(self, value: Dict[int, Area]):
        self._areas.clear()
        self._areas.update(value)

    @property
    def edges(self) -> Dict[int, Edge]:
        return self._edges

    @edges.setter
    def edges(self, value: Dict[int, Edge]):
        self._edges.clear()
        self._edges.update(value)

    @property
    def info(self) -> Info:
        return self._info

    @info.setter
    def info(self, value: Info):
        self.proto.info.CopyFrom(value.proto)
        
        self._info = value
        self._info._update_proto_references(self.proto.info)

    @property
    def junctions(self) -> Dict[int, Junction]:
        return self._junctions

    @junctions.setter
    def junctions(self, value: Dict[int, Junction]):
        self._junctions.clear()
        self._junctions.update(value)

    @property
    def lane_segments(self) -> Dict[int, LaneSegment]:
        return self._lane_segments

    @lane_segments.setter
    def lane_segments(self, value: Dict[int, LaneSegment]):
        self._lane_segments.clear()
        self._lane_segments.update(value)

    @property
    def objects(self) -> Dict[int, Object]:
        return self._objects

    @objects.setter
    def objects(self, value: Dict[int, Object]):
        self._objects.clear()
        self._objects.update(value)

    @property
    def road_markings(self) -> Dict[int, RoadMarking]:
        return self._road_markings

    @road_markings.setter
    def road_markings(self, value: Dict[int, RoadMarking]):
        self._road_markings.clear()
        self._road_markings.update(value)

    @property
    def road_segments(self) -> Dict[int, RoadSegment]:
        return self._road_segments

    @road_segments.setter
    def road_segments(self, value: Dict[int, RoadSegment]):
        self._road_segments.clear()
        self._road_segments.update(value)

    @property
    def signaled_intersections(self) -> Dict[int, SignaledIntersection]:
        return self._signaled_intersections

    @signaled_intersections.setter
    def signaled_intersections(self, value: Dict[int, SignaledIntersection]):
        self._signaled_intersections.clear()
        self._signaled_intersections.update(value)

    @property
    def signed_intersections(self) -> Dict[int, SignedIntersection]:
        return self._signed_intersections

    @signed_intersections.setter
    def signed_intersections(self, value: Dict[int, SignedIntersection]):
        self._signed_intersections.clear()
        self._signed_intersections.update(value)

    @property
    def zone_grid(self) -> ZoneGrid:
        return self._zone_grid

    @zone_grid.setter
    def zone_grid(self, value: ZoneGrid):
        self.proto.zone_grid.CopyFrom(value.proto)
        
        self._zone_grid = value
        self._zone_grid._update_proto_references(self.proto.zone_grid)

    def _update_proto_references(self, proto: UMD_pb2.UniversalMap):
        self.proto = proto
        for k, v in self.areas.items():
            v._update_proto_references(self.proto.areas[k])
        for k, v in self.edges.items():
            v._update_proto_references(self.proto.edges[k])
        self._info._update_proto_references(proto.info)
        for k, v in self.junctions.items():
            v._update_proto_references(self.proto.junctions[k])
        for k, v in self.lane_segments.items():
            v._update_proto_references(self.proto.lane_segments[k])
        for k, v in self.objects.items():
            v._update_proto_references(self.proto.objects[k])
        for k, v in self.road_markings.items():
            v._update_proto_references(self.proto.road_markings[k])
        for k, v in self.road_segments.items():
            v._update_proto_references(self.proto.road_segments[k])
        for k, v in self.signaled_intersections.items():
            v._update_proto_references(self.proto.signaled_intersections[k])
        for k, v in self.signed_intersections.items():
            v._update_proto_references(self.proto.signed_intersections[k])
        self._zone_grid._update_proto_references(proto.zone_grid)

@register_wrapper(proto_type=UMD_pb2.ZoneGrid)
class ZoneGrid(ProtoMessageClass):

    @register_wrapper(proto_type=UMD_pb2.ZoneGrid.ZoneType)
    class ZoneType(ProtoEnumClass):
        _proto_message = UMD_pb2.ZoneGrid.ZoneType
        UNCLASSIFIED: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.UNCLASSIFIED
        WATER: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.WATER
        PARKING: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.PARKING
        GREEN: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.GREEN
        RESIDENTIAL: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.RESIDENTIAL
        BROWN: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.BROWN
        COMMERCIAL: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.COMMERCIAL
        INDUSTRIAL: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.INDUSTRIAL
        RETAIL: UMD_pb2.ZoneGrid.ZoneType = UMD_pb2.ZoneGrid.ZoneType.RETAIL
    _proto_message = UMD_pb2.ZoneGrid

    def __init__(self, *, proto: Optional[UMD_pb2.ZoneGrid]=None, bound_NE: Optional[Point_ENU]=None, bound_SW: Optional[Point_ENU]=None, lat_samples: Optional[int]=None, lon_samples: Optional[int]=None, points: Optional[List[ZoneGrid.ZoneType]]=None):
        if proto is None:
            proto = UMD_pb2.ZoneGrid()
        self.proto = proto
        self._bound_NE = get_wrapper(proto_type=proto.bound_NE.__class__)(proto=proto.bound_NE)
        self._bound_SW = get_wrapper(proto_type=proto.bound_SW.__class__)(proto=proto.bound_SW)
        self._points = ProtoListWrapper(container=[int(v) for v in proto.points], attr_name='points', list_owner=self)
        if bound_NE is not None:
            self.bound_NE = bound_NE
        if bound_SW is not None:
            self.bound_SW = bound_SW
        if lat_samples is not None:
            self.lat_samples = lat_samples
        if lon_samples is not None:
            self.lon_samples = lon_samples
        if points is not None:
            self.points = points

    @property
    def bound_NE(self) -> Point_ENU:
        return self._bound_NE

    @bound_NE.setter
    def bound_NE(self, value: Point_ENU):
        self.proto.bound_NE.CopyFrom(value.proto)
        
        self._bound_NE = value
        self._bound_NE._update_proto_references(self.proto.bound_NE)

    @property
    def bound_SW(self) -> Point_ENU:
        return self._bound_SW

    @bound_SW.setter
    def bound_SW(self, value: Point_ENU):
        self.proto.bound_SW.CopyFrom(value.proto)
        
        self._bound_SW = value
        self._bound_SW._update_proto_references(self.proto.bound_SW)

    @property
    def lat_samples(self) -> int:
        return self.proto.lat_samples

    @lat_samples.setter
    def lat_samples(self, value: int):
        self.proto.lat_samples = value

    @property
    def lon_samples(self) -> int:
        return self.proto.lon_samples

    @lon_samples.setter
    def lon_samples(self, value: int):
        self.proto.lon_samples = value

    @property
    def points(self) -> int:
        return self._points

    @points.setter
    def points(self, value: int):
        self._points.clear()
        for v in value:
            self._points.append(v)

    def _update_proto_references(self, proto: UMD_pb2.ZoneGrid):
        self.proto = proto
        self._bound_NE._update_proto_references(proto.bound_NE)
        self._bound_SW._update_proto_references(proto.bound_SW)