from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_package_maps_from_p4_pb2
)


@register_wrapper(proto_type=pd_package_maps_from_p4_pb2.PackageMapsFromP4)
class PackageMapsFromP4(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        base_changelist: :attr:`base_changelist`
        unshelve_changelist: :attr:`unshelve_changelist`
        map_list: :attr:`map_list`
    Attributes:
        artifact_key:
        output_artifact_uid:
        code_build_artifact_uid:
        base_changelist:
        unshelve_changelist:
        map_list:"""

    @register_wrapper(proto_type=pd_package_maps_from_p4_pb2.PackageMapsFromP4.Map)
    class Map(ProtoMessageClass):
        """
        Args:
            map_output_artifact_uid: :attr:`map_output_artifact_uid`
            map_name: :attr:`map_name`
            parameters_path: :attr:`parameters_path`
            input_file_path: :attr:`input_file_path`
            elevation_path: :attr:`elevation_path`
        Attributes:
            map_output_artifact_uid:
            map_name:
            parameters_path:
            input_file_path:
            elevation_path:"""

        _proto_message = pd_package_maps_from_p4_pb2.PackageMapsFromP4.Map

        def __init__(
            self,
            *,
            proto: Optional[pd_package_maps_from_p4_pb2.PackageMapsFromP4.Map] = None,
            map_output_artifact_uid: str = None,
            map_name: str = None,
            parameters_path: str = None,
            input_file_path: str = None,
            elevation_path: str = None,
        ):
            if proto is None:
                proto = pd_package_maps_from_p4_pb2.PackageMapsFromP4.Map()
            self.proto = proto
            if map_output_artifact_uid is not None:
                self.map_output_artifact_uid = map_output_artifact_uid
            if map_name is not None:
                self.map_name = map_name
            if parameters_path is not None:
                self.parameters_path = parameters_path
            if input_file_path is not None:
                self.input_file_path = input_file_path
            if elevation_path is not None:
                self.elevation_path = elevation_path

        @property
        def map_output_artifact_uid(self) -> str:
            return self.proto.map_output_artifact_uid

        @map_output_artifact_uid.setter
        def map_output_artifact_uid(self, value: str):
            self.proto.map_output_artifact_uid = value

        @property
        def map_name(self) -> str:
            return self.proto.map_name

        @map_name.setter
        def map_name(self, value: str):
            self.proto.map_name = value

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

        @property
        def elevation_path(self) -> str:
            return self.proto.elevation_path

        @elevation_path.setter
        def elevation_path(self, value: str):
            self.proto.elevation_path = value

        def _update_proto_references(self, proto: pd_package_maps_from_p4_pb2.PackageMapsFromP4.Map):
            self.proto = proto

    _proto_message = pd_package_maps_from_p4_pb2.PackageMapsFromP4

    def __init__(
        self,
        *,
        proto: Optional[pd_package_maps_from_p4_pb2.PackageMapsFromP4] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        code_build_artifact_uid: str = None,
        base_changelist: str = None,
        unshelve_changelist: str = None,
        map_list: List[PackageMapsFromP4.Map] = None,
    ):
        if proto is None:
            proto = pd_package_maps_from_p4_pb2.PackageMapsFromP4()
        self.proto = proto
        self._map_list = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.map_list],
            attr_name="map_list",
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
        if map_list is not None:
            self.map_list = map_list

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
    def map_list(self) -> List[PackageMapsFromP4.Map]:
        return self._map_list

    @map_list.setter
    def map_list(self, value: List[PackageMapsFromP4.Map]):
        self._map_list.clear()
        for v in value:
            self._map_list.append(v)

    def _update_proto_references(self, proto: pd_package_maps_from_p4_pb2.PackageMapsFromP4):
        self.proto = proto
        for i, v in enumerate(self.map_list):
            v._update_proto_references(self.proto.map_list[i])
