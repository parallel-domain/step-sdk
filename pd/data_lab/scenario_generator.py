# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import logging
from typing import Optional, Type, TypeVar, Generic, Iterator, Union

import pypeln

from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.data_lab.label_engine_instance import LabelEngineInstance
from pd.data_lab.labeled_state_reference import LabeledStateReference, StateReference
from pd.data_lab.render_instance import AbstractRenderInstance, ManagedRenderInstance
from pd.data_lab.scenario import DiscreteScenario, Scenario
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_instance import SimulationStateProvider, CustomOnlySimulationInstance
from pd.data_lab.sim_state import SimState
from pd.internal.proto.umd.generated.wrapper import UMD_pb2
from pd.session import generate_scene_name

logger = logging.getLogger(__name__)

TSimState = TypeVar("TSimState", bound=SimState)


class ScenarioGenerator(Generic[TSimState]):
    def __init__(
        self,
        discrete_scenario: DiscreteScenario,
        label_engine_instance: Optional[LabelEngineInstance] = None,
        sim_instance: Optional[SimulationStateProvider] = None,
        render_instance: Optional[AbstractRenderInstance] = None,
        yield_every_sim_state: bool = False,
        sim_state_type: Type[TSimState] = SimState,
        run_sim_and_renderer_asynchronously: bool = True,
        fail_on_sim_error: bool = True,
        **kwargs,
    ):
        self.discrete_scenario = discrete_scenario

        if render_instance is None and "step_url" in kwargs:
            render_instance = ManagedRenderInstance(
                locations=[self.discrete_scenario.location],
                address=kwargs.pop("step_url", None),
                **kwargs,
            )
        elif isinstance(render_instance, ManagedRenderInstance):
            render_instance.locations = [self.discrete_scenario.location]
        if (
            isinstance(discrete_scenario, Scenario)
            and len(discrete_scenario.pd_generators) == 0
            and sim_instance is None
        ):
            sim_instance = CustomOnlySimulationInstance()
        self._run_sim_and_renderer_asynchronously = run_sim_and_renderer_asynchronously
        if label_engine_instance is None:
            self._run_sim_and_renderer_asynchronously = False
        self._render_instance = render_instance
        self._sim_instance = sim_instance
        self._label_engine_instance = label_engine_instance
        self._sim_state_type = sim_state_type
        self._yield_every_sim_state = yield_every_sim_state
        # self.sensor_rig = self.scenario.sensor_rig
        self._sim_state: Optional[TSimState] = None
        self._first_frame: bool = True
        self._map: Optional[UMD_pb2.UniversalMap] = None
        self._fail_on_sim_error = fail_on_sim_error

        self._unique_scene_name = generate_scene_name()
        if self._render_instance is not None:
            self._render_instance.set_unique_scene_name(self._unique_scene_name)
        if self._label_engine_instance is not None:
            self._label_engine_instance.set_unique_scene_name(self._unique_scene_name)

    def __enter__(self):
        if self._render_instance is not None:
            self._render_instance.__enter__()
        if self._sim_instance is not None:
            self._sim_instance.__enter__()
        if self._label_engine_instance is not None:
            self._label_engine_instance.__enter__()

        return self

    def __exit__(self, *args):
        if self._render_instance is not None:
            self._render_instance.__exit__()
        if self._sim_instance is not None:
            self._sim_instance.__exit__()
        if self._label_engine_instance is not None:
            self._label_engine_instance.__exit__()

    def __iter__(self) -> Iterator[LabeledStateReference]:
        try:
            self.setup_new_scene()
        except PdError as e:
            logger.exception(e)
            if self._fail_on_sim_error is True:
                raise
            else:
                logger.warning(
                    f"Had an error during scene setup. Likely a sim fail. Skipping scene {self.discrete_scenario.name}"
                )
                return
        if self._run_sim_and_renderer_asynchronously:
            run_env = pypeln.thread
        else:
            run_env = pypeln.sync
        pipeline = run_env.from_iterable(self.iterate_sim_states()) | run_env.flat_map(
            self.update_render_instance, workers=1, maxsize=10
        )

        yield from pipeline

    def setup_new_scene(self) -> TSimState:
        logger.info(f"setting up scene {self.discrete_scenario.name}")

        self._sim_state = self._sim_state_type.from_blank_state()

        self._sim_instance.setup(discrete_scenario=self.discrete_scenario, sim_state=self._sim_state)

        return self._sim_state

    def iterate_sim_states(self) -> Iterator[StateReference]:
        assert self._sim_state is not None

        first_frame = True
        while True:
            if first_frame:
                # on beginning we need to run start_skip_frames plus one frame we want to capture
                sim_capture_rate = self.discrete_scenario.start_skip_frames + 1
            else:
                sim_capture_rate = max(1, self.discrete_scenario.sim_capture_rate)

            for i in range(sim_capture_rate):
                # we already have the first state from sim instance setup, but have not rendered it yet
                if first_frame:
                    has_state = True
                    first_frame = False
                else:
                    # this updates the current simulation state in our sim state
                    has_state = self._sim_instance.next_frame(sim_state=self._sim_state)

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

                if self._render_instance is not None:
                    if not self._render_instance.location_is_set:
                        # for the first frame we render we also need to make sure that the current map
                        # and time of day is loaded
                        self._render_instance.load_environment(
                            location=Location(name=self._sim_state.current_state.world_info.location),
                            time_of_day=self._sim_state.current_state.world_info.time_of_day,
                        )
                        if self._render_instance.loaded_location is not None:
                            # if we have access to the loaded location of the renderer
                            # update the loaded map to make sure whe match the version
                            # since State only contains a map name but nor the version we use this to ensure that
                            # we can load the right umd map version that matches the loaded map
                            location = self._render_instance.loaded_location
                            self._sim_state.set_location(location=location)

                if self._label_engine_instance is None and self._render_instance is None:
                    yield StateReference(
                        state=self._sim_state.current_state,
                        frame_id=self._sim_state.current_frame_id,
                        ego_agent_id=self._sim_state.ego_agent_id,
                    )
                elif self._label_engine_instance is None:
                    yield self._render_instance.render_frame(sim_state=self._sim_state)
                else:
                    yield LabeledStateReference(
                        label_engine=self._label_engine_instance,
                        state=self._sim_state.current_state,
                        frame_id=self._sim_state.current_frame_id,
                        ego_agent_id=self._sim_state.ego_agent_id,
                    )

    def update_render_instance(self, item: Union[StateReference]) -> Iterator[StateReference]:
        if self._render_instance is not None:
            if self._label_engine_instance is not None:
                self._render_instance.update_state(sim_state=item.state)

        # We need to yield every sim state in step batch, to avoid aliasing effects from only outputting capture frames.
        # Here, not all frames have been necessarily been marked for capture.
        if self._yield_every_sim_state is True:
            yield item
        else:
            # Otherwise we only output capture frames, which is what we want to do in "Data Lab" mode.
            if item.state.capture is True:
                yield item
