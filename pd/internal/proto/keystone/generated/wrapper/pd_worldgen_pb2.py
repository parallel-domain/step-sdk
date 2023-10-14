from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_worldgen_pb2
)


@register_wrapper(proto_type=pd_worldgen_pb2.WorldGenInfo)
class WorldGenInfo(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        location_list: :attr:`location_list`
    Attributes:
        artifact_key:
        output_artifact_uid:
        location_list:"""

    @register_wrapper(proto_type=pd_worldgen_pb2.WorldGenInfo.Location)
    class Location(ProtoMessageClass):
        """
        Args:
            artifact_key: :attr:`artifact_key`
            code_build_artifact_uid: :attr:`code_build_artifact_uid`
            worldgen_output_artifact_uid: :attr:`worldgen_output_artifact_uid`
            imported_level_output_artifact_uid: :attr:`imported_level_output_artifact_uid`
            location_name: :attr:`location_name`
            parameters_path: :attr:`parameters_path`
            input_file_path: :attr:`input_file_path`
            geojson_path: :attr:`geojson_path`
        Attributes:
            artifact_key:
            code_build_artifact_uid:
            worldgen_output_artifact_uid:
            imported_level_output_artifact_uid:
            location_name:
            parameters_path:
            input_file_path:
            geojson_path:"""

        _proto_message = pd_worldgen_pb2.WorldGenInfo.Location

        def __init__(
            self,
            *,
            proto: Optional[pd_worldgen_pb2.WorldGenInfo.Location] = None,
            artifact_key: str = None,
            code_build_artifact_uid: str = None,
            worldgen_output_artifact_uid: str = None,
            imported_level_output_artifact_uid: str = None,
            location_name: str = None,
            parameters_path: str = None,
            input_file_path: str = None,
            geojson_path: str = None,
        ):
            if proto is None:
                proto = pd_worldgen_pb2.WorldGenInfo.Location()
            self.proto = proto
            if artifact_key is not None:
                self.artifact_key = artifact_key
            if code_build_artifact_uid is not None:
                self.code_build_artifact_uid = code_build_artifact_uid
            if worldgen_output_artifact_uid is not None:
                self.worldgen_output_artifact_uid = worldgen_output_artifact_uid
            if imported_level_output_artifact_uid is not None:
                self.imported_level_output_artifact_uid = imported_level_output_artifact_uid
            if location_name is not None:
                self.location_name = location_name
            if parameters_path is not None:
                self.parameters_path = parameters_path
            if input_file_path is not None:
                self.input_file_path = input_file_path
            if geojson_path is not None:
                self.geojson_path = geojson_path

        @property
        def artifact_key(self) -> str:
            return self.proto.artifact_key

        @artifact_key.setter
        def artifact_key(self, value: str):
            self.proto.artifact_key = value

        @property
        def code_build_artifact_uid(self) -> str:
            return self.proto.code_build_artifact_uid

        @code_build_artifact_uid.setter
        def code_build_artifact_uid(self, value: str):
            self.proto.code_build_artifact_uid = value

        @property
        def worldgen_output_artifact_uid(self) -> str:
            return self.proto.worldgen_output_artifact_uid

        @worldgen_output_artifact_uid.setter
        def worldgen_output_artifact_uid(self, value: str):
            self.proto.worldgen_output_artifact_uid = value

        @property
        def imported_level_output_artifact_uid(self) -> str:
            return self.proto.imported_level_output_artifact_uid

        @imported_level_output_artifact_uid.setter
        def imported_level_output_artifact_uid(self, value: str):
            self.proto.imported_level_output_artifact_uid = value

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

        @property
        def geojson_path(self) -> str:
            return self.proto.geojson_path

        @geojson_path.setter
        def geojson_path(self, value: str):
            self.proto.geojson_path = value

        def _update_proto_references(self, proto: pd_worldgen_pb2.WorldGenInfo.Location):
            self.proto = proto

    _proto_message = pd_worldgen_pb2.WorldGenInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_worldgen_pb2.WorldGenInfo] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        location_list: List[WorldGenInfo.Location] = None,
    ):
        if proto is None:
            proto = pd_worldgen_pb2.WorldGenInfo()
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
    def location_list(self) -> List[WorldGenInfo.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[WorldGenInfo.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

    def _update_proto_references(self, proto: pd_worldgen_pb2.WorldGenInfo):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])
