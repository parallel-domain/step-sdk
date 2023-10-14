from __future__ import annotations
from typing import List, Dict, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper,
    ProtoDictWrapper
)
from ..python import (
    pd_distributions_pb2
)


@register_wrapper(proto_type=pd_distributions_pb2.NormalDistribution)
class NormalDistribution(ProtoMessageClass):
    """
    Normal distribution.

    Args:
        mean: :attr:`mean`
        variance: :attr:`variance`
    Attributes:
        mean: Mean of the normal distribution.
        variance: Variance of the normal distribution"""

    _proto_message = pd_distributions_pb2.NormalDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.NormalDistribution] = None,
        mean: float = None,
        variance: float = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.NormalDistribution()
        self.proto = proto
        if mean is not None:
            self.mean = mean
        if variance is not None:
            self.variance = variance

    @property
    def mean(self) -> float:
        return self.proto.mean

    @mean.setter
    def mean(self, value: float):
        self.proto.mean = value

    @property
    def variance(self) -> float:
        return self.proto.variance

    @variance.setter
    def variance(self, value: float):
        self.proto.variance = value

    def _update_proto_references(self, proto: pd_distributions_pb2.NormalDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.TrucatedNormalDistribution)
class TrucatedNormalDistribution(ProtoMessageClass):
    """
    Normal distribution that is truncated to only contain values within the interval specified by min and max values.

    Args:
        mean: :attr:`mean`
        variance: :attr:`variance`
        min: :attr:`min`
        max: :attr:`max`
    Attributes:
        mean: Mean of the normal distribution.
        variance: Variance of the normal distribution.
        min: Minimum value of the truncated normal distribution.
        max: Maximum value of the truncated normal distribution."""

    _proto_message = pd_distributions_pb2.TrucatedNormalDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.TrucatedNormalDistribution] = None,
        mean: float = None,
        variance: float = None,
        min: float = None,
        max: float = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.TrucatedNormalDistribution()
        self.proto = proto
        if mean is not None:
            self.mean = mean
        if variance is not None:
            self.variance = variance
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def mean(self) -> float:
        return self.proto.mean

    @mean.setter
    def mean(self, value: float):
        self.proto.mean = value

    @property
    def variance(self) -> float:
        return self.proto.variance

    @variance.setter
    def variance(self, value: float):
        self.proto.variance = value

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    def _update_proto_references(self, proto: pd_distributions_pb2.TrucatedNormalDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.ContinousUniformDistribution)
class ContinousUniformDistribution(ProtoMessageClass):
    """
    A uniform distribution with constant probability.

    Args:
        min: :attr:`min`
        max: :attr:`max`
    Attributes:
        min: Minimum value of the continuous normal distribution.
        max: Maximum value of the continuous normal distribution."""

    _proto_message = pd_distributions_pb2.ContinousUniformDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.ContinousUniformDistribution] = None,
        min: float = None,
        max: float = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.ContinousUniformDistribution()
        self.proto = proto
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    def _update_proto_references(self, proto: pd_distributions_pb2.ContinousUniformDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.Bucket)
class Bucket(ProtoMessageClass):
    """
    A discrete value with an associated probability.

    Args:
        string_value: :attr:`string_value`
        float_value: :attr:`float_value`
        int32_value: :attr:`int32_value`
        probability: :attr:`probability`
    Attributes:
        string_value: String name of the bucket.
        float_value: Float value of the bucket.
        int32_value: Integer value of the bucket.
        probability: The probability associated with the bucket."""

    _proto_message = pd_distributions_pb2.Bucket

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.Bucket] = None,
        string_value: str = None,
        float_value: float = None,
        int32_value: int = None,
        probability: float = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.Bucket()
        self.proto = proto
        if string_value is not None:
            self.string_value = string_value
        if float_value is not None:
            self.float_value = float_value
        if int32_value is not None:
            self.int32_value = int32_value
        if probability is not None:
            self.probability = probability

    @property
    def string_value(self) -> str:
        return self.proto.string_value

    @string_value.setter
    def string_value(self, value: str):
        self.proto.string_value = value

    @property
    def float_value(self) -> float:
        return self.proto.float_value

    @float_value.setter
    def float_value(self, value: float):
        self.proto.float_value = value

    @property
    def int32_value(self) -> int:
        return self.proto.int32_value

    @int32_value.setter
    def int32_value(self, value: int):
        self.proto.int32_value = value

    @property
    def probability(self) -> float:
        return self.proto.probability

    @probability.setter
    def probability(self, value: float):
        self.proto.probability = value

    def _update_proto_references(self, proto: pd_distributions_pb2.Bucket):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.DiscreteUniformDistribution)
class DiscreteUniformDistribution(ProtoMessageClass):
    """
    A discrete distribution in which each bucket has a uniform probability.

    Args:
        buckets: :attr:`buckets`
    Attributes:
        buckets: The buckets which make up the discrete distribution."""

    _proto_message = pd_distributions_pb2.DiscreteUniformDistribution

    def __init__(
        self, *, proto: Optional[pd_distributions_pb2.DiscreteUniformDistribution] = None, buckets: List[Bucket] = None
    ):
        if proto is None:
            proto = pd_distributions_pb2.DiscreteUniformDistribution()
        self.proto = proto
        self._buckets = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.buckets],
            attr_name="buckets",
            list_owner=self,
        )
        if buckets is not None:
            self.buckets = buckets

    @property
    def buckets(self) -> List[Bucket]:
        return self._buckets

    @buckets.setter
    def buckets(self, value: List[Bucket]):
        self._buckets.clear()
        for v in value:
            self._buckets.append(v)

    def _update_proto_references(self, proto: pd_distributions_pb2.DiscreteUniformDistribution):
        self.proto = proto
        for i, v in enumerate(self.buckets):
            v._update_proto_references(self.proto.buckets[i])


@register_wrapper(proto_type=pd_distributions_pb2.CategoricalDistribution)
class CategoricalDistribution(ProtoMessageClass):
    """
    Discrete probability distribution that describes the results of
    a random variable that can take on one of K possible categories,
    with the probability of each category (bucket) separately specified.

    Args:
        buckets: :attr:`buckets`
    Attributes:
        buckets: The buckets which make up the distribution."""

    _proto_message = pd_distributions_pb2.CategoricalDistribution

    def __init__(
        self, *, proto: Optional[pd_distributions_pb2.CategoricalDistribution] = None, buckets: List[Bucket] = None
    ):
        if proto is None:
            proto = pd_distributions_pb2.CategoricalDistribution()
        self.proto = proto
        self._buckets = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.buckets],
            attr_name="buckets",
            list_owner=self,
        )
        if buckets is not None:
            self.buckets = buckets

    @property
    def buckets(self) -> List[Bucket]:
        return self._buckets

    @buckets.setter
    def buckets(self, value: List[Bucket]):
        self._buckets.clear()
        for v in value:
            self._buckets.append(v)

    def _update_proto_references(self, proto: pd_distributions_pb2.CategoricalDistribution):
        self.proto = proto
        for i, v in enumerate(self.buckets):
            v._update_proto_references(self.proto.buckets[i])


@register_wrapper(proto_type=pd_distributions_pb2.ConstantDistribution)
class ConstantDistribution(ProtoMessageClass):
    """
    A single sample distribution.

    Args:
        string_value: :attr:`string_value`
        float_value: :attr:`float_value`
        int32_value: :attr:`int32_value`
    Attributes:
        string_value: The string value of the distribution.
        float_value: The float value of the distribution.
        int32_value: The integer value of the distribution."""

    _proto_message = pd_distributions_pb2.ConstantDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.ConstantDistribution] = None,
        string_value: str = None,
        float_value: float = None,
        int32_value: int = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.ConstantDistribution()
        self.proto = proto
        if string_value is not None:
            self.string_value = string_value
        if float_value is not None:
            self.float_value = float_value
        if int32_value is not None:
            self.int32_value = int32_value

    @property
    def string_value(self) -> str:
        return self.proto.string_value

    @string_value.setter
    def string_value(self, value: str):
        self.proto.string_value = value

    @property
    def float_value(self) -> float:
        return self.proto.float_value

    @float_value.setter
    def float_value(self, value: float):
        self.proto.float_value = value

    @property
    def int32_value(self) -> int:
        return self.proto.int32_value

    @int32_value.setter
    def int32_value(self, value: int):
        self.proto.int32_value = value

    def _update_proto_references(self, proto: pd_distributions_pb2.ConstantDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.EnumDistribution)
class EnumDistribution(ProtoMessageClass):
    """
    A distribution represented by categories and their corresponding probabilities.
    All probability weights in the distribution should sum up to 1.

    Args:
        probabilities: :attr:`probabilities`
    Attributes:
        probabilities: The name and corresponding probability of each category."""

    _proto_message = pd_distributions_pb2.EnumDistribution

    def __init__(
        self, *, proto: Optional[pd_distributions_pb2.EnumDistribution] = None, probabilities: Dict[str, float] = None
    ):
        if proto is None:
            proto = pd_distributions_pb2.EnumDistribution()
        self.proto = proto
        self._probabilities = ProtoDictWrapper(
            container={k: float(v) for (k, v) in proto.probabilities.items()},
            attr_name="probabilities",
            dict_owner=self,
        )
        if probabilities is not None:
            self.probabilities = probabilities

    @property
    def probabilities(self) -> Dict[str, float]:
        return self._probabilities

    @probabilities.setter
    def probabilities(self, value: Dict[str, float]):
        self._probabilities.clear()
        self._probabilities.update(value)

    def _update_proto_references(self, proto: pd_distributions_pb2.EnumDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_distributions_pb2.Distribution)
class Distribution(ProtoMessageClass):
    """
    A wrapper which contains a single distribution.

    Args:
        normal: :attr:`normal`
        truncated_normal: :attr:`truncated_normal`
        uniform_continous: :attr:`uniform_continous`
        constant: :attr:`constant`
        uniform_discrete: :attr:`uniform_discrete`
        categorical: :attr:`categorical`
    Attributes:
        normal: A normal distribution.
        truncated_normal: A truncated normal distribution.
        uniform_continous: A continuous uniform distribution.
        constant: A constant distribution.
        uniform_discrete: A discrete uniform distribution.
        categorical: A categorical distribution."""

    _proto_message = pd_distributions_pb2.Distribution

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.Distribution] = None,
        normal: NormalDistribution = None,
        truncated_normal: TrucatedNormalDistribution = None,
        uniform_continous: ContinousUniformDistribution = None,
        constant: ConstantDistribution = None,
        uniform_discrete: DiscreteUniformDistribution = None,
        categorical: CategoricalDistribution = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.Distribution()
        self.proto = proto
        self._normal = get_wrapper(proto_type=proto.normal.__class__)(proto=proto.normal)
        self._truncated_normal = get_wrapper(proto_type=proto.truncated_normal.__class__)(proto=proto.truncated_normal)
        self._uniform_continous = get_wrapper(proto_type=proto.uniform_continous.__class__)(
            proto=proto.uniform_continous
        )
        self._constant = get_wrapper(proto_type=proto.constant.__class__)(proto=proto.constant)
        self._uniform_discrete = get_wrapper(proto_type=proto.uniform_discrete.__class__)(proto=proto.uniform_discrete)
        self._categorical = get_wrapper(proto_type=proto.categorical.__class__)(proto=proto.categorical)
        if normal is not None:
            self.normal = normal
        if truncated_normal is not None:
            self.truncated_normal = truncated_normal
        if uniform_continous is not None:
            self.uniform_continous = uniform_continous
        if constant is not None:
            self.constant = constant
        if uniform_discrete is not None:
            self.uniform_discrete = uniform_discrete
        if categorical is not None:
            self.categorical = categorical

    @property
    def normal(self) -> NormalDistribution:
        return self._normal

    @normal.setter
    def normal(self, value: NormalDistribution):
        self.proto.normal.CopyFrom(value.proto)

        self._normal = value
        self._normal._update_proto_references(self.proto.normal)

    @property
    def truncated_normal(self) -> TrucatedNormalDistribution:
        return self._truncated_normal

    @truncated_normal.setter
    def truncated_normal(self, value: TrucatedNormalDistribution):
        self.proto.truncated_normal.CopyFrom(value.proto)

        self._truncated_normal = value
        self._truncated_normal._update_proto_references(self.proto.truncated_normal)

    @property
    def uniform_continous(self) -> ContinousUniformDistribution:
        return self._uniform_continous

    @uniform_continous.setter
    def uniform_continous(self, value: ContinousUniformDistribution):
        self.proto.uniform_continous.CopyFrom(value.proto)

        self._uniform_continous = value
        self._uniform_continous._update_proto_references(self.proto.uniform_continous)

    @property
    def constant(self) -> ConstantDistribution:
        return self._constant

    @constant.setter
    def constant(self, value: ConstantDistribution):
        self.proto.constant.CopyFrom(value.proto)

        self._constant = value
        self._constant._update_proto_references(self.proto.constant)

    @property
    def uniform_discrete(self) -> DiscreteUniformDistribution:
        return self._uniform_discrete

    @uniform_discrete.setter
    def uniform_discrete(self, value: DiscreteUniformDistribution):
        self.proto.uniform_discrete.CopyFrom(value.proto)

        self._uniform_discrete = value
        self._uniform_discrete._update_proto_references(self.proto.uniform_discrete)

    @property
    def categorical(self) -> CategoricalDistribution:
        return self._categorical

    @categorical.setter
    def categorical(self, value: CategoricalDistribution):
        self.proto.categorical.CopyFrom(value.proto)

        self._categorical = value
        self._categorical._update_proto_references(self.proto.categorical)

    def _update_proto_references(self, proto: pd_distributions_pb2.Distribution):
        self.proto = proto
        self._normal._update_proto_references(proto.normal)
        self._truncated_normal._update_proto_references(proto.truncated_normal)
        self._uniform_continous._update_proto_references(proto.uniform_continous)
        self._constant._update_proto_references(proto.constant)
        self._uniform_discrete._update_proto_references(proto.uniform_discrete)
        self._categorical._update_proto_references(proto.categorical)


@register_wrapper(proto_type=pd_distributions_pb2.VehicleCategoryWeight)
class VehicleCategoryWeight(ProtoMessageClass):
    """
    The spawn probability weight of a particular vehicle category.

    Args:
        weight: :attr:`weight`
        model_weights: :attr:`model_weights`
    Attributes:
        weight: The spawn weight of a particular vehicle category.
        model_weights: A list containing the name of a vehicle model within the vehicle category, and the spawn probability weight
            of that vehicle mode"""

    _proto_message = pd_distributions_pb2.VehicleCategoryWeight

    def __init__(
        self,
        *,
        proto: Optional[pd_distributions_pb2.VehicleCategoryWeight] = None,
        weight: float = None,
        model_weights: Dict[str, float] = None,
    ):
        if proto is None:
            proto = pd_distributions_pb2.VehicleCategoryWeight()
        self.proto = proto
        if weight is not None:
            self.weight = weight
        self._model_weights = ProtoDictWrapper(
            container={k: float(v) for (k, v) in proto.model_weights.items()},
            attr_name="model_weights",
            dict_owner=self,
        )
        if model_weights is not None:
            self.model_weights = model_weights

    @property
    def weight(self) -> float:
        return self.proto.weight

    @weight.setter
    def weight(self, value: float):
        self.proto.weight = value

    @property
    def model_weights(self) -> Dict[str, float]:
        return self._model_weights

    @model_weights.setter
    def model_weights(self, value: Dict[str, float]):
        self._model_weights.clear()
        self._model_weights.update(value)

    def _update_proto_references(self, proto: pd_distributions_pb2.VehicleCategoryWeight):
        self.proto = proto
