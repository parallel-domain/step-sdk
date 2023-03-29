import os
from pathlib import Path
from typing import Generator, Optional, Tuple, TypeVar, Type

from pd.data_lab.constants import PD_CLIENT_ORG_ENV, PD_CLIENT_STEP_API_KEY_ENV
from pd.data_lab.scenario import Scenario
from pd.data_lab.scenario_generator import ScenarioGenerator
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_state import SimState
from pd.state import state_to_bytes
import pd.management


TSimState = TypeVar("TSimState", bound=SimState)


def setup_credentials():
    needed_envs = [PD_CLIENT_ORG_ENV, PD_CLIENT_STEP_API_KEY_ENV]

    if all([n in os.environ for n in needed_envs]):
        pd.management.api_key = os.environ[PD_CLIENT_STEP_API_KEY_ENV]
        pd.management.org = os.environ[PD_CLIENT_ORG_ENV]


setup_credentials()


def create_sensor_sim_stream(
    scenario: Scenario,
    scene_index: int,
    dataset_name: str = "Default Dataset Name",
    end_skip_frames: Optional[int] = None,
    estimated_startup_time: int = 180,
    frames_per_scene: Optional[int] = None,
    seconds_per_frame_estimate: int = 100,
    sim_capture_rate: Optional[int] = None,
    sim_settle_frames: Optional[int] = None,
    start_skip_frames: Optional[int] = None,
    merge_batches: Optional[bool] = None,
    sim_state_type: Type[TSimState] = SimState,
    **kwargs,
) -> Generator[Tuple[Optional[TemporalSessionReference], TSimState], None, None]:
    discrete_scenario = scenario.sample_discrete_scenario(
        dataset_name=dataset_name,
        end_skip_frames=end_skip_frames,
        num_frames=frames_per_scene,
        scene_index=scene_index,
        sim_capture_rate=sim_capture_rate,
        sim_settle_frames=sim_settle_frames,
        start_skip_frames=start_skip_frames,
        merge_batches=merge_batches,
    )

    frames_per_scene = discrete_scenario.sim_state.scenario_gen.num_frames
    if not kwargs.get("keep_instance_running", False):
        sensors_and_annotations = sum([len(s.annotations_types) + 1 for s in scenario.sensor_rig.sensors])
        kwargs["time_to_live"] = (
            estimated_startup_time + frames_per_scene * seconds_per_frame_estimate * sensors_and_annotations
        )

    with ScenarioGenerator(
        scenario=discrete_scenario,
        scene_index=scene_index,
        sim_state_type=sim_state_type,
        **kwargs,
    ) as scenario_generator:
        yield from scenario_generator


def _store_sim_state(state: SimState, output_folder: Path, scene_index: int):
    scene_name = f"scene_{str(scene_index).zfill(6)}"
    path = output_folder / scene_name / f"{state.current_frame_id}.pd"
    path.parent.mkdir(parents=True, exist_ok=True)
    state_bytes = state_to_bytes(state=state.current_state)
    with path.open("wb") as file:
        file.write(state_bytes)


def encode_sim_states(
    scenario: Scenario,
    output_folder: Path,
    number_of_scenes: int = 1,
    frames_per_scene: Optional[int] = None,
    yield_every_sim_state: bool = True,
    **kwargs,
):
    for scene_index in range(number_of_scenes):
        gen = create_sensor_sim_stream(
            scenario=scenario,
            scene_index=scene_index,
            frames_per_scene=frames_per_scene,
            yield_every_sim_state=yield_every_sim_state,
            **kwargs,
        )
        for temporal_sensor_session_reference, sim_state in gen:
            _store_sim_state(state=sim_state, output_folder=output_folder, scene_index=scene_index)
