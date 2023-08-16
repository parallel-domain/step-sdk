from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class WorldBuildInfo(_message.Message):
    __slots__ = ["artifact_key", "base_changelist", "code_build_artifact_uid", "do_houdini_only", "image_generator_core_artifact_uid", "levelcook_batch_size", "location_list", "output_artifact_uid", "qa_render", "unshelve_changelist", "world_preview_uid"]
    class Location(_message.Message):
        __slots__ = ["artifact_key", "geojson_path", "image_gen_level_artifact_uid", "imported_level_output_artifact_uid", "input_file_path", "location_name", "location_output_artifact_uid", "parameters_path", "worldgen_output_artifact_uid"]
        ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
        GEOJSON_PATH_FIELD_NUMBER: ClassVar[int]
        IMAGE_GEN_LEVEL_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        IMPORTED_LEVEL_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        INPUT_FILE_PATH_FIELD_NUMBER: ClassVar[int]
        LOCATION_NAME_FIELD_NUMBER: ClassVar[int]
        LOCATION_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        PARAMETERS_PATH_FIELD_NUMBER: ClassVar[int]
        WORLDGEN_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        artifact_key: str
        geojson_path: str
        image_gen_level_artifact_uid: str
        imported_level_output_artifact_uid: str
        input_file_path: str
        location_name: str
        location_output_artifact_uid: str
        parameters_path: str
        worldgen_output_artifact_uid: str
        def __init__(self, artifact_key: Optional[str] = ..., location_output_artifact_uid: Optional[str] = ..., worldgen_output_artifact_uid: Optional[str] = ..., imported_level_output_artifact_uid: Optional[str] = ..., image_gen_level_artifact_uid: Optional[str] = ..., location_name: Optional[str] = ..., parameters_path: Optional[str] = ..., input_file_path: Optional[str] = ..., geojson_path: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BASE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    DO_HOUDINI_ONLY_FIELD_NUMBER: ClassVar[int]
    IMAGE_GENERATOR_CORE_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    LEVELCOOK_BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    LOCATION_LIST_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    QA_RENDER_FIELD_NUMBER: ClassVar[int]
    UNSHELVE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    WORLD_PREVIEW_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    base_changelist: str
    code_build_artifact_uid: str
    do_houdini_only: bool
    image_generator_core_artifact_uid: str
    levelcook_batch_size: int
    location_list: _containers.RepeatedCompositeFieldContainer[WorldBuildInfo.Location]
    output_artifact_uid: str
    qa_render: bool
    unshelve_changelist: str
    world_preview_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., base_changelist: Optional[str] = ..., unshelve_changelist: Optional[str] = ..., qa_render: bool = ..., image_generator_core_artifact_uid: Optional[str] = ..., world_preview_uid: Optional[str] = ..., levelcook_batch_size: Optional[int] = ..., do_houdini_only: bool = ..., location_list: Optional[Iterable[Union[WorldBuildInfo.Location, Mapping]]] = ...) -> None: ...
