from abc import ABC, abstractmethod
from sys import platform
from typing import Any, Dict, List, Mapping, TypeVar, Type
from enum import Enum
from google.protobuf.json_format import MessageToDict, ParseDict

# During proto interface update, this file is copied from di/update-internal/utils.py.in into the wrapper folders!
# Please add your changes to the utils.py.in file.


if platform in ("linux", "linux2"):
    from google.protobuf.pyext._message import MessageMapContainer as MessageMapContainer
elif platform == "darwin":
    from google.protobuf.internal.containers import MessageMap as MessageMapContainer
elif platform == "win32":
    from google.protobuf.pyext._message import MessageMapContainer as MessageMapContainer

T = TypeVar("T")

WRAPPER_REGISTRY: Dict[str, Type] = dict()


def register_wrapper(proto_type: Type):
    def _cls_wrp(cls):
        if hasattr(proto_type, "__name__"):
            registered_name = f"{proto_type.__module__}.{proto_type.__name__}"
        elif hasattr(proto_type, "_enum_type"):
            registered_name = proto_type._enum_type.full_name
        else:
            raise ValueError(f"Can't register wrapper for class of type {cls}")

        if registered_name not in WRAPPER_REGISTRY:
            WRAPPER_REGISTRY[registered_name] = cls
        elif WRAPPER_REGISTRY[registered_name] in cls.__bases__:
            # If the is a subclass of a wrapper class. Override with the subclass to make sure we get the
            # convenience features
            WRAPPER_REGISTRY[registered_name] = cls
        return cls

    return _cls_wrp


def get_wrapper(proto_type: Type) -> Type:
    if hasattr(proto_type, "__name__"):
        registered_name = f"{proto_type.__module__}.{proto_type.__name__}"
    elif hasattr(proto_type, "_proto_message"):
        registered_name = proto_type._proto_message._enum_type.full_name
    else:
        raise ValueError(f"Can't retrieve wrapper for class of type {proto_type}")

    return WRAPPER_REGISTRY[registered_name]


class ProtoMessageClass(ABC):
    @classmethod
    def from_dict(cls, json_dict: Dict[str, Any]) -> "ProtoMessageClass":
        msg = ParseDict(
            js_dict=json_dict,
            message=cls._proto_message(),
            ignore_unknown_fields=True,
            descriptor_pool=None,
        )
        return cls.from_message(message=msg)

    @classmethod
    def from_message(cls, message) -> "ProtoMessageClass":
        return cls(proto=message)

    def to_dict(self) -> Dict[str, Any]:
        return MessageToDict(
            message=self.proto,
            including_default_value_fields=False,
            preserving_proto_field_name=True,
            use_integers_for_enums=False,
            descriptor_pool=None,
            float_precision=None,
        )

    def clone_message(self):
        msg = self.proto.__class__()
        msg.ParseFromString(self.proto.SerializeToString(deterministic=True))
        return msg

    def clone(self) -> "ProtoMessageClass":
        msg = self.clone_message()
        return self.__class__(proto=msg)

    @abstractmethod
    def _update_proto_references(self, proto: "ProtoMessageClass") -> None:
        ...


class AtomicGeneratorMessage(ProtoMessageClass):
    ...


class ProtoEnumClass:
    ...


class ProtoDictWrapper(Dict[Any, T]):
    def __init__(self, container: Dict[Any, ProtoMessageClass], attr_name: str, dict_owner: Any, **kwargs):
        super().__init__(**kwargs)
        self._dict_owner = dict_owner
        self._attr_name = attr_name
        for k, v in container.items():
            super().__setitem__(k, v)

    def __getitem__(self, item):
        return super().__getitem__(item)

    def __setitem__(self, key, value):  # real signature unknown
        """Set self[key] to value."""
        super().__setitem__(key, value)

        dict_obj = getattr(self._dict_owner.proto, self._attr_name)
        if isinstance(dict_obj, MessageMapContainer):
            if hasattr(value, "proto"):
                dict_obj.get_or_create(key).CopyFrom(value.proto)
                # calling CopyFrom actually copies the proto, so we need to update wrapper proto
                value._update_proto_references(dict_obj[key])
            elif isinstance(value, dict):
                value_msg = dict_obj.GetEntryClass()(key=key, value=value)
                dict_obj.get_or_create(key).CopyFrom(value_msg.value)
            else:
                dict_obj.MergeFrom({key: value})
        else:  # should only be the case for enums, float, str, int
            dict_obj.update({key: value})

    def clear(self):
        getattr(self._dict_owner.proto, self._attr_name).clear()
        super().clear()

    def update(self, value: Mapping[Any, T], **kwargs):
        for k, v in value.items():
            self[k] = v


class ProtoListWrapper(List[T]):
    def __init__(self, container: List[ProtoMessageClass], attr_name: str, list_owner: Any, **kwargs):
        super().__init__(**kwargs)
        self._list_owner = list_owner
        self._attr_name = attr_name
        for item in container:
            super().append(item)

    def append(self, item: ProtoMessageClass):
        super().append(item)

        if hasattr(item, "proto"):
            list_in_owner = getattr(self._list_owner.proto, self._attr_name)
            list_in_owner.extend([item.proto])
            # calling extend actually copies the proto, so we need to update wrapper proto
            item._update_proto_references(list_in_owner[-1])
        else:
            getattr(self._list_owner.proto, self._attr_name).extend([item])

    def clear(self) -> None:
        super().clear()
        self._list_owner.proto.ClearField(self._attr_name)
