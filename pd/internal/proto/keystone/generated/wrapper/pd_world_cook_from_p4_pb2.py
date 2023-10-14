from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_world_cook_from_p4_pb2
)


@register_wrapper(proto_type=pd_world_cook_from_p4_pb2.WorldCookFromP4Info)
class WorldCookFromP4Info(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        location_list: :attr:`location_list`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        base_changelist: :attr:`base_changelist`
        unshelve_changelist: :attr:`unshelve_changelist`
    Attributes:
        artifact_key:
        output_artifact_uid:
        location_list:
        code_build_artifact_uid:
        base_changelist:
        unshelve_changelist:"""

    @register_wrapper(proto_type=pd_world_cook_from_p4_pb2.WorldCookFromP4Info.Location)
    class Location(ProtoMessageClass):
        """
        Args:
            location_output_artifact_uid: :attr:`location_output_artifact_uid`
            location_name: :attr:`location_name`
        Attributes:
            location_output_artifact_uid:
            location_name:"""

        _proto_message = pd_world_cook_from_p4_pb2.WorldCookFromP4Info.Location

        def __init__(
            self,
            *,
            proto: Optional[pd_world_cook_from_p4_pb2.WorldCookFromP4Info.Location] = None,
            location_output_artifact_uid: str = None,
            location_name: str = None,
        ):
            if proto is None:
                proto = pd_world_cook_from_p4_pb2.WorldCookFromP4Info.Location()
            self.proto = proto
            if location_output_artifact_uid is not None:
                self.location_output_artifact_uid = location_output_artifact_uid
            if location_name is not None:
                self.location_name = location_name

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

        def _update_proto_references(self, proto: pd_world_cook_from_p4_pb2.WorldCookFromP4Info.Location):
            self.proto = proto

    _proto_message = pd_world_cook_from_p4_pb2.WorldCookFromP4Info

    def __init__(
        self,
        *,
        proto: Optional[pd_world_cook_from_p4_pb2.WorldCookFromP4Info] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        location_list: List[WorldCookFromP4Info.Location] = None,
        code_build_artifact_uid: str = None,
        base_changelist: str = None,
        unshelve_changelist: str = None,
    ):
        if proto is None:
            proto = pd_world_cook_from_p4_pb2.WorldCookFromP4Info()
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
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if base_changelist is not None:
            self.base_changelist = base_changelist
        if unshelve_changelist is not None:
            self.unshelve_changelist = unshelve_changelist

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
    def location_list(self) -> List[WorldCookFromP4Info.Location]:
        return self._location_list

    @location_list.setter
    def location_list(self, value: List[WorldCookFromP4Info.Location]):
        self._location_list.clear()
        for v in value:
            self._location_list.append(v)

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

    def _update_proto_references(self, proto: pd_world_cook_from_p4_pb2.WorldCookFromP4Info):
        self.proto = proto
        for i, v in enumerate(self.location_list):
            v._update_proto_references(self.proto.location_list[i])
