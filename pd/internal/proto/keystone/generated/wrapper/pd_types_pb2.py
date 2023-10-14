from __future__ import annotations
from typing import Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass
)
from ..python import (
    pd_types_pb2
)


@register_wrapper(proto_type=pd_types_pb2.Float3)
class Float3(ProtoMessageClass):
    """
    A three element vector of float values.

    Args:
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
    Attributes:
        x: First element of the vector.
        y: Second element of the vector.
        z: Third element of the vector."""

    _proto_message = pd_types_pb2.Float3

    def __init__(
        self, *, proto: Optional[pd_types_pb2.Float3] = None, x: float = None, y: float = None, z: float = None
    ):
        if proto is None:
            proto = pd_types_pb2.Float3()
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

    def _update_proto_references(self, proto: pd_types_pb2.Float3):
        self.proto = proto


@register_wrapper(proto_type=pd_types_pb2.Float3x3)
class Float3x3(ProtoMessageClass):
    """
    A 3x3 matrix of float values.

    Args:
        r0: :attr:`r0`
        r1: :attr:`r1`
        r2: :attr:`r2`
    Attributes:
        r0: The first row of the matrix.
        r1: The second row of the matrix.
        r2: The third row of the matrix."""

    _proto_message = pd_types_pb2.Float3x3

    def __init__(
        self, *, proto: Optional[pd_types_pb2.Float3x3] = None, r0: Float3 = None, r1: Float3 = None, r2: Float3 = None
    ):
        if proto is None:
            proto = pd_types_pb2.Float3x3()
        self.proto = proto
        self._r0 = get_wrapper(proto_type=proto.r0.__class__)(proto=proto.r0)
        self._r1 = get_wrapper(proto_type=proto.r1.__class__)(proto=proto.r1)
        self._r2 = get_wrapper(proto_type=proto.r2.__class__)(proto=proto.r2)
        if r0 is not None:
            self.r0 = r0
        if r1 is not None:
            self.r1 = r1
        if r2 is not None:
            self.r2 = r2

    @property
    def r0(self) -> Float3:
        return self._r0

    @r0.setter
    def r0(self, value: Float3):
        self.proto.r0.CopyFrom(value.proto)

        self._r0 = value
        self._r0._update_proto_references(self.proto.r0)

    @property
    def r1(self) -> Float3:
        return self._r1

    @r1.setter
    def r1(self, value: Float3):
        self.proto.r1.CopyFrom(value.proto)

        self._r1 = value
        self._r1._update_proto_references(self.proto.r1)

    @property
    def r2(self) -> Float3:
        return self._r2

    @r2.setter
    def r2(self, value: Float3):
        self.proto.r2.CopyFrom(value.proto)

        self._r2 = value
        self._r2._update_proto_references(self.proto.r2)

    def _update_proto_references(self, proto: pd_types_pb2.Float3x3):
        self.proto = proto
        self._r0._update_proto_references(proto.r0)
        self._r1._update_proto_references(proto.r1)
        self._r2._update_proto_references(proto.r2)


@register_wrapper(proto_type=pd_types_pb2.Pose)
class Pose(ProtoMessageClass):
    """
    Represents a pose in 3D space, including translation and rotation.

    Args:
        position: :attr:`position`
        orientation: :attr:`orientation`
    Attributes:
        position: The 3D position of the :obj:`Pose`.
        orientation: The 3D rotation of the :obj:`Pose`."""

    _proto_message = pd_types_pb2.Pose

    def __init__(
        self, *, proto: Optional[pd_types_pb2.Pose] = None, position: Float3 = None, orientation: Float3x3 = None
    ):
        if proto is None:
            proto = pd_types_pb2.Pose()
        self.proto = proto
        self._position = get_wrapper(proto_type=proto.position.__class__)(proto=proto.position)
        self._orientation = get_wrapper(proto_type=proto.orientation.__class__)(proto=proto.orientation)
        if position is not None:
            self.position = position
        if orientation is not None:
            self.orientation = orientation

    @property
    def position(self) -> Float3:
        return self._position

    @position.setter
    def position(self, value: Float3):
        self.proto.position.CopyFrom(value.proto)

        self._position = value
        self._position._update_proto_references(self.proto.position)

    @property
    def orientation(self) -> Float3x3:
        return self._orientation

    @orientation.setter
    def orientation(self, value: Float3x3):
        self.proto.orientation.CopyFrom(value.proto)

        self._orientation = value
        self._orientation._update_proto_references(self.proto.orientation)

    def _update_proto_references(self, proto: pd_types_pb2.Pose):
        self.proto = proto
        self._position._update_proto_references(proto.position)
        self._orientation._update_proto_references(proto.orientation)
