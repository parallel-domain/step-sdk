# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
from typing import Generator, List, Optional, Tuple, Type, Union

from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.data_lab.context import validate_instance_address
from pd.data_lab.generators.custom_generator import CustomAtomicGenerator
from pd.data_lab.scenario import DiscreteScenario, Lighting, SampledScenario, SimulatedScenario
from pd.data_lab.sim_state import SimState
from pd.data_lab.state_callback import StateCallback, TSimState
from pd.internal.assets.asset_registry import DataLightingSublevels
from pd.session import SimSession
from pd.state import ModelAgent, State, VehicleAgent

logger = logging.getLogger(__name__)


class SimulationStateProvider:
    def __init__(self):
        self._sim_state: Optional[SimState] = None
        self._location = None
        self._lighting = None
        self._street_lights: bool = False
        self._headlights: bool = False
        self.start_skip_frames = None
        self.sim_capture_rate = None

    @abc.abstractmethod
    def next_frame(self) -> bool:
        pass

    def configure(self, discrete_scenario: DiscreteScenario):
        self.start_skip_frames = discrete_scenario.start_skip_frames
        self.sim_capture_rate = discrete_scenario.sim_capture_rate

    def setup(self, unique_scene_name: str, location: Location, lighting: Lighting, sim_state_type: Type[TSimState]):
        self._sim_state = sim_state_type.from_blank_state()
        self._location = location

        lighting_levels = DataLightingSublevels.select().where(DataLightingSublevels.name == lighting)
        if len(lighting_levels) == 0:
            raise PdError(
                f"Lighting level {lighting} not found in database. Please check your spelling and make sure it exists"
                " in `DataLightingSublevels` table."
            )
        self._lighting = lighting
        self._street_lights = bool(lighting_levels[0].street_lights)
        self._headlights = bool(lighting_levels[0].street_lights)
        self.start_skip_frames = None
        self.sim_capture_rate = None

    def cleanup(self):
        self._sim_state = None
        self.start_skip_frames = None
        self.sim_capture_rate = None
        self._lighting = None
        self._street_lights = False
        self._headlights = False

    def _sim_state_generator(self) -> Generator[SimState, None, None]:
        first_frame = True
        while True:
            if first_frame:
                # on beginning we need to run start_skip_frames plus one frame we want to capture
                sim_capture_rate = self.start_skip_frames + 1
            else:
                sim_capture_rate = max(1, self.sim_capture_rate)

            for i in range(sim_capture_rate):
                # we already have the first state from sim instance setup, but have not rendered it yet
                if first_frame:
                    has_state = True
                    first_frame = False
                else:
                    # this updates the current simulation state in our sim state
                    has_state = self.next_frame()

                if has_state is False:
                    # if the sim instance has no more state we signal the end of the scene by returning None
                    # this is the case when loading states from disk or if we have defined a max number of frames
                    # in the simulation config
                    return

                # Flags to the renderer if we want to access this frame
                # e.g. preview the image or save to disk
                # Since we only capture the last frame of #sim_capture_rate we check for the last index
                capture = i == sim_capture_rate - 1
                self._sim_state.current_state.capture = capture
                yield self._sim_state

    def sim_state_generator(self, state_callbacks: List[StateCallback]) -> Generator[SimState, None, None]:
        for state in self._sim_state_generator():
            for cb in state_callbacks:
                cb(state)
            yield state

    def amend_sim_state(self):
        """
        Amends stored sim state to bring it in alignment with the provider

        Reason: Scenario gen API is not able to explicitly request certain parameters in sim state.
                In batch pipeline we are able to set these out-of-band, but for Data Lab they need to be
                in the state.
        """
        self._sim_state.current_state.world_info.time_of_day = self._lighting
        self._sim_state.current_state.world_info.street_lights = float(self._street_lights)
        self._sim_state.current_state.world_info.enable_headlights = self._headlights


class FromDiskSimulation(SimulationStateProvider):
    """
    Generates States from a SimulatedScenario that refers to a storage location of serialized States.
    This call will yield all states from a given SimulatedScenario.
    """

    def __init__(self, map_file: Optional[str] = None):
        super().__init__()
        self._map_file = map_file
        self._state_gen = None
        self._sim_time = 0.0

    def next_frame(self) -> bool:
        state: Union[bool, State] = next(self._state_gen, False)

        if state is False:
            return state
        else:
            time_delta = state.simulation_time_sec - self._sim_time
            self._sim_time = state.simulation_time_sec

            self._sim_state.set_next_state_message(state=state, time_delta=time_delta)
        return True

    def setup(self, unique_scene_name: str, location: Location, lighting: Lighting, sim_state_type: Type[TSimState]):
        super().setup(
            unique_scene_name=unique_scene_name,
            location=location,
            lighting=lighting,
            sim_state_type=sim_state_type,
        )
        self._state_gen = None
        self._sim_time = 0.0
        self._sim_state = sim_state_type.from_blank_state()

    def configure(self, discrete_scenario: DiscreteScenario):
        super().configure(discrete_scenario=discrete_scenario)
        if not isinstance(discrete_scenario, SimulatedScenario):
            raise ValueError(
                "FromDiskSimulation need a SimulatedScenario objects to setup the Simulation!"
                f"{type(discrete_scenario)} is not supported! "
                "Maybe try using SimulationInstance for simulation."
            )
        folder = discrete_scenario.folder
        if folder is not None:
            self._state_gen = discrete_scenario.state_generator()

            # This auxiliary state is to retrieve ego_agent and location
            first_state = discrete_scenario.first_state
            ego_agent = next(
                iter(
                    [a for a in first_state.agents if isinstance(a, (ModelAgent, VehicleAgent)) and len(a.sensors) > 0]
                )
            )
            self._sim_state.set_ego_agent_id(ego_id=ego_agent.id)
            self._sim_state.set_location(location=Location(name=first_state.world_info.location))
            # To be consistent with SimulationInstance we take the first step in the setup phase
            self.next_frame()

        else:
            raise ValueError("Scenario is not compatible with this sim provider")

    def cleanup(self):
        super().cleanup()
        self._state_gen = None
        self._sim_time = 0.0


class SimulationInstance(SimulationStateProvider):
    def __init__(
        self,
        name: Optional[str] = None,
        address: Optional[str] = None,
        map_file: Optional[str] = None,
    ):
        """
        Create a simulation instance for an existing remote Sim server

        Args:
            name: Instance name. Required for cloud mode
            address: Instance address. Used in local mode
        """
        super().__init__()
        self._map_file = map_file
        self._simulated_frames = 0
        self._sim_update_time = None
        self._max_frames = None
        self._custom_generators: Optional[List[CustomAtomicGenerator]] = None
        self.name = name
        self.address = address
        self._client_cert_file = None
        self._session: Optional[SimSession] = None

    @property
    def session(self) -> SimSession:
        return self._session

    def create_session(self):
        if self._session is None:
            logger.debug("Requesting sim session")
            self._session = SimSession(request_addr=self.address, client_cert_file=self._client_cert_file)
            self._session.transport.timeout_recv_ms = 600_000
            self._session.__enter__()
            logger.info("Created sim session")
        return self._session

    def end_session(self):
        if self._session is not None:
            self._session.__exit__()
            self._session = None
            logger.info("Ended sim session!")

    def setup(self, unique_scene_name: str, location: Location, lighting: Lighting, sim_state_type: Type[TSimState]):
        self.address, self.name, self._client_cert_file = validate_instance_address(
            instance_type="sim", address=self.address, name=self.name
        )

        super().setup(
            unique_scene_name=unique_scene_name,
            location=location,
            lighting=lighting,
            sim_state_type=sim_state_type,
        )
        self._custom_generators = None
        self._simulated_frames = 0
        self._max_frames = None
        self._sim_update_time = None
        self.create_session()

        logger.debug("Start sim load location")
        self.session.load_location(location.name, unique_scene_name)
        logger.debug("Sim loaded location")
        self._sim_state.set_location(location=location)

    def configure(self, discrete_scenario: DiscreteScenario):
        super().configure(discrete_scenario=discrete_scenario)
        if not isinstance(discrete_scenario, SampledScenario):
            raise ValueError(
                "SimulationInstances needs a SampledScenario object to setup the Simulation!"
                f"{type(discrete_scenario)} is not supported! "
                "Maybe try using FromDiskSimulation for simulation."
            )
        self._sim_update_time = discrete_scenario.sim_state.scenario_gen.sim_update_time

        self._max_frames = (
            (discrete_scenario.sim_state.scenario_gen.num_frames - 1)
            * discrete_scenario.sim_state.scenario_gen.sim_capture_rate
            + discrete_scenario.sim_state.scenario_gen.start_skip_frames
            + 1
        )

        # Need to make sure that first state is set in the sim state for custom generators to access ego pose.
        # sim state will be stored here and rendered in scenario generator loop.
        self._setup_pd_generators(scenario=discrete_scenario)
        self._update_pd_generators()
        self._setup_custom_generators(scenario=discrete_scenario)
        self.amend_sim_state()

    def cleanup(self):
        super().cleanup()
        self._custom_generators = None
        self._simulated_frames = 0
        self._sim_update_time = None
        self._max_frames = None
        self.end_session()

    def _setup_pd_generators(self, scenario: SampledScenario):
        if len(scenario.pd_generators) > 0:
            sim_state_str = scenario.to_scenario_generation_json()
            location, ego_id = self.load_scenario_generation(scenario_gen=sim_state_str)
            logger.info("Server loaded scenario")
            self._sim_state.set_ego_agent_id(ego_id=ego_id)
        else:
            logger.debug("Skip loading scenario because there are no atomic generators")

    def _setup_custom_generators(self, scenario: SampledScenario):
        self._custom_generators = scenario.custom_generators
        if len(self._custom_generators) > 0:
            for i, gen in enumerate(self._custom_generators):
                logger.info(f"Creating custom generator {i}")
                gen.on_new_scene(state=self._sim_state, random_seed=scenario.random_seed)

            self._custom_generators.sort(key=lambda a: a.has_ego_agent, reverse=True)

            for i, gen in enumerate(self._custom_generators):
                logger.info(f"Setting initial agent positions for custom generator {i}")
                gen.set_initial_agent_positions(
                    state=self._sim_state,
                    random_seed=scenario.random_seed,
                    raycast=self.session.raycast,
                )

    def _update_pd_generators(self):
        state = self.query_sim_state()

        self._sim_state.set_next_state_message(state=state, time_delta=self._sim_update_time)

    def _update_custom_generators(self):
        for gen in self._custom_generators:
            gen.update_state(state=self._sim_state, raycast=self.session.raycast)

    def next_frame(self) -> bool:
        if self._max_frames is not None and self._simulated_frames >= self._max_frames:
            return False

        self._update_pd_generators()
        self._update_custom_generators()

        self.amend_sim_state()

        self._simulated_frames += 1

        return True

    def load_scenario_generation(self, scenario_gen: str) -> Tuple[Location, int]:
        logger.info("Loading scenario generation")
        logger.debug(scenario_gen)
        loc_name, ego_id = self.session.load_scenario_generation(scenario_gen=scenario_gen)
        return Location(name=loc_name), ego_id

    def query_sim_state(self) -> State:
        sim_state = self.session.query_state_data()
        return sim_state


class CustomOnlySimulator(SimulationStateProvider):
    def __init__(
        self,
    ):
        """
        Sim Instance for local only simulation.
        """
        super().__init__()
        self._simulated_frames = 0
        self._sim_update_time = None
        self._max_frames = None
        self._custom_generators: Optional[List[CustomAtomicGenerator]] = None
        self._client_cert_file = None
        self._session: Optional[SimSession] = None

    def setup(self, unique_scene_name: str, location: Location, lighting: Lighting, sim_state_type: Type[TSimState]):
        super().setup(
            unique_scene_name=unique_scene_name,
            location=location,
            lighting=lighting,
            sim_state_type=sim_state_type,
        )
        self._custom_generators = None
        self._simulated_frames = 0
        self._max_frames = None
        self._sim_update_time = None

    def configure(self, discrete_scenario: DiscreteScenario):
        super().configure(discrete_scenario=discrete_scenario)
        if not isinstance(discrete_scenario, SampledScenario):
            raise ValueError(
                "SimulationInstances needs a SampledScenario object to setup the Simulation!"
                f"{type(discrete_scenario)} is not supported! "
                "Maybe try using FromDiskSimulation for simulation."
            )
        self._sim_update_time = discrete_scenario.sim_state.scenario_gen.sim_update_time

        self._max_frames = (
            (discrete_scenario.sim_state.scenario_gen.num_frames - 1)
            * discrete_scenario.sim_state.scenario_gen.sim_capture_rate
            + discrete_scenario.sim_state.scenario_gen.start_skip_frames
            + 1
        )

        # Need to make sure that first state is set in the sim state for custom generators to access ego pose.
        # sim state will be stored here and rendered in scenario generator loop.
        self._setup_custom_generators(scenario=discrete_scenario)
        for _ in range(discrete_scenario.sim_state.scenario_gen.sim_settle_frames):
            self._update_custom_generators()

    def cleanup(self):
        super().cleanup()
        self._custom_generators = None
        self._simulated_frames = 0
        self._sim_update_time = None
        self._max_frames = None

    def _setup_custom_generators(self, scenario: SampledScenario):
        self._custom_generators = scenario.custom_generators
        if len(self._custom_generators) > 0:
            if not self._sim_state.is_initialized:
                self._sim_state.set_location(location=self._location)
                self._sim_state.current_state.world_info.rain_intensity = scenario.environment.rain.sample(
                    random_seed=scenario.random_seed
                )
                self._sim_state.current_state.world_info.fog_intensity = scenario.environment.fog.sample(
                    random_seed=scenario.random_seed
                )
                self._sim_state.current_state.world_info.wetness = scenario.environment.wetness.sample(
                    random_seed=scenario.random_seed
                )

            for gen in self._custom_generators:
                gen.on_new_scene(state=self._sim_state, random_seed=scenario.random_seed)

            self._custom_generators.sort(key=lambda a: a.has_ego_agent, reverse=True)

            for gen in self._custom_generators:
                gen.set_initial_agent_positions(
                    state=self._sim_state,
                    random_seed=scenario.random_seed,
                )

    def _update_custom_generators(self):
        self._sim_state.set_next_state_message_from_previous(time_delta=self._sim_update_time)
        for gen in self._custom_generators:
            gen.update_state(state=self._sim_state, raycast=None)

    def next_frame(self) -> bool:
        if self._max_frames is not None and self._simulated_frames >= self._max_frames:
            return False
        self._update_custom_generators()

        self.amend_sim_state()

        self._simulated_frames += 1

        return True
