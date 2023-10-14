from __future__ import annotations
from typing import List, Dict, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoEnumClass,
    AtomicGeneratorMessage,
    ProtoListWrapper,
    ProtoDictWrapper
)
from ..python import (
    pd_unified_generator_pb2
)
from . import (
    pd_distributions_pb2 as _pd_distributions_pb2,
    pd_types_pb2 as _pd_types_pb2
)


class AgentType(ProtoEnumClass):
    """Collection of currently supported agent types. Only :obj:`AgentType.VEHICLE` is currently supported."""

    UNSPECIFIED = 0
    "DEPRECATED"
    VEHICLE = 1
    "Vehicle that follows the road network with physical body movement."
    PARKED_VEHICLE = 2
    "DEPRECATED"
    TRAILER_VEHICLE = 3
    "DEPRECATED"
    PEDESTRIAN = 4
    "DEPRECATED"
    STATIC_OBJECT = 5
    "DEPRECATED"
    DRONE = 6
    "DEPRECATED"
    ANIMAL = 7
    "DEPRECATED"


class ObstacleType(ProtoEnumClass):
    """Enum containing different obstacle types."""

    ROUTE_LENGTH = 0
    REVERSE_DISTANCE = 1
    PATH_END = 2
    FORWARD_AGENT = 3
    ONCOMING_AGENT = 4
    END_OF_LANE = 5
    BLOCKED_LANE = 6
    MERGE = 7
    LINEAR_MOVER = 8
    LANE_CLOSURE = 9
    CROSSTRAFFIC = 10
    STOP_LINE = 11


class Gear(ProtoEnumClass):
    """Enum containing the different types of vehicle transmission gears."""

    PARKED = 1
    REVERSE = 2
    NEUTRAL = 3
    DRIVE = 4


class PedestrianBehavior(ProtoEnumClass):
    """Contains parameter that governs and controls pedestrian behavior."""

    NORMAL = 1
    "Behavior where pedestrian will walk on sidewalks/crosswalks and only cross roads at crosswalks.  Note than pedestrians will attempt to walk to a random position in the pedestrian lane on which they are located. Upon reaching this goal, another goal will be selected at random.  Pedestrians will attempt to walk only on pedestrians surfaces.  If a pedestrian is not placed on a pedestrian  surface, it will attempt to take a direct line to the nearest pedestrian surface.  Pedestrians will attempt to avoid static objects and be biased to walking in the center of pedestrian lanes."
    STATIC = 2
    "Behavior where pedestrian will stay in place at spawn location."
    JAYWALKER = 3
    "Behavior where pedestrian will exhibit jaywalking behavior (eg. cross the road at a non-crosswalk)."
    EDGESTOPPER = 4
    "Behavior where pedestrian will spawn on sidewalk, walk towards agent and stop at edge of sidewalk."


class SpecialAgentTag(ProtoEnumClass):
    """DEPRECATED"""

    EGO = 0
    STAR = 1


@register_wrapper(proto_type=pd_unified_generator_pb2.UnifiedGeneratorParameters)
class UnifiedGeneratorParameters(AtomicGeneratorMessage):
    """
    Wrapper which contains all parameters which that define scenario generation. Applied once per scenario.

    Args:
        atomics: :attr:`atomics`
        use_merge_batches: :attr:`use_merge_batches`
        default_params: :attr:`default_params`
        environment_params: :attr:`environment_params`
    Attributes:
        atomics: A list containing the atomic generators which will be applied to the scenario in scenario generation. At least
            one atomic generator is required for a scenario to be generated.
        use_merge_batches: Flag which specifies where multiple scenarios will be batched into one scenario for rendering efficiency.
            Default: False
        default_params: Field to allow defaults which apply across atomic generators to be overridden. If not provided, defaults within
            each atomic generator will be used.
        environment_params: Field to allow map parameters to be modified. If not provided, default values of each map will be used.
    """

    _proto_message = pd_unified_generator_pb2.UnifiedGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.UnifiedGeneratorParameters] = None,
        atomics: List[AtomicGeneratorParameters] = None,
        use_merge_batches: bool = None,
        default_params: DefaultAtomicGeneratorParameters = None,
        environment_params: EnvironmentParameters = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.UnifiedGeneratorParameters()
        self.proto = proto
        self._atomics = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.atomics],
            attr_name="atomics",
            list_owner=self,
        )
        self._default_params = get_wrapper(proto_type=proto.default_params.__class__)(proto=proto.default_params)
        self._environment_params = get_wrapper(proto_type=proto.environment_params.__class__)(
            proto=proto.environment_params
        )
        if atomics is not None:
            self.atomics = atomics
        if use_merge_batches is not None:
            self.use_merge_batches = use_merge_batches
        if default_params is not None:
            self.default_params = default_params
        if environment_params is not None:
            self.environment_params = environment_params

    @property
    def atomics(self) -> List[AtomicGeneratorParameters]:
        return self._atomics

    @atomics.setter
    def atomics(self, value: List[AtomicGeneratorParameters]):
        self._atomics.clear()
        for v in value:
            self._atomics.append(v)

    @property
    def use_merge_batches(self) -> bool:
        return self.proto.use_merge_batches

    @use_merge_batches.setter
    def use_merge_batches(self, value: bool):
        self.proto.use_merge_batches = value

    @property
    def default_params(self) -> DefaultAtomicGeneratorParameters:
        return self._default_params

    @default_params.setter
    def default_params(self, value: DefaultAtomicGeneratorParameters):
        self.proto.default_params.CopyFrom(value.proto)

        self._default_params = value
        self._default_params._update_proto_references(self.proto.default_params)

    @property
    def environment_params(self) -> EnvironmentParameters:
        return self._environment_params

    @environment_params.setter
    def environment_params(self, value: EnvironmentParameters):
        self.proto.environment_params.CopyFrom(value.proto)

        self._environment_params = value
        self._environment_params._update_proto_references(self.proto.environment_params)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.UnifiedGeneratorParameters):
        self.proto = proto
        for i, v in enumerate(self.atomics):
            v._update_proto_references(self.proto.atomics[i])
        self._default_params._update_proto_references(proto.default_params)
        self._environment_params._update_proto_references(proto.environment_params)


@register_wrapper(proto_type=pd_unified_generator_pb2.AtomicGeneratorParameters)
class AtomicGeneratorParameters(AtomicGeneratorMessage):
    """
    Parent type of each atomic generator

    Args:
        ego_agent: :attr:`ego_agent`
        vehicle: :attr:`vehicle`
        traffic: :attr:`traffic`
        parked_vehicles: :attr:`parked_vehicles`
        static_agent: :attr:`static_agent`
        debris: :attr:`debris`
        pedestrian: :attr:`pedestrian`
        random_pedestrian: :attr:`random_pedestrian`
        drone: :attr:`drone`
    Attributes:
        ego_agent:
        vehicle:
        traffic:
        parked_vehicles:
        static_agent:
        debris:
        pedestrian:
        random_pedestrian:
        drone:"""

    _proto_message = pd_unified_generator_pb2.AtomicGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.AtomicGeneratorParameters] = None,
        ego_agent: EgoAgentGeneratorParameters = None,
        vehicle: VehicleGeneratorParameters = None,
        traffic: TrafficGeneratorParameters = None,
        parked_vehicles: ParkedVehicleGeneratorParameters = None,
        static_agent: StaticAgentGeneratorParameters = None,
        debris: DebrisGeneratorParameters = None,
        pedestrian: PedestrianGeneratorParameters = None,
        random_pedestrian: RandomPedestrianGeneratorParameters = None,
        drone: DroneGeneratorParameters = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.AtomicGeneratorParameters()
        self.proto = proto
        self._ego_agent = get_wrapper(proto_type=proto.ego_agent.__class__)(proto=proto.ego_agent)
        self._vehicle = get_wrapper(proto_type=proto.vehicle.__class__)(proto=proto.vehicle)
        self._traffic = get_wrapper(proto_type=proto.traffic.__class__)(proto=proto.traffic)
        self._parked_vehicles = get_wrapper(proto_type=proto.parked_vehicles.__class__)(proto=proto.parked_vehicles)
        self._static_agent = get_wrapper(proto_type=proto.static_agent.__class__)(proto=proto.static_agent)
        self._debris = get_wrapper(proto_type=proto.debris.__class__)(proto=proto.debris)
        self._pedestrian = get_wrapper(proto_type=proto.pedestrian.__class__)(proto=proto.pedestrian)
        self._random_pedestrian = get_wrapper(proto_type=proto.random_pedestrian.__class__)(
            proto=proto.random_pedestrian
        )
        self._drone = get_wrapper(proto_type=proto.drone.__class__)(proto=proto.drone)
        if ego_agent is not None:
            self.ego_agent = ego_agent
        if vehicle is not None:
            self.vehicle = vehicle
        if traffic is not None:
            self.traffic = traffic
        if parked_vehicles is not None:
            self.parked_vehicles = parked_vehicles
        if static_agent is not None:
            self.static_agent = static_agent
        if debris is not None:
            self.debris = debris
        if pedestrian is not None:
            self.pedestrian = pedestrian
        if random_pedestrian is not None:
            self.random_pedestrian = random_pedestrian
        if drone is not None:
            self.drone = drone

    @property
    def ego_agent(self) -> EgoAgentGeneratorParameters:
        return self._ego_agent

    @ego_agent.setter
    def ego_agent(self, value: EgoAgentGeneratorParameters):
        self.proto.ego_agent.CopyFrom(value.proto)

        self._ego_agent = value
        self._ego_agent._update_proto_references(self.proto.ego_agent)

    @property
    def vehicle(self) -> VehicleGeneratorParameters:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: VehicleGeneratorParameters):
        self.proto.vehicle.CopyFrom(value.proto)

        self._vehicle = value
        self._vehicle._update_proto_references(self.proto.vehicle)

    @property
    def traffic(self) -> TrafficGeneratorParameters:
        return self._traffic

    @traffic.setter
    def traffic(self, value: TrafficGeneratorParameters):
        self.proto.traffic.CopyFrom(value.proto)

        self._traffic = value
        self._traffic._update_proto_references(self.proto.traffic)

    @property
    def parked_vehicles(self) -> ParkedVehicleGeneratorParameters:
        return self._parked_vehicles

    @parked_vehicles.setter
    def parked_vehicles(self, value: ParkedVehicleGeneratorParameters):
        self.proto.parked_vehicles.CopyFrom(value.proto)

        self._parked_vehicles = value
        self._parked_vehicles._update_proto_references(self.proto.parked_vehicles)

    @property
    def static_agent(self) -> StaticAgentGeneratorParameters:
        return self._static_agent

    @static_agent.setter
    def static_agent(self, value: StaticAgentGeneratorParameters):
        self.proto.static_agent.CopyFrom(value.proto)

        self._static_agent = value
        self._static_agent._update_proto_references(self.proto.static_agent)

    @property
    def debris(self) -> DebrisGeneratorParameters:
        return self._debris

    @debris.setter
    def debris(self, value: DebrisGeneratorParameters):
        self.proto.debris.CopyFrom(value.proto)

        self._debris = value
        self._debris._update_proto_references(self.proto.debris)

    @property
    def pedestrian(self) -> PedestrianGeneratorParameters:
        return self._pedestrian

    @pedestrian.setter
    def pedestrian(self, value: PedestrianGeneratorParameters):
        self.proto.pedestrian.CopyFrom(value.proto)

        self._pedestrian = value
        self._pedestrian._update_proto_references(self.proto.pedestrian)

    @property
    def random_pedestrian(self) -> RandomPedestrianGeneratorParameters:
        return self._random_pedestrian

    @random_pedestrian.setter
    def random_pedestrian(self, value: RandomPedestrianGeneratorParameters):
        self.proto.random_pedestrian.CopyFrom(value.proto)

        self._random_pedestrian = value
        self._random_pedestrian._update_proto_references(self.proto.random_pedestrian)

    @property
    def drone(self) -> DroneGeneratorParameters:
        return self._drone

    @drone.setter
    def drone(self, value: DroneGeneratorParameters):
        self.proto.drone.CopyFrom(value.proto)

        self._drone = value
        self._drone._update_proto_references(self.proto.drone)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.AtomicGeneratorParameters):
        self.proto = proto
        self._ego_agent._update_proto_references(proto.ego_agent)
        self._vehicle._update_proto_references(proto.vehicle)
        self._traffic._update_proto_references(proto.traffic)
        self._parked_vehicles._update_proto_references(proto.parked_vehicles)
        self._static_agent._update_proto_references(proto.static_agent)
        self._debris._update_proto_references(proto.debris)
        self._pedestrian._update_proto_references(proto.pedestrian)
        self._random_pedestrian._update_proto_references(proto.random_pedestrian)
        self._drone._update_proto_references(proto.drone)


@register_wrapper(proto_type=pd_unified_generator_pb2.DefaultAtomicGeneratorParameters)
class DefaultAtomicGeneratorParameters(AtomicGeneratorMessage):
    """
    Contains default parameters applied to all atomics specified within :obj:`UnifiedGeneratorParameters`.

    Args:
        vehicle_distribution: :attr:`vehicle_distribution`
    Attributes:
        vehicle_distribution:"""

    _proto_message = pd_unified_generator_pb2.DefaultAtomicGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DefaultAtomicGeneratorParameters] = None,
        vehicle_distribution: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight] = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DefaultAtomicGeneratorParameters()
        self.proto = proto
        self._vehicle_distribution = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()
            },
            attr_name="vehicle_distribution",
            dict_owner=self,
        )
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DefaultAtomicGeneratorParameters):
        self.proto = proto
        for k, v in self.vehicle_distribution.items():
            v._update_proto_references(self.proto.vehicle_distribution[k])


@register_wrapper(proto_type=pd_unified_generator_pb2.EnvironmentParameters)
class EnvironmentParameters(ProtoMessageClass):
    """
    Parameters that modify map level attributes.

    Args:
        sign_spawn_probability: :attr:`sign_spawn_probability`
        crosswalk_sign_spawn_probability: :attr:`crosswalk_sign_spawn_probability`
        marker_data_map: :attr:`marker_data_map`
        region: :attr:`region`
        parking_space_data: :attr:`parking_space_data`
    Attributes:
        sign_spawn_probability: Specifies the spawn probability of signs on  maps that begin with 'SIGNAGE_'. Must be a sit within 0.0 to 1.0. If
            not provided, will default to 0.
        crosswalk_sign_spawn_probability: Probability of spawning crosswalk signs in crosswalk signs location in or near crosswalks on maps that begin with
            'SIGNAGE_'. Must be a sit within 0.0 to 1.0. If not provided, will default to 0.
        marker_data_map: Specifies road markings types across the map. If not provided, will default to the values below.

            Default values::

                "parking_spot_config"     {marker_type = MI_pavement_01, rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
                "parking_lot_marker"      {marker_type = "DOUBLE_SQUARE", rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
                "parallel_parking_marker" {rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
        region: Specifies the countries from which road signs should be spawned on ISA maps. If not provided, will use default
            values.

            Available options::

                "Austria"
                "Belgium"
                "Bulgaria"
                "Croatia"
                "Cyprus"
                "Czechia"
                "Denmark"
                "Estonia"
                "Finland"
                "France"
                "Germany"
                "Greece"
                "Hungary"
                "Ireland"
                "Italy"
                "Latvia"
                "Lithuania"
                "Luxembourg"
                "Malta"
                "Netherlands"
                "Norway"
                "Poland"
                "Portugal"
                "Romania"
                "Slovakia"
                "Slovenia"
                "Spain"
                "Sweden"
                "Switzerland"
        parking_space_data: Parameters which control the placement of parking spaces on maps. If not specified, will use defaults.
    """

    _proto_message = pd_unified_generator_pb2.EnvironmentParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.EnvironmentParameters] = None,
        sign_spawn_probability: CenterSpreadConfig = None,
        crosswalk_sign_spawn_probability: CenterSpreadConfig = None,
        marker_data_map: Dict[str, RoadMarkingData] = None,
        region: _pd_distributions_pb2.EnumDistribution = None,
        parking_space_data: ParkingSpaceData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.EnvironmentParameters()
        self.proto = proto
        self._sign_spawn_probability = get_wrapper(proto_type=proto.sign_spawn_probability.__class__)(
            proto=proto.sign_spawn_probability
        )
        self._crosswalk_sign_spawn_probability = get_wrapper(
            proto_type=proto.crosswalk_sign_spawn_probability.__class__
        )(proto=proto.crosswalk_sign_spawn_probability)
        self._marker_data_map = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.marker_data_map.items()},
            attr_name="marker_data_map",
            dict_owner=self,
        )
        self._region = get_wrapper(proto_type=proto.region.__class__)(proto=proto.region)
        self._parking_space_data = get_wrapper(proto_type=proto.parking_space_data.__class__)(
            proto=proto.parking_space_data
        )
        if sign_spawn_probability is not None:
            self.sign_spawn_probability = sign_spawn_probability
        if crosswalk_sign_spawn_probability is not None:
            self.crosswalk_sign_spawn_probability = crosswalk_sign_spawn_probability
        if marker_data_map is not None:
            self.marker_data_map = marker_data_map
        if region is not None:
            self.region = region
        if parking_space_data is not None:
            self.parking_space_data = parking_space_data

    @property
    def sign_spawn_probability(self) -> CenterSpreadConfig:
        return self._sign_spawn_probability

    @sign_spawn_probability.setter
    def sign_spawn_probability(self, value: CenterSpreadConfig):
        self.proto.sign_spawn_probability.CopyFrom(value.proto)

        self._sign_spawn_probability = value
        self._sign_spawn_probability._update_proto_references(self.proto.sign_spawn_probability)

    @property
    def crosswalk_sign_spawn_probability(self) -> CenterSpreadConfig:
        return self._crosswalk_sign_spawn_probability

    @crosswalk_sign_spawn_probability.setter
    def crosswalk_sign_spawn_probability(self, value: CenterSpreadConfig):
        self.proto.crosswalk_sign_spawn_probability.CopyFrom(value.proto)

        self._crosswalk_sign_spawn_probability = value
        self._crosswalk_sign_spawn_probability._update_proto_references(self.proto.crosswalk_sign_spawn_probability)

    @property
    def marker_data_map(self) -> Dict[str, RoadMarkingData]:
        return self._marker_data_map

    @marker_data_map.setter
    def marker_data_map(self, value: Dict[str, RoadMarkingData]):
        self._marker_data_map.clear()
        self._marker_data_map.update(value)

    @property
    def region(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._region

    @region.setter
    def region(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.region.CopyFrom(value.proto)

        self._region = value
        self._region._update_proto_references(self.proto.region)

    @property
    def parking_space_data(self) -> ParkingSpaceData:
        return self._parking_space_data

    @parking_space_data.setter
    def parking_space_data(self, value: ParkingSpaceData):
        self.proto.parking_space_data.CopyFrom(value.proto)

        self._parking_space_data = value
        self._parking_space_data._update_proto_references(self.proto.parking_space_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.EnvironmentParameters):
        self.proto = proto
        self._sign_spawn_probability._update_proto_references(proto.sign_spawn_probability)
        self._crosswalk_sign_spawn_probability._update_proto_references(proto.crosswalk_sign_spawn_probability)
        for k, v in self.marker_data_map.items():
            v._update_proto_references(self.proto.marker_data_map[k])
        self._region._update_proto_references(proto.region)
        self._parking_space_data._update_proto_references(proto.parking_space_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.ParkingSpaceData)
class ParkingSpaceData(ProtoMessageClass):
    """
    Parameters that configure parking space placement on maps.

    Args:
        parking_lot_angle_distribution: :attr:`parking_lot_angle_distribution`
        lot_parking_delineation_type: :attr:`lot_parking_delineation_type`
        street_parking_delineation_type: :attr:`street_parking_delineation_type`
        street_parking_angle_zero_override: :attr:`street_parking_angle_zero_override`
        delineation_color: :attr:`delineation_color`
        delineation_wear_amount: :attr:`delineation_wear_amount`
        parking_space_material: :attr:`parking_space_material`
        parking_space_tint: :attr:`parking_space_tint`
        parking_space_grunge_amount: :attr:`parking_space_grunge_amount`
        global_parking_decal_wear: :attr:`global_parking_decal_wear`
        parking_space_decoration: :attr:`parking_space_decoration`
    Attributes:
        parking_lot_angle_distribution: Desired parking space angle for parking lots in degrees and its associated probability. Does not apply to street
            parking spaces. If not provided, will use defaults.

            Valid angles are::

                "ANGLE_30"
                "ANGLE_45"
                "ANGLE_60"
                "PERPENDICULAR"
        lot_parking_delineation_type: Specifies delineation type for parking lot spaces and its associated probability. If not provided, will use defaults.

            Valid values::

                "SINGLE_DASHED"
                "DOUBLE_OPEN"
                "DOUBLE_SQUARED"
                "DOUBLE_ROUND"
                "T_SHAPE"
                "NO_LINE"
                "BOX_CLOSED"
                "BOX_OPEN_CURB"
                "BOX_DOUBLE"
                "SINGLE_SQUARED_OPEN_CURB"
                "DOUBLE_ROUND_50CM_GAP"
                "DOUBLE_ROUND_50CM_GAP_OPEN_CURB"
                "DOUBLE_SQUARED_50CM_GAP_OPEN_CURB"
                "T_FULL"
                "T_SHORT"
        street_parking_delineation_type: Specifies delineation type for non parallel street parking spaces. If not provided, will use default value of
            `SINGLE`.

            Valid values::

                "SINGLE"
                "DASHED"
                "DOUBLE_OPEN"
                "DOUBLE_SQUARED"
                "DOUBLE_ROUND"
                "T_SHAPE"
                "NO_LINE"
                "BOX_CLOSED"
                "BOX_OPEN_CURB"
                "BOX_DOUBLE"
                "SINGLE_SQUARED_OPEN_CURB"
                "DOUBLE_ROUND_50CM_GAP"
                "DOUBLE_ROUND_50CM_GAP_OPEN_CURB"
                "DOUBLE_SQUARED_50CM_GAP_OPEN_CURB"
                "T_FULL"
                "T_SHORT"
        street_parking_angle_zero_override: Specifies delineation type for parallel street parking spaces. If not provided, will use default value selected in
            :obj:`street_parking_delineation_type`.

            Valid values::

                "SINGLE"
                "DASHED"
                "DOUBLE_OPEN"
                "DOUBLE_SQUARED"
                "DOUBLE_ROUND"
                "T_SHAPE"
                "NO_LINE"
                "UNMETERED"
                "BOX_CLOSED"
                "BOX_OPEN_CURB"
                "BOX_DOUBLE"
                "SINGLE_SQUARED_OPEN_CURB"
                "DOUBLE_ROUND_50CM_GAP"
                "DOUBLE_ROUND_50CM_GAP_OPEN_CURB"
                "DOUBLE_SQUARED_50CM_GAP_OPEN_CURB"
                "T_FULL"
                "T_SHORT"
        delineation_color: Specifies the color of all parking lines in RGB format. If not provided, will default to white.
        delineation_wear_amount: Specifies the level of wear on all parking slot lines. A value of 0.0 is fully unworn and 1.0 is fully worn.
            If not provided, will use value of 0.25.
        parking_space_material: The type of parking slot ground material which should be applied to the map, and their associated probability values.
            If not provided, defaults to `MI_pavement_01`.

            Valid Values::

                "MI_pavement_01"
                "MI_ParkingTiles_BrickBasket_01"
                "MI_ParkingTiles_BrickHerring_01"
                "MI_ParkingTiles_BrickHex_01"
                "MI_ParkingTiles_BrickOrnate_01"
                "MI_ParkingTiles_CobbleStone_01"
                "MI_ParkingTiles_CobbleStone_02"
                "MI_ParkingTiles_ConcreteBrick_01"
                "MI_ParkingTiles_ConcreteBrick_02"
                "MI_ParkingTiles_ConcreteBrick_03"
                "MI_ParkingTiles_ConcretePavers_01"
                "MI_ParkingTiles_StoneFlag_01"
        parking_space_tint: Specifies the tint of all parking slot surfaces in RGB format. If not provided, will default to un-tinted.
        parking_space_grunge_amount: Specifies the level of grunge applied to all parking slot surfaces. A value of 0.0 is free of grunge and 1.0 applies
            maximum grunge to parking slots.        If not provided, will use value of 0.25.
        global_parking_decal_wear: Specifies the level of wear on all parking slot decals. A value of 0.0 is fully unworn and 1.0 is fully worn.
            If not provided, will use value of 0.25.
        parking_space_decoration: Parameter that specifies the types and probabilities of decals that should be applied to parking slots.
    """

    _proto_message = pd_unified_generator_pb2.ParkingSpaceData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.ParkingSpaceData] = None,
        parking_lot_angle_distribution: _pd_distributions_pb2.EnumDistribution = None,
        lot_parking_delineation_type: _pd_distributions_pb2.EnumDistribution = None,
        street_parking_delineation_type: _pd_distributions_pb2.EnumDistribution = None,
        street_parking_angle_zero_override: _pd_distributions_pb2.EnumDistribution = None,
        delineation_color: List[_pd_types_pb2.Float3] = None,
        delineation_wear_amount: CenterSpreadConfig = None,
        parking_space_material: _pd_distributions_pb2.EnumDistribution = None,
        parking_space_tint: List[_pd_types_pb2.Float3] = None,
        parking_space_grunge_amount: CenterSpreadConfig = None,
        global_parking_decal_wear: CenterSpreadConfig = None,
        parking_space_decoration: ObjectDecorationParams = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.ParkingSpaceData()
        self.proto = proto
        self._parking_lot_angle_distribution = get_wrapper(proto_type=proto.parking_lot_angle_distribution.__class__)(
            proto=proto.parking_lot_angle_distribution
        )
        self._lot_parking_delineation_type = get_wrapper(proto_type=proto.lot_parking_delineation_type.__class__)(
            proto=proto.lot_parking_delineation_type
        )
        self._street_parking_delineation_type = get_wrapper(proto_type=proto.street_parking_delineation_type.__class__)(
            proto=proto.street_parking_delineation_type
        )
        self._street_parking_angle_zero_override = get_wrapper(
            proto_type=proto.street_parking_angle_zero_override.__class__
        )(proto=proto.street_parking_angle_zero_override)
        self._delineation_color = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.delineation_color],
            attr_name="delineation_color",
            list_owner=self,
        )
        self._delineation_wear_amount = get_wrapper(proto_type=proto.delineation_wear_amount.__class__)(
            proto=proto.delineation_wear_amount
        )
        self._parking_space_material = get_wrapper(proto_type=proto.parking_space_material.__class__)(
            proto=proto.parking_space_material
        )
        self._parking_space_tint = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.parking_space_tint],
            attr_name="parking_space_tint",
            list_owner=self,
        )
        self._parking_space_grunge_amount = get_wrapper(proto_type=proto.parking_space_grunge_amount.__class__)(
            proto=proto.parking_space_grunge_amount
        )
        self._global_parking_decal_wear = get_wrapper(proto_type=proto.global_parking_decal_wear.__class__)(
            proto=proto.global_parking_decal_wear
        )
        self._parking_space_decoration = get_wrapper(proto_type=proto.parking_space_decoration.__class__)(
            proto=proto.parking_space_decoration
        )
        if parking_lot_angle_distribution is not None:
            self.parking_lot_angle_distribution = parking_lot_angle_distribution
        if lot_parking_delineation_type is not None:
            self.lot_parking_delineation_type = lot_parking_delineation_type
        if street_parking_delineation_type is not None:
            self.street_parking_delineation_type = street_parking_delineation_type
        if street_parking_angle_zero_override is not None:
            self.street_parking_angle_zero_override = street_parking_angle_zero_override
        if delineation_color is not None:
            self.delineation_color = delineation_color
        if delineation_wear_amount is not None:
            self.delineation_wear_amount = delineation_wear_amount
        if parking_space_material is not None:
            self.parking_space_material = parking_space_material
        if parking_space_tint is not None:
            self.parking_space_tint = parking_space_tint
        if parking_space_grunge_amount is not None:
            self.parking_space_grunge_amount = parking_space_grunge_amount
        if global_parking_decal_wear is not None:
            self.global_parking_decal_wear = global_parking_decal_wear
        if parking_space_decoration is not None:
            self.parking_space_decoration = parking_space_decoration

    @property
    def parking_lot_angle_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._parking_lot_angle_distribution

    @parking_lot_angle_distribution.setter
    def parking_lot_angle_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.parking_lot_angle_distribution.CopyFrom(value.proto)

        self._parking_lot_angle_distribution = value
        self._parking_lot_angle_distribution._update_proto_references(self.proto.parking_lot_angle_distribution)

    @property
    def lot_parking_delineation_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._lot_parking_delineation_type

    @lot_parking_delineation_type.setter
    def lot_parking_delineation_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.lot_parking_delineation_type.CopyFrom(value.proto)

        self._lot_parking_delineation_type = value
        self._lot_parking_delineation_type._update_proto_references(self.proto.lot_parking_delineation_type)

    @property
    def street_parking_delineation_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._street_parking_delineation_type

    @street_parking_delineation_type.setter
    def street_parking_delineation_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.street_parking_delineation_type.CopyFrom(value.proto)

        self._street_parking_delineation_type = value
        self._street_parking_delineation_type._update_proto_references(self.proto.street_parking_delineation_type)

    @property
    def street_parking_angle_zero_override(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._street_parking_angle_zero_override

    @street_parking_angle_zero_override.setter
    def street_parking_angle_zero_override(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.street_parking_angle_zero_override.CopyFrom(value.proto)

        self._street_parking_angle_zero_override = value
        self._street_parking_angle_zero_override._update_proto_references(self.proto.street_parking_angle_zero_override)

    @property
    def delineation_color(self) -> List[_pd_types_pb2.Float3]:
        return self._delineation_color

    @delineation_color.setter
    def delineation_color(self, value: List[_pd_types_pb2.Float3]):
        self._delineation_color.clear()
        for v in value:
            self._delineation_color.append(v)

    @property
    def delineation_wear_amount(self) -> CenterSpreadConfig:
        return self._delineation_wear_amount

    @delineation_wear_amount.setter
    def delineation_wear_amount(self, value: CenterSpreadConfig):
        self.proto.delineation_wear_amount.CopyFrom(value.proto)

        self._delineation_wear_amount = value
        self._delineation_wear_amount._update_proto_references(self.proto.delineation_wear_amount)

    @property
    def parking_space_material(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._parking_space_material

    @parking_space_material.setter
    def parking_space_material(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.parking_space_material.CopyFrom(value.proto)

        self._parking_space_material = value
        self._parking_space_material._update_proto_references(self.proto.parking_space_material)

    @property
    def parking_space_tint(self) -> List[_pd_types_pb2.Float3]:
        return self._parking_space_tint

    @parking_space_tint.setter
    def parking_space_tint(self, value: List[_pd_types_pb2.Float3]):
        self._parking_space_tint.clear()
        for v in value:
            self._parking_space_tint.append(v)

    @property
    def parking_space_grunge_amount(self) -> CenterSpreadConfig:
        return self._parking_space_grunge_amount

    @parking_space_grunge_amount.setter
    def parking_space_grunge_amount(self, value: CenterSpreadConfig):
        self.proto.parking_space_grunge_amount.CopyFrom(value.proto)

        self._parking_space_grunge_amount = value
        self._parking_space_grunge_amount._update_proto_references(self.proto.parking_space_grunge_amount)

    @property
    def global_parking_decal_wear(self) -> CenterSpreadConfig:
        return self._global_parking_decal_wear

    @global_parking_decal_wear.setter
    def global_parking_decal_wear(self, value: CenterSpreadConfig):
        self.proto.global_parking_decal_wear.CopyFrom(value.proto)

        self._global_parking_decal_wear = value
        self._global_parking_decal_wear._update_proto_references(self.proto.global_parking_decal_wear)

    @property
    def parking_space_decoration(self) -> ObjectDecorationParams:
        return self._parking_space_decoration

    @parking_space_decoration.setter
    def parking_space_decoration(self, value: ObjectDecorationParams):
        self.proto.parking_space_decoration.CopyFrom(value.proto)

        self._parking_space_decoration = value
        self._parking_space_decoration._update_proto_references(self.proto.parking_space_decoration)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.ParkingSpaceData):
        self.proto = proto
        self._parking_lot_angle_distribution._update_proto_references(proto.parking_lot_angle_distribution)
        self._lot_parking_delineation_type._update_proto_references(proto.lot_parking_delineation_type)
        self._street_parking_delineation_type._update_proto_references(proto.street_parking_delineation_type)
        self._street_parking_angle_zero_override._update_proto_references(proto.street_parking_angle_zero_override)
        for i, v in enumerate(self.delineation_color):
            v._update_proto_references(self.proto.delineation_color[i])
        self._delineation_wear_amount._update_proto_references(proto.delineation_wear_amount)
        self._parking_space_material._update_proto_references(proto.parking_space_material)
        for i, v in enumerate(self.parking_space_tint):
            v._update_proto_references(self.proto.parking_space_tint[i])
        self._parking_space_grunge_amount._update_proto_references(proto.parking_space_grunge_amount)
        self._global_parking_decal_wear._update_proto_references(proto.global_parking_decal_wear)
        self._parking_space_decoration._update_proto_references(proto.parking_space_decoration)


@register_wrapper(proto_type=pd_unified_generator_pb2.RoadMarkingData)
class RoadMarkingData(ProtoMessageClass):
    """
    Parameters which specify the appearance of road markings on the map.

    Args:
        use_preset: :attr:`use_preset`
        override_colors: :attr:`override_colors`
        preset_colors: :attr:`preset_colors`
        marker_types: :attr:`marker_types`
        wear: :attr:`wear`
    Attributes:
        use_preset: Flag to specify whether to use default RGB values. Not yet implemented.
            Default: False
        override_colors: Specify an RGB value (each channel from 0.0 to 1.0) for all road markings in the map. If not provided, will use
            default values.
        preset_colors: Specifies which colors in the asset registry to use for road markings used if :attr:`use_preset` is set to `True`.
            Not yet implemented, will currently have no effect.
        marker_types: Specifies a marker name, and corresponds to the key as listed in :obj:`marker_data_map`. If not provided, will use
            default values in :obj:`marker_data_map`.

            Valid values::

                "Single"
                "Dashed"
                "Double Open"
                "Double Squared"
                "Double Round"
                "T"
                "MI_pavement_01"
                "MI_ParkingTiles_BrickBasket_01"
                "MI_ParkingTiles_BrickHerring_01"
                "MI_ParkingTiles_BrickHex_01"
                "MI_ParkingTiles_BrickOrnate_01"
                "MI_ParkingTiles_CobbleStone_01"
                "MI_ParkingTiles_CobbleStone_02"
                "MI_ParkingTiles_ConcreteBrick_01"
                "MI_ParkingTiles_ConcreteBrick_02"
                "MI_ParkingTiles_ConcreteBrick_03"
                "MI_ParkingTiles_ConcretePavers_01"
                "MI_ParkingTiles_StoneFlag_01
        wear: Specifies the level of wear applied to road markings. Ranges from 0.0 to 1.0 where 0.0 is fully unworn and 1.0 is
            fully worn. If not provided, will default to 0.0."""

    _proto_message = pd_unified_generator_pb2.RoadMarkingData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.RoadMarkingData] = None,
        use_preset: bool = None,
        override_colors: List[FloatArray] = None,
        preset_colors: List[str] = None,
        marker_types: List[str] = None,
        wear: CenterSpreadConfig = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.RoadMarkingData()
        self.proto = proto
        self._override_colors = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.override_colors],
            attr_name="override_colors",
            list_owner=self,
        )
        self._wear = get_wrapper(proto_type=proto.wear.__class__)(proto=proto.wear)
        if use_preset is not None:
            self.use_preset = use_preset
        if override_colors is not None:
            self.override_colors = override_colors
        self._preset_colors = ProtoListWrapper(
            container=[str(v) for v in proto.preset_colors], attr_name="preset_colors", list_owner=self
        )
        if preset_colors is not None:
            self.preset_colors = preset_colors
        self._marker_types = ProtoListWrapper(
            container=[str(v) for v in proto.marker_types], attr_name="marker_types", list_owner=self
        )
        if marker_types is not None:
            self.marker_types = marker_types
        if wear is not None:
            self.wear = wear

    @property
    def use_preset(self) -> bool:
        return self.proto.use_preset

    @use_preset.setter
    def use_preset(self, value: bool):
        self.proto.use_preset = value

    @property
    def override_colors(self) -> List[FloatArray]:
        return self._override_colors

    @override_colors.setter
    def override_colors(self, value: List[FloatArray]):
        self._override_colors.clear()
        for v in value:
            self._override_colors.append(v)

    @property
    def preset_colors(self) -> List[str]:
        return self._preset_colors

    @preset_colors.setter
    def preset_colors(self, value: List[str]):
        self._preset_colors.clear()
        for v in value:
            self._preset_colors.append(v)

    @property
    def marker_types(self) -> List[str]:
        return self._marker_types

    @marker_types.setter
    def marker_types(self, value: List[str]):
        self._marker_types.clear()
        for v in value:
            self._marker_types.append(v)

    @property
    def wear(self) -> CenterSpreadConfig:
        return self._wear

    @wear.setter
    def wear(self, value: CenterSpreadConfig):
        self.proto.wear.CopyFrom(value.proto)

        self._wear = value
        self._wear._update_proto_references(self.proto.wear)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.RoadMarkingData):
        self.proto = proto
        for i, v in enumerate(self.override_colors):
            v._update_proto_references(self.proto.override_colors[i])
        self._wear._update_proto_references(proto.wear)


@register_wrapper(proto_type=pd_unified_generator_pb2.DecorationPreset)
class DecorationPreset(ProtoMessageClass):
    """
    Specifies the name of a parking slot decal decoration to be applied.

    Args:
        preset_name: :attr:`preset_name`
        variant: :attr:`variant`
    Attributes:
        preset_name: The name of the parking slot decal decoration. Must be provided.
        variant: Specifies which variant of the parking slot decal decoration should be used.
            Default: 0"""

    _proto_message = pd_unified_generator_pb2.DecorationPreset

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DecorationPreset] = None,
        preset_name: str = None,
        variant: int = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DecorationPreset()
        self.proto = proto
        if preset_name is not None:
            self.preset_name = preset_name
        if variant is not None:
            self.variant = variant

    @property
    def preset_name(self) -> str:
        return self.proto.preset_name

    @preset_name.setter
    def preset_name(self, value: str):
        self.proto.preset_name = value

    @property
    def variant(self) -> int:
        return self.proto.variant

    @variant.setter
    def variant(self, value: int):
        self.proto.variant = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DecorationPreset):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.DecorationData)
class DecorationData(ProtoMessageClass):
    """
    Metadata of parking slot decal decorations.

    Args:
        decoration_preset: :attr:`decoration_preset`
    Attributes:
        decoration_preset:"""

    _proto_message = pd_unified_generator_pb2.DecorationData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DecorationData] = None,
        decoration_preset: DecorationPreset = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DecorationData()
        self.proto = proto
        self._decoration_preset = get_wrapper(proto_type=proto.decoration_preset.__class__)(
            proto=proto.decoration_preset
        )
        if decoration_preset is not None:
            self.decoration_preset = decoration_preset

    @property
    def decoration_preset(self) -> DecorationPreset:
        return self._decoration_preset

    @decoration_preset.setter
    def decoration_preset(self, value: DecorationPreset):
        self.proto.decoration_preset.CopyFrom(value.proto)

        self._decoration_preset = value
        self._decoration_preset._update_proto_references(self.proto.decoration_preset)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DecorationData):
        self.proto = proto
        self._decoration_preset._update_proto_references(proto.decoration_preset)


@register_wrapper(proto_type=pd_unified_generator_pb2.ObjectDecorations)
class ObjectDecorations(ProtoMessageClass):
    """
    Message which specifies the link between an object in the world and the decoration that is applied to it (eg. a parking
    slot decal decoration).

    Args:
        object_id: :attr:`object_id`
        decoration_data: :attr:`decoration_data`
    Attributes:
        object_id: The id of the object to which the decoration should be applied.
        decoration_data: Parameters specifying the decoration which should be applied to the object."""

    _proto_message = pd_unified_generator_pb2.ObjectDecorations

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.ObjectDecorations] = None,
        object_id: int = None,
        decoration_data: DecorationData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.ObjectDecorations()
        self.proto = proto
        self._decoration_data = get_wrapper(proto_type=proto.decoration_data.__class__)(proto=proto.decoration_data)
        if object_id is not None:
            self.object_id = object_id
        if decoration_data is not None:
            self.decoration_data = decoration_data

    @property
    def object_id(self) -> int:
        return self.proto.object_id

    @object_id.setter
    def object_id(self, value: int):
        self.proto.object_id = value

    @property
    def decoration_data(self) -> DecorationData:
        return self._decoration_data

    @decoration_data.setter
    def decoration_data(self, value: DecorationData):
        self.proto.decoration_data.CopyFrom(value.proto)

        self._decoration_data = value
        self._decoration_data._update_proto_references(self.proto.decoration_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.ObjectDecorations):
        self.proto = proto
        self._decoration_data._update_proto_references(proto.decoration_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.ObjectDecorationParams)
class ObjectDecorationParams(ProtoMessageClass):
    '''
    Parameters which control the placement of decorations on an object.

    Args:
        decorate_chance: :attr:`decorate_chance`
        preset_distribution: :attr:`preset_distribution`
    Attributes:
        decorate_chance: The probability that a decoration will be applied to a particular object.
            Default: 0.1
        preset_distribution: The distribution of which decorations should be applied to a particular object and their associated probabilities.
            If not provided, will use default values.

            Valid values::

                "None"
                "TAXI_text"
                "TAXI_icon"
                "NO_PARKING_text"
                "LOADING_ZONE_text"
                "EV_JP_01_A_icon"
                "EV_JP_01_B_icon"
                "EV_JP_01_C_icon"
                "EV_01_icon"
                "EV_02_icon"
                "EV_03_icon"
                "Family_01_A_icon"
                "Family_01_B_icon"
                "Family_01_C_icon"
                "PARKING_10_MIN_text"
                "PARKING_30_MIN_text"
                "PARKING_15_MIN_text"
                "RESERVED_01_text"
                "Wheelchair_01_A_icon"
                "Wheelchair_01_B_icon"
                "Wheelchair_01_C_icon"
                "Wheelchair_01_D_icon"'''

    _proto_message = pd_unified_generator_pb2.ObjectDecorationParams

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.ObjectDecorationParams] = None,
        decorate_chance: float = None,
        preset_distribution: _pd_distributions_pb2.EnumDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.ObjectDecorationParams()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(
            proto=proto.preset_distribution
        )
        if decorate_chance is not None:
            self.decorate_chance = decorate_chance
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution

    @property
    def decorate_chance(self) -> float:
        return self.proto.decorate_chance

    @decorate_chance.setter
    def decorate_chance(self, value: float):
        self.proto.decorate_chance = value

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.preset_distribution.CopyFrom(value.proto)

        self._preset_distribution = value
        self._preset_distribution._update_proto_references(self.proto.preset_distribution)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.ObjectDecorationParams):
        self.proto = proto
        self._preset_distribution._update_proto_references(proto.preset_distribution)


@register_wrapper(proto_type=pd_unified_generator_pb2.FloatArray)
class FloatArray(ProtoMessageClass):
    """
    Message to store array of RGB values.

    Args:
        data: :attr:`data`
    Attributes:
        data:"""

    _proto_message = pd_unified_generator_pb2.FloatArray

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.FloatArray] = None, data: List[float] = None):
        if proto is None:
            proto = pd_unified_generator_pb2.FloatArray()
        self.proto = proto
        self._data = ProtoListWrapper(container=[float(v) for v in proto.data], attr_name="data", list_owner=self)
        if data is not None:
            self.data = data

    @property
    def data(self) -> List[float]:
        return self._data

    @data.setter
    def data(self, value: List[float]):
        self._data.clear()
        for v in value:
            self._data.append(v)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.FloatArray):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.EgoAgentGeneratorParameters)
class EgoAgentGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place an ego agent with sensor in the world. Required for every scenario. All agents placed by the
    EgoAgentGenerator will have an "EGO" tag added by default.

    Args:
        agent_type: :attr:`agent_type`
        ego_model: :attr:`ego_model`
        position_request: :attr:`position_request`
        use_traffic_light_color_probability: :attr:`use_traffic_light_color_probability`
        traffic_light_color_probability: :attr:`traffic_light_color_probability`
        vehicle_spawn_data: :attr:`vehicle_spawn_data`
        pedestrian_spawn_data: :attr:`pedestrian_spawn_data`
        drone_spawn_data: :attr:`drone_spawn_data`
    Attributes:
        agent_type: Determines the type of agent that the ego sensor is attached to.
            Default: :attr:`AgentType.VEHICLE`
        ego_model: Specifies the type of agent which the ego will be attached to is :attr:`agent_type` if :obj:`AgentType.VEHICLE`.
            Default: suv_medium_02
        position_request: Specify the location on the map at which the ego agent will be spawned. Must be provided.
        use_traffic_light_color_probability: Specifies if the ego agent should be placed in front of a traffic light at the beginning of a scenario.
            Default: False
        traffic_light_color_probability: Specifies the desired traffic light distribution (with associated probability) to use if
            :attr:`use_traffic_light_color_probability` is True. Must be provided if :attr:`use_traffic_light_color_probability`
            is True.

            Possible values::

                "Red"
                "Yellow"
                "Green"
        vehicle_spawn_data: Specifies parameters of the ego agent if :attr:`agent_type` is :obj:`AgentType.VEHICLE`. If not provided, will use
            defaults specified in `VehicleSpawnData`.
        pedestrian_spawn_data: DEPRECATED
        drone_spawn_data: DEPRECATED"""

    _proto_message = pd_unified_generator_pb2.EgoAgentGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.EgoAgentGeneratorParameters] = None,
        agent_type: AgentType = None,
        ego_model: str = None,
        position_request: PositionRequest = None,
        use_traffic_light_color_probability: bool = None,
        traffic_light_color_probability: _pd_distributions_pb2.EnumDistribution = None,
        vehicle_spawn_data: VehicleSpawnData = None,
        pedestrian_spawn_data: PedestrianSpawnData = None,
        drone_spawn_data: DroneSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.EgoAgentGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._traffic_light_color_probability = get_wrapper(proto_type=proto.traffic_light_color_probability.__class__)(
            proto=proto.traffic_light_color_probability
        )
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(
            proto=proto.vehicle_spawn_data
        )
        self._pedestrian_spawn_data = get_wrapper(proto_type=proto.pedestrian_spawn_data.__class__)(
            proto=proto.pedestrian_spawn_data
        )
        self._drone_spawn_data = get_wrapper(proto_type=proto.drone_spawn_data.__class__)(proto=proto.drone_spawn_data)
        if agent_type is not None:
            self.agent_type = agent_type
        if ego_model is not None:
            self.ego_model = ego_model
        if position_request is not None:
            self.position_request = position_request
        if use_traffic_light_color_probability is not None:
            self.use_traffic_light_color_probability = use_traffic_light_color_probability
        if traffic_light_color_probability is not None:
            self.traffic_light_color_probability = traffic_light_color_probability
        if vehicle_spawn_data is not None:
            self.vehicle_spawn_data = vehicle_spawn_data
        if pedestrian_spawn_data is not None:
            self.pedestrian_spawn_data = pedestrian_spawn_data
        if drone_spawn_data is not None:
            self.drone_spawn_data = drone_spawn_data

    @property
    def agent_type(self) -> AgentType:
        return self.proto.agent_type

    @agent_type.setter
    def agent_type(self, value: AgentType):
        self.proto.agent_type = value

    @property
    def ego_model(self) -> str:
        return self.proto.ego_model

    @ego_model.setter
    def ego_model(self, value: str):
        self.proto.ego_model = value

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def use_traffic_light_color_probability(self) -> bool:
        return self.proto.use_traffic_light_color_probability

    @use_traffic_light_color_probability.setter
    def use_traffic_light_color_probability(self, value: bool):
        self.proto.use_traffic_light_color_probability = value

    @property
    def traffic_light_color_probability(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._traffic_light_color_probability

    @traffic_light_color_probability.setter
    def traffic_light_color_probability(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.traffic_light_color_probability.CopyFrom(value.proto)

        self._traffic_light_color_probability = value
        self._traffic_light_color_probability._update_proto_references(self.proto.traffic_light_color_probability)

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self.proto.vehicle_spawn_data.CopyFrom(value.proto)

        self._vehicle_spawn_data = value
        self._vehicle_spawn_data._update_proto_references(self.proto.vehicle_spawn_data)

    @property
    def pedestrian_spawn_data(self) -> PedestrianSpawnData:
        return self._pedestrian_spawn_data

    @pedestrian_spawn_data.setter
    def pedestrian_spawn_data(self, value: PedestrianSpawnData):
        self.proto.pedestrian_spawn_data.CopyFrom(value.proto)

        self._pedestrian_spawn_data = value
        self._pedestrian_spawn_data._update_proto_references(self.proto.pedestrian_spawn_data)

    @property
    def drone_spawn_data(self) -> DroneSpawnData:
        return self._drone_spawn_data

    @drone_spawn_data.setter
    def drone_spawn_data(self, value: DroneSpawnData):
        self.proto.drone_spawn_data.CopyFrom(value.proto)

        self._drone_spawn_data = value
        self._drone_spawn_data._update_proto_references(self.proto.drone_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.EgoAgentGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._traffic_light_color_probability._update_proto_references(proto.traffic_light_color_probability)
        self._vehicle_spawn_data._update_proto_references(proto.vehicle_spawn_data)
        self._pedestrian_spawn_data._update_proto_references(proto.pedestrian_spawn_data)
        self._drone_spawn_data._update_proto_references(proto.drone_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleGeneratorParameters)
class VehicleGeneratorParameters(AtomicGeneratorMessage):
    """
    Places a single non-ego vehicle into the world. Requires previous use of :obj:`EgoAgentGeneratorParameters` in the
    scenario.

    Args:
        model: :attr:`model`
        position_request: :attr:`position_request`
        vehicle_spawn_data: :attr:`vehicle_spawn_data`
    Attributes:
        model: Name of the vehicle asset that should be spawned. Must be provided.
        position_request: Specifies the location at which the vehicle should be spawned. Must be provided.
        vehicle_spawn_data: Parameters that govern the vehicle's spawn characteristics and movement behavior. If not provided, will use
            defaults specified in :obj:`VehicleSpawnData`."""

    _proto_message = pd_unified_generator_pb2.VehicleGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.VehicleGeneratorParameters] = None,
        model: str = None,
        position_request: PositionRequest = None,
        vehicle_spawn_data: VehicleSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(
            proto=proto.vehicle_spawn_data
        )
        if model is not None:
            self.model = model
        if position_request is not None:
            self.position_request = position_request
        if vehicle_spawn_data is not None:
            self.vehicle_spawn_data = vehicle_spawn_data

    @property
    def model(self) -> str:
        return self.proto.model

    @model.setter
    def model(self, value: str):
        self.proto.model = value

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self.proto.vehicle_spawn_data.CopyFrom(value.proto)

        self._vehicle_spawn_data = value
        self._vehicle_spawn_data._update_proto_references(self.proto.vehicle_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.VehicleGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._vehicle_spawn_data._update_proto_references(proto.vehicle_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.TrafficGeneratorParameters)
class TrafficGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place multiple vehicles into the world. Requires previous use of :obj:`EgoAgentGeneratorParameters` in the
    scenario.

    Args:
        position_request: :attr:`position_request`
        spawn_probability: :attr:`spawn_probability`
        vehicle_spawn_data: :attr:`vehicle_spawn_data`
        vehicle_distribution: :attr:`vehicle_distribution`
        start_separation_time_map: :attr:`start_separation_time_map`
        target_separation_time_map: :attr:`target_separation_time_map`
    Attributes:
        position_request: Specifies the location around which traffic agents should be spawned. Only works with
            :obj:`LocationRelativePositionRequest`. Must be provided.
        spawn_probability: Specifies the density of traffic that is spawned by controlling the proportion of valid spawn points in which
            vehicles are spawned. Valid values are floats in the range 0.0 to 1.0. 0.0 indicates
            no traffic spawned. 1.0 indicates maximum possible density.
            Default: 0.8
        vehicle_spawn_data: Parameters that govern the vehicle's spawn characteristics and movement behavior. If not provided, will use
            defaults specified in :obj:`VehicleSpawnData`.
        vehicle_distribution: Specifies the likelihood of various vehicle categories spawning. If not provided, will use the values below.

            Default values::

                "MIDSIZE" : 0.181
                "COMPACT" : 0.177
                "BUS" : 0.019
                "TRUCK" : 0.038
                "SUV" : 0.197
                "VAN" : 0.066
                "BICYCLE" : 0.061
                "MOTORCYCLE" :  0.068
                "CARAVAN" :/RV  0.009
                "FULLSIZE" :  0.184
        start_separation_time_map: Controls the minimum separation distance between valid spawn points for vehicles by multiplying the
            `start_separation_time_map` by each vehicle's initial velocity. If not provided, defaults to the values below.

            Default values::

                {"bicycle", {0.7f, 1.7f}}
                {"heavy", {2.5f, 3.5f}}
                {"heavy_nondriven", {2.5f, 3.5f}}
                {"light", {0.7f, 1.7f}}
                {"light_nondriven", {0.7f, 1.7f}}
                {"medium", {1.5f, 2.5f}}
                {"medium_nondriven", {1.5f, 2.5f}}
                {"motorcycle", {0.7f, 1.7f}}
        target_separation_time_map: Specifies the separation time between vehicles which should be targeted through the scenario. If not provided, will
            use the values provided in :attr:`start_separation_time_map`."""

    _proto_message = pd_unified_generator_pb2.TrafficGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.TrafficGeneratorParameters] = None,
        position_request: PositionRequest = None,
        spawn_probability: float = None,
        vehicle_spawn_data: VehicleSpawnData = None,
        vehicle_distribution: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight] = None,
        start_separation_time_map: Dict[str, _pd_distributions_pb2.ContinousUniformDistribution] = None,
        target_separation_time_map: Dict[str, _pd_distributions_pb2.ContinousUniformDistribution] = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.TrafficGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(
            proto=proto.vehicle_spawn_data
        )
        self._vehicle_distribution = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()
            },
            attr_name="vehicle_distribution",
            dict_owner=self,
        )
        self._start_separation_time_map = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.start_separation_time_map.items()
            },
            attr_name="start_separation_time_map",
            dict_owner=self,
        )
        self._target_separation_time_map = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.target_separation_time_map.items()
            },
            attr_name="target_separation_time_map",
            dict_owner=self,
        )
        if position_request is not None:
            self.position_request = position_request
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability
        if vehicle_spawn_data is not None:
            self.vehicle_spawn_data = vehicle_spawn_data
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution
        if start_separation_time_map is not None:
            self.start_separation_time_map = start_separation_time_map
        if target_separation_time_map is not None:
            self.target_separation_time_map = target_separation_time_map

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def spawn_probability(self) -> float:
        return self.proto.spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: float):
        self.proto.spawn_probability = value

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self.proto.vehicle_spawn_data.CopyFrom(value.proto)

        self._vehicle_spawn_data = value
        self._vehicle_spawn_data._update_proto_references(self.proto.vehicle_spawn_data)

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

    @property
    def start_separation_time_map(self) -> Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]:
        return self._start_separation_time_map

    @start_separation_time_map.setter
    def start_separation_time_map(self, value: Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]):
        self._start_separation_time_map.clear()
        self._start_separation_time_map.update(value)

    @property
    def target_separation_time_map(self) -> Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]:
        return self._target_separation_time_map

    @target_separation_time_map.setter
    def target_separation_time_map(self, value: Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]):
        self._target_separation_time_map.clear()
        self._target_separation_time_map.update(value)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.TrafficGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._vehicle_spawn_data._update_proto_references(proto.vehicle_spawn_data)
        for k, v in self.vehicle_distribution.items():
            v._update_proto_references(self.proto.vehicle_distribution[k])
        for k, v in self.start_separation_time_map.items():
            v._update_proto_references(self.proto.start_separation_time_map[k])
        for k, v in self.target_separation_time_map.items():
            v._update_proto_references(self.proto.target_separation_time_map[k])


@register_wrapper(proto_type=pd_unified_generator_pb2.ParkedVehicleGeneratorParameters)
class ParkedVehicleGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place parked vehicles in the scenario. Requires previous use of :obj:`EgoAgentGeneratorParameters` in the
    scenario.

    Args:
        position_request: :attr:`position_request`
        spawn_probability: :attr:`spawn_probability`
        vehicle_distribution: :attr:`vehicle_distribution`
        agent_spawn_data: :attr:`agent_spawn_data`
    Attributes:
        position_request: Specifies the location around which traffic should be spawned. Only works with
            :obj:`LocationRelativePositionRequest`. Must be provided.
        spawn_probability: Specifies the density of parked vehicles that is spawned by controlling the proportion of valid spawn points in which
            vehicles are spawned. Valid values are floats in the range 0.0 to 1.0. 0.0 indicates
            no traffic spawned. 1.0 indicates maximum possible density. If not provided, will use default value of 0.
        vehicle_distribution: Specifies the likelihood of various vehicle categories spawning. If not provided, will use the values below.

            Default values::

                "MIDSIZE" : 0.181
                "COMPACT" : 0.177
                "BUS" : 0.019
                "TRUCK" : 0.038
                "SUV" : 0.197
                "VAN" : 0.066
                "BICYCLE" : 0.061
                "MOTORCYCLE" :  0.068
                "CARAVAN" :/RV  0.009
                "FULLSIZE" :  0.184
        agent_spawn_data: Specifies spawn data which applies to the agents spawned by this generator. If not provided, will default to default
            values in :obj:`AgentSpawnData`."""

    _proto_message = pd_unified_generator_pb2.ParkedVehicleGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.ParkedVehicleGeneratorParameters] = None,
        position_request: PositionRequest = None,
        spawn_probability: CenterSpreadConfig = None,
        vehicle_distribution: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight] = None,
        agent_spawn_data: AgentSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.ParkedVehicleGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._spawn_probability = get_wrapper(proto_type=proto.spawn_probability.__class__)(
            proto=proto.spawn_probability
        )
        self._vehicle_distribution = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()
            },
            attr_name="vehicle_distribution",
            dict_owner=self,
        )
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        if position_request is not None:
            self.position_request = position_request
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def spawn_probability(self) -> CenterSpreadConfig:
        return self._spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: CenterSpreadConfig):
        self.proto.spawn_probability.CopyFrom(value.proto)

        self._spawn_probability = value
        self._spawn_probability._update_proto_references(self.proto.spawn_probability)

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.ParkedVehicleGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._spawn_probability._update_proto_references(proto.spawn_probability)
        for k, v in self.vehicle_distribution.items():
            v._update_proto_references(self.proto.vehicle_distribution[k])
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.StaticAgentGeneratorParameters)
class StaticAgentGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place a static agent in the world. Requires previous use of :obj:`EgoAgentGeneratorParameters` in the
    scenario.

    Args:
        position_request: :attr:`position_request`
        model: :attr:`model`
        agent_spawn_data: :attr:`agent_spawn_data`
    Attributes:
        position_request: Specifies the location around which traffic should be spawned.
        model: The asset name of the static agent which should be spawned. Must be provided.
        agent_spawn_data: Specifies spawn data which applies to the agents spawned by this generator. If not provided, will default to default
            values in :obj:`AgentSpawnData`."""

    _proto_message = pd_unified_generator_pb2.StaticAgentGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.StaticAgentGeneratorParameters] = None,
        position_request: PositionRequest = None,
        model: str = None,
        agent_spawn_data: AgentSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.StaticAgentGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        if position_request is not None:
            self.position_request = position_request
        if model is not None:
            self.model = model
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def model(self) -> str:
        return self.proto.model

    @model.setter
    def model(self, value: str):
        self.proto.model = value

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.StaticAgentGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.DebrisGeneratorParameters)
class DebrisGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place debris in the scenario. Requires previous use of :obj:`EgoAgentGeneratorParameters` in the
    scenario.

    Args:
        spawn_probability: :attr:`spawn_probability`
        debris_center_bias: :attr:`debris_center_bias`
        min_debris_distance: :attr:`min_debris_distance`
        max_debris_distance: :attr:`max_debris_distance`
        debris_asset_tag: :attr:`debris_asset_tag`
        debris_asset_remove_tag: :attr:`debris_asset_remove_tag`
        position_request: :attr:`position_request`
        asset_distribution: :attr:`asset_distribution`
        agent_spawn_data: :attr:`agent_spawn_data`
    Attributes:
        spawn_probability: Specifies the density of debris that is spawned by controlling the proportion of valid spawn points in which
            debris are spawned. Valid values are floats in the range 0.0 to 1.0. 0.0 indicates
            no debris spawned. 1.0 indicates maximum possible density.
            Default: 0.01
        debris_center_bias: Determines the lateral bias of debris placement within lanes. Valid values are in the range -1.0 to 1.0. A value
            of 1.0 will bias debris placement to the center of the lane. A value of -1.0 will bias debris placement to the
            edges of the lane. A value of 0.0 will evenly place debris throughout the lane.

            If not provided, a value of 0.0 will be used
        min_debris_distance: Specifies the minimum distance from the ego that debris is spawned. Must be a float greater than 0.0. If not
            provided, will use value of 0.0.
        max_debris_distance: Specifies the maximum distance from the ego that debris is spawned. Must be a float greater than 0.0.
            Default: 50.0
        debris_asset_tag: Comma separated string which lists the assets to be spawn as debris. Every asset has an equal spawn probability.
            Default: trash_bottle_tall_01
        debris_asset_remove_tag: Comma separated string which lists debris assets that appear in :attr:`debris_asset_tag` which should be skipped
            and not spawned. If not provided, no assets are removed from :attr:`debris_asset_tag`.
        position_request: Specifies the location around which traffic should be spawned. Only works with
            :obj:`LocationRelativePositionRequest` and :obj:`LaneSpawnPolicy`. Must be provided.
        asset_distribution: Specifies the asset names that should be spawned as debris together with their associated spawn probability. If
            provided, asset names in :attr:`debris_asset_tag` and :attr:`debris_asset_remove_tag` are ignored.
        agent_spawn_data: Specifies spawn data which applies to the agents spawned by this generator. If not provided, will default to default
            values in :obj:`AgentSpawnData`."""

    _proto_message = pd_unified_generator_pb2.DebrisGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DebrisGeneratorParameters] = None,
        spawn_probability: float = None,
        debris_center_bias: float = None,
        min_debris_distance: float = None,
        max_debris_distance: float = None,
        debris_asset_tag: str = None,
        debris_asset_remove_tag: str = None,
        position_request: PositionRequest = None,
        asset_distribution: Dict[str, float] = None,
        agent_spawn_data: AgentSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DebrisGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability
        if debris_center_bias is not None:
            self.debris_center_bias = debris_center_bias
        if min_debris_distance is not None:
            self.min_debris_distance = min_debris_distance
        if max_debris_distance is not None:
            self.max_debris_distance = max_debris_distance
        if debris_asset_tag is not None:
            self.debris_asset_tag = debris_asset_tag
        if debris_asset_remove_tag is not None:
            self.debris_asset_remove_tag = debris_asset_remove_tag
        if position_request is not None:
            self.position_request = position_request
        self._asset_distribution = ProtoDictWrapper(
            container={k: float(v) for (k, v) in proto.asset_distribution.items()},
            attr_name="asset_distribution",
            dict_owner=self,
        )
        if asset_distribution is not None:
            self.asset_distribution = asset_distribution
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data

    @property
    def spawn_probability(self) -> float:
        return self.proto.spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: float):
        self.proto.spawn_probability = value

    @property
    def debris_center_bias(self) -> float:
        return self.proto.debris_center_bias

    @debris_center_bias.setter
    def debris_center_bias(self, value: float):
        self.proto.debris_center_bias = value

    @property
    def min_debris_distance(self) -> float:
        return self.proto.min_debris_distance

    @min_debris_distance.setter
    def min_debris_distance(self, value: float):
        self.proto.min_debris_distance = value

    @property
    def max_debris_distance(self) -> float:
        return self.proto.max_debris_distance

    @max_debris_distance.setter
    def max_debris_distance(self, value: float):
        self.proto.max_debris_distance = value

    @property
    def debris_asset_tag(self) -> str:
        return self.proto.debris_asset_tag

    @debris_asset_tag.setter
    def debris_asset_tag(self, value: str):
        self.proto.debris_asset_tag = value

    @property
    def debris_asset_remove_tag(self) -> str:
        return self.proto.debris_asset_remove_tag

    @debris_asset_remove_tag.setter
    def debris_asset_remove_tag(self, value: str):
        self.proto.debris_asset_remove_tag = value

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def asset_distribution(self) -> Dict[str, float]:
        return self._asset_distribution

    @asset_distribution.setter
    def asset_distribution(self, value: Dict[str, float]):
        self._asset_distribution.clear()
        self._asset_distribution.update(value)

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DebrisGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.PedestrianGeneratorParameters)
class PedestrianGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place a single pedestrian in the scenario. Requires previous use of :obj:`EgoAgentGeneratorParameters` in
    the scenario.

    Args:
        position_request: :attr:`position_request`
        ped_spawn_data: :attr:`ped_spawn_data`
    Attributes:
        position_request: Specifies the location around which traffic should be spawned. Works with all `PositionRequest` types except
            :obj:`PathTimeRelativePositionRequest`.
        ped_spawn_data: Specifies parameters that control pedestrian spawning and movement behavior. If not provided, will use defaults
            specified in :obj:`PedestrianSpawnData`."""

    _proto_message = pd_unified_generator_pb2.PedestrianGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.PedestrianGeneratorParameters] = None,
        position_request: PositionRequest = None,
        ped_spawn_data: PedestrianSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.PedestrianGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._ped_spawn_data = get_wrapper(proto_type=proto.ped_spawn_data.__class__)(proto=proto.ped_spawn_data)
        if position_request is not None:
            self.position_request = position_request
        if ped_spawn_data is not None:
            self.ped_spawn_data = ped_spawn_data

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def ped_spawn_data(self) -> PedestrianSpawnData:
        return self._ped_spawn_data

    @ped_spawn_data.setter
    def ped_spawn_data(self, value: PedestrianSpawnData):
        self.proto.ped_spawn_data.CopyFrom(value.proto)

        self._ped_spawn_data = value
        self._ped_spawn_data._update_proto_references(self.proto.ped_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.PedestrianGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._ped_spawn_data._update_proto_references(proto.ped_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.RandomPedestrianGeneratorParameters)
class RandomPedestrianGeneratorParameters(AtomicGeneratorMessage):
    """
    Generator to place multiple pedestrians in a scenario. Requires previous use of :obj:`EgoAgentGeneratorParameters` in
    the scenario.

    Args:
        speed_range: :attr:`speed_range`
        position_request: :attr:`position_request`
        num_of_pedestrians_range: :attr:`num_of_pedestrians_range`
        min_radius_between_pedestrians: :attr:`min_radius_between_pedestrians`
        ped_spawn_data: :attr:`ped_spawn_data`
    Attributes:
        speed_range: Specifies the minimum and maximum values for the speed of each pedestrian. Each spawned pedestrian's speed is then
            randomly sampled from this range. The specified `min` value must be greater than 0.0 and the specified `max` value
            must be greater than `min`.

            If not provided, will use a `min` of 0.5 and a `max` of 1.5.
        position_request: Specifies the location around which traffic should be spawned. Only works with
            :obj:`LocationRelativePositionRequest` and :obj:`LaneSpawnPolicy`. Must be provided.
        num_of_pedestrians_range: Specifies the minimum and maximum number of pedestrians to generate. The actual number of pedestrians to spawn is
            selected from a normal distribution within this range. The specified `min` value must be greater than 0.0 and the
            specified `max` value must be greater than `min`. This parameter must be provided.
        min_radius_between_pedestrians: Specified the spatial separation between pedestrians in meters. Specified values must be greater than 0.0.
            Default: 0.5
        ped_spawn_data: Specifies parameters that control pedestrian spawning and movement behavior. If not provided, will use defaults
            specified in :obj:`PedestrianSpawnData`."""

    _proto_message = pd_unified_generator_pb2.RandomPedestrianGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.RandomPedestrianGeneratorParameters] = None,
        speed_range: MinMaxConfigFloat = None,
        position_request: PositionRequest = None,
        num_of_pedestrians_range: MinMaxConfigInt = None,
        min_radius_between_pedestrians: float = None,
        ped_spawn_data: PedestrianSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.RandomPedestrianGeneratorParameters()
        self.proto = proto
        self._speed_range = get_wrapper(proto_type=proto.speed_range.__class__)(proto=proto.speed_range)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._num_of_pedestrians_range = get_wrapper(proto_type=proto.num_of_pedestrians_range.__class__)(
            proto=proto.num_of_pedestrians_range
        )
        self._ped_spawn_data = get_wrapper(proto_type=proto.ped_spawn_data.__class__)(proto=proto.ped_spawn_data)
        if speed_range is not None:
            self.speed_range = speed_range
        if position_request is not None:
            self.position_request = position_request
        if num_of_pedestrians_range is not None:
            self.num_of_pedestrians_range = num_of_pedestrians_range
        if min_radius_between_pedestrians is not None:
            self.min_radius_between_pedestrians = min_radius_between_pedestrians
        if ped_spawn_data is not None:
            self.ped_spawn_data = ped_spawn_data

    @property
    def speed_range(self) -> MinMaxConfigFloat:
        return self._speed_range

    @speed_range.setter
    def speed_range(self, value: MinMaxConfigFloat):
        self.proto.speed_range.CopyFrom(value.proto)

        self._speed_range = value
        self._speed_range._update_proto_references(self.proto.speed_range)

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def num_of_pedestrians_range(self) -> MinMaxConfigInt:
        return self._num_of_pedestrians_range

    @num_of_pedestrians_range.setter
    def num_of_pedestrians_range(self, value: MinMaxConfigInt):
        self.proto.num_of_pedestrians_range.CopyFrom(value.proto)

        self._num_of_pedestrians_range = value
        self._num_of_pedestrians_range._update_proto_references(self.proto.num_of_pedestrians_range)

    @property
    def min_radius_between_pedestrians(self) -> float:
        return self.proto.min_radius_between_pedestrians

    @min_radius_between_pedestrians.setter
    def min_radius_between_pedestrians(self, value: float):
        self.proto.min_radius_between_pedestrians = value

    @property
    def ped_spawn_data(self) -> PedestrianSpawnData:
        return self._ped_spawn_data

    @ped_spawn_data.setter
    def ped_spawn_data(self, value: PedestrianSpawnData):
        self.proto.ped_spawn_data.CopyFrom(value.proto)

        self._ped_spawn_data = value
        self._ped_spawn_data._update_proto_references(self.proto.ped_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.RandomPedestrianGeneratorParameters):
        self.proto = proto
        self._speed_range._update_proto_references(proto.speed_range)
        self._position_request._update_proto_references(proto.position_request)
        self._num_of_pedestrians_range._update_proto_references(proto.num_of_pedestrians_range)
        self._ped_spawn_data._update_proto_references(proto.ped_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.DroneGeneratorParameters)
class DroneGeneratorParameters(AtomicGeneratorMessage):
    """
    Not yet implemented.

    Args:
        position_request: :attr:`position_request`
        drone_spawn_data: :attr:`drone_spawn_data`
    Attributes:
        position_request: Not yet implemented.
        drone_spawn_data: Not yet implemented."""

    _proto_message = pd_unified_generator_pb2.DroneGeneratorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DroneGeneratorParameters] = None,
        position_request: PositionRequest = None,
        drone_spawn_data: DroneSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DroneGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._drone_spawn_data = get_wrapper(proto_type=proto.drone_spawn_data.__class__)(proto=proto.drone_spawn_data)
        if position_request is not None:
            self.position_request = position_request
        if drone_spawn_data is not None:
            self.drone_spawn_data = drone_spawn_data

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self.proto.position_request.CopyFrom(value.proto)

        self._position_request = value
        self._position_request._update_proto_references(self.proto.position_request)

    @property
    def drone_spawn_data(self) -> DroneSpawnData:
        return self._drone_spawn_data

    @drone_spawn_data.setter
    def drone_spawn_data(self, value: DroneSpawnData):
        self.proto.drone_spawn_data.CopyFrom(value.proto)

        self._drone_spawn_data = value
        self._drone_spawn_data._update_proto_references(self.proto.drone_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DroneGeneratorParameters):
        self.proto = proto
        self._position_request._update_proto_references(proto.position_request)
        self._drone_spawn_data._update_proto_references(proto.drone_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.PositionRequest)
class PositionRequest(ProtoMessageClass):
    """
    Specifies a location in the world which can be used to govern object placement.

    Args:
        longitudinal_offset: :attr:`longitudinal_offset`
        lateral_offset: :attr:`lateral_offset`
        yaw_offset: :attr:`yaw_offset`
        absolute_position_request: :attr:`absolute_position_request`
        path_time_relative_position_request: :attr:`path_time_relative_position_request`
        location_relative_position_request: :attr:`location_relative_position_request`
        lane_spawn_policy: :attr:`lane_spawn_policy`
        road_pitch_position_request: :attr:`road_pitch_position_request`
    Attributes:
        longitudinal_offset: Specifies the distance in meters to move along a lane after an initial is found within the :obj:`PositionRequest`.
            Can be any float: positive values will move forwards along the lane and negative values will move backwards along
            the lane. If not provided, will default to 0.0.
        lateral_offset: Specifies the distance in meters to move laterally (relative to a lane) after an initial is found within the
            :obj:`PositionRequest`. Can be any float: positive values will move rightwards in the lane and negative values will
            move leftwards in the lane. If not provided, will default to 0.0.
        yaw_offset: Specifies a rotation of the returned position about the up axis of the world. The rotation is specified in radians
            and is aligned with the right hand rule for rotation about the up axis. Rotation is applied about the center of the
            object. If not specified, will use a value of 0.0.
        absolute_position_request: Position request that specifies an x,y,z position in the world.
        path_time_relative_position_request: Position request that specifies a time to "path-crossing" between agents.
        location_relative_position_request: Position request that specifies a location relative to another agent.
        lane_spawn_policy: Position request that returns a location in a specified lane.
        road_pitch_position_request: DEPRECATED"""

    _proto_message = pd_unified_generator_pb2.PositionRequest

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.PositionRequest] = None,
        longitudinal_offset: CenterSpreadConfig = None,
        lateral_offset: CenterSpreadConfig = None,
        yaw_offset: CenterSpreadConfig = None,
        absolute_position_request: AbsolutePositionRequest = None,
        path_time_relative_position_request: PathTimeRelativePositionRequest = None,
        location_relative_position_request: LocationRelativePositionRequest = None,
        lane_spawn_policy: LaneSpawnPolicy = None,
        road_pitch_position_request: RoadPitchPositionRequest = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.PositionRequest()
        self.proto = proto
        self._longitudinal_offset = get_wrapper(proto_type=proto.longitudinal_offset.__class__)(
            proto=proto.longitudinal_offset
        )
        self._lateral_offset = get_wrapper(proto_type=proto.lateral_offset.__class__)(proto=proto.lateral_offset)
        self._yaw_offset = get_wrapper(proto_type=proto.yaw_offset.__class__)(proto=proto.yaw_offset)
        self._absolute_position_request = get_wrapper(proto_type=proto.absolute_position_request.__class__)(
            proto=proto.absolute_position_request
        )
        self._path_time_relative_position_request = get_wrapper(
            proto_type=proto.path_time_relative_position_request.__class__
        )(proto=proto.path_time_relative_position_request)
        self._location_relative_position_request = get_wrapper(
            proto_type=proto.location_relative_position_request.__class__
        )(proto=proto.location_relative_position_request)
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(
            proto=proto.lane_spawn_policy
        )
        self._road_pitch_position_request = get_wrapper(proto_type=proto.road_pitch_position_request.__class__)(
            proto=proto.road_pitch_position_request
        )
        if longitudinal_offset is not None:
            self.longitudinal_offset = longitudinal_offset
        if lateral_offset is not None:
            self.lateral_offset = lateral_offset
        if yaw_offset is not None:
            self.yaw_offset = yaw_offset
        if absolute_position_request is not None:
            self.absolute_position_request = absolute_position_request
        if path_time_relative_position_request is not None:
            self.path_time_relative_position_request = path_time_relative_position_request
        if location_relative_position_request is not None:
            self.location_relative_position_request = location_relative_position_request
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy
        if road_pitch_position_request is not None:
            self.road_pitch_position_request = road_pitch_position_request

    @property
    def longitudinal_offset(self) -> CenterSpreadConfig:
        return self._longitudinal_offset

    @longitudinal_offset.setter
    def longitudinal_offset(self, value: CenterSpreadConfig):
        self.proto.longitudinal_offset.CopyFrom(value.proto)

        self._longitudinal_offset = value
        self._longitudinal_offset._update_proto_references(self.proto.longitudinal_offset)

    @property
    def lateral_offset(self) -> CenterSpreadConfig:
        return self._lateral_offset

    @lateral_offset.setter
    def lateral_offset(self, value: CenterSpreadConfig):
        self.proto.lateral_offset.CopyFrom(value.proto)

        self._lateral_offset = value
        self._lateral_offset._update_proto_references(self.proto.lateral_offset)

    @property
    def yaw_offset(self) -> CenterSpreadConfig:
        return self._yaw_offset

    @yaw_offset.setter
    def yaw_offset(self, value: CenterSpreadConfig):
        self.proto.yaw_offset.CopyFrom(value.proto)

        self._yaw_offset = value
        self._yaw_offset._update_proto_references(self.proto.yaw_offset)

    @property
    def absolute_position_request(self) -> AbsolutePositionRequest:
        return self._absolute_position_request

    @absolute_position_request.setter
    def absolute_position_request(self, value: AbsolutePositionRequest):
        self.proto.absolute_position_request.CopyFrom(value.proto)

        self._absolute_position_request = value
        self._absolute_position_request._update_proto_references(self.proto.absolute_position_request)

    @property
    def path_time_relative_position_request(self) -> PathTimeRelativePositionRequest:
        return self._path_time_relative_position_request

    @path_time_relative_position_request.setter
    def path_time_relative_position_request(self, value: PathTimeRelativePositionRequest):
        self.proto.path_time_relative_position_request.CopyFrom(value.proto)

        self._path_time_relative_position_request = value
        self._path_time_relative_position_request._update_proto_references(
            self.proto.path_time_relative_position_request
        )

    @property
    def location_relative_position_request(self) -> LocationRelativePositionRequest:
        return self._location_relative_position_request

    @location_relative_position_request.setter
    def location_relative_position_request(self, value: LocationRelativePositionRequest):
        self.proto.location_relative_position_request.CopyFrom(value.proto)

        self._location_relative_position_request = value
        self._location_relative_position_request._update_proto_references(self.proto.location_relative_position_request)

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self.proto.lane_spawn_policy.CopyFrom(value.proto)

        self._lane_spawn_policy = value
        self._lane_spawn_policy._update_proto_references(self.proto.lane_spawn_policy)

    @property
    def road_pitch_position_request(self) -> RoadPitchPositionRequest:
        return self._road_pitch_position_request

    @road_pitch_position_request.setter
    def road_pitch_position_request(self, value: RoadPitchPositionRequest):
        self.proto.road_pitch_position_request.CopyFrom(value.proto)

        self._road_pitch_position_request = value
        self._road_pitch_position_request._update_proto_references(self.proto.road_pitch_position_request)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.PositionRequest):
        self.proto = proto
        self._longitudinal_offset._update_proto_references(proto.longitudinal_offset)
        self._lateral_offset._update_proto_references(proto.lateral_offset)
        self._yaw_offset._update_proto_references(proto.yaw_offset)
        self._absolute_position_request._update_proto_references(proto.absolute_position_request)
        self._path_time_relative_position_request._update_proto_references(proto.path_time_relative_position_request)
        self._location_relative_position_request._update_proto_references(proto.location_relative_position_request)
        self._lane_spawn_policy._update_proto_references(proto.lane_spawn_policy)
        self._road_pitch_position_request._update_proto_references(proto.road_pitch_position_request)


@register_wrapper(proto_type=pd_unified_generator_pb2.LaneCurvatureSpawnPolicy)
class LaneCurvatureSpawnPolicy(ProtoMessageClass):
    """
    Policy to return a spawn location based on the curvature of lanes around the spawn location.

    Args:
        curvature_bounds: :attr:`curvature_bounds`
        min_section_length: :attr:`min_section_length`
    Attributes:
        curvature_bounds: Specifies the minimum and maximum values for the curvature of lane segments when searching for valid spawn locations.
            If not provided, will use default values.
        min_section_length: Specifies a minimum length in meters for the lane on which the returned spawn location is located.
    """

    _proto_message = pd_unified_generator_pb2.LaneCurvatureSpawnPolicy

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.LaneCurvatureSpawnPolicy] = None,
        curvature_bounds: MinMaxConfigFloat = None,
        min_section_length: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.LaneCurvatureSpawnPolicy()
        self.proto = proto
        self._curvature_bounds = get_wrapper(proto_type=proto.curvature_bounds.__class__)(proto=proto.curvature_bounds)
        if curvature_bounds is not None:
            self.curvature_bounds = curvature_bounds
        if min_section_length is not None:
            self.min_section_length = min_section_length

    @property
    def curvature_bounds(self) -> MinMaxConfigFloat:
        return self._curvature_bounds

    @curvature_bounds.setter
    def curvature_bounds(self, value: MinMaxConfigFloat):
        self.proto.curvature_bounds.CopyFrom(value.proto)

        self._curvature_bounds = value
        self._curvature_bounds._update_proto_references(self.proto.curvature_bounds)

    @property
    def min_section_length(self) -> float:
        return self.proto.min_section_length

    @min_section_length.setter
    def min_section_length(self, value: float):
        self.proto.min_section_length = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.LaneCurvatureSpawnPolicy):
        self.proto = proto
        self._curvature_bounds._update_proto_references(proto.curvature_bounds)


@register_wrapper(proto_type=pd_unified_generator_pb2.JunctionSpawnPolicy)
class JunctionSpawnPolicy(ProtoMessageClass):
    '''
    Policy to return a spawn location based on proximity to a junction.

    Args:
        distance_to_junction: :attr:`distance_to_junction`
        use_intersection_type_probability: :attr:`use_intersection_type_probability`
        intersection_type_probability: :attr:`intersection_type_probability`
    Attributes:
        distance_to_junction: Specifies a desired range of distances from the spawn location and the junction. The distance between the returned
            spawn point and the junction will be randomly samples from this distribution. Specified values must be greater than
            0.0. If not provided, will revert to default.
        use_intersection_type_probability: Flag to control whether to use specified intersection type probabilities.
            Default: False
        intersection_type_probability: Specifies distribution for intersection types (with associated probability) to use if
            :attr:`use_intersection_type_probability` is `True`. Must be provided if
            :attr:`use_intersection_type_probability` is `True`.

            Valid values::

                "Signaled"
                "Signed"'''

    _proto_message = pd_unified_generator_pb2.JunctionSpawnPolicy

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.JunctionSpawnPolicy] = None,
        distance_to_junction: _pd_distributions_pb2.ContinousUniformDistribution = None,
        use_intersection_type_probability: bool = None,
        intersection_type_probability: _pd_distributions_pb2.EnumDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.JunctionSpawnPolicy()
        self.proto = proto
        self._distance_to_junction = get_wrapper(proto_type=proto.distance_to_junction.__class__)(
            proto=proto.distance_to_junction
        )
        self._intersection_type_probability = get_wrapper(proto_type=proto.intersection_type_probability.__class__)(
            proto=proto.intersection_type_probability
        )
        if distance_to_junction is not None:
            self.distance_to_junction = distance_to_junction
        if use_intersection_type_probability is not None:
            self.use_intersection_type_probability = use_intersection_type_probability
        if intersection_type_probability is not None:
            self.intersection_type_probability = intersection_type_probability

    @property
    def distance_to_junction(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._distance_to_junction

    @distance_to_junction.setter
    def distance_to_junction(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.distance_to_junction.CopyFrom(value.proto)

        self._distance_to_junction = value
        self._distance_to_junction._update_proto_references(self.proto.distance_to_junction)

    @property
    def use_intersection_type_probability(self) -> bool:
        return self.proto.use_intersection_type_probability

    @use_intersection_type_probability.setter
    def use_intersection_type_probability(self, value: bool):
        self.proto.use_intersection_type_probability = value

    @property
    def intersection_type_probability(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._intersection_type_probability

    @intersection_type_probability.setter
    def intersection_type_probability(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.intersection_type_probability.CopyFrom(value.proto)

        self._intersection_type_probability = value
        self._intersection_type_probability._update_proto_references(self.proto.intersection_type_probability)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.JunctionSpawnPolicy):
        self.proto = proto
        self._distance_to_junction._update_proto_references(proto.distance_to_junction)
        self._intersection_type_probability._update_proto_references(proto.intersection_type_probability)


@register_wrapper(proto_type=pd_unified_generator_pb2.PositionOfInterestPolicy)
class PositionOfInterestPolicy(ProtoMessageClass):
    """
    Specifies a type of policy to be applied when spawning agents on a lane.

    Args:
        lane_curvature_spawn_policy: :attr:`lane_curvature_spawn_policy`
        junction_spawn_policy: :attr:`junction_spawn_policy`
    Attributes:
        lane_curvature_spawn_policy:
        junction_spawn_policy:"""

    _proto_message = pd_unified_generator_pb2.PositionOfInterestPolicy

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.PositionOfInterestPolicy] = None,
        lane_curvature_spawn_policy: LaneCurvatureSpawnPolicy = None,
        junction_spawn_policy: JunctionSpawnPolicy = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.PositionOfInterestPolicy()
        self.proto = proto
        self._lane_curvature_spawn_policy = get_wrapper(proto_type=proto.lane_curvature_spawn_policy.__class__)(
            proto=proto.lane_curvature_spawn_policy
        )
        self._junction_spawn_policy = get_wrapper(proto_type=proto.junction_spawn_policy.__class__)(
            proto=proto.junction_spawn_policy
        )
        if lane_curvature_spawn_policy is not None:
            self.lane_curvature_spawn_policy = lane_curvature_spawn_policy
        if junction_spawn_policy is not None:
            self.junction_spawn_policy = junction_spawn_policy

    @property
    def lane_curvature_spawn_policy(self) -> LaneCurvatureSpawnPolicy:
        return self._lane_curvature_spawn_policy

    @lane_curvature_spawn_policy.setter
    def lane_curvature_spawn_policy(self, value: LaneCurvatureSpawnPolicy):
        self.proto.lane_curvature_spawn_policy.CopyFrom(value.proto)

        self._lane_curvature_spawn_policy = value
        self._lane_curvature_spawn_policy._update_proto_references(self.proto.lane_curvature_spawn_policy)

    @property
    def junction_spawn_policy(self) -> JunctionSpawnPolicy:
        return self._junction_spawn_policy

    @junction_spawn_policy.setter
    def junction_spawn_policy(self, value: JunctionSpawnPolicy):
        self.proto.junction_spawn_policy.CopyFrom(value.proto)

        self._junction_spawn_policy = value
        self._junction_spawn_policy._update_proto_references(self.proto.junction_spawn_policy)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.PositionOfInterestPolicy):
        self.proto = proto
        self._lane_curvature_spawn_policy._update_proto_references(proto.lane_curvature_spawn_policy)
        self._junction_spawn_policy._update_proto_references(proto.junction_spawn_policy)


@register_wrapper(proto_type=pd_unified_generator_pb2.AbsolutePositionRequest)
class AbsolutePositionRequest(ProtoMessageClass):
    """
    Returns a location based on an exact coordinate system. Note that when a vehicle agent is placed using an Absolute
    Position Request, the vehicle may not be placed in the exact position specified by the user.

    The vehicle will be placed in the center of, and aligned with, the lane which is closest to the position requested
    by the user, as long as the initially requested position falls within a drivable lane.

    If a :attr:`lane_id` is provided, the vehicle will be placed in the center of, and aligned with, that lane,
    regardless of what position is requested inside the Absolute Position Request.

    Args:
        position: :attr:`position`
        rotation: :attr:`rotation`
        lane_id: :attr:`lane_id`
        resolve_z: :attr:`resolve_z`
    Attributes:
        position: `x`, `y`, `z` coordinates in world coordinates of the position desired.
        rotation: 3x3 Rotation matrix which specifies the rotation of the returned location. If not provided, rotation will be
            determined by the lane underneath the specified :attr:`position`.
        lane_id: Specify the id of a lane on which the position should be returned. If no id is provided, the lane id will be
            inferred from the :attr:`position` specified.
            In cases where the lane is inferred, the lane will be inferred from one of the following lane types::

                "Drivable"
                "Sidewalk"
                "Parking"
                "ParkingAisle"
                "ParkingSpace"
        resolve_z: Flag to control whether the `z` value of the returned location is automatically resolved. If set to `True`, the
            returned `z` location will be the ground location of the specified `x` and `y` in :attr:`position`. If set to
            `False`, the returned `z` location will be that specified in :attr:`position`.

            If not provided, will be set to `True`."""

    _proto_message = pd_unified_generator_pb2.AbsolutePositionRequest

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.AbsolutePositionRequest] = None,
        position: _pd_types_pb2.Float3 = None,
        rotation: _pd_types_pb2.Float3x3 = None,
        lane_id: int = None,
        resolve_z: bool = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.AbsolutePositionRequest()
        self.proto = proto
        self._position = get_wrapper(proto_type=proto.position.__class__)(proto=proto.position)
        self._rotation = get_wrapper(proto_type=proto.rotation.__class__)(proto=proto.rotation)
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if lane_id is not None:
            self.lane_id = lane_id
        if resolve_z is not None:
            self.resolve_z = resolve_z

    @property
    def position(self) -> _pd_types_pb2.Float3:
        return self._position

    @position.setter
    def position(self, value: _pd_types_pb2.Float3):
        self.proto.position.CopyFrom(value.proto)

        self._position = value
        self._position._update_proto_references(self.proto.position)

    @property
    def rotation(self) -> _pd_types_pb2.Float3x3:
        return self._rotation

    @rotation.setter
    def rotation(self, value: _pd_types_pb2.Float3x3):
        self.proto.rotation.CopyFrom(value.proto)

        self._rotation = value
        self._rotation._update_proto_references(self.proto.rotation)

    @property
    def lane_id(self) -> int:
        return self.proto.lane_id

    @lane_id.setter
    def lane_id(self, value: int):
        self.proto.lane_id = value

    @property
    def resolve_z(self) -> bool:
        return self.proto.resolve_z

    @resolve_z.setter
    def resolve_z(self, value: bool):
        self.proto.resolve_z = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.AbsolutePositionRequest):
        self.proto = proto
        self._position._update_proto_references(proto.position)
        self._rotation._update_proto_references(proto.rotation)


@register_wrapper(proto_type=pd_unified_generator_pb2.PathTimeRelativePositionRequest)
class PathTimeRelativePositionRequest(ProtoMessageClass):
    """
    Generator to place an agent in a position and path that will cause it to intersect with another agent's path at a
    specified time.

    Only works on `DRIVABLE` lanes and requires the agent with which an intersecting path is desired to the placed first.

    Args:
        agent_tags: :attr:`agent_tags`
        time_to_path: :attr:`time_to_path`
        time_along_path: :attr:`time_along_path`
        incident_angle: :attr:`incident_angle`
    Attributes:
        agent_tags: The tag(s) of the agent(s) with which the agent being placed should intersect paths with.
        time_to_path: The time in seconds required for the agent being placed to intersect with the agent(s) specified in
            :attr:`agent_tags`. The minimum and maximum of a continuous distribution must be specified and the returned
            time_to_path will be randomly sampled from this distribution.

            If not provided, will default to 0. If both :attr:`time_to_path` and :attr:`time_along_path` are 0,
            a :attr:`PositionRequest.longitudinal_offset` and/or :attr:`PositionRequest.lateral_offset` must be specified.
        time_along_path: Time for agent(s) specified by agent_tag to reach intersection point. The minimum and maximum of a continuous
            distribution must be specified and the returned time_along_path will be randomly sampled from this distribution.

            If not provided, will default to 0. If both :attr:`time_to_path` and :attr:`time_along_path` are 0,
            a :attr:`PositionRequest.longitudinal_offset` and/or :attr:`PositionRequest.lateral_offset` must be specified.
        incident_angle: Specifies the angle at which the paths of the agent being placed and the agent(s) specified in :attr:`agent_tags`
            cross. Angle is specified in radians in the form of the minimums and maximums of a continuous uniform distribution.
            If not provided, paths can cross at any angle."""

    _proto_message = pd_unified_generator_pb2.PathTimeRelativePositionRequest

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.PathTimeRelativePositionRequest] = None,
        agent_tags: List[str] = None,
        time_to_path: _pd_distributions_pb2.ContinousUniformDistribution = None,
        time_along_path: _pd_distributions_pb2.ContinousUniformDistribution = None,
        incident_angle: _pd_distributions_pb2.ContinousUniformDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.PathTimeRelativePositionRequest()
        self.proto = proto
        self._time_to_path = get_wrapper(proto_type=proto.time_to_path.__class__)(proto=proto.time_to_path)
        self._time_along_path = get_wrapper(proto_type=proto.time_along_path.__class__)(proto=proto.time_along_path)
        self._incident_angle = get_wrapper(proto_type=proto.incident_angle.__class__)(proto=proto.incident_angle)
        self._agent_tags = ProtoListWrapper(
            container=[str(v) for v in proto.agent_tags], attr_name="agent_tags", list_owner=self
        )
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if time_to_path is not None:
            self.time_to_path = time_to_path
        if time_along_path is not None:
            self.time_along_path = time_along_path
        if incident_angle is not None:
            self.incident_angle = incident_angle

    @property
    def agent_tags(self) -> List[str]:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: List[str]):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    @property
    def time_to_path(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._time_to_path

    @time_to_path.setter
    def time_to_path(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.time_to_path.CopyFrom(value.proto)

        self._time_to_path = value
        self._time_to_path._update_proto_references(self.proto.time_to_path)

    @property
    def time_along_path(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._time_along_path

    @time_along_path.setter
    def time_along_path(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.time_along_path.CopyFrom(value.proto)

        self._time_along_path = value
        self._time_along_path._update_proto_references(self.proto.time_along_path)

    @property
    def incident_angle(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._incident_angle

    @incident_angle.setter
    def incident_angle(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.incident_angle.CopyFrom(value.proto)

        self._incident_angle = value
        self._incident_angle._update_proto_references(self.proto.incident_angle)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.PathTimeRelativePositionRequest):
        self.proto = proto
        self._time_to_path._update_proto_references(proto.time_to_path)
        self._time_along_path._update_proto_references(proto.time_along_path)
        self._incident_angle._update_proto_references(proto.incident_angle)


@register_wrapper(proto_type=pd_unified_generator_pb2.LocationRelativePositionRequest)
class LocationRelativePositionRequest(ProtoMessageClass):
    """
    Returns a location in a position relative to a tagged agent. Requires the tagged agent to be placed first.

    Args:
        agent_tags: :attr:`agent_tags`
        max_spawn_radius: :attr:`max_spawn_radius`
        lane_spawn_policy: :attr:`lane_spawn_policy`
    Attributes:
        agent_tags: The tag(s) of the agent(s) relative to which the returned location should be calculated.
        max_spawn_radius: The maximum radius in meters from the agent in :attr:`agent_tags` the returned location can exist. Any value greater
            than 0.0 can be specified.

            Default: 150.0
        lane_spawn_policy: Specifies a lane criteria on which the returned location can exist. If not provided, no restrictions are placed on
            what lane type the returned location can exist on."""

    _proto_message = pd_unified_generator_pb2.LocationRelativePositionRequest

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.LocationRelativePositionRequest] = None,
        agent_tags: List[str] = None,
        max_spawn_radius: float = None,
        lane_spawn_policy: LaneSpawnPolicy = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.LocationRelativePositionRequest()
        self.proto = proto
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(
            proto=proto.lane_spawn_policy
        )
        self._agent_tags = ProtoListWrapper(
            container=[str(v) for v in proto.agent_tags], attr_name="agent_tags", list_owner=self
        )
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if max_spawn_radius is not None:
            self.max_spawn_radius = max_spawn_radius
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy

    @property
    def agent_tags(self) -> List[str]:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: List[str]):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    @property
    def max_spawn_radius(self) -> float:
        return self.proto.max_spawn_radius

    @max_spawn_radius.setter
    def max_spawn_radius(self, value: float):
        self.proto.max_spawn_radius = value

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self.proto.lane_spawn_policy.CopyFrom(value.proto)

        self._lane_spawn_policy = value
        self._lane_spawn_policy._update_proto_references(self.proto.lane_spawn_policy)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.LocationRelativePositionRequest):
        self.proto = proto
        self._lane_spawn_policy._update_proto_references(proto.lane_spawn_policy)


@register_wrapper(proto_type=pd_unified_generator_pb2.LaneSpawnPolicy)
class LaneSpawnPolicy(ProtoMessageClass):
    """
    Specifies a lane type (or multiple) on which a location can be returned.

    Args:
        min_num_lanes_in_same_direction: :attr:`min_num_lanes_in_same_direction`
        lane_type: :attr:`lane_type`
        min_num_lanes_in_opposite_direction: :attr:`min_num_lanes_in_opposite_direction`
        lateral_offset: :attr:`lateral_offset`
        bicycles_only_in_bike_lanes: :attr:`bicycles_only_in_bike_lanes`
        nearby_asset_policy: :attr:`nearby_asset_policy`
        road_type: :attr:`road_type`
        position_of_interest_policy: :attr:`position_of_interest_policy`
        min_path_length: :attr:`min_path_length`
        min_length_behind: :attr:`min_length_behind`
        on_road_parking_angle_distribution: :attr:`on_road_parking_angle_distribution`
        lane_decoration_distribution: :attr:`lane_decoration_distribution`
    Attributes:
        min_num_lanes_in_same_direction: Specifies the minimum number of lanes that should exist in the same direction on the road on which the returned
            location is located. Must be an integer greater than 0. If not provided, will use 0.
        lane_type: Specifies the lane types on which the returned location should exist and their associated probabilities.

            Valid lane types are::

                "Drivable"
                "NonDrivable"
                "Parking"
                "Shoulder"
                "Biking"
                "Crosswalk"
                "ParkingAisle"
                "ParkingSpace"
                "Sidewalk"
        min_num_lanes_in_opposite_direction: Specifies the minimum number of lanes that should exist in the opposite direction on the road on which the returned
            location is located. Must be an integer greater than 0.
            Default: 0
        lateral_offset: Specifies the lateral offset in lanes of the returned location. Values in the range from -1.0 to 1.0 are valid.
            Negative values offset to the left of the lane, positive values to the right. If not provided, will use 0.0.
        bicycles_only_in_bike_lanes: Flag to specify if bicycles should only be spawned in bike lanes.
            Default: True
        nearby_asset_policy: Specifies a policy which controls assets near which the returned location should be located.
        road_type: Specifies the road types on which the returned location should exist and their associated probabilities. If not
            provided, no restrictions are placed on the type of road on which a returned location can be located.

            Valid values::

                "Motorway"
                "Residential"
                "Trunk"
                "Primary"
                "Secondary"
                "Tertiary"
                "Unclassified"
                "Motorway_Link"
                "Truck_Link"
                "Primary_Link"
                "Secondary_Link"
                "Tertiary_Link"
                "Service"
                "Driveway"
                "Parking_Aisle"
                "Driveway_Parking_Entry"
        position_of_interest_policy: Specifies a policy which controls the proximity of a returned location to a particular position of interest.
        min_path_length: Specifies the minimum length (in meters) of the path (ahead of the spawn location) on which the returned location
            exists. `min_path_length` is specified as a `CenterSpreadConfig` with a minimum and maximum value. The exact
            `min_path_length` for a returned location will be randomly sampled from this distribution.

            This parameter does not have an effect if spawning in a driveway, parking aisle or parking space. If not provided,
            200.0 will be used.
        min_length_behind: Specifies the minimum length (in meters) of the path (behind the spawn location) on which the returned location
            exists. `min_path_length` is specified as a `CenterSpreadConfig` with a minimum and maximum value. The exact
            `min_path_length` for a returned location will be randomly sampled from this distribution.

            This parameter does not have an effect if spawning in a driveway, parking aisle or parking space. If not provided,
            100.0 will be used.
        on_road_parking_angle_distribution: Specifies the type of parking spaces which should exist on stree parking spaces if a location on street parking
            spaces is returned by this `LaneSpawnPolicy`. Parking space types for parking spaces in lots are specified in
            :obj:`ParkingSpaceData`.

            Valid values::

                "PARALLEL"
                "ANGLE_30"
                "ANGLE_45"
                "ANGLE_60"
                "PERPENDICULAR"

        lane_decoration_distribution: Specifies the distribution of lane decorations and their associated probabilities if object decorations are enabled.
            If not provided, no lane decorations are applied. See :obj:`ObjectDecorationParams` for list of valid values.
    """

    _proto_message = pd_unified_generator_pb2.LaneSpawnPolicy

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.LaneSpawnPolicy] = None,
        min_num_lanes_in_same_direction: int = None,
        lane_type: _pd_distributions_pb2.EnumDistribution = None,
        min_num_lanes_in_opposite_direction: int = None,
        lateral_offset: CenterSpreadConfig = None,
        bicycles_only_in_bike_lanes: bool = None,
        nearby_asset_policy: NearbyAssetPolicy = None,
        road_type: _pd_distributions_pb2.EnumDistribution = None,
        position_of_interest_policy: List[PositionOfInterestPolicy] = None,
        min_path_length: CenterSpreadConfig = None,
        min_length_behind: CenterSpreadConfig = None,
        on_road_parking_angle_distribution: _pd_distributions_pb2.EnumDistribution = None,
        lane_decoration_distribution: _pd_distributions_pb2.EnumDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.LaneSpawnPolicy()
        self.proto = proto
        self._lane_type = get_wrapper(proto_type=proto.lane_type.__class__)(proto=proto.lane_type)
        self._lateral_offset = get_wrapper(proto_type=proto.lateral_offset.__class__)(proto=proto.lateral_offset)
        self._nearby_asset_policy = get_wrapper(proto_type=proto.nearby_asset_policy.__class__)(
            proto=proto.nearby_asset_policy
        )
        self._road_type = get_wrapper(proto_type=proto.road_type.__class__)(proto=proto.road_type)
        self._position_of_interest_policy = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.position_of_interest_policy],
            attr_name="position_of_interest_policy",
            list_owner=self,
        )
        self._min_path_length = get_wrapper(proto_type=proto.min_path_length.__class__)(proto=proto.min_path_length)
        self._min_length_behind = get_wrapper(proto_type=proto.min_length_behind.__class__)(
            proto=proto.min_length_behind
        )
        self._on_road_parking_angle_distribution = get_wrapper(
            proto_type=proto.on_road_parking_angle_distribution.__class__
        )(proto=proto.on_road_parking_angle_distribution)
        self._lane_decoration_distribution = get_wrapper(proto_type=proto.lane_decoration_distribution.__class__)(
            proto=proto.lane_decoration_distribution
        )
        if min_num_lanes_in_same_direction is not None:
            self.min_num_lanes_in_same_direction = min_num_lanes_in_same_direction
        if lane_type is not None:
            self.lane_type = lane_type
        if min_num_lanes_in_opposite_direction is not None:
            self.min_num_lanes_in_opposite_direction = min_num_lanes_in_opposite_direction
        if lateral_offset is not None:
            self.lateral_offset = lateral_offset
        if bicycles_only_in_bike_lanes is not None:
            self.bicycles_only_in_bike_lanes = bicycles_only_in_bike_lanes
        if nearby_asset_policy is not None:
            self.nearby_asset_policy = nearby_asset_policy
        if road_type is not None:
            self.road_type = road_type
        if position_of_interest_policy is not None:
            self.position_of_interest_policy = position_of_interest_policy
        if min_path_length is not None:
            self.min_path_length = min_path_length
        if min_length_behind is not None:
            self.min_length_behind = min_length_behind
        if on_road_parking_angle_distribution is not None:
            self.on_road_parking_angle_distribution = on_road_parking_angle_distribution
        if lane_decoration_distribution is not None:
            self.lane_decoration_distribution = lane_decoration_distribution

    @property
    def min_num_lanes_in_same_direction(self) -> int:
        return self.proto.min_num_lanes_in_same_direction

    @min_num_lanes_in_same_direction.setter
    def min_num_lanes_in_same_direction(self, value: int):
        self.proto.min_num_lanes_in_same_direction = value

    @property
    def lane_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._lane_type

    @lane_type.setter
    def lane_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.lane_type.CopyFrom(value.proto)

        self._lane_type = value
        self._lane_type._update_proto_references(self.proto.lane_type)

    @property
    def min_num_lanes_in_opposite_direction(self) -> int:
        return self.proto.min_num_lanes_in_opposite_direction

    @min_num_lanes_in_opposite_direction.setter
    def min_num_lanes_in_opposite_direction(self, value: int):
        self.proto.min_num_lanes_in_opposite_direction = value

    @property
    def lateral_offset(self) -> CenterSpreadConfig:
        return self._lateral_offset

    @lateral_offset.setter
    def lateral_offset(self, value: CenterSpreadConfig):
        self.proto.lateral_offset.CopyFrom(value.proto)

        self._lateral_offset = value
        self._lateral_offset._update_proto_references(self.proto.lateral_offset)

    @property
    def bicycles_only_in_bike_lanes(self) -> bool:
        return self.proto.bicycles_only_in_bike_lanes

    @bicycles_only_in_bike_lanes.setter
    def bicycles_only_in_bike_lanes(self, value: bool):
        self.proto.bicycles_only_in_bike_lanes = value

    @property
    def nearby_asset_policy(self) -> NearbyAssetPolicy:
        return self._nearby_asset_policy

    @nearby_asset_policy.setter
    def nearby_asset_policy(self, value: NearbyAssetPolicy):
        self.proto.nearby_asset_policy.CopyFrom(value.proto)

        self._nearby_asset_policy = value
        self._nearby_asset_policy._update_proto_references(self.proto.nearby_asset_policy)

    @property
    def road_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._road_type

    @road_type.setter
    def road_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.road_type.CopyFrom(value.proto)

        self._road_type = value
        self._road_type._update_proto_references(self.proto.road_type)

    @property
    def position_of_interest_policy(self) -> List[PositionOfInterestPolicy]:
        return self._position_of_interest_policy

    @position_of_interest_policy.setter
    def position_of_interest_policy(self, value: List[PositionOfInterestPolicy]):
        self._position_of_interest_policy.clear()
        for v in value:
            self._position_of_interest_policy.append(v)

    @property
    def min_path_length(self) -> CenterSpreadConfig:
        return self._min_path_length

    @min_path_length.setter
    def min_path_length(self, value: CenterSpreadConfig):
        self.proto.min_path_length.CopyFrom(value.proto)

        self._min_path_length = value
        self._min_path_length._update_proto_references(self.proto.min_path_length)

    @property
    def min_length_behind(self) -> CenterSpreadConfig:
        return self._min_length_behind

    @min_length_behind.setter
    def min_length_behind(self, value: CenterSpreadConfig):
        self.proto.min_length_behind.CopyFrom(value.proto)

        self._min_length_behind = value
        self._min_length_behind._update_proto_references(self.proto.min_length_behind)

    @property
    def on_road_parking_angle_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._on_road_parking_angle_distribution

    @on_road_parking_angle_distribution.setter
    def on_road_parking_angle_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.on_road_parking_angle_distribution.CopyFrom(value.proto)

        self._on_road_parking_angle_distribution = value
        self._on_road_parking_angle_distribution._update_proto_references(self.proto.on_road_parking_angle_distribution)

    @property
    def lane_decoration_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._lane_decoration_distribution

    @lane_decoration_distribution.setter
    def lane_decoration_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.lane_decoration_distribution.CopyFrom(value.proto)

        self._lane_decoration_distribution = value
        self._lane_decoration_distribution._update_proto_references(self.proto.lane_decoration_distribution)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.LaneSpawnPolicy):
        self.proto = proto
        self._lane_type._update_proto_references(proto.lane_type)
        self._lateral_offset._update_proto_references(proto.lateral_offset)
        self._nearby_asset_policy._update_proto_references(proto.nearby_asset_policy)
        self._road_type._update_proto_references(proto.road_type)
        for i, v in enumerate(self.position_of_interest_policy):
            v._update_proto_references(self.proto.position_of_interest_policy[i])
        self._min_path_length._update_proto_references(proto.min_path_length)
        self._min_length_behind._update_proto_references(proto.min_length_behind)
        self._on_road_parking_angle_distribution._update_proto_references(proto.on_road_parking_angle_distribution)
        self._lane_decoration_distribution._update_proto_references(proto.lane_decoration_distribution)


@register_wrapper(proto_type=pd_unified_generator_pb2.RoadPitchPositionRequest)
class RoadPitchPositionRequest(ProtoMessageClass):
    """
    Selects a location based on the difference in slope of the road on either side of the returned location.

    Args:
        road_pitch: :attr:`road_pitch`
        lane_spawn_policy: :attr:`lane_spawn_policy`
        bin_pitch_points: :attr:`bin_pitch_points`
        bin_width: :attr:`bin_width`
    Attributes:
        road_pitch: Specifies the desired difference in pitch angle (in radians) which should exist in the road segments on either
            side of the returned location. The desired pitch is specified as a :obj:`ContinousUniformDistribution` which is
            randomly sampled from in searching for a location to return.
        lane_spawn_policy: Specifies a policy for the types of lanes on which a location can be returned.
        bin_pitch_points: Flag to control whether the specified :attr:`road_pitch` distribution is split into bins when sampled.
            This results in a more even distribution of pitches when the `RoadPitchPositionRequest` is called multiple times.
            Default: True
        bin_width: When :attr:`bin_pitch_points` is `True`, specifies the width in radians of the each bin.
            Default: 0.0087"""

    _proto_message = pd_unified_generator_pb2.RoadPitchPositionRequest

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.RoadPitchPositionRequest] = None,
        road_pitch: _pd_distributions_pb2.ContinousUniformDistribution = None,
        lane_spawn_policy: LaneSpawnPolicy = None,
        bin_pitch_points: bool = None,
        bin_width: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.RoadPitchPositionRequest()
        self.proto = proto
        self._road_pitch = get_wrapper(proto_type=proto.road_pitch.__class__)(proto=proto.road_pitch)
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(
            proto=proto.lane_spawn_policy
        )
        if road_pitch is not None:
            self.road_pitch = road_pitch
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy
        if bin_pitch_points is not None:
            self.bin_pitch_points = bin_pitch_points
        if bin_width is not None:
            self.bin_width = bin_width

    @property
    def road_pitch(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._road_pitch

    @road_pitch.setter
    def road_pitch(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.road_pitch.CopyFrom(value.proto)

        self._road_pitch = value
        self._road_pitch._update_proto_references(self.proto.road_pitch)

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self.proto.lane_spawn_policy.CopyFrom(value.proto)

        self._lane_spawn_policy = value
        self._lane_spawn_policy._update_proto_references(self.proto.lane_spawn_policy)

    @property
    def bin_pitch_points(self) -> bool:
        return self.proto.bin_pitch_points

    @bin_pitch_points.setter
    def bin_pitch_points(self, value: bool):
        self.proto.bin_pitch_points = value

    @property
    def bin_width(self) -> float:
        return self.proto.bin_width

    @bin_width.setter
    def bin_width(self, value: float):
        self.proto.bin_width = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.RoadPitchPositionRequest):
        self.proto = proto
        self._road_pitch._update_proto_references(proto.road_pitch)
        self._lane_spawn_policy._update_proto_references(proto.lane_spawn_policy)


@register_wrapper(proto_type=pd_unified_generator_pb2.NearbyAssetPolicy)
class NearbyAssetPolicy(ProtoMessageClass):
    """
    Policy that allows for spawn placement to be near a specified asset.

    Args:
        search_radius: :attr:`search_radius`
        num_assets: :attr:`num_assets`
        asset_tags: :attr:`asset_tags`
    Attributes:
        search_radius: The radius from the asset specified in :attr:`asset_tags` within which the policy should return a location.
            Radius is specified as a :obj:`CenterSpreadConfig` which is randomly sampled from during scenario generation.
        num_assets: The number of assets to spawn, specified as a :obj:`MinMaxConfigInt` which is randomly sampled from during
            scenario generation.
        asset_tags: The names of assets that the policy should return positions near to, subject to the parameters in
            :attr:`search_radius`."""

    _proto_message = pd_unified_generator_pb2.NearbyAssetPolicy

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.NearbyAssetPolicy] = None,
        search_radius: CenterSpreadConfig = None,
        num_assets: MinMaxConfigInt = None,
        asset_tags: List[str] = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.NearbyAssetPolicy()
        self.proto = proto
        self._search_radius = get_wrapper(proto_type=proto.search_radius.__class__)(proto=proto.search_radius)
        self._num_assets = get_wrapper(proto_type=proto.num_assets.__class__)(proto=proto.num_assets)
        if search_radius is not None:
            self.search_radius = search_radius
        if num_assets is not None:
            self.num_assets = num_assets
        self._asset_tags = ProtoListWrapper(
            container=[str(v) for v in proto.asset_tags], attr_name="asset_tags", list_owner=self
        )
        if asset_tags is not None:
            self.asset_tags = asset_tags

    @property
    def search_radius(self) -> CenterSpreadConfig:
        return self._search_radius

    @search_radius.setter
    def search_radius(self, value: CenterSpreadConfig):
        self.proto.search_radius.CopyFrom(value.proto)

        self._search_radius = value
        self._search_radius._update_proto_references(self.proto.search_radius)

    @property
    def num_assets(self) -> MinMaxConfigInt:
        return self._num_assets

    @num_assets.setter
    def num_assets(self, value: MinMaxConfigInt):
        self.proto.num_assets.CopyFrom(value.proto)

        self._num_assets = value
        self._num_assets._update_proto_references(self.proto.num_assets)

    @property
    def asset_tags(self) -> List[str]:
        return self._asset_tags

    @asset_tags.setter
    def asset_tags(self, value: List[str]):
        self._asset_tags.clear()
        for v in value:
            self._asset_tags.append(v)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.NearbyAssetPolicy):
        self.proto = proto
        self._search_radius._update_proto_references(proto.search_radius)
        self._num_assets._update_proto_references(proto.num_assets)


@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleSpawnData)
class VehicleSpawnData(ProtoMessageClass):
    """
    Parameters to controls a vehicle's spawn characteristics and movement behavior.

    Args:
        vehicle_behavior: :attr:`vehicle_behavior`
        vehicle_peripheral: :attr:`vehicle_peripheral`
        agent_spawn_data: :attr:`agent_spawn_data`
    Attributes:
        vehicle_behavior: Parameters to control the movement behavior of a vehicle. If not provided, will default to default
            values in :obj:`VehicleBehavior`.
        vehicle_peripheral: Parameters that control vehicle peripherals (eg. accessories, color, occupants, etc.). If not provided, will default
            to default values in :obj:`VehiclePeripheral`.
        agent_spawn_data: Specifies spawn data which applies to the agents. If not provided, will default to default
            values in :obj:`AgentSpawnData`."""

    _proto_message = pd_unified_generator_pb2.VehicleSpawnData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.VehicleSpawnData] = None,
        vehicle_behavior: VehicleBehavior = None,
        vehicle_peripheral: VehiclePeripheral = None,
        agent_spawn_data: AgentSpawnData = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleSpawnData()
        self.proto = proto
        self._vehicle_behavior = get_wrapper(proto_type=proto.vehicle_behavior.__class__)(proto=proto.vehicle_behavior)
        self._vehicle_peripheral = get_wrapper(proto_type=proto.vehicle_peripheral.__class__)(
            proto=proto.vehicle_peripheral
        )
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        if vehicle_behavior is not None:
            self.vehicle_behavior = vehicle_behavior
        if vehicle_peripheral is not None:
            self.vehicle_peripheral = vehicle_peripheral
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data

    @property
    def vehicle_behavior(self) -> VehicleBehavior:
        return self._vehicle_behavior

    @vehicle_behavior.setter
    def vehicle_behavior(self, value: VehicleBehavior):
        self.proto.vehicle_behavior.CopyFrom(value.proto)

        self._vehicle_behavior = value
        self._vehicle_behavior._update_proto_references(self.proto.vehicle_behavior)

    @property
    def vehicle_peripheral(self) -> VehiclePeripheral:
        return self._vehicle_peripheral

    @vehicle_peripheral.setter
    def vehicle_peripheral(self, value: VehiclePeripheral):
        self.proto.vehicle_peripheral.CopyFrom(value.proto)

        self._vehicle_peripheral = value
        self._vehicle_peripheral._update_proto_references(self.proto.vehicle_peripheral)

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.VehicleSpawnData):
        self.proto = proto
        self._vehicle_behavior._update_proto_references(proto.vehicle_behavior)
        self._vehicle_peripheral._update_proto_references(proto.vehicle_peripheral)
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleBehavior)
class VehicleBehavior(ProtoMessageClass):
    """
    Parameters which direct a vehicle's movement behavior (eg. lane change, speed, etc.).

    Note that in some cases, the Vehicle Behavior exhibited in the simulation may differ from that which the user has directed.
    Vehicle Behavior is affected by obstacles near the vehicle, curvature of the road, end-of-lanes the vehicle is
    approaching and the slope of the road.

    Args:
        start_speed: :attr:`start_speed`
        target_speed: :attr:`target_speed`
        ignore_speed_limit: :attr:`ignore_speed_limit`
        lane_offset: :attr:`lane_offset`
        lane_drift_scale: :attr:`lane_drift_scale`
        lane_drift_amplitude: :attr:`lane_drift_amplitude`
        lane_change_probability: :attr:`lane_change_probability`
        lane_change_cooldown: :attr:`lane_change_cooldown`
        enable_dynamic_lane_selection: :attr:`enable_dynamic_lane_selection`
        start_gear: :attr:`start_gear`
        start_separation_time: :attr:`start_separation_time`
        target_separation_time: :attr:`target_separation_time`
        vehicle_aggression: :attr:`vehicle_aggression`
        ignore_obstacle_types: :attr:`ignore_obstacle_types`
        parking_scenario_goal: :attr:`parking_scenario_goal`
        parking_scenario_time: :attr:`parking_scenario_time`
    Attributes:
        start_speed: Specifies the start speed of a vehicle at the beginning of a scenario. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        target_speed: Specifies the target speed of the vehicle. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.

            Will not cause vehicle to exceed the speed limit of a road unless :attr:`ignore_speed_limit` is set to `True`.
        ignore_speed_limit: Flag to control whether vehicle will ignore speed limits in attempting to achieve the :attr:`target_speed`.
            Default: False
        lane_offset: Specifies the lateral offset of the vehicle in the vehicle's motion plan relative to lane center line. Possible
            values are floats from -1.0 to 1.0, and represent the proportion of the lane's half width to offset laterally.
            Positive values offset to the right and negative values offset to the left.

            If not provided, will default to 0.0. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        lane_drift_scale: Controls the frequency of weaving within the vehicle's lanes during travel. Weaving is modelled as a perlin noise
            driven wave. If not provided, will default to 0.0. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        lane_drift_amplitude: Controls the amplitude of weaving within the vehicle's lanes during travel. Weaving is modelled as a perlin noise
            driven wave. If not provided, will default to 0.0. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        lane_change_probability: Specifies the probability that a vehicle will make a lane change.
            Evaluated once every second. If evaluated to true, vehicle will lane change if conditions allow
            (having lanes to change to, no obstables in those lanes or in lane change path)
            Values can range from 0.0 to 1.0. If not provided, defaults to zero. Value is specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        lane_change_cooldown: Specifies the time in seconds during which another lane change cannot occur after the vehicle undergoes a lane
            change. If not provided, a default value of 10 is used. Value is specified as a
            ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        enable_dynamic_lane_selection: Boolean flag to specify whether lane change decisions are made dynamically while the scenario is being simulated.
            Default: False
        start_gear: Specifies the gear that the vehicle should start in at the beginning of scenario generation.
            Default: :attr:`Gear.DRIVE`
        start_separation_time: Specifies the spacing, in seconds, that should exist between vehicles in the same lane at the start of the scenario.
            Value is specified as a :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        target_separation_time: Specifies the spacing, in seconds, that targeted between vehicles in the same lane over the course of the scenario.
            Value is specified as a :obj:`ContinousUniformDistribution` which is randomly sampled from during scenario generation.
        vehicle_aggression: Specifies a float measurement of the level of aggression with which the vehicle should drive. Impacts values such
            as lane change speed, abruptness of turns. Also multiplies the set :attr:`target_speed` to define the speed that
            will be targeted by the vehicle during the scenario.

            Must be a float greater than 0.0 if specified. If not specified, a default value is used.
        ignore_obstacle_types: Specifies a list of :obj:`ObstacleType` that the vehicle should ignore in driving.
        parking_scenario_goal: Specifies the goal position for the vehicle to target in a parking/unparking scenario. Only
            :obj:`AbsolutePositionRequest` and :obj:`LaneSpawnPolicy` position request types are supported.

            Must be provided if a parking/unparking scenario is desired. Will result in a scenario with standard vehicle
            driving behavior if not provided.

            To specify a parking scenario, set a `lane_spawn_policy` that specifies a `ParkingSpace` as the goal. To control
            whether the parking occurs in a parking lot or on the street, specify a `road_type` within the `lane_spawn_policy`
            as appropriate.

            To specify an unparking scenario, set a :obj:`position_request` in the generator to a `LaneSpawnPolicy` that
            specifies a parking space, and use this :attr:`parking_scenario_goal` to specify only a `road_type` that corresponds
            to the type of road the vehicle should exit onto. Unparking is not supported on streets.

            Examples::

                >>> # Parking in Parking Lot
                >>> {
                >>>    lane_spawn_policy: {
                >>>        lane_type: {
                >>>            probabilities: {
                >>>                "ParkingSpace": 1.0
                >>>            }
                >>>        },
                >>>        road_type: {
                >>>            probabilities: {
                >>>                "Parking_Aisle": 1.0
                >>>            }
                >>>        }
                >>>    }
                >>> }
                >>>
                >>> # Parking on street
                >>> {
                >>>     lane_spawn_policy: {
                >>>         lane_type: {
                >>>             probabilities: {
                >>>                 "ParkingSpace": 1.0
                >>>             }
                >>>         },
                >>>         road_type: {
                >>>             probabilities: {
                >>>                 "Primary": 1.0
                >>>             }
                >>>         }
                >>>     }
                >>> }
                >>>
                >>> # Unparking in Parking Lot
                >>> {
                >>>     lane_spawn_policy: {
                >>>         lane_type: {
                >>>             probabilities: {
                >>>                 "ParkingSpace": 1.0
                >>>             }
                >>>         },
                >>>         road_type: {
                >>>             probabilities: {
                >>>                 "ParkingAisle": 1.0
                >>>             }
                >>>         }
                >>>     }
                >>> }
        parking_scenario_time: Specifies the time (in seconds) it takes to reach the end of the parking maneuver assuming constant acceleration
            from the initial speed to the targe speed. Does not account for vehicle slow downs due to obstacles etc. If not
            provided, will use a value 5s."""

    _proto_message = pd_unified_generator_pb2.VehicleBehavior

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.VehicleBehavior] = None,
        start_speed: _pd_distributions_pb2.ContinousUniformDistribution = None,
        target_speed: _pd_distributions_pb2.ContinousUniformDistribution = None,
        ignore_speed_limit: bool = None,
        lane_offset: _pd_distributions_pb2.ContinousUniformDistribution = None,
        lane_drift_scale: _pd_distributions_pb2.ContinousUniformDistribution = None,
        lane_drift_amplitude: _pd_distributions_pb2.ContinousUniformDistribution = None,
        lane_change_probability: _pd_distributions_pb2.ContinousUniformDistribution = None,
        lane_change_cooldown: _pd_distributions_pb2.ContinousUniformDistribution = None,
        enable_dynamic_lane_selection: bool = None,
        start_gear: Gear = None,
        start_separation_time: _pd_distributions_pb2.ContinousUniformDistribution = None,
        target_separation_time: _pd_distributions_pb2.ContinousUniformDistribution = None,
        vehicle_aggression: _pd_distributions_pb2.ContinousUniformDistribution = None,
        ignore_obstacle_types: List[ObstacleType] = None,
        parking_scenario_goal: PositionRequest = None,
        parking_scenario_time: _pd_distributions_pb2.ContinousUniformDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleBehavior()
        self.proto = proto
        self._start_speed = get_wrapper(proto_type=proto.start_speed.__class__)(proto=proto.start_speed)
        self._target_speed = get_wrapper(proto_type=proto.target_speed.__class__)(proto=proto.target_speed)
        self._lane_offset = get_wrapper(proto_type=proto.lane_offset.__class__)(proto=proto.lane_offset)
        self._lane_drift_scale = get_wrapper(proto_type=proto.lane_drift_scale.__class__)(proto=proto.lane_drift_scale)
        self._lane_drift_amplitude = get_wrapper(proto_type=proto.lane_drift_amplitude.__class__)(
            proto=proto.lane_drift_amplitude
        )
        self._lane_change_probability = get_wrapper(proto_type=proto.lane_change_probability.__class__)(
            proto=proto.lane_change_probability
        )
        self._lane_change_cooldown = get_wrapper(proto_type=proto.lane_change_cooldown.__class__)(
            proto=proto.lane_change_cooldown
        )
        self._start_separation_time = get_wrapper(proto_type=proto.start_separation_time.__class__)(
            proto=proto.start_separation_time
        )
        self._target_separation_time = get_wrapper(proto_type=proto.target_separation_time.__class__)(
            proto=proto.target_separation_time
        )
        self._vehicle_aggression = get_wrapper(proto_type=proto.vehicle_aggression.__class__)(
            proto=proto.vehicle_aggression
        )
        self._parking_scenario_goal = get_wrapper(proto_type=proto.parking_scenario_goal.__class__)(
            proto=proto.parking_scenario_goal
        )
        self._parking_scenario_time = get_wrapper(proto_type=proto.parking_scenario_time.__class__)(
            proto=proto.parking_scenario_time
        )
        if start_speed is not None:
            self.start_speed = start_speed
        if target_speed is not None:
            self.target_speed = target_speed
        if ignore_speed_limit is not None:
            self.ignore_speed_limit = ignore_speed_limit
        if lane_offset is not None:
            self.lane_offset = lane_offset
        if lane_drift_scale is not None:
            self.lane_drift_scale = lane_drift_scale
        if lane_drift_amplitude is not None:
            self.lane_drift_amplitude = lane_drift_amplitude
        if lane_change_probability is not None:
            self.lane_change_probability = lane_change_probability
        if lane_change_cooldown is not None:
            self.lane_change_cooldown = lane_change_cooldown
        if enable_dynamic_lane_selection is not None:
            self.enable_dynamic_lane_selection = enable_dynamic_lane_selection
        if start_gear is not None:
            self.start_gear = start_gear
        if start_separation_time is not None:
            self.start_separation_time = start_separation_time
        if target_separation_time is not None:
            self.target_separation_time = target_separation_time
        if vehicle_aggression is not None:
            self.vehicle_aggression = vehicle_aggression
        self._ignore_obstacle_types = ProtoListWrapper(
            container=[ObstacleType(v) for v in proto.ignore_obstacle_types],
            attr_name="ignore_obstacle_types",
            list_owner=self,
        )
        if ignore_obstacle_types is not None:
            self.ignore_obstacle_types = ignore_obstacle_types
        if parking_scenario_goal is not None:
            self.parking_scenario_goal = parking_scenario_goal
        if parking_scenario_time is not None:
            self.parking_scenario_time = parking_scenario_time

    @property
    def start_speed(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._start_speed

    @start_speed.setter
    def start_speed(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.start_speed.CopyFrom(value.proto)

        self._start_speed = value
        self._start_speed._update_proto_references(self.proto.start_speed)

    @property
    def target_speed(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._target_speed

    @target_speed.setter
    def target_speed(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.target_speed.CopyFrom(value.proto)

        self._target_speed = value
        self._target_speed._update_proto_references(self.proto.target_speed)

    @property
    def ignore_speed_limit(self) -> bool:
        return self.proto.ignore_speed_limit

    @ignore_speed_limit.setter
    def ignore_speed_limit(self, value: bool):
        self.proto.ignore_speed_limit = value

    @property
    def lane_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_offset

    @lane_offset.setter
    def lane_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.lane_offset.CopyFrom(value.proto)

        self._lane_offset = value
        self._lane_offset._update_proto_references(self.proto.lane_offset)

    @property
    def lane_drift_scale(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_drift_scale

    @lane_drift_scale.setter
    def lane_drift_scale(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.lane_drift_scale.CopyFrom(value.proto)

        self._lane_drift_scale = value
        self._lane_drift_scale._update_proto_references(self.proto.lane_drift_scale)

    @property
    def lane_drift_amplitude(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_drift_amplitude

    @lane_drift_amplitude.setter
    def lane_drift_amplitude(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.lane_drift_amplitude.CopyFrom(value.proto)

        self._lane_drift_amplitude = value
        self._lane_drift_amplitude._update_proto_references(self.proto.lane_drift_amplitude)

    @property
    def lane_change_probability(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_change_probability

    @lane_change_probability.setter
    def lane_change_probability(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.lane_change_probability.CopyFrom(value.proto)

        self._lane_change_probability = value
        self._lane_change_probability._update_proto_references(self.proto.lane_change_probability)

    @property
    def lane_change_cooldown(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_change_cooldown

    @lane_change_cooldown.setter
    def lane_change_cooldown(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.lane_change_cooldown.CopyFrom(value.proto)

        self._lane_change_cooldown = value
        self._lane_change_cooldown._update_proto_references(self.proto.lane_change_cooldown)

    @property
    def enable_dynamic_lane_selection(self) -> bool:
        return self.proto.enable_dynamic_lane_selection

    @enable_dynamic_lane_selection.setter
    def enable_dynamic_lane_selection(self, value: bool):
        self.proto.enable_dynamic_lane_selection = value

    @property
    def start_gear(self) -> Gear:
        return self.proto.start_gear

    @start_gear.setter
    def start_gear(self, value: Gear):
        self.proto.start_gear = value

    @property
    def start_separation_time(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._start_separation_time

    @start_separation_time.setter
    def start_separation_time(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.start_separation_time.CopyFrom(value.proto)

        self._start_separation_time = value
        self._start_separation_time._update_proto_references(self.proto.start_separation_time)

    @property
    def target_separation_time(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._target_separation_time

    @target_separation_time.setter
    def target_separation_time(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.target_separation_time.CopyFrom(value.proto)

        self._target_separation_time = value
        self._target_separation_time._update_proto_references(self.proto.target_separation_time)

    @property
    def vehicle_aggression(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._vehicle_aggression

    @vehicle_aggression.setter
    def vehicle_aggression(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.vehicle_aggression.CopyFrom(value.proto)

        self._vehicle_aggression = value
        self._vehicle_aggression._update_proto_references(self.proto.vehicle_aggression)

    @property
    def ignore_obstacle_types(self) -> List[ObstacleType]:
        return self._ignore_obstacle_types

    @ignore_obstacle_types.setter
    def ignore_obstacle_types(self, value: List[ObstacleType]):
        self._ignore_obstacle_types.clear()
        for v in value:
            self._ignore_obstacle_types.append(v)

    @property
    def parking_scenario_goal(self) -> PositionRequest:
        return self._parking_scenario_goal

    @parking_scenario_goal.setter
    def parking_scenario_goal(self, value: PositionRequest):
        self.proto.parking_scenario_goal.CopyFrom(value.proto)

        self._parking_scenario_goal = value
        self._parking_scenario_goal._update_proto_references(self.proto.parking_scenario_goal)

    @property
    def parking_scenario_time(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._parking_scenario_time

    @parking_scenario_time.setter
    def parking_scenario_time(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.parking_scenario_time.CopyFrom(value.proto)

        self._parking_scenario_time = value
        self._parking_scenario_time._update_proto_references(self.proto.parking_scenario_time)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.VehicleBehavior):
        self.proto = proto
        self._start_speed._update_proto_references(proto.start_speed)
        self._target_speed._update_proto_references(proto.target_speed)
        self._lane_offset._update_proto_references(proto.lane_offset)
        self._lane_drift_scale._update_proto_references(proto.lane_drift_scale)
        self._lane_drift_amplitude._update_proto_references(proto.lane_drift_amplitude)
        self._lane_change_probability._update_proto_references(proto.lane_change_probability)
        self._lane_change_cooldown._update_proto_references(proto.lane_change_cooldown)
        self._start_separation_time._update_proto_references(proto.start_separation_time)
        self._target_separation_time._update_proto_references(proto.target_separation_time)
        self._vehicle_aggression._update_proto_references(proto.vehicle_aggression)
        self._parking_scenario_goal._update_proto_references(proto.parking_scenario_goal)
        self._parking_scenario_time._update_proto_references(proto.parking_scenario_time)


@register_wrapper(proto_type=pd_unified_generator_pb2.VehiclePeripheral)
class VehiclePeripheral(ProtoMessageClass):
    """
    Specifies and controls parameters of a vehicle's peripherals (eg. accessory data, color, occupants, etc.).

    Args:
        spawn_trailer_probability: :attr:`spawn_trailer_probability`
        trailer_initial_yaw: :attr:`trailer_initial_yaw`
        disable_occupants: :attr:`disable_occupants`
        disable_accessories: :attr:`disable_accessories`
        randomize_vehicle_parts: :attr:`randomize_vehicle_parts`
        emergency_light_probability: :attr:`emergency_light_probability`
        set_headlight_based_on_time_of_day: :attr:`set_headlight_based_on_time_of_day`
        headlight_probability: :attr:`headlight_probability`
    Attributes:
        spawn_trailer_probability: The probability that the vehicle will be spawned with an attached articulated trailer. Must be a float in the range
            of 0.0 to 1.0.
            Default: 0.0
        trailer_initial_yaw: The angle, in radians, that an articulated trailer will be spawned at relative to the ego vehicle. Specified as a
            :obj:`ContinousUniformDistribution` which is randomly sampled from at scenario generation.
        disable_occupants: Boolean flag to control whether vehicle occupants are disabled.
            Default: False
        disable_accessories: Boolean flag to control whether vehicles are spawned with accessories.
            Default: False
        randomize_vehicle_parts: Boolean flag to control whether vehicle accessories have randomized colors.
            Default: True
        emergency_light_probability: Probability that emergency lights are on for vehicles that are equipped with emergency lights.
            Default: 0.5
        set_headlight_based_on_time_of_day: Boolean flag to control whether headlight on/off states are controlled by the time of day of the scenario. If
            `True`, headlights will turn on in dark time of day scenarios. If `False`, :attr:`headlight_probability` is used to
            determine headlight on/off state.
            Default: True
        headlight_probability: Controls the probability that headlights are turned on if :attr:`set_headlight_based_on_time_of_day` is `False`.
            Ignored if :attr:`set_headlight_based_on_time_of_day` is `True`.
            Default: 0.0"""

    _proto_message = pd_unified_generator_pb2.VehiclePeripheral

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.VehiclePeripheral] = None,
        spawn_trailer_probability: float = None,
        trailer_initial_yaw: _pd_distributions_pb2.ContinousUniformDistribution = None,
        disable_occupants: bool = None,
        disable_accessories: bool = None,
        randomize_vehicle_parts: bool = None,
        emergency_light_probability: float = None,
        set_headlight_based_on_time_of_day: bool = None,
        headlight_probability: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.VehiclePeripheral()
        self.proto = proto
        self._trailer_initial_yaw = get_wrapper(proto_type=proto.trailer_initial_yaw.__class__)(
            proto=proto.trailer_initial_yaw
        )
        if spawn_trailer_probability is not None:
            self.spawn_trailer_probability = spawn_trailer_probability
        if trailer_initial_yaw is not None:
            self.trailer_initial_yaw = trailer_initial_yaw
        if disable_occupants is not None:
            self.disable_occupants = disable_occupants
        if disable_accessories is not None:
            self.disable_accessories = disable_accessories
        if randomize_vehicle_parts is not None:
            self.randomize_vehicle_parts = randomize_vehicle_parts
        if emergency_light_probability is not None:
            self.emergency_light_probability = emergency_light_probability
        if set_headlight_based_on_time_of_day is not None:
            self.set_headlight_based_on_time_of_day = set_headlight_based_on_time_of_day
        if headlight_probability is not None:
            self.headlight_probability = headlight_probability

    @property
    def spawn_trailer_probability(self) -> float:
        return self.proto.spawn_trailer_probability

    @spawn_trailer_probability.setter
    def spawn_trailer_probability(self, value: float):
        self.proto.spawn_trailer_probability = value

    @property
    def trailer_initial_yaw(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._trailer_initial_yaw

    @trailer_initial_yaw.setter
    def trailer_initial_yaw(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.trailer_initial_yaw.CopyFrom(value.proto)

        self._trailer_initial_yaw = value
        self._trailer_initial_yaw._update_proto_references(self.proto.trailer_initial_yaw)

    @property
    def disable_occupants(self) -> bool:
        return self.proto.disable_occupants

    @disable_occupants.setter
    def disable_occupants(self, value: bool):
        self.proto.disable_occupants = value

    @property
    def disable_accessories(self) -> bool:
        return self.proto.disable_accessories

    @disable_accessories.setter
    def disable_accessories(self, value: bool):
        self.proto.disable_accessories = value

    @property
    def randomize_vehicle_parts(self) -> bool:
        return self.proto.randomize_vehicle_parts

    @randomize_vehicle_parts.setter
    def randomize_vehicle_parts(self, value: bool):
        self.proto.randomize_vehicle_parts = value

    @property
    def emergency_light_probability(self) -> float:
        return self.proto.emergency_light_probability

    @emergency_light_probability.setter
    def emergency_light_probability(self, value: float):
        self.proto.emergency_light_probability = value

    @property
    def set_headlight_based_on_time_of_day(self) -> bool:
        return self.proto.set_headlight_based_on_time_of_day

    @set_headlight_based_on_time_of_day.setter
    def set_headlight_based_on_time_of_day(self, value: bool):
        self.proto.set_headlight_based_on_time_of_day = value

    @property
    def headlight_probability(self) -> float:
        return self.proto.headlight_probability

    @headlight_probability.setter
    def headlight_probability(self, value: float):
        self.proto.headlight_probability = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.VehiclePeripheral):
        self.proto = proto
        self._trailer_initial_yaw._update_proto_references(proto.trailer_initial_yaw)


@register_wrapper(proto_type=pd_unified_generator_pb2.PedestrianSpawnData)
class PedestrianSpawnData(ProtoMessageClass):
    """
    Parameters to control a pedestrian's spawn characteristics and movement behavior.

    Args:
        pedestrian_color_override_probability: :attr:`pedestrian_color_override_probability`
        pedestrian_color_override_rgb: :attr:`pedestrian_color_override_rgb`
        orient_to_velocity: :attr:`orient_to_velocity`
        check_occupancy: :attr:`check_occupancy`
        jaywalker_ego_fwd_offset: :attr:`jaywalker_ego_fwd_offset`
        agent_spawn_data: :attr:`agent_spawn_data`
        ped_behavior: :attr:`ped_behavior`
        asset_name: :attr:`asset_name`
        speed: :attr:`speed`
    Attributes:
        pedestrian_color_override_probability: Specifies probability of overriding color of pedestrian's clothes to RGB color specified by
            :attr:`pedestrian_color_override_rgb`. Probability is specified as a `CenterSpreadConfig` with values in the range
            0.0 to 1.0, and is randomly sampled from during scenario generation. If not provided, will default to 0.0.
        pedestrian_color_override_rgb: Specifies color to override pedestrian's clothes with if a pedestrian will have its clothing color overridden
            based on :attr:`pedestrian_color_override_probability`. Specified as `RGB` values in the range 0.0 to 1.0.
        orient_to_velocity: Boolean flag to specify whether pedestrians always face the direction of travel.
            Default: True
        check_occupancy: Boolean flag to specify whether spawn locations are checked for occupancy by other agents prior to spawning.
            Default: True
        jaywalker_ego_fwd_offset: Specifies how far ahead, in meters, a jaywalking pedestrian should be from the tagged vehicle. If
            :attr:`ped_behavior` does not specify that the pedestrian is a `JAYWALKER`, this field is ignored.
            Default: 20.0
        agent_spawn_data: Specifies spawn data which applies to the agents. If not provided, will default to default
            values in :obj:`AgentSpawnData`.
        ped_behavior: Specifies desired behavior of pedestrian being spawned. If not provided, will default to `NORMAL` behavior.
        asset_name: Asset name of the pedestrian being spawned.
            Default: char_hannah_001
        speed: Specifies the speed in meters per second of the pedestrian being spawned.
            Default: 1.0"""

    _proto_message = pd_unified_generator_pb2.PedestrianSpawnData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.PedestrianSpawnData] = None,
        pedestrian_color_override_probability: CenterSpreadConfig = None,
        pedestrian_color_override_rgb: _pd_types_pb2.Float3 = None,
        orient_to_velocity: bool = None,
        check_occupancy: bool = None,
        jaywalker_ego_fwd_offset: float = None,
        agent_spawn_data: AgentSpawnData = None,
        ped_behavior: PedestrianBehavior = None,
        asset_name: str = None,
        speed: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.PedestrianSpawnData()
        self.proto = proto
        self._pedestrian_color_override_probability = get_wrapper(
            proto_type=proto.pedestrian_color_override_probability.__class__
        )(proto=proto.pedestrian_color_override_probability)
        self._pedestrian_color_override_rgb = get_wrapper(proto_type=proto.pedestrian_color_override_rgb.__class__)(
            proto=proto.pedestrian_color_override_rgb
        )
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        if pedestrian_color_override_probability is not None:
            self.pedestrian_color_override_probability = pedestrian_color_override_probability
        if pedestrian_color_override_rgb is not None:
            self.pedestrian_color_override_rgb = pedestrian_color_override_rgb
        if orient_to_velocity is not None:
            self.orient_to_velocity = orient_to_velocity
        if check_occupancy is not None:
            self.check_occupancy = check_occupancy
        if jaywalker_ego_fwd_offset is not None:
            self.jaywalker_ego_fwd_offset = jaywalker_ego_fwd_offset
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data
        if ped_behavior is not None:
            self.ped_behavior = ped_behavior
        if asset_name is not None:
            self.asset_name = asset_name
        if speed is not None:
            self.speed = speed

    @property
    def pedestrian_color_override_probability(self) -> CenterSpreadConfig:
        return self._pedestrian_color_override_probability

    @pedestrian_color_override_probability.setter
    def pedestrian_color_override_probability(self, value: CenterSpreadConfig):
        self.proto.pedestrian_color_override_probability.CopyFrom(value.proto)

        self._pedestrian_color_override_probability = value
        self._pedestrian_color_override_probability._update_proto_references(
            self.proto.pedestrian_color_override_probability
        )

    @property
    def pedestrian_color_override_rgb(self) -> _pd_types_pb2.Float3:
        return self._pedestrian_color_override_rgb

    @pedestrian_color_override_rgb.setter
    def pedestrian_color_override_rgb(self, value: _pd_types_pb2.Float3):
        self.proto.pedestrian_color_override_rgb.CopyFrom(value.proto)

        self._pedestrian_color_override_rgb = value
        self._pedestrian_color_override_rgb._update_proto_references(self.proto.pedestrian_color_override_rgb)

    @property
    def orient_to_velocity(self) -> bool:
        return self.proto.orient_to_velocity

    @orient_to_velocity.setter
    def orient_to_velocity(self, value: bool):
        self.proto.orient_to_velocity = value

    @property
    def check_occupancy(self) -> bool:
        return self.proto.check_occupancy

    @check_occupancy.setter
    def check_occupancy(self, value: bool):
        self.proto.check_occupancy = value

    @property
    def jaywalker_ego_fwd_offset(self) -> float:
        return self.proto.jaywalker_ego_fwd_offset

    @jaywalker_ego_fwd_offset.setter
    def jaywalker_ego_fwd_offset(self, value: float):
        self.proto.jaywalker_ego_fwd_offset = value

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    @property
    def ped_behavior(self) -> PedestrianBehavior:
        return self.proto.ped_behavior

    @ped_behavior.setter
    def ped_behavior(self, value: PedestrianBehavior):
        self.proto.ped_behavior = value

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

    @property
    def speed(self) -> float:
        return self.proto.speed

    @speed.setter
    def speed(self, value: float):
        self.proto.speed = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.PedestrianSpawnData):
        self.proto = proto
        self._pedestrian_color_override_probability._update_proto_references(
            proto.pedestrian_color_override_probability
        )
        self._pedestrian_color_override_rgb._update_proto_references(proto.pedestrian_color_override_rgb)
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)


@register_wrapper(proto_type=pd_unified_generator_pb2.DroneSpawnData)
class DroneSpawnData(ProtoMessageClass):
    """
    Parameters to control a drone's spawn characteristics and movement behavior.

    Args:
        ascend_probability: :attr:`ascend_probability`
        ground_asset_probability: :attr:`ground_asset_probability`
        ground_assets: :attr:`ground_assets`
        flight_path_dir: :attr:`flight_path_dir`
        agent_spawn_data: :attr:`agent_spawn_data`
        height_offset: :attr:`height_offset`
        ground_asset_height_offset: :attr:`ground_asset_height_offset`
    Attributes:
        ascend_probability: Specify the probability that the drone will ascend (as opposed to descend). Specified as a float in the range 0.0
            to 1.0.
            Default: 0.5
        ground_asset_probability: Probability of having a ground asset directly below the lowest point of the drone's flight path.
            Default: 0.5
        ground_assets: List of ground assets to choose from if a ground asset should be spawned based on the parameter
            :attr:`ground_asset_probability`.
        flight_path_dir: Directory where flight path csv files are stored within the instance. If not provided, default flight path shape
            is used.
        agent_spawn_data: Specifies spawn data which applies to the agents. If not provided, will default to default
            values in :obj:`AgentSpawnData`.
        height_offset: Specifies the vertical distance, in meters, between the lowest point of the drone flight path and the ground.
            Specified as a :obj:`ContinousUniformDistribution` which is randomly sampled from at scenario generation.
        ground_asset_height_offset: Specifies the vertical distance above the ground which the ground asset should be spawned at if a ground asset
            should be spawned according to parameters in :attr:`ground_asset_probability`.

            Specified as a :obj:`ContinousUniformDistribution` which is randomly sampled from at scenario generation."""

    _proto_message = pd_unified_generator_pb2.DroneSpawnData

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.DroneSpawnData] = None,
        ascend_probability: float = None,
        ground_asset_probability: float = None,
        ground_assets: List[str] = None,
        flight_path_dir: str = None,
        agent_spawn_data: AgentSpawnData = None,
        height_offset: _pd_distributions_pb2.ContinousUniformDistribution = None,
        ground_asset_height_offset: _pd_distributions_pb2.ContinousUniformDistribution = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.DroneSpawnData()
        self.proto = proto
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        self._height_offset = get_wrapper(proto_type=proto.height_offset.__class__)(proto=proto.height_offset)
        self._ground_asset_height_offset = get_wrapper(proto_type=proto.ground_asset_height_offset.__class__)(
            proto=proto.ground_asset_height_offset
        )
        if ascend_probability is not None:
            self.ascend_probability = ascend_probability
        if ground_asset_probability is not None:
            self.ground_asset_probability = ground_asset_probability
        self._ground_assets = ProtoListWrapper(
            container=[str(v) for v in proto.ground_assets], attr_name="ground_assets", list_owner=self
        )
        if ground_assets is not None:
            self.ground_assets = ground_assets
        if flight_path_dir is not None:
            self.flight_path_dir = flight_path_dir
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data
        if height_offset is not None:
            self.height_offset = height_offset
        if ground_asset_height_offset is not None:
            self.ground_asset_height_offset = ground_asset_height_offset

    @property
    def ascend_probability(self) -> float:
        return self.proto.ascend_probability

    @ascend_probability.setter
    def ascend_probability(self, value: float):
        self.proto.ascend_probability = value

    @property
    def ground_asset_probability(self) -> float:
        return self.proto.ground_asset_probability

    @ground_asset_probability.setter
    def ground_asset_probability(self, value: float):
        self.proto.ground_asset_probability = value

    @property
    def ground_assets(self) -> List[str]:
        return self._ground_assets

    @ground_assets.setter
    def ground_assets(self, value: List[str]):
        self._ground_assets.clear()
        for v in value:
            self._ground_assets.append(v)

    @property
    def flight_path_dir(self) -> str:
        return self.proto.flight_path_dir

    @flight_path_dir.setter
    def flight_path_dir(self, value: str):
        self.proto.flight_path_dir = value

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self.proto.agent_spawn_data.CopyFrom(value.proto)

        self._agent_spawn_data = value
        self._agent_spawn_data._update_proto_references(self.proto.agent_spawn_data)

    @property
    def height_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._height_offset

    @height_offset.setter
    def height_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.height_offset.CopyFrom(value.proto)

        self._height_offset = value
        self._height_offset._update_proto_references(self.proto.height_offset)

    @property
    def ground_asset_height_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._ground_asset_height_offset

    @ground_asset_height_offset.setter
    def ground_asset_height_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self.proto.ground_asset_height_offset.CopyFrom(value.proto)

        self._ground_asset_height_offset = value
        self._ground_asset_height_offset._update_proto_references(self.proto.ground_asset_height_offset)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.DroneSpawnData):
        self.proto = proto
        self._agent_spawn_data._update_proto_references(proto.agent_spawn_data)
        self._height_offset._update_proto_references(proto.height_offset)
        self._ground_asset_height_offset._update_proto_references(proto.ground_asset_height_offset)


@register_wrapper(proto_type=pd_unified_generator_pb2.AgentSpawnData)
class AgentSpawnData(ProtoMessageClass):
    """
    Contains spawn metadata that applies across agent types.

    Args:
        tags: :attr:`tags`
    Attributes:
        tags: Tags to be applied to the agent. Tags are case sensitive."""

    _proto_message = pd_unified_generator_pb2.AgentSpawnData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.AgentSpawnData] = None, tags: List[str] = None):
        if proto is None:
            proto = pd_unified_generator_pb2.AgentSpawnData()
        self.proto = proto
        self._tags = ProtoListWrapper(container=[str(v) for v in proto.tags], attr_name="tags", list_owner=self)
        if tags is not None:
            self.tags = tags

    @property
    def tags(self) -> List[str]:
        return self._tags

    @tags.setter
    def tags(self, value: List[str]):
        self._tags.clear()
        for v in value:
            self._tags.append(v)

    def _update_proto_references(self, proto: pd_unified_generator_pb2.AgentSpawnData):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.SignalLightDistribution)
class SignalLightDistribution(ProtoMessageClass):
    """
    Specifies distribution of bulb colors in the traffic signal lights.

    Args:
        green: :attr:`green`
        red: :attr:`red`
        yellow: :attr:`yellow`
    Attributes:
        green: Default: 0.3333
        red: Default: 0.3333
        yellow: Default: 0.3333"""

    _proto_message = pd_unified_generator_pb2.SignalLightDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.SignalLightDistribution] = None,
        green: float = None,
        red: float = None,
        yellow: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.SignalLightDistribution()
        self.proto = proto
        if green is not None:
            self.green = green
        if red is not None:
            self.red = red
        if yellow is not None:
            self.yellow = yellow

    @property
    def green(self) -> float:
        return self.proto.green

    @green.setter
    def green(self, value: float):
        self.proto.green = value

    @property
    def red(self) -> float:
        return self.proto.red

    @red.setter
    def red(self, value: float):
        self.proto.red = value

    @property
    def yellow(self) -> float:
        return self.proto.yellow

    @yellow.setter
    def yellow(self, value: float):
        self.proto.yellow = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.SignalLightDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.TurnTypeDistribution)
class TurnTypeDistribution(ProtoMessageClass):
    """
    Specifies distribution of turns types of incoming lanes in a junction.

    Args:
        straight: :attr:`straight`
        left: :attr:`left`
        right: :attr:`right`
    Attributes:
        straight: Default: 0.3333
        left: Default: 0.3333
        right: Default: 0.3333"""

    _proto_message = pd_unified_generator_pb2.TurnTypeDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.TurnTypeDistribution] = None,
        straight: float = None,
        left: float = None,
        right: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.TurnTypeDistribution()
        self.proto = proto
        if straight is not None:
            self.straight = straight
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right

    @property
    def straight(self) -> float:
        return self.proto.straight

    @straight.setter
    def straight(self, value: float):
        self.proto.straight = value

    @property
    def left(self) -> float:
        return self.proto.left

    @left.setter
    def left(self, value: float):
        self.proto.left = value

    @property
    def right(self) -> float:
        return self.proto.right

    @right.setter
    def right(self, value: float):
        self.proto.right = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.TurnTypeDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.ParkingTypeDistribution)
class ParkingTypeDistribution(ProtoMessageClass):
    """
    Specifies distribution of parking types present in the map.

    Args:
        forward: :attr:`forward`
        reverse: :attr:`reverse`
        parallel: :attr:`parallel`
    Attributes:
        forward: Default: 0.5
        reverse: Default: 0.5
        parallel: Default: 0.0"""

    _proto_message = pd_unified_generator_pb2.ParkingTypeDistribution

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.ParkingTypeDistribution] = None,
        forward: float = None,
        reverse: float = None,
        parallel: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.ParkingTypeDistribution()
        self.proto = proto
        if forward is not None:
            self.forward = forward
        if reverse is not None:
            self.reverse = reverse
        if parallel is not None:
            self.parallel = parallel

    @property
    def forward(self) -> float:
        return self.proto.forward

    @forward.setter
    def forward(self, value: float):
        self.proto.forward = value

    @property
    def reverse(self) -> float:
        return self.proto.reverse

    @reverse.setter
    def reverse(self, value: float):
        self.proto.reverse = value

    @property
    def parallel(self) -> float:
        return self.proto.parallel

    @parallel.setter
    def parallel(self, value: float):
        self.proto.parallel = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.ParkingTypeDistribution):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadProbabilityConfig)
class CenterSpreadProbabilityConfig(ProtoMessageClass):
    """
    Specifies probability distribution defined by center and spread.

    Args:
        probability: :attr:`probability`
        center: :attr:`center`
        spread: :attr:`spread`
    Attributes:
        probability: Default: 0.0
        center: Default: 0.0
        spread: Default: 0.0"""

    _proto_message = pd_unified_generator_pb2.CenterSpreadProbabilityConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.CenterSpreadProbabilityConfig] = None,
        probability: float = None,
        center: float = None,
        spread: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.CenterSpreadProbabilityConfig()
        self.proto = proto
        if probability is not None:
            self.probability = probability
        if center is not None:
            self.center = center
        if spread is not None:
            self.spread = spread

    @property
    def probability(self) -> float:
        return self.proto.probability

    @probability.setter
    def probability(self, value: float):
        self.proto.probability = value

    @property
    def center(self) -> float:
        return self.proto.center

    @center.setter
    def center(self, value: float):
        self.proto.center = value

    @property
    def spread(self) -> float:
        return self.proto.spread

    @spread.setter
    def spread(self, value: float):
        self.proto.spread = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.CenterSpreadProbabilityConfig):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadConfig)
class CenterSpreadConfig(ProtoMessageClass):
    """
    Specifies center and spread of distribution defined with float values.

    Args:
        center: :attr:`center`
        spread: :attr:`spread`
    Attributes:
        center: Default: 0.0
        spread: Default: 0.0"""

    _proto_message = pd_unified_generator_pb2.CenterSpreadConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.CenterSpreadConfig] = None,
        center: float = None,
        spread: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.CenterSpreadConfig()
        self.proto = proto
        if center is not None:
            self.center = center
        if spread is not None:
            self.spread = spread

    @property
    def center(self) -> float:
        return self.proto.center

    @center.setter
    def center(self, value: float):
        self.proto.center = value

    @property
    def spread(self) -> float:
        return self.proto.spread

    @spread.setter
    def spread(self, value: float):
        self.proto.spread = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadConfigInt)
class CenterSpreadConfigInt(ProtoMessageClass):
    """
    Specifies center and spread of distribution defined with integer values.

    Args:
        center: :attr:`center`
        spread: :attr:`spread`
    Attributes:
        center: Default: 0
        spread: Default: 0"""

    _proto_message = pd_unified_generator_pb2.CenterSpreadConfigInt

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.CenterSpreadConfigInt] = None,
        center: int = None,
        spread: int = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.CenterSpreadConfigInt()
        self.proto = proto
        if center is not None:
            self.center = center
        if spread is not None:
            self.spread = spread

    @property
    def center(self) -> int:
        return self.proto.center

    @center.setter
    def center(self, value: int):
        self.proto.center = value

    @property
    def spread(self) -> int:
        return self.proto.spread

    @spread.setter
    def spread(self, value: int):
        self.proto.spread = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.CenterSpreadConfigInt):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.MinMaxConfigFloat)
class MinMaxConfigFloat(ProtoMessageClass):
    """
    Specifies lower and upper bounds of distributions defined with float values.

    Args:
        min: :attr:`min`
        max: :attr:`max`
    Attributes:
        min: Default: 0.0
        max: Default: 0.0"""

    _proto_message = pd_unified_generator_pb2.MinMaxConfigFloat

    def __init__(
        self,
        *,
        proto: Optional[pd_unified_generator_pb2.MinMaxConfigFloat] = None,
        min: float = None,
        max: float = None,
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.MinMaxConfigFloat()
        self.proto = proto
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.MinMaxConfigFloat):
        self.proto = proto


@register_wrapper(proto_type=pd_unified_generator_pb2.MinMaxConfigInt)
class MinMaxConfigInt(ProtoMessageClass):
    """
    Specifies lower and upper bounds of distributions defined with integer values.

    Args:
        min: :attr:`min`
        max: :attr:`max`
    Attributes:
        min: Default: 0
        max: Default: 0"""

    _proto_message = pd_unified_generator_pb2.MinMaxConfigInt

    def __init__(
        self, *, proto: Optional[pd_unified_generator_pb2.MinMaxConfigInt] = None, min: int = None, max: int = None
    ):
        if proto is None:
            proto = pd_unified_generator_pb2.MinMaxConfigInt()
        self.proto = proto
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

    @property
    def min(self) -> int:
        return self.proto.min

    @min.setter
    def min(self, value: int):
        self.proto.min = value

    @property
    def max(self) -> int:
        return self.proto.max

    @max.setter
    def max(self, value: int):
        self.proto.max = value

    def _update_proto_references(self, proto: pd_unified_generator_pb2.MinMaxConfigInt):
        self.proto = proto
