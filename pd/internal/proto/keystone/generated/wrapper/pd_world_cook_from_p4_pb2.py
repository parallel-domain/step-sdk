from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_world_cook_from_p4_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_world_cook_from_p4_pb2.WorldCookFromP4Info)
class WorldCookFromP4Info(ProtoMessageClass):
    _proto_message = pd_world_cook_from_p4_pb2.WorldCookFromP4Info

    def __init__(self, *, proto: Optional[pd_world_cook_from_p4_pb2.WorldCookFromP4Info]=None, artifact_key: Optional[str]=None, base_changelist: Optional[str]=None, code_build_artifact_uid: Optional[str]=None, location_list: Optional[List[WorldCookFromP4Info.Location]]=None, output_artifact_uid: Optional[str]=None, unshelve_changelist: Optional[str]=None):
        if proto is None:
            proto = pd_world_cook_from_p4_pb2.WorldCookFromP4Info()
        self.proto = proto
        self._location_list = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.location_list], attr_name='location_list', list_owner=self)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if base_changelist is not None:
            self.base_changelist = base_changelist
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if location_list is not None:
            self.location_list = location_list
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if unshelve_changelist is not None:
            self.unshelve_changelist = unshelve_changelist

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def base_changelist(self) -> str:
        return self.proto.base_changelist

    @base_changelist.setter
    def base_changelist(self, value: str):
        self.proto.base_changelist = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def location_list(self) -> List[WorldCookFromP4Info.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[WorldCookFromP4Info.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def unshelve_changelist(self) -> str:
        return self.proto.unshelve_changelist

    @unshelve_changelist.setter
    def unshelve_changelist(self, value: str):
        self.proto.unshelve_changelist = value

    def _update_proto_references(self, proto: pd_world_cook_from_p4_pb2.WorldCookFromP4Info):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])