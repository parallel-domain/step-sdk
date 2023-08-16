# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import abc
import json
from pathlib import Path
from typing import List, Optional, Union

from google.protobuf.json_format import MessageToDict, ParseDict, ParseError

from pd.core import PdError
from pd.data_lab.config.build_sim_state import BuildSimState, GeneratorConfigPreset
from pd.data_lab.config.distribution import Bucket, CategoricalDistribution
from pd.data_lab.config.environment import Environment, TimeOfDays
from pd.data_lab.config.location import Location, LatLonLocation
from pd.data_lab.generators.custom_generator import CustomAtomicGenerator, DefaultCustomAtomicGenerator
from pd.data_lab.generators.custom_simulation_agent import CustomSimulationAgent
from pd.data_lab.generators.helper import decode_generator_preset, encode_atomic_generator
from pd.data_lab.generators.non_atomics import NonAtomicGeneratorMessage
from pd.data_lab.state_callback import StateCallback
from pd.internal.proto.keystone.generated.python import pd_environments_pb2, pd_sim_state_pb2
from pd.internal.proto.keystone.generated.wrapper import pd_sim_state_pb2
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig
from pd.internal.proto.keystone.generated.wrapper.pd_unified_generator_pb2 import EnvironmentParameters
from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage, get_wrapper


class DiscreteScenario:
    def __init__(
        self,
        name: str,
        start_skip_frames: int,
        sim_capture_rate: int,
        state_callbacks: Optional[List[StateCallback]] = None,
    ):
        self.name = name
        self.start_skip_frames = start_skip_frames
        self.sim_capture_rate = sim_capture_rate
        self.state_callbacks = state_callbacks if state_callbacks is not None else list()


class ScenarioSource(abc.ABC):
    """
    Base class to abstract from getting a discrete scenario from stored sim states
    or by sampling from a scenario distribution
    """

    def __init__(self):
        self.state_callbacks = list()

    @abc.abstractmethod
    def get_discrete_scenario(
        self,
        scenario_index: int,
        dataset_name: Optional[str] = None,
        end_skip_frames: Optional[int] = None,
        num_frames: int = -1,
        sim_capture_rate: Optional[int] = None,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = None,
        merge_batches: Optional[bool] = None,
    ) -> "DiscreteScenario":
        pass

    def add_state_callback(self, state_callback: StateCallback):
        self.state_callbacks.append(state_callback)


class SimulatedScenarioCollection(ScenarioSource):
    """
    References a collection of stored discrete scenarios that have frame-wise state files
    that define position of all agents in the scene. Use this to re-render specific scenarios
    and tweak the states of agents e.g. change time of day, remove agents, change asset type.
    """

    def __init__(self, storage_folder: Path):
        super().__init__()
        self._storage_folder = storage_folder

    @property
    def _scene_folders(self) -> List[Path]:
        return [sf for sf in self._storage_folder.iterdir() if sf.is_dir()]

    @property
    def number_of_stored_scenes(self) -> int:
        return len(self._scene_folders)

    def get_discrete_scenario(
        self,
        scenario_index: int,
        dataset_name: Optional[str] = None,
        end_skip_frames: Optional[int] = None,
        num_frames: int = -1,
        sim_capture_rate: Optional[int] = 10,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = 5,
        merge_batches: Optional[bool] = None,
    ) -> "DiscreteScenario":
        scene_folder = self._scene_folders[scenario_index]
        return SimulatedScenario(
            folder=scene_folder,
            state_callbacks=[c.clone() for c in self.state_callbacks],
            start_skip_frames=start_skip_frames,
            sim_capture_rate=sim_capture_rate,
        )


class Scenario(ScenarioSource):
    def __init__(
        self, sim_state_message: Optional[pd_sim_state_pb2.BuildSimState] = None, sensor_rig: Optional[SensorRig] = None
    ):
        super().__init__()
        self._custom_generators = list()
        # self._custom_agents = list()
        self._default_custom_generator: Optional[CustomAtomicGenerator] = None

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
            None
            if len(self._sim_state_message.locations) == 0
            else Location(name=self._sim_state_message.locations[0].location)
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
    def location(self) -> Location:
        return self._location

    def set_location(self, location: Location):  # FIXME: workaround to allow usage of lat/lon via existing APIs
        def convert_lat_lon(lat, lon):
            return (lat / 180.0) + 0.5, (lon / 360.0) + 0.5

        if isinstance(location, LatLonLocation):
            self._location = Location(name="PD_Cesium")
            lat, lon = convert_lat_lon(location.latitude, location.longitude)

            self.environment.fog.set_constant_value(lat)  # latitude
            self.environment.wetness.set_constant_value(lon)  # longitude
        else:
            self._location = location
        self._sim_state_message.locations[0].location = location.name

    def add_objects(
        self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator, CustomSimulationAgent]
    ) -> "Scenario":
        # At the moment we don't really differentiate between 'agents' and 'objects', but we may in the future.
        # That's the reason for keeping this method.
        return self.add_agents(generator)

    def _add_atomic(self, generator: AtomicGeneratorMessage):
        location = self._sim_state_message.locations[0]
        if len(location.generator_config.presets) == 0:
            dist_type = get_wrapper(proto_type=CategoricalDistribution._proto_message)
            preset_distribution = dist_type(proto=location.generator_config.preset_distribution)
            preset_distribution.set_category_weight(Bucket(), weight=1.0)
            location.generator_config.presets.append(GeneratorConfigPreset().proto)
        unified_generator = location.generator_config.presets[0].unified_generator
        unified_generator.atomics.append(encode_atomic_generator(generator))

    def _set_environment(self, parameters: EnvironmentParameters):
        location = self._sim_state_message.locations[0]
        if len(location.generator_config.presets) == 0:
            dist_type = get_wrapper(proto_type=CategoricalDistribution._proto_message)
            preset_distribution = dist_type(proto=location.generator_config.preset_distribution)
            preset_distribution.set_category_weight(Bucket(), weight=1.0)
            location.generator_config.presets.append(GeneratorConfigPreset().proto)
        unified_generator = location.generator_config.presets[0].unified_generator
        unified_generator.environment_params.CopyFrom(parameters.proto)

    def add_agents(
        self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator, CustomSimulationAgent]
    ) -> "Scenario":
        if isinstance(generator, CustomSimulationAgent):
            if self._default_custom_generator is None:
                self._default_custom_generator = DefaultCustomAtomicGenerator()
                self._custom_generators.append(self._default_custom_generator)
            self._default_custom_generator.add_agent(agent=generator)

        elif isinstance(generator, CustomAtomicGenerator):
            self._custom_generators.append(generator)
        else:
            self._add_atomic(generator)
        return self

    def add_ego(
        self, generator: Union[AtomicGeneratorMessage, CustomAtomicGenerator, CustomSimulationAgent]
    ) -> "Scenario":
        if isinstance(generator, CustomSimulationAgent):
            if self._default_custom_generator is None:
                self._default_custom_generator = DefaultCustomAtomicGenerator()
                self._custom_generators.append(self._default_custom_generator)
            self._default_custom_generator.add_agent(agent=generator)
        elif isinstance(generator, CustomAtomicGenerator):
            self._custom_generators.append(generator)
        else:
            self._add_atomic(generator)
        return self

    def set_environment(self, parameters: EnvironmentParameters) -> "Scenario":
        self._set_environment(parameters=parameters)
        return self

    def save_scenario(self, path: Union[str, Path]):
        path = Path(path) if isinstance(path, str) else path

        sim_state_str = self.to_scenario_generation_json()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as fp:
            fp.write(sim_state_str)

    def to_scenario_generation_json(self) -> str:
        return json.dumps(
            MessageToDict(
                message=self.sim_state.proto,
                including_default_value_fields=False,
                preserving_proto_field_name=True,
                use_integers_for_enums=False,
                descriptor_pool=None,
                float_precision=None,
            ),
            indent=2,
        )

    @classmethod
    def load_scenario(cls, path: Union[str, Path], sensor_rig: SensorRig = None) -> "Scenario":
        path = Path(path) if isinstance(path, str) else path
        with path.open("r") as fp:
            message_json = json.load(fp)
        try:
            if "stages" in message_json:
                message = next(
                    stage["build_sim_state"] for stage in message_json["stages"] if "build_sim_state" in stage
                )

                message = ParseDict(
                    js_dict=message,
                    message=pd_sim_state_pb2.BuildSimState().proto,
                    ignore_unknown_fields=False,
                    descriptor_pool=None,
                )
            else:
                message = ParseDict(
                    js_dict=message_json,
                    message=pd_sim_state_pb2.BuildSimState().proto,
                    ignore_unknown_fields=False,
                    descriptor_pool=None,
                )
        except ParseError as e:
            raise PdError(f"Couldn't load scenario from file {path}.", "\n".join(e.args))

        if sensor_rig is not None:
            message.sensor_rig.MergeFrom(sensor_rig.proto)

        return Scenario(sim_state_message=message, sensor_rig=sensor_rig)

    @classmethod
    def create_clone(cls, other: "Scenario", **kwrags) -> "Scenario":
        sim_state_message_clone = other.sim_state.clone_message()
        cloned = cls(sim_state_message=sim_state_message_clone, **kwrags)
        if (
            other.location is not None
        ):  # When loading from existing scenario gen config, location is not set on scenario object
            cloned.set_location(other.location)
        for g in other.custom_generators:
            if g is other._default_custom_generator:
                cloned_default = g.clone()
                cloned._default_custom_generator = cloned_default
                cloned.add_objects(generator=cloned_default)
            else:
                cloned.add_objects(g.clone())
        for cb in other.state_callbacks:
            cloned.add_state_callback(state_callback=cb)
        return cloned

    def clone(self) -> "Scenario":
        return self.create_clone(other=self)

    def get_discrete_scenario(
        self,
        scenario_index: int,
        dataset_name: Optional[str] = None,
        end_skip_frames: Optional[int] = None,
        num_frames: int = -1,
        sim_capture_rate: Optional[int] = None,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = None,
        merge_batches: Optional[bool] = None,
    ) -> "DiscreteScenario":
        random_seed = self.random_seed + scenario_index

        name = f"scene_{str(scenario_index).zfill(6)}"

        cloned = self.clone()
        cloned.random_seed = random_seed
        cloned.scenario_index = scenario_index

        if len(self.environment.time_of_day.buckets) == 0:
            cloned.environment.time_of_day.set_category_weight(category=TimeOfDays.Day, weight=1.0)
        else:
            cloned.environment.time_of_day.proto.CopyFrom(self.environment.time_of_day.proto)

        cloned.environment.clouds.proto.CopyFrom(self.environment.clouds.proto)  # do not sample but output directly
        cloned.environment.rain.proto.CopyFrom(self.environment.rain.proto)
        cloned.environment.fog.proto.CopyFrom(self.environment.fog.proto)
        cloned.environment.wetness.proto.CopyFrom(self.environment.wetness.proto)

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

        return SampledScenario(
            name=name,
            sim_state=cloned.sim_state,
            state_callbacks=cloned.state_callbacks,
            custom_generators=cloned.custom_generators,
        )


class SampledScenario(DiscreteScenario):
    def __init__(
        self,
        name: str,
        sim_state: BuildSimState,
        custom_generators: List[CustomAtomicGenerator],
        state_callbacks: Optional[List[StateCallback]] = None,
    ):
        self.sim_state = sim_state
        self.custom_generators = custom_generators
        super().__init__(
            name=name,
            start_skip_frames=self.sim_state.scenario_gen.start_skip_frames,
            sim_capture_rate=self.sim_state.scenario_gen.sim_capture_rate,
            state_callbacks=state_callbacks,
        )

    @property
    def pd_generators(self) -> Union[List[AtomicGeneratorMessage], List[NonAtomicGeneratorMessage]]:
        location = self.sim_state.proto.locations[0]
        if len(location.generator_config.presets) == 0:
            return list()
        gen = location.generator_config.presets[0]
        return decode_generator_preset(generator_preset=gen)

    def to_scenario_generation_json(self) -> str:
        return json.dumps(
            MessageToDict(
                message=self.sim_state.proto,
                including_default_value_fields=False,
                preserving_proto_field_name=True,
                use_integers_for_enums=False,
                descriptor_pool=None,
                float_precision=None,
            ),
            indent=2,
        )

    @property
    def random_seed(self) -> int:
        return self.sim_state.proto.scenario_gen.scenario_seed

    @property
    def sensor_rig(self) -> SensorRig:
        return self.sim_state.sensor_rig

    @property
    def environment(self) -> Environment:
        env_type = get_wrapper(proto_type=Environment._proto_message)
        return env_type(proto=self.sim_state.proto.scenario_gen.environment.presets[0])

    @property
    def location(self) -> Location:
        return Location(name=self.sim_state.locations[0].location)


class SimulatedScenario(DiscreteScenario):
    def __init__(
        self,
        start_skip_frames: int,
        sim_capture_rate: int,
        folder: Optional[Path] = None,
        state_callbacks: Optional[List[StateCallback]] = None,
    ):
        super().__init__(
            name=folder.name,
            start_skip_frames=start_skip_frames,
            sim_capture_rate=sim_capture_rate,
            state_callbacks=state_callbacks,
        )
        self.folder = folder
