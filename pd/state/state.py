# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Represents the state of the environment and all the agents

This set of dataclass wrappers provide an abstraction for representing the state of all
the agents and the environment within the system at a given time step.
The resultant :class:`State` object, can be passed to the :func:`pd.Session.update_state`
method in order to transmit the State information to the session.
For example::

    sensor_agent = pd.SensorAgent(
        id=1,
        pose=pd.Pose6D.from_rpy_angles(
            x_metres=100.0, y_metres=50.0, z_metres=300,
            roll_degrees=0.0, pitch_degrees=-90.0, yaw_degrees=9
        ),
        velocity=(0.0, 0.0, 0.0),
        sensors=[sensor]
    )
    world_info = pd.WorldInfo(
        location=location,
        time_of_day=lighting
    )
    state = pd.State(
        simulation_time_sec=world_time,
        world_info=world_info,
        agents=[sensor_agent]
    )
    session.update_state(state, world_time)
"""

from dataclasses import dataclass, field
from abc import ABC
from typing import List, Tuple, Optional, Union
from enum import Enum, auto, IntEnum
import uuid
import warnings

import numpy as np

from pd.state.pose6d import Pose6D
from pd.state.sensor import Sensor


def rand_agent_id() -> int:
    """
    Generates a random id for :class:`Agent`.

    Returns:
        Random id that can be used for an Agent
    """
    return uuid.uuid1().int >> 64


@dataclass
class Agent(ABC):
    """
    Basic data common to all agent types
    """

    id: int
    """Unique agent identifier, must be positive"""


@dataclass
class PosedAgent(ABC):
    """
    Agent with Pose information
    """

    pose: Union[Pose6D, np.ndarray]
    """
    Pose describing agent's position and orientation in world coordinate system

    Value must be a valid :class:`Pose6D` object or a 4x4 transformation matrix
    """

    velocity: Tuple[float, float, float]
    """Agent's velocity"""

    angular_velocity: Tuple[float, float, float] = field(default=(0., 0., 0.), init=False)
    """Agent's angular velocity"""


@dataclass
class SensorAgent(Agent, PosedAgent):
    """
    Agents with no physical representation in the world
    """

    sensors: List[Sensor] = field(default_factory=list)
    """List of sensors attached to this agent"""


@dataclass
class ModelAgent(Agent, PosedAgent):
    """
    Agents that have a physical model representing them in the world
    """

    asset_name: str
    """Name of the model asset"""

    lock_to_ground: bool = False
    """Whether to lock the model to the ground plane"""

    ground_offset: float = 0.0
    """Offset from the ground"""

    pedestrian_animation_data: Optional[str] = None
    """For internal use"""

    sensors: List[Sensor] = field(default_factory=list)
    """List of sensors attached to agent"""


class VehicleIndicatorState(IntEnum):
    """
    Enumerates logical states of a vehicle turn indicator
    """

    Inactive = 0
    Left = 1
    Right = 2
    Hazards = 3


@dataclass
class VehicleAgent(Agent, PosedAgent):
    """
    Agents that have a vehicle model representing them in the world
    """

    vehicle_type: str
    """Name of the vehicle model asset"""

    vehicle_color: Optional[str] = None
    """Color of the vehicle"""

    vehicle_accessory: Optional[str] = None
    """Accessories attached to the vehicle"""

    vehicle_wear: float = 0.0
    """Wear on the vehicle body"""

    vehicle_actor: Optional[str] = None
    """Deprecated: use occupants :attr:`occupants` instead"""

    wheel_type: Optional[str] = None
    """Type of wheel attached to the vehicle"""

    wheel_poses: List[Union[Pose6D, np.ndarray]] = field(default_factory=list)
    """
    Poses of the wheels attached to the vehicle

    Values must be a valid :class:`Pose6D` object or a 4x4 transformation matrix
    """

    lock_to_ground: bool = False
    """Whether to lock the model to the ground plane"""

    ground_offset: float = 0.0
    """Offset from the ground"""

    wheel_combo: List[str] = field(default_factory=list)
    """List of wheel combinations"""

    wheel_combo_style: List[str] = field(default_factory=list)
    """List of wheel combination styles"""

    accessories: List[str] = field(default_factory=list)
    """List of accessories"""

    occupants: List[str] = field(default_factory=list)
    """List of occupants"""

    brake_light_on: bool = False
    """Whether vehicle brake light is on"""

    indicator_state: VehicleIndicatorState = VehicleIndicatorState.Inactive
    """State of the vehicle's turn indicator"""

    is_parked: bool = False
    """Whether a vehicle is parked"""

    sensors: List[Sensor] = field(default_factory=list)
    """List of sensors attached to agent"""

    def __post_init__(self):
        if self.vehicle_actor is not None:
            warnings.warn("'vehicle_actor' property has been removed, use 'occupants' instead", stacklevel=2)


@dataclass
class SignalAgent(Agent):
    """
    Agents representing signals
    """

    elapsed_time: float = 0.0

    phase_bulb_values: List['PhaseBulbValue'] = field(default_factory=list)


class PhaseBulbLogicalState(IntEnum):
    """
    Enumerates logical states of a phase bulb
    """

    Inactive = 0
    Red = 1
    RedFlashing = 2
    Yellow = 3
    YellowFlashing = 4
    Green = 5
    GreenFlashing = 6


@dataclass
class PhaseBulbValue:
    """
    Represents state of a traffic light
    """

    phase: int = 0

    red: float = 0.0
    yellow: float = 0.0
    green: float = 0.0

    logical_state: PhaseBulbLogicalState = PhaseBulbLogicalState.Inactive


class PerformanceMode(Enum):
    """
    Enumerates available performance modes
    """

    HighFidelity = auto()
    """High-fidelty mode"""

    Performance = auto()
    """Performance mode"""


@dataclass
class WorldInfo:
    """
    Describes the world environment
    """

    location: Optional[str] = None
    """Currently unused in Step and Stream modes"""

    time_of_day: Optional[str] = None
    """Currently unused in Step and Stream modes"""

    wetness: float = 0.0
    """Value from [0,1] indicating current wetness of surfaces in environment"""

    rain_intensity: float = 0.0
    """Value from [0,1] indicating current level of rain in environment"""

    street_lights: float = 0.0
    """Value from [0,1] indicating current intensity of streetlights in environment"""

    fog_intensity: float = 0.0
    """Value from [0,1] indicating the current intensity of fog in the environment"""

    enable_headlights: bool = False
    """Whether vehicle headlights are active"""

    performance_mode: PerformanceMode = PerformanceMode.HighFidelity
    """Whether to enable to high performance rendering mode for performance sensitive applications"""

    anti_aliasing: int = 4
    """Anti-aliasing level"""


@dataclass
class State:
    """
    Holds the necessary information to define the state of the system at a particular timestamp
    """

    simulation_time_sec: float
    """
    Simulation time in seconds

    Successive states received by server must contain strictly increasing timestamps.
    Successive states with equal or decreasing timestamps will result in undefined behaviour.
    This restriction does not apply across level reloads.
    """

    world_info: WorldInfo
    """:class:`WorldInfo` object describing the world"""

    agents: List[Agent]
    """List of agents in the world"""

    capture: bool = True
    """For internal use"""
