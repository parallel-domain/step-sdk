from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_keystone_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_keystone_pb2.KeystoneBuildMessage)
class KeystoneBuildMessage(ProtoMessageClass):
    _proto_message = pd_keystone_pb2.KeystoneBuildMessage

    def __init__(self, *, proto: Optional[pd_keystone_pb2.KeystoneBuildMessage]=None, stages: Optional[List[KeystoneBuildMessage.PipelineStage]]=None):
        if proto is None:
            proto = pd_keystone_pb2.KeystoneBuildMessage()
        self.proto = proto
        self._stages = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.stages], attr_name='stages', list_owner=self)
        if stages is not None:
            self.stages = stages

    @property
    def stages(self) -> List[KeystoneBuildMessage.PipelineStage]:
        return self._stages

    @stages.setter
    def stages(self, value: List[KeystoneBuildMessage.PipelineStage]):
        self._stages.clear()
        for v in value:
            self._stages.append(v)

    def _update_proto_references(self, proto: pd_keystone_pb2.KeystoneBuildMessage):
        self.proto = proto
        for i, v in enumerate(self.stages):
            v._update_proto_references(self.proto.stages[i])