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
from typing import List, Tuple, Optional, Union, Dict
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

    indicator_state: Union[VehicleIndicatorState, int] = VehicleIndicatorState.Inactive
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

    logical_state: Union[PhaseBulbLogicalState, int] = PhaseBulbLogicalState.Inactive


@dataclass
class WorldAgent(Agent):
    """
    Represents global information about the World
    """

    parking_config: Optional['ParkingConfig'] = None
    object_decorations: Dict[int, 'ObjectDecorations'] = field(default_factory=dict)


@dataclass
class DecorationPreset:
    preset_name: str
    variant: int


@dataclass
class ParkingSpaceDecal:
    decal_preset: str


@dataclass
class PaintTexture:
    color_rgb: Tuple[float, float, float]
    wear: float


class DecorationObjectType(IntEnum):
    Lane = 0


@dataclass
class ObjectDecorations:
    type: Union[DecorationObjectType, int]
    object_id: int
    decorations: Dict[int, Union[DecorationPreset, ParkingSpaceDecal, PaintTexture, str]]


class LotParkingDelineationType(IntEnum):
    Single = 0
    Dashed = 1
    DoubleOpen = 2
    DoubleSquared = 3
    DoubleRound = 4
    TShape = 5
    NoLine = 6
    Random = 7


class StreetParkingDelineationType(IntEnum):
    Single = 0
    Dashed = 1
    Double = 2
    DoubleOpen = 3
    DoubleSquared = 4
    DoubleRound = 5
    TShape = 6
    NoLine = 7
    Random = 8


class StreetParkingAngleZeroOverride(IntEnum):
    Single = 0
    Dashed = 1
    Double = 2
    DoubleOpen = 3
    DoubleSquared = 4
    DoubleRound = 5
    TShape = 6
    NoLine = 7
    Random = 8
    Unmetered = 9


class ParkingSpaceMaterial(IntEnum):
    MI_pavement_01 = 0
    MI_ParkingTiles_BrickBasket_01 = 1
    MI_ParkingTiles_BrickHerring_01 = 2
    MI_ParkingTiles_BrickHex_01 = 3
    MI_ParkingTiles_BrickOrnate_01 = 4
    MI_ParkingTiles_CobbleStone_01 = 5
    MI_ParkingTiles_CobbleStone_02 = 6
    MI_ParkingTiles_ConcreteBrick_01 = 7
    MI_ParkingTiles_ConcreteBrick_02 = 8
    MI_ParkingTiles_ConcreteBrick_03 = 9
    MI_ParkingTiles_ConcretePavers_01 = 10
    MI_ParkingTiles_StoneFlag_01 = 11


@dataclass
class ParkingConfig:

    angle: int
    """Angle of the parking spaces in degrees"""

    delineation_color: Tuple[float, float, float]
    """Parking line color"""

    delineation_wear_amount: float
    """Parking line wear between 0 and 1"""

    parking_space_tint: Tuple[float, float, float]
    """Tint applies to parking space material"""

    parking_space_grunge_amount: float
    """Grunge applied to parking space material, between 0 and 1"""

    lot_parking_delineation_type: Union[LotParkingDelineationType, int] = LotParkingDelineationType.Single
    """Parking lot line type"""

    street_parking_delineation_type: Union[StreetParkingDelineationType, int] = StreetParkingDelineationType.Single
    """Street parking line type"""

    street_parking_angle_zero_override: Union[StreetParkingAngleZeroOverride, int] = StreetParkingAngleZeroOverride.Single
    """Parallel street parking line type"""

    parking_space_material: Union[ParkingSpaceMaterial, int] = ParkingSpaceMaterial.MI_pavement_01
    """Material to show inside parking spaces"""


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

    scenario_seed: int = 0
    """For internal use only"""

    agent_tags: Dict[int, List[str]] = field(default_factory=dict)
    """Map of agent id to a list of tags"""


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
