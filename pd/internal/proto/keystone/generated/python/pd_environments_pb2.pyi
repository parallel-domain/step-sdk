import pd_distributions_pb2 as _pd_distributions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnvironmentDefinition(_message.Message):
    __slots__ = ["preset_distribution", "presets"]
    PRESETS_FIELD_NUMBER: ClassVar[int]
    PRESET_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    preset_distribution: _pd_distributions_pb2.CategoricalDistribution
    presets: _containers.RepeatedCompositeFieldContainer[EnvironmentPreset]
    def __init__(self, preset_distribution: Optional[Union[_pd_distributions_pb2.CategoricalDistribution, Mapping]] = ..., presets: Optional[Iterable[Union[EnvironmentPreset, Mapping]]] = ...) -> None: ...

class EnvironmentPreset(_message.Message):
    __slots__ = ["cloud_coverage", "fog_intensity", "independent_wetness", "rain_intensity", "time_of_day", "wetness"]
    CLOUD_COVERAGE_FIELD_NUMBER: ClassVar[int]
    FOG_INTENSITY_FIELD_NUMBER: ClassVar[int]
    INDEPENDENT_WETNESS_FIELD_NUMBER: ClassVar[int]
    RAIN_INTENSITY_FIELD_NUMBER: ClassVar[int]
    TIME_OF_DAY_FIELD_NUMBER: ClassVar[int]
    WETNESS_FIELD_NUMBER: ClassVar[int]
    cloud_coverage: _pd_distributions_pb2.Distribution
    fog_intensity: _pd_distributions_pb2.Distribution
    independent_wetness: bool
    rain_intensity: _pd_distributions_pb2.Distribution
    time_of_day: _pd_distributions_pb2.CategoricalDistribution
    wetness: _pd_distributions_pb2.Distribution
    def __init__(self, time_of_day: Optional[Union[_pd_distributions_pb2.CategoricalDistribution, Mapping]] = ..., cloud_coverage: Optional[Union[_pd_distributions_pb2.Distribution, Mapping]] = ..., rain_intensity: Optional[Union[_pd_distributions_pb2.Distribution, Mapping]] = ..., fog_intensity: Optional[Union[_pd_distributions_pb2.Distribution, Mapping]] = ..., wetness: Optional[Union[_pd_distributions_pb2.Distribution, Mapping]] = ..., independent_wetness: bool = ...) -> None: ...
