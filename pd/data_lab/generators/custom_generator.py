# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
from typing import Callable, Generic, List, Optional, TypeVar

from pd.data_lab.generators import BaseGenerator
from pd.data_lab.generators.custom_simulation_agent import CustomSimulationAgent
from pd.data_lab.sim_state import SimState

TSimState = TypeVar("TSimState", bound=SimState)


class CustomAtomicGenerator(BaseGenerator, Generic[TSimState]):
    def __init__(self):
        self.agents: List[CustomSimulationAgent] = list()
        self._has_ego_agent = False

    def add_agent(self, agent: CustomSimulationAgent):
        self.agents.append(agent)

    @abc.abstractmethod
    def create_agents_for_new_scene(self, state: TSimState, random_seed: int) -> List[CustomSimulationAgent]:
        pass

    @property
    def has_ego_agent(self) -> bool:
        return self._has_ego_agent

    def on_new_scene(self, state: TSimState, random_seed: int):
        self.agents = list()
        self._has_ego_agent = False

        for agent in self.create_agents_for_new_scene(state=state, random_seed=random_seed):
            if agent.sensor_rig is not None:
                state.set_ego_agent_id(agent.agent_id)
                self._has_ego_agent = True
            self.add_agent(agent)
            state.set_agent(agent=agent)

        self.agents.sort(key=lambda a: len(a.step_agent.sensors) > 0, reverse=True)

    def update_state(self, state: TSimState, raycast: Optional[Callable] = None):
        for agent in self.agents:
            agent.update_state(state, raycast=raycast)
            state.set_agent(agent=agent)

    def set_initial_agent_positions(self, state: TSimState, random_seed: int, raycast: Optional[Callable] = None):
        for agent in self.agents:
            agent.set_initial_state(sim_state=state, random_seed=random_seed, raycast=raycast)


class DefaultCustomAtomicGenerator(CustomAtomicGenerator[TSimState]):
    def create_agents_for_new_scene(self, state: TSimState, random_seed: int) -> List[CustomSimulationAgent[TSimState]]:
        return []

    def add_agent(self, agent: CustomSimulationAgent[TSimState]):
        self.agents.append(agent)

    def on_new_scene(self, state: TSimState, random_seed: int):
        for agent in self.agents:
            if agent.sensor_rig is not None:
                state.set_ego_agent_id(agent.agent_id)
                self._has_ego_agent = True
            state.set_agent(agent=agent)

        self.agents.sort(key=lambda a: len(a.step_agent.sensors) > 0, reverse=True)

    def clone(self) -> "DefaultCustomAtomicGenerator[TSimState]":
        clone = DefaultCustomAtomicGenerator[TSimState]()
        for a in self.agents:
            clone.add_agent(agent=a.clone())
        return clone
