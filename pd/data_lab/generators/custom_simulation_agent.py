# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
import random
from typing import Callable, Generic, List, Literal, Optional, Tuple, TypeVar, Union
from warnings import warn

import numpy as np
from deprecation import deprecated

import pd.state
from pd.assets import get_asset_names_in_category, get_vehicle_colors, get_vehicle_wheel_names, get_vehicle_wheel_poses
from pd.core import PdError
from pd.data_lab.generators.simulation_agent import SimulationAgentBase
from pd.data_lab.sim_state import SimState
from pd.internal.assets.asset_registry import ObjAssets
from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorRigConfig as SensorRig
from pd.state import Pose6D

TSimState = TypeVar("TSimState", bound=SimState)
StepAgentType = Union[pd.state.VehicleAgent, pd.state.ModelAgent, pd.state.SensorAgent]

logger = logging.getLogger()


class CustomSimulationAgentBehavior(Generic[TSimState]):
    @abc.abstractmethod
    def update_state(self, sim_state: TSimState, agent: "CustomSimulationAgent", raycast: Optional[Callable] = None):
        pass

    @abc.abstractmethod
    def set_initial_state(
        self, sim_state: TSimState, agent: "CustomSimulationAgent", random_seed: int, raycast: Optional[Callable] = None
    ):
        pass

    @abc.abstractmethod
    def clone(self) -> "CustomSimulationAgentBehavior[TSimState]":
        pass


# Maintained for backwards compatibility
CustomSimulationAgentBehaviour = CustomSimulationAgentBehavior


class CustomSimulationAgent(SimulationAgentBase, Generic[TSimState]):
    def __init__(self, sensor_rig: Optional[SensorRig], step_agent: StepAgentType):
        super().__init__()
        self._behavior: Optional[CustomSimulationAgentBehavior[TSimState]] = None
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

    # Maintained for backwards compatibility
    @deprecated(details="Use `set_behavior` instead")
    def set_behaviour(self, behaviour: CustomSimulationAgentBehavior) -> "CustomSimulationAgent":
        return self.set_behavior(behavior=behaviour)

    def set_behavior(self, behavior: CustomSimulationAgentBehavior) -> "CustomSimulationAgent":
        self._behavior = behavior
        return self

    def set_initial_state(self, sim_state: TSimState, random_seed: int, raycast: Optional[Callable] = None):
        self._initialize_step_agent(random_seed=random_seed)
        self.set_pose(pose=self._pose, velocity=self._velocity)

        if self._behavior is not None:
            self._behavior.set_initial_state(sim_state=sim_state, agent=self, random_seed=random_seed, raycast=raycast)

    def set_pose(self, pose: np.ndarray, velocity: Optional[Tuple[float, float, float]] = None):
        self._pose = pose
        self._velocity = velocity
        if self._step_agent is not None:
            self.step_agent.pose = pose
            if velocity is not None:
                self.step_agent.velocity = velocity

    def update_state(self, sim_state: TSimState, raycast: Optional[Callable] = None):
        if self._behavior is not None:
            self._behavior.update_state(sim_state=sim_state, agent=self, raycast=raycast)

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

    @abc.abstractmethod
    def clone(self) -> "CustomSimulationAgent[TSimState]":
        pass


class CustomVehicleSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        asset_name: Optional[str] = None,
        agent_id: Optional[int] = None,
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        # Just setup defaults. Init later
        step_agent = pd.state.VehicleAgent(
            vehicle_type=asset_name,
            id=pd.state.rand_agent_id() if agent_id is None else agent_id,
            pose=np.eye(4),
            velocity=(0.0, 0.0, 0.0),
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
            sensor_rig=self.sensor_rig.clone() if self.sensor_rig is not None else None,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
            agent_id=self.agent_id,
        )
        if self._behavior is None:
            raise PdError(f"Missing behavior for {self.__class__.__name__}. Use `set_behavior()` to set a behavior.")
        cloned.set_behavior(behavior=self._behavior.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomPedestrianSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        asset_name: Optional[str] = None,
        agent_id: Optional[int] = None,
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        step_agent = pd.state.ModelAgent(
            asset_name=asset_name,
            id=pd.state.rand_agent_id() if agent_id is None else agent_id,
            pose=np.eye(4),
            velocity=(0.0, 0.0, 0.0),
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
            sensor_rig=self.sensor_rig.clone() if self.sensor_rig is not None else None,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
            agent_id=self.agent_id,
        )
        if self._behavior is None:
            raise PdError(f"Missing behavior for {self.__class__.__name__}. Use `set_behavior()` to set a behavior.")
        cloned.set_behavior(behavior=self._behavior.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomSensorSimulationAgent(CustomSimulationAgent, Generic[TSimState]):
    def __init__(
        self,
        sensor_rig: Optional[SensorRig] = None,
        agent_id: Optional[int] = None,
    ):
        step_agent = pd.state.SensorAgent(
            id=pd.state.rand_agent_id() if agent_id is None else agent_id, pose=np.eye(4), velocity=(0.0, 0.0, 0.0)
        )
        super().__init__(sensor_rig=sensor_rig, step_agent=step_agent)

    def _initialize_step_agent(self, random_seed: int) -> StepAgentType:
        sensors = list()
        if self.sensor_rig is not None:
            sensors.extend(self.sensor_rig.sensors)

        self.step_agent.sensors = [s.to_step_sensor() for s in sensors]

    def clone(self) -> "CustomSensorSimulationAgent[TSimState]":
        cloned = CustomSensorSimulationAgent(
            sensor_rig=self.sensor_rig.clone() if self.sensor_rig is not None else None,
        )
        if self._behavior is None:
            raise PdError(f"Missing behavior for {self.__class__.__name__}. Use `set_behavior()` to set a behavior.")
        cloned.set_behavior(behavior=self._behavior.clone())
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
        agent_id: Optional[int] = None,
    ):
        self.ground_offset = ground_offset
        self.lock_to_ground = lock_to_ground
        self._asset_name = asset_name
        self._asset_category = asset_category
        step_agent = pd.state.ModelAgent(
            asset_name=asset_name,
            id=pd.state.rand_agent_id() if agent_id is None else agent_id,
            pose=np.eye(4),
            velocity=(0.0, 0.0, 0.0),
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
            sensor_rig=self.sensor_rig.clone() if self.sensor_rig is not None else None,
            lock_to_ground=self.lock_to_ground,
            ground_offset=self.ground_offset,
            asset_name=self._asset_name,
            asset_category=self._asset_category,
            agent_id=self.agent_id,
        )
        if self._behavior is None:
            raise PdError(f"Missing behavior for {self.__class__.__name__}. Use `set_behavior()` to set a behavior.")
        cloned.set_behavior(behavior=self._behavior.clone())
        cloned.set_pose(self._pose)
        return cloned


class CustomSimulationAgents(Generic[TSimState]):
    @staticmethod
    def create_ego_pedestrian(
        sensor_rig: Optional[SensorRig] = None,
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent:
        return CustomPedestrianSimulationAgent(
            sensor_rig=sensor_rig,
            ground_offset=ground_offset,
            lock_to_ground=lock_to_ground,
            asset_name=asset_name,
            agent_id=agent_id,
        )

    @staticmethod
    def create_pedestrian(
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomPedestrianSimulationAgent(
            ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name, agent_id=agent_id
        )

    @staticmethod
    def create_object(
        sensor_rig: Optional[SensorRig] = None,
        asset_name: Optional[str] = None,
        asset_category: Optional[Literal["character", "vehicle", "traffic_control", "prop"]] = "traffic_control",
        lock_to_ground: bool = True,
        ground_offset=0.0,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomObjectSimulationAgent(
            ground_offset=ground_offset,
            lock_to_ground=lock_to_ground,
            asset_name=asset_name,
            asset_category=asset_category,
            sensor_rig=sensor_rig,
            agent_id=agent_id,
        )

    @staticmethod
    def create_ego_sensor(
        sensor_rig: SensorRig,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomSensorSimulationAgent(sensor_rig=sensor_rig, agent_id=agent_id)

    @staticmethod
    def create_ego_vehicle(
        sensor_rig: SensorRig,
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomVehicleSimulationAgent(
            sensor_rig=sensor_rig,
            ground_offset=ground_offset,
            lock_to_ground=lock_to_ground,
            asset_name=asset_name,
            agent_id=agent_id,
        )

    @staticmethod
    def create_vehicle(
        asset_name: Optional[str] = None,
        lock_to_ground: bool = True,
        ground_offset=0.0,
        agent_id: Optional[int] = None,
    ) -> CustomSimulationAgent[TSimState]:
        return CustomVehicleSimulationAgent(
            ground_offset=ground_offset, lock_to_ground=lock_to_ground, asset_name=asset_name, agent_id=agent_id
        )

    @staticmethod
    def get_asset_size(asset_name: str) -> Tuple[float, float, float]:
        assets = [i for i in ObjAssets.select().where(ObjAssets.name == asset_name)]
        if len(assets) == 0:
            logger.info(f"Could not find asset {asset_name} in database. Using default size (1,1,1)")
            return 1.0, 1.0, 1.0

        asset = assets[0]
        return asset.width, asset.length, asset.height
