# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import logging
from pathlib import Path
from typing import Generator, List, Literal, Optional, Type, TypeVar, Union

from pd.data_lab.context import setup_datalab
from pd.data_lab.data_lab_instance import DataLabInstance
from pd.data_lab.label_engine_instance import LabelEngineInstance
from pd.data_lab.labeled_state_reference import LabeledStateReference, StateReference
from pd.data_lab.render_instance import RenderInstance
from pd.data_lab.scenario import DiscreteScenario, Scenario, ScenarioCreator, ScenarioSource, scene_index_to_name
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_instance import SimulationStateProvider
from pd.data_lab.sim_state import SimState
from pd.state import state_to_bytes

logger = logging.getLogger(__name__)

TSimState = TypeVar("TSimState", bound=SimState)


def create_sensor_sim_stream(
    scenario_creator: ScenarioCreator,
    scene_index: int,
    number_of_scenes: int,
    random_seed: int,
    data_lab_version: str,
    simulator: Union[bool, SimulationStateProvider, str, None] = None,
    label_engine: Union[bool, LabelEngineInstance, str, None] = None,
    renderer: Union[bool, RenderInstance, str, None] = None,
    instance_name: Optional[str] = None,
    auto_start_instance: bool = False,
    shutdown_after_scene: Optional[bool] = None,
    sim_state_type: Type[TSimState] = SimState,
    fail_on_version_mismatch: bool = True,
    environment: Literal["prod", "stage", "dev"] = "prod",
    **kwargs,
) -> Generator[StateReference, None, None]:
    try:
        data_lab_instance = DataLabInstance.from_names(
            simulator=simulator,
            data_lab_version=data_lab_version,
            instance_name=instance_name,
            renderer=renderer,
            label_engine=label_engine,
            shutdown_on_cleanup=shutdown_after_scene,
            fail_on_version_mismatch=fail_on_version_mismatch,
            environment=environment,
        )
    except ValueError as e:
        if not auto_start_instance:
            raise e
        else:
            data_lab_instance = DataLabInstance.start(
                data_lab_version=data_lab_version,
                shutdown_on_cleanup=shutdown_after_scene,
                fail_on_version_mismatch=fail_on_version_mismatch,
                environment=environment,
                locations=[
                    scenario_creator.get_location(
                        random_seed=random_seed, scene_index=scene_index, number_of_scenes=number_of_scenes
                    )[0]
                ],
            )

    yield from data_lab_instance.create_sensor_sim_stream(
        scenario_creator=scenario_creator,
        scene_index=scene_index,
        number_of_scenes=number_of_scenes,
        random_seed=random_seed,
        sim_state_type=sim_state_type,
        **kwargs,
    )


def _store_sim_state(state_reference: StateReference, output_folder: Path, scene_name: str):
    path = output_folder / scene_name / f"{state_reference.frame_id:0>10}.pd"
    path.parent.mkdir(parents=True, exist_ok=True)
    state_bytes = state_to_bytes(state=state_reference.state)
    with path.open("wb") as file:
        file.write(state_bytes)


def encode_sim_states(
    scenario_creator: ScenarioCreator,
    output_folder: Path,
    instance_name: Optional[str] = None,
    simulator: Union[bool, SimulationStateProvider, str, None] = None,
    scene_indices: List[int] = None,
    start_skip_frames: Optional[int] = 0,
    frames_per_scene: Optional[int] = None,
    yield_every_sim_state: bool = True,
    **kwargs,
):
    if scene_indices is None:
        scene_indices = [0]
    if "number_of_scenes" in kwargs:
        logger.warning("Deprecated parameter number_of_scenes. Use scene_indices instead.")
        number_of_scenes = kwargs.pop("number_of_scenes")
        if number_of_scenes < 1:
            raise ValueError("A number of scenes > 0 has to be passed!")
        scene_indices = list(range(number_of_scenes))

    number_of_scenes = len(scene_indices)
    for scene_index in scene_indices:
        gen = create_sensor_sim_stream(
            scenario_creator=scenario_creator,
            scene_index=scene_index,
            instance_name=instance_name,
            simulator=simulator,
            number_of_scenes=number_of_scenes,
            renderer=False,
            label_engine=False,
            start_skip_frames=start_skip_frames,
            frames_per_scene=frames_per_scene,
            yield_every_sim_state=yield_every_sim_state,
            **kwargs,
        )

        for state_reference in gen:
            _store_sim_state(
                state_reference=state_reference,
                output_folder=output_folder,
                scene_name=scene_index_to_name(scene_index=scene_index),
            )
