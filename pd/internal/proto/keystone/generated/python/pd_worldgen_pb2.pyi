from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldGenInfo(_message.Message):
    __slots__ = ["artifact_key", "location_list", "output_artifact_uid"]
    class Location(_message.Message):
        __slots__ = ["artifact_key", "code_build_artifact_uid", "geojson_path", "imported_level_output_artifact_uid", "input_file_path", "location_name", "parameters_path", "worldgen_output_artifact_uid"]
        ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
        CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        GEOJSON_PATH_FIELD_NUMBER: ClassVar[int]
        IMPORTED_LEVEL_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        INPUT_FILE_PATH_FIELD_NUMBER: ClassVar[int]
        LOCATION_NAME_FIELD_NUMBER: ClassVar[int]
        PARAMETERS_PATH_FIELD_NUMBER: ClassVar[int]
        WORLDGEN_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        artifact_key: str
        code_build_artifact_uid: str
        geojson_path: str
        imported_level_output_artifact_uid: str
        input_file_path: str
        location_name: str
        parameters_path: str
        worldgen_output_artifact_uid: str
        def __init__(self, artifact_key: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., worldgen_output_artifact_uid: Optional[str] = ..., imported_level_output_artifact_uid: Optional[str] = ..., location_name: Optional[str] = ..., parameters_path: Optional[str] = ..., input_file_path: Optional[str] = ..., geojson_path: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    LOCATION_LIST_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    location_list: _containers.RepeatedCompositeFieldContainer[WorldGenInfo.Location]
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., location_list: Optional[Iterable[Union[WorldGenInfo.Location, Mapping]]] = ...) -> None: ...
