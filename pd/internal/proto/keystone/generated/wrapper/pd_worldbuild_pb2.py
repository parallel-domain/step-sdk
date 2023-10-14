from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_worldbuild_pb2
)


@register_wrapper(proto_type=pd_worldbuild_pb2.WorldBuildInfo)
class WorldBuildInfo(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        base_changelist: :attr:`base_changelist`
        unshelve_changelist: :attr:`unshelve_changelist`
        qa_render: :attr:`qa_render`
        image_generator_core_artifact_uid: :attr:`image_generator_core_artifact_uid`
        world_preview_uid: :attr:`world_preview_uid`
        levelcook_batch_size: :attr:`levelcook_batch_size`
        do_houdini_only: :attr:`do_houdini_only`
        location_list: :attr:`location_list`
    Attributes:
        artifact_key:
        output_artifact_uid:
        code_build_artifact_uid:
        base_changelist:
        unshelve_changelist:
        qa_render:
        image_generator_core_artifact_uid:
        world_preview_uid:
        levelcook_batch_size:
        do_houdini_only:
        location_list:"""

    @register_wrapper(proto_type=pd_worldbuild_pb2.WorldBuildInfo.Location)
    class Location(ProtoMessageClass):
        """
        Args:
            location_output_artifact_uid: :attr:`location_output_artifact_uid`
            location_name: :attr:`location_name`
            parameters_path: :attr:`parameters_path`
            input_file_path: :attr:`input_file_path`
        Attributes:
            location_output_artifact_uid:
            location_name:
            parameters_path:
            input_file_path:"""

        _proto_message = pd_worldbuild_pb2.WorldBuildInfo.Location

        def __init__(
            self,
            *,
            proto: Optional[pd_worldbuild_pb2.WorldBuildInfo.Location] = None,
            location_output_artifact_uid: str = None,
            location_name: str = None,
            parameters_path: str = None,
            input_file_path: str = None,
        ):
            if proto is None:
                proto = pd_worldbuild_pb2.WorldBuildInfo.Location()
            self.proto = proto
            if location_output_artifact_uid is not None:
                self.location_output_artifact_uid = location_output_artifact_uid
            if location_name is not None:
                self.location_name = location_name
            if parameters_path is not None:
                self.parameters_path = parameters_path
            if input_file_path is not None:
                self.input_file_path = input_file_path

        @property
        def location_output_artifact_uid(self) -> str:
            return self.proto.location_output_artifact_uid

        @location_output_artifact_uid.setter
        def location_output_artifact_uid(self, value: str):
            self.proto.location_output_artifact_uid = value

        @property
        def location_name(self) -> str:
            return self.proto.location_name

        @location_name.setter
        def location_name(self, value: str):
            self.proto.location_name = value

        @property
        def parameters_path(self) -> str:
            return self.proto.parameters_path

        @parameters_path.setter
        def parameters_path(self, value: str):
            self.proto.parameters_path = value

        @property
        def input_file_path(self) -> str:
            return self.proto.input_file_path

        @input_file_path.setter
        def input_file_path(self, value: str):
            self.proto.input_file_path = value

        def _update_proto_references(self, proto: pd_worldbuild_pb2.WorldBuildInfo.Location):
            self.proto = proto

    _proto_message = pd_worldbuild_pb2.WorldBuildInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_worldbuild_pb2.WorldBuildInfo] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        code_build_artifact_uid: str = None,
        base_changelist: str = None,
        unshelve_changelist: str = None,
        qa_render: bool = None,
        image_generator_core_artifact_uid: str = None,
        world_preview_uid: str = None,
        levelcook_batch_size: int = None,
        do_houdini_only: bool = None,
        location_list: List[WorldBuildInfo.Location] = None,
    ):
        if proto is None:
            proto = pd_worldbuild_pb2.WorldBuildInfo()
        self.proto = proto
        self._location_list = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.location_list],
            attr_name="location_list",
            list_owner=self,
        )
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if base_changelist is not None:
            self.base_changelist = base_changelist
        if unshelve_changelist is not None:
            self.unshelve_changelist = unshelve_changelist
        if qa_render is not None:
            self.qa_render = qa_render
        if image_generator_core_artifact_uid is not None:
            self.image_generator_core_artifact_uid = image_generator_core_artifact_uid
        if world_preview_uid is not None:
            self.world_preview_uid = world_preview_uid
        if levelcook_batch_size is not None:
            self.levelcook_batch_size = levelcook_batch_size
        if do_houdini_only is not None:
            self.do_houdini_only = do_houdini_only
        if location_list is not None:
            self.location_list = location_list

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def base_changelist(self) -> str:
        return self.proto.base_changelist

    @base_changelist.setter
    def base_changelist(self, value: str):
        self.proto.base_changelist = value

    @property
    def unshelve_changelist(self) -> str:
        return self.proto.unshelve_changelist

    @unshelve_changelist.setter
    def unshelve_changelist(self, value: str):
        self.proto.unshelve_changelist = value

    @property
    def qa_render(self) -> bool:
        return self.proto.qa_render

    @qa_render.setter
    def qa_render(self, value: bool):
        self.proto.qa_render = value

    @property
    def image_generator_core_artifact_uid(self) -> str:
        return self.proto.image_generator_core_artifact_uid

    @image_generator_core_artifact_uid.setter
    def image_generator_core_artifact_uid(self, value: str):
        self.proto.image_generator_core_artifact_uid = value

    @property
    def world_preview_uid(self) -> str:
        return self.proto.world_preview_uid

    @world_preview_uid.setter
    def world_preview_uid(self, value: str):
        self.proto.world_preview_uid = value

    @property
    def levelcook_batch_size(self) -> int:
        return self.proto.levelcook_batch_size

    @levelcook_batch_size.setter
    def levelcook_batch_size(self, value: int):
        self.proto.levelcook_batch_size = value

    @property
    def do_houdini_only(self) -> bool:
        return self.proto.do_houdini_only

    @do_houdini_only.setter
    def do_houdini_only(self, value: bool):
        self.proto.do_houdini_only = value

    @property
    def location_list(self) -> List[WorldBuildInfo.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[WorldBuildInfo.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

    def _update_proto_references(self, proto: pd_worldbuild_pb2.WorldBuildInfo):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])
