from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Recook(_message.Message):
    __slots__ = ["artifact_key", "base_changelist", "code_build_artifact_uid", "do_reimport", "levelcook_batch_size", "location_list", "output_artifact_uid", "unshelve_changelist"]
    class Location(_message.Message):
        __slots__ = ["location_guid", "location_name", "location_output_artifact_uid"]
        LOCATION_GUID_FIELD_NUMBER: ClassVar[int]
        LOCATION_NAME_FIELD_NUMBER: ClassVar[int]
        LOCATION_OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        location_guid: str
        location_name: str
        location_output_artifact_uid: str
        def __init__(self, location_output_artifact_uid: Optional[str] = ..., location_name: Optional[str] = ..., location_guid: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BASE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    DO_REIMPORT_FIELD_NUMBER: ClassVar[int]
    LEVELCOOK_BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    LOCATION_LIST_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    UNSHELVE_CHANGELIST_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    base_changelist: str
    code_build_artifact_uid: str
    do_reimport: bool
    levelcook_batch_size: int
    location_list: _containers.RepeatedCompositeFieldContainer[Recook.Location]
    output_artifact_uid: str
    unshelve_changelist: str
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., base_changelist: Optional[str] = ..., unshelve_changelist: Optional[str] = ..., levelcook_batch_size: Optional[int] = ..., do_reimport: bool = ..., location_list: Optional[Iterable[Union[Recook.Location, Mapping]]] = ...) -> None: ...
