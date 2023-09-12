import pd_sensor_pb2 as _pd_sensor_pb2
import pd_render_pb2 as _pd_render_pb2
import pd_scenario_pb2 as _pd_scenario_pb2
import pd_post_process_pb2 as _pd_post_process_pb2
import pd_sim_state_pb2 as _pd_sim_state_pb2
import pd_levelcook_pb2 as _pd_levelcook_pb2
import pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2
import pd_worldgen_pb2 as _pd_worldgen_pb2
import pd_worldbuild_pb2 as _pd_worldbuild_pb2
import pd_source_maps_pb2 as _pd_source_maps_pb2
import pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2
import pd_recook_pb2 as _pd_recook_pb2
import pd_step_batch_pb2 as _pd_step_batch_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class KeystoneBuildMessage(_message.Message):
    __slots__ = ["stages"]
    class PipelineStage(_message.Message):
        __slots__ = ["build_sim_state", "field_encoder", "le_encoder", "levelcook", "package_maps_from_p4", "qa_processor", "recook", "render", "sim_state_cull", "sim_state_process", "source_maps", "step_batch", "world_cook_from_p4", "worldbuild", "worldgen"]
        BUILD_SIM_STATE_FIELD_NUMBER: ClassVar[int]
        FIELD_ENCODER_FIELD_NUMBER: ClassVar[int]
        LEVELCOOK_FIELD_NUMBER: ClassVar[int]
        LE_ENCODER_FIELD_NUMBER: ClassVar[int]
        PACKAGE_MAPS_FROM_P4_FIELD_NUMBER: ClassVar[int]
        QA_PROCESSOR_FIELD_NUMBER: ClassVar[int]
        RECOOK_FIELD_NUMBER: ClassVar[int]
        RENDER_FIELD_NUMBER: ClassVar[int]
        SIM_STATE_CULL_FIELD_NUMBER: ClassVar[int]
        SIM_STATE_PROCESS_FIELD_NUMBER: ClassVar[int]
        SOURCE_MAPS_FIELD_NUMBER: ClassVar[int]
        STEP_BATCH_FIELD_NUMBER: ClassVar[int]
        WORLDBUILD_FIELD_NUMBER: ClassVar[int]
        WORLDGEN_FIELD_NUMBER: ClassVar[int]
        WORLD_COOK_FROM_P4_FIELD_NUMBER: ClassVar[int]
        build_sim_state: _pd_sim_state_pb2.BuildSimState
        field_encoder: _pd_post_process_pb2.FieldEncoder
        le_encoder: _pd_post_process_pb2.LEEncoder
        levelcook: _pd_levelcook_pb2.LevelCookInfo
        package_maps_from_p4: _pd_package_maps_from_p4_pb2.PackageMapsFromP4
        qa_processor: _pd_post_process_pb2.QAProcessor
        recook: _pd_recook_pb2.Recook
        render: _pd_render_pb2.RenderInfo
        sim_state_cull: _pd_sim_state_pb2.SimStateCull
        sim_state_process: _pd_sim_state_pb2.ProcessSimState
        source_maps: _pd_source_maps_pb2.SourceMaps
        step_batch: _pd_step_batch_pb2.StepBatch
        world_cook_from_p4: _pd_world_cook_from_p4_pb2.WorldCookFromP4Info
        worldbuild: _pd_worldbuild_pb2.WorldBuildInfo
        worldgen: _pd_worldgen_pb2.WorldGenInfo
        def __init__(self, build_sim_state: Optional[Union[_pd_sim_state_pb2.BuildSimState, Mapping]] = ..., render: Optional[Union[_pd_render_pb2.RenderInfo, Mapping]] = ..., qa_processor: Optional[Union[_pd_post_process_pb2.QAProcessor, Mapping]] = ..., field_encoder: Optional[Union[_pd_post_process_pb2.FieldEncoder, Mapping]] = ..., sim_state_cull: Optional[Union[_pd_sim_state_pb2.SimStateCull, Mapping]] = ..., levelcook: Optional[Union[_pd_levelcook_pb2.LevelCookInfo, Mapping]] = ..., worldgen: Optional[Union[_pd_worldgen_pb2.WorldGenInfo, Mapping]] = ..., worldbuild: Optional[Union[_pd_worldbuild_pb2.WorldBuildInfo, Mapping]] = ..., world_cook_from_p4: Optional[Union[_pd_world_cook_from_p4_pb2.WorldCookFromP4Info, Mapping]] = ..., source_maps: Optional[Union[_pd_source_maps_pb2.SourceMaps, Mapping]] = ..., package_maps_from_p4: Optional[Union[_pd_package_maps_from_p4_pb2.PackageMapsFromP4, Mapping]] = ..., le_encoder: Optional[Union[_pd_post_process_pb2.LEEncoder, Mapping]] = ..., sim_state_process: Optional[Union[_pd_sim_state_pb2.ProcessSimState, Mapping]] = ..., recook: Optional[Union[_pd_recook_pb2.Recook, Mapping]] = ..., step_batch: Optional[Union[_pd_step_batch_pb2.StepBatch, Mapping]] = ...) -> None: ...
    STAGES_FIELD_NUMBER: ClassVar[int]
    stages: _containers.RepeatedCompositeFieldContainer[KeystoneBuildMessage.PipelineStage]
    def __init__(self, stages: Optional[Iterable[Union[KeystoneBuildMessage.PipelineStage, Mapping]]] = ...) -> None: ...
