from __future__ import annotations
from typing import Optional
from .utils import (
    register_wrapper,
    ProtoMessageClass
)
from ..python import (
    pd_post_process_pb2
)


@register_wrapper(proto_type=pd_post_process_pb2.QAProcessor)
class QAProcessor(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        batch_size: :attr:`batch_size`
    Attributes:
        artifact_key: Artifact key provided by the user during submission from webapp UI
        input_artifact_uid: Input artifact uid for the post process
        output_artifact_uid: Output artifact uid for the post process
        batch_size: Batch size specified for bundling scenes (execute serially on a pod)"""

    _proto_message = pd_post_process_pb2.QAProcessor

    def __init__(
        self,
        *,
        proto: Optional[pd_post_process_pb2.QAProcessor] = None,
        artifact_key: str = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        batch_size: int = None,
    ):
        if proto is None:
            proto = pd_post_process_pb2.QAProcessor()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if batch_size is not None:
            self.batch_size = batch_size

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    def _update_proto_references(self, proto: pd_post_process_pb2.QAProcessor):
        self.proto = proto


@register_wrapper(proto_type=pd_post_process_pb2.FieldEncoder)
class FieldEncoder(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        batch_size: :attr:`batch_size`
        encoder_script: :attr:`encoder_script`
        finalize_script: :attr:`finalize_script`
        field_container: :attr:`field_container`
        options: :attr:`options`
        enable_gpu_node: :attr:`enable_gpu_node`
        is_lec_encoder: :attr:`is_lec_encoder`
    Attributes:
        artifact_key: Artifact key provided by the user during submission from webapp UI
        input_artifact_uid: Input artifact uid for the field encoder script
        output_artifact_uid: Output artifact uid for the field encoder script
        batch_size: Batch size specified for bundling scenes (execute serially on a pod)
        encoder_script: Field script to run for scene conversion
        finalize_script:
        field_container: Container to deploy for processing
        options: options to pass to encoder
        enable_gpu_node: Enable GPU support on nodes for this encoder
        is_lec_encoder: Flag to check if this is a LEC encoding"""

    _proto_message = pd_post_process_pb2.FieldEncoder

    def __init__(
        self,
        *,
        proto: Optional[pd_post_process_pb2.FieldEncoder] = None,
        artifact_key: str = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        batch_size: int = None,
        encoder_script: str = None,
        finalize_script: str = None,
        field_container: str = None,
        options: str = None,
        enable_gpu_node: bool = None,
        is_lec_encoder: bool = None,
    ):
        if proto is None:
            proto = pd_post_process_pb2.FieldEncoder()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if batch_size is not None:
            self.batch_size = batch_size
        if encoder_script is not None:
            self.encoder_script = encoder_script
        if finalize_script is not None:
            self.finalize_script = finalize_script
        if field_container is not None:
            self.field_container = field_container
        if options is not None:
            self.options = options
        if enable_gpu_node is not None:
            self.enable_gpu_node = enable_gpu_node
        if is_lec_encoder is not None:
            self.is_lec_encoder = is_lec_encoder

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def encoder_script(self) -> str:
        return self.proto.encoder_script

    @encoder_script.setter
    def encoder_script(self, value: str):
        self.proto.encoder_script = value

    @property
    def finalize_script(self) -> str:
        return self.proto.finalize_script

    @finalize_script.setter
    def finalize_script(self, value: str):
        self.proto.finalize_script = value

    @property
    def field_container(self) -> str:
        return self.proto.field_container

    @field_container.setter
    def field_container(self, value: str):
        self.proto.field_container = value

    @property
    def options(self) -> str:
        return self.proto.options

    @options.setter
    def options(self, value: str):
        self.proto.options = value

    @property
    def enable_gpu_node(self) -> bool:
        return self.proto.enable_gpu_node

    @enable_gpu_node.setter
    def enable_gpu_node(self, value: bool):
        self.proto.enable_gpu_node = value

    @property
    def is_lec_encoder(self) -> bool:
        return self.proto.is_lec_encoder

    @is_lec_encoder.setter
    def is_lec_encoder(self, value: bool):
        self.proto.is_lec_encoder = value

    def _update_proto_references(self, proto: pd_post_process_pb2.FieldEncoder):
        self.proto = proto


@register_wrapper(proto_type=pd_post_process_pb2.LEEncoder)
class LEEncoder(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        batch_size: :attr:`batch_size`
        encoder_script: :attr:`encoder_script`
        finalize_script: :attr:`finalize_script`
        le_container: :attr:`le_container`
        options: :attr:`options`
        enable_gpu_node: :attr:`enable_gpu_node`
    Attributes:
        artifact_key: Artifact key provided by the user during submission from webapp UI
        input_artifact_uid: Input artifact uid for the field encoder script
        output_artifact_uid: Output artifact uid for the field encoder script
        batch_size: Batch size specified for bundling scenes (execute serially on a pod)
        encoder_script: Field script to run for scene conversion
        finalize_script:
        le_container: Container to deploy for processing
        options: options to pass to encoder
        enable_gpu_node: Enable GPU support on nodes for this encoder"""

    _proto_message = pd_post_process_pb2.LEEncoder

    def __init__(
        self,
        *,
        proto: Optional[pd_post_process_pb2.LEEncoder] = None,
        artifact_key: str = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        batch_size: int = None,
        encoder_script: str = None,
        finalize_script: str = None,
        le_container: str = None,
        options: str = None,
        enable_gpu_node: bool = None,
    ):
        if proto is None:
            proto = pd_post_process_pb2.LEEncoder()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if batch_size is not None:
            self.batch_size = batch_size
        if encoder_script is not None:
            self.encoder_script = encoder_script
        if finalize_script is not None:
            self.finalize_script = finalize_script
        if le_container is not None:
            self.le_container = le_container
        if options is not None:
            self.options = options
        if enable_gpu_node is not None:
            self.enable_gpu_node = enable_gpu_node

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def encoder_script(self) -> str:
        return self.proto.encoder_script

    @encoder_script.setter
    def encoder_script(self, value: str):
        self.proto.encoder_script = value

    @property
    def finalize_script(self) -> str:
        return self.proto.finalize_script

    @finalize_script.setter
    def finalize_script(self, value: str):
        self.proto.finalize_script = value

    @property
    def le_container(self) -> str:
        return self.proto.le_container

    @le_container.setter
    def le_container(self, value: str):
        self.proto.le_container = value

    @property
    def options(self) -> str:
        return self.proto.options

    @options.setter
    def options(self, value: str):
        self.proto.options = value

    @property
    def enable_gpu_node(self) -> bool:
        return self.proto.enable_gpu_node

    @enable_gpu_node.setter
    def enable_gpu_node(self, value: bool):
        self.proto.enable_gpu_node = value

    def _update_proto_references(self, proto: pd_post_process_pb2.LEEncoder):
        self.proto = proto


@register_wrapper(proto_type=pd_post_process_pb2.AgentFilter)
class AgentFilter(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        input_artifact_uid: :attr:`input_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        batch_size: :attr:`batch_size`
    Attributes:
        artifact_key: Artifact key provided by the user during submission from webapp UI
        input_artifact_uid: Input artifact uid for the field encoder script
        output_artifact_uid: Output artifact uid for the field encoder script
        batch_size: Batch size specified for bundling scenes (execute serially on a pod)"""

    _proto_message = pd_post_process_pb2.AgentFilter

    def __init__(
        self,
        *,
        proto: Optional[pd_post_process_pb2.AgentFilter] = None,
        artifact_key: str = None,
        input_artifact_uid: str = None,
        output_artifact_uid: str = None,
        batch_size: int = None,
    ):
        if proto is None:
            proto = pd_post_process_pb2.AgentFilter()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if batch_size is not None:
            self.batch_size = batch_size

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    def _update_proto_references(self, proto: pd_post_process_pb2.AgentFilter):
        self.proto = proto


@register_wrapper(proto_type=pd_post_process_pb2.ExtractAgentData)
class ExtractAgentData(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        ground_truth_artifact_uid: :attr:`ground_truth_artifact_uid`
        filtered_artifact_uid: :attr:`filtered_artifact_uid`
        filter_info_artifact_uid: :attr:`filter_info_artifact_uid`
        output_artifact_uid: :attr:`output_artifact_uid`
        batch_size: :attr:`batch_size`
    Attributes:
        artifact_key: Artifact key provided by the user during submission from webapp UI
        ground_truth_artifact_uid: Input artifact uid for the ground truth dataset
        filtered_artifact_uid: Input artifact uid for the filtered dataset
        filter_info_artifact_uid: Input artifact uid for the filtering info
        output_artifact_uid: Output artifact uid for the field encoder script
        batch_size: Batch size specified for bundling scenes (execute serially on a pod)"""

    _proto_message = pd_post_process_pb2.ExtractAgentData

    def __init__(
        self,
        *,
        proto: Optional[pd_post_process_pb2.ExtractAgentData] = None,
        artifact_key: str = None,
        ground_truth_artifact_uid: str = None,
        filtered_artifact_uid: str = None,
        filter_info_artifact_uid: str = None,
        output_artifact_uid: str = None,
        batch_size: int = None,
    ):
        if proto is None:
            proto = pd_post_process_pb2.ExtractAgentData()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if ground_truth_artifact_uid is not None:
            self.ground_truth_artifact_uid = ground_truth_artifact_uid
        if filtered_artifact_uid is not None:
            self.filtered_artifact_uid = filtered_artifact_uid
        if filter_info_artifact_uid is not None:
            self.filter_info_artifact_uid = filter_info_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if batch_size is not None:
            self.batch_size = batch_size

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def ground_truth_artifact_uid(self) -> str:
        return self.proto.ground_truth_artifact_uid

    @ground_truth_artifact_uid.setter
    def ground_truth_artifact_uid(self, value: str):
        self.proto.ground_truth_artifact_uid = value

    @property
    def filtered_artifact_uid(self) -> str:
        return self.proto.filtered_artifact_uid

    @filtered_artifact_uid.setter
    def filtered_artifact_uid(self, value: str):
        self.proto.filtered_artifact_uid = value

    @property
    def filter_info_artifact_uid(self) -> str:
        return self.proto.filter_info_artifact_uid

    @filter_info_artifact_uid.setter
    def filter_info_artifact_uid(self, value: str):
        self.proto.filter_info_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    def _update_proto_references(self, proto: pd_post_process_pb2.ExtractAgentData):
        self.proto = proto
