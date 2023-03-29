# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import uuid
from typing import List, Optional

from pd.internal.proto.keystone.generated.python import pd_distributions_pb2 as pd_distributions_pb2_base
from pd.internal.proto.keystone.generated.python import pd_scenario_pb2 as pd_scenario_pb2_base
from pd.internal.proto.keystone.generated.python import pd_sim_state_pb2 as pd_sim_state_pb2_base
from pd.internal.proto.keystone.generated.python import pd_spawn_pb2 as pd_spawn_pb2_base
from pd.internal.proto.keystone.generated.python import pd_unified_generator_pb2 as pd_unified_generator_pb2_base
from pd.internal.proto.keystone.generated.wrapper import (
    pd_scenario_pb2,
    pd_sim_state_pb2,
    pd_spawn_pb2,
    pd_unified_generator_pb2,
)
from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage, register_wrapper

from pd.data_lab.config.environment import Environment, EnvironmentDefinition
from pd.data_lab.config.location import Location
from pd.data_lab.generators.helper import encode_atomic_generator
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig

AtomicGeneratorParameters = pd_unified_generator_pb2.AtomicGeneratorParameters
GeneratorConfigPreset = pd_spawn_pb2.GeneratorConfigPreset


@register_wrapper(proto_type=pd_unified_generator_pb2_base.UnifiedGeneratorParameters)
class UnifiedGeneratorParameters(pd_unified_generator_pb2.UnifiedGeneratorParameters):
    @staticmethod
    def encode_unified_generator(
        config: List[AtomicGeneratorMessage],
    ) -> pd_unified_generator_pb2_base.UnifiedGeneratorParameters:
        unified_generator_proto = pd_unified_generator_pb2_base.UnifiedGeneratorParameters(
            atomics=[encode_atomic_generator(config=s) for s in config]
        )

        return unified_generator_proto


@register_wrapper(proto_type=pd_spawn_pb2_base.GeneratorConfig)
class GeneratorConfig(pd_spawn_pb2.GeneratorConfig):
    @staticmethod
    def encode_generator_config(config: List[AtomicGeneratorMessage]) -> pd_spawn_pb2_base.GeneratorConfig:
        return pd_spawn_pb2_base.GeneratorConfig(
            preset_distribution=pd_distributions_pb2_base.CategoricalDistribution(
                buckets=[pd_distributions_pb2_base.Bucket(probability=1.0)]
            ),
            presets=[
                pd_spawn_pb2_base.GeneratorConfigPreset(
                    unified_generator=UnifiedGeneratorParameters.encode_unified_generator(config=config)
                )
            ],
        )


@register_wrapper(proto_type=pd_scenario_pb2_base.ScenarioLocation)
class ScenarioLocation(pd_scenario_pb2.ScenarioLocation):
    @staticmethod
    def encode_location(
        location: Location, steps: List[AtomicGeneratorMessage]
    ) -> pd_scenario_pb2_base.ScenarioLocation:
        scenario_location_proto = pd_scenario_pb2_base.ScenarioLocation(
            location=location.name,
            location_guid="latest",
            num_scenarios=1,
            num_retries=0,
            generator_config=GeneratorConfig.encode_generator_config(config=steps) if len(steps) > 0 else None,
        )

        return scenario_location_proto


@register_wrapper(proto_type=pd_scenario_pb2_base.ScenarioGenConfig)
class ScenarioGenConfig(
    pd_scenario_pb2.ScenarioGenConfig,
):
    @staticmethod
    def encode_scenario_generator_config(
        environment: Environment, number_of_frames: int, random_seed: int, merge_batches: bool = False
    ) -> pd_scenario_pb2_base.ScenarioGenConfig:
        scenario_gen_proto = pd_scenario_pb2_base.ScenarioGenConfig(
            num_frames=number_of_frames,
            sim_settle_frames=100,
            start_skip_frames=5,
            end_skip_frames=5,
            sim_capture_rate=10,
            scenario_seed=random_seed,
            output_offset=0,
            merge_batches=merge_batches,
            batch_size=1,
            sim_update_time=0.01,
            environment=EnvironmentDefinition.encode_environment_configs(configs=[environment]),
            spawn_config=SpawnConfig.default_spawn_config(),  # TODO TBD just return default spawn config for the moment
            sim_terminate_on_collision_within_radius_m=0.0,
            sim_terminate_on_pedestrian_collision_within_radius_m=0.0,
            check_offroad_vehicles=False,
        )

        return scenario_gen_proto

    @property
    def frame_rate(self) -> float:
        return self.sim_capture_rate / self.sim_update_time


@register_wrapper(proto_type=pd_spawn_pb2_base.SpawnConfig)
class SpawnConfig(pd_spawn_pb2.SpawnConfig):
    @staticmethod
    def default_spawn_config() -> pd_spawn_pb2_base.SpawnConfig:
        return pd_spawn_pb2_base.SpawnConfig(
            preset_distribution=pd_distributions_pb2_base.CategoricalDistribution(
                buckets=[pd_distributions_pb2_base.Bucket(probability=1.0)]
            ),
            presets=[pd_spawn_pb2_base.SpawnConfigPreset()],
        )


@register_wrapper(proto_type=pd_sim_state_pb2_base.BuildSimState)
class BuildSimState(pd_sim_state_pb2.BuildSimState):
    @staticmethod
    def encode_sim_state(
        environment: Environment,
        generators: List[AtomicGeneratorMessage],
        sensor_rig: SensorRig,
        location: Location,
        number_of_frames: int,
        random_seed: int,
        merge_batches: bool,
        name: str = "test",
        code_build_artifact_uid: str = "latest",
        output_artifact_uid: Optional[str] = None,
    ) -> pd_sim_state_pb2_base.BuildSimState:
        sim_state_proto = pd_sim_state_pb2_base.BuildSimState(
            name=name,
            output_artifact_uid=str(uuid.uuid4()) if output_artifact_uid is None else output_artifact_uid,
            code_build_artifact_uid=code_build_artifact_uid,
            locations=[ScenarioLocation.encode_location(location=location, steps=generators)],
            scenario_gen=ScenarioGenConfig.encode_scenario_generator_config(
                environment=environment,
                number_of_frames=number_of_frames,
                random_seed=random_seed,
                merge_batches=merge_batches,
            ),
            sensor_rig=sensor_rig.proto,
        )

        return sim_state_proto

    @property
    def scenario_gen(self) -> ScenarioGenConfig:
        return self._scenario_gen
