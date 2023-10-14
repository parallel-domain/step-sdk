from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_keystone_pb2
)
from . import (
    pd_render_pb2 as _pd_render_pb2,
    pd_post_process_pb2 as _pd_post_process_pb2,
    pd_sim_state_pb2 as _pd_sim_state_pb2,
    pd_levelcook_pb2 as _pd_levelcook_pb2,
    pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2,
    pd_worldgen_pb2 as _pd_worldgen_pb2,
    pd_worldbuild_pb2 as _pd_worldbuild_pb2,
    pd_source_maps_pb2 as _pd_source_maps_pb2,
    pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2,
    pd_recook_pb2 as _pd_recook_pb2,
    pd_step_batch_pb2 as _pd_step_batch_pb2
)


@register_wrapper(proto_type=pd_keystone_pb2.KeystoneBuildMessage)
class KeystoneBuildMessage(ProtoMessageClass):
    """
    Args:
        stages: :attr:`stages`
    Attributes:
        stages: Keystone build message will be an array of available sub build messages for
            each of the Keystone pipeline stage"""

    @register_wrapper(proto_type=pd_keystone_pb2.KeystoneBuildMessage.PipelineStage)
    class PipelineStage(ProtoMessageClass):
        """
        Args:
            build_sim_state: :attr:`build_sim_state`
            render: :attr:`render`
            qa_processor: :attr:`qa_processor`
            field_encoder: :attr:`field_encoder`
            sim_state_cull: :attr:`sim_state_cull`
            levelcook: :attr:`levelcook`
            worldgen: :attr:`worldgen`
            worldbuild: :attr:`worldbuild`
            world_cook_from_p4: :attr:`world_cook_from_p4`
            source_maps: :attr:`source_maps`
            package_maps_from_p4: :attr:`package_maps_from_p4`
            le_encoder: :attr:`le_encoder`
            sim_state_process: :attr:`sim_state_process`
            recook: :attr:`recook`
            step_batch: :attr:`step_batch`
        Attributes:
            build_sim_state:
            render:
            qa_processor:
            field_encoder:
            sim_state_cull:
            levelcook:
            worldgen:
            worldbuild:
            world_cook_from_p4:
            source_maps:
            package_maps_from_p4:
            le_encoder:
            sim_state_process:
            recook:
            step_batch:"""

        _proto_message = pd_keystone_pb2.KeystoneBuildMessage.PipelineStage

        def __init__(
            self,
            *,
            proto: Optional[pd_keystone_pb2.KeystoneBuildMessage.PipelineStage] = None,
            build_sim_state: _pd_sim_state_pb2.BuildSimState = None,
            render: _pd_render_pb2.RenderInfo = None,
            qa_processor: _pd_post_process_pb2.QAProcessor = None,
            field_encoder: _pd_post_process_pb2.FieldEncoder = None,
            sim_state_cull: _pd_sim_state_pb2.SimStateCull = None,
            levelcook: _pd_levelcook_pb2.LevelCookInfo = None,
            worldgen: _pd_worldgen_pb2.WorldGenInfo = None,
            worldbuild: _pd_worldbuild_pb2.WorldBuildInfo = None,
            world_cook_from_p4: _pd_world_cook_from_p4_pb2.WorldCookFromP4Info = None,
            source_maps: _pd_source_maps_pb2.SourceMaps = None,
            package_maps_from_p4: _pd_package_maps_from_p4_pb2.PackageMapsFromP4 = None,
            le_encoder: _pd_post_process_pb2.LEEncoder = None,
            sim_state_process: _pd_sim_state_pb2.ProcessSimState = None,
            recook: _pd_recook_pb2.Recook = None,
            step_batch: _pd_step_batch_pb2.StepBatch = None,
        ):
            if proto is None:
                proto = pd_keystone_pb2.KeystoneBuildMessage.PipelineStage()
            self.proto = proto
            self._build_sim_state = get_wrapper(proto_type=proto.build_sim_state.__class__)(proto=proto.build_sim_state)
            self._render = get_wrapper(proto_type=proto.render.__class__)(proto=proto.render)
            self._qa_processor = get_wrapper(proto_type=proto.qa_processor.__class__)(proto=proto.qa_processor)
            self._field_encoder = get_wrapper(proto_type=proto.field_encoder.__class__)(proto=proto.field_encoder)
            self._sim_state_cull = get_wrapper(proto_type=proto.sim_state_cull.__class__)(proto=proto.sim_state_cull)
            self._levelcook = get_wrapper(proto_type=proto.levelcook.__class__)(proto=proto.levelcook)
            self._worldgen = get_wrapper(proto_type=proto.worldgen.__class__)(proto=proto.worldgen)
            self._worldbuild = get_wrapper(proto_type=proto.worldbuild.__class__)(proto=proto.worldbuild)
            self._world_cook_from_p4 = get_wrapper(proto_type=proto.world_cook_from_p4.__class__)(
                proto=proto.world_cook_from_p4
            )
            self._source_maps = get_wrapper(proto_type=proto.source_maps.__class__)(proto=proto.source_maps)
            self._package_maps_from_p4 = get_wrapper(proto_type=proto.package_maps_from_p4.__class__)(
                proto=proto.package_maps_from_p4
            )
            self._le_encoder = get_wrapper(proto_type=proto.le_encoder.__class__)(proto=proto.le_encoder)
            self._sim_state_process = get_wrapper(proto_type=proto.sim_state_process.__class__)(
                proto=proto.sim_state_process
            )
            self._recook = get_wrapper(proto_type=proto.recook.__class__)(proto=proto.recook)
            self._step_batch = get_wrapper(proto_type=proto.step_batch.__class__)(proto=proto.step_batch)
            if build_sim_state is not None:
                self.build_sim_state = build_sim_state
            if render is not None:
                self.render = render
            if qa_processor is not None:
                self.qa_processor = qa_processor
            if field_encoder is not None:
                self.field_encoder = field_encoder
            if sim_state_cull is not None:
                self.sim_state_cull = sim_state_cull
            if levelcook is not None:
                self.levelcook = levelcook
            if worldgen is not None:
                self.worldgen = worldgen
            if worldbuild is not None:
                self.worldbuild = worldbuild
            if world_cook_from_p4 is not None:
                self.world_cook_from_p4 = world_cook_from_p4
            if source_maps is not None:
                self.source_maps = source_maps
            if package_maps_from_p4 is not None:
                self.package_maps_from_p4 = package_maps_from_p4
            if le_encoder is not None:
                self.le_encoder = le_encoder
            if sim_state_process is not None:
                self.sim_state_process = sim_state_process
            if recook is not None:
                self.recook = recook
            if step_batch is not None:
                self.step_batch = step_batch

        @property
        def build_sim_state(self) -> _pd_sim_state_pb2.BuildSimState:
            return self._build_sim_state

        @build_sim_state.setter
        def build_sim_state(self, value: _pd_sim_state_pb2.BuildSimState):
            self.proto.build_sim_state.CopyFrom(value.proto)

            self._build_sim_state = value
            self._build_sim_state._update_proto_references(self.proto.build_sim_state)

        @property
        def render(self) -> _pd_render_pb2.RenderInfo:
            return self._render

        @render.setter
        def render(self, value: _pd_render_pb2.RenderInfo):
            self.proto.render.CopyFrom(value.proto)

            self._render = value
            self._render._update_proto_references(self.proto.render)

        @property
        def qa_processor(self) -> _pd_post_process_pb2.QAProcessor:
            return self._qa_processor

        @qa_processor.setter
        def qa_processor(self, value: _pd_post_process_pb2.QAProcessor):
            self.proto.qa_processor.CopyFrom(value.proto)

            self._qa_processor = value
            self._qa_processor._update_proto_references(self.proto.qa_processor)

        @property
        def field_encoder(self) -> _pd_post_process_pb2.FieldEncoder:
            return self._field_encoder

        @field_encoder.setter
        def field_encoder(self, value: _pd_post_process_pb2.FieldEncoder):
            self.proto.field_encoder.CopyFrom(value.proto)

            self._field_encoder = value
            self._field_encoder._update_proto_references(self.proto.field_encoder)

        @property
        def sim_state_cull(self) -> _pd_sim_state_pb2.SimStateCull:
            return self._sim_state_cull

        @sim_state_cull.setter
        def sim_state_cull(self, value: _pd_sim_state_pb2.SimStateCull):
            self.proto.sim_state_cull.CopyFrom(value.proto)

            self._sim_state_cull = value
            self._sim_state_cull._update_proto_references(self.proto.sim_state_cull)

        @property
        def levelcook(self) -> _pd_levelcook_pb2.LevelCookInfo:
            return self._levelcook

        @levelcook.setter
        def levelcook(self, value: _pd_levelcook_pb2.LevelCookInfo):
            self.proto.levelcook.CopyFrom(value.proto)

            self._levelcook = value
            self._levelcook._update_proto_references(self.proto.levelcook)

        @property
        def worldgen(self) -> _pd_worldgen_pb2.WorldGenInfo:
            return self._worldgen

        @worldgen.setter
        def worldgen(self, value: _pd_worldgen_pb2.WorldGenInfo):
            self.proto.worldgen.CopyFrom(value.proto)

            self._worldgen = value
            self._worldgen._update_proto_references(self.proto.worldgen)

        @property
        def worldbuild(self) -> _pd_worldbuild_pb2.WorldBuildInfo:
            return self._worldbuild

        @worldbuild.setter
        def worldbuild(self, value: _pd_worldbuild_pb2.WorldBuildInfo):
            self.proto.worldbuild.CopyFrom(value.proto)

            self._worldbuild = value
            self._worldbuild._update_proto_references(self.proto.worldbuild)

        @property
        def world_cook_from_p4(self) -> _pd_world_cook_from_p4_pb2.WorldCookFromP4Info:
            return self._world_cook_from_p4

        @world_cook_from_p4.setter
        def world_cook_from_p4(self, value: _pd_world_cook_from_p4_pb2.WorldCookFromP4Info):
            self.proto.world_cook_from_p4.CopyFrom(value.proto)

            self._world_cook_from_p4 = value
            self._world_cook_from_p4._update_proto_references(self.proto.world_cook_from_p4)

        @property
        def source_maps(self) -> _pd_source_maps_pb2.SourceMaps:
            return self._source_maps

        @source_maps.setter
        def source_maps(self, value: _pd_source_maps_pb2.SourceMaps):
            self.proto.source_maps.CopyFrom(value.proto)

            self._source_maps = value
            self._source_maps._update_proto_references(self.proto.source_maps)

        @property
        def package_maps_from_p4(self) -> _pd_package_maps_from_p4_pb2.PackageMapsFromP4:
            return self._package_maps_from_p4

        @package_maps_from_p4.setter
        def package_maps_from_p4(self, value: _pd_package_maps_from_p4_pb2.PackageMapsFromP4):
            self.proto.package_maps_from_p4.CopyFrom(value.proto)

            self._package_maps_from_p4 = value
            self._package_maps_from_p4._update_proto_references(self.proto.package_maps_from_p4)

        @property
        def le_encoder(self) -> _pd_post_process_pb2.LEEncoder:
            return self._le_encoder

        @le_encoder.setter
        def le_encoder(self, value: _pd_post_process_pb2.LEEncoder):
            self.proto.le_encoder.CopyFrom(value.proto)

            self._le_encoder = value
            self._le_encoder._update_proto_references(self.proto.le_encoder)

        @property
        def sim_state_process(self) -> _pd_sim_state_pb2.ProcessSimState:
            return self._sim_state_process

        @sim_state_process.setter
        def sim_state_process(self, value: _pd_sim_state_pb2.ProcessSimState):
            self.proto.sim_state_process.CopyFrom(value.proto)

            self._sim_state_process = value
            self._sim_state_process._update_proto_references(self.proto.sim_state_process)

        @property
        def recook(self) -> _pd_recook_pb2.Recook:
            return self._recook

        @recook.setter
        def recook(self, value: _pd_recook_pb2.Recook):
            self.proto.recook.CopyFrom(value.proto)

            self._recook = value
            self._recook._update_proto_references(self.proto.recook)

        @property
        def step_batch(self) -> _pd_step_batch_pb2.StepBatch:
            return self._step_batch

        @step_batch.setter
        def step_batch(self, value: _pd_step_batch_pb2.StepBatch):
            self.proto.step_batch.CopyFrom(value.proto)

            self._step_batch = value
            self._step_batch._update_proto_references(self.proto.step_batch)

        def _update_proto_references(self, proto: pd_keystone_pb2.KeystoneBuildMessage.PipelineStage):
            self.proto = proto
            self._build_sim_state._update_proto_references(proto.build_sim_state)
            self._render._update_proto_references(proto.render)
            self._qa_processor._update_proto_references(proto.qa_processor)
            self._field_encoder._update_proto_references(proto.field_encoder)
            self._sim_state_cull._update_proto_references(proto.sim_state_cull)
            self._levelcook._update_proto_references(proto.levelcook)
            self._worldgen._update_proto_references(proto.worldgen)
            self._worldbuild._update_proto_references(proto.worldbuild)
            self._world_cook_from_p4._update_proto_references(proto.world_cook_from_p4)
            self._source_maps._update_proto_references(proto.source_maps)
            self._package_maps_from_p4._update_proto_references(proto.package_maps_from_p4)
            self._le_encoder._update_proto_references(proto.le_encoder)
            self._sim_state_process._update_proto_references(proto.sim_state_process)
            self._recook._update_proto_references(proto.recook)
            self._step_batch._update_proto_references(proto.step_batch)

    _proto_message = pd_keystone_pb2.KeystoneBuildMessage

    def __init__(
        self,
        *,
        proto: Optional[pd_keystone_pb2.KeystoneBuildMessage] = None,
        stages: List[KeystoneBuildMessage.PipelineStage] = None,
    ):
        if proto is None:
            proto = pd_keystone_pb2.KeystoneBuildMessage()
        self.proto = proto
        self._stages = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.stages],
            attr_name="stages",
            list_owner=self,
        )
        if stages is not None:
            self.stages = stages

    @property
    def stages(self) -> List[KeystoneBuildMessage.PipelineStage]:
        return self._stages

    @stages.setter
    def stages(self, value: List[KeystoneBuildMessage.PipelineStage]):
        self._stages.clear()
        for v in value:
            self._stages.append(v)

    def _update_proto_references(self, proto: pd_keystone_pb2.KeystoneBuildMessage):
        self.proto = proto
        for i, v in enumerate(self.stages):
            v._update_proto_references(self.proto.stages[i])
