from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AgentFilter(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "input_artifact_uid", "output_artifact_uid"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    input_artifact_uid: str
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., batch_size: Optional[int] = ...) -> None: ...

class ExtractAgentData(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "filter_info_artifact_uid", "filtered_artifact_uid", "ground_truth_artifact_uid", "output_artifact_uid"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    FILTERED_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    FILTER_INFO_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    GROUND_TRUTH_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    filter_info_artifact_uid: str
    filtered_artifact_uid: str
    ground_truth_artifact_uid: str
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., ground_truth_artifact_uid: Optional[str] = ..., filtered_artifact_uid: Optional[str] = ..., filter_info_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., batch_size: Optional[int] = ...) -> None: ...

class FieldEncoder(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "enable_gpu_node", "encoder_script", "field_container", "finalize_script", "input_artifact_uid", "is_lec_encoder", "options", "output_artifact_uid"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    ENABLE_GPU_NODE_FIELD_NUMBER: ClassVar[int]
    ENCODER_SCRIPT_FIELD_NUMBER: ClassVar[int]
    FIELD_CONTAINER_FIELD_NUMBER: ClassVar[int]
    FINALIZE_SCRIPT_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    IS_LEC_ENCODER_FIELD_NUMBER: ClassVar[int]
    OPTIONS_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    enable_gpu_node: bool
    encoder_script: str
    field_container: str
    finalize_script: str
    input_artifact_uid: str
    is_lec_encoder: bool
    options: str
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., batch_size: Optional[int] = ..., encoder_script: Optional[str] = ..., finalize_script: Optional[str] = ..., field_container: Optional[str] = ..., options: Optional[str] = ..., enable_gpu_node: bool = ..., is_lec_encoder: bool = ...) -> None: ...

class LEEncoder(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "enable_gpu_node", "encoder_script", "finalize_script", "input_artifact_uid", "le_container", "options", "output_artifact_uid"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    ENABLE_GPU_NODE_FIELD_NUMBER: ClassVar[int]
    ENCODER_SCRIPT_FIELD_NUMBER: ClassVar[int]
    FINALIZE_SCRIPT_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    LE_CONTAINER_FIELD_NUMBER: ClassVar[int]
    OPTIONS_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    enable_gpu_node: bool
    encoder_script: str
    finalize_script: str
    input_artifact_uid: str
    le_container: str
    options: str
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., batch_size: Optional[int] = ..., encoder_script: Optional[str] = ..., finalize_script: Optional[str] = ..., le_container: Optional[str] = ..., options: Optional[str] = ..., enable_gpu_node: bool = ...) -> None: ...

class QAProcessor(_message.Message):
    __slots__ = ["artifact_key", "batch_size", "input_artifact_uid", "output_artifact_uid"]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    INPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    artifact_key: str
    batch_size: int
    input_artifact_uid: str
    output_artifact_uid: str
    def __init__(self, artifact_key: Optional[str] = ..., input_artifact_uid: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., batch_size: Optional[int] = ...) -> None: ...
