from __future__ import annotations
from typing import List, Dict, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoEnumClass,
    ProtoListWrapper,
    ProtoDictWrapper
)
from ..python import UMD_pb2


@register_wrapper(proto_type=UMD_pb2.Point_LLA)
class Point_LLA(ProtoMessageClass):
    """
    Point defined by a latitude, longitude and altitude

    Args:
        lat: :attr:`lat`
        lon: :attr:`lon`
        alt: :attr:`alt`
    Attributes:
        lat:
        lon:
        alt:"""

    _proto_message = UMD_pb2.Point_LLA

    def __init__(
        self, *, proto: Optional[UMD_pb2.Point_LLA] = None, lat: float = None, lon: float = None, alt: float = None
    ):
        if proto is None:
            proto = UMD_pb2.Point_LLA()
        self.proto = proto
        if lat is not None:
            self.lat = lat
        if lon is not None:
            self.lon = lon
        if alt is not None:
            self.alt = alt

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

    @property
    def alt(self) -> float:
        return self.proto.alt

    @alt.setter
    def alt(self, value: float):
        self.proto.alt = value

    def _update_proto_references(self, proto: UMD_pb2.Point_LLA):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.Point_ECEF)
class Point_ECEF(ProtoMessageClass):
    """
    Point defined in Earth-Centered, Earth-Fixed coordinate system.

    Args:
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
    Attributes:
        x:
        y:
        z:"""

    _proto_message = UMD_pb2.Point_ECEF

    def __init__(
        self, *, proto: Optional[UMD_pb2.Point_ECEF] = None, x: float = None, y: float = None, z: float = None
    ):
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
    """
    3D Point in East, North Up coordinate system

    Args:
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
    Attributes:
        x:
        y:
        z:"""

    _proto_message = UMD_pb2.Point_ENU

    def __init__(self, *, proto: Optional[UMD_pb2.Point_ENU] = None, x: float = None, y: float = None, z: float = None):
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


@register_wrapper(proto_type=UMD_pb2.Quaternion)
class Quaternion(ProtoMessageClass):
    """
    Message to store the coefficients of a quaternion

    Args:
        w: :attr:`w`
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
    Attributes:
        w:
        x:
        y:
        z:"""

    _proto_message = UMD_pb2.Quaternion

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Quaternion] = None,
        w: float = None,
        x: float = None,
        y: float = None,
        z: float = None,
    ):
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


@register_wrapper(proto_type=UMD_pb2.AABB)
class AABB(ProtoMessageClass):
    """
    Axis aligned bounding box

    Args:
        min: :attr:`min`
        max: :attr:`max`
    Attributes:
        min: Point that defines the minimum corner of the axis aligned bounding box
        max: Point that defines the maximum corner of the axis aligned bounding box"""

    _proto_message = UMD_pb2.AABB

    def __init__(self, *, proto: Optional[UMD_pb2.AABB] = None, min: Point_ENU = None, max: Point_ENU = None):
        if proto is None:
            proto = UMD_pb2.AABB()
        self.proto = proto
        self._min = get_wrapper(proto_type=proto.min.__class__)(proto=proto.min)
        self._max = get_wrapper(proto_type=proto.max.__class__)(proto=proto.max)
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def min(self) -> Point_ENU:
        return self._min

    @min.setter
    def min(self, value: Point_ENU):
        self.proto.min.CopyFrom(value.proto)

        self._min = value
        self._min._update_proto_references(self.proto.min)

    @property
    def max(self) -> Point_ENU:
        return self._max

    @max.setter
    def max(self, value: Point_ENU):
        self.proto.max.CopyFrom(value.proto)

        self._max = value
        self._max._update_proto_references(self.proto.max)

    def _update_proto_references(self, proto: UMD_pb2.AABB):
        self.proto = proto
        self._min._update_proto_references(proto.min)
        self._max._update_proto_references(proto.max)


@register_wrapper(proto_type=UMD_pb2.Edge)
class Edge(ProtoMessageClass):
    """
    Message to store information about lines or edges in a UMD map.

    Args:
        id: :attr:`id`
        open: :attr:`open`
        points: :attr:`points`
        user_data: :attr:`user_data`
    Attributes:
        id: The integer ID of the edge.
        open: Boolean value to store whether an edge is closed (first point equals last) or not.
        points: List of points that define the edge.
        user_data: String to store optional data about the :obj:`Edge`."""

    _proto_message = UMD_pb2.Edge

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Edge] = None,
        id: int = None,
        open: bool = None,
        points: List[Point_ENU] = None,
        user_data: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.Edge()
        self.proto = proto
        self._points = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.points],
            attr_name="points",
            list_owner=self,
        )
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
    """
    Message to store map level information and metadata.

    Args:
        name: :attr:`name`
        origin: :attr:`origin`
        audit: :attr:`audit`
    Attributes:
        name: The name of the map
        origin: The latitude, longitude and altitude of the UMD map.
        audit:"""

    _proto_message = UMD_pb2.Info

    def __init__(
        self, *, proto: Optional[UMD_pb2.Info] = None, name: str = None, origin: Point_LLA = None, audit: str = None
    ):
        if proto is None:
            proto = UMD_pb2.Info()
        self.proto = proto
        self._origin = get_wrapper(proto_type=proto.origin.__class__)(proto=proto.origin)
        if name is not None:
            self.name = name
        if origin is not None:
            self.origin = origin
        if audit is not None:
            self.audit = audit

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

    @property
    def audit(self) -> str:
        return self.proto.audit

    @audit.setter
    def audit(self, value: str):
        self.proto.audit = value

    def _update_proto_references(self, proto: UMD_pb2.Info):
        self.proto = proto
        self._origin._update_proto_references(proto.origin)


@register_wrapper(proto_type=UMD_pb2.LaneSegment)
class LaneSegment(ProtoMessageClass):
    """
    A lane object within the UMD world

    Args:
        id: :attr:`id`
        type: :attr:`type`
        direction: :attr:`direction`
        road: :attr:`road`
        left_edge: :attr:`left_edge`
        right_edge: :attr:`right_edge`
        reference_line: :attr:`reference_line`
        predecessors: :attr:`predecessors`
        successors: :attr:`successors`
        left_neighbor: :attr:`left_neighbor`
        right_neighbor: :attr:`right_neighbor`
        compass_angle: :attr:`compass_angle`
        turn_angle: :attr:`turn_angle`
        turn_type: :attr:`turn_type`
        user_data: :attr:`user_data`
    Attributes:
        id: The integer ID of the :obj:`LaneSegment`
        type: The type of lane
        direction: The direction of the lane when traversed in the same order as the points in :attr:`left_edge`, :attr:`right_edge`
            and :attr:`reference_line`.
        road: The integer ID of the :obj:`RoadSegment` that a :obj:`LaneSegment` corresponds to
        left_edge: The integer ID of the :obj:`Edge` that defines the left edge of the :obj:`LaneSegment`
        right_edge: The integer ID of the :obj:`Edge` that defines the right edge of the :obj:`LaneSegment`
        reference_line: The integer ID of the :obj:`Edge` that defines the center reference line of the :obj:`LaneSegment`
        predecessors: The :obj:`LaneSegment` that connects to the beginning of the current :obj:`LaneSegment`
        successors: The :obj:`LaneSegment` that connects to the end of the current :obj:`LaneSegment`
        left_neighbor: The :obj:`LaneSegment` that is the left neighbor of the current :obj:`LaneSegment`. Left is defined relative
            to the forward direction of travel in the :obj:`LaneSegment`.
        right_neighbor: The :obj:`LaneSegment` that is the right neighbor of the current :obj:`LaneSegment`. Right is defined relative
            to the forward direction of travel in the :obj:`LaneSegment`.
        compass_angle: The angle between the direction of the :obj:`LaneSegment` and North
        turn_angle: Angle between the incoming and outgoing directions of the :obj:`LaneSegment` if the :obj:`LaneSegment` is a turn
            lane
        turn_type: The type of turn that the :obj:`LaneSegment` corresponds to if :obj:`LaneSegment` is a turn lane.
        user_data: Optional information about the :obj:`LaneSegment`"""

    class LaneType(ProtoEnumClass):
        """All possible lane types"""

        UNDEFINED_LANE = 0
        DRIVABLE = 1
        NON_DRIVABLE = 2
        PARKING = 3
        SHOULDER = 4
        BIKING = 5
        CROSSWALK = 6
        RESTRICTED = 7
        PARKING_AISLE = 8
        PARKING_SPACE = 9
        SIDEWALK = 10

    class Direction(ProtoEnumClass):
        """All possible directions of a lane"""

        UNDEFINED_DIR = 0
        FORWARD = 1
        BACKWARD = 2
        BIDIRECTIONAL = 3

    class TurnType(ProtoEnumClass):
        """All possible turn types"""

        STRAIGHT = 0
        LEFT = 1
        RIGHT = 2
        SLIGHT_LEFT = 3
        SLIGHT_RIGHT = 4
        U_TURN = 5

    _proto_message = UMD_pb2.LaneSegment

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.LaneSegment] = None,
        id: int = None,
        type: LaneSegment.LaneType = None,
        direction: LaneSegment.Direction = None,
        road: int = None,
        left_edge: int = None,
        right_edge: int = None,
        reference_line: int = None,
        predecessors: List[int] = None,
        successors: List[int] = None,
        left_neighbor: int = None,
        right_neighbor: int = None,
        compass_angle: float = None,
        turn_angle: float = None,
        turn_type: LaneSegment.TurnType = None,
        user_data: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.LaneSegment()
        self.proto = proto
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if direction is not None:
            self.direction = direction
        if road is not None:
            self.road = road
        if left_edge is not None:
            self.left_edge = left_edge
        if right_edge is not None:
            self.right_edge = right_edge
        if reference_line is not None:
            self.reference_line = reference_line
        self._predecessors = ProtoListWrapper(
            container=[int(v) for v in proto.predecessors], attr_name="predecessors", list_owner=self
        )
        if predecessors is not None:
            self.predecessors = predecessors
        self._successors = ProtoListWrapper(
            container=[int(v) for v in proto.successors], attr_name="successors", list_owner=self
        )
        if successors is not None:
            self.successors = successors
        if left_neighbor is not None:
            self.left_neighbor = left_neighbor
        if right_neighbor is not None:
            self.right_neighbor = right_neighbor
        if compass_angle is not None:
            self.compass_angle = compass_angle
        if turn_angle is not None:
            self.turn_angle = turn_angle
        if turn_type is not None:
            self.turn_type = turn_type
        if user_data is not None:
            self.user_data = user_data

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def type(self) -> LaneSegment.LaneType:
        return self.proto.type

    @type.setter
    def type(self, value: LaneSegment.LaneType):
        self.proto.type = value

    @property
    def direction(self) -> LaneSegment.Direction:
        return self.proto.direction

    @direction.setter
    def direction(self, value: LaneSegment.Direction):
        self.proto.direction = value

    @property
    def road(self) -> int:
        return self.proto.road

    @road.setter
    def road(self, value: int):
        self.proto.road = value

    @property
    def left_edge(self) -> int:
        return self.proto.left_edge

    @left_edge.setter
    def left_edge(self, value: int):
        self.proto.left_edge = value

    @property
    def right_edge(self) -> int:
        return self.proto.right_edge

    @right_edge.setter
    def right_edge(self, value: int):
        self.proto.right_edge = value

    @property
    def reference_line(self) -> int:
        return self.proto.reference_line

    @reference_line.setter
    def reference_line(self, value: int):
        self.proto.reference_line = value

    @property
    def predecessors(self) -> List[int]:
        return self._predecessors

    @predecessors.setter
    def predecessors(self, value: List[int]):
        self._predecessors.clear()
        for v in value:
            self._predecessors.append(v)

    @property
    def successors(self) -> List[int]:
        return self._successors

    @successors.setter
    def successors(self, value: List[int]):
        self._successors.clear()
        for v in value:
            self._successors.append(v)

    @property
    def left_neighbor(self) -> int:
        return self.proto.left_neighbor

    @left_neighbor.setter
    def left_neighbor(self, value: int):
        self.proto.left_neighbor = value

    @property
    def right_neighbor(self) -> int:
        return self.proto.right_neighbor

    @right_neighbor.setter
    def right_neighbor(self, value: int):
        self.proto.right_neighbor = value

    @property
    def compass_angle(self) -> float:
        return self.proto.compass_angle

    @compass_angle.setter
    def compass_angle(self, value: float):
        self.proto.compass_angle = value

    @property
    def turn_angle(self) -> float:
        return self.proto.turn_angle

    @turn_angle.setter
    def turn_angle(self, value: float):
        self.proto.turn_angle = value

    @property
    def turn_type(self) -> LaneSegment.TurnType:
        return self.proto.turn_type

    @turn_type.setter
    def turn_type(self, value: LaneSegment.TurnType):
        self.proto.turn_type = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.LaneSegment):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.RoadSegment)
class RoadSegment(ProtoMessageClass):
    """
    A road object within the UMD world

    Args:
        id: :attr:`id`
        name: :attr:`name`
        predecessors: :attr:`predecessors`
        successors: :attr:`successors`
        lane_segments: :attr:`lane_segments`
        reference_line: :attr:`reference_line`
        type: :attr:`type`
        ground_type: :attr:`ground_type`
        speed_limit: :attr:`speed_limit`
        junction_id: :attr:`junction_id`
        user_data: :attr:`user_data`
    Attributes:
        id: The integer ID of the :obj:`RoadSegment`
        name: The name of the :obj:`RoadSegment`
        predecessors: The integer ID of the :obj:`RoadSegment` that connects to the beginning of the current :obj:`RoadSegment`
        successors: The integer ID of the :obj:`RoadSegment` that connects to the edn of the current :obj:`RoadSegment`
        lane_segments: The integer ID of the :obj:`LaneSegment` that make up this :obj:`RoadSegment`
        reference_line: The integer ID of the :obj:`Edge` that defines the center reference line of the :obj:`RoadSegment`
        type: The type of the current :obj:`RoadSegment`
        ground_type: The ground type on which the :obj:`RoadSegment` exists
        speed_limit: The speed limit of the :obj:`RoadSegment`
        junction_id: The integer ID of the junction that exists on the road if the :obj:`RoadSegment` contains a :obj:`Junction`
        user_data: Optional information about the :obj:`RoadSegment`"""

    class RoadType(ProtoEnumClass):
        """All possible road types"""

        MOTORWAY = 0
        TRUNK = 1
        PRIMARY = 2
        SECONDARY = 3
        TERTIARY = 4
        UNCLASSIFIED = 5
        RESIDENTIAL = 6
        MOTORWAY_LINK = 7
        TRUNK_LINK = 8
        PRIMARY_LINK = 9
        SECONDARY_LINK = 10
        TERTIARY_LINK = 11
        SERVICE = 12
        DRIVEWAY = 13
        PARKING_AISLE = 14
        DRIVEWAY_PARKING_ENTRY = 15

    class GroundType(ProtoEnumClass):
        """All possible ground types that an :obj:`RoadSegment` can exist on"""

        GROUND = 0
        BRIDGE = 1
        TUNNEL = 2

    _proto_message = UMD_pb2.RoadSegment

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.RoadSegment] = None,
        id: int = None,
        name: str = None,
        predecessors: List[int] = None,
        successors: List[int] = None,
        lane_segments: List[int] = None,
        reference_line: int = None,
        type: RoadSegment.RoadType = None,
        ground_type: RoadSegment.GroundType = None,
        speed_limit: SpeedLimit = None,
        junction_id: int = None,
        user_data: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.RoadSegment()
        self.proto = proto
        self._speed_limit = get_wrapper(proto_type=proto.speed_limit.__class__)(proto=proto.speed_limit)
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self._predecessors = ProtoListWrapper(
            container=[int(v) for v in proto.predecessors], attr_name="predecessors", list_owner=self
        )
        if predecessors is not None:
            self.predecessors = predecessors
        self._successors = ProtoListWrapper(
            container=[int(v) for v in proto.successors], attr_name="successors", list_owner=self
        )
        if successors is not None:
            self.successors = successors
        self._lane_segments = ProtoListWrapper(
            container=[int(v) for v in proto.lane_segments], attr_name="lane_segments", list_owner=self
        )
        if lane_segments is not None:
            self.lane_segments = lane_segments
        if reference_line is not None:
            self.reference_line = reference_line
        if type is not None:
            self.type = type
        if ground_type is not None:
            self.ground_type = ground_type
        if speed_limit is not None:
            self.speed_limit = speed_limit
        if junction_id is not None:
            self.junction_id = junction_id
        if user_data is not None:
            self.user_data = user_data

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

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
    def successors(self) -> List[int]:
        return self._successors

    @successors.setter
    def successors(self, value: List[int]):
        self._successors.clear()
        for v in value:
            self._successors.append(v)

    @property
    def lane_segments(self) -> List[int]:
        return self._lane_segments

    @lane_segments.setter
    def lane_segments(self, value: List[int]):
        self._lane_segments.clear()
        for v in value:
            self._lane_segments.append(v)

    @property
    def reference_line(self) -> int:
        return self.proto.reference_line

    @reference_line.setter
    def reference_line(self, value: int):
        self.proto.reference_line = value

    @property
    def type(self) -> RoadSegment.RoadType:
        return self.proto.type

    @type.setter
    def type(self, value: RoadSegment.RoadType):
        self.proto.type = value

    @property
    def ground_type(self) -> RoadSegment.GroundType:
        return self.proto.ground_type

    @ground_type.setter
    def ground_type(self, value: RoadSegment.GroundType):
        self.proto.ground_type = value

    @property
    def speed_limit(self) -> SpeedLimit:
        return self._speed_limit

    @speed_limit.setter
    def speed_limit(self, value: SpeedLimit):
        self.proto.speed_limit.CopyFrom(value.proto)

        self._speed_limit = value
        self._speed_limit._update_proto_references(self.proto.speed_limit)

    @property
    def junction_id(self) -> int:
        return self.proto.junction_id

    @junction_id.setter
    def junction_id(self, value: int):
        self.proto.junction_id = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.RoadSegment):
        self.proto = proto
        self._speed_limit._update_proto_references(proto.speed_limit)


@register_wrapper(proto_type=UMD_pb2.SpeedLimit)
class SpeedLimit(ProtoMessageClass):
    """
    Defines the speed limit of a :obj:`RoadSegment`

    Args:
        speed: :attr:`speed`
        units: :attr:`units`
    Attributes:
        speed: The speed limit in units defined by :attr:`SpeedUnits`
        units: The units that the :attr:`speed` is in"""

    class SpeedUnits(ProtoEnumClass):
        """All possible types for units of the speed limit"""

        MILES_PER_HOUR = 0
        KILOMETERS_PER_HOUR = 1

    _proto_message = UMD_pb2.SpeedLimit

    def __init__(
        self, *, proto: Optional[UMD_pb2.SpeedLimit] = None, speed: int = None, units: SpeedLimit.SpeedUnits = None
    ):
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
    def units(self) -> SpeedLimit.SpeedUnits:
        return self.proto.units

    @units.setter
    def units(self, value: SpeedLimit.SpeedUnits):
        self.proto.units = value

    def _update_proto_references(self, proto: UMD_pb2.SpeedLimit):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.Area)
class Area(ProtoMessageClass):
    """
    An area of the UMD map

    Args:
        id: :attr:`id`
        type: :attr:`type`
        edges: :attr:`edges`
        height: :attr:`height`
        floors: :attr:`floors`
        user_data: :attr:`user_data`
    Attributes:
        id: The id of the :obj:`Area`
        type: The type of the :obj:`Area`
        edges: The :obj:`Edge` that defines the boundary of the :obj:`Area`. Can be more than one.
        height: The height of the area in meters. Used for areas that define buildings.
        floors: The number of floors in an area when the :obj:`Area` defines a building.
        user_data: Optional information about an :obj:`Area`"""

    class AreaType(ProtoEnumClass):
        """All possible types that an :obj:`Area` can be"""

        BUILDING_COMMERCIAL = 0
        BUILDING_RESIDENTIAL = 1
        BUILDING_INDUSTRIAL = 2
        BUILDING_HOUSE = 3
        BUILDING_APARTMENT = 8
        BUILDING_GARAGE = 9
        BUILDING_GAS = 10
        BUILDING_PARKING = 11
        BUILDING_OFFICE = 12
        BUILDING_RETAIL = 13
        BUILDING_SCHOOL = 14
        BUILDING_WAREHOUSE = 15
        BUILDING_UNCLASSIFIED = 29
        EMPTY_LOT = 7
        PARKING_LOT = 4
        PARKING_SPACE = 5
        PARK = 6
        POWER = 18
        RAIL = 19
        SIDEWALK = 17
        UNCLASSIFIED = 16
        WATER = 20
        ZONE_BROWN = 21
        ZONE_COMMERCIAL = 22
        ZONE_GREEN = 23
        ZONE_INDUSTRIAL = 24
        ZONE_RESIDENTIAL = 25
        ZONE_RETAIL = 26
        ZONE_WATER = 27
        SPEEDBUMP = 28
        CONSTRUCTION = 30
        YARD = 31

    _proto_message = UMD_pb2.Area

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Area] = None,
        id: int = None,
        type: Area.AreaType = None,
        edges: List[int] = None,
        height: float = None,
        floors: int = None,
        user_data: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.Area()
        self.proto = proto
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        self._edges = ProtoListWrapper(container=[int(v) for v in proto.edges], attr_name="edges", list_owner=self)
        if edges is not None:
            self.edges = edges
        if height is not None:
            self.height = height
        if floors is not None:
            self.floors = floors
        if user_data is not None:
            self.user_data = user_data

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def type(self) -> Area.AreaType:
        return self.proto.type

    @type.setter
    def type(self, value: Area.AreaType):
        self.proto.type = value

    @property
    def edges(self) -> List[int]:
        return self._edges

    @edges.setter
    def edges(self, value: List[int]):
        self._edges.clear()
        for v in value:
            self._edges.append(v)

    @property
    def height(self) -> float:
        return self.proto.height

    @height.setter
    def height(self, value: float):
        self.proto.height = value

    @property
    def floors(self) -> int:
        return self.proto.floors

    @floors.setter
    def floors(self, value: int):
        self.proto.floors = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Area):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.ZoneGrid)
class ZoneGrid(ProtoMessageClass):
    """
    A grid that exists across the entire UMD map. Used to map what exists in each part of the grid on the map

    Args:
        bound_NE: :attr:`bound_NE`
        bound_SW: :attr:`bound_SW`
        lat_samples: :attr:`lat_samples`
        lon_samples: :attr:`lon_samples`
        points: :attr:`points`
    Attributes:
        bound_NE: Point that represents the upper right corner of the :obj:`ZoneGrid`
        bound_SW: Point that represents the lower left corner of the :obj:`ZoneGrid`
        lat_samples: The number of examples that exist in the latitudinal direction of the :obj:`ZoneGrid`
        lon_samples: The number of examples that exist in the longitudinal direction of the :obj:`ZoneGrid`
        points: List of all the points in the :obj:`ZoneGrid`, the value of which is the :attr:`ZoneType` at each point.
    """

    class ZoneType(ProtoEnumClass):
        """All possible zone types that can exist in each cell of the :obj:`ZoneGrid`"""

        COMMERCIAL = 0
        RETAIL = 1
        INDUSTRIAL = 2
        RESIDENTIAL = 3
        PARKING = 4
        WATER = 5
        GREEN = 6
        BROWN = 7
        UNCLASSIFIED = 8

    _proto_message = UMD_pb2.ZoneGrid

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.ZoneGrid] = None,
        bound_NE: Point_ENU = None,
        bound_SW: Point_ENU = None,
        lat_samples: int = None,
        lon_samples: int = None,
        points: List[ZoneGrid.ZoneType] = None,
    ):
        if proto is None:
            proto = UMD_pb2.ZoneGrid()
        self.proto = proto
        self._bound_NE = get_wrapper(proto_type=proto.bound_NE.__class__)(proto=proto.bound_NE)
        self._bound_SW = get_wrapper(proto_type=proto.bound_SW.__class__)(proto=proto.bound_SW)
        if bound_NE is not None:
            self.bound_NE = bound_NE
        if bound_SW is not None:
            self.bound_SW = bound_SW
        if lat_samples is not None:
            self.lat_samples = lat_samples
        if lon_samples is not None:
            self.lon_samples = lon_samples
        self._points = ProtoListWrapper(
            container=[ZoneGrid.ZoneType(v) for v in proto.points], attr_name="points", list_owner=self
        )
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
    def points(self) -> List[ZoneGrid.ZoneType]:
        return self._points

    @points.setter
    def points(self, value: List[ZoneGrid.ZoneType]):
        self._points.clear()
        for v in value:
            self._points.append(v)

    def _update_proto_references(self, proto: UMD_pb2.ZoneGrid):
        self.proto = proto
        self._bound_NE._update_proto_references(proto.bound_NE)
        self._bound_SW._update_proto_references(proto.bound_SW)


@register_wrapper(proto_type=UMD_pb2.TrafficSignData)
class TrafficSignData(ProtoMessageClass):
    """
    Information about traffic signs in a UMD map.

    Args:
        type: :attr:`type`
        sign_code: :attr:`sign_code`
        face_value: :attr:`face_value`
        face_text: :attr:`face_text`
        asset_name: :attr:`asset_name`
    Attributes:
        type: The type of the sign
        sign_code: The code that represents the content of the sign.
        face_value: The "value" that is shown on the rendered sign (e.g. in a speed limit sign).
        face_text: The "text" that is shown on the rendered sign (e.g. in a direction sign).
        asset_name: The name of the sign asset."""

    class SignType(ProtoEnumClass):
        """All possible types of signs that can exist"""

        REGULATORY_STOP_YIELD_PEDESTRIAN_CROSSING = 0
        REGULATORY_SPEED_REGULATION = 1
        REGULATORY_TURN_AND_LANE_USE = 2
        REGULATORY_MOVEMENT_REGULATION = 3
        REGULATORY_SELECTIVE_EXCLUSION = 4
        REGULATORY_ONE_WAY_DIVIDED_HIGHWAY_ROUNDABOUT = 5
        REGULATORY_PARKING_REGULATION = 6
        REGULATORY_PARKING_PROHIBITION_EMERGENCY_RESTRICTION_RAIL = 7
        REGULATORY_PEDESTRIAN_BICYCLE_EQUESTRIAN = 8
        REGULATORY_TRAFFIC_SIGNAL = 9
        REGULATORY_ROAD_CLOSURE = 10
        REGULATORY_WEIGHT_LIMIT = 11
        REGULATORY_WEIGH_STATION = 12
        REGULATORY_TRUCK_ROUTE = 13
        REGULATORY_RAILROAD_AND_LIGHT_RAIL = 14
        REGULATORY_SEATBELT_CRASH_CLEARANCE_HEADLIGHT_USE = 15
        WARNING_TURN_AND_CURVE = 16
        WARNING_INTERSECTION = 17
        WARNING_ADVANCE_TRAFFIC_CONTROL = 18
        WARNING_MERGE_AND_LANE_TRANSITION = 19
        WARNING_WIDTH_RESTRICTION = 20
        WARNING_DIVIDED_HIGHWAY = 21
        WARNING_HILL = 22
        WARNING_PAVEMENT_CONDITION = 23
        WARNING_LANE_TRANSITION = 24
        WARNING_RAILROAD_AND_LIGHT_RAIL = 25
        WARNING_ADVANCE_WARNING_CROSSING = 26
        WARNING_LOW_CLEARANCE = 27
        WARNING_ADVISORY_SPEED = 28
        WARNING_DEAD_END_NO_OUTLET_NO_PASSING = 29
        WARNING_PLAYGROUND = 30
        WARNING_SUPPLEMENTAL_PLAQUES = 31
        WARNING_SPEED_HUMP = 32
        WARNING_NO_TRAFFIC_SIGNS = 33
        WARNING_WORK_ZONE = 34
        WARNING_ROAD_WORK = 35
        WARNING_BLASTING = 36
        WARNING_SLOW_TRAFFIC = 37
        WARNING_DOUBLE_REVERSE_CURVE = 38
        WARNING_YELLOW_TRAP = 39
        MARKER_ROUTE_MARKERS = 40
        MARKER_JUNCTION_SIGNS = 41
        MARKER_CARDINAL_DIRECTIONAL_AUXILLARIES = 42
        MARKER_ALTERNATIVE_ROUTE_SIGNS = 43
        MARKER_ADVANCE_TURN_AUXILLARIES = 44
        MARKER_DIRECTIONAL_ARROW_AUXILLARIES = 45
        MARKER_DIRECTIONAL_ARROW_AUXILLARIES_BICYCLE = 46
        GUIDE_DESTINATION = 47
        GUIDE_DISTANCE = 48
        GUIDE_STREET_NAME = 49
        GUIDE_PARKING = 50
        GUIDE_REST_AREA = 51
        GUIDE_SCENIC = 52
        GUIDE_RECREATIONAL = 53
        GUIDE_WEIGH_STATION = 54
        GUIDE_GENERAL_SERVICES = 55
        GUIDE_REFERENCE_LOCATION_MILEPOSTS = 56
        GUIDE_BICYCLE = 57
        GUIDE_GENERAL_INFORMATION = 58
        GUIDE_CROSSOVER_FREEWAY_ENTRANCE = 59
        GUIDE_EXPRESSWAY_AND_FREEWAY = 60
        GUIDE_WORK_ZONE_INFORMATION = 61
        GUIDE_RECREATIONAL_AND_CULTURAL_INTEREST = 62
        CULTURAL_INTEREST_GENERAL_INFORMATION = 63
        CULTURAL_INTEREST_TRAVELER_SERVICES = 64
        CULTURAL_INTEREST_ACCOMMODATION_SERVICES = 65
        CULTURAL_INTEREST_LAND_RECREATION = 66
        CULTURAL_INTEREST_WATER_RECREATION = 67
        CULTURAL_INTEREST_WINTER_RECREATION = 68
        OBJECT_MARKER = 69
        BICYCLE_FACILITIES = 70
        SCHOOL = 71
        EMERGENCY_MANAGEMENT_CIVIL_DEFENSE = 72

    _proto_message = UMD_pb2.TrafficSignData

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.TrafficSignData] = None,
        type: TrafficSignData.SignType = None,
        sign_code: str = None,
        face_value: int = None,
        face_text: str = None,
        asset_name: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.TrafficSignData()
        self.proto = proto
        if type is not None:
            self.type = type
        if sign_code is not None:
            self.sign_code = sign_code
        if face_value is not None:
            self.face_value = face_value
        if face_text is not None:
            self.face_text = face_text
        if asset_name is not None:
            self.asset_name = asset_name

    @property
    def type(self) -> TrafficSignData.SignType:
        return self.proto.type

    @type.setter
    def type(self, value: TrafficSignData.SignType):
        self.proto.type = value

    @property
    def sign_code(self) -> str:
        return self.proto.sign_code

    @sign_code.setter
    def sign_code(self, value: str):
        self.proto.sign_code = value

    @property
    def face_value(self) -> int:
        return self.proto.face_value

    @face_value.setter
    def face_value(self, value: int):
        self.proto.face_value = value

    @property
    def face_text(self) -> str:
        return self.proto.face_text

    @face_text.setter
    def face_text(self, value: str):
        self.proto.face_text = value

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficSignData):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.TrafficLightData)
class TrafficLightData(ProtoMessageClass):
    """
    Information about traffic lights that exist in the UMD map.

    Args:
        signaled_intersection_id: :attr:`signaled_intersection_id`
        bulbs: :attr:`bulbs`
        asset_name: :attr:`asset_name`
    Attributes:
        signaled_intersection_id: The integer ID of the junction to which the Traffic Light belongs.
        bulbs: A list of bulbs that exist on the traffic light.
        asset_name: An optional reference to the asset name of this traffic light box."""

    _proto_message = UMD_pb2.TrafficLightData

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.TrafficLightData] = None,
        signaled_intersection_id: int = None,
        bulbs: List[TrafficLightBulb] = None,
        asset_name: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.TrafficLightData()
        self.proto = proto
        self._bulbs = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.bulbs],
            attr_name="bulbs",
            list_owner=self,
        )
        if signaled_intersection_id is not None:
            self.signaled_intersection_id = signaled_intersection_id
        if bulbs is not None:
            self.bulbs = bulbs
        if asset_name is not None:
            self.asset_name = asset_name

    @property
    def signaled_intersection_id(self) -> int:
        return self.proto.signaled_intersection_id

    @signaled_intersection_id.setter
    def signaled_intersection_id(self, value: int):
        self.proto.signaled_intersection_id = value

    @property
    def bulbs(self) -> List[TrafficLightBulb]:
        return self._bulbs

    @bulbs.setter
    def bulbs(self, value: List[TrafficLightBulb]):
        self._bulbs.clear()
        for v in value:
            self._bulbs.append(v)

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficLightData):
        self.proto = proto
        for i, v in enumerate(self.bulbs):
            v._update_proto_references(self.proto.bulbs[i])


@register_wrapper(proto_type=UMD_pb2.TrafficLightBulb)
class TrafficLightBulb(ProtoMessageClass):
    """
    Information about the bulbs that exist in traffic lights.

    Args:
        shape: :attr:`shape`
        color: :attr:`color`
        phase_id: :attr:`phase_id`
        is_flashing: :attr:`is_flashing`
    Attributes:
        shape: The shape of the traffic light bulb
        color: The color of the traffic light bulb
        phase_id: The integer ID of the phase of the traffic light signal (e.g. red vs green etc).
        is_flashing: Boolean flag to show whether or not the traffic light bulb is flashing"""

    class Shape(ProtoEnumClass):
        """All possible shapes of traffic light bulbs."""

        CIRCLE = 0
        ARROW_LEFT = 1
        ARROW_LEFT_DIAGONAL = 2
        ARROW_RIGHT = 3
        ARROW_RIGHT_DIAGONAL = 4
        ARROW_UP = 6
        ARROW_DOWN = 7
        U_TURN = 5
        BICYCLE = 8
        WALK = 9
        DONT_WALK = 10
        NUMBER = 11

    class Color(ProtoEnumClass):
        """All possible colors that a traffic light bulb can have."""

        RED = 0
        YELLOW = 1
        GREEN = 2

    _proto_message = UMD_pb2.TrafficLightBulb

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.TrafficLightBulb] = None,
        shape: TrafficLightBulb.Shape = None,
        color: TrafficLightBulb.Color = None,
        phase_id: int = None,
        is_flashing: bool = None,
    ):
        if proto is None:
            proto = UMD_pb2.TrafficLightBulb()
        self.proto = proto
        if shape is not None:
            self.shape = shape
        if color is not None:
            self.color = color
        if phase_id is not None:
            self.phase_id = phase_id
        if is_flashing is not None:
            self.is_flashing = is_flashing

    @property
    def shape(self) -> TrafficLightBulb.Shape:
        return self.proto.shape

    @shape.setter
    def shape(self, value: TrafficLightBulb.Shape):
        self.proto.shape = value

    @property
    def color(self) -> TrafficLightBulb.Color:
        return self.proto.color

    @color.setter
    def color(self, value: TrafficLightBulb.Color):
        self.proto.color = value

    @property
    def phase_id(self) -> int:
        return self.proto.phase_id

    @phase_id.setter
    def phase_id(self, value: int):
        self.proto.phase_id = value

    @property
    def is_flashing(self) -> bool:
        return self.proto.is_flashing

    @is_flashing.setter
    def is_flashing(self, value: bool):
        self.proto.is_flashing = value

    def _update_proto_references(self, proto: UMD_pb2.TrafficLightBulb):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.PropData)
class PropData(ProtoMessageClass):
    """
    Information about props that exist in the UMD map.

    Args:
        type: :attr:`type`
        asset_name: :attr:`asset_name`
    Attributes:
        type: The type of the prop
        asset_name: The name of the asset represented by the prop."""

    class PropType(ProtoEnumClass):
        """All possible types that a prop can be"""

        VEHICLE = 0
        TERRAIN_NATURAL = 1
        VEGETATION_HIGH = 2
        VEGETATION_LOW = 3
        BUILDING = 4
        HARDSCAPE = 5
        BARRIER = 6
        POLE = 7
        OTHER = 8

    _proto_message = UMD_pb2.PropData

    def __init__(
        self, *, proto: Optional[UMD_pb2.PropData] = None, type: PropData.PropType = None, asset_name: str = None
    ):
        if proto is None:
            proto = UMD_pb2.PropData()
        self.proto = proto
        if type is not None:
            self.type = type
        if asset_name is not None:
            self.asset_name = asset_name

    @property
    def type(self) -> PropData.PropType:
        return self.proto.type

    @type.setter
    def type(self, value: PropData.PropType):
        self.proto.type = value

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    def _update_proto_references(self, proto: UMD_pb2.PropData):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.Object)
class Object(ProtoMessageClass):
    """
    An object that exists in the UMD map.

    Args:
        id: :attr:`id`
        orientation: :attr:`orientation`
        origin: :attr:`origin`
        bounding_box: :attr:`bounding_box`
        traffic_sign_data: :attr:`traffic_sign_data`
        traffic_light_data: :attr:`traffic_light_data`
        prop_data: :attr:`prop_data`
        exclusion_radius: :attr:`exclusion_radius`
        user_data: :attr:`user_data`
    Attributes:
        id: The integer ID of the :obj:`Object`
        orientation: The orientation of the :obj:`Object`
        origin: The point on which the :obj:`Object` is placed.
        bounding_box: The bounding box that encapsulates the :obj:`Object`.
        traffic_sign_data: Data about the traffic sign if the :obj:`Object` is a traffic sign.
        traffic_light_data: Data about the traffic light if the :obj:`Object` is a traffic light.
        prop_data: Data about the prop if the :obj:`Object` is a prop.
        exclusion_radius: The radius around the :obj:`Object` in which other :obj:`Object` should not be placed.
            Default: -1.0
        user_data: Optional information about the :obj:`Object`"""

    _proto_message = UMD_pb2.Object

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Object] = None,
        id: int = None,
        orientation: Quaternion = None,
        origin: Point_ENU = None,
        bounding_box: AABB = None,
        traffic_sign_data: TrafficSignData = None,
        traffic_light_data: TrafficLightData = None,
        prop_data: PropData = None,
        exclusion_radius: float = None,
        user_data: str = None,
    ):
        if proto is None:
            proto = UMD_pb2.Object()
        self.proto = proto
        self._orientation = get_wrapper(proto_type=proto.orientation.__class__)(proto=proto.orientation)
        self._origin = get_wrapper(proto_type=proto.origin.__class__)(proto=proto.origin)
        self._bounding_box = get_wrapper(proto_type=proto.bounding_box.__class__)(proto=proto.bounding_box)
        self._traffic_sign_data = get_wrapper(proto_type=proto.traffic_sign_data.__class__)(
            proto=proto.traffic_sign_data
        )
        self._traffic_light_data = get_wrapper(proto_type=proto.traffic_light_data.__class__)(
            proto=proto.traffic_light_data
        )
        self._prop_data = get_wrapper(proto_type=proto.prop_data.__class__)(proto=proto.prop_data)
        if id is not None:
            self.id = id
        if orientation is not None:
            self.orientation = orientation
        if origin is not None:
            self.origin = origin
        if bounding_box is not None:
            self.bounding_box = bounding_box
        if traffic_sign_data is not None:
            self.traffic_sign_data = traffic_sign_data
        if traffic_light_data is not None:
            self.traffic_light_data = traffic_light_data
        if prop_data is not None:
            self.prop_data = prop_data
        if exclusion_radius is not None:
            self.exclusion_radius = exclusion_radius
        if user_data is not None:
            self.user_data = user_data

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
    def bounding_box(self) -> AABB:
        return self._bounding_box

    @bounding_box.setter
    def bounding_box(self, value: AABB):
        self.proto.bounding_box.CopyFrom(value.proto)

        self._bounding_box = value
        self._bounding_box._update_proto_references(self.proto.bounding_box)

    @property
    def traffic_sign_data(self) -> TrafficSignData:
        return self._traffic_sign_data

    @traffic_sign_data.setter
    def traffic_sign_data(self, value: TrafficSignData):
        self.proto.traffic_sign_data.CopyFrom(value.proto)

        self._traffic_sign_data = value
        self._traffic_sign_data._update_proto_references(self.proto.traffic_sign_data)

    @property
    def traffic_light_data(self) -> TrafficLightData:
        return self._traffic_light_data

    @traffic_light_data.setter
    def traffic_light_data(self, value: TrafficLightData):
        self.proto.traffic_light_data.CopyFrom(value.proto)

        self._traffic_light_data = value
        self._traffic_light_data._update_proto_references(self.proto.traffic_light_data)

    @property
    def prop_data(self) -> PropData:
        return self._prop_data

    @prop_data.setter
    def prop_data(self, value: PropData):
        self.proto.prop_data.CopyFrom(value.proto)

        self._prop_data = value
        self._prop_data._update_proto_references(self.proto.prop_data)

    @property
    def exclusion_radius(self) -> float:
        return self.proto.exclusion_radius

    @exclusion_radius.setter
    def exclusion_radius(self, value: float):
        self.proto.exclusion_radius = value

    @property
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

    def _update_proto_references(self, proto: UMD_pb2.Object):
        self.proto = proto
        self._orientation._update_proto_references(proto.orientation)
        self._origin._update_proto_references(proto.origin)
        self._bounding_box._update_proto_references(proto.bounding_box)
        self._traffic_sign_data._update_proto_references(proto.traffic_sign_data)
        self._traffic_light_data._update_proto_references(proto.traffic_light_data)
        self._prop_data._update_proto_references(proto.prop_data)


@register_wrapper(proto_type=UMD_pb2.Junction)
class Junction(ProtoMessageClass):
    """
    A junction that exists in the UMD map.

    Args:
        id: :attr:`id`
        lane_segments: :attr:`lane_segments`
        road_segments: :attr:`road_segments`
        signaled_intersection: :attr:`signaled_intersection`
        user_data: :attr:`user_data`
        corners: :attr:`corners`
        crosswalk_lanes: :attr:`crosswalk_lanes`
        signed_intersection: :attr:`signed_intersection`
    Attributes:
        id: The integer ID of the :obj:`Junction`
        lane_segments: List of :obj:`LaneSegment`s that connect to the :obj:`Junction`.
        road_segments: List of :obj:`RoadSegment`s that connect to the :obj:`Junction`.
        signaled_intersection: Integer ID of the signaled intersection that controls this :obj:`Junction` if the :obj:`Junction` is a signaled
            intersection
        user_data: Optional information about the :obj:`Junction`.
        corners: List of integer IDs of the :obj:`Edge` objects that define the corners of the :obj:`Junction`.
        crosswalk_lanes: List of the integer IDs of the  :obj:`LaneSegment` objects that define the crosswalks on the :obj:`Junction`
        signed_intersection: Integer ID of the signed intersection that controls this :obj:`Junction` if the :obj:`Junction` is a signed
            intersection"""

    _proto_message = UMD_pb2.Junction

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Junction] = None,
        id: int = None,
        lane_segments: List[int] = None,
        road_segments: List[int] = None,
        signaled_intersection: int = None,
        user_data: str = None,
        corners: List[int] = None,
        crosswalk_lanes: List[int] = None,
        signed_intersection: int = None,
    ):
        if proto is None:
            proto = UMD_pb2.Junction()
        self.proto = proto
        if id is not None:
            self.id = id
        self._lane_segments = ProtoListWrapper(
            container=[int(v) for v in proto.lane_segments], attr_name="lane_segments", list_owner=self
        )
        if lane_segments is not None:
            self.lane_segments = lane_segments
        self._road_segments = ProtoListWrapper(
            container=[int(v) for v in proto.road_segments], attr_name="road_segments", list_owner=self
        )
        if road_segments is not None:
            self.road_segments = road_segments
        if signaled_intersection is not None:
            self.signaled_intersection = signaled_intersection
        if user_data is not None:
            self.user_data = user_data
        self._corners = ProtoListWrapper(
            container=[int(v) for v in proto.corners], attr_name="corners", list_owner=self
        )
        if corners is not None:
            self.corners = corners
        self._crosswalk_lanes = ProtoListWrapper(
            container=[int(v) for v in proto.crosswalk_lanes], attr_name="crosswalk_lanes", list_owner=self
        )
        if crosswalk_lanes is not None:
            self.crosswalk_lanes = crosswalk_lanes
        if signed_intersection is not None:
            self.signed_intersection = signed_intersection

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
    def user_data(self) -> str:
        return self.proto.user_data

    @user_data.setter
    def user_data(self, value: str):
        self.proto.user_data = value

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
    def signed_intersection(self) -> int:
        return self.proto.signed_intersection

    @signed_intersection.setter
    def signed_intersection(self, value: int):
        self.proto.signed_intersection = value

    def _update_proto_references(self, proto: UMD_pb2.Junction):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.RoadMarking)
class RoadMarking(ProtoMessageClass):
    """
    Markings that exist on the road to separate :obj:`LaneSegment`s

    Args:
        id: :attr:`id`
        edge_id: :attr:`edge_id`
        width: :attr:`width`
        type: :attr:`type`
        color: :attr:`color`
        dash_length: :attr:`dash_length`
        dash_separation: :attr:`dash_separation`
        is_stopline: :attr:`is_stopline`
    Attributes:
        id: The integer ID of the :obj:`RoadMarking`.
        edge_id: The integer ID of the :obj:`Edge` that defines the line on which the :obj:`RoadMarking` exists.
        width: The width of the :obj:`RoadMarking` in meters.
        type: The type of the :obj:`RoadMarking`.
        color: The color of the :obj:`RoadMarking`.
        dash_length: The length in meters of the dashes on the :obj:`RoadMarking` if the :obj:`RoadMarking` is dashed.
        dash_separation: The length of the separation between dashes in meters on the :obj:`RoadMarking` if the :obj:`RoadMarking` is dashed.
        is_stopline: Boolean flag to denote whether or not the :obj:`RoadMarking` is a stop line."""

    class Type(ProtoEnumClass):
        """All possible types of :obj:`RoadMarking`."""

        SOLID = 0
        DASHED = 1
        SOLID_SOLID = 2
        SOLID_DASHED = 3
        DASHED_SOLID = 4
        DASHED_DASHED = 5
        BOTTS_DOTS = 6
        NO_PAINT = 7

    class Color(ProtoEnumClass):
        """All possible colors that a :obj:`RoadMarking` can be."""

        WHITE = 0
        BLUE = 1
        GREEN = 2
        RED = 3
        YELLOW = 4

    _proto_message = UMD_pb2.RoadMarking

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.RoadMarking] = None,
        id: int = None,
        edge_id: int = None,
        width: float = None,
        type: RoadMarking.Type = None,
        color: RoadMarking.Color = None,
        dash_length: float = None,
        dash_separation: float = None,
        is_stopline: bool = None,
    ):
        if proto is None:
            proto = UMD_pb2.RoadMarking()
        self.proto = proto
        if id is not None:
            self.id = id
        if edge_id is not None:
            self.edge_id = edge_id
        if width is not None:
            self.width = width
        if type is not None:
            self.type = type
        if color is not None:
            self.color = color
        if dash_length is not None:
            self.dash_length = dash_length
        if dash_separation is not None:
            self.dash_separation = dash_separation
        if is_stopline is not None:
            self.is_stopline = is_stopline

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def edge_id(self) -> int:
        return self.proto.edge_id

    @edge_id.setter
    def edge_id(self, value: int):
        self.proto.edge_id = value

    @property
    def width(self) -> float:
        return self.proto.width

    @width.setter
    def width(self, value: float):
        self.proto.width = value

    @property
    def type(self) -> RoadMarking.Type:
        return self.proto.type

    @type.setter
    def type(self, value: RoadMarking.Type):
        self.proto.type = value

    @property
    def color(self) -> RoadMarking.Color:
        return self.proto.color

    @color.setter
    def color(self, value: RoadMarking.Color):
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
    def is_stopline(self) -> bool:
        return self.proto.is_stopline

    @is_stopline.setter
    def is_stopline(self, value: bool):
        self.proto.is_stopline = value

    def _update_proto_references(self, proto: UMD_pb2.RoadMarking):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.SignalOnset)
class SignalOnset(ProtoMessageClass):
    """
    The state of a Traffic Light

    Args:
        onset: :attr:`onset`
        signal_state: :attr:`signal_state`
        logical_state: :attr:`logical_state`
    Attributes:
        onset: The time in seconds until the :attr:`signal_state` activates.
        signal_state: The type of signal state.
        logical_state: The logical state of the traffic signal."""

    class SignalState(ProtoEnumClass):
        """All possible states of the signal."""

        red = 0
        yellow = 1
        green = 2

    class LogicalState(ProtoEnumClass):
        """All possible logical states of the signal."""

        inactive = 0
        red_solid = 1
        red_flashing = 2
        yellow_solid = 3
        yellow_flashing = 4
        green_solid = 5
        green_flashing = 6

    _proto_message = UMD_pb2.SignalOnset

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.SignalOnset] = None,
        onset: float = None,
        signal_state: SignalOnset.SignalState = None,
        logical_state: SignalOnset.LogicalState = None,
    ):
        if proto is None:
            proto = UMD_pb2.SignalOnset()
        self.proto = proto
        if onset is not None:
            self.onset = onset
        if signal_state is not None:
            self.signal_state = signal_state
        if logical_state is not None:
            self.logical_state = logical_state

    @property
    def onset(self) -> float:
        return self.proto.onset

    @onset.setter
    def onset(self, value: float):
        self.proto.onset = value

    @property
    def signal_state(self) -> SignalOnset.SignalState:
        return self.proto.signal_state

    @signal_state.setter
    def signal_state(self, value: SignalOnset.SignalState):
        self.proto.signal_state = value

    @property
    def logical_state(self) -> SignalOnset.LogicalState:
        return self.proto.logical_state

    @logical_state.setter
    def logical_state(self, value: SignalOnset.LogicalState):
        self.proto.logical_state = value

    def _update_proto_references(self, proto: UMD_pb2.SignalOnset):
        self.proto = proto


@register_wrapper(proto_type=UMD_pb2.Phase)
class Phase(ProtoMessageClass):
    """
    The phase of a :obj:`TrafficLightBulb`.

    Args:
        id: :attr:`id`
        phase_timing: :attr:`phase_timing`
        controlled_lanes: :attr:`controlled_lanes`
    Attributes:
        id: The integer ID of the phase.
        phase_timing: The signal state that is about to activate.
        controlled_lanes: The integer IDs of the :obj:`LaneSegment` objects that are controlled by this :obj:`TrafficLightBulb`.
    """

    _proto_message = UMD_pb2.Phase

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.Phase] = None,
        id: int = None,
        phase_timing: List[SignalOnset] = None,
        controlled_lanes: List[int] = None,
    ):
        if proto is None:
            proto = UMD_pb2.Phase()
        self.proto = proto
        self._phase_timing = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.phase_timing],
            attr_name="phase_timing",
            list_owner=self,
        )
        if id is not None:
            self.id = id
        if phase_timing is not None:
            self.phase_timing = phase_timing
        self._controlled_lanes = ProtoListWrapper(
            container=[int(v) for v in proto.controlled_lanes], attr_name="controlled_lanes", list_owner=self
        )
        if controlled_lanes is not None:
            self.controlled_lanes = controlled_lanes

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

    @property
    def controlled_lanes(self) -> List[int]:
        return self._controlled_lanes

    @controlled_lanes.setter
    def controlled_lanes(self, value: List[int]):
        self._controlled_lanes.clear()
        for v in value:
            self._controlled_lanes.append(v)

    def _update_proto_references(self, proto: UMD_pb2.Phase):
        self.proto = proto
        for i, v in enumerate(self.phase_timing):
            v._update_proto_references(self.proto.phase_timing[i])


@register_wrapper(proto_type=UMD_pb2.SignaledIntersection)
class SignaledIntersection(ProtoMessageClass):
    """
    An intersection that is controlled by a signal.

    Args:
        id: :attr:`id`
        junction: :attr:`junction`
        phase_timings: :attr:`phase_timings`
        cycle_time: :attr:`cycle_time`
    Attributes:
        id: The integer ID of the intersection.
        junction: The :obj:`Junction` that is controlled by the signaled intersection.
        phase_timings: The timings of phases in the intersection.
        cycle_time: The cycle time of the :attr:`phase_timings`."""

    _proto_message = UMD_pb2.SignaledIntersection

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.SignaledIntersection] = None,
        id: int = None,
        junction: int = None,
        phase_timings: List[Phase] = None,
        cycle_time: float = None,
    ):
        if proto is None:
            proto = UMD_pb2.SignaledIntersection()
        self.proto = proto
        self._phase_timings = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.phase_timings],
            attr_name="phase_timings",
            list_owner=self,
        )
        if id is not None:
            self.id = id
        if junction is not None:
            self.junction = junction
        if phase_timings is not None:
            self.phase_timings = phase_timings
        if cycle_time is not None:
            self.cycle_time = cycle_time

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

    @property
    def cycle_time(self) -> float:
        return self.proto.cycle_time

    @cycle_time.setter
    def cycle_time(self, value: float):
        self.proto.cycle_time = value

    def _update_proto_references(self, proto: UMD_pb2.SignaledIntersection):
        self.proto = proto
        for i, v in enumerate(self.phase_timings):
            v._update_proto_references(self.proto.phase_timings[i])


@register_wrapper(proto_type=UMD_pb2.SignedIntersection)
class SignedIntersection(ProtoMessageClass):
    """
    An intersection that is controlled by a sign.

    Args:
        id: :attr:`id`
        junction: :attr:`junction`
        stop_sign_lane_ids: :attr:`stop_sign_lane_ids`
        yield_sign_lane_ids: :attr:`yield_sign_lane_ids`
    Attributes:
        id: The integer ID of the intersection.
        junction: The :obj:`Junction` that is controlled by the signaled intersection.
        stop_sign_lane_ids: The integer IDs of :obj:`LaneSegment` objects that are controlled by a stop sign.
        yield_sign_lane_ids: The integer IDs of :obj:`LaneSegment` objects that are controlled by a yield sign."""

    _proto_message = UMD_pb2.SignedIntersection

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.SignedIntersection] = None,
        id: int = None,
        junction: int = None,
        stop_sign_lane_ids: List[int] = None,
        yield_sign_lane_ids: List[int] = None,
    ):
        if proto is None:
            proto = UMD_pb2.SignedIntersection()
        self.proto = proto
        if id is not None:
            self.id = id
        if junction is not None:
            self.junction = junction
        self._stop_sign_lane_ids = ProtoListWrapper(
            container=[int(v) for v in proto.stop_sign_lane_ids], attr_name="stop_sign_lane_ids", list_owner=self
        )
        if stop_sign_lane_ids is not None:
            self.stop_sign_lane_ids = stop_sign_lane_ids
        self._yield_sign_lane_ids = ProtoListWrapper(
            container=[int(v) for v in proto.yield_sign_lane_ids], attr_name="yield_sign_lane_ids", list_owner=self
        )
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


@register_wrapper(proto_type=UMD_pb2.UniversalMap)
class UniversalMap(ProtoMessageClass):
    """
    Wrapper message for a UMD map and all its constituent parts.

    Args:
        info: :attr:`info`
        road_segments: :attr:`road_segments`
        lane_segments: :attr:`lane_segments`
        areas: :attr:`areas`
        objects: :attr:`objects`
        edges: :attr:`edges`
        junctions: :attr:`junctions`
        road_markings: :attr:`road_markings`
        signaled_intersections: :attr:`signaled_intersections`
        signed_intersections: :attr:`signed_intersections`
        zone_grid: :attr:`zone_grid`
    Attributes:
        info: Information about the UMD map.
        road_segments: All :obj:`RoadSegment` objects in the UMD map.
        lane_segments: All :obj:`LaneSegment` objects in the UMD map.
        areas: All :obj:`Area` objects in the UMD map.
        objects: All :obj:`Object` objects in the UMD map.
        edges: All :obj:`Edge` objects in the UMD map.
        junctions: All :obj:`Junction` objects in the UMD map.
        road_markings: All :obj:`RoadMarking` objects in the UMD map.
        signaled_intersections: All :obj:`SignaledIntersection` objects in the UMD map.
        signed_intersections: All :obj:`SignedIntersection` objects in the UMD map.
        zone_grid: The :obj:`ZoneGrid` objects of the UMD Map."""

    _proto_message = UMD_pb2.UniversalMap

    def __init__(
        self,
        *,
        proto: Optional[UMD_pb2.UniversalMap] = None,
        info: Info = None,
        road_segments: Dict[int, RoadSegment] = None,
        lane_segments: Dict[int, LaneSegment] = None,
        areas: Dict[int, Area] = None,
        objects: Dict[int, Object] = None,
        edges: Dict[int, Edge] = None,
        junctions: Dict[int, Junction] = None,
        road_markings: Dict[int, RoadMarking] = None,
        signaled_intersections: Dict[int, SignaledIntersection] = None,
        signed_intersections: Dict[int, SignedIntersection] = None,
        zone_grid: ZoneGrid = None,
    ):
        if proto is None:
            proto = UMD_pb2.UniversalMap()
        self.proto = proto
        self._info = get_wrapper(proto_type=proto.info.__class__)(proto=proto.info)
        self._road_segments = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.road_segments.items()},
            attr_name="road_segments",
            dict_owner=self,
        )
        self._lane_segments = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.lane_segments.items()},
            attr_name="lane_segments",
            dict_owner=self,
        )
        self._areas = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.areas.items()},
            attr_name="areas",
            dict_owner=self,
        )
        self._objects = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.objects.items()},
            attr_name="objects",
            dict_owner=self,
        )
        self._edges = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.edges.items()},
            attr_name="edges",
            dict_owner=self,
        )
        self._junctions = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.junctions.items()},
            attr_name="junctions",
            dict_owner=self,
        )
        self._road_markings = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.road_markings.items()},
            attr_name="road_markings",
            dict_owner=self,
        )
        self._signaled_intersections = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.signaled_intersections.items()
            },
            attr_name="signaled_intersections",
            dict_owner=self,
        )
        self._signed_intersections = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.signed_intersections.items()
            },
            attr_name="signed_intersections",
            dict_owner=self,
        )
        self._zone_grid = get_wrapper(proto_type=proto.zone_grid.__class__)(proto=proto.zone_grid)
        if info is not None:
            self.info = info
        if road_segments is not None:
            self.road_segments = road_segments
        if lane_segments is not None:
            self.lane_segments = lane_segments
        if areas is not None:
            self.areas = areas
        if objects is not None:
            self.objects = objects
        if edges is not None:
            self.edges = edges
        if junctions is not None:
            self.junctions = junctions
        if road_markings is not None:
            self.road_markings = road_markings
        if signaled_intersections is not None:
            self.signaled_intersections = signaled_intersections
        if signed_intersections is not None:
            self.signed_intersections = signed_intersections
        if zone_grid is not None:
            self.zone_grid = zone_grid

    @property
    def info(self) -> Info:
        return self._info

    @info.setter
    def info(self, value: Info):
        self.proto.info.CopyFrom(value.proto)

        self._info = value
        self._info._update_proto_references(self.proto.info)

    @property
    def road_segments(self) -> Dict[int, RoadSegment]:
        return self._road_segments

    @road_segments.setter
    def road_segments(self, value: Dict[int, RoadSegment]):
        self._road_segments.clear()
        self._road_segments.update(value)

    @property
    def lane_segments(self) -> Dict[int, LaneSegment]:
        return self._lane_segments

    @lane_segments.setter
    def lane_segments(self, value: Dict[int, LaneSegment]):
        self._lane_segments.clear()
        self._lane_segments.update(value)

    @property
    def areas(self) -> Dict[int, Area]:
        return self._areas

    @areas.setter
    def areas(self, value: Dict[int, Area]):
        self._areas.clear()
        self._areas.update(value)

    @property
    def objects(self) -> Dict[int, Object]:
        return self._objects

    @objects.setter
    def objects(self, value: Dict[int, Object]):
        self._objects.clear()
        self._objects.update(value)

    @property
    def edges(self) -> Dict[int, Edge]:
        return self._edges

    @edges.setter
    def edges(self, value: Dict[int, Edge]):
        self._edges.clear()
        self._edges.update(value)

    @property
    def junctions(self) -> Dict[int, Junction]:
        return self._junctions

    @junctions.setter
    def junctions(self, value: Dict[int, Junction]):
        self._junctions.clear()
        self._junctions.update(value)

    @property
    def road_markings(self) -> Dict[int, RoadMarking]:
        return self._road_markings

    @road_markings.setter
    def road_markings(self, value: Dict[int, RoadMarking]):
        self._road_markings.clear()
        self._road_markings.update(value)

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
        self._info._update_proto_references(proto.info)
        for k, v in self.road_segments.items():
            v._update_proto_references(self.proto.road_segments[k])
        for k, v in self.lane_segments.items():
            v._update_proto_references(self.proto.lane_segments[k])
        for k, v in self.areas.items():
            v._update_proto_references(self.proto.areas[k])
        for k, v in self.objects.items():
            v._update_proto_references(self.proto.objects[k])
        for k, v in self.edges.items():
            v._update_proto_references(self.proto.edges[k])
        for k, v in self.junctions.items():
            v._update_proto_references(self.proto.junctions[k])
        for k, v in self.road_markings.items():
            v._update_proto_references(self.proto.road_markings[k])
        for k, v in self.signaled_intersections.items():
            v._update_proto_references(self.proto.signaled_intersections[k])
        for k, v in self.signed_intersections.items():
            v._update_proto_references(self.proto.signed_intersections[k])
        self._zone_grid._update_proto_references(proto.zone_grid)
