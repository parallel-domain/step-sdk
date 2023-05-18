# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from pathlib import Path
from typing import Generator, Optional, Tuple, TypeVar, Type

from pd.data_lab.scenario import Scenario, ScenarioSource, DiscreteScenario
from pd.data_lab.scenario_generator import ScenarioGenerator
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_state import SimState
from pd.state import state_to_bytes

TSimState = TypeVar("TSimState", bound=SimState)


def sim_stream_from_discrete_scenario(
    discrete_scenario: DiscreteScenario,
    sim_state_type: Type[TSimState] = SimState,
    **kwargs,
) -> Generator[Tuple[Optional[TemporalSessionReference], TSimState], None, None]:

    with ScenarioGenerator(
        discrete_scenario=discrete_scenario,
        sim_state_type=sim_state_type,
        **kwargs,
    ) as scenario_generator:
        yield from scenario_generator


def create_sensor_sim_stream(
    scenario: ScenarioSource,
    scenario_index: int,
    dataset_name: str = "Default Dataset Name",
    end_skip_frames: Optional[int] = None,
    frames_per_scene: Optional[int] = None,
    sim_capture_rate: Optional[int] = None,
    sim_settle_frames: Optional[int] = None,
    start_skip_frames: Optional[int] = None,
    merge_batches: Optional[bool] = None,
    sim_state_type: Type[TSimState] = SimState,
    **kwargs,
) -> Tuple[DiscreteScenario, Generator[Tuple[Optional[TemporalSessionReference], TSimState], None, None]]:
    discrete_scenario = scenario.get_discrete_scenario(
        dataset_name=dataset_name,
        end_skip_frames=end_skip_frames,
        num_frames=frames_per_scene,
        scenario_index=scenario_index,
        sim_capture_rate=sim_capture_rate,
        sim_settle_frames=sim_settle_frames,
        start_skip_frames=start_skip_frames,
        merge_batches=merge_batches,
    )

    return discrete_scenario, sim_stream_from_discrete_scenario(
        discrete_scenario=discrete_scenario, sim_state_type=sim_state_type, **kwargs
    )


def _store_sim_state(state: SimState, output_folder: Path, scene_name: str):
    path = output_folder / scene_name / f"{state.current_frame_id:0>10}.pd"
    path.parent.mkdir(parents=True, exist_ok=True)
    state_bytes = state_to_bytes(state=state.current_state)
    with path.open("wb") as file:
        file.write(state_bytes)


def encode_sim_states(
    scenario: ScenarioSource,
    output_folder: Path,
    number_of_scenes: int = 1,
    start_skip_frames: Optional[int] = 0,
    frames_per_scene: Optional[int] = None,
    yield_every_sim_state: bool = True,
    **kwargs,
):
    for scenario_index in range(number_of_scenes):
        discrete_scenario, gen = create_sensor_sim_stream(
            scenario=scenario,
            scenario_index=scenario_index,
            start_skip_frames=start_skip_frames,
            frames_per_scene=frames_per_scene,
            yield_every_sim_state=yield_every_sim_state,
            **kwargs,
        )

        for temporal_sensor_session_reference, sim_state in gen:
            _store_sim_state(state=sim_state, output_folder=output_folder, scene_name=discrete_scenario.name)
