# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import asyncio
import logging
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Any, Dict, Generator, List, Literal, Optional, Tuple, Type, TypeVar, Union

import pypeln
from requests import HTTPError

from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.data_lab.context import get_datalab_context, setup_datalab
from pd.data_lab.label_engine_instance import LabelEngineInstance
from pd.data_lab.labeled_state_reference import LabeledStateReference, StateReference
from pd.data_lab.render_instance import RenderInstance
from pd.data_lab.scenario import Lighting, Scenario, ScenarioCreator
from pd.data_lab.session_reference import StepSessionReference, TemporalSessionReference
from pd.data_lab.sim_instance import CustomOnlySimulator, SimulationInstance, SimulationStateProvider
from pd.data_lab.sim_state import SimState
from pd.data_lab.state_callback import StateCallback
from pd.management import Ig, IgQuality, IgStatus
from pd.session import generate_scene_name

logger = logging.getLogger(__name__)

TSimState = TypeVar("TSimState", bound=SimState)
TInstanceType = TypeVar("TInstanceType")


class DataLabInstance:
    def __init__(
        self,
        name: str,
        shutdown_on_cleanup: bool,
        simulator: SimulationStateProvider,
        renderer: Optional[RenderInstance],
        label_engine: Optional[LabelEngineInstance] = None,
    ):
        self.name = name
        self.shutdown_on_cleanup = shutdown_on_cleanup
        self.label_engine = label_engine
        self.renderer = renderer
        self.simulator = simulator

    def setup_renderer(self, unique_scene_name: str, location: Location, lighting: Lighting) -> bool:
        try:
            if self.renderer is not None:
                self.renderer.setup(unique_scene_name=unique_scene_name, location=location, lighting=lighting)
            return True
        except Exception as e:
            logger.exception(e)
            return False

    def setup_simulator(
        self,
        scenario_creator: ScenarioCreator,
        scene_index: int,
        number_of_scenes: int,
        random_seed: int,
        unique_scene_name: str,
        location: Location,
        lighting: Lighting,
        fail_on_sim_error: bool,
        sim_state_type: Type[TSimState],
        create_scenario_kwargs: Dict[str, Any],
    ) -> bool:
        self.simulator.setup(
            unique_scene_name=unique_scene_name,
            location=location,
            lighting=lighting,
            sim_state_type=sim_state_type,
        )

        # In the future this will happen after sim and rendering is setup incase
        # we need ray casting for scenario creation
        # replace with create_scenario call when we deprecate create_scenario_with_set_location
        scenario = scenario_creator.create_scenario_with_set_location(
            random_seed=random_seed,
            scene_index=scene_index,
            number_of_scenes=number_of_scenes,
            location=location,
            lighting=lighting,
        )

        # TODO: in beta discrete_scenario will be deprecated and just scenario is used
        discrete_scenario = scenario.get_discrete_scenario(**create_scenario_kwargs)

        try:
            self.simulator.configure(discrete_scenario=discrete_scenario)
            return True
        except PdError as e:
            logger.exception(e)
            if fail_on_sim_error is True:
                raise
            else:
                logger.warning(
                    f"Had an error during scene setup. Likely a sim fail. Skipping scene {discrete_scenario.name}"
                )
                return False

    def setup_label_engine(self, unique_scene_name: str) -> bool:
        if self.label_engine is not None:
            self.label_engine.setup(unique_scene_name=unique_scene_name)
        return True

    async def setup_instances(
        self,
        scenario_creator: ScenarioCreator,
        scene_index: int,
        number_of_scenes: int,
        random_seed: int,
        sim_state_type: Type[TSimState],
        fail_on_sim_error: bool,
        dataset_name: str,
        end_skip_frames: Optional[int] = None,
        frames_per_scene: Optional[int] = None,
        sim_capture_rate: Optional[int] = None,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = None,
        merge_batches: Optional[bool] = None,
    ) -> bool:
        create_scenario_kwargs = dict(
            dataset_name=dataset_name,
            end_skip_frames=end_skip_frames,
            num_frames=frames_per_scene,
            scene_index=scene_index,
            sim_capture_rate=sim_capture_rate,
            sim_settle_frames=sim_settle_frames,
            start_skip_frames=start_skip_frames,
            merge_batches=merge_batches,
        )

        unique_scene_name = generate_scene_name()
        location, lighting = scenario_creator.get_location(
            random_seed=random_seed, scene_index=scene_index, number_of_scenes=number_of_scenes
        )

        if not get_datalab_context().is_mode_local:
            # in case the instance was started automatically, we want to wait until its running
            await DataLabInstance.wait_until_instance_started(instance_name=self.name)
            # now that we are sure the instance is running, we initialize render, sim, le in parallel

        executor = ThreadPoolExecutor(max_workers=4)
        loop = asyncio.get_running_loop()
        done, _ = await asyncio.wait(
            fs={
                loop.run_in_executor(
                    executor,
                    self.setup_simulator,
                    scenario_creator,
                    scene_index,
                    number_of_scenes,
                    random_seed,
                    unique_scene_name,
                    location,
                    lighting,
                    fail_on_sim_error,
                    sim_state_type,
                    create_scenario_kwargs,
                ),
                loop.run_in_executor(executor, self.setup_renderer, unique_scene_name, location, lighting),
                loop.run_in_executor(executor, self.setup_label_engine, unique_scene_name),
            },
            return_when=asyncio.ALL_COMPLETED,
        )
        if not all([d.result() for d in done]):
            # something failed during setup
            return False
        return True

    def _state_reference_generator(self, state_callbacks: List[StateCallback]) -> Generator[StateReference, None, None]:
        for sim_state in self.simulator.sim_state_generator(state_callbacks=state_callbacks):
            if self.label_engine is None and self.renderer is None:
                yield StateReference(
                    state=sim_state.current_state,
                    frame_id=sim_state.current_frame_id,
                    ego_agent_id=sim_state.ego_agent_id,
                )
            elif self.label_engine is None:
                if sim_state.ego_agent is None or not sim_state.sensor_rig:
                    raise PdError("No ego agent with sensor rig provided. Cannot render without a sensor rig.")
                yield StepSessionReference(
                    state=sim_state.current_state,
                    frame_id=sim_state.current_frame_id,
                    sensor_rig=sim_state.sensor_rig,
                    ego_agent_id=sim_state.ego_agent_id,
                )
            else:
                if sim_state.ego_agent is None or not sim_state.sensor_rig:
                    raise PdError("No ego agent with sensor rig provided. Cannot render without a sensor rig.")
                yield LabeledStateReference(
                    label_engine=self.label_engine,
                    state=sim_state.current_state,
                    sensor_rig=sim_state.sensor_rig,
                    frame_id=sim_state.current_frame_id,
                    ego_agent_id=sim_state.ego_agent_id,
                )

    def _update_render_instance(
        self, item: Union[StateReference], yield_every_sim_state: bool
    ) -> Generator[StateReference, None, None]:
        if self.renderer is not None:
            self.renderer.update_state(sim_state=item.state)
            if isinstance(item, StepSessionReference):
                item = TemporalSessionReference(
                    session=self.renderer.session,
                    state=item.state,
                    frame_id=item.frame_id,
                    sensor_rig=item.sensor_rig,
                    ego_agent_id=item.ego_agent_id,
                )

        # We need to yield every sim state in step batch, to avoid aliasing effects from only outputting capture frames.
        # Here, not all frames have been necessarily been marked for capture.
        if yield_every_sim_state is True:
            yield item
        else:
            # Otherwise we only output capture frames, which is what we want to do in "Data Lab" mode.
            if item.state.capture is True:
                yield item

        if isinstance(item, TemporalSessionReference):
            item.on_session_state_changed()

    def create_sensor_sim_stream(
        self,
        scenario_creator: ScenarioCreator,
        scene_index: int,
        number_of_scenes: int,
        random_seed: int,
        sim_state_type: Type[TSimState],
        yield_every_sim_state: bool = False,
        fail_on_sim_error: bool = True,
        run_sim_and_renderer_asynchronously: bool = True,
        dataset_name: str = "Default Dataset Name",
        end_skip_frames: Optional[int] = None,
        frames_per_scene: Optional[int] = None,
        sim_capture_rate: Optional[int] = None,
        sim_settle_frames: Optional[int] = None,
        start_skip_frames: Optional[int] = None,
        merge_batches: Optional[bool] = None,
    ) -> Generator[StateReference, None, None]:
        successful = asyncio.run(
            self.setup_instances(
                scenario_creator=scenario_creator,
                random_seed=random_seed,
                scene_index=scene_index,
                number_of_scenes=number_of_scenes,
                sim_capture_rate=sim_capture_rate,
                dataset_name=dataset_name,
                end_skip_frames=end_skip_frames,
                sim_state_type=sim_state_type,
                sim_settle_frames=sim_settle_frames,
                fail_on_sim_error=fail_on_sim_error,
                merge_batches=merge_batches,
                start_skip_frames=start_skip_frames,
                frames_per_scene=frames_per_scene,
            )
        )

        if successful is False:
            return

        if run_sim_and_renderer_asynchronously:
            run_env = pypeln.thread
            render_env = run_env
        else:
            run_env = pypeln.sync
            render_env = run_env
        if self.label_engine is None:
            render_env = pypeln.sync

        pipeline = run_env.from_iterable(
            self._state_reference_generator(state_callbacks=scenario_creator.state_callbacks)
        ) | render_env.flat_map(
            partial(self._update_render_instance, yield_every_sim_state=yield_every_sim_state),
            workers=1,
            maxsize=2 * sim_capture_rate if sim_capture_rate is not None else 20,
        )

        yield from pipeline

        self.cleanup()

    def cleanup(self):
        if self.renderer is not None:
            self.renderer.cleanup()
        self.simulator.cleanup()
        if self.label_engine is not None:
            self.label_engine.cleanup()
        if self.shutdown_on_cleanup:
            self.shutdown()

    @staticmethod
    def resolve_by_name(
        instance_type: Type[TInstanceType],
        obj: Union[bool, TInstanceType, str, None] = None,
        instance_name: Optional[str] = None,
    ) -> Optional[TInstanceType]:
        if obj is False:
            obj = None
        elif obj is None or obj is True:
            if instance_name is not None:
                obj = instance_type(name=instance_name)
        elif isinstance(obj, str):
            obj = instance_type(name=obj)
        return obj

    @staticmethod
    def _resolve_name_to_instances(
        is_local_mode: bool,
        simulator: Union[bool, SimulationStateProvider, str, None] = None,
        renderer: Union[bool, RenderInstance, str, None] = None,
        label_engine: Union[bool, LabelEngineInstance, str, None] = None,
        instance_name: Optional[str] = None,
        **kwargs,
    ) -> Tuple[Optional[RenderInstance], Optional[SimulationStateProvider], Optional[LabelEngineInstance], str]:
        if simulator is False:
            simulator = CustomOnlySimulator()
        simulator = DataLabInstance.resolve_by_name(
            instance_type=SimulationInstance, obj=simulator, instance_name=instance_name
        )
        renderer = DataLabInstance.resolve_by_name(
            instance_type=RenderInstance, obj=renderer, instance_name=instance_name
        )
        label_engine = DataLabInstance.resolve_by_name(
            instance_type=LabelEngineInstance, obj=label_engine, instance_name=instance_name
        )

        if instance_name is None:
            if simulator is not None and hasattr(simulator, "name") and simulator.name is not None:
                instance_name = simulator.name
            elif renderer is not None:
                instance_name = renderer.name
            elif label_engine is not None:
                instance_name = label_engine.name
            elif not is_local_mode:
                raise ValueError(
                    "No instance name specified and no instance provided! Please provide an instance name."
                )
        return renderer, simulator, label_engine, instance_name

    @staticmethod
    def from_names(
        data_lab_version: str,
        fail_on_version_mismatch: bool = True,
        environment: Literal["prod", "stage", "dev"] = "prod",
        shutdown_on_cleanup: Optional[bool] = None,
        simulator: Union[bool, SimulationStateProvider, str, None] = None,
        label_engine: Union[bool, LabelEngineInstance, str, None] = None,
        renderer: Union[bool, RenderInstance, str, None] = None,
        instance_name: Optional[str] = None,
        **kwargs,
    ) -> "DataLabInstance":
        if data_lab_version == "local":
            if instance_name is not None or any(
                [
                    e.name is not None
                    for e in [simulator, label_engine, renderer]
                    if e is not None and hasattr(e, "name")
                ]
            ):
                raise ValueError(
                    "You cannot specify an instance name or renderer, simulation or label engine using an instance name"
                    "when using local mode. If you are using a local instance, set the address value instead of a name."
                    "Set the instance name to None or dont pass it at all to run in local mode."
                )

        setup_datalab(
            version=data_lab_version, environment=environment, fail_on_version_mismatch=fail_on_version_mismatch
        )
        renderer, simulator, label_engine, instance_name = DataLabInstance._resolve_name_to_instances(
            instance_name=instance_name,
            simulator=simulator,
            renderer=renderer,
            label_engine=label_engine,
            is_local_mode=data_lab_version == "local",
        )
        return DataLabInstance(
            simulator=simulator,
            renderer=renderer,
            label_engine=label_engine,
            name=instance_name,
            shutdown_on_cleanup=shutdown_on_cleanup if shutdown_on_cleanup is True else False,
        )

    @staticmethod
    def start(
        data_lab_version: str,
        locations: List[Location],
        simulator: bool = True,
        renderer: bool = True,
        label_engine: bool = True,
        fail_on_version_mismatch: bool = True,
        environment: Literal["prod", "stage", "dev"] = "prod",
        shutdown_on_cleanup: Optional[bool] = None,
        quality: Literal["high", "low"] = "high",
        ttl: Optional[int] = None,
    ) -> "DataLabInstance":
        if data_lab_version == "local":
            raise ValueError(
                "You cannot start a local instance. If you are using a local instance, you have to start it manually."
            )
        setup_datalab(
            version=data_lab_version, environment=environment, fail_on_version_mismatch=fail_on_version_mismatch
        )

        ig = Ig.create(
            ig_version=data_lab_version,
            sim_version=data_lab_version,
            le_version=data_lab_version if label_engine else None,
            quality=IgQuality(quality),
            levelpaks={ll.name: ll.version if ll.version is not None else data_lab_version for ll in locations},
            ttl=ttl,
        )
        instance_name = ig.name
        renderer, simulator, label_engine, instance_name = DataLabInstance._resolve_name_to_instances(
            instance_name=instance_name,
            simulator=simulator,
            renderer=renderer,
            label_engine=label_engine,
            is_local_mode=data_lab_version == "local",
        )
        return DataLabInstance(
            simulator=simulator,
            renderer=renderer,
            label_engine=label_engine,
            name=instance_name,
            # if we start an instance just for a single scene we want to shut it down afterwards
            shutdown_on_cleanup=shutdown_on_cleanup if shutdown_on_cleanup is False else True,
        )

    def shutdown(self):
        if self.name is not None:
            Ig.delete(self.name)
            logger.info(f"Instance {self.name} shut down")

    @staticmethod
    async def wait_until_instance_started(instance_name: str, sleep_time: int = 1, max_wait_time: int = 1800):
        tries = 0
        wait_time = 0
        time_since_last_log = 0
        log_every = 5  # 5 * 1 tries
        try:
            ig = Ig.read(name=instance_name)
        except HTTPError as e:
            if "NOT FOUND" not in str(e):  # other HTTPError we don't expect
                raise e
            raise PdError(
                f"Your instance '{instance_name}' could not be found. Please check your instance name and status."
            )
        status = ig.status
        started = status == IgStatus.Running
        status_changed = False
        while not started:
            tries += 1
            try:
                ig = Ig.read(name=instance_name)
                current_status = ig.status
                status_changed = status != current_status
                status = current_status
                started = status == IgStatus.Running
            except Exception as e:
                logger.exception(e)
            if time_since_last_log % log_every == 0 or status_changed:
                logger.info(f"Instance {ig.name} is {status.name}: {wait_time}s")
                time_since_last_log = 0
            if not started:
                log_every = min(30, 5 * tries)
                if status_changed:
                    status_changed = False
                await asyncio.sleep(sleep_time)
                time_since_last_log += sleep_time
                wait_time += sleep_time
            else:
                await asyncio.sleep(30)

            if wait_time >= max_wait_time:
                raise ConnectionError(
                    f"Instance {ig.name} seems to have problems starting up! Please consult with the PD Step team!"
                )
        # sleep to make sure all server daemon are up and running. We get zmq connection issues atm without this
        logger.info(f"Instance {ig.name} is {status.name}")
