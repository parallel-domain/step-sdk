from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_source_maps_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_source_maps_pb2.SourceMaps)
class SourceMaps(ProtoMessageClass):
    _proto_message = pd_source_maps_pb2.SourceMaps

    def __init__(self, *, proto: Optional[pd_source_maps_pb2.SourceMaps]=None, artifact_key: Optional[str]=None, avoid_overlap_production_locations: Optional[bool]=None, code_build_artifact_uid: Optional[str]=None, map_sector: Optional[SourceMaps.MapSector]=None, osm_branch: Optional[str]=None, osm_feature_search: Optional[str]=None, osmcell_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None, parent_region: Optional[str]=None, restrict_to_elevation_data: Optional[bool]=None, source_location_seed: Optional[int]=None, total_maps: Optional[int]=None, zoom_level: Optional[int]=None):
        if proto is None:
            proto = pd_source_maps_pb2.SourceMaps()
        self.proto = proto
        self._map_sector = get_wrapper(proto_type=proto.map_sector.__class__)(proto=proto.map_sector)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if avoid_overlap_production_locations is not None:
            self.avoid_overlap_production_locations = avoid_overlap_production_locations
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if map_sector is not None:
            self.map_sector = map_sector
        if osm_branch is not None:
            self.osm_branch = osm_branch
        if osm_feature_search is not None:
            self.osm_feature_search = osm_feature_search
        if osmcell_uid is not None:
            self.osmcell_uid = osmcell_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if parent_region is not None:
            self.parent_region = parent_region
        if restrict_to_elevation_data is not None:
            self.restrict_to_elevation_data = restrict_to_elevation_data
        if source_location_seed is not None:
            self.source_location_seed = source_location_seed
        if total_maps is not None:
            self.total_maps = total_maps
        if zoom_level is not None:
            self.zoom_level = zoom_level

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def avoid_overlap_production_locations(self) -> bool:
        return self.proto.avoid_overlap_production_locations

    @avoid_overlap_production_locations.setter
    def avoid_overlap_production_locations(self, value: bool):
        self.proto.avoid_overlap_production_locations = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def map_sector(self) -> SourceMaps.MapSector:
        return self._map_sector

    @map_sector.setter
    def map_sector(self, value: SourceMaps.MapSector):
        self.proto.map_sector.CopyFrom(value.proto)
        
        self._map_sector = value
        self._map_sector._update_proto_references(self.proto.map_sector)

    @property
    def osm_branch(self) -> str:
        return self.proto.osm_branch

    @osm_branch.setter
    def osm_branch(self, value: str):
        self.proto.osm_branch = value

    @property
    def osm_feature_search(self) -> str:
        return self.proto.osm_feature_search

    @osm_feature_search.setter
    def osm_feature_search(self, value: str):
        self.proto.osm_feature_search = value

    @property
    def osmcell_uid(self) -> str:
        return self.proto.osmcell_uid

    @osmcell_uid.setter
    def osmcell_uid(self, value: str):
        self.proto.osmcell_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def parent_region(self) -> str:
        return self.proto.parent_region

    @parent_region.setter
    def parent_region(self, value: str):
        self.proto.parent_region = value

    @property
    def restrict_to_elevation_data(self) -> bool:
        return self.proto.restrict_to_elevation_data

    @restrict_to_elevation_data.setter
    def restrict_to_elevation_data(self, value: bool):
        self.proto.restrict_to_elevation_data = value

    @property
    def source_location_seed(self) -> int:
        return self.proto.source_location_seed

    @source_location_seed.setter
    def source_location_seed(self, value: int):
        self.proto.source_location_seed = value

    @property
    def total_maps(self) -> int:
        return self.proto.total_maps

    @total_maps.setter
    def total_maps(self, value: int):
        self.proto.total_maps = value

    @property
    def zoom_level(self) -> int:
        return self.proto.zoom_level

    @zoom_level.setter
    def zoom_level(self, value: int):
        self.proto.zoom_level = value

    def _update_proto_references(self, proto: pd_source_maps_pb2.SourceMaps):
        self.proto = proto
        self._map_sector._update_proto_references(proto.map_sector)