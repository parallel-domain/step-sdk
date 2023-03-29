from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class SourceMaps(_message.Message):
    __slots__ = ["artifact_key", "avoid_overlap_production_locations", "code_build_artifact_uid", "map_sector", "osm_branch", "osm_feature_search", "osmcell_uid", "output_artifact_uid", "parent_region", "restrict_to_elevation_data", "source_location_seed", "total_maps", "zoom_level"]
    class MapSector(_message.Message):
        __slots__ = ["map_sector_key", "map_sector_uid"]
        MAP_SECTOR_KEY_FIELD_NUMBER: ClassVar[int]
        MAP_SECTOR_UID_FIELD_NUMBER: ClassVar[int]
        map_sector_key: str
        map_sector_uid: str
        def __init__(self, map_sector_key: Optional[str] = ..., map_sector_uid: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    AVOID_OVERLAP_PRODUCTION_LOCATIONS_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    MAP_SECTOR_FIELD_NUMBER: ClassVar[int]
    OSMCELL_UID_FIELD_NUMBER: ClassVar[int]
    OSM_BRANCH_FIELD_NUMBER: ClassVar[int]
    OSM_FEATURE_SEARCH_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    PARENT_REGION_FIELD_NUMBER: ClassVar[int]
    RESTRICT_TO_ELEVATION_DATA_FIELD_NUMBER: ClassVar[int]
    SOURCE_LOCATION_SEED_FIELD_NUMBER: ClassVar[int]
    TOTAL_MAPS_FIELD_NUMBER: ClassVar[int]
    ZOOM_LEVEL_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    avoid_overlap_production_locations: bool
    code_build_artifact_uid: str
    map_sector: SourceMaps.MapSector
    osm_branch: str
    osm_feature_search: str
    osmcell_uid: str
    output_artifact_uid: str
    parent_region: str
    restrict_to_elevation_data: bool
    source_location_seed: int
    total_maps: int
    zoom_level: int
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., map_sector: Optional[Union[SourceMaps.MapSector, Mapping]] = ..., code_build_artifact_uid: Optional[str] = ..., osm_branch: Optional[str] = ..., osm_feature_search: Optional[str] = ..., zoom_level: Optional[int] = ..., total_maps: Optional[int] = ..., parent_region: Optional[str] = ..., avoid_overlap_production_locations: bool = ..., restrict_to_elevation_data: bool = ..., source_location_seed: Optional[int] = ..., osmcell_uid: Optional[str] = ...) -> None: ...
