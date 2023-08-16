# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import abc
from functools import lru_cache
from typing import Union, Tuple

import numpy as np

import pd.state
from pd.internal.assets.asset_registry import ObjAssets
from pd.state import Pose6D, ModelAgent

StepAgentType = Union[pd.state.VehicleAgent, pd.state.ModelAgent]


class SimulationAgentBase:
    @property
    @abc.abstractmethod
    def step_agent(self) -> StepAgentType:
        pass

    @property
    @lru_cache(maxsize=1)
    def width_height_length(self) -> Tuple[float, float, float]:
        agent_name = (
            self.step_agent.asset_name if isinstance(self.step_agent, ModelAgent) else self.step_agent.vehicle_type
        )
        assets = ObjAssets.select(ObjAssets.name, ObjAssets.width, ObjAssets.height, ObjAssets.length).where(
            ObjAssets.name == agent_name
        )
        try:
            width, height, length = {obj.name: (obj.width, obj.height, obj.length) for obj in assets}[agent_name]
        except KeyError:  # asset name was not found during query, so use unit cube as default size
            width, height, length = 1.0, 1.0, 1.0

        return width, height, length

    @property
    def width(self) -> float:  # or: transverse
        return self.width_height_length[0]

    @property
    def height(self) -> float:  # or: vertical
        return self.width_height_length[1]

    @property
    def length(self) -> float:  # or: longitudinal
        return self.width_height_length[2]

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
