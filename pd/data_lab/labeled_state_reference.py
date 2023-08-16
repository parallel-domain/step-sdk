# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from datetime import datetime, timezone

from pd.data_lab.label_engine_instance import LabelEngineInstance
from pd.label_engine import simulation_time_as_timestamp
from pd.state import State
from pd.state.state import Agent


class StateReference:
    def __init__(self, state: State, frame_id: str, ego_agent_id: int):
        self._state = state
        self.frame_id = frame_id
        self.ego_agent_id = ego_agent_id

    @property
    def ego_agent(self) -> Agent:
        matching_agents = [a for a in self._state.agents if a.id == self.ego_agent_id]
        if len(matching_agents) != 1:
            raise ValueError(f"Found {len(matching_agents)} agents with ego agent id. Expected 1.")
        return matching_agents[0]

    @property
    def date_time(self) -> datetime:
        return datetime.fromtimestamp(self._state.simulation_time_sec, tz=timezone.utc)

    @property
    def state(self) -> State:
        return self._state


class LabeledStateReference(StateReference):
    def __init__(self, label_engine: LabelEngineInstance, state: State, frame_id: str, ego_agent_id: int):
        super().__init__(state=state, frame_id=frame_id, ego_agent_id=ego_agent_id)
        self.label_engine = label_engine

    @property
    def frame_timestamp(self) -> str:
        return simulation_time_as_timestamp(self.state.simulation_time_sec)
