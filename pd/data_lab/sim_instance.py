# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
import random
from abc import abstractmethod
from pathlib import Path
from typing import Optional, Tuple, Generator, Union, List

from pd.core import PdError
from pd.data_lab.config.build_sim_state import BuildSimState
from pd.data_lab.config.location import Location
from pd.data_lab.constants import TIME_OF_DAY_MAP
from pd.data_lab.context import get_datalab_context
from pd.data_lab.generators.custom_generator import CustomAtomicGenerator
from pd.data_lab.scenario import Scenario, DiscreteScenario, SimulatedScenario, SampledScenario
from pd.data_lab.sim_state import SimState
from pd.data_lab.state_callback import StateCallback
from pd.management import Ig
from pd.session import SimSession
from pd.state import State, bytes_to_state, ModelAgent, VehicleAgent

logger = logging.getLogger(__name__)


class SimulationStateProvider:
    @abc.abstractmethod
    def next_frame(self, sim_state: SimState) -> bool:
        pass

    @abc.abstractmethod
    def setup(self, discrete_scenario: DiscreteScenario, sim_state: SimState):
        pass

    @abc.abstractmethod
    def _init_sim_state(self, scenario: DiscreteScenario, sim_state: SimState):
        pass

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self):
        pass


class FromDiskSimulation(SimulationStateProvider):
    """
    Generates States from a SimulatedScenario that refers to a storage location of serialized States.
    This call will yield all states from a given SimulatedScenario.
    """

    def __init__(self, map_file: Optional[str] = None):
        self._map_file = map_file
        self._state_gen = None
        self._sim_time = 0.0
        self._state_callbacks: Optional[List[StateCallback]] = list()

    def next_frame(self, sim_state: SimState) -> bool:
        state: Union[bool, State] = next(self._state_gen, False)
        if state is False:
            return state
        else:
            time_delta = state.simulation_time_sec - self._sim_time
            self._sim_time = state.simulation_time_sec

            sim_state.set_next_state_message(state=state, time_delta=time_delta)

        for cb in self._state_callbacks:
            cb(sim_state)
        return True

    @staticmethod
    def state_generator(folder: Path) -> Generator[State, None, None]:
        if folder is not None:
            sorted_state_files = sorted([i for i in folder.iterdir() if i.suffix == ".pd"], key=lambda k: int(k.stem))
            for sim_state_file in sorted_state_files:
                with sim_state_file.open("rb") as file:
                    sim_state = bytes_to_state(file.read())
                    yield sim_state

    def setup(self, discrete_scenario: DiscreteScenario, sim_state: SimState):
        if not isinstance(discrete_scenario, SimulatedScenario):
            raise ValueError(
                "FromDiskSimulation need a SimulatedScenario objects to setup the Simulation!"
                f"{type(discrete_scenario)} is not supported! "
                "Maybe try using SimulationInstance for simulation."
            )
        folder = discrete_scenario.folder
        self._state_callbacks = discrete_scenario.state_callbacks
        if folder is not None:
            self._state_gen = self.state_generator(folder=folder)
            self._init_sim_state(scenario=discrete_scenario, sim_state=sim_state)
        else:
            raise ValueError("Scenario is not compatible with this sim provider")

    def _init_sim_state(self, scenario: SimulatedScenario, sim_state: SimState):
        # This auxiliary state is to retrieve ego_agent and location
        first_state = next(self.state_generator(folder=scenario.folder))
        ego_agent = next(
            iter(
                [a for a in first_state.agents if isinstance(a, (ModelAgent, VehicleAgent)) and len(a.sensors) > 0]
            )
        )
        sim_state.set_ego_agent_id(ego_id=ego_agent.id)
        sim_state.set_location(location=Location(name=first_state.world_info.location))
        # To be consistent with AbstractSimulationInstance we take the first step in the setup phase
        self.next_frame(sim_state=sim_state)

    def __enter__(self):
        self._state_gen = None
        self._sim_time = 0.0
        self._state_callbacks = list()

    def __exit__(self):
        self._state_gen = None
        self._sim_time = 0.0
        self._state_callbacks = list()


class AbstractSimulationInstance(SimulationStateProvider):
    """
    Base class for a simulation that creates states using a remote simulation instances
    and/or local custom simulation agents. Will be configured from a Scenario object that contians
    the configs for remote generators as well as references to custom simulation behaviours.
    """

    def __init__(self, verbose: bool = True, map_file: Optional[str] = None):
        self._verbose = verbose
        self._map_file = map_file
        self._simulated_frames = 0
        self._max_frames = None
        self._sim_config: Optional[BuildSimState] = None
        self._use_remote_simulation: Optional[bool] = None
        self._custom_generators: Optional[List[CustomAtomicGenerator]] = None
        self._state_callbacks: Optional[List[StateCallback]] = list()

    def __enter__(self):
        self._sim_config = None
        self._use_remote_simulation = None
        self._custom_generators = None
        self._state_callbacks = list()
        self._simulated_frames = 0
        self._max_frames = None

    def __exit__(self):
        self._sim_config = None
        self._use_remote_simulation = None
        self._custom_generators = None
        self._state_callbacks = list()
        self._simulated_frames = 0
        self._max_frames = None

    def setup(self, discrete_scenario: DiscreteScenario, sim_state: SimState):
        if not isinstance(discrete_scenario, SampledScenario):
            raise ValueError(
                "SimulationInstances needs a SampledScenario object to setup the Simulation!"
                f"{type(discrete_scenario)} is not supported! "
                "Maybe try using FromDiskSimulation for simulation."
            )
        self._sim_config = discrete_scenario.sim_state
        self._state_callbacks = discrete_scenario.state_callbacks

        self._simulated_frames = 0
        self._max_frames = (
                (discrete_scenario.sim_state.scenario_gen.num_frames - 1)
                * discrete_scenario.sim_state.scenario_gen.sim_capture_rate
                + discrete_scenario.sim_state.scenario_gen.start_skip_frames + 1
        )
        self._init_sim_state(scenario=discrete_scenario, sim_state=sim_state)

    def _setup_pd_generators(self, scenario: SampledScenario, sim_state: SimState):
        self._use_remote_simulation = len(scenario.pd_generators) > 0
        if self._use_remote_simulation:
            sim_state_str = scenario.to_scenario_generation_json()
            if self._verbose:
                logger.info("Created sim_state json string:")
                logger.info(sim_state_str)

            location, ego_id = self.load_scenario_generation(scenario_gen=sim_state_str)
            sim_state.set_ego_agent_id(ego_id=ego_id)
            sim_state.set_location(location=location)

    def _setup_custom_generators(self, scenario: SampledScenario, sim_state: SimState):
        self._custom_generators = scenario.custom_generators
        if len(self._custom_generators) > 0:
            if not sim_state.is_initialized:
                tod_category = scenario.environment.time_of_day.sample(random_seed=scenario.random_seed)
                time_of_day = random.Random(scenario.random_seed).choice(TIME_OF_DAY_MAP[tod_category])
                location = scenario.location

                sim_state.set_location(location=location)
                sim_state.set_time_of_day(time_of_day=time_of_day)
                sim_state.current_state.world_info.rain_intensity = scenario.environment.rain.sample(
                    random_seed=scenario.random_seed
                )
                sim_state.current_state.world_info.fog_intensity = scenario.environment.fog.sample(
                    random_seed=scenario.random_seed
                )
                sim_state.current_state.world_info.wetness = scenario.environment.wetness.sample(
                    random_seed=scenario.random_seed
                )

            for gen in self._custom_generators:
                gen.on_new_scene(state=sim_state, random_seed=scenario.random_seed)

            self._custom_generators.sort(key=lambda a: a.has_ego_agent, reverse=True)

            for gen in self._custom_generators:
                gen.set_initial_agent_positions(
                    state=sim_state,
                    random_seed=scenario.random_seed,
                    raycast=self.session.raycast,
                )

    def _update_pd_generators(self, sim_state: SimState):
        if self._use_remote_simulation:
            state = self.query_sim_state()
            sim_state.set_next_state_message(state=state, time_delta=self._sim_config.scenario_gen.sim_update_time)

    def _update_custom_generators(self, sim_state: SimState):
        if not self._use_remote_simulation:
            sim_state.set_next_state_message_from_previous(time_delta=self._sim_config.scenario_gen.sim_update_time)
        for gen in self._custom_generators:
            gen.update_state(state=sim_state, raycast=self.session.raycast)

    def _init_sim_state(self, scenario: SampledScenario, sim_state: SimState):
        # Need to make sure that first state is set in the sim state for custom generators to access ego pose.
        # sim state will be stored here and rendered in scenario generator loop.
        self._setup_pd_generators(scenario=scenario, sim_state=sim_state)
        self._update_pd_generators(sim_state=sim_state)
        self._setup_custom_generators(scenario=scenario, sim_state=sim_state)
        self._update_custom_generators(sim_state=sim_state)
        for cb in self._state_callbacks:
            cb(sim_state)
        self._simulated_frames += 1

    def next_frame(self, sim_state: SimState) -> bool:
        if self._max_frames is not None and self._simulated_frames >= self._max_frames:
            return False

        self._update_pd_generators(sim_state=sim_state)
        self._update_custom_generators(sim_state=sim_state)
        self._simulated_frames += 1
        for cb in self._state_callbacks:
            cb(sim_state)
        return True

    @property
    @abstractmethod
    def session(self) -> SimSession:
        ...

    def load_scenario_generation(self, scenario_gen: str) -> Tuple[Location, int]:
        loc_name, ego_id = self.session.load_scenario_generation(scenario_gen=scenario_gen)
        return Location(name=loc_name), ego_id

    def query_sim_state(self) -> State:
        # state_data = self.session.query_state_data()
        # sim_state = bytes_to_state(state_data)
        sim_state = self.session.query_state_data()
        return sim_state


class SimulationInstance(AbstractSimulationInstance):
    def __init__(
        self,
        name: Optional[str] = None,
        address: Optional[str] = None,
    ):
        """
        Create a simulation instance for an existing remote Sim server

        Args:
            name: Instance name. Required for cloud mode
            address: Instance address. Used in local mode
        """
        super().__init__()
        self._name = name
        self._address = address
        context = get_datalab_context()
        self._client_cert_file = context.client_cert_file
        self._temporal_session_reference = None

        self._session: Optional[SimSession] = None

        if name and address:
            raise PdError("Only one of 'name' or 'address' can be specified for SimulationInstance.")
        if not context.is_mode_local and not name:
            raise PdError("A 'name' is required in SimulationInstance when running in cloud mode.")

        if context.is_mode_local:
            # Local mode, use local address if none is provided
            self._address = self._address or "tcp://localhost:9002"
        else:
            # Cloud mode, resolve the address
            try:
                ig = next(ig for ig in Ig.list() if ig.name == name)
            except StopIteration:
                raise PdError(
                    f"Couldn't find a simulation instance with the name '{name}'. "
                    "Please verify that the name is correct."
                )
            if context.fail_on_version_mismatch:
                if ig.ig_version != context.version:
                    raise PdError(
                        f"There's a mismatch between the selected Data Lab version ({context.version}) "
                        f"and the version of the sim instance ({ig.ig_version}). "
                        "To disable this check, pass fail_on_version_mismatch=False to setup_datalab()."
                    )
            self._address = ig.sim_url
            if self._address is None:
                raise PdError("Render Instance doesn't have a simulation server.")

    @property
    def session(self) -> SimSession:
        return self._session

    def create_session(self):
        if self._session is None:
            self._session = SimSession(request_addr=self._address, client_cert_file=self._client_cert_file)
            self._session.transport.timeout_recv_ms = 600_000
            self._session.__enter__()
            logger.info("Started Sim Session.")
        return self._session

    def end_session(self):
        if self._session is not None:
            self._session.__exit__()
            self._session = None
            logger.info("Ended Sim Session!")

    def __enter__(self) -> SimSession:
        super().__enter__()
        return self.create_session()

    def __exit__(self, *args):
        super().__exit__()
        self.end_session()


class ManagedSimulationInstance(SimulationInstance):
    pass


class CustomOnlySimulationInstance(AbstractSimulationInstance):
    @property
    def session(self) -> SimSession:
        raise RuntimeError("This instance does not support remote simulation")

    def _setup_pd_generators(self, scenario: Scenario, sim_state: SimState):
        pass

    def _update_pd_generators(self, sim_state: SimState):
        pass
