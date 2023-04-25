# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import os
import logging
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Union

import numpy as np

import pd.state
from pd.core import PdError
from pd.data_lab.generators.simulation_agent import SimulationAgent, SimulationAgentBase
from pd.state import Pose6D
from pd.umd import load_umd_map, load_umd_map_from_file
from pd.data_lab.context import get_datalab_context
from pd.data_lab.config.location import Location
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig
from pd.internal.proto.umd.generated.wrapper.UMD_pb2 import UniversalMap

logger = logging.getLogger(__name__)


class SimState:
    def __init__(self, initial_state: Optional[pd.state.State] = None, sensor_rig: SensorRig = None):
        self._current_state = initial_state
        self._previous_state = None
        self.sensor_rig = sensor_rig
        self.ego_agent_id = None
        self._map = None
        self.frame_count = 0
        self.sim_time: float = 0.0
        self.frame_ids = [str(0)]
        self.frame_date_times = [datetime.fromtimestamp(self.sim_time)]
        self.time_since_last_frame: float = 0

        self._current_agents = list()
        self._previous_agents = list()

    @property
    def is_initialized(self) -> bool:
        return self._current_state is not None and self.ego_agent_id is not None

    @property
    def current_state(self) -> pd.state.State:
        return self._current_state

    @property
    def previous_state(self) -> pd.state.State:
        return self._previous_state

    @property
    def current_sim_date_time(self) -> datetime:
        return self.frame_date_times[-1]

    @property
    def current_frame_id(self) -> str:
        return self.frame_ids[-1]

    def set_next_state_message(self, state: Optional[pd.state.State], time_delta: float):
        if state is None:
            world_info = pd.state.WorldInfo(street_lights=1.0)
            state = pd.state.State(simulation_time_sec=0.0, world_info=world_info, agents=[])
        self._previous_state = self._current_state
        self._current_state = state

        self._previous_agents = self._current_agents
        self._current_agents = [SimulationAgent(step_agent=a) for a in state.agents]

        self.frame_ids.append(str(self.frame_count))
        self.frame_date_times.append(datetime.fromtimestamp(self.sim_time))

        self.frame_count += 1
        self.time_since_last_frame = time_delta
        self.sim_time += time_delta

    def set_next_state_message_from_previous(self, time_delta: float):
        state = pd.state.State(simulation_time_sec=self.sim_time, world_info=self._current_state.world_info, agents=[])
        self.set_next_state_message(state=state, time_delta=time_delta)

    def set_ego_agent_id(self, ego_id: int):
        self.ego_agent_id = ego_id

    def set_location(self, location: Location, map_file: Optional[Union[str, Path]] = None):
        if self.current_state is not None:
            self.current_state.world_info.location = location.name

        # Load Map now that location has been identified
        context = get_datalab_context()
        if context.is_mode_local:
            if not map_file:
                map_file = Path(os.environ.get("PD_ROOT", "")) / 'generated' / 'locations' / \
                           location.name / f'{location.name}.umd'
                if not map_file.is_file():
                    raise PdError(f"Couldn't find local map (Umd) for map {location.name} at {str(map_file)}. "
                                  "Please download the map artifact or pass a 'map_file' "
                                  "parameter with the path to the map (Umd) file.")
            self._map = UniversalMap(proto=load_umd_map_from_file(path=Path(map_file)))
        else:
            try:
                self._map = UniversalMap(proto=load_umd_map(name=location.name, version=location.version))
            except PdError as e:
                logger.warning("Could not load map from management API with error:")
                logger.warning(str(e))

    def set_time_of_day(self, time_of_day: str):
        if self.current_state is not None:
            self.current_state.world_info.time_of_day = time_of_day

    @property
    def map(self) -> UniversalMap:
        if self._map is None:
            raise ValueError("No map data available for the currently loaded map!")
        return self._map

    def set_agent(self, agent: SimulationAgentBase):
        self._current_agents.append(agent)
        self.current_state.agents.append(agent.step_agent)

    @property
    def ego_agent(self) -> SimulationAgentBase:
        return self.get_agent(agent_id=self.ego_agent_id, on_current_frame=True)

    @property
    def prev_ego_agent(self) -> SimulationAgentBase:
        return self.get_agent(agent_id=self.ego_agent_id, on_current_frame=False)

    def get_agent(self, agent_id: int, on_current_frame: bool = False) -> Union[SimulationAgentBase, None]:
        if on_current_frame:
            return next(iter([a for a in self.current_agents if a.agent_id == agent_id]), None)
        else:
            return next(iter([a for a in self.previous_agents if a.agent_id == agent_id]), None)

    @property
    def current_agents(self) -> List[SimulationAgentBase]:
        return self._current_agents

    @property
    def previous_agents(self) -> List[SimulationAgentBase]:
        return self._previous_agents

    @property
    def ego_pose(self) -> Union[Pose6D, np.ndarray]:
        return self.ego_agent.pose
        # if isinstance(ego_pose, np.ndarray):
        #     mat = ego_pose
        # else:
        #     mat = ego_pose.as_transformation_matrix()
        # quaternion = Rotation.from_matrix(mat[:3, :3]).as_quat()
        # quaternion = [quaternion[3], quaternion[0], quaternion[1], quaternion[2]]
        # return Transformation(quaternion=quaternion, translation=mat[:3, 3])

    @staticmethod
    def from_blank_state(**kwargs) -> "SimState":
        world_info = pd.state.WorldInfo(street_lights=1.0)
        state = pd.state.State(simulation_time_sec=0.0, world_info=world_info, agents=[])
        return SimState(initial_state=state, **kwargs)
