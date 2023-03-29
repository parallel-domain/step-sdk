from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class LevelCookInfo(_message.Message):
    __slots__ = ["artifact_key", "location_list", "output_artifact_uid"]
    class Location(_message.Message):
        __slots__ = ["artifact_key", "location_name", "output_artifact_uid"]
        ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
        LOCATION_NAME_FIELD_NUMBER: ClassVar[int]
        OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
        artifact_key: str
        location_name: str
        output_artifact_uid: str
        def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., location_name: Optional[str] = ...) -> None: ...
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    LOCATION_LIST_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    location_list: _containers.RepeatedCompositeFieldContainer[LevelCookInfo.Location]
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., location_list: Optional[Iterable[Union[LevelCookInfo.Location, Mapping]]] = ...) -> None: ...
