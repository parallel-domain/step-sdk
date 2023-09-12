from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_environments_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_step_batch_pb2 as _pd_step_batch_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_environments_pb2.EnvironmentDefinition)
class EnvironmentDefinition(ProtoMessageClass):
    _proto_message = pd_environments_pb2.EnvironmentDefinition

    def __init__(self, *, proto: Optional[pd_environments_pb2.EnvironmentDefinition]=None, preset_distribution: Optional[_pd_distributions_pb2.CategoricalDistribution]=None, presets: Optional[List[EnvironmentPreset]]=None):
        if proto is None:
            proto = pd_environments_pb2.EnvironmentDefinition()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(proto=proto.preset_distribution)
        self._presets = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets], attr_name='presets', list_owner=self)
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

@register_wrapper(proto_type=pd_environments_pb2.EnvironmentPreset)
class EnvironmentPreset(ProtoMessageClass):
    _proto_message = pd_environments_pb2.EnvironmentPreset

    def __init__(self, *, proto: Optional[pd_environments_pb2.EnvironmentPreset]=None, cloud_coverage: Optional[_pd_distributions_pb2.Distribution]=None, fog_intensity: Optional[_pd_distributions_pb2.Distribution]=None, independent_wetness: Optional[bool]=None, rain_intensity: Optional[_pd_distributions_pb2.Distribution]=None, time_of_day: Optional[_pd_distributions_pb2.CategoricalDistribution]=None, wetness: Optional[_pd_distributions_pb2.Distribution]=None):
        if proto is None:
            proto = pd_environments_pb2.EnvironmentPreset()
        self.proto = proto
        self._cloud_coverage = get_wrapper(proto_type=proto.cloud_coverage.__class__)(proto=proto.cloud_coverage)
        self._fog_intensity = get_wrapper(proto_type=proto.fog_intensity.__class__)(proto=proto.fog_intensity)
        self._rain_intensity = get_wrapper(proto_type=proto.rain_intensity.__class__)(proto=proto.rain_intensity)
        self._time_of_day = get_wrapper(proto_type=proto.time_of_day.__class__)(proto=proto.time_of_day)
        self._wetness = get_wrapper(proto_type=proto.wetness.__class__)(proto=proto.wetness)
        if cloud_coverage is not None:
            self.cloud_coverage = cloud_coverage
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if independent_wetness is not None:
            self.independent_wetness = independent_wetness
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if time_of_day is not None:
            self.time_of_day = time_of_day
        if wetness is not None:
            self.wetness = wetness

    @property
    def cloud_coverage(self) -> _pd_distributions_pb2.Distribution:
        return self._cloud_coverage

    @cloud_coverage.setter
    def cloud_coverage(self, value: _pd_distributions_pb2.Distribution):
        self.proto.cloud_coverage.CopyFrom(value.proto)
        
        self._cloud_coverage = value
        self._cloud_coverage._update_proto_references(self.proto.cloud_coverage)

    @property
    def fog_intensity(self) -> _pd_distributions_pb2.Distribution:
        return self._fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: _pd_distributions_pb2.Distribution):
        self.proto.fog_intensity.CopyFrom(value.proto)
        
        self._fog_intensity = value
        self._fog_intensity._update_proto_references(self.proto.fog_intensity)

    @property
    def independent_wetness(self) -> bool:
        return self.proto.independent_wetness

    @independent_wetness.setter
    def independent_wetness(self, value: bool):
        self.proto.independent_wetness = value

    @property
    def rain_intensity(self) -> _pd_distributions_pb2.Distribution:
        return self._rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: _pd_distributions_pb2.Distribution):
        self.proto.rain_intensity.CopyFrom(value.proto)
        
        self._rain_intensity = value
        self._rain_intensity._update_proto_references(self.proto.rain_intensity)

    @property
    def time_of_day(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._time_of_day

    @time_of_day.setter
    def time_of_day(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.time_of_day.CopyFrom(value.proto)
        
        self._time_of_day = value
        self._time_of_day._update_proto_references(self.proto.time_of_day)

    @property
    def wetness(self) -> _pd_distributions_pb2.Distribution:
        return self._wetness

    @wetness.setter
    def wetness(self, value: _pd_distributions_pb2.Distribution):
        self.proto.wetness.CopyFrom(value.proto)
        
        self._wetness = value
        self._wetness._update_proto_references(self.proto.wetness)

    def _update_proto_references(self, proto: pd_environments_pb2.EnvironmentPreset):
        self.proto = proto
        self._cloud_coverage._update_proto_references(proto.cloud_coverage)
        self._fog_intensity._update_proto_references(proto.fog_intensity)
        self._rain_intensity._update_proto_references(proto.rain_intensity)
        self._time_of_day._update_proto_references(proto.time_of_day)
        self._wetness._update_proto_references(proto.wetness)