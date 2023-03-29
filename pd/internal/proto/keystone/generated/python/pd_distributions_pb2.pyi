from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class Bucket(_message.Message):
    __slots__ = ["float_value", "int32_value", "probability", "string_value"]
    FLOAT_VALUE_FIELD_NUMBER: ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: ClassVar[int]
    PROBABILITY_FIELD_NUMBER: ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: ClassVar[int]
    float_value: float
    int32_value: int
    probability: float
    string_value: str
    def __init__(self, string_value: Optional[str] = ..., float_value: Optional[float] = ..., int32_value: Optional[int] = ..., probability: Optional[float] = ...) -> None: ...

class CategoricalDistribution(_message.Message):
    __slots__ = ["buckets"]
    BUCKETS_FIELD_NUMBER: ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[Bucket]
    def __init__(self, buckets: Optional[Iterable[Union[Bucket, Mapping]]] = ...) -> None: ...

class ConstantDistribution(_message.Message):
    __slots__ = ["float_value", "int32_value", "string_value"]
    FLOAT_VALUE_FIELD_NUMBER: ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: ClassVar[int]
    float_value: float
    int32_value: int
    string_value: str
    def __init__(self, string_value: Optional[str] = ..., float_value: Optional[float] = ..., int32_value: Optional[int] = ...) -> None: ...

class ContinousUniformDistribution(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: ClassVar[int]
    MIN_FIELD_NUMBER: ClassVar[int]
    max: float
    min: float
    def __init__(self, min: Optional[float] = ..., max: Optional[float] = ...) -> None: ...

class DiscreteUniformDistribution(_message.Message):
    __slots__ = ["buckets"]
    BUCKETS_FIELD_NUMBER: ClassVar[int]
    buckets: _containers.RepeatedCompositeFieldContainer[Bucket]
    def __init__(self, buckets: Optional[Iterable[Union[Bucket, Mapping]]] = ...) -> None: ...

class Distribution(_message.Message):
    __slots__ = ["categorical", "constant", "normal", "truncated_normal", "uniform_continous", "uniform_discrete"]
    CATEGORICAL_FIELD_NUMBER: ClassVar[int]
    CONSTANT_FIELD_NUMBER: ClassVar[int]
    NORMAL_FIELD_NUMBER: ClassVar[int]
    TRUNCATED_NORMAL_FIELD_NUMBER: ClassVar[int]
    UNIFORM_CONTINOUS_FIELD_NUMBER: ClassVar[int]
    UNIFORM_DISCRETE_FIELD_NUMBER: ClassVar[int]
    categorical: CategoricalDistribution
    constant: ConstantDistribution
    normal: NormalDistribution
    truncated_normal: TrucatedNormalDistribution
    uniform_continous: ContinousUniformDistribution
    uniform_discrete: DiscreteUniformDistribution
    def __init__(self, normal: Optional[Union[NormalDistribution, Mapping]] = ..., truncated_normal: Optional[Union[TrucatedNormalDistribution, Mapping]] = ..., uniform_continous: Optional[Union[ContinousUniformDistribution, Mapping]] = ..., constant: Optional[Union[ConstantDistribution, Mapping]] = ..., uniform_discrete: Optional[Union[DiscreteUniformDistribution, Mapping]] = ..., categorical: Optional[Union[CategoricalDistribution, Mapping]] = ...) -> None: ...

class EnumDistribution(_message.Message):
    __slots__ = ["probabilities"]
    class ProbabilitiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: float
        def __init__(self, key: Optional[str] = ..., value: Optional[float] = ...) -> None: ...
    PROBABILITIES_FIELD_NUMBER: ClassVar[int]
    probabilities: _containers.ScalarMap[str, float]
    def __init__(self, probabilities: Optional[Mapping[str, float]] = ...) -> None: ...

class NormalDistribution(_message.Message):
    __slots__ = ["mean", "variance"]
    MEAN_FIELD_NUMBER: ClassVar[int]
    VARIANCE_FIELD_NUMBER: ClassVar[int]
    mean: float
    variance: float
    def __init__(self, mean: Optional[float] = ..., variance: Optional[float] = ...) -> None: ...

class TrucatedNormalDistribution(_message.Message):
    __slots__ = ["max", "mean", "min", "variance"]
    MAX_FIELD_NUMBER: ClassVar[int]
    MEAN_FIELD_NUMBER: ClassVar[int]
    MIN_FIELD_NUMBER: ClassVar[int]
    VARIANCE_FIELD_NUMBER: ClassVar[int]
    max: float
    mean: float
    min: float
    variance: float
    def __init__(self, mean: Optional[float] = ..., variance: Optional[float] = ..., min: Optional[float] = ..., max: Optional[float] = ...) -> None: ...

class VehicleCategoryWeight(_message.Message):
    __slots__ = ["model_weights", "weight"]
    class ModelWeightsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: float
        def __init__(self, key: Optional[str] = ..., value: Optional[float] = ...) -> None: ...
    MODEL_WEIGHTS_FIELD_NUMBER: ClassVar[int]
    WEIGHT_FIELD_NUMBER: ClassVar[int]
    model_weights: _containers.ScalarMap[str, float]
    weight: float
    def __init__(self, weight: Optional[float] = ..., model_weights: Optional[Mapping[str, float]] = ...) -> None: ...
