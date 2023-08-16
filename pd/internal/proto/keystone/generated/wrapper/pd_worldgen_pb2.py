from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_worldgen_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_worldgen_pb2.WorldGenInfo)
class WorldGenInfo(ProtoMessageClass):
    _proto_message = pd_worldgen_pb2.WorldGenInfo

    def __init__(self, *, proto: Optional[pd_worldgen_pb2.WorldGenInfo]=None, artifact_key: Optional[str]=None, location_list: Optional[List[WorldGenInfo.Location]]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_worldgen_pb2.WorldGenInfo()
        self.proto = proto
        self._location_list = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.location_list], attr_name='location_list', list_owner=self)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if location_list is not None:
            self.location_list = location_list
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def location_list(self) -> List[WorldGenInfo.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[WorldGenInfo.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    def _update_proto_references(self, proto: pd_worldgen_pb2.WorldGenInfo):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])