from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Float3(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...) -> None: ...

class Float3x3(_message.Message):
    __slots__ = ["r0", "r1", "r2"]
    R0_FIELD_NUMBER: ClassVar[int]
    R1_FIELD_NUMBER: ClassVar[int]
    R2_FIELD_NUMBER: ClassVar[int]
    r0: Float3
    r1: Float3
    r2: Float3
    def __init__(self, r0: Optional[Union[Float3, Mapping]] = ..., r1: Optional[Union[Float3, Mapping]] = ..., r2: Optional[Union[Float3, Mapping]] = ...) -> None: ...

class Pose(_message.Message):
    __slots__ = ["orientation", "position"]
    ORIENTATION_FIELD_NUMBER: ClassVar[int]
    POSITION_FIELD_NUMBER: ClassVar[int]
    orientation: Float3x3
    position: Float3
    def __init__(self, position: Optional[Union[Float3, Mapping]] = ..., orientation: Optional[Union[Float3x3, Mapping]] = ...) -> None: ...
