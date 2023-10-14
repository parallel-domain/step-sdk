from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_environments_pb2
)
from . import (
    pd_distributions_pb2 as _pd_distributions_pb2
)


@register_wrapper(proto_type=pd_environments_pb2.EnvironmentPreset)
class EnvironmentPreset(ProtoMessageClass):
    """
    Args:
        time_of_day: :attr:`time_of_day`
        cloud_coverage: :attr:`cloud_coverage`
        rain_intensity: :attr:`rain_intensity`
        fog_intensity: :attr:`fog_intensity`
        wetness: :attr:`wetness`
        independent_wetness: :attr:`independent_wetness`
    Attributes:
        time_of_day: This is where we want to go with dynamic time of day
            Distribution sun_angle = 1;
            This is what we currently support
        cloud_coverage:
        rain_intensity:
        fog_intensity:
        wetness:
        independent_wetness: Maybe there is a more elegant way to couple/decouple rain from wetness"""

    _proto_message = pd_environments_pb2.EnvironmentPreset

    def __init__(
        self,
        *,
        proto: Optional[pd_environments_pb2.EnvironmentPreset] = None,
        time_of_day: _pd_distributions_pb2.CategoricalDistribution = None,
        cloud_coverage: _pd_distributions_pb2.Distribution = None,
        rain_intensity: _pd_distributions_pb2.Distribution = None,
        fog_intensity: _pd_distributions_pb2.Distribution = None,
        wetness: _pd_distributions_pb2.Distribution = None,
        independent_wetness: bool = None,
    ):
        if proto is None:
            proto = pd_environments_pb2.EnvironmentPreset()
        self.proto = proto
        self._time_of_day = get_wrapper(proto_type=proto.time_of_day.__class__)(proto=proto.time_of_day)
        self._cloud_coverage = get_wrapper(proto_type=proto.cloud_coverage.__class__)(proto=proto.cloud_coverage)
        self._rain_intensity = get_wrapper(proto_type=proto.rain_intensity.__class__)(proto=proto.rain_intensity)
        self._fog_intensity = get_wrapper(proto_type=proto.fog_intensity.__class__)(proto=proto.fog_intensity)
        self._wetness = get_wrapper(proto_type=proto.wetness.__class__)(proto=proto.wetness)
        if time_of_day is not None:
            self.time_of_day = time_of_day
        if cloud_coverage is not None:
            self.cloud_coverage = cloud_coverage
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if wetness is not None:
            self.wetness = wetness
        if independent_wetness is not None:
            self.independent_wetness = independent_wetness

    @property
    def time_of_day(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.time_of_day.CopyFrom(value.proto)

        self._time_of_day = value
        self._time_of_day._update_proto_references(self.proto.time_of_day)

    @property
    def cloud_coverage(self) -> _pd_distributions_pb2.Distribution:
        return self._cloud_coverage

    @cloud_coverage.setter
    def cloud_coverage(self, value: _pd_distributions_pb2.Distribution):
        self.proto.cloud_coverage.CopyFrom(value.proto)

        self._cloud_coverage = value
        self._cloud_coverage._update_proto_references(self.proto.cloud_coverage)

    @property
    def rain_intensity(self) -> _pd_distributions_pb2.Distribution:
        return self._rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: _pd_distributions_pb2.Distribution):
        self.proto.rain_intensity.CopyFrom(value.proto)

        self._rain_intensity = value
        self._rain_intensity._update_proto_references(self.proto.rain_intensity)

    @property
    def fog_intensity(self) -> _pd_distributions_pb2.Distribution:
        return self._fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: _pd_distributions_pb2.Distribution):
        self.proto.fog_intensity.CopyFrom(value.proto)

        self._fog_intensity = value
        self._fog_intensity._update_proto_references(self.proto.fog_intensity)

    @property
    def wetness(self) -> _pd_distributions_pb2.Distribution:
        return self._wetness

    @wetness.setter
    def wetness(self, value: _pd_distributions_pb2.Distribution):
        self.proto.wetness.CopyFrom(value.proto)

        self._wetness = value
        self._wetness._update_proto_references(self.proto.wetness)

    @property
    def independent_wetness(self) -> bool:
        return self.proto.independent_wetness

    @independent_wetness.setter
    def independent_wetness(self, value: bool):
        self.proto.independent_wetness = value

    def _update_proto_references(self, proto: pd_environments_pb2.EnvironmentPreset):
        self.proto = proto
        self._time_of_day._update_proto_references(proto.time_of_day)
        self._cloud_coverage._update_proto_references(proto.cloud_coverage)
        self._rain_intensity._update_proto_references(proto.rain_intensity)
        self._fog_intensity._update_proto_references(proto.fog_intensity)
        self._wetness._update_proto_references(proto.wetness)


@register_wrapper(proto_type=pd_environments_pb2.EnvironmentDefinition)
class EnvironmentDefinition(ProtoMessageClass):
    """
    Args:
        preset_distribution: :attr:`preset_distribution`
        presets: :attr:`presets`
    Attributes:
        preset_distribution: The number of categories in the distribution must match the number of scenario presets
        presets:"""

    _proto_message = pd_environments_pb2.EnvironmentDefinition

    def __init__(
        self,
        *,
        proto: Optional[pd_environments_pb2.EnvironmentDefinition] = None,
        preset_distribution: _pd_distributions_pb2.CategoricalDistribution = None,
        presets: List[EnvironmentPreset] = None,
    ):
        if proto is None:
            proto = pd_environments_pb2.EnvironmentDefinition()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(
            proto=proto.preset_distribution
        )
        self._presets = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets],
            attr_name="presets",
            list_owner=self,
        )
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution
        if presets is not None:
            self.presets = presets

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.preset_distribution.CopyFrom(value.proto)

        self._preset_distribution = value
        self._preset_distribution._update_proto_references(self.proto.preset_distribution)

    @property
    def presets(self) -> List[EnvironmentPreset]:
        return self._presets

    @presets.setter
    def presets(self, value: List[EnvironmentPreset]):
        self._presets.clear()
        for v in value:
            self._presets.append(v)

    def _update_proto_references(self, proto: pd_environments_pb2.EnvironmentDefinition):
        self.proto = proto
        self._preset_distribution._update_proto_references(proto.preset_distribution)
        for i, v in enumerate(self.presets):
            v._update_proto_references(self.proto.presets[i])
