from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackageMapsFromP4(_message.Message):
    __slots__ = ["artifact_key", "base_changelist", "code_build_artifact_uid", "map_list", "output_artifact_uid", "unshelve_changelist"]
    class Map(_message.Message):
        __slots__ = ["elevation_path", "geojson_path", "input_file_path", "map_name", "map_output_artifact_uid", "parameters_path"]
        ELEVATION_PATH_FIELD_NUMBER: ClassVar[int]
        GEOJSON_PATH_FIELD_NUMBER: ClassVar[int]
        INPUT_FILE_PATH_FIELD_NUMBER: ClassVar[int]
        MAP_NAME_FIELD_NUMBER: ClassVar[int]
        MAP_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        PARAMETERS_PATH_FIELD_NUMBER: ClassVar[int]
        elevation_path: str
        geojson_path: str
        input_file_path: str
        map_name: str
        map_output_artifact_uid: str
        parameters_path: str
        def __init__(self, map_output_artifact_uid: Optional[str] = ..., map_name: Optional[str] = ..., parameters_path: Optional[str] = ..., input_file_path: Optional[str] = ..., geojson_path: Optional[str] = ..., elevation_path: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BASE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    MAP_LIST_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    UNSHELVE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    base_changelist: str
    code_build_artifact_uid: str
    map_list: _containers.RepeatedCompositeFieldContainer[PackageMapsFromP4.Map]
    output_artifact_uid: str
    unshelve_changelist: str
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., base_changelist: Optional[str] = ..., unshelve_changelist: Optional[str] = ..., map_list: Optional[Iterable[Union[PackageMapsFromP4.Map, Mapping]]] = ...) -> None: ...
