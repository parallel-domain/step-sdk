# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import enum
import math
import random
from typing import Any, Callable, Dict, List, Tuple, TypeVar, Union

import numpy as np

from pd.internal.proto.keystone.generated.python import pd_distributions_pb2 as pd_distributions_pb2_base
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2, pd_unified_generator_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import register_wrapper

T = TypeVar("T")
K = TypeVar("K")
N = Union[float, int]
EnumDistribution = pd_distributions_pb2.EnumDistribution


VehicleCategoryWeight = pd_distributions_pb2.VehicleCategoryWeight
SignalLightDistribution = pd_unified_generator_pb2.SignalLightDistribution
TurnTypeDistribution = pd_unified_generator_pb2.TurnTypeDistribution
ParkingTypeDistribution = pd_unified_generator_pb2.ParkingTypeDistribution
CenterSpreadProbabilityConfig = pd_unified_generator_pb2.CenterSpreadProbabilityConfig
CenterSpreadConfig = pd_unified_generator_pb2.CenterSpreadConfig
CenterSpreadConfigInt = pd_unified_generator_pb2.CenterSpreadConfigInt
MinMaxConfigFloat = pd_unified_generator_pb2.MinMaxConfigFloat
MinMaxConfigInt = pd_unified_generator_pb2.MinMaxConfigInt


@register_wrapper(proto_type=pd_distributions_pb2_base.NormalDistribution)
class NormalDistribution(pd_distributions_pb2.NormalDistribution):
    def sample(self, random_seed: int) -> Union[float, int]:
        """Sample from a normal distribution with mean and variance.

        Args:
            random_seed: Random seed.

        Returns:
            Sampled value.
        """
        random_state = np.random.RandomState(random_seed)
        return float(random_state.normal(self.mean, math.sqrt(self.variance)))


@register_wrapper(proto_type=pd_distributions_pb2_base.TrucatedNormalDistribution)
class TrucatedNormalDistribution(pd_distributions_pb2.TrucatedNormalDistribution):
    def sample(self, random_seed: int) -> Union[float, int]:
        """
        Raises:
            :obj:`NotImplementedError` every time.
        """
        raise NotImplementedError()


@register_wrapper(proto_type=pd_distributions_pb2_base.ContinousUniformDistribution)
class ContinousUniformDistribution(pd_distributions_pb2.ContinousUniformDistribution):
    def sample(self, random_seed: int) -> Union[float, int]:
        """Sample from a continuous uniform distribution with min and max.

        Args:
            random_seed: Random seed.

        Returns:
            Sampled value.
        """
        random_state = random.Random(random_seed)

        diff = self.max - self.min
        value = self.min + diff * random_state.random()
        if isinstance(self.max, int) and isinstance(self.min, int):
            value = int(value)
        return value


@register_wrapper(proto_type=pd_distributions_pb2_base.Bucket)
class Bucket(pd_distributions_pb2.Bucket):
    @property
    def value(self) -> Union[str, int, float]:
        if self.proto.HasField("int32_value"):
            return self.proto.int32_value
        elif self.proto.HasField("string_value"):
            return self.proto.string_value
        elif self.proto.HasField("float_value"):
            return self.proto.float_value
        raise ValueError()

    @value.setter
    def value(self, val: Union[str, int, float]):
        if self.proto.HasField("int32_value"):
            self.proto.int32_value = val
        elif self.proto.HasField("string_value"):
            self.proto.string_value = val
        elif self.proto.HasField("float_value"):
            self.proto.float_value = val

    @staticmethod
    def from_value(value: Union[str, int, float], probability: float) -> "Bucket":
        if isinstance(value, int):
            return Bucket(int32_value=value, probability=probability)
        elif isinstance(value, str):
            return Bucket(string_value=value, probability=probability)
        elif isinstance(value, float):
            return Bucket(float_value=value, probability=probability)
        elif isinstance(value, Bucket):
            val = value.clone()
            val.probability = probability
            return val
        raise ValueError()


@register_wrapper(proto_type=pd_distributions_pb2_base.DiscreteUniformDistribution)
class DiscreteUniformDistribution(pd_distributions_pb2.DiscreteUniformDistribution):
    def sample(self, random_seed: int) -> Bucket:
        """Sample from a discrete uniform distribution with buckets.

        Args:
            random_seed: Random seed.

        Returns:
            Sampled value.
        """
        random_state = random.Random(random_seed)

        choices = list()
        weights = list()
        for bucket in self.buckets:
            choices.append(bucket)
            weights.append(bucket.probability)

        return random_state.choices(choices, weights=weights, k=1)[0]


@register_wrapper(proto_type=pd_distributions_pb2_base.CategoricalDistribution)
class CategoricalDistribution(pd_distributions_pb2.CategoricalDistribution):
    def set_category_weight(self, category: Union[float, int, str, Bucket], weight: float = 1.0):
        if not any(
            [
                b.value == category if not isinstance(category, Bucket) else b.value == category.value
                for b in self.buckets
            ]
        ):
            category = Bucket.from_value(value=category, probability=weight)
            self.buckets.append(category)
        else:
            if isinstance(category, Bucket):
                bucket = next(iter([b for b in self.buckets if b.value == category.value]))
                bucket.probability = weight
                bucket.value = category.value
            else:
                bucket = next(iter([b for b in self.buckets if b.value == category]))
                bucket.probability = weight

    def sample(self, random_seed: int) -> Bucket:
        """Sample from a categorical distribution with buckets.

        Args:
            random_seed: Random seed.

        Returns:
            Sampled value.
        """
        random_state = random.Random(random_seed)

        choices = list()
        weights = list()
        for bucket in self.buckets:
            choices.append(bucket.value)
            weights.append(bucket.probability)

        return random_state.choices(choices, weights=weights, k=1)[0]

    @property
    def is_set(self) -> bool:
        return len(self.buckets) > 0


@register_wrapper(proto_type=pd_distributions_pb2_base.ConstantDistribution)
class ConstantDistribution(pd_distributions_pb2.ConstantDistribution):
    ...

    @staticmethod
    def from_value(value: Union[str, int, float]) -> "ConstantDistribution":
        if isinstance(value, int):
            return ConstantDistribution(int32_value=value)
        elif isinstance(value, str):
            return ConstantDistribution(string_value=value)
        elif isinstance(value, float):
            return ConstantDistribution(float_value=value)
        else:
            pass

    @property
    def value(self) -> Union[str, int, float]:
        if self.proto.HasField("int32_value"):
            return self.proto.int32_value
        elif self.proto.HasField("string_value"):
            return self.proto.string_value
        elif self.proto.HasField("float_value"):
            return self.proto.float_value
        raise ValueError()


@register_wrapper(proto_type=pd_distributions_pb2_base.Distribution)
class Distribution(pd_distributions_pb2.Distribution):
    def set_choices(self, choices: List[T], weights: List[float] = None):
        weights = weights if weights is not None else [1.0 for _ in range(len(choices))]
        self.uniform_discrete = DiscreteUniformDistribution(
            buckets=[Bucket.from_value(value=s, probability=p) for s, p in zip(choices, weights)]
        )

    def set_categorial_choices(self, choices: List[T], weights: List[float] = None):
        weights = weights if weights is not None else [1.0 for _ in range(len(choices))]
        for s, p in zip(choices, weights):
            self.categorical.buckets.append(Bucket.from_value(value=s, probability=p))

    def set_category_weight(self, category: Any, weight: float = 1.0):
        if not self.proto.HasField("categorical"):
            self.set_categorial_choices(choices=[category], weights=[weight])
        else:
            self.categorical.set_category_weight(category=category, weight=weight)

    def set_uniform_distribution(self, min_value: float, max_value: float):
        self.uniform_continous = ContinousUniformDistribution(min=min_value, max=max_value)

    def set_constant_value(self, value: T):
        if isinstance(value, enum.Enum):
            value = value.value
        self.constant = ConstantDistribution.from_value(value=value)

    @property
    def is_set(self) -> bool:
        if (
            self.proto.HasField("categorical")
            or self.proto.HasField("uniform_discrete")
            or self.proto.HasField("uniform_continous")
            or self.proto.HasField("constant")
        ):
            return True
        else:
            return False

    def sample(self, random_seed: int) -> Union[str, int, float, Bucket]:
        """Sample from a distribution.

        Args:
            random_seed: Random seed.

        Returns:
            Sampled value.
        """
        field = self.proto.WhichOneof("distribution")
        if field == "categorical":
            sampled = self.categorical.sample(random_seed=random_seed)
        elif field == "uniform_discrete":
            sampled = self.uniform_discrete.sample(random_seed=random_seed)
        elif field == "uniform_continous":
            sampled = self.uniform_continous.sample(random_seed=random_seed)
        elif field == "constant":
            sampled = self.constant.value
        else:
            raise ValueError("Missing assigned distribution!")
        return sampled

    @staticmethod
    def create(
        value: Union[Callable[[], T], List[T], Dict[K, List[T]], Tuple[T, T], T],
    ) -> "Distribution":
        distribution: Distribution = Distribution()
        if isinstance(value, list):
            distribution.set_categorial_choices(choices=value)
        elif isinstance(value, tuple):
            distribution.set_uniform_distribution(min_value=value[0], max_value=value[1])
        else:
            distribution.set_constant_value(value=value)
        return distribution
