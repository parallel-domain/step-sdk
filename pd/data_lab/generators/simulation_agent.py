# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import abc
from typing import Union

import numpy as np

import pd.state
from pd.state import Pose6D


StepAgentType = Union[pd.state.VehicleAgent, pd.state.ModelAgent]

class SimulationAgentBase:
    @property
    @abc.abstractmethod
    def step_agent(self) -> StepAgentType:
        pass

    @property
    @abc.abstractmethod
    def agent_id(self) -> int:
        return self.step_agent.id

    @property
    def pose(self) -> np.ndarray:
        if isinstance(self.step_agent.pose, Pose6D):
            mat = self.step_agent.pose.as_transformation_matrix()
        else:
            mat = self.step_agent.pose
        return mat


class SimulationAgent(SimulationAgentBase):
    def __init__(self, step_agent: StepAgentType):
        self._step_agent = step_agent
    @property
    def step_agent(self) -> StepAgentType:
        return self._step_agent

    @property
    def agent_id(self) -> int:
        return self.step_agent.id

    @property
    def pose(self) -> np.ndarray:
        if isinstance(self.step_agent.pose, Pose6D):
            mat = self.step_agent.pose.as_transformation_matrix()
        else:
            mat = self.step_agent.pose
        return mat
