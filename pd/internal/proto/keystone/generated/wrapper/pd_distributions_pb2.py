from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_distributions_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_distributions_pb2.Bucket)
class Bucket(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.Bucket

    def __init__(self, *, proto: Optional[pd_distributions_pb2.Bucket]=None, float_value: Optional[float]=None, int32_value: Optional[int]=None, probability: Optional[float]=None, string_value: Optional[str]=None):
        if proto is None:
            proto = pd_distributions_pb2.Bucket()
        self.proto = proto
        if float_value is not None:
            self.float_value = float_value
        if int32_value is not None:
            self.int32_value = int32_value
        if probability is not None:
            self.probability = probability
        if string_value is not None:
            self.string_value = string_value

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

    @property
    def string_value(self) -> str:
        return self.proto.string_value

    @string_value.setter
    def string_value(self, value: str):
        self.proto.string_value = value

    def _update_proto_references(self, proto: pd_distributions_pb2.Bucket):
        self.proto = proto

@register_wrapper(proto_type=pd_distributions_pb2.CategoricalDistribution)
class CategoricalDistribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.CategoricalDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.CategoricalDistribution]=None, buckets: Optional[List[Bucket]]=None):
        if proto is None:
            proto = pd_distributions_pb2.CategoricalDistribution()
        self.proto = proto
        self._buckets = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.buckets], attr_name='buckets', list_owner=self)
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
    _proto_message = pd_distributions_pb2.ConstantDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.ConstantDistribution]=None, float_value: Optional[float]=None, int32_value: Optional[int]=None, string_value: Optional[str]=None):
        if proto is None:
            proto = pd_distributions_pb2.ConstantDistribution()
        self.proto = proto
        if float_value is not None:
            self.float_value = float_value
        if int32_value is not None:
            self.int32_value = int32_value
        if string_value is not None:
            self.string_value = string_value

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
    def string_value(self) -> str:
        return self.proto.string_value

    @string_value.setter
    def string_value(self, value: str):
        self.proto.string_value = value

    def _update_proto_references(self, proto: pd_distributions_pb2.ConstantDistribution):
        self.proto = proto

@register_wrapper(proto_type=pd_distributions_pb2.ContinousUniformDistribution)
class ContinousUniformDistribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.ContinousUniformDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.ContinousUniformDistribution]=None, max: Optional[float]=None, min: Optional[float]=None):
        if proto is None:
            proto = pd_distributions_pb2.ContinousUniformDistribution()
        self.proto = proto
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

    def _update_proto_references(self, proto: pd_distributions_pb2.ContinousUniformDistribution):
        self.proto = proto

@register_wrapper(proto_type=pd_distributions_pb2.DiscreteUniformDistribution)
class DiscreteUniformDistribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.DiscreteUniformDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.DiscreteUniformDistribution]=None, buckets: Optional[List[Bucket]]=None):
        if proto is None:
            proto = pd_distributions_pb2.DiscreteUniformDistribution()
        self.proto = proto
        self._buckets = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.buckets], attr_name='buckets', list_owner=self)
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

@register_wrapper(proto_type=pd_distributions_pb2.Distribution)
class Distribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.Distribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.Distribution]=None, categorical: Optional[CategoricalDistribution]=None, constant: Optional[ConstantDistribution]=None, normal: Optional[NormalDistribution]=None, truncated_normal: Optional[TrucatedNormalDistribution]=None, uniform_continous: Optional[ContinousUniformDistribution]=None, uniform_discrete: Optional[DiscreteUniformDistribution]=None):
        if proto is None:
            proto = pd_distributions_pb2.Distribution()
        self.proto = proto
        self._categorical = get_wrapper(proto_type=proto.categorical.__class__)(proto=proto.categorical)
        self._constant = get_wrapper(proto_type=proto.constant.__class__)(proto=proto.constant)
        self._normal = get_wrapper(proto_type=proto.normal.__class__)(proto=proto.normal)
        self._truncated_normal = get_wrapper(proto_type=proto.truncated_normal.__class__)(proto=proto.truncated_normal)
        self._uniform_continous = get_wrapper(proto_type=proto.uniform_continous.__class__)(proto=proto.uniform_continous)
        self._uniform_discrete = get_wrapper(proto_type=proto.uniform_discrete.__class__)(proto=proto.uniform_discrete)
        if categorical is not None:
            self.categorical = categorical
        if constant is not None:
            self.constant = constant
        if normal is not None:
            self.normal = normal
        if truncated_normal is not None:
            self.truncated_normal = truncated_normal
        if uniform_continous is not None:
            self.uniform_continous = uniform_continous
        if uniform_discrete is not None:
            self.uniform_discrete = uniform_discrete

    @property
    def categorical(self) -> CategoricalDistribution:
        return self._categorical

    @categorical.setter
    def categorical(self, value: CategoricalDistribution):
        self.proto.categorical.CopyFrom(value.proto)
        
        self._categorical = value
        self._categorical._update_proto_references(self.proto.categorical)

    @property
    def constant(self) -> ConstantDistribution:
        return self._constant

    @constant.setter
    def constant(self, value: ConstantDistribution):
        self.proto.constant.CopyFrom(value.proto)
        
        self._constant = value
        self._constant._update_proto_references(self.proto.constant)

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
    def uniform_discrete(self) -> DiscreteUniformDistribution:
        return self._uniform_discrete

    @uniform_discrete.setter
    def uniform_discrete(self, value: DiscreteUniformDistribution):
        self.proto.uniform_discrete.CopyFrom(value.proto)
        
        self._uniform_discrete = value
        self._uniform_discrete._update_proto_references(self.proto.uniform_discrete)

    def _update_proto_references(self, proto: pd_distributions_pb2.Distribution):
        self.proto = proto
        self._categorical._update_proto_references(proto.categorical)
        self._constant._update_proto_references(proto.constant)
        self._normal._update_proto_references(proto.normal)
        self._truncated_normal._update_proto_references(proto.truncated_normal)
        self._uniform_continous._update_proto_references(proto.uniform_continous)
        self._uniform_discrete._update_proto_references(proto.uniform_discrete)

@register_wrapper(proto_type=pd_distributions_pb2.EnumDistribution)
class EnumDistribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.EnumDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.EnumDistribution]=None, probabilities: Optional[Dict[str, float]]=None):
        if proto is None:
            proto = pd_distributions_pb2.EnumDistribution()
        self.proto = proto
        self._probabilities = ProtoDictWrapper(container={k: float(v) for (k, v) in proto.probabilities.items()}, attr_name='probabilities', dict_owner=self)
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

@register_wrapper(proto_type=pd_distributions_pb2.NormalDistribution)
class NormalDistribution(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.NormalDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.NormalDistribution]=None, mean: Optional[float]=None, variance: Optional[float]=None):
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
    _proto_message = pd_distributions_pb2.TrucatedNormalDistribution

    def __init__(self, *, proto: Optional[pd_distributions_pb2.TrucatedNormalDistribution]=None, max: Optional[float]=None, mean: Optional[float]=None, min: Optional[float]=None, variance: Optional[float]=None):
        if proto is None:
            proto = pd_distributions_pb2.TrucatedNormalDistribution()
        self.proto = proto
        if max is not None:
            self.max = max
        if mean is not None:
            self.mean = mean
        if min is not None:
            self.min = min
        if variance is not None:
            self.variance = variance

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    @property
    def mean(self) -> float:
        return self.proto.mean

    @mean.setter
    def mean(self, value: float):
        self.proto.mean = value

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

    @property
    def variance(self) -> float:
        return self.proto.variance

    @variance.setter
    def variance(self, value: float):
        self.proto.variance = value

    def _update_proto_references(self, proto: pd_distributions_pb2.TrucatedNormalDistribution):
        self.proto = proto

@register_wrapper(proto_type=pd_distributions_pb2.VehicleCategoryWeight)
class VehicleCategoryWeight(ProtoMessageClass):
    _proto_message = pd_distributions_pb2.VehicleCategoryWeight

    def __init__(self, *, proto: Optional[pd_distributions_pb2.VehicleCategoryWeight]=None, model_weights: Optional[Dict[str, float]]=None, weight: Optional[float]=None):
        if proto is None:
            proto = pd_distributions_pb2.VehicleCategoryWeight()
        self.proto = proto
        self._model_weights = ProtoDictWrapper(container={k: float(v) for (k, v) in proto.model_weights.items()}, attr_name='model_weights', dict_owner=self)
        if model_weights is not None:
            self.model_weights = model_weights
        if weight is not None:
            self.weight = weight

    @property
    def model_weights(self) -> Dict[str, float]:
        return self._model_weights

    @model_weights.setter
    def model_weights(self, value: Dict[str, float]):
        self._model_weights.clear()
        self._model_weights.update(value)

    @property
    def weight(self) -> float:
        return self.proto.weight

    @weight.setter
    def weight(self, value: float):
        self.proto.weight = value

    def _update_proto_references(self, proto: pd_distributions_pb2.VehicleCategoryWeight):
        self.proto = proto