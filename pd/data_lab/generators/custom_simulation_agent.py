# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import random
from typing import Literal, Optional, Tuple, Union, TypeVar, Generic, List

import numpy as np
import pd.state
from pd.assets import get_asset_names_in_category, get_vehicle_colors, get_vehicle_wheel_names, get_vehicle_wheel_poses
from pd.data_lab.generators.simulation_agent import SimulationAgentBase
from pd.data_lab.sim_state import SimState
from pd.internal.assets.asset_registry import ObjAssets
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig
from pd.state import Pose6D

TSimState = TypeVar("TSimState", bound=SimState)
StepAgentType = Union[pd.state.VehicleAgent, pd.state.ModelAgent]


class CustomSimulationAgentBehaviour(Generic[TSimState]):
    @abc.abstractmethod
    def update_state(self, sim_state: TSimState, agent: "CustomSimulationAgent"):
        pass

    @abc.abstractmethod
    def set_inital_state(self, sim_state: TSimState, agent: "CustomSimulationAgent", random_seed: int):
        pass

    @abc.abstractmethod
    def clone(self) -> "CustomSimulationAgentBehaviour[TSimState]":
        pass


class CustomSimulationAgent(SimulationAgentBase, Generic[TSimState]):
    def __init__(self, sensor_rig: Optional[SensorRig], step_agent: StepAgentType):
        super().__init__()
        self._behaviour: CustomSimulationAgentBehaviour[TSimState] = None
        self._pose = np.eye(4)
        self._velocity = None
        self._step_agent = step_agent
        self.sensor_rig = sensor_rig

    @property
    def agent_id(self) -> int:
        return self._step_agent.id

    @property
    def step_agent(self) -> StepAgentType:
        return self._step_agent

    def set_behaviour(self, behaviour: CustomSimulationAgentBehaviour) -> "CustomSimulationAgent":
        self._behaviour = behaviour
        return self

    def set_inital_state(self, sim_state: TSimState, random_seed: int):
        self._initialize_step_agent(random_seed=random_seed)
        self.set_pose(pose=self._pose, velocity=self._velocity)

        if self._behaviour is not None:
            self._behaviour.set_inital_state(sim_state=sim_state, agent=self, random_seed=random_seed)

    def set_pose(self, pose: np.ndarray, velocity: Optional[Tuple[float, float, float]] = None):
        self._pose = pose
        self._velocity = velocity
        if self._step_agent is not None:
            self.step_agent.pose = pose
            if velocity is not None:
                self.step_agent.velocity = velocity

    def update_state(self, sim_state: TSimState):
        if self._behaviour is not None:
            self._behaviour.update_state(sim_state=sim_state, agent=self)

    @abc.abstractmethod
    def _initialize_step_agent(self, random_seed: int):
        pass

    @staticmethod
    def character_assets() -> List[str]:
        return sorted(list(get_asset_names_in_category("character")))

    @staticmethod
    def vehicle_assets() -> List[str]:
        return sorted(list(get_asset_names_in_category("vehicle")))

    @staticmethod
    def traffic_control_assets() -> List[str]:
        return sorted(list(get_asset_names_in_category("traffic_control")))

    @staticmethod
    def prop_assets() -> List[str]:
        return sorted(list(get_asset_names_in_category("prop")))


class CustomVehicleSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        asset_name: Optional[str] = None,
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        # Just setup defaults. Init later
        step_agent = pd.state.VehicleAgent(
            vehicle_type=asset_name, id=pd.state.rand_agent_id(), pose=np.eye(4), velocity=(0.0, 0.0, 0.0)
        )
        super().__init__(sensor_rig=sensor_rig, step_agent=step_agent)

    def _initialize_step_agent(self, random_seed: int):
        state = random.Random(random_seed)
        asset_name = self._asset_name
        if asset_name is None:
            asset_name = state.choice(CustomSimulationAgent.vehicle_assets())

        possible_wheels = get_vehicle_wheel_names(asset_name)
        wheel_name = None
        wheel_poses = []
        if len(possible_wheels) > 0:
            wheel_name = state.choice(possible_wheels)
            wheel_poses = get_vehicle_wheel_poses(vehicle_name=asset_name, wheel_name=wheel_name)

        color = None
        colors = get_vehicle_colors(asset_name)
        if len(colors) > 0:
            color = state.choice(colors)

        occupants = state.choice(CustomSimulationAgent.character_assets())

        sensors = list()
        if self.sensor_rig is not None:
            sensors.extend(self.sensor_rig.sensors)

        self.step_agent.pose = Pose6D.from_transformation_matrix(np.eye(4))
        self.step_agent.velocity = (0.0, 0.0, 0.0)
        self.step_agent.vehicle_type = asset_name
        self.step_agent.lock_to_ground = self.lock_to_ground
        self.step_agent.ground_offset = self.ground_offset
        self.step_agent.wheel_type = wheel_name
        self.step_agent.wheel_poses = wheel_poses
        self.step_agent.vehicle_color = color
        self.step_agent.vehicle_wear = state.random()
        self.step_agent.occupants = [occupants]
        self.step_agent.sensors = [s.to_step_sensor() for s in sensors]

    def clone(self) -> "CustomVehicleSimulationAgent[TSimState]":
        cloned = CustomVehicleSimulationAgent(
            sensor_rig=self.sensor_rig,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
        )
        cloned.set_behaviour(behaviour=self._behaviour.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomPedestrianSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        asset_name: Optional[str] = None,
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        step_agent = pd.state.ModelAgent(
            asset_name=asset_name, id=pd.state.rand_agent_id(), pose=np.eye(4), velocity=(0.0, 0.0, 0.0)
        )
        super().__init__(sensor_rig=sensor_rig, step_agent=step_agent)

    def _initialize_step_agent(self, random_seed: int) -> StepAgentType:
        asset_name = self._asset_name
        if asset_name is None:
            if random_seed is None:
                raise ValueError("If no asset name is passed, a random seed is required!")
            asset_name = random.Random(random_seed).choice(CustomSimulationAgent.character_assets())

        sensors = list()
        if self.sensor_rig is not None:
            sensors.extend(self.sensor_rig.sensors)

            self._step_agent.pose = Pose6D.from_transformation_matrix(np.eye(4))
            self._step_agent.velocity = (0.0, 0.0, 0.0)
            self._step_agent.asset_name = asset_name
            self._step_agent.lock_to_ground = self.lock_to_ground
            self._step_agent.ground_offset = self.ground_offset
            self._step_agent.sensors = [s.to_step_sensor() for s in sensors]

    def clone(self) -> "CustomPedestrianSimulationAgent[TSimState]":
        cloned = CustomPedestrianSimulationAgent(
            sensor_rig=self.sensor_rig,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
        )
        cloned.set_behaviour(behaviour=self._behaviour.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomObjectSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        asset_name: Optional[str] = None,
        asset_category: Optional[Literal["character", "vehicle", "traffic_control", "prop"]] = "traffic_control",
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        self._asset_category = asset_category
        step_agent = pd.state.ModelAgent(
            asset_name=asset_name, id=pd.state.rand_agent_id(), pose=np.eye(4), velocity=(0.0, 0.0, 0.0)
        )
        super().__init__(sensor_rig=sensor_rig, step_agent=step_agent)

    def _initialize_step_agent(self, random_seed: int) -> StepAgentType:
        asset_name = self._asset_name
        asset_category = self._asset_category
        if asset_name is None:
            if random_seed is None:
                raise ValueError("If no asset name is passed, a random seed is required!")
            if asset_category == "traffic_control":
                dist = CustomSimulationAgent.traffic_control_assets()
            elif asset_category == "character":
                dist = CustomSimulationAgent.character_assets()
            elif asset_category == "vehicle":
                dist = CustomSimulationAgent.vehicle_assets()
            else:
                dist = CustomSimulationAgent.prop_assets()
            asset_name = random.Random(random_seed).choice(dist)

        sensors = list()
        if self.sensor_rig is not None:
            sensors.extend(self.sensor_rig.sensors)

            self._step_agent.pose = Pose6D.from_transformation_matrix(np.eye(4))
            self._step_agent.velocity = (0.0, 0.0, 0.0)
            self._step_agent.asset_name = asset_name
            self._step_agent.lock_to_ground = self.lock_to_ground
            self._step_agent.ground_offset = self.ground_offset
            self._step_agent.sensors = [s.to_step_sensor() for s in sensors], self._step_agent

    def clone(self) -> "CustomObjectSimulationAgent[TSimState]":
        cloned = CustomObjectSimulationAgent(
            sensor_rig=self.sensor_rig,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
            asset_category=self._asset_category,
        )
        cloned.set_behaviour(behaviour=self._behaviour.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomSimulationAgents(Generic[TSimState]):
    @staticmethod
    def create_ego_pedestrian(
        sensor_rig: Optional[SensorRig] = None,
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
    ) -> CustomSimulationAgent:
        return CustomPedestrianSimulationAgent(
            sensor_rig=sensor_rig, ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name
        )

    @staticmethod
    def create_pedestrian(
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomPedestrianSimulationAgent(
            ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name
        )

    @staticmethod
    def create_object(
        sensor_rig: Optional[SensorRig] = None,
        asset_name: Optional[str] = None,
        asset_category: Optional[Literal["character", "vehicle", "traffic_control", "prop"]] = "traffic_control",
        lock_to_ground: bool = True,
        ground_offset=0.0,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomObjectSimulationAgent(
            ground_offset=ground_offset,
            lock_to_ground=lock_to_ground,
            asset_name=asset_name,
            asset_category=asset_category,
            sensor_rig=sensor_rig,
        )

    @staticmethod
    def create_ego_vehicle(
        sensor_rig: SensorRig,
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomVehicleSimulationAgent(
            sensor_rig=sensor_rig, ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name
        )

    @staticmethod
    def create_vehicle(
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomVehicleSimulationAgent(
            ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name
        )

    @staticmethod
    def get_asset_size(asset_name: str) -> Tuple[float, float, float]:
        asset = [i for i in ObjAssets.select().where(ObjAssets.name == asset_name)][0]
        return asset.width, asset.length, asset.height
