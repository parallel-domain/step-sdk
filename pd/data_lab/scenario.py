# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from pathlib import Path
from typing import List, Optional, Union

import ujson
from google.protobuf.json_format import MessageToDict, ParseDict, ParseError

from pd.data_lab.config.distribution import Bucket, CategoricalDistribution
from pd.data_lab.config.environment import Environment, TimeOfDays
from pd.data_lab.config.location import Location
from pd.data_lab.config.build_sim_state import BuildSimState, GeneratorConfigPreset
from pd.data_lab.generators.custom_generator import CustomAtomicGenerator
from pd.data_lab.generators.custom_simulation_agent import CustomSimulationAgent
from pd.data_lab.generators.helper import decode_generator_preset, encode_atomic_generator
from pd.data_lab.generators.non_atomics import NonAtomicGeneratorMessage
from pd.internal.proto.keystone.generated.python import pd_environments_pb2, pd_sim_state_pb2
from pd.internal.proto.keystone.generated.wrapper import pd_sim_state_pb2

from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig
from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage, get_wrapper


class Scenario:
    def __init__(
        self, sim_state_message: Optional[pd_sim_state_pb2.BuildSimState] = None, sensor_rig: Optional[SensorRig] = None
    ):
        self._custom_generators = list()
        self._custom_agents = list()

        if sim_state_message is None:
            sim_state_message = BuildSimState.encode_sim_state(
                environment=Environment(),
                generators=[],
                location=Location(name="SF_6thAndMission_medium"),
                sensor_rig=sensor_rig if sensor_rig is not None else SensorRig(),
                number_of_frames=100,
                random_seed=42,
                merge_batches=False,
            )
        self._sim_state_message: pd_sim_state_pb2.BuildSimState = sim_state_message

        if sensor_rig is not None:
            self.sim_state.sensor_rig = sensor_rig

        if len(self._sim_state_message.scenario_gen.environment.presets) == 0:
            self._sim_state_message.scenario_gen.environment.presets.append(pd_environments_pb2.EnvironmentPreset())

        self._location = (
            None if len(self._sim_state_message.locations) == 0 else Location(name=self._sim_state_message.locations[0].location)
        )

    @property
    def sim_state(self) -> BuildSimState:
        state_type = get_wrapper(proto_type=BuildSimState._proto_message)
        return state_type(proto=self._sim_state_message)

    @property
    def random_seed(self) -> int:
        return self.sim_state.proto.scenario_gen.scenario_seed

    @random_seed.setter
    def random_seed(self, value: int):
        self.sim_state.proto.scenario_gen.scenario_seed = value

    @property
    def sensor_rig(self) -> SensorRig:
        rig_type = get_wrapper(proto_type=SensorRig._proto_message)
        return rig_type(proto=self._sim_state_message.sensor_rig)

    @property
    def environment(self) -> Environment:
        env_type = get_wrapper(proto_type=Environment._proto_message)
        return env_type(proto=self._sim_state_message.scenario_gen.environment.presets[0])

    @property
    def pd_generators(self) -> Union[List[AtomicGeneratorMessage], List[NonAtomicGeneratorMessage]]:
        location = self._sim_state_message.locations[0]
        if len(location.generator_config.presets) == 0:
            return list()
        gen = location.generator_config.presets[0]
        return decode_generator_preset(generator_preset=gen)

    @property
    def custom_generators(self) -> List[CustomAtomicGenerator]:
        return self._custom_generators

    @property
    def custom_agents(self) -> List[CustomSimulationAgent]:
        return self._custom_agents

    @property
    def location(self) -> Location:
        return self._location

    def set_location(self, location: Location):
        self._location = location
        self._sim_state_message.locations[0].location = location.name

    def add_objects(self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator]) -> "Scenario":
        if isinstance(generator, CustomAtomicGenerator):
            self._custom_generators.append(generator)
        else:
            self._add_atomic(generator)

        return self

    def _add_atomic(self, generator: AtomicGeneratorMessage):
        location = self._sim_state_message.locations[0]
        if len(location.generator_config.presets) == 0:
            dist_type = get_wrapper(proto_type=CategoricalDistribution._proto_message)
            preset_distribution = dist_type(proto=location.generator_config.preset_distribution)
            preset_distribution.set_category_weight(Bucket(), weight=1.0)
            location.generator_config.presets.append(GeneratorConfigPreset().proto)
        unified_generator = location.generator_config.presets[0].unified_generator
        unified_generator.atomics.append(encode_atomic_generator(generator))

    def add_agents(
        self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator, CustomSimulationAgent]
    ) -> "Scenario":
        if isinstance(generator, CustomSimulationAgent):
            self._custom_agents.append(generator)
        elif isinstance(generator, CustomAtomicGenerator):
            self._custom_generators.append(generator)
        else:
            self._add_atomic(generator)
        return self

    def add_ego(
        self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator, CustomSimulationAgent]
    ) -> "Scenario":
        if isinstance(generator, CustomSimulationAgent):
            self._custom_agents.append(generator)
        elif isinstance(generator, CustomAtomicGenerator):
            self._custom_generators.append(generator)
        else:
            self._add_atomic(generator)
        return self

    def save_scenario(self, path: Union[str, Path]):
        path = Path(path) if isinstance(path, str) else path

        sim_state_str = self.to_scenario_generation_json()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as fp:
            fp.write(sim_state_str)

    def to_scenario_generation_json(self) -> str:
        return ujson.dumps(
            MessageToDict(
                message=self.sim_state.proto,
                including_default_value_fields=False,
                preserving_proto_field_name=True,
                use_integers_for_enums=False,
                descriptor_pool=None,
                float_precision=None,
            ),
            indent=2,
            escape_forward_slashes=False,
        )

    @classmethod
    def load_scenario(cls, path: Union[str, Path], sensor_rig: SensorRig = None) -> "Scenario":
        path = Path(path) if isinstance(path, str) else path
        try:
            with path.open("r") as fp:
                json_data = ujson.load(fp)

            message = ParseDict(
                js_dict=json_data,
                message=pd_sim_state_pb2.BuildSimState().proto,
                ignore_unknown_fields=False,
                descriptor_pool=None,
            )
        except ParseError:
            with path.open("r") as fp:
                message_json = ujson.load(fp)
            message = next(stage["build_sim_state"] for stage in message_json["stages"] if "build_sim_state" in stage)

            message = ParseDict(
                js_dict=message,
                message=pd_sim_state_pb2.BuildSimState().proto,
                ignore_unknown_fields=False,
                descriptor_pool=None,
            )

        if sensor_rig is not None:
            message.sensor_rig.MergeFrom(sensor_rig.proto)

        return Scenario(sim_state_message=message, sensor_rig=sensor_rig)

    def clone(self) -> "Scenario":
        sim_state_message_clone = self.sim_state.clone_message()
        cloned = Scenario(sim_state_message=sim_state_message_clone)
        if (
            self.location is not None
        ):  # When loading from existing scenario gen config, location is not set on scenario object
            cloned.set_location(self.location)
        for g in self.custom_generators:
            cloned.add_objects(g.clone())
        for g in self.custom_agents:
            cloned.add_agents(g.clone())
        return cloned

    def sample_discrete_scenario(
        self,
        scene_index: int,
        dataset_name: Optional[str] = None,
        end_skip_frames: Optional[int] = None,
        num_frames: int = -1,
        sim_capture_rate: Optional[int] = None,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = None,
        merge_batches: Optional[bool] = None,
    ) -> "Scenario":
        random_seed = self.random_seed + scene_index
        cloned = self.clone()
        cloned.random_seed = random_seed

        if len(self.environment.time_of_day.buckets) == 0:
            sampled_tod = TimeOfDays.Day
        else:
            sampled_tod = self.environment.time_of_day.sample(random_seed=random_seed)

        cloned.environment.time_of_day.set_category_weight(sampled_tod, 1.0)

        cloned.environment.clouds.set_constant_value(self.environment.clouds.sample(random_seed=random_seed))
        cloned.environment.rain.set_constant_value(self.environment.rain.sample(random_seed=random_seed))
        cloned.environment.fog.set_constant_value(self.environment.fog.sample(random_seed=random_seed))
        cloned.environment.wetness.set_constant_value(self.environment.wetness.sample(random_seed=random_seed))

        if sim_settle_frames is not None:
            cloned.sim_state.scenario_gen.sim_settle_frames = sim_settle_frames
        if num_frames is not None:
            cloned.sim_state.scenario_gen.num_frames = num_frames
        if sim_capture_rate is not None:
            cloned.sim_state.scenario_gen.sim_capture_rate = sim_capture_rate
        if start_skip_frames is not None:
            cloned.sim_state.scenario_gen.start_skip_frames = start_skip_frames
        if end_skip_frames is not None:
            cloned.sim_state.scenario_gen.end_skip_frames = end_skip_frames
        if merge_batches is not None:
            cloned.sim_state.scenario_gen.merge_batches = merge_batches
        if dataset_name is not None:
            cloned.sim_state.name = dataset_name

        return cloned
