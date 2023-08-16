from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_post_process_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_post_process_pb2.AgentFilter)
class AgentFilter(ProtoMessageClass):
    _proto_message = pd_post_process_pb2.AgentFilter

    def __init__(self, *, proto: Optional[pd_post_process_pb2.AgentFilter]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, input_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_post_process_pb2.AgentFilter()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

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

    def _update_proto_references(self, proto: pd_post_process_pb2.AgentFilter):
        self.proto = proto

@register_wrapper(proto_type=pd_post_process_pb2.ExtractAgentData)
class ExtractAgentData(ProtoMessageClass):
    _proto_message = pd_post_process_pb2.ExtractAgentData

    def __init__(self, *, proto: Optional[pd_post_process_pb2.ExtractAgentData]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, filter_info_artifact_uid: Optional[str]=None, filtered_artifact_uid: Optional[str]=None, ground_truth_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_post_process_pb2.ExtractAgentData()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if filter_info_artifact_uid is not None:
            self.filter_info_artifact_uid = filter_info_artifact_uid
        if filtered_artifact_uid is not None:
            self.filtered_artifact_uid = filtered_artifact_uid
        if ground_truth_artifact_uid is not None:
            self.ground_truth_artifact_uid = ground_truth_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def filter_info_artifact_uid(self) -> str:
        return self.proto.filter_info_artifact_uid

    @filter_info_artifact_uid.setter
    def filter_info_artifact_uid(self, value: str):
        self.proto.filter_info_artifact_uid = value

    @property
    def filtered_artifact_uid(self) -> str:
        return self.proto.filtered_artifact_uid

    @filtered_artifact_uid.setter
    def filtered_artifact_uid(self, value: str):
        self.proto.filtered_artifact_uid = value

    @property
    def ground_truth_artifact_uid(self) -> str:
        return self.proto.ground_truth_artifact_uid

    @ground_truth_artifact_uid.setter
    def ground_truth_artifact_uid(self, value: str):
        self.proto.ground_truth_artifact_uid = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    def _update_proto_references(self, proto: pd_post_process_pb2.ExtractAgentData):
        self.proto = proto

@register_wrapper(proto_type=pd_post_process_pb2.FieldEncoder)
class FieldEncoder(ProtoMessageClass):
    _proto_message = pd_post_process_pb2.FieldEncoder

    def __init__(self, *, proto: Optional[pd_post_process_pb2.FieldEncoder]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, enable_gpu_node: Optional[bool]=None, encoder_script: Optional[str]=None, field_container: Optional[str]=None, finalize_script: Optional[str]=None, input_artifact_uid: Optional[str]=None, is_lec_encoder: Optional[bool]=None, options: Optional[str]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_post_process_pb2.FieldEncoder()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if enable_gpu_node is not None:
            self.enable_gpu_node = enable_gpu_node
        if encoder_script is not None:
            self.encoder_script = encoder_script
        if field_container is not None:
            self.field_container = field_container
        if finalize_script is not None:
            self.finalize_script = finalize_script
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if is_lec_encoder is not None:
            self.is_lec_encoder = is_lec_encoder
        if options is not None:
            self.options = options
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def enable_gpu_node(self) -> bool:
        return self.proto.enable_gpu_node

    @enable_gpu_node.setter
    def enable_gpu_node(self, value: bool):
        self.proto.enable_gpu_node = value

    @property
    def encoder_script(self) -> str:
        return self.proto.encoder_script

    @encoder_script.setter
    def encoder_script(self, value: str):
        self.proto.encoder_script = value

    @property
    def field_container(self) -> str:
        return self.proto.field_container

    @field_container.setter
    def field_container(self, value: str):
        self.proto.field_container = value

    @property
    def finalize_script(self) -> str:
        return self.proto.finalize_script

    @finalize_script.setter
    def finalize_script(self, value: str):
        self.proto.finalize_script = value

    @property
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

    @property
    def is_lec_encoder(self) -> bool:
        return self.proto.is_lec_encoder

    @is_lec_encoder.setter
    def is_lec_encoder(self, value: bool):
        self.proto.is_lec_encoder = value

    @property
    def options(self) -> str:
        return self.proto.options

    @options.setter
    def options(self, value: str):
        self.proto.options = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    def _update_proto_references(self, proto: pd_post_process_pb2.FieldEncoder):
        self.proto = proto

@register_wrapper(proto_type=pd_post_process_pb2.LEEncoder)
class LEEncoder(ProtoMessageClass):
    _proto_message = pd_post_process_pb2.LEEncoder

    def __init__(self, *, proto: Optional[pd_post_process_pb2.LEEncoder]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, enable_gpu_node: Optional[bool]=None, encoder_script: Optional[str]=None, finalize_script: Optional[str]=None, input_artifact_uid: Optional[str]=None, le_container: Optional[str]=None, options: Optional[str]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_post_process_pb2.LEEncoder()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if enable_gpu_node is not None:
            self.enable_gpu_node = enable_gpu_node
        if encoder_script is not None:
            self.encoder_script = encoder_script
        if finalize_script is not None:
            self.finalize_script = finalize_script
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if le_container is not None:
            self.le_container = le_container
        if options is not None:
            self.options = options
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def enable_gpu_node(self) -> bool:
        return self.proto.enable_gpu_node

    @enable_gpu_node.setter
    def enable_gpu_node(self, value: bool):
        self.proto.enable_gpu_node = value

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
    def input_artifact_uid(self) -> str:
        return self.proto.input_artifact_uid

    @input_artifact_uid.setter
    def input_artifact_uid(self, value: str):
        self.proto.input_artifact_uid = value

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
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    def _update_proto_references(self, proto: pd_post_process_pb2.LEEncoder):
        self.proto = proto

@register_wrapper(proto_type=pd_post_process_pb2.QAProcessor)
class QAProcessor(ProtoMessageClass):
    _proto_message = pd_post_process_pb2.QAProcessor

    def __init__(self, *, proto: Optional[pd_post_process_pb2.QAProcessor]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, input_artifact_uid: Optional[str]=None, output_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_post_process_pb2.QAProcessor()
        self.proto = proto
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if input_artifact_uid is not None:
            self.input_artifact_uid = input_artifact_uid
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

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

    def _update_proto_references(self, proto: pd_post_process_pb2.QAProcessor):
        self.proto = proto