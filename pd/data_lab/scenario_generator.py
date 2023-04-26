# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import logging
import random
from typing import List, Optional, Tuple, Type, TypeVar, Generic

from pd.data_lab.config.location import Location
from pd.data_lab.constants import TIME_OF_DAY_MAP
from pd.data_lab.generators.custom_generator import CustomAtomicGenerator, DefaultCustomAtomicGenerator
from pd.data_lab.render_instance import AbstractRenderInstance, ManagedRenderInstance
from pd.data_lab.scenario import Scenario
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_instance import AbstractSimulationInstance
from pd.data_lab.sim_state import SimState
from pd.internal.proto.keystone.generated.wrapper.utils import AtomicGeneratorMessage
from pd.internal.proto.umd.generated.wrapper import UMD_pb2

logger = logging.getLogger(__name__)

TSimState = TypeVar("TSimState", bound=SimState)


class ScenarioGenerator(Generic[TSimState]):
    def __init__(
        self,
        scenario: Scenario,
        scene_index: int,
        sim_instance: Optional[AbstractSimulationInstance] = None,
        render_instance: Optional[AbstractRenderInstance] = None,
        yield_every_sim_state: bool = False,
        verbose: bool = True,
        sim_state_type: Type[TSimState] = SimState,
        **kwargs,
    ):
        self.scenario = scenario
        self._verbose = verbose
        self._scene_index = scene_index

        if render_instance is None and "step_url" in kwargs:
            render_instance = ManagedRenderInstance(
                locations=[scenario.location],
                address=kwargs.pop("step_url", None),
                **kwargs,
            )
        elif isinstance(render_instance, ManagedRenderInstance):
            render_instance.locations = [scenario.location]

        self._render_instance = render_instance
        self._sim_instance = sim_instance
        self._sim_state_type = sim_state_type
        self._yield_every_sim_state = yield_every_sim_state
        self.sensor_rig = scenario.sensor_rig
        self._dataset_name = scenario.sim_state.name
        self._current_scene_name = None
        self._sim_state: Optional[TSimState] = None
        self._first_frame: bool = True
        self._map: Optional[UMD_pb2.UniversalMap] = None
        self._map_file: Optional[str] = kwargs["map_file"] if "map_file" in kwargs else None

    def __enter__(self):
        if self._render_instance is not None:
            self._render_instance.__enter__()
        if self._sim_instance is not None:
            self._sim_instance.__enter__()

        return self

    def __exit__(self, *args):
        if self._render_instance is not None:
            self._render_instance.__exit__()
        if self._sim_instance is not None:
            self._sim_instance.__exit__()

    def __iter__(self):
        self.setup_new_scene()
        frames_in_scene = 0
        max_frames = self.scenario.sim_state.scenario_gen.num_frames
        if self._yield_every_sim_state:
            max_frames *= self.scenario.sim_state.scenario_gen.sim_capture_rate
        while frames_in_scene < max_frames:
            temporal_sensor_session_reference, sim_state = self.next_frame()
            yield temporal_sensor_session_reference, sim_state
            frames_in_scene += 1

    def setup_new_scene(self) -> TSimState:
        logger.info(f"setting up scene with index {self._scene_index}")

        self._initialize_generators(
            scenario=self.scenario,
        )
        return self._sim_state

    def next_frame(self) -> Tuple[Optional[TemporalSessionReference], TSimState]:
        if not self._first_frame or not self._use_pd_sim:
            # on beginning we ran start_skip_frames in setup, so first frame is good to go.
            # unless its custom sim only. Then we use the regular capture rate
            sim_capture_rate = max(1, self.scenario.sim_state.scenario_gen.sim_capture_rate)
        else:
            self._first_frame = False
            sim_capture_rate = 1

        temporal_session_reference = None
        for _ in range(sim_capture_rate):
            self._update_pd_generators()
            self._update_custom_generators()

            if self._render_instance is not None:
                temporal_session_reference = self._render_instance.render_frame(
                    step_state=self._sim_state.current_state,
                    time_delta=self.scenario.sim_state.scenario_gen.sim_update_time,
                )
            if self._yield_every_sim_state:
                return temporal_session_reference, self._sim_state

        if not self._yield_every_sim_state:
            return temporal_session_reference, self._sim_state

    def _setup_pd_generators(self, scenario: Scenario, generators: List[AtomicGeneratorMessage]):
        self._use_pd_sim = len(generators) > 0
        if self._use_pd_sim:
            sim_state_str = scenario.to_scenario_generation_json()
            if self._verbose:
                logger.info("Created sim_state json string:")
                logger.info(sim_state_str)

            location, ego_id = self._sim_instance.load_scenario_generation(scenario_gen=sim_state_str)
            self._sim_state.set_ego_agent_id(ego_id=ego_id)
            self._sim_state.set_location(location=location, map_file=self._map_file)

            for _ in range(self.scenario.sim_state.scenario_gen.start_skip_frames):
                self._update_pd_generators()
                if self._render_instance is not None:
                    if not self._render_instance.location_is_set:
                        self._render_instance.load_environment(
                            location=Location(name=self._sim_state.current_state.world_info.location),
                            time_of_day=self._sim_state.current_state.world_info.time_of_day,
                        )
                        if self._render_instance.loaded_location is not None:
                            # if we have access to the laoded location of the renderer
                            # update the loaded map to make sure whe match the version
                            location = self._render_instance.loaded_location
                            self._sim_state.set_location(location=location, map_file=self._map_file)
                    self._render_instance.render_frame(
                        step_state=self._sim_state.current_state,
                        time_delta=self.scenario.sim_state.scenario_gen.sim_update_time,
                    )

    def _setup_custom_generators(self, scenario: Scenario, custom_generators: List[CustomAtomicGenerator]):
        if len(custom_generators) > 0:
            if not self._sim_state.is_initialized:
                tod_category = scenario.environment.time_of_day.sample(random_seed=scenario.random_seed)
                time_of_day = random.Random(scenario.random_seed).choice(TIME_OF_DAY_MAP[tod_category])
                location = scenario.location
                if self._render_instance is not None:
                    if not self._render_instance.location_is_set:
                        self._render_instance.load_environment(
                            location=scenario.location,
                            time_of_day=time_of_day,
                        )
                    if self._render_instance.loaded_location is not None:
                        location = self._render_instance.loaded_location
                self._sim_state.set_location(location=location, map_file=self._map_file)
                self._sim_state.set_time_of_day(time_of_day=time_of_day)
                self._sim_state.current_state.world_info.rain_intensity = scenario.environment.rain.sample(
                    random_seed=scenario.random_seed
                )
                self._sim_state.current_state.world_info.fog_intensity = scenario.environment.fog.sample(
                    random_seed=scenario.random_seed
                )
                self._sim_state.current_state.world_info.wetness = scenario.environment.wetness.sample(
                    random_seed=scenario.random_seed
                )

            for gen in custom_generators:
                gen.on_new_scene(state=self._sim_state, random_seed=scenario.random_seed)

            custom_generators.sort(key=lambda a: a.has_ego_agent, reverse=True)

            for gen in custom_generators:
                gen.set_initial_agent_positions(
                    state=self._sim_state,
                    random_seed=scenario.random_seed,
                    raycast=self._sim_instance.session.raycast if self._sim_instance is not None else None,
                )

    def _initialize_generators(self, scenario: Scenario):
        pd_generators = scenario.pd_generators
        custom_generators = scenario.custom_generators

        if len(scenario.custom_agents) > 0:
            custom_gen = DefaultCustomAtomicGenerator[TSimState]()
            for a in scenario.custom_agents:
                custom_gen.add_agent(agent=a)
            custom_generators.append(custom_gen)

        self._custom_generators = custom_generators

        self._sim_state = self._sim_state_type.from_blank_state(sensor_rig=scenario.sensor_rig)

        self._setup_pd_generators(scenario=scenario, generators=pd_generators)
        self._setup_custom_generators(
            scenario=scenario,
            custom_generators=custom_generators,
        )

    def _update_pd_generators(self):
        if self._use_pd_sim:
            sim_state = self._sim_instance.query_sim_state()
            self._sim_state.set_next_state_message(
                state=sim_state, time_delta=self.scenario.sim_state.scenario_gen.sim_update_time
            )

    def _update_custom_generators(self):
        if not self._use_pd_sim:
            self._sim_state.set_next_state_message_from_previous(
                time_delta=self.scenario.sim_state.scenario_gen.sim_update_time
            )
        for gen in self._custom_generators:
            gen.update_state(
                state=self._sim_state,
                raycast=self._sim_instance.session.raycast if self._sim_instance is not None else None,
            )
