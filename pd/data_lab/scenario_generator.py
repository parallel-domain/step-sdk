# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import logging
from typing import Optional, Tuple, Type, TypeVar, Generic

from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.data_lab.render_instance import AbstractRenderInstance, ManagedRenderInstance
from pd.data_lab.scenario import DiscreteScenario, Scenario
from pd.data_lab.session_reference import TemporalSessionReference
from pd.data_lab.sim_instance import SimulationStateProvider, CustomOnlySimulationInstance
from pd.data_lab.sim_state import SimState
from pd.internal.proto.umd.generated.wrapper import UMD_pb2

logger = logging.getLogger(__name__)

TSimState = TypeVar("TSimState", bound=SimState)


class ScenarioGenerator(Generic[TSimState]):
    def __init__(
        self,
        discrete_scenario: DiscreteScenario,
        sim_instance: Optional[SimulationStateProvider] = None,
        render_instance: Optional[AbstractRenderInstance] = None,
        yield_every_sim_state: bool = False,
        sim_state_type: Type[TSimState] = SimState,
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
        self._render_instance = render_instance
        self._sim_instance = sim_instance
        self._sim_state_type = sim_state_type
        self._yield_every_sim_state = yield_every_sim_state
        # self.sensor_rig = self.scenario.sensor_rig
        self._sim_state: Optional[TSimState] = None
        self._first_frame: bool = True
        self._map: Optional[UMD_pb2.UniversalMap] = None

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
        try:
            self.setup_new_scene()
        except PdError as e:
            logger.exception(e)
            logger.warning(
                f"Had an error during scene setup. Likely a sim fail. Skipping scene {self.discrete_scenario.name}"
            )
            return

        while True:
            temporal_sensor_session_reference, sim_state = self.next_frame()
            if sim_state is None:
                return
            yield temporal_sensor_session_reference, sim_state

    def setup_new_scene(self) -> TSimState:
        logger.info(f"setting up scene {self.discrete_scenario.name}")

        self._sim_state = self._sim_state_type.from_blank_state()

        self._sim_instance.setup(discrete_scenario=self.discrete_scenario, sim_state=self._sim_state)

        return self._sim_state

    def next_frame(self) -> Tuple[Optional[TemporalSessionReference], Optional[TSimState]]:
        if self._first_frame:
            # on beginning we need to run start_skip_frames plus one frame we want to capture
            self._first_frame = False
            sim_capture_rate = self.discrete_scenario.start_skip_frames + 1
        else:
            sim_capture_rate = max(1, self.discrete_scenario.sim_capture_rate)

        temporal_session_reference = None
        for i in range(sim_capture_rate):
            # this updates the current simulation state in our sim state
            has_state = self._sim_instance.next_frame(sim_state=self._sim_state)

            if has_state is False:
                # if the sim instance has no more state we signal the end of the scene by returning None
                # this is the case when loading states from disk or if we have defined a max number of frames
                # in the simulation config
                return None, None

            # Flags to the renderer if we want to access this frame
            # e.g. preview the image or save to disk
            # Since we only capture the last frame of #sim_capture_rate we check for the last index
            # or in case we set the yield_every_sim_state flag (this is only used for storing sim states though)
            capture = i == sim_capture_rate - 1 or self._yield_every_sim_state
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

                # here we actually render the frame and get a reference to the rendered data
                # we only return this if yield_every_sim_state is set or for the last frame in this loop
                temporal_session_reference = self._render_instance.render_frame(sim_state=self._sim_state)
            if self._yield_every_sim_state:
                return temporal_session_reference, self._sim_state

        if not self._yield_every_sim_state:
            return temporal_session_reference, self._sim_state
