from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_types_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_types_pb2.Float3)
class Float3(ProtoMessageClass):
    _proto_message = pd_types_pb2.Float3

    def __init__(self, *, proto: Optional[pd_types_pb2.Float3]=None, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None):
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
    _proto_message = pd_types_pb2.Float3x3

    def __init__(self, *, proto: Optional[pd_types_pb2.Float3x3]=None, r0: Optional[Float3]=None, r1: Optional[Float3]=None, r2: Optional[Float3]=None):
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
    _proto_message = pd_types_pb2.Pose

    def __init__(self, *, proto: Optional[pd_types_pb2.Pose]=None, orientation: Optional[Float3x3]=None, position: Optional[Float3]=None):
        if proto is None:
            proto = pd_types_pb2.Pose()
        self.proto = proto
        self._orientation = get_wrapper(proto_type=proto.orientation.__class__)(proto=proto.orientation)
        self._position = get_wrapper(proto_type=proto.position.__class__)(proto=proto.position)
        if orientation is not None:
            self.orientation = orientation
        if position is not None:
            self.position = position

    @property
    def orientation(self) -> Float3x3:
        return self._orientation

    @orientation.setter
    def orientation(self, value: Float3x3):
        self.proto.orientation.CopyFrom(value.proto)
        
        self._orientation = value
        self._orientation._update_proto_references(self.proto.orientation)

    @property
    def position(self) -> Float3:
        return self._position

    @position.setter
    def position(self, value: Float3):
        self.proto.position.CopyFrom(value.proto)
        
        self._position = value
        self._position._update_proto_references(self.proto.position)

    def _update_proto_references(self, proto: pd_types_pb2.Pose):
        self.proto = proto
        self._orientation._update_proto_references(proto.orientation)
        self._position._update_proto_references(proto.position)