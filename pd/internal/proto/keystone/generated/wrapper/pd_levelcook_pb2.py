from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_levelcook_pb2
)


@register_wrapper(proto_type=pd_levelcook_pb2.LevelCookInfo)
class LevelCookInfo(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        location_list: :attr:`location_list`
    Attributes:
        artifact_key:
        output_artifact_uid:
        location_list:"""

    @register_wrapper(proto_type=pd_levelcook_pb2.LevelCookInfo.Location)
    class Location(ProtoMessageClass):
        """
        Args:
            artifact_key: :attr:`artifact_key`
            output_artifact_uid: :attr:`output_artifact_uid`
            location_name: :attr:`location_name`
        Attributes:
            artifact_key:
            output_artifact_uid:
            location_name:"""

        _proto_message = pd_levelcook_pb2.LevelCookInfo.Location

        def __init__(
            self,
            *,
            proto: Optional[pd_levelcook_pb2.LevelCookInfo.Location] = None,
            artifact_key: str = None,
            output_artifact_uid: str = None,
            location_name: str = None,
        ):
            if proto is None:
                proto = pd_levelcook_pb2.LevelCookInfo.Location()
            self.proto = proto
            if artifact_key is not None:
                self.artifact_key = artifact_key
            if output_artifact_uid is not None:
                self.output_artifact_uid = output_artifact_uid
            if location_name is not None:
                self.location_name = location_name

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
        def location_name(self) -> str:
            return self.proto.location_name

        @location_name.setter
        def location_name(self, value: str):
            self.proto.location_name = value

        def _update_proto_references(self, proto: pd_levelcook_pb2.LevelCookInfo.Location):
            self.proto = proto

    _proto_message = pd_levelcook_pb2.LevelCookInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_levelcook_pb2.LevelCookInfo] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        location_list: List[LevelCookInfo.Location] = None,
    ):
        if proto is None:
            proto = pd_levelcook_pb2.LevelCookInfo()
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
    def location_list(self) -> List[LevelCookInfo.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[LevelCookInfo.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

    def _update_proto_references(self, proto: pd_levelcook_pb2.LevelCookInfo):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])
