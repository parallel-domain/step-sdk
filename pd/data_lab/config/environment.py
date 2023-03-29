# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from typing import List

from pd.internal.proto.keystone.generated.python import pd_distributions_pb2 as pd_distributions_pb2_base
from pd.internal.proto.keystone.generated.python import pd_environments_pb2 as pd_environments_pb2_base
from pd.internal.proto.keystone.generated.wrapper import pd_environments_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import register_wrapper

from pd.data_lab.config.distribution import Bucket, CategoricalDistribution, Distribution


class TimeOfDays:
    Dawn = Bucket(string_value="DAWN")
    Dusk = Bucket(string_value="DUSK")
    Night = Bucket(string_value="NIGHT")
    Evening = Bucket(string_value="EVENING")
    Day = Bucket(string_value="DAY")


@register_wrapper(proto_type=pd_environments_pb2_base.EnvironmentPreset)
class Environment(pd_environments_pb2.EnvironmentPreset):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.clouds.is_set:
            self.clouds.set_constant_value(0.0)
        if not self.rain.is_set:
            self.rain.set_constant_value(0.0)
        if not self.wetness.is_set:
            self.wetness.set_constant_value(0.0)
        if not self.fog.is_set:
            self.fog.set_constant_value(0.0)

    @property
    def clouds(self) -> Distribution:
        if hasattr(self, "cloud_coverage"):
            return self.cloud_coverage
        raise RuntimeError()

    @property
    def rain(self) -> Distribution:
        if hasattr(self, "rain_intensity"):
            return self.rain_intensity
        raise RuntimeError()

    @property
    def fog(self) -> Distribution:
        if hasattr(self, "fog_intensity"):
            return self.fog_intensity
        raise RuntimeError()

    @property
    def time_of_day(self) -> CategoricalDistribution:
        if hasattr(self, "_time_of_day"):
            return self._time_of_day
        raise RuntimeError()

    @property
    def wetness(self) -> Distribution:
        if hasattr(self, "_wetness"):
            return self._wetness
        raise RuntimeError()

    def sample(self, random_seed: int) -> "Environment":
        clone: Environment = Environment()
        clone.time_of_day.set_category_weight(self.time_of_day.sample(random_seed=random_seed), 1.0)

        clone.wetness.set_constant_value(self.wetness.sample(random_seed=random_seed))
        clone.clouds.set_constant_value(self.clouds.sample(random_seed=random_seed))
        clone.rain.set_constant_value(self.rain.sample(random_seed=random_seed))
        clone.fog.set_constant_value(self.fog.sample(random_seed=random_seed))
        clone.wetness.set_constant_value(self.wetness.sample(random_seed=random_seed))

        return clone


@register_wrapper(proto_type=pd_environments_pb2_base.EnvironmentDefinition)
class EnvironmentDefinition(pd_environments_pb2.EnvironmentDefinition):
    @staticmethod
    def encode_environment_configs(configs: List[Environment]) -> pd_environments_pb2_base.EnvironmentDefinition:
        if len(configs) > 1:
            raise NotImplementedError("More than one environment config is not supported in encoding")

        environment_definition_proto = pd_environments_pb2_base.EnvironmentDefinition(
            preset_distribution=pd_distributions_pb2_base.CategoricalDistribution(
                buckets=[pd_distributions_pb2_base.Bucket(probability=1.0)]
            ),
            presets=[configs[0].proto],
        )

        return environment_definition_proto
