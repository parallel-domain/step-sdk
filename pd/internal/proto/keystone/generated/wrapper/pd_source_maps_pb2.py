from __future__ import annotations
from typing import Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass
)
from ..python import (
    pd_source_maps_pb2
)


@register_wrapper(proto_type=pd_source_maps_pb2.SourceMaps)
class SourceMaps(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        map_sector: :attr:`map_sector`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        osm_branch: :attr:`osm_branch`
        osm_feature_search: :attr:`osm_feature_search`
        zoom_level: :attr:`zoom_level`
        total_maps: :attr:`total_maps`
        parent_region: :attr:`parent_region`
        avoid_overlap_production_locations: :attr:`avoid_overlap_production_locations`
        restrict_to_elevation_data: :attr:`restrict_to_elevation_data`
        source_location_seed: :attr:`source_location_seed`
        osmcell_uid: :attr:`osmcell_uid`
    Attributes:
        artifact_key:
        output_artifact_uid:
        map_sector:
        code_build_artifact_uid:
        osm_branch:
        osm_feature_search:
        zoom_level:
        total_maps:
        parent_region:
        avoid_overlap_production_locations:
        restrict_to_elevation_data:
        source_location_seed:
        osmcell_uid:"""

    @register_wrapper(proto_type=pd_source_maps_pb2.SourceMaps.MapSector)
    class MapSector(ProtoMessageClass):
        """
        Args:
            map_sector_key: :attr:`map_sector_key`
            map_sector_uid: :attr:`map_sector_uid`
        Attributes:
            map_sector_key:
            map_sector_uid:"""

        _proto_message = pd_source_maps_pb2.SourceMaps.MapSector

        def __init__(
            self,
            *,
            proto: Optional[pd_source_maps_pb2.SourceMaps.MapSector] = None,
            map_sector_key: str = None,
            map_sector_uid: str = None,
        ):
            if proto is None:
                proto = pd_source_maps_pb2.SourceMaps.MapSector()
            self.proto = proto
            if map_sector_key is not None:
                self.map_sector_key = map_sector_key
            if map_sector_uid is not None:
                self.map_sector_uid = map_sector_uid

        @property
        def map_sector_key(self) -> str:
            return self.proto.map_sector_key

        @map_sector_key.setter
        def map_sector_key(self, value: str):
            self.proto.map_sector_key = value

        @property
        def map_sector_uid(self) -> str:
            return self.proto.map_sector_uid

        @map_sector_uid.setter
        def map_sector_uid(self, value: str):
            self.proto.map_sector_uid = value

        def _update_proto_references(self, proto: pd_source_maps_pb2.SourceMaps.MapSector):
            self.proto = proto

    _proto_message = pd_source_maps_pb2.SourceMaps

    def __init__(
        self,
        *,
        proto: Optional[pd_source_maps_pb2.SourceMaps] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        map_sector: SourceMaps.MapSector = None,
        code_build_artifact_uid: str = None,
        osm_branch: str = None,
        osm_feature_search: str = None,
        zoom_level: int = None,
        total_maps: int = None,
        parent_region: str = None,
        avoid_overlap_production_locations: bool = None,
        restrict_to_elevation_data: bool = None,
        source_location_seed: int = None,
        osmcell_uid: str = None,
    ):
        if proto is None:
            proto = pd_source_maps_pb2.SourceMaps()
        self.proto = proto
        self._map_sector = get_wrapper(proto_type=proto.map_sector.__class__)(proto=proto.map_sector)
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if map_sector is not None:
            self.map_sector = map_sector
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if osm_branch is not None:
            self.osm_branch = osm_branch
        if osm_feature_search is not None:
            self.osm_feature_search = osm_feature_search
        if zoom_level is not None:
            self.zoom_level = zoom_level
        if total_maps is not None:
            self.total_maps = total_maps
        if parent_region is not None:
            self.parent_region = parent_region
        if avoid_overlap_production_locations is not None:
            self.avoid_overlap_production_locations = avoid_overlap_production_locations
        if restrict_to_elevation_data is not None:
            self.restrict_to_elevation_data = restrict_to_elevation_data
        if source_location_seed is not None:
            self.source_location_seed = source_location_seed
        if osmcell_uid is not None:
            self.osmcell_uid = osmcell_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def map_sector(self) -> SourceMaps.MapSector:
        return self._map_sector

    @map_sector.setter
    def map_sector(self, value: SourceMaps.MapSector):
        self.proto.map_sector.CopyFrom(value.proto)

        self._map_sector = value
        self._map_sector._update_proto_references(self.proto.map_sector)

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

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
    def zoom_level(self) -> int:
        return self.proto.zoom_level

    @zoom_level.setter
    def zoom_level(self, value: int):
        self.proto.zoom_level = value

    @property
    def total_maps(self) -> int:
        return self.proto.total_maps

    @total_maps.setter
    def total_maps(self, value: int):
        self.proto.total_maps = value

    @property
    def parent_region(self) -> str:
        return self.proto.parent_region

    @parent_region.setter
    def parent_region(self, value: str):
        self.proto.parent_region = value

    @property
    def avoid_overlap_production_locations(self) -> bool:
        return self.proto.avoid_overlap_production_locations

    @avoid_overlap_production_locations.setter
    def avoid_overlap_production_locations(self, value: bool):
        self.proto.avoid_overlap_production_locations = value

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
    def osmcell_uid(self) -> str:
        return self.proto.osmcell_uid

    @osmcell_uid.setter
    def osmcell_uid(self, value: str):
        self.proto.osmcell_uid = value

    def _update_proto_references(self, proto: pd_source_maps_pb2.SourceMaps):
        self.proto = proto
        self._map_sector._update_proto_references(proto.map_sector)
