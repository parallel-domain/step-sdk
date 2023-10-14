from __future__ import annotations
from typing import List, Dict, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoEnumClass,
    ProtoListWrapper,
    ProtoDictWrapper
)
from ..python import (
    pd_spawn_pb2
)
from . import (
    pd_distributions_pb2 as _pd_distributions_pb2,
    pd_unified_generator_pb2 as _pd_unified_generator_pb2
)


class VehicleType(ProtoEnumClass):
    UNDEFINED = 0
    MIDSIZE = 1
    COMPACT = 2
    BUS = 3
    TRUCK = 4
    SUV = 5
    VAN = 6
    BICYCLE = 7
    MOTORCYCLE = 8
    CARAVAN = 9
    FULLSIZE = 10
    TRAILER = 11
    TRAIN = 12


@register_wrapper(proto_type=pd_spawn_pb2.RandomScenarioGenerator)
class RandomScenarioGenerator(ProtoMessageClass):
    """Default scenario generator
    Spawn the ego vehicle on a random lane on the map
    Spawn all other agents around the ego vehicle

    Args:
    Attributes:"""

    _proto_message = pd_spawn_pb2.RandomScenarioGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.RandomScenarioGenerator] = None):
        if proto is None:
            proto = pd_spawn_pb2.RandomScenarioGenerator()
        self.proto = proto

    def _update_proto_references(self, proto: pd_spawn_pb2.RandomScenarioGenerator):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.JunctionScenarioGenerator)
class JunctionScenarioGenerator(ProtoMessageClass):
    """Generate scenarios that around junctions

    Args:
        min_distance_to_junction: :attr:`min_distance_to_junction`
        max_distance_to_junction: :attr:`max_distance_to_junction`
        crowd_density: :attr:`crowd_density`
        signal_light_distribution: :attr:`signal_light_distribution`
        turn_type_distribution: :attr:`turn_type_distribution`
        junction_id: :attr:`junction_id`
        junction_ids: :attr:`junction_ids`
    Attributes:
        min_distance_to_junction:
        max_distance_to_junction:
        crowd_density:
        signal_light_distribution:
        turn_type_distribution:
        junction_id: use a list of junction ids instead of just 1
            leaving the junction_id field in for compatibility with old spawn configs
        junction_ids:"""

    _proto_message = pd_spawn_pb2.JunctionScenarioGenerator

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.JunctionScenarioGenerator] = None,
        min_distance_to_junction: float = None,
        max_distance_to_junction: float = None,
        crowd_density: float = None,
        signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution = None,
        turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution = None,
        junction_id: int = None,
        junction_ids: List[int] = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.JunctionScenarioGenerator()
        self.proto = proto
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(
            proto=proto.signal_light_distribution
        )
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(
            proto=proto.turn_type_distribution
        )
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if crowd_density is not None:
            self.crowd_density = crowd_density
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution
        if junction_id is not None:
            self.junction_id = junction_id
        self._junction_ids = ProtoListWrapper(
            container=[int(v) for v in proto.junction_ids], attr_name="junction_ids", list_owner=self
        )
        if junction_ids is not None:
            self.junction_ids = junction_ids

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def crowd_density(self) -> float:
        return self.proto.crowd_density

    @crowd_density.setter
    def crowd_density(self, value: float):
        self.proto.crowd_density = value

    @property
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self.proto.signal_light_distribution.CopyFrom(value.proto)

        self._signal_light_distribution = value
        self._signal_light_distribution._update_proto_references(self.proto.signal_light_distribution)

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self.proto.turn_type_distribution.CopyFrom(value.proto)

        self._turn_type_distribution = value
        self._turn_type_distribution._update_proto_references(self.proto.turn_type_distribution)

    @property
    def junction_id(self) -> int:
        return self.proto.junction_id

    @junction_id.setter
    def junction_id(self, value: int):
        self.proto.junction_id = value

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

    def _update_proto_references(self, proto: pd_spawn_pb2.JunctionScenarioGenerator):
        self.proto = proto
        self._signal_light_distribution._update_proto_references(proto.signal_light_distribution)
        self._turn_type_distribution._update_proto_references(proto.turn_type_distribution)


@register_wrapper(proto_type=pd_spawn_pb2.VehicleOfInterestGenerator)
class VehicleOfInterestGenerator(ProtoMessageClass):
    """Generate scenarios in which

    Args:
        vehicle_list: :attr:`vehicle_list`
        max_distance_front: :attr:`max_distance_front`
        max_distance_back: :attr:`max_distance_back`
        min_number_of_vehicles: :attr:`min_number_of_vehicles`
        max_number_of_vehicles: :attr:`max_number_of_vehicles`
        include_opposite_lanes: :attr:`include_opposite_lanes`
    Attributes:
        vehicle_list: A list of vehicle model names which are samples and spawned around the ego vehicle
        max_distance_front: Maximum distance of a special vehicle in front of the ego vehicle
        max_distance_back: Maximum distance of a special vehicle behind the ego vehicle
        min_number_of_vehicles: Minimum number of vehicles that are placed per scenario
        max_number_of_vehicles: Maximum number of vehicles that are placed per scenario
        include_opposite_lanes: Spawn vehicles on opposite lanes if available"""

    _proto_message = pd_spawn_pb2.VehicleOfInterestGenerator

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.VehicleOfInterestGenerator] = None,
        vehicle_list: List[str] = None,
        max_distance_front: float = None,
        max_distance_back: float = None,
        min_number_of_vehicles: int = None,
        max_number_of_vehicles: int = None,
        include_opposite_lanes: bool = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.VehicleOfInterestGenerator()
        self.proto = proto
        self._vehicle_list = ProtoListWrapper(
            container=[str(v) for v in proto.vehicle_list], attr_name="vehicle_list", list_owner=self
        )
        if vehicle_list is not None:
            self.vehicle_list = vehicle_list
        if max_distance_front is not None:
            self.max_distance_front = max_distance_front
        if max_distance_back is not None:
            self.max_distance_back = max_distance_back
        if min_number_of_vehicles is not None:
            self.min_number_of_vehicles = min_number_of_vehicles
        if max_number_of_vehicles is not None:
            self.max_number_of_vehicles = max_number_of_vehicles
        if include_opposite_lanes is not None:
            self.include_opposite_lanes = include_opposite_lanes

    @property
    def vehicle_list(self) -> List[str]:
        return self._vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, value: List[str]):
        self._vehicle_list.clear()
        for v in value:
            self._vehicle_list.append(v)

    @property
    def max_distance_front(self) -> float:
        return self.proto.max_distance_front

    @max_distance_front.setter
    def max_distance_front(self, value: float):
        self.proto.max_distance_front = value

    @property
    def max_distance_back(self) -> float:
        return self.proto.max_distance_back

    @max_distance_back.setter
    def max_distance_back(self, value: float):
        self.proto.max_distance_back = value

    @property
    def min_number_of_vehicles(self) -> int:
        return self.proto.min_number_of_vehicles

    @min_number_of_vehicles.setter
    def min_number_of_vehicles(self, value: int):
        self.proto.min_number_of_vehicles = value

    @property
    def max_number_of_vehicles(self) -> int:
        return self.proto.max_number_of_vehicles

    @max_number_of_vehicles.setter
    def max_number_of_vehicles(self, value: int):
        self.proto.max_number_of_vehicles = value

    @property
    def include_opposite_lanes(self) -> bool:
        return self.proto.include_opposite_lanes

    @include_opposite_lanes.setter
    def include_opposite_lanes(self, value: bool):
        self.proto.include_opposite_lanes = value

    def _update_proto_references(self, proto: pd_spawn_pb2.VehicleOfInterestGenerator):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.KittiScenarioGenerator)
class KittiScenarioGenerator(ProtoMessageClass):
    """Generate kitti-like scenarios

    Args:
        min_distance_to_junction: :attr:`min_distance_to_junction`
        max_distance_to_junction: :attr:`max_distance_to_junction`
        turn_type_distribution: :attr:`turn_type_distribution`
    Attributes:
        min_distance_to_junction:
        max_distance_to_junction:
        turn_type_distribution:"""

    _proto_message = pd_spawn_pb2.KittiScenarioGenerator

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.KittiScenarioGenerator] = None,
        min_distance_to_junction: float = None,
        max_distance_to_junction: float = None,
        turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.KittiScenarioGenerator()
        self.proto = proto
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(
            proto=proto.turn_type_distribution
        )
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self.proto.turn_type_distribution.CopyFrom(value.proto)

        self._turn_type_distribution = value
        self._turn_type_distribution._update_proto_references(self.proto.turn_type_distribution)

    def _update_proto_references(self, proto: pd_spawn_pb2.KittiScenarioGenerator):
        self.proto = proto
        self._turn_type_distribution._update_proto_references(proto.turn_type_distribution)


@register_wrapper(proto_type=pd_spawn_pb2.PositionGenerator)
class PositionGenerator(ProtoMessageClass):
    """
    Args:
        radius_to_star_min: :attr:`radius_to_star_min`
        radius_to_star_max: :attr:`radius_to_star_max`
        star_vehicles: :attr:`star_vehicles`
        junction_ids: :attr:`junction_ids`
        face_same_direction: :attr:`face_same_direction`
        ego_behind_star: :attr:`ego_behind_star`
    Attributes:
        radius_to_star_min:
        radius_to_star_max:
        star_vehicles:
        junction_ids:
        face_same_direction:
        ego_behind_star:"""

    _proto_message = pd_spawn_pb2.PositionGenerator

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.PositionGenerator] = None,
        radius_to_star_min: float = None,
        radius_to_star_max: float = None,
        star_vehicles: List[str] = None,
        junction_ids: List[int] = None,
        face_same_direction: bool = None,
        ego_behind_star: bool = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.PositionGenerator()
        self.proto = proto
        if radius_to_star_min is not None:
            self.radius_to_star_min = radius_to_star_min
        if radius_to_star_max is not None:
            self.radius_to_star_max = radius_to_star_max
        self._star_vehicles = ProtoListWrapper(
            container=[str(v) for v in proto.star_vehicles], attr_name="star_vehicles", list_owner=self
        )
        if star_vehicles is not None:
            self.star_vehicles = star_vehicles
        self._junction_ids = ProtoListWrapper(
            container=[int(v) for v in proto.junction_ids], attr_name="junction_ids", list_owner=self
        )
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if face_same_direction is not None:
            self.face_same_direction = face_same_direction
        if ego_behind_star is not None:
            self.ego_behind_star = ego_behind_star

    @property
    def radius_to_star_min(self) -> float:
        return self.proto.radius_to_star_min

    @radius_to_star_min.setter
    def radius_to_star_min(self, value: float):
        self.proto.radius_to_star_min = value

    @property
    def radius_to_star_max(self) -> float:
        return self.proto.radius_to_star_max

    @radius_to_star_max.setter
    def radius_to_star_max(self, value: float):
        self.proto.radius_to_star_max = value

    @property
    def star_vehicles(self) -> List[str]:
        return self._star_vehicles

    @star_vehicles.setter
    def star_vehicles(self, value: List[str]):
        self._star_vehicles.clear()
        for v in value:
            self._star_vehicles.append(v)

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

    @property
    def face_same_direction(self) -> bool:
        return self.proto.face_same_direction

    @face_same_direction.setter
    def face_same_direction(self, value: bool):
        self.proto.face_same_direction = value

    @property
    def ego_behind_star(self) -> bool:
        return self.proto.ego_behind_star

    @ego_behind_star.setter
    def ego_behind_star(self, value: bool):
        self.proto.ego_behind_star = value

    def _update_proto_references(self, proto: pd_spawn_pb2.PositionGenerator):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.AgentStateProbabilityConfig)
class AgentStateProbabilityConfig(ProtoMessageClass):
    """
    Args:
        stateName: :attr:`stateName`
        probability: :attr:`probability`
        probabilitySpread: :attr:`probabilitySpread`
        time: :attr:`time`
        timeSpread: :attr:`timeSpread`
        maxPerScene: :attr:`maxPerScene`
        allowedAfter: :attr:`allowedAfter`
    Attributes:
        stateName:
        probability: Default: 0.0
        probabilitySpread: Default: 0.0
        time: Default: 0.0
        timeSpread: Default: 0.0
        maxPerScene: Default value of max int32 for max per scene so it has no effect by default.
            Default: 2147483647
        allowedAfter: Default: 0.0"""

    _proto_message = pd_spawn_pb2.AgentStateProbabilityConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.AgentStateProbabilityConfig] = None,
        stateName: str = None,
        probability: float = None,
        probabilitySpread: float = None,
        time: float = None,
        timeSpread: float = None,
        maxPerScene: int = None,
        allowedAfter: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.AgentStateProbabilityConfig()
        self.proto = proto
        if stateName is not None:
            self.stateName = stateName
        if probability is not None:
            self.probability = probability
        if probabilitySpread is not None:
            self.probabilitySpread = probabilitySpread
        if time is not None:
            self.time = time
        if timeSpread is not None:
            self.timeSpread = timeSpread
        if maxPerScene is not None:
            self.maxPerScene = maxPerScene
        if allowedAfter is not None:
            self.allowedAfter = allowedAfter

    @property
    def stateName(self) -> str:
        return self.proto.stateName

    @stateName.setter
    def stateName(self, value: str):
        self.proto.stateName = value

    @property
    def probability(self) -> float:
        return self.proto.probability

    @probability.setter
    def probability(self, value: float):
        self.proto.probability = value

    @property
    def probabilitySpread(self) -> float:
        return self.proto.probabilitySpread

    @probabilitySpread.setter
    def probabilitySpread(self, value: float):
        self.proto.probabilitySpread = value

    @property
    def time(self) -> float:
        return self.proto.time

    @time.setter
    def time(self, value: float):
        self.proto.time = value

    @property
    def timeSpread(self) -> float:
        return self.proto.timeSpread

    @timeSpread.setter
    def timeSpread(self, value: float):
        self.proto.timeSpread = value

    @property
    def maxPerScene(self) -> int:
        return self.proto.maxPerScene

    @maxPerScene.setter
    def maxPerScene(self, value: int):
        self.proto.maxPerScene = value

    @property
    def allowedAfter(self) -> float:
        return self.proto.allowedAfter

    @allowedAfter.setter
    def allowedAfter(self, value: float):
        self.proto.allowedAfter = value

    def _update_proto_references(self, proto: pd_spawn_pb2.AgentStateProbabilityConfig):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.SpawnConfigPreset)
class SpawnConfigPreset(ProtoMessageClass):
    """
    Args:
        random_generator: :attr:`random_generator`
        junction_generator: :attr:`junction_generator`
        voi_generator: :attr:`voi_generator`
        kitti_generator: :attr:`kitti_generator`
        position_generator: :attr:`position_generator`
        searchRadius: :attr:`searchRadius`
        startVelocity: :attr:`startVelocity`
        startVelocitySpread: :attr:`startVelocitySpread`
        targetVelocity: :attr:`targetVelocity`
        targetVelocitySpread: :attr:`targetVelocitySpread`
        vehicleDensityModifier: :attr:`vehicleDensityModifier`
        aggression: :attr:`aggression`
        aggressionSpread: :attr:`aggressionSpread`
        laneOffset: :attr:`laneOffset`
        laneOffsetSpread: :attr:`laneOffsetSpread`
        laneDriftAmp: :attr:`laneDriftAmp`
        laneDriftAmpSpread: :attr:`laneDriftAmpSpread`
        laneDriftScale: :attr:`laneDriftScale`
        laneDriftScaleSpread: :attr:`laneDriftScaleSpread`
        pedestrianSpawnRadius: :attr:`pedestrianSpawnRadius`
        pedestrianVelocity: :attr:`pedestrianVelocity`
        pedestrianVelocitySpread: :attr:`pedestrianVelocitySpread`
        numberOfPedestrians: :attr:`numberOfPedestrians`
        numberOfAnimals: :attr:`numberOfAnimals`
        enableCrosswalkPlacement: :attr:`enableCrosswalkPlacement`
        enableDynamicLaneSelection: :attr:`enableDynamicLaneSelection`
        enableJunctionPlacement: :attr:`enableJunctionPlacement`
        egoRoadTypes: :attr:`egoRoadTypes`
        vehicleRoadTypes: :attr:`vehicleRoadTypes`
        bicyclesOnlyInBikeLanes: :attr:`bicyclesOnlyInBikeLanes`
        egoLaneChangeChance: :attr:`egoLaneChangeChance`
        egoLaneChangeChanceSpread: :attr:`egoLaneChangeChanceSpread`
        egoLaneChangeCooldown: :attr:`egoLaneChangeCooldown`
        egoLaneChangeCooldownSpread: :attr:`egoLaneChangeCooldownSpread`
        egoPedestrians: :attr:`egoPedestrians`
        spawnPedestriansOnRoad: :attr:`spawnPedestriansOnRoad`
        egoPedestrianExclusionRadius: :attr:`egoPedestrianExclusionRadius`
        egoPedestrianExclusionRadiusSpread: :attr:`egoPedestrianExclusionRadiusSpread`
        disableAccessories: :attr:`disableAccessories`
        disableOccupants: :attr:`disableOccupants`
        alignEgoPedestrianToLane: :attr:`alignEgoPedestrianToLane`
        emergencyLightsOnProbability: :attr:`emergencyLightsOnProbability`
        emergencyLightsOnProbabilitySpread: :attr:`emergencyLightsOnProbabilitySpread`
        parkingTypeDistribution: :attr:`parkingTypeDistribution`
        parkedVehicleSpawnProbability: :attr:`parkedVehicleSpawnProbability`
        parkedVehicleSpawnProbabilitySpread: :attr:`parkedVehicleSpawnProbabilitySpread`
        parkedVehicleSpawnRadius: :attr:`parkedVehicleSpawnRadius`
        egoMinDistToEdge: :attr:`egoMinDistToEdge`
        egoMinDistToEdgeSpread: :attr:`egoMinDistToEdgeSpread`
        egoMinPathLength: :attr:`egoMinPathLength`
        egoMinPathLengthSpread: :attr:`egoMinPathLengthSpread`
        egoForceMinLengthBehind: :attr:`egoForceMinLengthBehind`
        laneChangeChance: :attr:`laneChangeChance`
        laneChangeChanceSpread: :attr:`laneChangeChanceSpread`
        laneChangeCooldown: :attr:`laneChangeCooldown`
        laneChangeCooldownSpread: :attr:`laneChangeCooldownSpread`
        egoVehicleModel: :attr:`egoVehicleModel`
        pedestrianColorOverrideChance: :attr:`pedestrianColorOverrideChance`
        pedestrianColorOverrideChanceSpread: :attr:`pedestrianColorOverrideChanceSpread`
        pedestrianColorOverrideRGB: :attr:`pedestrianColorOverrideRGB`
        vehicleDistribution: :attr:`vehicleDistribution`
        rollingStop: :attr:`rollingStop`
        stopLineOffset: :attr:`stopLineOffset`
        proceedOutOfTurnProbability: :attr:`proceedOutOfTurnProbability`
        agentStateProbabilities: :attr:`agentStateProbabilities`
        pedestrianJaywalkLookAhead: :attr:`pedestrianJaywalkLookAhead`
        pedestrianJaywalkRadius: :attr:`pedestrianJaywalkRadius`
        pedestrianJaywalkAngle: :attr:`pedestrianJaywalkAngle`
        pedestrianSpawnTightness: :attr:`pedestrianSpawnTightness`
        pedestrianSpawnMinEdgeDistance: :attr:`pedestrianSpawnMinEdgeDistance`
        enableDrivewayPlacement: :attr:`enableDrivewayPlacement`
        turnTypeDistribution: :attr:`turnTypeDistribution`
        startSeparationTime: :attr:`startSeparationTime`
        targetSeparationTime: :attr:`targetSeparationTime`
        egoMinLaneCountDist: :attr:`egoMinLaneCountDist`
        laneStartOffset: :attr:`laneStartOffset`
        applyRollingStopToEgo: :attr:`applyRollingStopToEgo`
        applyStopLineOffsetToEgo: :attr:`applyStopLineOffsetToEgo`
        applyProceedOutOfTurnProbabilityToEgo: :attr:`applyProceedOutOfTurnProbabilityToEgo`
        signDensity: :attr:`signDensity`
        crosswalkSignDensity: :attr:`crosswalkSignDensity`
        egoIgnoreObstacleTypes: :attr:`egoIgnoreObstacleTypes`
        markerDataMap: :attr:`markerDataMap`
        randomizeVehicleParts: :attr:`randomizeVehicleParts`
        instanceParallelParkingSpaces: :attr:`instanceParallelParkingSpaces`
        instanceParallelParkingMarkers: :attr:`instanceParallelParkingMarkers`
        region: :attr:`region`
        spawnTrailerProbabilities: :attr:`spawnTrailerProbabilities`
        spawnTrailerOnEgoProbability: :attr:`spawnTrailerOnEgoProbability`
        minNumberOfPedestrians: :attr:`minNumberOfPedestrians`
        pedestriansSpawnInParkingLot: :attr:`pedestriansSpawnInParkingLot`
        lightFlashingPeriod: :attr:`lightFlashingPeriod`
        lightIlluminatedPercentage: :attr:`lightIlluminatedPercentage`
        pedestriansDynamicPathing: :attr:`pedestriansDynamicPathing`
        useStaticTrailers: :attr:`useStaticTrailers`
        minNumberOfAnimals: :attr:`minNumberOfAnimals`
        animalSpeciesAllowed: :attr:`animalSpeciesAllowed`
        restrictLargeVehicleLaneCurvature: :attr:`restrictLargeVehicleLaneCurvature`
        largeVehicleTurnRadiusMultiple: :attr:`largeVehicleTurnRadiusMultiple`
        parking_space_data: :attr:`parking_space_data`
        object_decoration_params: :attr:`object_decoration_params`
        object_decoration_radius: :attr:`object_decoration_radius`
        ego_parking_space_decoration_params: :attr:`ego_parking_space_decoration_params`
    Attributes:
        random_generator:
        junction_generator:
        voi_generator:
        kitti_generator:
        position_generator:
        searchRadius: Default: 150.0
        startVelocity: Default: 20.0
        startVelocitySpread: Default: 2.0
        targetVelocity: Default: 25.0
        targetVelocitySpread: Default: 2.0
        vehicleDensityModifier: Default: 0.8
        aggression: Default: 0.5
        aggressionSpread: Default: 0.2
        laneOffset: Default: 0.0
        laneOffsetSpread: Default: 0.25
        laneDriftAmp: Default: 0.75
        laneDriftAmpSpread: Default: 0.25
        laneDriftScale: Default: 100.0
        laneDriftScaleSpread: Default: 20.0
        pedestrianSpawnRadius: Default: 75.0
        pedestrianVelocity: Default: 1.1
        pedestrianVelocitySpread: Default: 0.5
        numberOfPedestrians: Default: 100
        numberOfAnimals: Default: 2
        enableCrosswalkPlacement: Default: False
        enableDynamicLaneSelection: Default: True
        enableJunctionPlacement: Default: False
        egoRoadTypes:
        vehicleRoadTypes:
        bicyclesOnlyInBikeLanes: Default: True
        egoLaneChangeChance: Default: 0.005
        egoLaneChangeChanceSpread: Default: 0.0
        egoLaneChangeCooldown: Default: 10.0
        egoLaneChangeCooldownSpread: Default: 0.0
        egoPedestrians: Default: False
        spawnPedestriansOnRoad: Default: False
        egoPedestrianExclusionRadius: Default: 5.0
        egoPedestrianExclusionRadiusSpread: Default: 0.0
        disableAccessories: Default: False
        disableOccupants: Default: False
        alignEgoPedestrianToLane: Default: True
        emergencyLightsOnProbability: Default: 0.2
        emergencyLightsOnProbabilitySpread: Default: 0.0
        parkingTypeDistribution:
        parkedVehicleSpawnProbability: Default: 0.4
        parkedVehicleSpawnProbabilitySpread: Default: 0.1
        parkedVehicleSpawnRadius: Default: 50.0
        egoMinDistToEdge: Default: 100.0
        egoMinDistToEdgeSpread: Default: 0.0
        egoMinPathLength: Default: 200.0
        egoMinPathLengthSpread: Default: 0.0
        egoForceMinLengthBehind: Default: False
        laneChangeChance: Default: 0.005
        laneChangeChanceSpread: Default: 0.0
        laneChangeCooldown: Default: 10.0
        laneChangeCooldownSpread: Default: 0.0
        egoVehicleModel: Default: suv_medium_02
        pedestrianColorOverrideChance: Default: 0.0
        pedestrianColorOverrideChanceSpread: Default: 0.0
        pedestrianColorOverrideRGB:
        vehicleDistribution:
        rollingStop:
        stopLineOffset:
        proceedOutOfTurnProbability: Default: 0.0
        agentStateProbabilities:
        pedestrianJaywalkLookAhead: Default: 10.0
        pedestrianJaywalkRadius: Default: 15.0
        pedestrianJaywalkAngle: Default: 35.0
        pedestrianSpawnTightness: Default: 2.4
        pedestrianSpawnMinEdgeDistance: Default: 0.0
        enableDrivewayPlacement: Default: False
        turnTypeDistribution:
        startSeparationTime:
        targetSeparationTime:
        egoMinLaneCountDist:
        laneStartOffset:
        applyRollingStopToEgo: Default: True
        applyStopLineOffsetToEgo: Default: True
        applyProceedOutOfTurnProbabilityToEgo: Default: True
        signDensity:
        crosswalkSignDensity:
        egoIgnoreObstacleTypes:
        markerDataMap:
        randomizeVehicleParts: Default: True
        instanceParallelParkingSpaces: Default: True
        instanceParallelParkingMarkers: Default: True
        region: Default: None
        spawnTrailerProbabilities:
        spawnTrailerOnEgoProbability: Default: 0.0
        minNumberOfPedestrians: Default: 0
        pedestriansSpawnInParkingLot: Default: False
        lightFlashingPeriod:
        lightIlluminatedPercentage:
        pedestriansDynamicPathing: Default: True
        useStaticTrailers: Default: False
        minNumberOfAnimals: Default: 0
        animalSpeciesAllowed: Default: dog,cat,rabbit,raccoon,squirrel
        restrictLargeVehicleLaneCurvature: Default: True
        largeVehicleTurnRadiusMultiple: Default: 3.0
        parking_space_data:
        object_decoration_params:
        object_decoration_radius:
        ego_parking_space_decoration_params:"""

    class RoadType(ProtoEnumClass):
        MOTORWAY = 0
        TRUNK = 1
        PRIMARY = 2
        SECONDARY = 3
        TERTIARY = 4
        UNCLASSIFIED = 5
        RESIDENTIAL = 6
        MOTORWAY_LINK = 7
        TRUNK_LINK = 8
        PRIMARY_LINK = 9
        SECONDARY_LINK = 10
        TERTIARY_LINK = 11
        SERVICE = 12
        DRIVEWAY = 13
        PARKING_AISLE = 14

    _proto_message = pd_spawn_pb2.SpawnConfigPreset

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.SpawnConfigPreset] = None,
        random_generator: RandomScenarioGenerator = None,
        junction_generator: JunctionScenarioGenerator = None,
        voi_generator: VehicleOfInterestGenerator = None,
        kitti_generator: KittiScenarioGenerator = None,
        position_generator: PositionGenerator = None,
        searchRadius: float = None,
        startVelocity: float = None,
        startVelocitySpread: float = None,
        targetVelocity: float = None,
        targetVelocitySpread: float = None,
        vehicleDensityModifier: float = None,
        aggression: float = None,
        aggressionSpread: float = None,
        laneOffset: float = None,
        laneOffsetSpread: float = None,
        laneDriftAmp: float = None,
        laneDriftAmpSpread: float = None,
        laneDriftScale: float = None,
        laneDriftScaleSpread: float = None,
        pedestrianSpawnRadius: float = None,
        pedestrianVelocity: float = None,
        pedestrianVelocitySpread: float = None,
        numberOfPedestrians: int = None,
        numberOfAnimals: int = None,
        enableCrosswalkPlacement: bool = None,
        enableDynamicLaneSelection: bool = None,
        enableJunctionPlacement: bool = None,
        egoRoadTypes: List[SpawnConfigPreset.RoadType] = None,
        vehicleRoadTypes: List[SpawnConfigPreset.RoadType] = None,
        bicyclesOnlyInBikeLanes: bool = None,
        egoLaneChangeChance: float = None,
        egoLaneChangeChanceSpread: float = None,
        egoLaneChangeCooldown: float = None,
        egoLaneChangeCooldownSpread: float = None,
        egoPedestrians: bool = None,
        spawnPedestriansOnRoad: bool = None,
        egoPedestrianExclusionRadius: float = None,
        egoPedestrianExclusionRadiusSpread: float = None,
        disableAccessories: bool = None,
        disableOccupants: bool = None,
        alignEgoPedestrianToLane: bool = None,
        emergencyLightsOnProbability: float = None,
        emergencyLightsOnProbabilitySpread: float = None,
        parkingTypeDistribution: _pd_unified_generator_pb2.ParkingTypeDistribution = None,
        parkedVehicleSpawnProbability: float = None,
        parkedVehicleSpawnProbabilitySpread: float = None,
        parkedVehicleSpawnRadius: float = None,
        egoMinDistToEdge: float = None,
        egoMinDistToEdgeSpread: float = None,
        egoMinPathLength: float = None,
        egoMinPathLengthSpread: float = None,
        egoForceMinLengthBehind: bool = None,
        laneChangeChance: float = None,
        laneChangeChanceSpread: float = None,
        laneChangeCooldown: float = None,
        laneChangeCooldownSpread: float = None,
        egoVehicleModel: str = None,
        pedestrianColorOverrideChance: float = None,
        pedestrianColorOverrideChanceSpread: float = None,
        pedestrianColorOverrideRGB: List[float] = None,
        vehicleDistribution: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight] = None,
        rollingStop: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig = None,
        stopLineOffset: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig = None,
        proceedOutOfTurnProbability: float = None,
        agentStateProbabilities: List[AgentStateProbabilityConfig] = None,
        pedestrianJaywalkLookAhead: float = None,
        pedestrianJaywalkRadius: float = None,
        pedestrianJaywalkAngle: float = None,
        pedestrianSpawnTightness: float = None,
        pedestrianSpawnMinEdgeDistance: float = None,
        enableDrivewayPlacement: bool = None,
        turnTypeDistribution: _pd_distributions_pb2.EnumDistribution = None,
        startSeparationTime: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig] = None,
        targetSeparationTime: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig] = None,
        egoMinLaneCountDist: _pd_unified_generator_pb2.CenterSpreadConfigInt = None,
        laneStartOffset: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        applyRollingStopToEgo: bool = None,
        applyStopLineOffsetToEgo: bool = None,
        applyProceedOutOfTurnProbabilityToEgo: bool = None,
        signDensity: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        crosswalkSignDensity: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        egoIgnoreObstacleTypes: List[str] = None,
        markerDataMap: Dict[str, _pd_unified_generator_pb2.RoadMarkingData] = None,
        randomizeVehicleParts: bool = None,
        instanceParallelParkingSpaces: bool = None,
        instanceParallelParkingMarkers: bool = None,
        region: str = None,
        spawnTrailerProbabilities: Dict[str, float] = None,
        spawnTrailerOnEgoProbability: float = None,
        minNumberOfPedestrians: int = None,
        pedestriansSpawnInParkingLot: bool = None,
        lightFlashingPeriod: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        lightIlluminatedPercentage: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        pedestriansDynamicPathing: bool = None,
        useStaticTrailers: bool = None,
        minNumberOfAnimals: int = None,
        animalSpeciesAllowed: str = None,
        restrictLargeVehicleLaneCurvature: bool = None,
        largeVehicleTurnRadiusMultiple: float = None,
        parking_space_data: _pd_unified_generator_pb2.ParkingSpaceData = None,
        object_decoration_params: _pd_unified_generator_pb2.ObjectDecorationParams = None,
        object_decoration_radius: float = None,
        ego_parking_space_decoration_params: _pd_unified_generator_pb2.ObjectDecorationParams = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.SpawnConfigPreset()
        self.proto = proto
        self._random_generator = get_wrapper(proto_type=proto.random_generator.__class__)(proto=proto.random_generator)
        self._junction_generator = get_wrapper(proto_type=proto.junction_generator.__class__)(
            proto=proto.junction_generator
        )
        self._voi_generator = get_wrapper(proto_type=proto.voi_generator.__class__)(proto=proto.voi_generator)
        self._kitti_generator = get_wrapper(proto_type=proto.kitti_generator.__class__)(proto=proto.kitti_generator)
        self._position_generator = get_wrapper(proto_type=proto.position_generator.__class__)(
            proto=proto.position_generator
        )
        self._parkingTypeDistribution = get_wrapper(proto_type=proto.parkingTypeDistribution.__class__)(
            proto=proto.parkingTypeDistribution
        )
        self._vehicleDistribution = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicleDistribution.items()},
            attr_name="vehicleDistribution",
            dict_owner=self,
        )
        self._rollingStop = get_wrapper(proto_type=proto.rollingStop.__class__)(proto=proto.rollingStop)
        self._stopLineOffset = get_wrapper(proto_type=proto.stopLineOffset.__class__)(proto=proto.stopLineOffset)
        self._agentStateProbabilities = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.agentStateProbabilities],
            attr_name="agentStateProbabilities",
            list_owner=self,
        )
        self._turnTypeDistribution = get_wrapper(proto_type=proto.turnTypeDistribution.__class__)(
            proto=proto.turnTypeDistribution
        )
        self._startSeparationTime = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.startSeparationTime.items()},
            attr_name="startSeparationTime",
            dict_owner=self,
        )
        self._targetSeparationTime = ProtoDictWrapper(
            container={
                k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.targetSeparationTime.items()
            },
            attr_name="targetSeparationTime",
            dict_owner=self,
        )
        self._egoMinLaneCountDist = get_wrapper(proto_type=proto.egoMinLaneCountDist.__class__)(
            proto=proto.egoMinLaneCountDist
        )
        self._laneStartOffset = get_wrapper(proto_type=proto.laneStartOffset.__class__)(proto=proto.laneStartOffset)
        self._signDensity = get_wrapper(proto_type=proto.signDensity.__class__)(proto=proto.signDensity)
        self._crosswalkSignDensity = get_wrapper(proto_type=proto.crosswalkSignDensity.__class__)(
            proto=proto.crosswalkSignDensity
        )
        self._markerDataMap = ProtoDictWrapper(
            container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.markerDataMap.items()},
            attr_name="markerDataMap",
            dict_owner=self,
        )
        self._lightFlashingPeriod = get_wrapper(proto_type=proto.lightFlashingPeriod.__class__)(
            proto=proto.lightFlashingPeriod
        )
        self._lightIlluminatedPercentage = get_wrapper(proto_type=proto.lightIlluminatedPercentage.__class__)(
            proto=proto.lightIlluminatedPercentage
        )
        self._parking_space_data = get_wrapper(proto_type=proto.parking_space_data.__class__)(
            proto=proto.parking_space_data
        )
        self._object_decoration_params = get_wrapper(proto_type=proto.object_decoration_params.__class__)(
            proto=proto.object_decoration_params
        )
        self._ego_parking_space_decoration_params = get_wrapper(
            proto_type=proto.ego_parking_space_decoration_params.__class__
        )(proto=proto.ego_parking_space_decoration_params)
        if random_generator is not None:
            self.random_generator = random_generator
        if junction_generator is not None:
            self.junction_generator = junction_generator
        if voi_generator is not None:
            self.voi_generator = voi_generator
        if kitti_generator is not None:
            self.kitti_generator = kitti_generator
        if position_generator is not None:
            self.position_generator = position_generator
        if searchRadius is not None:
            self.searchRadius = searchRadius
        if startVelocity is not None:
            self.startVelocity = startVelocity
        if startVelocitySpread is not None:
            self.startVelocitySpread = startVelocitySpread
        if targetVelocity is not None:
            self.targetVelocity = targetVelocity
        if targetVelocitySpread is not None:
            self.targetVelocitySpread = targetVelocitySpread
        if vehicleDensityModifier is not None:
            self.vehicleDensityModifier = vehicleDensityModifier
        if aggression is not None:
            self.aggression = aggression
        if aggressionSpread is not None:
            self.aggressionSpread = aggressionSpread
        if laneOffset is not None:
            self.laneOffset = laneOffset
        if laneOffsetSpread is not None:
            self.laneOffsetSpread = laneOffsetSpread
        if laneDriftAmp is not None:
            self.laneDriftAmp = laneDriftAmp
        if laneDriftAmpSpread is not None:
            self.laneDriftAmpSpread = laneDriftAmpSpread
        if laneDriftScale is not None:
            self.laneDriftScale = laneDriftScale
        if laneDriftScaleSpread is not None:
            self.laneDriftScaleSpread = laneDriftScaleSpread
        if pedestrianSpawnRadius is not None:
            self.pedestrianSpawnRadius = pedestrianSpawnRadius
        if pedestrianVelocity is not None:
            self.pedestrianVelocity = pedestrianVelocity
        if pedestrianVelocitySpread is not None:
            self.pedestrianVelocitySpread = pedestrianVelocitySpread
        if numberOfPedestrians is not None:
            self.numberOfPedestrians = numberOfPedestrians
        if numberOfAnimals is not None:
            self.numberOfAnimals = numberOfAnimals
        if enableCrosswalkPlacement is not None:
            self.enableCrosswalkPlacement = enableCrosswalkPlacement
        if enableDynamicLaneSelection is not None:
            self.enableDynamicLaneSelection = enableDynamicLaneSelection
        if enableJunctionPlacement is not None:
            self.enableJunctionPlacement = enableJunctionPlacement
        self._egoRoadTypes = ProtoListWrapper(
            container=[SpawnConfigPreset.RoadType(v) for v in proto.egoRoadTypes],
            attr_name="egoRoadTypes",
            list_owner=self,
        )
        if egoRoadTypes is not None:
            self.egoRoadTypes = egoRoadTypes
        self._vehicleRoadTypes = ProtoListWrapper(
            container=[SpawnConfigPreset.RoadType(v) for v in proto.vehicleRoadTypes],
            attr_name="vehicleRoadTypes",
            list_owner=self,
        )
        if vehicleRoadTypes is not None:
            self.vehicleRoadTypes = vehicleRoadTypes
        if bicyclesOnlyInBikeLanes is not None:
            self.bicyclesOnlyInBikeLanes = bicyclesOnlyInBikeLanes
        if egoLaneChangeChance is not None:
            self.egoLaneChangeChance = egoLaneChangeChance
        if egoLaneChangeChanceSpread is not None:
            self.egoLaneChangeChanceSpread = egoLaneChangeChanceSpread
        if egoLaneChangeCooldown is not None:
            self.egoLaneChangeCooldown = egoLaneChangeCooldown
        if egoLaneChangeCooldownSpread is not None:
            self.egoLaneChangeCooldownSpread = egoLaneChangeCooldownSpread
        if egoPedestrians is not None:
            self.egoPedestrians = egoPedestrians
        if spawnPedestriansOnRoad is not None:
            self.spawnPedestriansOnRoad = spawnPedestriansOnRoad
        if egoPedestrianExclusionRadius is not None:
            self.egoPedestrianExclusionRadius = egoPedestrianExclusionRadius
        if egoPedestrianExclusionRadiusSpread is not None:
            self.egoPedestrianExclusionRadiusSpread = egoPedestrianExclusionRadiusSpread
        if disableAccessories is not None:
            self.disableAccessories = disableAccessories
        if disableOccupants is not None:
            self.disableOccupants = disableOccupants
        if alignEgoPedestrianToLane is not None:
            self.alignEgoPedestrianToLane = alignEgoPedestrianToLane
        if emergencyLightsOnProbability is not None:
            self.emergencyLightsOnProbability = emergencyLightsOnProbability
        if emergencyLightsOnProbabilitySpread is not None:
            self.emergencyLightsOnProbabilitySpread = emergencyLightsOnProbabilitySpread
        if parkingTypeDistribution is not None:
            self.parkingTypeDistribution = parkingTypeDistribution
        if parkedVehicleSpawnProbability is not None:
            self.parkedVehicleSpawnProbability = parkedVehicleSpawnProbability
        if parkedVehicleSpawnProbabilitySpread is not None:
            self.parkedVehicleSpawnProbabilitySpread = parkedVehicleSpawnProbabilitySpread
        if parkedVehicleSpawnRadius is not None:
            self.parkedVehicleSpawnRadius = parkedVehicleSpawnRadius
        if egoMinDistToEdge is not None:
            self.egoMinDistToEdge = egoMinDistToEdge
        if egoMinDistToEdgeSpread is not None:
            self.egoMinDistToEdgeSpread = egoMinDistToEdgeSpread
        if egoMinPathLength is not None:
            self.egoMinPathLength = egoMinPathLength
        if egoMinPathLengthSpread is not None:
            self.egoMinPathLengthSpread = egoMinPathLengthSpread
        if egoForceMinLengthBehind is not None:
            self.egoForceMinLengthBehind = egoForceMinLengthBehind
        if laneChangeChance is not None:
            self.laneChangeChance = laneChangeChance
        if laneChangeChanceSpread is not None:
            self.laneChangeChanceSpread = laneChangeChanceSpread
        if laneChangeCooldown is not None:
            self.laneChangeCooldown = laneChangeCooldown
        if laneChangeCooldownSpread is not None:
            self.laneChangeCooldownSpread = laneChangeCooldownSpread
        if egoVehicleModel is not None:
            self.egoVehicleModel = egoVehicleModel
        if pedestrianColorOverrideChance is not None:
            self.pedestrianColorOverrideChance = pedestrianColorOverrideChance
        if pedestrianColorOverrideChanceSpread is not None:
            self.pedestrianColorOverrideChanceSpread = pedestrianColorOverrideChanceSpread
        self._pedestrianColorOverrideRGB = ProtoListWrapper(
            container=[float(v) for v in proto.pedestrianColorOverrideRGB],
            attr_name="pedestrianColorOverrideRGB",
            list_owner=self,
        )
        if pedestrianColorOverrideRGB is not None:
            self.pedestrianColorOverrideRGB = pedestrianColorOverrideRGB
        if vehicleDistribution is not None:
            self.vehicleDistribution = vehicleDistribution
        if rollingStop is not None:
            self.rollingStop = rollingStop
        if stopLineOffset is not None:
            self.stopLineOffset = stopLineOffset
        if proceedOutOfTurnProbability is not None:
            self.proceedOutOfTurnProbability = proceedOutOfTurnProbability
        if agentStateProbabilities is not None:
            self.agentStateProbabilities = agentStateProbabilities
        if pedestrianJaywalkLookAhead is not None:
            self.pedestrianJaywalkLookAhead = pedestrianJaywalkLookAhead
        if pedestrianJaywalkRadius is not None:
            self.pedestrianJaywalkRadius = pedestrianJaywalkRadius
        if pedestrianJaywalkAngle is not None:
            self.pedestrianJaywalkAngle = pedestrianJaywalkAngle
        if pedestrianSpawnTightness is not None:
            self.pedestrianSpawnTightness = pedestrianSpawnTightness
        if pedestrianSpawnMinEdgeDistance is not None:
            self.pedestrianSpawnMinEdgeDistance = pedestrianSpawnMinEdgeDistance
        if enableDrivewayPlacement is not None:
            self.enableDrivewayPlacement = enableDrivewayPlacement
        if turnTypeDistribution is not None:
            self.turnTypeDistribution = turnTypeDistribution
        if startSeparationTime is not None:
            self.startSeparationTime = startSeparationTime
        if targetSeparationTime is not None:
            self.targetSeparationTime = targetSeparationTime
        if egoMinLaneCountDist is not None:
            self.egoMinLaneCountDist = egoMinLaneCountDist
        if laneStartOffset is not None:
            self.laneStartOffset = laneStartOffset
        if applyRollingStopToEgo is not None:
            self.applyRollingStopToEgo = applyRollingStopToEgo
        if applyStopLineOffsetToEgo is not None:
            self.applyStopLineOffsetToEgo = applyStopLineOffsetToEgo
        if applyProceedOutOfTurnProbabilityToEgo is not None:
            self.applyProceedOutOfTurnProbabilityToEgo = applyProceedOutOfTurnProbabilityToEgo
        if signDensity is not None:
            self.signDensity = signDensity
        if crosswalkSignDensity is not None:
            self.crosswalkSignDensity = crosswalkSignDensity
        self._egoIgnoreObstacleTypes = ProtoListWrapper(
            container=[str(v) for v in proto.egoIgnoreObstacleTypes],
            attr_name="egoIgnoreObstacleTypes",
            list_owner=self,
        )
        if egoIgnoreObstacleTypes is not None:
            self.egoIgnoreObstacleTypes = egoIgnoreObstacleTypes
        if markerDataMap is not None:
            self.markerDataMap = markerDataMap
        if randomizeVehicleParts is not None:
            self.randomizeVehicleParts = randomizeVehicleParts
        if instanceParallelParkingSpaces is not None:
            self.instanceParallelParkingSpaces = instanceParallelParkingSpaces
        if instanceParallelParkingMarkers is not None:
            self.instanceParallelParkingMarkers = instanceParallelParkingMarkers
        if region is not None:
            self.region = region
        self._spawnTrailerProbabilities = ProtoDictWrapper(
            container={k: float(v) for (k, v) in proto.spawnTrailerProbabilities.items()},
            attr_name="spawnTrailerProbabilities",
            dict_owner=self,
        )
        if spawnTrailerProbabilities is not None:
            self.spawnTrailerProbabilities = spawnTrailerProbabilities
        if spawnTrailerOnEgoProbability is not None:
            self.spawnTrailerOnEgoProbability = spawnTrailerOnEgoProbability
        if minNumberOfPedestrians is not None:
            self.minNumberOfPedestrians = minNumberOfPedestrians
        if pedestriansSpawnInParkingLot is not None:
            self.pedestriansSpawnInParkingLot = pedestriansSpawnInParkingLot
        if lightFlashingPeriod is not None:
            self.lightFlashingPeriod = lightFlashingPeriod
        if lightIlluminatedPercentage is not None:
            self.lightIlluminatedPercentage = lightIlluminatedPercentage
        if pedestriansDynamicPathing is not None:
            self.pedestriansDynamicPathing = pedestriansDynamicPathing
        if useStaticTrailers is not None:
            self.useStaticTrailers = useStaticTrailers
        if minNumberOfAnimals is not None:
            self.minNumberOfAnimals = minNumberOfAnimals
        if animalSpeciesAllowed is not None:
            self.animalSpeciesAllowed = animalSpeciesAllowed
        if restrictLargeVehicleLaneCurvature is not None:
            self.restrictLargeVehicleLaneCurvature = restrictLargeVehicleLaneCurvature
        if largeVehicleTurnRadiusMultiple is not None:
            self.largeVehicleTurnRadiusMultiple = largeVehicleTurnRadiusMultiple
        if parking_space_data is not None:
            self.parking_space_data = parking_space_data
        if object_decoration_params is not None:
            self.object_decoration_params = object_decoration_params
        if object_decoration_radius is not None:
            self.object_decoration_radius = object_decoration_radius
        if ego_parking_space_decoration_params is not None:
            self.ego_parking_space_decoration_params = ego_parking_space_decoration_params

    @property
    def random_generator(self) -> RandomScenarioGenerator:
        return self._random_generator

    @random_generator.setter
    def random_generator(self, value: RandomScenarioGenerator):
        self.proto.random_generator.CopyFrom(value.proto)

        self._random_generator = value
        self._random_generator._update_proto_references(self.proto.random_generator)

    @property
    def junction_generator(self) -> JunctionScenarioGenerator:
        return self._junction_generator

    @junction_generator.setter
    def junction_generator(self, value: JunctionScenarioGenerator):
        self.proto.junction_generator.CopyFrom(value.proto)

        self._junction_generator = value
        self._junction_generator._update_proto_references(self.proto.junction_generator)

    @property
    def voi_generator(self) -> VehicleOfInterestGenerator:
        return self._voi_generator

    @voi_generator.setter
    def voi_generator(self, value: VehicleOfInterestGenerator):
        self.proto.voi_generator.CopyFrom(value.proto)

        self._voi_generator = value
        self._voi_generator._update_proto_references(self.proto.voi_generator)

    @property
    def kitti_generator(self) -> KittiScenarioGenerator:
        return self._kitti_generator

    @kitti_generator.setter
    def kitti_generator(self, value: KittiScenarioGenerator):
        self.proto.kitti_generator.CopyFrom(value.proto)

        self._kitti_generator = value
        self._kitti_generator._update_proto_references(self.proto.kitti_generator)

    @property
    def position_generator(self) -> PositionGenerator:
        return self._position_generator

    @position_generator.setter
    def position_generator(self, value: PositionGenerator):
        self.proto.position_generator.CopyFrom(value.proto)

        self._position_generator = value
        self._position_generator._update_proto_references(self.proto.position_generator)

    @property
    def searchRadius(self) -> float:
        return self.proto.searchRadius

    @searchRadius.setter
    def searchRadius(self, value: float):
        self.proto.searchRadius = value

    @property
    def startVelocity(self) -> float:
        return self.proto.startVelocity

    @startVelocity.setter
    def startVelocity(self, value: float):
        self.proto.startVelocity = value

    @property
    def startVelocitySpread(self) -> float:
        return self.proto.startVelocitySpread

    @startVelocitySpread.setter
    def startVelocitySpread(self, value: float):
        self.proto.startVelocitySpread = value

    @property
    def targetVelocity(self) -> float:
        return self.proto.targetVelocity

    @targetVelocity.setter
    def targetVelocity(self, value: float):
        self.proto.targetVelocity = value

    @property
    def targetVelocitySpread(self) -> float:
        return self.proto.targetVelocitySpread

    @targetVelocitySpread.setter
    def targetVelocitySpread(self, value: float):
        self.proto.targetVelocitySpread = value

    @property
    def vehicleDensityModifier(self) -> float:
        return self.proto.vehicleDensityModifier

    @vehicleDensityModifier.setter
    def vehicleDensityModifier(self, value: float):
        self.proto.vehicleDensityModifier = value

    @property
    def aggression(self) -> float:
        return self.proto.aggression

    @aggression.setter
    def aggression(self, value: float):
        self.proto.aggression = value

    @property
    def aggressionSpread(self) -> float:
        return self.proto.aggressionSpread

    @aggressionSpread.setter
    def aggressionSpread(self, value: float):
        self.proto.aggressionSpread = value

    @property
    def laneOffset(self) -> float:
        return self.proto.laneOffset

    @laneOffset.setter
    def laneOffset(self, value: float):
        self.proto.laneOffset = value

    @property
    def laneOffsetSpread(self) -> float:
        return self.proto.laneOffsetSpread

    @laneOffsetSpread.setter
    def laneOffsetSpread(self, value: float):
        self.proto.laneOffsetSpread = value

    @property
    def laneDriftAmp(self) -> float:
        return self.proto.laneDriftAmp

    @laneDriftAmp.setter
    def laneDriftAmp(self, value: float):
        self.proto.laneDriftAmp = value

    @property
    def laneDriftAmpSpread(self) -> float:
        return self.proto.laneDriftAmpSpread

    @laneDriftAmpSpread.setter
    def laneDriftAmpSpread(self, value: float):
        self.proto.laneDriftAmpSpread = value

    @property
    def laneDriftScale(self) -> float:
        return self.proto.laneDriftScale

    @laneDriftScale.setter
    def laneDriftScale(self, value: float):
        self.proto.laneDriftScale = value

    @property
    def laneDriftScaleSpread(self) -> float:
        return self.proto.laneDriftScaleSpread

    @laneDriftScaleSpread.setter
    def laneDriftScaleSpread(self, value: float):
        self.proto.laneDriftScaleSpread = value

    @property
    def pedestrianSpawnRadius(self) -> float:
        return self.proto.pedestrianSpawnRadius

    @pedestrianSpawnRadius.setter
    def pedestrianSpawnRadius(self, value: float):
        self.proto.pedestrianSpawnRadius = value

    @property
    def pedestrianVelocity(self) -> float:
        return self.proto.pedestrianVelocity

    @pedestrianVelocity.setter
    def pedestrianVelocity(self, value: float):
        self.proto.pedestrianVelocity = value

    @property
    def pedestrianVelocitySpread(self) -> float:
        return self.proto.pedestrianVelocitySpread

    @pedestrianVelocitySpread.setter
    def pedestrianVelocitySpread(self, value: float):
        self.proto.pedestrianVelocitySpread = value

    @property
    def numberOfPedestrians(self) -> int:
        return self.proto.numberOfPedestrians

    @numberOfPedestrians.setter
    def numberOfPedestrians(self, value: int):
        self.proto.numberOfPedestrians = value

    @property
    def numberOfAnimals(self) -> int:
        return self.proto.numberOfAnimals

    @numberOfAnimals.setter
    def numberOfAnimals(self, value: int):
        self.proto.numberOfAnimals = value

    @property
    def enableCrosswalkPlacement(self) -> bool:
        return self.proto.enableCrosswalkPlacement

    @enableCrosswalkPlacement.setter
    def enableCrosswalkPlacement(self, value: bool):
        self.proto.enableCrosswalkPlacement = value

    @property
    def enableDynamicLaneSelection(self) -> bool:
        return self.proto.enableDynamicLaneSelection

    @enableDynamicLaneSelection.setter
    def enableDynamicLaneSelection(self, value: bool):
        self.proto.enableDynamicLaneSelection = value

    @property
    def enableJunctionPlacement(self) -> bool:
        return self.proto.enableJunctionPlacement

    @enableJunctionPlacement.setter
    def enableJunctionPlacement(self, value: bool):
        self.proto.enableJunctionPlacement = value

    @property
    def egoRoadTypes(self) -> List[SpawnConfigPreset.RoadType]:
        return self._egoRoadTypes

    @egoRoadTypes.setter
    def egoRoadTypes(self, value: List[SpawnConfigPreset.RoadType]):
        self._egoRoadTypes.clear()
        for v in value:
            self._egoRoadTypes.append(v)

    @property
    def vehicleRoadTypes(self) -> List[SpawnConfigPreset.RoadType]:
        return self._vehicleRoadTypes

    @vehicleRoadTypes.setter
    def vehicleRoadTypes(self, value: List[SpawnConfigPreset.RoadType]):
        self._vehicleRoadTypes.clear()
        for v in value:
            self._vehicleRoadTypes.append(v)

    @property
    def bicyclesOnlyInBikeLanes(self) -> bool:
        return self.proto.bicyclesOnlyInBikeLanes

    @bicyclesOnlyInBikeLanes.setter
    def bicyclesOnlyInBikeLanes(self, value: bool):
        self.proto.bicyclesOnlyInBikeLanes = value

    @property
    def egoLaneChangeChance(self) -> float:
        return self.proto.egoLaneChangeChance

    @egoLaneChangeChance.setter
    def egoLaneChangeChance(self, value: float):
        self.proto.egoLaneChangeChance = value

    @property
    def egoLaneChangeChanceSpread(self) -> float:
        return self.proto.egoLaneChangeChanceSpread

    @egoLaneChangeChanceSpread.setter
    def egoLaneChangeChanceSpread(self, value: float):
        self.proto.egoLaneChangeChanceSpread = value

    @property
    def egoLaneChangeCooldown(self) -> float:
        return self.proto.egoLaneChangeCooldown

    @egoLaneChangeCooldown.setter
    def egoLaneChangeCooldown(self, value: float):
        self.proto.egoLaneChangeCooldown = value

    @property
    def egoLaneChangeCooldownSpread(self) -> float:
        return self.proto.egoLaneChangeCooldownSpread

    @egoLaneChangeCooldownSpread.setter
    def egoLaneChangeCooldownSpread(self, value: float):
        self.proto.egoLaneChangeCooldownSpread = value

    @property
    def egoPedestrians(self) -> bool:
        return self.proto.egoPedestrians

    @egoPedestrians.setter
    def egoPedestrians(self, value: bool):
        self.proto.egoPedestrians = value

    @property
    def spawnPedestriansOnRoad(self) -> bool:
        return self.proto.spawnPedestriansOnRoad

    @spawnPedestriansOnRoad.setter
    def spawnPedestriansOnRoad(self, value: bool):
        self.proto.spawnPedestriansOnRoad = value

    @property
    def egoPedestrianExclusionRadius(self) -> float:
        return self.proto.egoPedestrianExclusionRadius

    @egoPedestrianExclusionRadius.setter
    def egoPedestrianExclusionRadius(self, value: float):
        self.proto.egoPedestrianExclusionRadius = value

    @property
    def egoPedestrianExclusionRadiusSpread(self) -> float:
        return self.proto.egoPedestrianExclusionRadiusSpread

    @egoPedestrianExclusionRadiusSpread.setter
    def egoPedestrianExclusionRadiusSpread(self, value: float):
        self.proto.egoPedestrianExclusionRadiusSpread = value

    @property
    def disableAccessories(self) -> bool:
        return self.proto.disableAccessories

    @disableAccessories.setter
    def disableAccessories(self, value: bool):
        self.proto.disableAccessories = value

    @property
    def disableOccupants(self) -> bool:
        return self.proto.disableOccupants

    @disableOccupants.setter
    def disableOccupants(self, value: bool):
        self.proto.disableOccupants = value

    @property
    def alignEgoPedestrianToLane(self) -> bool:
        return self.proto.alignEgoPedestrianToLane

    @alignEgoPedestrianToLane.setter
    def alignEgoPedestrianToLane(self, value: bool):
        self.proto.alignEgoPedestrianToLane = value

    @property
    def emergencyLightsOnProbability(self) -> float:
        return self.proto.emergencyLightsOnProbability

    @emergencyLightsOnProbability.setter
    def emergencyLightsOnProbability(self, value: float):
        self.proto.emergencyLightsOnProbability = value

    @property
    def emergencyLightsOnProbabilitySpread(self) -> float:
        return self.proto.emergencyLightsOnProbabilitySpread

    @emergencyLightsOnProbabilitySpread.setter
    def emergencyLightsOnProbabilitySpread(self, value: float):
        self.proto.emergencyLightsOnProbabilitySpread = value

    @property
    def parkingTypeDistribution(self) -> _pd_unified_generator_pb2.ParkingTypeDistribution:
        return self._parkingTypeDistribution

    @parkingTypeDistribution.setter
    def parkingTypeDistribution(self, value: _pd_unified_generator_pb2.ParkingTypeDistribution):
        self.proto.parkingTypeDistribution.CopyFrom(value.proto)

        self._parkingTypeDistribution = value
        self._parkingTypeDistribution._update_proto_references(self.proto.parkingTypeDistribution)

    @property
    def parkedVehicleSpawnProbability(self) -> float:
        return self.proto.parkedVehicleSpawnProbability

    @parkedVehicleSpawnProbability.setter
    def parkedVehicleSpawnProbability(self, value: float):
        self.proto.parkedVehicleSpawnProbability = value

    @property
    def parkedVehicleSpawnProbabilitySpread(self) -> float:
        return self.proto.parkedVehicleSpawnProbabilitySpread

    @parkedVehicleSpawnProbabilitySpread.setter
    def parkedVehicleSpawnProbabilitySpread(self, value: float):
        self.proto.parkedVehicleSpawnProbabilitySpread = value

    @property
    def parkedVehicleSpawnRadius(self) -> float:
        return self.proto.parkedVehicleSpawnRadius

    @parkedVehicleSpawnRadius.setter
    def parkedVehicleSpawnRadius(self, value: float):
        self.proto.parkedVehicleSpawnRadius = value

    @property
    def egoMinDistToEdge(self) -> float:
        return self.proto.egoMinDistToEdge

    @egoMinDistToEdge.setter
    def egoMinDistToEdge(self, value: float):
        self.proto.egoMinDistToEdge = value

    @property
    def egoMinDistToEdgeSpread(self) -> float:
        return self.proto.egoMinDistToEdgeSpread

    @egoMinDistToEdgeSpread.setter
    def egoMinDistToEdgeSpread(self, value: float):
        self.proto.egoMinDistToEdgeSpread = value

    @property
    def egoMinPathLength(self) -> float:
        return self.proto.egoMinPathLength

    @egoMinPathLength.setter
    def egoMinPathLength(self, value: float):
        self.proto.egoMinPathLength = value

    @property
    def egoMinPathLengthSpread(self) -> float:
        return self.proto.egoMinPathLengthSpread

    @egoMinPathLengthSpread.setter
    def egoMinPathLengthSpread(self, value: float):
        self.proto.egoMinPathLengthSpread = value

    @property
    def egoForceMinLengthBehind(self) -> bool:
        return self.proto.egoForceMinLengthBehind

    @egoForceMinLengthBehind.setter
    def egoForceMinLengthBehind(self, value: bool):
        self.proto.egoForceMinLengthBehind = value

    @property
    def laneChangeChance(self) -> float:
        return self.proto.laneChangeChance

    @laneChangeChance.setter
    def laneChangeChance(self, value: float):
        self.proto.laneChangeChance = value

    @property
    def laneChangeChanceSpread(self) -> float:
        return self.proto.laneChangeChanceSpread

    @laneChangeChanceSpread.setter
    def laneChangeChanceSpread(self, value: float):
        self.proto.laneChangeChanceSpread = value

    @property
    def laneChangeCooldown(self) -> float:
        return self.proto.laneChangeCooldown

    @laneChangeCooldown.setter
    def laneChangeCooldown(self, value: float):
        self.proto.laneChangeCooldown = value

    @property
    def laneChangeCooldownSpread(self) -> float:
        return self.proto.laneChangeCooldownSpread

    @laneChangeCooldownSpread.setter
    def laneChangeCooldownSpread(self, value: float):
        self.proto.laneChangeCooldownSpread = value

    @property
    def egoVehicleModel(self) -> str:
        return self.proto.egoVehicleModel

    @egoVehicleModel.setter
    def egoVehicleModel(self, value: str):
        self.proto.egoVehicleModel = value

    @property
    def pedestrianColorOverrideChance(self) -> float:
        return self.proto.pedestrianColorOverrideChance

    @pedestrianColorOverrideChance.setter
    def pedestrianColorOverrideChance(self, value: float):
        self.proto.pedestrianColorOverrideChance = value

    @property
    def pedestrianColorOverrideChanceSpread(self) -> float:
        return self.proto.pedestrianColorOverrideChanceSpread

    @pedestrianColorOverrideChanceSpread.setter
    def pedestrianColorOverrideChanceSpread(self, value: float):
        self.proto.pedestrianColorOverrideChanceSpread = value

    @property
    def pedestrianColorOverrideRGB(self) -> List[float]:
        return self._pedestrianColorOverrideRGB

    @pedestrianColorOverrideRGB.setter
    def pedestrianColorOverrideRGB(self, value: List[float]):
        self._pedestrianColorOverrideRGB.clear()
        for v in value:
            self._pedestrianColorOverrideRGB.append(v)

    @property
    def vehicleDistribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicleDistribution

    @vehicleDistribution.setter
    def vehicleDistribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicleDistribution.clear()
        self._vehicleDistribution.update(value)

    @property
    def rollingStop(self) -> _pd_unified_generator_pb2.CenterSpreadProbabilityConfig:
        return self._rollingStop

    @rollingStop.setter
    def rollingStop(self, value: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig):
        self.proto.rollingStop.CopyFrom(value.proto)

        self._rollingStop = value
        self._rollingStop._update_proto_references(self.proto.rollingStop)

    @property
    def stopLineOffset(self) -> _pd_unified_generator_pb2.CenterSpreadProbabilityConfig:
        return self._stopLineOffset

    @stopLineOffset.setter
    def stopLineOffset(self, value: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig):
        self.proto.stopLineOffset.CopyFrom(value.proto)

        self._stopLineOffset = value
        self._stopLineOffset._update_proto_references(self.proto.stopLineOffset)

    @property
    def proceedOutOfTurnProbability(self) -> float:
        return self.proto.proceedOutOfTurnProbability

    @proceedOutOfTurnProbability.setter
    def proceedOutOfTurnProbability(self, value: float):
        self.proto.proceedOutOfTurnProbability = value

    @property
    def agentStateProbabilities(self) -> List[AgentStateProbabilityConfig]:
        return self._agentStateProbabilities

    @agentStateProbabilities.setter
    def agentStateProbabilities(self, value: List[AgentStateProbabilityConfig]):
        self._agentStateProbabilities.clear()
        for v in value:
            self._agentStateProbabilities.append(v)

    @property
    def pedestrianJaywalkLookAhead(self) -> float:
        return self.proto.pedestrianJaywalkLookAhead

    @pedestrianJaywalkLookAhead.setter
    def pedestrianJaywalkLookAhead(self, value: float):
        self.proto.pedestrianJaywalkLookAhead = value

    @property
    def pedestrianJaywalkRadius(self) -> float:
        return self.proto.pedestrianJaywalkRadius

    @pedestrianJaywalkRadius.setter
    def pedestrianJaywalkRadius(self, value: float):
        self.proto.pedestrianJaywalkRadius = value

    @property
    def pedestrianJaywalkAngle(self) -> float:
        return self.proto.pedestrianJaywalkAngle

    @pedestrianJaywalkAngle.setter
    def pedestrianJaywalkAngle(self, value: float):
        self.proto.pedestrianJaywalkAngle = value

    @property
    def pedestrianSpawnTightness(self) -> float:
        return self.proto.pedestrianSpawnTightness

    @pedestrianSpawnTightness.setter
    def pedestrianSpawnTightness(self, value: float):
        self.proto.pedestrianSpawnTightness = value

    @property
    def pedestrianSpawnMinEdgeDistance(self) -> float:
        return self.proto.pedestrianSpawnMinEdgeDistance

    @pedestrianSpawnMinEdgeDistance.setter
    def pedestrianSpawnMinEdgeDistance(self, value: float):
        self.proto.pedestrianSpawnMinEdgeDistance = value

    @property
    def enableDrivewayPlacement(self) -> bool:
        return self.proto.enableDrivewayPlacement

    @enableDrivewayPlacement.setter
    def enableDrivewayPlacement(self, value: bool):
        self.proto.enableDrivewayPlacement = value

    @property
    def turnTypeDistribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._turnTypeDistribution

    @turnTypeDistribution.setter
    def turnTypeDistribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.turnTypeDistribution.CopyFrom(value.proto)

        self._turnTypeDistribution = value
        self._turnTypeDistribution._update_proto_references(self.proto.turnTypeDistribution)

    @property
    def startSeparationTime(self) -> Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]:
        return self._startSeparationTime

    @startSeparationTime.setter
    def startSeparationTime(self, value: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]):
        self._startSeparationTime.clear()
        self._startSeparationTime.update(value)

    @property
    def targetSeparationTime(self) -> Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]:
        return self._targetSeparationTime

    @targetSeparationTime.setter
    def targetSeparationTime(self, value: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]):
        self._targetSeparationTime.clear()
        self._targetSeparationTime.update(value)

    @property
    def egoMinLaneCountDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._egoMinLaneCountDist

    @egoMinLaneCountDist.setter
    def egoMinLaneCountDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self.proto.egoMinLaneCountDist.CopyFrom(value.proto)

        self._egoMinLaneCountDist = value
        self._egoMinLaneCountDist._update_proto_references(self.proto.egoMinLaneCountDist)

    @property
    def laneStartOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._laneStartOffset

    @laneStartOffset.setter
    def laneStartOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.laneStartOffset.CopyFrom(value.proto)

        self._laneStartOffset = value
        self._laneStartOffset._update_proto_references(self.proto.laneStartOffset)

    @property
    def applyRollingStopToEgo(self) -> bool:
        return self.proto.applyRollingStopToEgo

    @applyRollingStopToEgo.setter
    def applyRollingStopToEgo(self, value: bool):
        self.proto.applyRollingStopToEgo = value

    @property
    def applyStopLineOffsetToEgo(self) -> bool:
        return self.proto.applyStopLineOffsetToEgo

    @applyStopLineOffsetToEgo.setter
    def applyStopLineOffsetToEgo(self, value: bool):
        self.proto.applyStopLineOffsetToEgo = value

    @property
    def applyProceedOutOfTurnProbabilityToEgo(self) -> bool:
        return self.proto.applyProceedOutOfTurnProbabilityToEgo

    @applyProceedOutOfTurnProbabilityToEgo.setter
    def applyProceedOutOfTurnProbabilityToEgo(self, value: bool):
        self.proto.applyProceedOutOfTurnProbabilityToEgo = value

    @property
    def signDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._signDensity

    @signDensity.setter
    def signDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.signDensity.CopyFrom(value.proto)

        self._signDensity = value
        self._signDensity._update_proto_references(self.proto.signDensity)

    @property
    def crosswalkSignDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._crosswalkSignDensity

    @crosswalkSignDensity.setter
    def crosswalkSignDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.crosswalkSignDensity.CopyFrom(value.proto)

        self._crosswalkSignDensity = value
        self._crosswalkSignDensity._update_proto_references(self.proto.crosswalkSignDensity)

    @property
    def egoIgnoreObstacleTypes(self) -> List[str]:
        return self._egoIgnoreObstacleTypes

    @egoIgnoreObstacleTypes.setter
    def egoIgnoreObstacleTypes(self, value: List[str]):
        self._egoIgnoreObstacleTypes.clear()
        for v in value:
            self._egoIgnoreObstacleTypes.append(v)

    @property
    def markerDataMap(self) -> Dict[str, _pd_unified_generator_pb2.RoadMarkingData]:
        return self._markerDataMap

    @markerDataMap.setter
    def markerDataMap(self, value: Dict[str, _pd_unified_generator_pb2.RoadMarkingData]):
        self._markerDataMap.clear()
        self._markerDataMap.update(value)

    @property
    def randomizeVehicleParts(self) -> bool:
        return self.proto.randomizeVehicleParts

    @randomizeVehicleParts.setter
    def randomizeVehicleParts(self, value: bool):
        self.proto.randomizeVehicleParts = value

    @property
    def instanceParallelParkingSpaces(self) -> bool:
        return self.proto.instanceParallelParkingSpaces

    @instanceParallelParkingSpaces.setter
    def instanceParallelParkingSpaces(self, value: bool):
        self.proto.instanceParallelParkingSpaces = value

    @property
    def instanceParallelParkingMarkers(self) -> bool:
        return self.proto.instanceParallelParkingMarkers

    @instanceParallelParkingMarkers.setter
    def instanceParallelParkingMarkers(self, value: bool):
        self.proto.instanceParallelParkingMarkers = value

    @property
    def region(self) -> str:
        return self.proto.region

    @region.setter
    def region(self, value: str):
        self.proto.region = value

    @property
    def spawnTrailerProbabilities(self) -> Dict[str, float]:
        return self._spawnTrailerProbabilities

    @spawnTrailerProbabilities.setter
    def spawnTrailerProbabilities(self, value: Dict[str, float]):
        self._spawnTrailerProbabilities.clear()
        self._spawnTrailerProbabilities.update(value)

    @property
    def spawnTrailerOnEgoProbability(self) -> float:
        return self.proto.spawnTrailerOnEgoProbability

    @spawnTrailerOnEgoProbability.setter
    def spawnTrailerOnEgoProbability(self, value: float):
        self.proto.spawnTrailerOnEgoProbability = value

    @property
    def minNumberOfPedestrians(self) -> int:
        return self.proto.minNumberOfPedestrians

    @minNumberOfPedestrians.setter
    def minNumberOfPedestrians(self, value: int):
        self.proto.minNumberOfPedestrians = value

    @property
    def pedestriansSpawnInParkingLot(self) -> bool:
        return self.proto.pedestriansSpawnInParkingLot

    @pedestriansSpawnInParkingLot.setter
    def pedestriansSpawnInParkingLot(self, value: bool):
        self.proto.pedestriansSpawnInParkingLot = value

    @property
    def lightFlashingPeriod(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._lightFlashingPeriod

    @lightFlashingPeriod.setter
    def lightFlashingPeriod(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.lightFlashingPeriod.CopyFrom(value.proto)

        self._lightFlashingPeriod = value
        self._lightFlashingPeriod._update_proto_references(self.proto.lightFlashingPeriod)

    @property
    def lightIlluminatedPercentage(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._lightIlluminatedPercentage

    @lightIlluminatedPercentage.setter
    def lightIlluminatedPercentage(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.lightIlluminatedPercentage.CopyFrom(value.proto)

        self._lightIlluminatedPercentage = value
        self._lightIlluminatedPercentage._update_proto_references(self.proto.lightIlluminatedPercentage)

    @property
    def pedestriansDynamicPathing(self) -> bool:
        return self.proto.pedestriansDynamicPathing

    @pedestriansDynamicPathing.setter
    def pedestriansDynamicPathing(self, value: bool):
        self.proto.pedestriansDynamicPathing = value

    @property
    def useStaticTrailers(self) -> bool:
        return self.proto.useStaticTrailers

    @useStaticTrailers.setter
    def useStaticTrailers(self, value: bool):
        self.proto.useStaticTrailers = value

    @property
    def minNumberOfAnimals(self) -> int:
        return self.proto.minNumberOfAnimals

    @minNumberOfAnimals.setter
    def minNumberOfAnimals(self, value: int):
        self.proto.minNumberOfAnimals = value

    @property
    def animalSpeciesAllowed(self) -> str:
        return self.proto.animalSpeciesAllowed

    @animalSpeciesAllowed.setter
    def animalSpeciesAllowed(self, value: str):
        self.proto.animalSpeciesAllowed = value

    @property
    def restrictLargeVehicleLaneCurvature(self) -> bool:
        return self.proto.restrictLargeVehicleLaneCurvature

    @restrictLargeVehicleLaneCurvature.setter
    def restrictLargeVehicleLaneCurvature(self, value: bool):
        self.proto.restrictLargeVehicleLaneCurvature = value

    @property
    def largeVehicleTurnRadiusMultiple(self) -> float:
        return self.proto.largeVehicleTurnRadiusMultiple

    @largeVehicleTurnRadiusMultiple.setter
    def largeVehicleTurnRadiusMultiple(self, value: float):
        self.proto.largeVehicleTurnRadiusMultiple = value

    @property
    def parking_space_data(self) -> _pd_unified_generator_pb2.ParkingSpaceData:
        return self._parking_space_data

    @parking_space_data.setter
    def parking_space_data(self, value: _pd_unified_generator_pb2.ParkingSpaceData):
        self.proto.parking_space_data.CopyFrom(value.proto)

        self._parking_space_data = value
        self._parking_space_data._update_proto_references(self.proto.parking_space_data)

    @property
    def object_decoration_params(self) -> _pd_unified_generator_pb2.ObjectDecorationParams:
        return self._object_decoration_params

    @object_decoration_params.setter
    def object_decoration_params(self, value: _pd_unified_generator_pb2.ObjectDecorationParams):
        self.proto.object_decoration_params.CopyFrom(value.proto)

        self._object_decoration_params = value
        self._object_decoration_params._update_proto_references(self.proto.object_decoration_params)

    @property
    def object_decoration_radius(self) -> float:
        return self.proto.object_decoration_radius

    @object_decoration_radius.setter
    def object_decoration_radius(self, value: float):
        self.proto.object_decoration_radius = value

    @property
    def ego_parking_space_decoration_params(self) -> _pd_unified_generator_pb2.ObjectDecorationParams:
        return self._ego_parking_space_decoration_params

    @ego_parking_space_decoration_params.setter
    def ego_parking_space_decoration_params(self, value: _pd_unified_generator_pb2.ObjectDecorationParams):
        self.proto.ego_parking_space_decoration_params.CopyFrom(value.proto)

        self._ego_parking_space_decoration_params = value
        self._ego_parking_space_decoration_params._update_proto_references(
            self.proto.ego_parking_space_decoration_params
        )

    def _update_proto_references(self, proto: pd_spawn_pb2.SpawnConfigPreset):
        self.proto = proto
        self._random_generator._update_proto_references(proto.random_generator)
        self._junction_generator._update_proto_references(proto.junction_generator)
        self._voi_generator._update_proto_references(proto.voi_generator)
        self._kitti_generator._update_proto_references(proto.kitti_generator)
        self._position_generator._update_proto_references(proto.position_generator)
        self._parkingTypeDistribution._update_proto_references(proto.parkingTypeDistribution)
        for k, v in self.vehicleDistribution.items():
            v._update_proto_references(self.proto.vehicleDistribution[k])
        self._rollingStop._update_proto_references(proto.rollingStop)
        self._stopLineOffset._update_proto_references(proto.stopLineOffset)
        for i, v in enumerate(self.agentStateProbabilities):
            v._update_proto_references(self.proto.agentStateProbabilities[i])
        self._turnTypeDistribution._update_proto_references(proto.turnTypeDistribution)
        for k, v in self.startSeparationTime.items():
            v._update_proto_references(self.proto.startSeparationTime[k])
        for k, v in self.targetSeparationTime.items():
            v._update_proto_references(self.proto.targetSeparationTime[k])
        self._egoMinLaneCountDist._update_proto_references(proto.egoMinLaneCountDist)
        self._laneStartOffset._update_proto_references(proto.laneStartOffset)
        self._signDensity._update_proto_references(proto.signDensity)
        self._crosswalkSignDensity._update_proto_references(proto.crosswalkSignDensity)
        for k, v in self.markerDataMap.items():
            v._update_proto_references(self.proto.markerDataMap[k])
        self._lightFlashingPeriod._update_proto_references(proto.lightFlashingPeriod)
        self._lightIlluminatedPercentage._update_proto_references(proto.lightIlluminatedPercentage)
        self._parking_space_data._update_proto_references(proto.parking_space_data)
        self._object_decoration_params._update_proto_references(proto.object_decoration_params)
        self._ego_parking_space_decoration_params._update_proto_references(proto.ego_parking_space_decoration_params)


@register_wrapper(proto_type=pd_spawn_pb2.SpawnConfig)
class SpawnConfig(ProtoMessageClass):
    """
    Args:
        preset_distribution: :attr:`preset_distribution`
        presets: :attr:`presets`
    Attributes:
        preset_distribution:
        presets:"""

    _proto_message = pd_spawn_pb2.SpawnConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.SpawnConfig] = None,
        preset_distribution: _pd_distributions_pb2.CategoricalDistribution = None,
        presets: List[SpawnConfigPreset] = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.SpawnConfig()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(
            proto=proto.preset_distribution
        )
        self._presets = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets],
            attr_name="presets",
            list_owner=self,
        )
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution
        if presets is not None:
            self.presets = presets

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.preset_distribution.CopyFrom(value.proto)

        self._preset_distribution = value
        self._preset_distribution._update_proto_references(self.proto.preset_distribution)

    @property
    def presets(self) -> List[SpawnConfigPreset]:
        return self._presets

    @presets.setter
    def presets(self, value: List[SpawnConfigPreset]):
        self._presets.clear()
        for v in value:
            self._presets.append(v)

    def _update_proto_references(self, proto: pd_spawn_pb2.SpawnConfig):
        self.proto = proto
        self._preset_distribution._update_proto_references(proto.preset_distribution)
        for i, v in enumerate(self.presets):
            v._update_proto_references(self.proto.presets[i])


@register_wrapper(proto_type=pd_spawn_pb2.RandomLaneScenarioGeneratorInfo)
class RandomLaneScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
    Attributes:"""

    _proto_message = pd_spawn_pb2.RandomLaneScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.RandomLaneScenarioGeneratorInfo] = None):
        if proto is None:
            proto = pd_spawn_pb2.RandomLaneScenarioGeneratorInfo()
        self.proto = proto

    def _update_proto_references(self, proto: pd_spawn_pb2.RandomLaneScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.JunctionScenarioGeneratorInfo)
class JunctionScenarioGeneratorInfo(ProtoMessageClass):
    """Generate scenarios that around junctions

    Args:
        min_distance_to_junction: :attr:`min_distance_to_junction`
        max_distance_to_junction: :attr:`max_distance_to_junction`
        signal_light_distribution: :attr:`signal_light_distribution`
        turn_type_distribution: :attr:`turn_type_distribution`
        junction_id: :attr:`junction_id`
        junction_ids: :attr:`junction_ids`
        crowd_density: :attr:`crowd_density`
        force_cross_traffic: :attr:`force_cross_traffic`
        control_type_distribution: :attr:`control_type_distribution`
        geometry_type_distribution: :attr:`geometry_type_distribution`
        road_type_distribution: :attr:`road_type_distribution`
        allow_crossing_peds: :attr:`allow_crossing_peds`
        enable_vehicle_occlusions: :attr:`enable_vehicle_occlusions`
        enable_prop_occlusions: :attr:`enable_prop_occlusions`
        prop_occlusion_spacing_dist: :attr:`prop_occlusion_spacing_dist`
        prop_occlusion_count_dist: :attr:`prop_occlusion_count_dist`
        occlusion_offset_dist: :attr:`occlusion_offset_dist`
        use_cross_road_speed_limit: :attr:`use_cross_road_speed_limit`
        cross_road_speed_limit_mps: :attr:`cross_road_speed_limit_mps`
        use_only_cross_roads_with_straight_turn_type: :attr:`use_only_cross_roads_with_straight_turn_type`
        ego_stopped_at_junction: :attr:`ego_stopped_at_junction`
        cone_placement_freq: :attr:`cone_placement_freq`
        cone_placement_max_dist: :attr:`cone_placement_max_dist`
    Attributes:
        min_distance_to_junction: Default: 2.0
        max_distance_to_junction: Default: 10.0
        signal_light_distribution:
        turn_type_distribution:
        junction_id:
        junction_ids:
        crowd_density: Default: 0.5
        force_cross_traffic: Default: False
        control_type_distribution:
        geometry_type_distribution:
        road_type_distribution:
        allow_crossing_peds:
        enable_vehicle_occlusions: Default: False
        enable_prop_occlusions: Default: False
        prop_occlusion_spacing_dist:
        prop_occlusion_count_dist:
        occlusion_offset_dist:
        use_cross_road_speed_limit: Default: False
        cross_road_speed_limit_mps:
        use_only_cross_roads_with_straight_turn_type: Default: False
        ego_stopped_at_junction: Default: False
        cone_placement_freq: Default: 0.0
        cone_placement_max_dist: Default: 200.0"""

    _proto_message = pd_spawn_pb2.JunctionScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.JunctionScenarioGeneratorInfo] = None,
        min_distance_to_junction: float = None,
        max_distance_to_junction: float = None,
        signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution = None,
        turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution = None,
        junction_id: int = None,
        junction_ids: List[int] = None,
        crowd_density: float = None,
        force_cross_traffic: bool = None,
        control_type_distribution: _pd_distributions_pb2.EnumDistribution = None,
        geometry_type_distribution: _pd_distributions_pb2.EnumDistribution = None,
        road_type_distribution: _pd_distributions_pb2.EnumDistribution = None,
        allow_crossing_peds: bool = None,
        enable_vehicle_occlusions: bool = None,
        enable_prop_occlusions: bool = None,
        prop_occlusion_spacing_dist: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        prop_occlusion_count_dist: _pd_unified_generator_pb2.CenterSpreadConfigInt = None,
        occlusion_offset_dist: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        use_cross_road_speed_limit: bool = None,
        cross_road_speed_limit_mps: _pd_unified_generator_pb2.MinMaxConfigFloat = None,
        use_only_cross_roads_with_straight_turn_type: bool = None,
        ego_stopped_at_junction: bool = None,
        cone_placement_freq: float = None,
        cone_placement_max_dist: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.JunctionScenarioGeneratorInfo()
        self.proto = proto
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(
            proto=proto.signal_light_distribution
        )
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(
            proto=proto.turn_type_distribution
        )
        self._control_type_distribution = get_wrapper(proto_type=proto.control_type_distribution.__class__)(
            proto=proto.control_type_distribution
        )
        self._geometry_type_distribution = get_wrapper(proto_type=proto.geometry_type_distribution.__class__)(
            proto=proto.geometry_type_distribution
        )
        self._road_type_distribution = get_wrapper(proto_type=proto.road_type_distribution.__class__)(
            proto=proto.road_type_distribution
        )
        self._prop_occlusion_spacing_dist = get_wrapper(proto_type=proto.prop_occlusion_spacing_dist.__class__)(
            proto=proto.prop_occlusion_spacing_dist
        )
        self._prop_occlusion_count_dist = get_wrapper(proto_type=proto.prop_occlusion_count_dist.__class__)(
            proto=proto.prop_occlusion_count_dist
        )
        self._occlusion_offset_dist = get_wrapper(proto_type=proto.occlusion_offset_dist.__class__)(
            proto=proto.occlusion_offset_dist
        )
        self._cross_road_speed_limit_mps = get_wrapper(proto_type=proto.cross_road_speed_limit_mps.__class__)(
            proto=proto.cross_road_speed_limit_mps
        )
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution
        if junction_id is not None:
            self.junction_id = junction_id
        self._junction_ids = ProtoListWrapper(
            container=[int(v) for v in proto.junction_ids], attr_name="junction_ids", list_owner=self
        )
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if crowd_density is not None:
            self.crowd_density = crowd_density
        if force_cross_traffic is not None:
            self.force_cross_traffic = force_cross_traffic
        if control_type_distribution is not None:
            self.control_type_distribution = control_type_distribution
        if geometry_type_distribution is not None:
            self.geometry_type_distribution = geometry_type_distribution
        if road_type_distribution is not None:
            self.road_type_distribution = road_type_distribution
        if allow_crossing_peds is not None:
            self.allow_crossing_peds = allow_crossing_peds
        if enable_vehicle_occlusions is not None:
            self.enable_vehicle_occlusions = enable_vehicle_occlusions
        if enable_prop_occlusions is not None:
            self.enable_prop_occlusions = enable_prop_occlusions
        if prop_occlusion_spacing_dist is not None:
            self.prop_occlusion_spacing_dist = prop_occlusion_spacing_dist
        if prop_occlusion_count_dist is not None:
            self.prop_occlusion_count_dist = prop_occlusion_count_dist
        if occlusion_offset_dist is not None:
            self.occlusion_offset_dist = occlusion_offset_dist
        if use_cross_road_speed_limit is not None:
            self.use_cross_road_speed_limit = use_cross_road_speed_limit
        if cross_road_speed_limit_mps is not None:
            self.cross_road_speed_limit_mps = cross_road_speed_limit_mps
        if use_only_cross_roads_with_straight_turn_type is not None:
            self.use_only_cross_roads_with_straight_turn_type = use_only_cross_roads_with_straight_turn_type
        if ego_stopped_at_junction is not None:
            self.ego_stopped_at_junction = ego_stopped_at_junction
        if cone_placement_freq is not None:
            self.cone_placement_freq = cone_placement_freq
        if cone_placement_max_dist is not None:
            self.cone_placement_max_dist = cone_placement_max_dist

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self.proto.signal_light_distribution.CopyFrom(value.proto)

        self._signal_light_distribution = value
        self._signal_light_distribution._update_proto_references(self.proto.signal_light_distribution)

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self.proto.turn_type_distribution.CopyFrom(value.proto)

        self._turn_type_distribution = value
        self._turn_type_distribution._update_proto_references(self.proto.turn_type_distribution)

    @property
    def junction_id(self) -> int:
        return self.proto.junction_id

    @junction_id.setter
    def junction_id(self, value: int):
        self.proto.junction_id = value

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

    @property
    def crowd_density(self) -> float:
        return self.proto.crowd_density

    @crowd_density.setter
    def crowd_density(self, value: float):
        self.proto.crowd_density = value

    @property
    def force_cross_traffic(self) -> bool:
        return self.proto.force_cross_traffic

    @force_cross_traffic.setter
    def force_cross_traffic(self, value: bool):
        self.proto.force_cross_traffic = value

    @property
    def control_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._control_type_distribution

    @control_type_distribution.setter
    def control_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.control_type_distribution.CopyFrom(value.proto)

        self._control_type_distribution = value
        self._control_type_distribution._update_proto_references(self.proto.control_type_distribution)

    @property
    def geometry_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._geometry_type_distribution

    @geometry_type_distribution.setter
    def geometry_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.geometry_type_distribution.CopyFrom(value.proto)

        self._geometry_type_distribution = value
        self._geometry_type_distribution._update_proto_references(self.proto.geometry_type_distribution)

    @property
    def road_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._road_type_distribution

    @road_type_distribution.setter
    def road_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.road_type_distribution.CopyFrom(value.proto)

        self._road_type_distribution = value
        self._road_type_distribution._update_proto_references(self.proto.road_type_distribution)

    @property
    def allow_crossing_peds(self) -> bool:
        return self.proto.allow_crossing_peds

    @allow_crossing_peds.setter
    def allow_crossing_peds(self, value: bool):
        self.proto.allow_crossing_peds = value

    @property
    def enable_vehicle_occlusions(self) -> bool:
        return self.proto.enable_vehicle_occlusions

    @enable_vehicle_occlusions.setter
    def enable_vehicle_occlusions(self, value: bool):
        self.proto.enable_vehicle_occlusions = value

    @property
    def enable_prop_occlusions(self) -> bool:
        return self.proto.enable_prop_occlusions

    @enable_prop_occlusions.setter
    def enable_prop_occlusions(self, value: bool):
        self.proto.enable_prop_occlusions = value

    @property
    def prop_occlusion_spacing_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._prop_occlusion_spacing_dist

    @prop_occlusion_spacing_dist.setter
    def prop_occlusion_spacing_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.prop_occlusion_spacing_dist.CopyFrom(value.proto)

        self._prop_occlusion_spacing_dist = value
        self._prop_occlusion_spacing_dist._update_proto_references(self.proto.prop_occlusion_spacing_dist)

    @property
    def prop_occlusion_count_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._prop_occlusion_count_dist

    @prop_occlusion_count_dist.setter
    def prop_occlusion_count_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self.proto.prop_occlusion_count_dist.CopyFrom(value.proto)

        self._prop_occlusion_count_dist = value
        self._prop_occlusion_count_dist._update_proto_references(self.proto.prop_occlusion_count_dist)

    @property
    def occlusion_offset_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._occlusion_offset_dist

    @occlusion_offset_dist.setter
    def occlusion_offset_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.occlusion_offset_dist.CopyFrom(value.proto)

        self._occlusion_offset_dist = value
        self._occlusion_offset_dist._update_proto_references(self.proto.occlusion_offset_dist)

    @property
    def use_cross_road_speed_limit(self) -> bool:
        return self.proto.use_cross_road_speed_limit

    @use_cross_road_speed_limit.setter
    def use_cross_road_speed_limit(self, value: bool):
        self.proto.use_cross_road_speed_limit = value

    @property
    def cross_road_speed_limit_mps(self) -> _pd_unified_generator_pb2.MinMaxConfigFloat:
        return self._cross_road_speed_limit_mps

    @cross_road_speed_limit_mps.setter
    def cross_road_speed_limit_mps(self, value: _pd_unified_generator_pb2.MinMaxConfigFloat):
        self.proto.cross_road_speed_limit_mps.CopyFrom(value.proto)

        self._cross_road_speed_limit_mps = value
        self._cross_road_speed_limit_mps._update_proto_references(self.proto.cross_road_speed_limit_mps)

    @property
    def use_only_cross_roads_with_straight_turn_type(self) -> bool:
        return self.proto.use_only_cross_roads_with_straight_turn_type

    @use_only_cross_roads_with_straight_turn_type.setter
    def use_only_cross_roads_with_straight_turn_type(self, value: bool):
        self.proto.use_only_cross_roads_with_straight_turn_type = value

    @property
    def ego_stopped_at_junction(self) -> bool:
        return self.proto.ego_stopped_at_junction

    @ego_stopped_at_junction.setter
    def ego_stopped_at_junction(self, value: bool):
        self.proto.ego_stopped_at_junction = value

    @property
    def cone_placement_freq(self) -> float:
        return self.proto.cone_placement_freq

    @cone_placement_freq.setter
    def cone_placement_freq(self, value: float):
        self.proto.cone_placement_freq = value

    @property
    def cone_placement_max_dist(self) -> float:
        return self.proto.cone_placement_max_dist

    @cone_placement_max_dist.setter
    def cone_placement_max_dist(self, value: float):
        self.proto.cone_placement_max_dist = value

    def _update_proto_references(self, proto: pd_spawn_pb2.JunctionScenarioGeneratorInfo):
        self.proto = proto
        self._signal_light_distribution._update_proto_references(proto.signal_light_distribution)
        self._turn_type_distribution._update_proto_references(proto.turn_type_distribution)
        self._control_type_distribution._update_proto_references(proto.control_type_distribution)
        self._geometry_type_distribution._update_proto_references(proto.geometry_type_distribution)
        self._road_type_distribution._update_proto_references(proto.road_type_distribution)
        self._prop_occlusion_spacing_dist._update_proto_references(proto.prop_occlusion_spacing_dist)
        self._prop_occlusion_count_dist._update_proto_references(proto.prop_occlusion_count_dist)
        self._occlusion_offset_dist._update_proto_references(proto.occlusion_offset_dist)
        self._cross_road_speed_limit_mps._update_proto_references(proto.cross_road_speed_limit_mps)


@register_wrapper(proto_type=pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo)
class VehicleOfInterestScenarioGeneratorInfo(ProtoMessageClass):
    """Generate scenarios in which vehicle model names are sampled and spawned around the ego vehicle

    Args:
        vehicle_list: :attr:`vehicle_list`
        max_distance_front: :attr:`max_distance_front`
        max_distance_back: :attr:`max_distance_back`
        min_number_of_vehicles: :attr:`min_number_of_vehicles`
        max_number_of_vehicles: :attr:`max_number_of_vehicles`
        include_opposite_lanes: :attr:`include_opposite_lanes`
    Attributes:
        vehicle_list: A list of vehicle model names which are samples and spawned around the ego vehicle
        max_distance_front: Maximum distance of a special vehicle in front of the ego vehicle
            Default: 50.0
        max_distance_back: Maximum distance of a special vehicle behind the ego vehicle
            Default: 50.0
        min_number_of_vehicles: Minimum number of vehicles that are placed per scenario
            Default: 1
        max_number_of_vehicles: Maximum number of vehicles that are placed per scenario
            Default: 4
        include_opposite_lanes: Spawn vehicles on opposite lanes if available
            Default: True"""

    _proto_message = pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo] = None,
        vehicle_list: List[str] = None,
        max_distance_front: float = None,
        max_distance_back: float = None,
        min_number_of_vehicles: int = None,
        max_number_of_vehicles: int = None,
        include_opposite_lanes: bool = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo()
        self.proto = proto
        self._vehicle_list = ProtoListWrapper(
            container=[str(v) for v in proto.vehicle_list], attr_name="vehicle_list", list_owner=self
        )
        if vehicle_list is not None:
            self.vehicle_list = vehicle_list
        if max_distance_front is not None:
            self.max_distance_front = max_distance_front
        if max_distance_back is not None:
            self.max_distance_back = max_distance_back
        if min_number_of_vehicles is not None:
            self.min_number_of_vehicles = min_number_of_vehicles
        if max_number_of_vehicles is not None:
            self.max_number_of_vehicles = max_number_of_vehicles
        if include_opposite_lanes is not None:
            self.include_opposite_lanes = include_opposite_lanes

    @property
    def vehicle_list(self) -> List[str]:
        return self._vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, value: List[str]):
        self._vehicle_list.clear()
        for v in value:
            self._vehicle_list.append(v)

    @property
    def max_distance_front(self) -> float:
        return self.proto.max_distance_front

    @max_distance_front.setter
    def max_distance_front(self, value: float):
        self.proto.max_distance_front = value

    @property
    def max_distance_back(self) -> float:
        return self.proto.max_distance_back

    @max_distance_back.setter
    def max_distance_back(self, value: float):
        self.proto.max_distance_back = value

    @property
    def min_number_of_vehicles(self) -> int:
        return self.proto.min_number_of_vehicles

    @min_number_of_vehicles.setter
    def min_number_of_vehicles(self, value: int):
        self.proto.min_number_of_vehicles = value

    @property
    def max_number_of_vehicles(self) -> int:
        return self.proto.max_number_of_vehicles

    @max_number_of_vehicles.setter
    def max_number_of_vehicles(self, value: int):
        self.proto.max_number_of_vehicles = value

    @property
    def include_opposite_lanes(self) -> bool:
        return self.proto.include_opposite_lanes

    @include_opposite_lanes.setter
    def include_opposite_lanes(self, value: bool):
        self.proto.include_opposite_lanes = value

    def _update_proto_references(self, proto: pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.KittiScenarioGeneratorInfo)
class KittiScenarioGeneratorInfo(ProtoMessageClass):
    """Generate kitti-like scenarios

    Args:
        min_distance_to_junction: :attr:`min_distance_to_junction`
        max_distance_to_junction: :attr:`max_distance_to_junction`
        turn_type_distribution: :attr:`turn_type_distribution`
    Attributes:
        min_distance_to_junction: Default: 2.0
        max_distance_to_junction: Default: 10.0
        turn_type_distribution:"""

    _proto_message = pd_spawn_pb2.KittiScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.KittiScenarioGeneratorInfo] = None,
        min_distance_to_junction: float = None,
        max_distance_to_junction: float = None,
        turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.KittiScenarioGeneratorInfo()
        self.proto = proto
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(
            proto=proto.turn_type_distribution
        )
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self.proto.turn_type_distribution.CopyFrom(value.proto)

        self._turn_type_distribution = value
        self._turn_type_distribution._update_proto_references(self.proto.turn_type_distribution)

    def _update_proto_references(self, proto: pd_spawn_pb2.KittiScenarioGeneratorInfo):
        self.proto = proto
        self._turn_type_distribution._update_proto_references(proto.turn_type_distribution)


@register_wrapper(proto_type=pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo)
class VehiclePositionScenarioGeneratorInfo(ProtoMessageClass):
    """Generate scenarios with vehicle placement requirements

    Args:
        radius_to_star_min: :attr:`radius_to_star_min`
        radius_to_star_max: :attr:`radius_to_star_max`
        star_vehicles: :attr:`star_vehicles`
        junction_ids: :attr:`junction_ids`
        face_same_direction: :attr:`face_same_direction`
        ego_behind_star: :attr:`ego_behind_star`
        place_on_shoulder: :attr:`place_on_shoulder`
        peds_around_star_vehicle: :attr:`peds_around_star_vehicle`
        num_stars_in_scene_min: :attr:`num_stars_in_scene_min`
        num_stars_in_scene_max: :attr:`num_stars_in_scene_max`
        star_on_same_road: :attr:`star_on_same_road`
        ego_in_star_adjacent_lane: :attr:`ego_in_star_adjacent_lane`
        star_vehicle_peds_min_distance: :attr:`star_vehicle_peds_min_distance`
        star_vehicle_peds_max_distance: :attr:`star_vehicle_peds_max_distance`
        star_vehicle_peds_social_distancing: :attr:`star_vehicle_peds_social_distancing`
        star_vehicle_peds_place_between_ego_and_star: :attr:`star_vehicle_peds_place_between_ego_and_star`
        star_vehicle_peds_max_distance_from_driveable_lane: :attr:`star_vehicle_peds_max_distance_from_driveable_lane`
        shoulder_peds_max_distance_from_ref: :attr:`shoulder_peds_max_distance_from_ref`
        min_peds_per_star: :attr:`min_peds_per_star`
        max_peds_per_star: :attr:`max_peds_per_star`
        min_peds_no_stars: :attr:`min_peds_no_stars`
        max_peds_no_stars: :attr:`max_peds_no_stars`
        max_attempts_to_place_each_ped: :attr:`max_attempts_to_place_each_ped`
        max_attempts_to_place_each_star: :attr:`max_attempts_to_place_each_star`
        max_lane_recursions_to_check_ego_adjacency: :attr:`max_lane_recursions_to_check_ego_adjacency`
        scenario_fov_cull_limit: :attr:`scenario_fov_cull_limit`
        scenario_los_cull: :attr:`scenario_los_cull`
        reduce_spawn_to_zero_at_star_range: :attr:`reduce_spawn_to_zero_at_star_range`
        ped_pose_distribution: :attr:`ped_pose_distribution`
        emergency_vehicle_spawn_behind_star_probability: :attr:`emergency_vehicle_spawn_behind_star_probability`
        emergency_vehicle_distance_behind_star: :attr:`emergency_vehicle_distance_behind_star`
        min_emergency_vehicles_per_star: :attr:`min_emergency_vehicles_per_star`
        max_emergency_vehicles_per_star: :attr:`max_emergency_vehicles_per_star`
        emergency_vehicle_asset_tag: :attr:`emergency_vehicle_asset_tag`
        emergency_vehicle_country_tag: :attr:`emergency_vehicle_country_tag`
    Attributes:
        radius_to_star_min: Default: 10.0
        radius_to_star_max: Default: 50.0
        star_vehicles:
        junction_ids:
        face_same_direction: Default: False
        ego_behind_star: Default: False
        place_on_shoulder: Default: False
        peds_around_star_vehicle: Default: False
        num_stars_in_scene_min: Default: 1
        num_stars_in_scene_max: Default: 1
        star_on_same_road: Default: False
        ego_in_star_adjacent_lane: Default: False
        star_vehicle_peds_min_distance: Default: 2.0
        star_vehicle_peds_max_distance: Default: 5.0
        star_vehicle_peds_social_distancing: Default: 2.0
        star_vehicle_peds_place_between_ego_and_star: Default: True
        star_vehicle_peds_max_distance_from_driveable_lane: Default: 2.5
        shoulder_peds_max_distance_from_ref: Default: 4.0
        min_peds_per_star: Default: 1
        max_peds_per_star: Default: 2
        min_peds_no_stars: Default: 1
        max_peds_no_stars: Default: 5
        max_attempts_to_place_each_ped: Default: 100
        max_attempts_to_place_each_star: Default: 10
        max_lane_recursions_to_check_ego_adjacency: Default: 30
        scenario_fov_cull_limit: Default: 0.0
        scenario_los_cull: Default: True
        reduce_spawn_to_zero_at_star_range: Default: 500.0
        ped_pose_distribution:
        emergency_vehicle_spawn_behind_star_probability:
        emergency_vehicle_distance_behind_star: Default: 5.0
        min_emergency_vehicles_per_star: Default: 0
        max_emergency_vehicles_per_star: Default: 3
        emergency_vehicle_asset_tag: Default: police_vehicle,fire_truck,ambulance
        emergency_vehicle_country_tag:"""

    _proto_message = pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo] = None,
        radius_to_star_min: float = None,
        radius_to_star_max: float = None,
        star_vehicles: List[str] = None,
        junction_ids: List[int] = None,
        face_same_direction: bool = None,
        ego_behind_star: bool = None,
        place_on_shoulder: bool = None,
        peds_around_star_vehicle: bool = None,
        num_stars_in_scene_min: int = None,
        num_stars_in_scene_max: int = None,
        star_on_same_road: bool = None,
        ego_in_star_adjacent_lane: bool = None,
        star_vehicle_peds_min_distance: float = None,
        star_vehicle_peds_max_distance: float = None,
        star_vehicle_peds_social_distancing: float = None,
        star_vehicle_peds_place_between_ego_and_star: bool = None,
        star_vehicle_peds_max_distance_from_driveable_lane: float = None,
        shoulder_peds_max_distance_from_ref: float = None,
        min_peds_per_star: int = None,
        max_peds_per_star: int = None,
        min_peds_no_stars: int = None,
        max_peds_no_stars: int = None,
        max_attempts_to_place_each_ped: int = None,
        max_attempts_to_place_each_star: int = None,
        max_lane_recursions_to_check_ego_adjacency: int = None,
        scenario_fov_cull_limit: float = None,
        scenario_los_cull: bool = None,
        reduce_spawn_to_zero_at_star_range: float = None,
        ped_pose_distribution: _pd_distributions_pb2.CategoricalDistribution = None,
        emergency_vehicle_spawn_behind_star_probability: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        emergency_vehicle_distance_behind_star: float = None,
        min_emergency_vehicles_per_star: int = None,
        max_emergency_vehicles_per_star: int = None,
        emergency_vehicle_asset_tag: str = None,
        emergency_vehicle_country_tag: str = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo()
        self.proto = proto
        self._ped_pose_distribution = get_wrapper(proto_type=proto.ped_pose_distribution.__class__)(
            proto=proto.ped_pose_distribution
        )
        self._emergency_vehicle_spawn_behind_star_probability = get_wrapper(
            proto_type=proto.emergency_vehicle_spawn_behind_star_probability.__class__
        )(proto=proto.emergency_vehicle_spawn_behind_star_probability)
        if radius_to_star_min is not None:
            self.radius_to_star_min = radius_to_star_min
        if radius_to_star_max is not None:
            self.radius_to_star_max = radius_to_star_max
        self._star_vehicles = ProtoListWrapper(
            container=[str(v) for v in proto.star_vehicles], attr_name="star_vehicles", list_owner=self
        )
        if star_vehicles is not None:
            self.star_vehicles = star_vehicles
        self._junction_ids = ProtoListWrapper(
            container=[int(v) for v in proto.junction_ids], attr_name="junction_ids", list_owner=self
        )
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if face_same_direction is not None:
            self.face_same_direction = face_same_direction
        if ego_behind_star is not None:
            self.ego_behind_star = ego_behind_star
        if place_on_shoulder is not None:
            self.place_on_shoulder = place_on_shoulder
        if peds_around_star_vehicle is not None:
            self.peds_around_star_vehicle = peds_around_star_vehicle
        if num_stars_in_scene_min is not None:
            self.num_stars_in_scene_min = num_stars_in_scene_min
        if num_stars_in_scene_max is not None:
            self.num_stars_in_scene_max = num_stars_in_scene_max
        if star_on_same_road is not None:
            self.star_on_same_road = star_on_same_road
        if ego_in_star_adjacent_lane is not None:
            self.ego_in_star_adjacent_lane = ego_in_star_adjacent_lane
        if star_vehicle_peds_min_distance is not None:
            self.star_vehicle_peds_min_distance = star_vehicle_peds_min_distance
        if star_vehicle_peds_max_distance is not None:
            self.star_vehicle_peds_max_distance = star_vehicle_peds_max_distance
        if star_vehicle_peds_social_distancing is not None:
            self.star_vehicle_peds_social_distancing = star_vehicle_peds_social_distancing
        if star_vehicle_peds_place_between_ego_and_star is not None:
            self.star_vehicle_peds_place_between_ego_and_star = star_vehicle_peds_place_between_ego_and_star
        if star_vehicle_peds_max_distance_from_driveable_lane is not None:
            self.star_vehicle_peds_max_distance_from_driveable_lane = star_vehicle_peds_max_distance_from_driveable_lane
        if shoulder_peds_max_distance_from_ref is not None:
            self.shoulder_peds_max_distance_from_ref = shoulder_peds_max_distance_from_ref
        if min_peds_per_star is not None:
            self.min_peds_per_star = min_peds_per_star
        if max_peds_per_star is not None:
            self.max_peds_per_star = max_peds_per_star
        if min_peds_no_stars is not None:
            self.min_peds_no_stars = min_peds_no_stars
        if max_peds_no_stars is not None:
            self.max_peds_no_stars = max_peds_no_stars
        if max_attempts_to_place_each_ped is not None:
            self.max_attempts_to_place_each_ped = max_attempts_to_place_each_ped
        if max_attempts_to_place_each_star is not None:
            self.max_attempts_to_place_each_star = max_attempts_to_place_each_star
        if max_lane_recursions_to_check_ego_adjacency is not None:
            self.max_lane_recursions_to_check_ego_adjacency = max_lane_recursions_to_check_ego_adjacency
        if scenario_fov_cull_limit is not None:
            self.scenario_fov_cull_limit = scenario_fov_cull_limit
        if scenario_los_cull is not None:
            self.scenario_los_cull = scenario_los_cull
        if reduce_spawn_to_zero_at_star_range is not None:
            self.reduce_spawn_to_zero_at_star_range = reduce_spawn_to_zero_at_star_range
        if ped_pose_distribution is not None:
            self.ped_pose_distribution = ped_pose_distribution
        if emergency_vehicle_spawn_behind_star_probability is not None:
            self.emergency_vehicle_spawn_behind_star_probability = emergency_vehicle_spawn_behind_star_probability
        if emergency_vehicle_distance_behind_star is not None:
            self.emergency_vehicle_distance_behind_star = emergency_vehicle_distance_behind_star
        if min_emergency_vehicles_per_star is not None:
            self.min_emergency_vehicles_per_star = min_emergency_vehicles_per_star
        if max_emergency_vehicles_per_star is not None:
            self.max_emergency_vehicles_per_star = max_emergency_vehicles_per_star
        if emergency_vehicle_asset_tag is not None:
            self.emergency_vehicle_asset_tag = emergency_vehicle_asset_tag
        if emergency_vehicle_country_tag is not None:
            self.emergency_vehicle_country_tag = emergency_vehicle_country_tag

    @property
    def radius_to_star_min(self) -> float:
        return self.proto.radius_to_star_min

    @radius_to_star_min.setter
    def radius_to_star_min(self, value: float):
        self.proto.radius_to_star_min = value

    @property
    def radius_to_star_max(self) -> float:
        return self.proto.radius_to_star_max

    @radius_to_star_max.setter
    def radius_to_star_max(self, value: float):
        self.proto.radius_to_star_max = value

    @property
    def star_vehicles(self) -> List[str]:
        return self._star_vehicles

    @star_vehicles.setter
    def star_vehicles(self, value: List[str]):
        self._star_vehicles.clear()
        for v in value:
            self._star_vehicles.append(v)

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

    @property
    def face_same_direction(self) -> bool:
        return self.proto.face_same_direction

    @face_same_direction.setter
    def face_same_direction(self, value: bool):
        self.proto.face_same_direction = value

    @property
    def ego_behind_star(self) -> bool:
        return self.proto.ego_behind_star

    @ego_behind_star.setter
    def ego_behind_star(self, value: bool):
        self.proto.ego_behind_star = value

    @property
    def place_on_shoulder(self) -> bool:
        return self.proto.place_on_shoulder

    @place_on_shoulder.setter
    def place_on_shoulder(self, value: bool):
        self.proto.place_on_shoulder = value

    @property
    def peds_around_star_vehicle(self) -> bool:
        return self.proto.peds_around_star_vehicle

    @peds_around_star_vehicle.setter
    def peds_around_star_vehicle(self, value: bool):
        self.proto.peds_around_star_vehicle = value

    @property
    def num_stars_in_scene_min(self) -> int:
        return self.proto.num_stars_in_scene_min

    @num_stars_in_scene_min.setter
    def num_stars_in_scene_min(self, value: int):
        self.proto.num_stars_in_scene_min = value

    @property
    def num_stars_in_scene_max(self) -> int:
        return self.proto.num_stars_in_scene_max

    @num_stars_in_scene_max.setter
    def num_stars_in_scene_max(self, value: int):
        self.proto.num_stars_in_scene_max = value

    @property
    def star_on_same_road(self) -> bool:
        return self.proto.star_on_same_road

    @star_on_same_road.setter
    def star_on_same_road(self, value: bool):
        self.proto.star_on_same_road = value

    @property
    def ego_in_star_adjacent_lane(self) -> bool:
        return self.proto.ego_in_star_adjacent_lane

    @ego_in_star_adjacent_lane.setter
    def ego_in_star_adjacent_lane(self, value: bool):
        self.proto.ego_in_star_adjacent_lane = value

    @property
    def star_vehicle_peds_min_distance(self) -> float:
        return self.proto.star_vehicle_peds_min_distance

    @star_vehicle_peds_min_distance.setter
    def star_vehicle_peds_min_distance(self, value: float):
        self.proto.star_vehicle_peds_min_distance = value

    @property
    def star_vehicle_peds_max_distance(self) -> float:
        return self.proto.star_vehicle_peds_max_distance

    @star_vehicle_peds_max_distance.setter
    def star_vehicle_peds_max_distance(self, value: float):
        self.proto.star_vehicle_peds_max_distance = value

    @property
    def star_vehicle_peds_social_distancing(self) -> float:
        return self.proto.star_vehicle_peds_social_distancing

    @star_vehicle_peds_social_distancing.setter
    def star_vehicle_peds_social_distancing(self, value: float):
        self.proto.star_vehicle_peds_social_distancing = value

    @property
    def star_vehicle_peds_place_between_ego_and_star(self) -> bool:
        return self.proto.star_vehicle_peds_place_between_ego_and_star

    @star_vehicle_peds_place_between_ego_and_star.setter
    def star_vehicle_peds_place_between_ego_and_star(self, value: bool):
        self.proto.star_vehicle_peds_place_between_ego_and_star = value

    @property
    def star_vehicle_peds_max_distance_from_driveable_lane(self) -> float:
        return self.proto.star_vehicle_peds_max_distance_from_driveable_lane

    @star_vehicle_peds_max_distance_from_driveable_lane.setter
    def star_vehicle_peds_max_distance_from_driveable_lane(self, value: float):
        self.proto.star_vehicle_peds_max_distance_from_driveable_lane = value

    @property
    def shoulder_peds_max_distance_from_ref(self) -> float:
        return self.proto.shoulder_peds_max_distance_from_ref

    @shoulder_peds_max_distance_from_ref.setter
    def shoulder_peds_max_distance_from_ref(self, value: float):
        self.proto.shoulder_peds_max_distance_from_ref = value

    @property
    def min_peds_per_star(self) -> int:
        return self.proto.min_peds_per_star

    @min_peds_per_star.setter
    def min_peds_per_star(self, value: int):
        self.proto.min_peds_per_star = value

    @property
    def max_peds_per_star(self) -> int:
        return self.proto.max_peds_per_star

    @max_peds_per_star.setter
    def max_peds_per_star(self, value: int):
        self.proto.max_peds_per_star = value

    @property
    def min_peds_no_stars(self) -> int:
        return self.proto.min_peds_no_stars

    @min_peds_no_stars.setter
    def min_peds_no_stars(self, value: int):
        self.proto.min_peds_no_stars = value

    @property
    def max_peds_no_stars(self) -> int:
        return self.proto.max_peds_no_stars

    @max_peds_no_stars.setter
    def max_peds_no_stars(self, value: int):
        self.proto.max_peds_no_stars = value

    @property
    def max_attempts_to_place_each_ped(self) -> int:
        return self.proto.max_attempts_to_place_each_ped

    @max_attempts_to_place_each_ped.setter
    def max_attempts_to_place_each_ped(self, value: int):
        self.proto.max_attempts_to_place_each_ped = value

    @property
    def max_attempts_to_place_each_star(self) -> int:
        return self.proto.max_attempts_to_place_each_star

    @max_attempts_to_place_each_star.setter
    def max_attempts_to_place_each_star(self, value: int):
        self.proto.max_attempts_to_place_each_star = value

    @property
    def max_lane_recursions_to_check_ego_adjacency(self) -> int:
        return self.proto.max_lane_recursions_to_check_ego_adjacency

    @max_lane_recursions_to_check_ego_adjacency.setter
    def max_lane_recursions_to_check_ego_adjacency(self, value: int):
        self.proto.max_lane_recursions_to_check_ego_adjacency = value

    @property
    def scenario_fov_cull_limit(self) -> float:
        return self.proto.scenario_fov_cull_limit

    @scenario_fov_cull_limit.setter
    def scenario_fov_cull_limit(self, value: float):
        self.proto.scenario_fov_cull_limit = value

    @property
    def scenario_los_cull(self) -> bool:
        return self.proto.scenario_los_cull

    @scenario_los_cull.setter
    def scenario_los_cull(self, value: bool):
        self.proto.scenario_los_cull = value

    @property
    def reduce_spawn_to_zero_at_star_range(self) -> float:
        return self.proto.reduce_spawn_to_zero_at_star_range

    @reduce_spawn_to_zero_at_star_range.setter
    def reduce_spawn_to_zero_at_star_range(self, value: float):
        self.proto.reduce_spawn_to_zero_at_star_range = value

    @property
    def ped_pose_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._ped_pose_distribution

    @ped_pose_distribution.setter
    def ped_pose_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.ped_pose_distribution.CopyFrom(value.proto)

        self._ped_pose_distribution = value
        self._ped_pose_distribution._update_proto_references(self.proto.ped_pose_distribution)

    @property
    def emergency_vehicle_spawn_behind_star_probability(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._emergency_vehicle_spawn_behind_star_probability

    @emergency_vehicle_spawn_behind_star_probability.setter
    def emergency_vehicle_spawn_behind_star_probability(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.emergency_vehicle_spawn_behind_star_probability.CopyFrom(value.proto)

        self._emergency_vehicle_spawn_behind_star_probability = value
        self._emergency_vehicle_spawn_behind_star_probability._update_proto_references(
            self.proto.emergency_vehicle_spawn_behind_star_probability
        )

    @property
    def emergency_vehicle_distance_behind_star(self) -> float:
        return self.proto.emergency_vehicle_distance_behind_star

    @emergency_vehicle_distance_behind_star.setter
    def emergency_vehicle_distance_behind_star(self, value: float):
        self.proto.emergency_vehicle_distance_behind_star = value

    @property
    def min_emergency_vehicles_per_star(self) -> int:
        return self.proto.min_emergency_vehicles_per_star

    @min_emergency_vehicles_per_star.setter
    def min_emergency_vehicles_per_star(self, value: int):
        self.proto.min_emergency_vehicles_per_star = value

    @property
    def max_emergency_vehicles_per_star(self) -> int:
        return self.proto.max_emergency_vehicles_per_star

    @max_emergency_vehicles_per_star.setter
    def max_emergency_vehicles_per_star(self, value: int):
        self.proto.max_emergency_vehicles_per_star = value

    @property
    def emergency_vehicle_asset_tag(self) -> str:
        return self.proto.emergency_vehicle_asset_tag

    @emergency_vehicle_asset_tag.setter
    def emergency_vehicle_asset_tag(self, value: str):
        self.proto.emergency_vehicle_asset_tag = value

    @property
    def emergency_vehicle_country_tag(self) -> str:
        return self.proto.emergency_vehicle_country_tag

    @emergency_vehicle_country_tag.setter
    def emergency_vehicle_country_tag(self, value: str):
        self.proto.emergency_vehicle_country_tag = value

    def _update_proto_references(self, proto: pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo):
        self.proto = proto
        self._ped_pose_distribution._update_proto_references(proto.ped_pose_distribution)
        self._emergency_vehicle_spawn_behind_star_probability._update_proto_references(
            proto.emergency_vehicle_spawn_behind_star_probability
        )


@register_wrapper(proto_type=pd_spawn_pb2.LaneTypeScenarioGeneratorInfo)
class LaneTypeScenarioGeneratorInfo(ProtoMessageClass):
    """Generate scenarios with certain lane types

    Args:
        lane_type: :attr:`lane_type`
        dead_zone: :attr:`dead_zone`
        dead_zone_spread: :attr:`dead_zone_spread`
        asset_tags: :attr:`asset_tags`
        asset_search_radius: :attr:`asset_search_radius`
        num_instances: :attr:`num_instances`
    Attributes:
        lane_type: umd lane type enum converted to int
            Default: 1
        dead_zone: dead zone before end of a parking aisle lane
            Default: 10.0
        dead_zone_spread: Default: 0.0
        asset_tags:
        asset_search_radius:
        num_instances:"""

    _proto_message = pd_spawn_pb2.LaneTypeScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.LaneTypeScenarioGeneratorInfo] = None,
        lane_type: int = None,
        dead_zone: float = None,
        dead_zone_spread: float = None,
        asset_tags: str = None,
        asset_search_radius: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        num_instances: _pd_unified_generator_pb2.MinMaxConfigInt = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.LaneTypeScenarioGeneratorInfo()
        self.proto = proto
        self._asset_search_radius = get_wrapper(proto_type=proto.asset_search_radius.__class__)(
            proto=proto.asset_search_radius
        )
        self._num_instances = get_wrapper(proto_type=proto.num_instances.__class__)(proto=proto.num_instances)
        if lane_type is not None:
            self.lane_type = lane_type
        if dead_zone is not None:
            self.dead_zone = dead_zone
        if dead_zone_spread is not None:
            self.dead_zone_spread = dead_zone_spread
        if asset_tags is not None:
            self.asset_tags = asset_tags
        if asset_search_radius is not None:
            self.asset_search_radius = asset_search_radius
        if num_instances is not None:
            self.num_instances = num_instances

    @property
    def lane_type(self) -> int:
        return self.proto.lane_type

    @lane_type.setter
    def lane_type(self, value: int):
        self.proto.lane_type = value

    @property
    def dead_zone(self) -> float:
        return self.proto.dead_zone

    @dead_zone.setter
    def dead_zone(self, value: float):
        self.proto.dead_zone = value

    @property
    def dead_zone_spread(self) -> float:
        return self.proto.dead_zone_spread

    @dead_zone_spread.setter
    def dead_zone_spread(self, value: float):
        self.proto.dead_zone_spread = value

    @property
    def asset_tags(self) -> str:
        return self.proto.asset_tags

    @asset_tags.setter
    def asset_tags(self, value: str):
        self.proto.asset_tags = value

    @property
    def asset_search_radius(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._asset_search_radius

    @asset_search_radius.setter
    def asset_search_radius(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.asset_search_radius.CopyFrom(value.proto)

        self._asset_search_radius = value
        self._asset_search_radius._update_proto_references(self.proto.asset_search_radius)

    @property
    def num_instances(self) -> _pd_unified_generator_pb2.MinMaxConfigInt:
        return self._num_instances

    @num_instances.setter
    def num_instances(self, value: _pd_unified_generator_pb2.MinMaxConfigInt):
        self.proto.num_instances.CopyFrom(value.proto)

        self._num_instances = value
        self._num_instances._update_proto_references(self.proto.num_instances)

    def _update_proto_references(self, proto: pd_spawn_pb2.LaneTypeScenarioGeneratorInfo):
        self.proto = proto
        self._asset_search_radius._update_proto_references(proto.asset_search_radius)
        self._num_instances._update_proto_references(proto.num_instances)


@register_wrapper(proto_type=pd_spawn_pb2.StaticCamScenarioGeneratorInfo)
class StaticCamScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        distance_from_junction: :attr:`distance_from_junction`
        distance_from_junction_spread: :attr:`distance_from_junction_spread`
        elevation: :attr:`elevation`
        elevation_spread: :attr:`elevation_spread`
    Attributes:
        distance_from_junction: Distance from junction to spawn sensors
            Default: 10.0
        distance_from_junction_spread: Default: 5.0
        elevation: Elevation above road to spawn sensors
            Default: 5.0
        elevation_spread: Default: 2.0"""

    _proto_message = pd_spawn_pb2.StaticCamScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.StaticCamScenarioGeneratorInfo] = None,
        distance_from_junction: float = None,
        distance_from_junction_spread: float = None,
        elevation: float = None,
        elevation_spread: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.StaticCamScenarioGeneratorInfo()
        self.proto = proto
        if distance_from_junction is not None:
            self.distance_from_junction = distance_from_junction
        if distance_from_junction_spread is not None:
            self.distance_from_junction_spread = distance_from_junction_spread
        if elevation is not None:
            self.elevation = elevation
        if elevation_spread is not None:
            self.elevation_spread = elevation_spread

    @property
    def distance_from_junction(self) -> float:
        return self.proto.distance_from_junction

    @distance_from_junction.setter
    def distance_from_junction(self, value: float):
        self.proto.distance_from_junction = value

    @property
    def distance_from_junction_spread(self) -> float:
        return self.proto.distance_from_junction_spread

    @distance_from_junction_spread.setter
    def distance_from_junction_spread(self, value: float):
        self.proto.distance_from_junction_spread = value

    @property
    def elevation(self) -> float:
        return self.proto.elevation

    @elevation.setter
    def elevation(self, value: float):
        self.proto.elevation = value

    @property
    def elevation_spread(self) -> float:
        return self.proto.elevation_spread

    @elevation_spread.setter
    def elevation_spread(self, value: float):
        self.proto.elevation_spread = value

    def _update_proto_references(self, proto: pd_spawn_pb2.StaticCamScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.JaywalkingScenarioGeneratorInfo)
class JaywalkingScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        jaywalkerMaxDistance: :attr:`jaywalkerMaxDistance`
        jaywalkerMinDistance: :attr:`jaywalkerMinDistance`
        jaywalkerConeAngle: :attr:`jaywalkerConeAngle`
        jaywalkerEgoCarlengths: :attr:`jaywalkerEgoCarlengths`
        jaywalkerFinalRadiusSpread: :attr:`jaywalkerFinalRadiusSpread`
        jaywalkerNumber: :attr:`jaywalkerNumber`
        jaywalkerRoadDistanceMax: :attr:`jaywalkerRoadDistanceMax`
        jaywalkerRoadDistanceMin: :attr:`jaywalkerRoadDistanceMin`
        generateOccluders: :attr:`generateOccluders`
        placeCarOccluders: :attr:`placeCarOccluders`
        placePropOccluders: :attr:`placePropOccluders`
        animalProbability: :attr:`animalProbability`
        coneDensity: :attr:`coneDensity`
        vehicleOccluderPreference: :attr:`vehicleOccluderPreference`
        signal_light_distribution: :attr:`signal_light_distribution`
    Attributes:
        jaywalkerMaxDistance: Default: 50.0
        jaywalkerMinDistance: Default: 10.0
        jaywalkerConeAngle: Default: 45.0
        jaywalkerEgoCarlengths: Default: 3.0
        jaywalkerFinalRadiusSpread: Default: 3.0
        jaywalkerNumber: Default: 1
        jaywalkerRoadDistanceMax: Default: 1.0
        jaywalkerRoadDistanceMin: Default: 0.0
        generateOccluders: Default: False
        placeCarOccluders: Default: False
        placePropOccluders: Default: False
        animalProbability: Default: 0.0
        coneDensity: Default: 0.0
        vehicleOccluderPreference: Default: 0.5
        signal_light_distribution:"""

    _proto_message = pd_spawn_pb2.JaywalkingScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.JaywalkingScenarioGeneratorInfo] = None,
        jaywalkerMaxDistance: float = None,
        jaywalkerMinDistance: float = None,
        jaywalkerConeAngle: float = None,
        jaywalkerEgoCarlengths: float = None,
        jaywalkerFinalRadiusSpread: float = None,
        jaywalkerNumber: int = None,
        jaywalkerRoadDistanceMax: float = None,
        jaywalkerRoadDistanceMin: float = None,
        generateOccluders: bool = None,
        placeCarOccluders: bool = None,
        placePropOccluders: bool = None,
        animalProbability: float = None,
        coneDensity: float = None,
        vehicleOccluderPreference: float = None,
        signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.JaywalkingScenarioGeneratorInfo()
        self.proto = proto
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(
            proto=proto.signal_light_distribution
        )
        if jaywalkerMaxDistance is not None:
            self.jaywalkerMaxDistance = jaywalkerMaxDistance
        if jaywalkerMinDistance is not None:
            self.jaywalkerMinDistance = jaywalkerMinDistance
        if jaywalkerConeAngle is not None:
            self.jaywalkerConeAngle = jaywalkerConeAngle
        if jaywalkerEgoCarlengths is not None:
            self.jaywalkerEgoCarlengths = jaywalkerEgoCarlengths
        if jaywalkerFinalRadiusSpread is not None:
            self.jaywalkerFinalRadiusSpread = jaywalkerFinalRadiusSpread
        if jaywalkerNumber is not None:
            self.jaywalkerNumber = jaywalkerNumber
        if jaywalkerRoadDistanceMax is not None:
            self.jaywalkerRoadDistanceMax = jaywalkerRoadDistanceMax
        if jaywalkerRoadDistanceMin is not None:
            self.jaywalkerRoadDistanceMin = jaywalkerRoadDistanceMin
        if generateOccluders is not None:
            self.generateOccluders = generateOccluders
        if placeCarOccluders is not None:
            self.placeCarOccluders = placeCarOccluders
        if placePropOccluders is not None:
            self.placePropOccluders = placePropOccluders
        if animalProbability is not None:
            self.animalProbability = animalProbability
        if coneDensity is not None:
            self.coneDensity = coneDensity
        if vehicleOccluderPreference is not None:
            self.vehicleOccluderPreference = vehicleOccluderPreference
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution

    @property
    def jaywalkerMaxDistance(self) -> float:
        return self.proto.jaywalkerMaxDistance

    @jaywalkerMaxDistance.setter
    def jaywalkerMaxDistance(self, value: float):
        self.proto.jaywalkerMaxDistance = value

    @property
    def jaywalkerMinDistance(self) -> float:
        return self.proto.jaywalkerMinDistance

    @jaywalkerMinDistance.setter
    def jaywalkerMinDistance(self, value: float):
        self.proto.jaywalkerMinDistance = value

    @property
    def jaywalkerConeAngle(self) -> float:
        return self.proto.jaywalkerConeAngle

    @jaywalkerConeAngle.setter
    def jaywalkerConeAngle(self, value: float):
        self.proto.jaywalkerConeAngle = value

    @property
    def jaywalkerEgoCarlengths(self) -> float:
        return self.proto.jaywalkerEgoCarlengths

    @jaywalkerEgoCarlengths.setter
    def jaywalkerEgoCarlengths(self, value: float):
        self.proto.jaywalkerEgoCarlengths = value

    @property
    def jaywalkerFinalRadiusSpread(self) -> float:
        return self.proto.jaywalkerFinalRadiusSpread

    @jaywalkerFinalRadiusSpread.setter
    def jaywalkerFinalRadiusSpread(self, value: float):
        self.proto.jaywalkerFinalRadiusSpread = value

    @property
    def jaywalkerNumber(self) -> int:
        return self.proto.jaywalkerNumber

    @jaywalkerNumber.setter
    def jaywalkerNumber(self, value: int):
        self.proto.jaywalkerNumber = value

    @property
    def jaywalkerRoadDistanceMax(self) -> float:
        return self.proto.jaywalkerRoadDistanceMax

    @jaywalkerRoadDistanceMax.setter
    def jaywalkerRoadDistanceMax(self, value: float):
        self.proto.jaywalkerRoadDistanceMax = value

    @property
    def jaywalkerRoadDistanceMin(self) -> float:
        return self.proto.jaywalkerRoadDistanceMin

    @jaywalkerRoadDistanceMin.setter
    def jaywalkerRoadDistanceMin(self, value: float):
        self.proto.jaywalkerRoadDistanceMin = value

    @property
    def generateOccluders(self) -> bool:
        return self.proto.generateOccluders

    @generateOccluders.setter
    def generateOccluders(self, value: bool):
        self.proto.generateOccluders = value

    @property
    def placeCarOccluders(self) -> bool:
        return self.proto.placeCarOccluders

    @placeCarOccluders.setter
    def placeCarOccluders(self, value: bool):
        self.proto.placeCarOccluders = value

    @property
    def placePropOccluders(self) -> bool:
        return self.proto.placePropOccluders

    @placePropOccluders.setter
    def placePropOccluders(self, value: bool):
        self.proto.placePropOccluders = value

    @property
    def animalProbability(self) -> float:
        return self.proto.animalProbability

    @animalProbability.setter
    def animalProbability(self, value: float):
        self.proto.animalProbability = value

    @property
    def coneDensity(self) -> float:
        return self.proto.coneDensity

    @coneDensity.setter
    def coneDensity(self, value: float):
        self.proto.coneDensity = value

    @property
    def vehicleOccluderPreference(self) -> float:
        return self.proto.vehicleOccluderPreference

    @vehicleOccluderPreference.setter
    def vehicleOccluderPreference(self, value: float):
        self.proto.vehicleOccluderPreference = value

    @property
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self.proto.signal_light_distribution.CopyFrom(value.proto)

        self._signal_light_distribution = value
        self._signal_light_distribution._update_proto_references(self.proto.signal_light_distribution)

    def _update_proto_references(self, proto: pd_spawn_pb2.JaywalkingScenarioGeneratorInfo):
        self.proto = proto
        self._signal_light_distribution._update_proto_references(proto.signal_light_distribution)


@register_wrapper(proto_type=pd_spawn_pb2.PropScenarioGeneratorInfo)
class PropScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        propMaxDistance: :attr:`propMaxDistance`
        propMinDistance: :attr:`propMinDistance`
        placeMessageBoard: :attr:`placeMessageBoard`
        initialMessageBoardAssetTag: :attr:`initialMessageBoardAssetTag`
        initialMessageBoardRightAssetTag: :attr:`initialMessageBoardRightAssetTag`
        placeIntermediateMessageBoards: :attr:`placeIntermediateMessageBoards`
        placeIntermediateMessageBoardsProbability: :attr:`placeIntermediateMessageBoardsProbability`
        intermediateMessageBoardAssetTag: :attr:`intermediateMessageBoardAssetTag`
        intermediateMessageBoardRightAssetTag: :attr:`intermediateMessageBoardRightAssetTag`
        intermediateMessageBoardAngleVariation: :attr:`intermediateMessageBoardAngleVariation`
        coneSpacing: :attr:`coneSpacing`
        maxConeSpacingDeviationPercent: :attr:`maxConeSpacingDeviationPercent`
        maxLateralTaperConeSpacingDeviation: :attr:`maxLateralTaperConeSpacingDeviation`
        maxLateralClosureConeSpacingDeviation: :attr:`maxLateralClosureConeSpacingDeviation`
        maxLateralLeadConeSpacingDeviation: :attr:`maxLateralLeadConeSpacingDeviation`
        maxConeAngleDeviation: :attr:`maxConeAngleDeviation`
        coneAssetTag: :attr:`coneAssetTag`
        taperLowerSpeedThreshold: :attr:`taperLowerSpeedThreshold`
        taperUpperSpeedThreshold: :attr:`taperUpperSpeedThreshold`
        taperSlowFormulaDemoninator: :attr:`taperSlowFormulaDemoninator`
        minTaperLength: :attr:`minTaperLength`
        taperLengthSpeedSpreadPercent: :attr:`taperLengthSpeedSpreadPercent`
        taperLengthScaleFactor: :attr:`taperLengthScaleFactor`
        minLanesToClose: :attr:`minLanesToClose`
        maxLanesToClose: :attr:`maxLanesToClose`
        placeLeadCones: :attr:`placeLeadCones`
        leadConeLength: :attr:`leadConeLength`
        leadConeLengthForSingleLaneClosure: :attr:`leadConeLengthForSingleLaneClosure`
        placeClosureCones: :attr:`placeClosureCones`
        closureConeLength: :attr:`closureConeLength`
        closureConeLengthForSingleLaneClosure: :attr:`closureConeLengthForSingleLaneClosure`
        rightSideClosureProbability: :attr:`rightSideClosureProbability`
        propVehicleTag: :attr:`propVehicleTag`
        propTag: :attr:`propTag`
        leadConeSpacing: :attr:`leadConeSpacing`
        closureConeSpacing: :attr:`closureConeSpacing`
        scenario_cull_on_bad_cone_los: :attr:`scenario_cull_on_bad_cone_los`
        scenario_cull_on_bad_cone_fov: :attr:`scenario_cull_on_bad_cone_fov`
        reduce_spawn_to_zero_at_construction_range: :attr:`reduce_spawn_to_zero_at_construction_range`
        missing_cone_chance: :attr:`missing_cone_chance`
        num_fallen_cone_groups: :attr:`num_fallen_cone_groups`
        size_fallen_cone_groups: :attr:`size_fallen_cone_groups`
        suffix_fallen_cone_assets: :attr:`suffix_fallen_cone_assets`
        vehiclePlacementProbability: :attr:`vehiclePlacementProbability`
    Attributes:
        propMaxDistance: generator for placing static objects in the scene
            Default: 15.0
        propMinDistance: Default: 20.0
        placeMessageBoard: Default: True
        initialMessageBoardAssetTag:
        initialMessageBoardRightAssetTag:
        placeIntermediateMessageBoards: Default: False
        placeIntermediateMessageBoardsProbability: Default: 0.3
        intermediateMessageBoardAssetTag:
        intermediateMessageBoardRightAssetTag:
        intermediateMessageBoardAngleVariation: Default: 0.1
        coneSpacing:
        maxConeSpacingDeviationPercent: Default: 0.25
        maxLateralTaperConeSpacingDeviation: Default: 0.1
        maxLateralClosureConeSpacingDeviation: Default: 0.05
        maxLateralLeadConeSpacingDeviation: Default: 0.05
        maxConeAngleDeviation: Default: 0.2
        coneAssetTag: Default: cone_lane_closure
        taperLowerSpeedThreshold: Default: 40.0
        taperUpperSpeedThreshold: Default: 45.0
        taperSlowFormulaDemoninator: Default: 60.0
        minTaperLength: Default: 30.0
        taperLengthSpeedSpreadPercent: Default: 0.1
        taperLengthScaleFactor: Default: 0.7
        minLanesToClose: Default: 1
        maxLanesToClose: Default: 2
        placeLeadCones: Default: True
        leadConeLength:
        leadConeLengthForSingleLaneClosure:
        placeClosureCones: Default: True
        closureConeLength:
        closureConeLengthForSingleLaneClosure:
        rightSideClosureProbability: Default: 0.5
        propVehicleTag: Default: construction_vehicle
        propTag: Default: lane_closure_vignette
        leadConeSpacing:
        closureConeSpacing:
        scenario_cull_on_bad_cone_los: Default: True
        scenario_cull_on_bad_cone_fov: Default: 0.0
        reduce_spawn_to_zero_at_construction_range: Default: 500.0
        missing_cone_chance: Default: 0.05
        num_fallen_cone_groups:
        size_fallen_cone_groups:
        suffix_fallen_cone_assets: Default: _fallen_over
        vehiclePlacementProbability: Default: 0.5"""

    _proto_message = pd_spawn_pb2.PropScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.PropScenarioGeneratorInfo] = None,
        propMaxDistance: float = None,
        propMinDistance: float = None,
        placeMessageBoard: bool = None,
        initialMessageBoardAssetTag: str = None,
        initialMessageBoardRightAssetTag: str = None,
        placeIntermediateMessageBoards: bool = None,
        placeIntermediateMessageBoardsProbability: float = None,
        intermediateMessageBoardAssetTag: str = None,
        intermediateMessageBoardRightAssetTag: str = None,
        intermediateMessageBoardAngleVariation: float = None,
        coneSpacing: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        maxConeSpacingDeviationPercent: float = None,
        maxLateralTaperConeSpacingDeviation: float = None,
        maxLateralClosureConeSpacingDeviation: float = None,
        maxLateralLeadConeSpacingDeviation: float = None,
        maxConeAngleDeviation: float = None,
        coneAssetTag: str = None,
        taperLowerSpeedThreshold: float = None,
        taperUpperSpeedThreshold: float = None,
        taperSlowFormulaDemoninator: float = None,
        minTaperLength: float = None,
        taperLengthSpeedSpreadPercent: float = None,
        taperLengthScaleFactor: float = None,
        minLanesToClose: int = None,
        maxLanesToClose: int = None,
        placeLeadCones: bool = None,
        leadConeLength: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        leadConeLengthForSingleLaneClosure: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        placeClosureCones: bool = None,
        closureConeLength: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        closureConeLengthForSingleLaneClosure: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        rightSideClosureProbability: float = None,
        propVehicleTag: str = None,
        propTag: str = None,
        leadConeSpacing: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        closureConeSpacing: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        scenario_cull_on_bad_cone_los: bool = None,
        scenario_cull_on_bad_cone_fov: float = None,
        reduce_spawn_to_zero_at_construction_range: float = None,
        missing_cone_chance: float = None,
        num_fallen_cone_groups: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        size_fallen_cone_groups: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        suffix_fallen_cone_assets: str = None,
        vehiclePlacementProbability: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.PropScenarioGeneratorInfo()
        self.proto = proto
        self._coneSpacing = get_wrapper(proto_type=proto.coneSpacing.__class__)(proto=proto.coneSpacing)
        self._leadConeLength = get_wrapper(proto_type=proto.leadConeLength.__class__)(proto=proto.leadConeLength)
        self._leadConeLengthForSingleLaneClosure = get_wrapper(
            proto_type=proto.leadConeLengthForSingleLaneClosure.__class__
        )(proto=proto.leadConeLengthForSingleLaneClosure)
        self._closureConeLength = get_wrapper(proto_type=proto.closureConeLength.__class__)(
            proto=proto.closureConeLength
        )
        self._closureConeLengthForSingleLaneClosure = get_wrapper(
            proto_type=proto.closureConeLengthForSingleLaneClosure.__class__
        )(proto=proto.closureConeLengthForSingleLaneClosure)
        self._leadConeSpacing = get_wrapper(proto_type=proto.leadConeSpacing.__class__)(proto=proto.leadConeSpacing)
        self._closureConeSpacing = get_wrapper(proto_type=proto.closureConeSpacing.__class__)(
            proto=proto.closureConeSpacing
        )
        self._num_fallen_cone_groups = get_wrapper(proto_type=proto.num_fallen_cone_groups.__class__)(
            proto=proto.num_fallen_cone_groups
        )
        self._size_fallen_cone_groups = get_wrapper(proto_type=proto.size_fallen_cone_groups.__class__)(
            proto=proto.size_fallen_cone_groups
        )
        if propMaxDistance is not None:
            self.propMaxDistance = propMaxDistance
        if propMinDistance is not None:
            self.propMinDistance = propMinDistance
        if placeMessageBoard is not None:
            self.placeMessageBoard = placeMessageBoard
        if initialMessageBoardAssetTag is not None:
            self.initialMessageBoardAssetTag = initialMessageBoardAssetTag
        if initialMessageBoardRightAssetTag is not None:
            self.initialMessageBoardRightAssetTag = initialMessageBoardRightAssetTag
        if placeIntermediateMessageBoards is not None:
            self.placeIntermediateMessageBoards = placeIntermediateMessageBoards
        if placeIntermediateMessageBoardsProbability is not None:
            self.placeIntermediateMessageBoardsProbability = placeIntermediateMessageBoardsProbability
        if intermediateMessageBoardAssetTag is not None:
            self.intermediateMessageBoardAssetTag = intermediateMessageBoardAssetTag
        if intermediateMessageBoardRightAssetTag is not None:
            self.intermediateMessageBoardRightAssetTag = intermediateMessageBoardRightAssetTag
        if intermediateMessageBoardAngleVariation is not None:
            self.intermediateMessageBoardAngleVariation = intermediateMessageBoardAngleVariation
        if coneSpacing is not None:
            self.coneSpacing = coneSpacing
        if maxConeSpacingDeviationPercent is not None:
            self.maxConeSpacingDeviationPercent = maxConeSpacingDeviationPercent
        if maxLateralTaperConeSpacingDeviation is not None:
            self.maxLateralTaperConeSpacingDeviation = maxLateralTaperConeSpacingDeviation
        if maxLateralClosureConeSpacingDeviation is not None:
            self.maxLateralClosureConeSpacingDeviation = maxLateralClosureConeSpacingDeviation
        if maxLateralLeadConeSpacingDeviation is not None:
            self.maxLateralLeadConeSpacingDeviation = maxLateralLeadConeSpacingDeviation
        if maxConeAngleDeviation is not None:
            self.maxConeAngleDeviation = maxConeAngleDeviation
        if coneAssetTag is not None:
            self.coneAssetTag = coneAssetTag
        if taperLowerSpeedThreshold is not None:
            self.taperLowerSpeedThreshold = taperLowerSpeedThreshold
        if taperUpperSpeedThreshold is not None:
            self.taperUpperSpeedThreshold = taperUpperSpeedThreshold
        if taperSlowFormulaDemoninator is not None:
            self.taperSlowFormulaDemoninator = taperSlowFormulaDemoninator
        if minTaperLength is not None:
            self.minTaperLength = minTaperLength
        if taperLengthSpeedSpreadPercent is not None:
            self.taperLengthSpeedSpreadPercent = taperLengthSpeedSpreadPercent
        if taperLengthScaleFactor is not None:
            self.taperLengthScaleFactor = taperLengthScaleFactor
        if minLanesToClose is not None:
            self.minLanesToClose = minLanesToClose
        if maxLanesToClose is not None:
            self.maxLanesToClose = maxLanesToClose
        if placeLeadCones is not None:
            self.placeLeadCones = placeLeadCones
        if leadConeLength is not None:
            self.leadConeLength = leadConeLength
        if leadConeLengthForSingleLaneClosure is not None:
            self.leadConeLengthForSingleLaneClosure = leadConeLengthForSingleLaneClosure
        if placeClosureCones is not None:
            self.placeClosureCones = placeClosureCones
        if closureConeLength is not None:
            self.closureConeLength = closureConeLength
        if closureConeLengthForSingleLaneClosure is not None:
            self.closureConeLengthForSingleLaneClosure = closureConeLengthForSingleLaneClosure
        if rightSideClosureProbability is not None:
            self.rightSideClosureProbability = rightSideClosureProbability
        if propVehicleTag is not None:
            self.propVehicleTag = propVehicleTag
        if propTag is not None:
            self.propTag = propTag
        if leadConeSpacing is not None:
            self.leadConeSpacing = leadConeSpacing
        if closureConeSpacing is not None:
            self.closureConeSpacing = closureConeSpacing
        if scenario_cull_on_bad_cone_los is not None:
            self.scenario_cull_on_bad_cone_los = scenario_cull_on_bad_cone_los
        if scenario_cull_on_bad_cone_fov is not None:
            self.scenario_cull_on_bad_cone_fov = scenario_cull_on_bad_cone_fov
        if reduce_spawn_to_zero_at_construction_range is not None:
            self.reduce_spawn_to_zero_at_construction_range = reduce_spawn_to_zero_at_construction_range
        if missing_cone_chance is not None:
            self.missing_cone_chance = missing_cone_chance
        if num_fallen_cone_groups is not None:
            self.num_fallen_cone_groups = num_fallen_cone_groups
        if size_fallen_cone_groups is not None:
            self.size_fallen_cone_groups = size_fallen_cone_groups
        if suffix_fallen_cone_assets is not None:
            self.suffix_fallen_cone_assets = suffix_fallen_cone_assets
        if vehiclePlacementProbability is not None:
            self.vehiclePlacementProbability = vehiclePlacementProbability

    @property
    def propMaxDistance(self) -> float:
        return self.proto.propMaxDistance

    @propMaxDistance.setter
    def propMaxDistance(self, value: float):
        self.proto.propMaxDistance = value

    @property
    def propMinDistance(self) -> float:
        return self.proto.propMinDistance

    @propMinDistance.setter
    def propMinDistance(self, value: float):
        self.proto.propMinDistance = value

    @property
    def placeMessageBoard(self) -> bool:
        return self.proto.placeMessageBoard

    @placeMessageBoard.setter
    def placeMessageBoard(self, value: bool):
        self.proto.placeMessageBoard = value

    @property
    def initialMessageBoardAssetTag(self) -> str:
        return self.proto.initialMessageBoardAssetTag

    @initialMessageBoardAssetTag.setter
    def initialMessageBoardAssetTag(self, value: str):
        self.proto.initialMessageBoardAssetTag = value

    @property
    def initialMessageBoardRightAssetTag(self) -> str:
        return self.proto.initialMessageBoardRightAssetTag

    @initialMessageBoardRightAssetTag.setter
    def initialMessageBoardRightAssetTag(self, value: str):
        self.proto.initialMessageBoardRightAssetTag = value

    @property
    def placeIntermediateMessageBoards(self) -> bool:
        return self.proto.placeIntermediateMessageBoards

    @placeIntermediateMessageBoards.setter
    def placeIntermediateMessageBoards(self, value: bool):
        self.proto.placeIntermediateMessageBoards = value

    @property
    def placeIntermediateMessageBoardsProbability(self) -> float:
        return self.proto.placeIntermediateMessageBoardsProbability

    @placeIntermediateMessageBoardsProbability.setter
    def placeIntermediateMessageBoardsProbability(self, value: float):
        self.proto.placeIntermediateMessageBoardsProbability = value

    @property
    def intermediateMessageBoardAssetTag(self) -> str:
        return self.proto.intermediateMessageBoardAssetTag

    @intermediateMessageBoardAssetTag.setter
    def intermediateMessageBoardAssetTag(self, value: str):
        self.proto.intermediateMessageBoardAssetTag = value

    @property
    def intermediateMessageBoardRightAssetTag(self) -> str:
        return self.proto.intermediateMessageBoardRightAssetTag

    @intermediateMessageBoardRightAssetTag.setter
    def intermediateMessageBoardRightAssetTag(self, value: str):
        self.proto.intermediateMessageBoardRightAssetTag = value

    @property
    def intermediateMessageBoardAngleVariation(self) -> float:
        return self.proto.intermediateMessageBoardAngleVariation

    @intermediateMessageBoardAngleVariation.setter
    def intermediateMessageBoardAngleVariation(self, value: float):
        self.proto.intermediateMessageBoardAngleVariation = value

    @property
    def coneSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._coneSpacing

    @coneSpacing.setter
    def coneSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.coneSpacing.CopyFrom(value.proto)

        self._coneSpacing = value
        self._coneSpacing._update_proto_references(self.proto.coneSpacing)

    @property
    def maxConeSpacingDeviationPercent(self) -> float:
        return self.proto.maxConeSpacingDeviationPercent

    @maxConeSpacingDeviationPercent.setter
    def maxConeSpacingDeviationPercent(self, value: float):
        self.proto.maxConeSpacingDeviationPercent = value

    @property
    def maxLateralTaperConeSpacingDeviation(self) -> float:
        return self.proto.maxLateralTaperConeSpacingDeviation

    @maxLateralTaperConeSpacingDeviation.setter
    def maxLateralTaperConeSpacingDeviation(self, value: float):
        self.proto.maxLateralTaperConeSpacingDeviation = value

    @property
    def maxLateralClosureConeSpacingDeviation(self) -> float:
        return self.proto.maxLateralClosureConeSpacingDeviation

    @maxLateralClosureConeSpacingDeviation.setter
    def maxLateralClosureConeSpacingDeviation(self, value: float):
        self.proto.maxLateralClosureConeSpacingDeviation = value

    @property
    def maxLateralLeadConeSpacingDeviation(self) -> float:
        return self.proto.maxLateralLeadConeSpacingDeviation

    @maxLateralLeadConeSpacingDeviation.setter
    def maxLateralLeadConeSpacingDeviation(self, value: float):
        self.proto.maxLateralLeadConeSpacingDeviation = value

    @property
    def maxConeAngleDeviation(self) -> float:
        return self.proto.maxConeAngleDeviation

    @maxConeAngleDeviation.setter
    def maxConeAngleDeviation(self, value: float):
        self.proto.maxConeAngleDeviation = value

    @property
    def coneAssetTag(self) -> str:
        return self.proto.coneAssetTag

    @coneAssetTag.setter
    def coneAssetTag(self, value: str):
        self.proto.coneAssetTag = value

    @property
    def taperLowerSpeedThreshold(self) -> float:
        return self.proto.taperLowerSpeedThreshold

    @taperLowerSpeedThreshold.setter
    def taperLowerSpeedThreshold(self, value: float):
        self.proto.taperLowerSpeedThreshold = value

    @property
    def taperUpperSpeedThreshold(self) -> float:
        return self.proto.taperUpperSpeedThreshold

    @taperUpperSpeedThreshold.setter
    def taperUpperSpeedThreshold(self, value: float):
        self.proto.taperUpperSpeedThreshold = value

    @property
    def taperSlowFormulaDemoninator(self) -> float:
        return self.proto.taperSlowFormulaDemoninator

    @taperSlowFormulaDemoninator.setter
    def taperSlowFormulaDemoninator(self, value: float):
        self.proto.taperSlowFormulaDemoninator = value

    @property
    def minTaperLength(self) -> float:
        return self.proto.minTaperLength

    @minTaperLength.setter
    def minTaperLength(self, value: float):
        self.proto.minTaperLength = value

    @property
    def taperLengthSpeedSpreadPercent(self) -> float:
        return self.proto.taperLengthSpeedSpreadPercent

    @taperLengthSpeedSpreadPercent.setter
    def taperLengthSpeedSpreadPercent(self, value: float):
        self.proto.taperLengthSpeedSpreadPercent = value

    @property
    def taperLengthScaleFactor(self) -> float:
        return self.proto.taperLengthScaleFactor

    @taperLengthScaleFactor.setter
    def taperLengthScaleFactor(self, value: float):
        self.proto.taperLengthScaleFactor = value

    @property
    def minLanesToClose(self) -> int:
        return self.proto.minLanesToClose

    @minLanesToClose.setter
    def minLanesToClose(self, value: int):
        self.proto.minLanesToClose = value

    @property
    def maxLanesToClose(self) -> int:
        return self.proto.maxLanesToClose

    @maxLanesToClose.setter
    def maxLanesToClose(self, value: int):
        self.proto.maxLanesToClose = value

    @property
    def placeLeadCones(self) -> bool:
        return self.proto.placeLeadCones

    @placeLeadCones.setter
    def placeLeadCones(self, value: bool):
        self.proto.placeLeadCones = value

    @property
    def leadConeLength(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeLength

    @leadConeLength.setter
    def leadConeLength(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.leadConeLength.CopyFrom(value.proto)

        self._leadConeLength = value
        self._leadConeLength._update_proto_references(self.proto.leadConeLength)

    @property
    def leadConeLengthForSingleLaneClosure(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeLengthForSingleLaneClosure

    @leadConeLengthForSingleLaneClosure.setter
    def leadConeLengthForSingleLaneClosure(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.leadConeLengthForSingleLaneClosure.CopyFrom(value.proto)

        self._leadConeLengthForSingleLaneClosure = value
        self._leadConeLengthForSingleLaneClosure._update_proto_references(self.proto.leadConeLengthForSingleLaneClosure)

    @property
    def placeClosureCones(self) -> bool:
        return self.proto.placeClosureCones

    @placeClosureCones.setter
    def placeClosureCones(self, value: bool):
        self.proto.placeClosureCones = value

    @property
    def closureConeLength(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeLength

    @closureConeLength.setter
    def closureConeLength(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.closureConeLength.CopyFrom(value.proto)

        self._closureConeLength = value
        self._closureConeLength._update_proto_references(self.proto.closureConeLength)

    @property
    def closureConeLengthForSingleLaneClosure(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeLengthForSingleLaneClosure

    @closureConeLengthForSingleLaneClosure.setter
    def closureConeLengthForSingleLaneClosure(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.closureConeLengthForSingleLaneClosure.CopyFrom(value.proto)

        self._closureConeLengthForSingleLaneClosure = value
        self._closureConeLengthForSingleLaneClosure._update_proto_references(
            self.proto.closureConeLengthForSingleLaneClosure
        )

    @property
    def rightSideClosureProbability(self) -> float:
        return self.proto.rightSideClosureProbability

    @rightSideClosureProbability.setter
    def rightSideClosureProbability(self, value: float):
        self.proto.rightSideClosureProbability = value

    @property
    def propVehicleTag(self) -> str:
        return self.proto.propVehicleTag

    @propVehicleTag.setter
    def propVehicleTag(self, value: str):
        self.proto.propVehicleTag = value

    @property
    def propTag(self) -> str:
        return self.proto.propTag

    @propTag.setter
    def propTag(self, value: str):
        self.proto.propTag = value

    @property
    def leadConeSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeSpacing

    @leadConeSpacing.setter
    def leadConeSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.leadConeSpacing.CopyFrom(value.proto)

        self._leadConeSpacing = value
        self._leadConeSpacing._update_proto_references(self.proto.leadConeSpacing)

    @property
    def closureConeSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeSpacing

    @closureConeSpacing.setter
    def closureConeSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.closureConeSpacing.CopyFrom(value.proto)

        self._closureConeSpacing = value
        self._closureConeSpacing._update_proto_references(self.proto.closureConeSpacing)

    @property
    def scenario_cull_on_bad_cone_los(self) -> bool:
        return self.proto.scenario_cull_on_bad_cone_los

    @scenario_cull_on_bad_cone_los.setter
    def scenario_cull_on_bad_cone_los(self, value: bool):
        self.proto.scenario_cull_on_bad_cone_los = value

    @property
    def scenario_cull_on_bad_cone_fov(self) -> float:
        return self.proto.scenario_cull_on_bad_cone_fov

    @scenario_cull_on_bad_cone_fov.setter
    def scenario_cull_on_bad_cone_fov(self, value: float):
        self.proto.scenario_cull_on_bad_cone_fov = value

    @property
    def reduce_spawn_to_zero_at_construction_range(self) -> float:
        return self.proto.reduce_spawn_to_zero_at_construction_range

    @reduce_spawn_to_zero_at_construction_range.setter
    def reduce_spawn_to_zero_at_construction_range(self, value: float):
        self.proto.reduce_spawn_to_zero_at_construction_range = value

    @property
    def missing_cone_chance(self) -> float:
        return self.proto.missing_cone_chance

    @missing_cone_chance.setter
    def missing_cone_chance(self, value: float):
        self.proto.missing_cone_chance = value

    @property
    def num_fallen_cone_groups(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._num_fallen_cone_groups

    @num_fallen_cone_groups.setter
    def num_fallen_cone_groups(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.num_fallen_cone_groups.CopyFrom(value.proto)

        self._num_fallen_cone_groups = value
        self._num_fallen_cone_groups._update_proto_references(self.proto.num_fallen_cone_groups)

    @property
    def size_fallen_cone_groups(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._size_fallen_cone_groups

    @size_fallen_cone_groups.setter
    def size_fallen_cone_groups(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.size_fallen_cone_groups.CopyFrom(value.proto)

        self._size_fallen_cone_groups = value
        self._size_fallen_cone_groups._update_proto_references(self.proto.size_fallen_cone_groups)

    @property
    def suffix_fallen_cone_assets(self) -> str:
        return self.proto.suffix_fallen_cone_assets

    @suffix_fallen_cone_assets.setter
    def suffix_fallen_cone_assets(self, value: str):
        self.proto.suffix_fallen_cone_assets = value

    @property
    def vehiclePlacementProbability(self) -> float:
        return self.proto.vehiclePlacementProbability

    @vehiclePlacementProbability.setter
    def vehiclePlacementProbability(self, value: float):
        self.proto.vehiclePlacementProbability = value

    def _update_proto_references(self, proto: pd_spawn_pb2.PropScenarioGeneratorInfo):
        self.proto = proto
        self._coneSpacing._update_proto_references(proto.coneSpacing)
        self._leadConeLength._update_proto_references(proto.leadConeLength)
        self._leadConeLengthForSingleLaneClosure._update_proto_references(proto.leadConeLengthForSingleLaneClosure)
        self._closureConeLength._update_proto_references(proto.closureConeLength)
        self._closureConeLengthForSingleLaneClosure._update_proto_references(
            proto.closureConeLengthForSingleLaneClosure
        )
        self._leadConeSpacing._update_proto_references(proto.leadConeSpacing)
        self._closureConeSpacing._update_proto_references(proto.closureConeSpacing)
        self._num_fallen_cone_groups._update_proto_references(proto.num_fallen_cone_groups)
        self._size_fallen_cone_groups._update_proto_references(proto.size_fallen_cone_groups)


@register_wrapper(proto_type=pd_spawn_pb2.DebrisScenarioGeneratorInfo)
class DebrisScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        smallDebrisDensity: :attr:`smallDebrisDensity`
        largeDebrisDensity: :attr:`largeDebrisDensity`
        foliageDensity: :attr:`foliageDensity`
        smallDebrisCenterBias: :attr:`smallDebrisCenterBias`
        largeDebrisCenterBias: :attr:`largeDebrisCenterBias`
        foliageCenterBias: :attr:`foliageCenterBias`
        minFoliageDistance: :attr:`minFoliageDistance`
        maxFoliageDistance: :attr:`maxFoliageDistance`
        minLargeDebrisDistance: :attr:`minLargeDebrisDistance`
        maxLargeDebrisDistance: :attr:`maxLargeDebrisDistance`
        minSmallDebrisDistance: :attr:`minSmallDebrisDistance`
        maxSmallDebrisDistance: :attr:`maxSmallDebrisDistance`
        smallDebrisAssetTag: :attr:`smallDebrisAssetTag`
        largeDebrisAssetTag: :attr:`largeDebrisAssetTag`
        foliageDebrisAssetTag: :attr:`foliageDebrisAssetTag`
        smallDebrisAssetRemoveTag: :attr:`smallDebrisAssetRemoveTag`
        largeDebrisAssetRemoveTag: :attr:`largeDebrisAssetRemoveTag`
        foliageDebrisAssetRemoveTag: :attr:`foliageDebrisAssetRemoveTag`
        minHeightDebrisToPlaceAtLaneEdges: :attr:`minHeightDebrisToPlaceAtLaneEdges`
        minDistanceFromLaneEdgeForShortDebris: :attr:`minDistanceFromLaneEdgeForShortDebris`
    Attributes:
        smallDebrisDensity: generator for placing debris objects in the scene
            Default: 0.01
        largeDebrisDensity: Default: 0.01
        foliageDensity: Default: 0.01
        smallDebrisCenterBias: Default: 0.0
        largeDebrisCenterBias: Default: 0.0
        foliageCenterBias: Default: 0.0
        minFoliageDistance: Default: 0.0
        maxFoliageDistance: Default: 50.0
        minLargeDebrisDistance: Default: 0.0
        maxLargeDebrisDistance: Default: 50.0
        minSmallDebrisDistance: Default: 0.0
        maxSmallDebrisDistance: Default: 50.0
        smallDebrisAssetTag:
        largeDebrisAssetTag:
        foliageDebrisAssetTag:
        smallDebrisAssetRemoveTag:
        largeDebrisAssetRemoveTag:
        foliageDebrisAssetRemoveTag:
        minHeightDebrisToPlaceAtLaneEdges: Default: 0.1
        minDistanceFromLaneEdgeForShortDebris: Default: 0.2"""

    _proto_message = pd_spawn_pb2.DebrisScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.DebrisScenarioGeneratorInfo] = None,
        smallDebrisDensity: float = None,
        largeDebrisDensity: float = None,
        foliageDensity: float = None,
        smallDebrisCenterBias: float = None,
        largeDebrisCenterBias: float = None,
        foliageCenterBias: float = None,
        minFoliageDistance: float = None,
        maxFoliageDistance: float = None,
        minLargeDebrisDistance: float = None,
        maxLargeDebrisDistance: float = None,
        minSmallDebrisDistance: float = None,
        maxSmallDebrisDistance: float = None,
        smallDebrisAssetTag: str = None,
        largeDebrisAssetTag: str = None,
        foliageDebrisAssetTag: str = None,
        smallDebrisAssetRemoveTag: str = None,
        largeDebrisAssetRemoveTag: str = None,
        foliageDebrisAssetRemoveTag: str = None,
        minHeightDebrisToPlaceAtLaneEdges: float = None,
        minDistanceFromLaneEdgeForShortDebris: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.DebrisScenarioGeneratorInfo()
        self.proto = proto
        if smallDebrisDensity is not None:
            self.smallDebrisDensity = smallDebrisDensity
        if largeDebrisDensity is not None:
            self.largeDebrisDensity = largeDebrisDensity
        if foliageDensity is not None:
            self.foliageDensity = foliageDensity
        if smallDebrisCenterBias is not None:
            self.smallDebrisCenterBias = smallDebrisCenterBias
        if largeDebrisCenterBias is not None:
            self.largeDebrisCenterBias = largeDebrisCenterBias
        if foliageCenterBias is not None:
            self.foliageCenterBias = foliageCenterBias
        if minFoliageDistance is not None:
            self.minFoliageDistance = minFoliageDistance
        if maxFoliageDistance is not None:
            self.maxFoliageDistance = maxFoliageDistance
        if minLargeDebrisDistance is not None:
            self.minLargeDebrisDistance = minLargeDebrisDistance
        if maxLargeDebrisDistance is not None:
            self.maxLargeDebrisDistance = maxLargeDebrisDistance
        if minSmallDebrisDistance is not None:
            self.minSmallDebrisDistance = minSmallDebrisDistance
        if maxSmallDebrisDistance is not None:
            self.maxSmallDebrisDistance = maxSmallDebrisDistance
        if smallDebrisAssetTag is not None:
            self.smallDebrisAssetTag = smallDebrisAssetTag
        if largeDebrisAssetTag is not None:
            self.largeDebrisAssetTag = largeDebrisAssetTag
        if foliageDebrisAssetTag is not None:
            self.foliageDebrisAssetTag = foliageDebrisAssetTag
        if smallDebrisAssetRemoveTag is not None:
            self.smallDebrisAssetRemoveTag = smallDebrisAssetRemoveTag
        if largeDebrisAssetRemoveTag is not None:
            self.largeDebrisAssetRemoveTag = largeDebrisAssetRemoveTag
        if foliageDebrisAssetRemoveTag is not None:
            self.foliageDebrisAssetRemoveTag = foliageDebrisAssetRemoveTag
        if minHeightDebrisToPlaceAtLaneEdges is not None:
            self.minHeightDebrisToPlaceAtLaneEdges = minHeightDebrisToPlaceAtLaneEdges
        if minDistanceFromLaneEdgeForShortDebris is not None:
            self.minDistanceFromLaneEdgeForShortDebris = minDistanceFromLaneEdgeForShortDebris

    @property
    def smallDebrisDensity(self) -> float:
        return self.proto.smallDebrisDensity

    @smallDebrisDensity.setter
    def smallDebrisDensity(self, value: float):
        self.proto.smallDebrisDensity = value

    @property
    def largeDebrisDensity(self) -> float:
        return self.proto.largeDebrisDensity

    @largeDebrisDensity.setter
    def largeDebrisDensity(self, value: float):
        self.proto.largeDebrisDensity = value

    @property
    def foliageDensity(self) -> float:
        return self.proto.foliageDensity

    @foliageDensity.setter
    def foliageDensity(self, value: float):
        self.proto.foliageDensity = value

    @property
    def smallDebrisCenterBias(self) -> float:
        return self.proto.smallDebrisCenterBias

    @smallDebrisCenterBias.setter
    def smallDebrisCenterBias(self, value: float):
        self.proto.smallDebrisCenterBias = value

    @property
    def largeDebrisCenterBias(self) -> float:
        return self.proto.largeDebrisCenterBias

    @largeDebrisCenterBias.setter
    def largeDebrisCenterBias(self, value: float):
        self.proto.largeDebrisCenterBias = value

    @property
    def foliageCenterBias(self) -> float:
        return self.proto.foliageCenterBias

    @foliageCenterBias.setter
    def foliageCenterBias(self, value: float):
        self.proto.foliageCenterBias = value

    @property
    def minFoliageDistance(self) -> float:
        return self.proto.minFoliageDistance

    @minFoliageDistance.setter
    def minFoliageDistance(self, value: float):
        self.proto.minFoliageDistance = value

    @property
    def maxFoliageDistance(self) -> float:
        return self.proto.maxFoliageDistance

    @maxFoliageDistance.setter
    def maxFoliageDistance(self, value: float):
        self.proto.maxFoliageDistance = value

    @property
    def minLargeDebrisDistance(self) -> float:
        return self.proto.minLargeDebrisDistance

    @minLargeDebrisDistance.setter
    def minLargeDebrisDistance(self, value: float):
        self.proto.minLargeDebrisDistance = value

    @property
    def maxLargeDebrisDistance(self) -> float:
        return self.proto.maxLargeDebrisDistance

    @maxLargeDebrisDistance.setter
    def maxLargeDebrisDistance(self, value: float):
        self.proto.maxLargeDebrisDistance = value

    @property
    def minSmallDebrisDistance(self) -> float:
        return self.proto.minSmallDebrisDistance

    @minSmallDebrisDistance.setter
    def minSmallDebrisDistance(self, value: float):
        self.proto.minSmallDebrisDistance = value

    @property
    def maxSmallDebrisDistance(self) -> float:
        return self.proto.maxSmallDebrisDistance

    @maxSmallDebrisDistance.setter
    def maxSmallDebrisDistance(self, value: float):
        self.proto.maxSmallDebrisDistance = value

    @property
    def smallDebrisAssetTag(self) -> str:
        return self.proto.smallDebrisAssetTag

    @smallDebrisAssetTag.setter
    def smallDebrisAssetTag(self, value: str):
        self.proto.smallDebrisAssetTag = value

    @property
    def largeDebrisAssetTag(self) -> str:
        return self.proto.largeDebrisAssetTag

    @largeDebrisAssetTag.setter
    def largeDebrisAssetTag(self, value: str):
        self.proto.largeDebrisAssetTag = value

    @property
    def foliageDebrisAssetTag(self) -> str:
        return self.proto.foliageDebrisAssetTag

    @foliageDebrisAssetTag.setter
    def foliageDebrisAssetTag(self, value: str):
        self.proto.foliageDebrisAssetTag = value

    @property
    def smallDebrisAssetRemoveTag(self) -> str:
        return self.proto.smallDebrisAssetRemoveTag

    @smallDebrisAssetRemoveTag.setter
    def smallDebrisAssetRemoveTag(self, value: str):
        self.proto.smallDebrisAssetRemoveTag = value

    @property
    def largeDebrisAssetRemoveTag(self) -> str:
        return self.proto.largeDebrisAssetRemoveTag

    @largeDebrisAssetRemoveTag.setter
    def largeDebrisAssetRemoveTag(self, value: str):
        self.proto.largeDebrisAssetRemoveTag = value

    @property
    def foliageDebrisAssetRemoveTag(self) -> str:
        return self.proto.foliageDebrisAssetRemoveTag

    @foliageDebrisAssetRemoveTag.setter
    def foliageDebrisAssetRemoveTag(self, value: str):
        self.proto.foliageDebrisAssetRemoveTag = value

    @property
    def minHeightDebrisToPlaceAtLaneEdges(self) -> float:
        return self.proto.minHeightDebrisToPlaceAtLaneEdges

    @minHeightDebrisToPlaceAtLaneEdges.setter
    def minHeightDebrisToPlaceAtLaneEdges(self, value: float):
        self.proto.minHeightDebrisToPlaceAtLaneEdges = value

    @property
    def minDistanceFromLaneEdgeForShortDebris(self) -> float:
        return self.proto.minDistanceFromLaneEdgeForShortDebris

    @minDistanceFromLaneEdgeForShortDebris.setter
    def minDistanceFromLaneEdgeForShortDebris(self, value: float):
        self.proto.minDistanceFromLaneEdgeForShortDebris = value

    def _update_proto_references(self, proto: pd_spawn_pb2.DebrisScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.DrivewayScenarioGeneratorInfo)
class DrivewayScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        minDrivewayLongitudinalOffsetPercentage: :attr:`minDrivewayLongitudinalOffsetPercentage`
        maxDrivewayLongitudinalOffsetPercentage: :attr:`maxDrivewayLongitudinalOffsetPercentage`
        minDrivewayLateralOffsetPercentage: :attr:`minDrivewayLateralOffsetPercentage`
        maxDrivewayLateralOffsetPercentage: :attr:`maxDrivewayLateralOffsetPercentage`
        vehicleDepartsDrivewayProbability: :attr:`vehicleDepartsDrivewayProbability`
        minEgoSpawnDistFromDriveway: :attr:`minEgoSpawnDistFromDriveway`
        maxEgoSpawnDistFromDriveway: :attr:`maxEgoSpawnDistFromDriveway`
        drivewayVehiclesFacingRoadProbability: :attr:`drivewayVehiclesFacingRoadProbability`
        enableVehicleOcclusions: :attr:`enableVehicleOcclusions`
        enablePropOcclusions: :attr:`enablePropOcclusions`
        propOcclusionSpacingDist: :attr:`propOcclusionSpacingDist`
        propOcclusionCountDist: :attr:`propOcclusionCountDist`
        occlusionOffsetDist: :attr:`occlusionOffsetDist`
        egoSpawnLocationProbability: :attr:`egoSpawnLocationProbability`
        excludeDrivewayRoadType: :attr:`excludeDrivewayRoadType`
        excludeDrivewayParkingEntryRoadType: :attr:`excludeDrivewayParkingEntryRoadType`
        placeEgoOnClosestCrossRoadLane: :attr:`placeEgoOnClosestCrossRoadLane`
        useBrakeUntilEgoTimeToAgent: :attr:`useBrakeUntilEgoTimeToAgent`
        brakeUntilEgoTimeToAgentS: :attr:`brakeUntilEgoTimeToAgentS`
    Attributes:
        minDrivewayLongitudinalOffsetPercentage: generator for placing vehicles in driveways and driving by as they pull out.
            Default: 0.0
        maxDrivewayLongitudinalOffsetPercentage: Default: 1.0
        minDrivewayLateralOffsetPercentage: Default: 0.5
        maxDrivewayLateralOffsetPercentage: Default: 0.5
        vehicleDepartsDrivewayProbability: Default: 0.0
        minEgoSpawnDistFromDriveway: Default: 0.0
        maxEgoSpawnDistFromDriveway: Default: 20.0
        drivewayVehiclesFacingRoadProbability: Default: 1.0
        enableVehicleOcclusions: Default: False
        enablePropOcclusions: Default: False
        propOcclusionSpacingDist:
        propOcclusionCountDist:
        occlusionOffsetDist:
        egoSpawnLocationProbability:
        excludeDrivewayRoadType:
        excludeDrivewayParkingEntryRoadType:
        placeEgoOnClosestCrossRoadLane: Default: True
        useBrakeUntilEgoTimeToAgent: Default: True
        brakeUntilEgoTimeToAgentS:"""

    _proto_message = pd_spawn_pb2.DrivewayScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.DrivewayScenarioGeneratorInfo] = None,
        minDrivewayLongitudinalOffsetPercentage: float = None,
        maxDrivewayLongitudinalOffsetPercentage: float = None,
        minDrivewayLateralOffsetPercentage: float = None,
        maxDrivewayLateralOffsetPercentage: float = None,
        vehicleDepartsDrivewayProbability: float = None,
        minEgoSpawnDistFromDriveway: float = None,
        maxEgoSpawnDistFromDriveway: float = None,
        drivewayVehiclesFacingRoadProbability: float = None,
        enableVehicleOcclusions: bool = None,
        enablePropOcclusions: bool = None,
        propOcclusionSpacingDist: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        propOcclusionCountDist: _pd_unified_generator_pb2.CenterSpreadConfigInt = None,
        occlusionOffsetDist: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        egoSpawnLocationProbability: _pd_distributions_pb2.EnumDistribution = None,
        excludeDrivewayRoadType: bool = None,
        excludeDrivewayParkingEntryRoadType: bool = None,
        placeEgoOnClosestCrossRoadLane: bool = None,
        useBrakeUntilEgoTimeToAgent: bool = None,
        brakeUntilEgoTimeToAgentS: _pd_unified_generator_pb2.CenterSpreadConfig = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.DrivewayScenarioGeneratorInfo()
        self.proto = proto
        self._propOcclusionSpacingDist = get_wrapper(proto_type=proto.propOcclusionSpacingDist.__class__)(
            proto=proto.propOcclusionSpacingDist
        )
        self._propOcclusionCountDist = get_wrapper(proto_type=proto.propOcclusionCountDist.__class__)(
            proto=proto.propOcclusionCountDist
        )
        self._occlusionOffsetDist = get_wrapper(proto_type=proto.occlusionOffsetDist.__class__)(
            proto=proto.occlusionOffsetDist
        )
        self._egoSpawnLocationProbability = get_wrapper(proto_type=proto.egoSpawnLocationProbability.__class__)(
            proto=proto.egoSpawnLocationProbability
        )
        self._brakeUntilEgoTimeToAgentS = get_wrapper(proto_type=proto.brakeUntilEgoTimeToAgentS.__class__)(
            proto=proto.brakeUntilEgoTimeToAgentS
        )
        if minDrivewayLongitudinalOffsetPercentage is not None:
            self.minDrivewayLongitudinalOffsetPercentage = minDrivewayLongitudinalOffsetPercentage
        if maxDrivewayLongitudinalOffsetPercentage is not None:
            self.maxDrivewayLongitudinalOffsetPercentage = maxDrivewayLongitudinalOffsetPercentage
        if minDrivewayLateralOffsetPercentage is not None:
            self.minDrivewayLateralOffsetPercentage = minDrivewayLateralOffsetPercentage
        if maxDrivewayLateralOffsetPercentage is not None:
            self.maxDrivewayLateralOffsetPercentage = maxDrivewayLateralOffsetPercentage
        if vehicleDepartsDrivewayProbability is not None:
            self.vehicleDepartsDrivewayProbability = vehicleDepartsDrivewayProbability
        if minEgoSpawnDistFromDriveway is not None:
            self.minEgoSpawnDistFromDriveway = minEgoSpawnDistFromDriveway
        if maxEgoSpawnDistFromDriveway is not None:
            self.maxEgoSpawnDistFromDriveway = maxEgoSpawnDistFromDriveway
        if drivewayVehiclesFacingRoadProbability is not None:
            self.drivewayVehiclesFacingRoadProbability = drivewayVehiclesFacingRoadProbability
        if enableVehicleOcclusions is not None:
            self.enableVehicleOcclusions = enableVehicleOcclusions
        if enablePropOcclusions is not None:
            self.enablePropOcclusions = enablePropOcclusions
        if propOcclusionSpacingDist is not None:
            self.propOcclusionSpacingDist = propOcclusionSpacingDist
        if propOcclusionCountDist is not None:
            self.propOcclusionCountDist = propOcclusionCountDist
        if occlusionOffsetDist is not None:
            self.occlusionOffsetDist = occlusionOffsetDist
        if egoSpawnLocationProbability is not None:
            self.egoSpawnLocationProbability = egoSpawnLocationProbability
        if excludeDrivewayRoadType is not None:
            self.excludeDrivewayRoadType = excludeDrivewayRoadType
        if excludeDrivewayParkingEntryRoadType is not None:
            self.excludeDrivewayParkingEntryRoadType = excludeDrivewayParkingEntryRoadType
        if placeEgoOnClosestCrossRoadLane is not None:
            self.placeEgoOnClosestCrossRoadLane = placeEgoOnClosestCrossRoadLane
        if useBrakeUntilEgoTimeToAgent is not None:
            self.useBrakeUntilEgoTimeToAgent = useBrakeUntilEgoTimeToAgent
        if brakeUntilEgoTimeToAgentS is not None:
            self.brakeUntilEgoTimeToAgentS = brakeUntilEgoTimeToAgentS

    @property
    def minDrivewayLongitudinalOffsetPercentage(self) -> float:
        return self.proto.minDrivewayLongitudinalOffsetPercentage

    @minDrivewayLongitudinalOffsetPercentage.setter
    def minDrivewayLongitudinalOffsetPercentage(self, value: float):
        self.proto.minDrivewayLongitudinalOffsetPercentage = value

    @property
    def maxDrivewayLongitudinalOffsetPercentage(self) -> float:
        return self.proto.maxDrivewayLongitudinalOffsetPercentage

    @maxDrivewayLongitudinalOffsetPercentage.setter
    def maxDrivewayLongitudinalOffsetPercentage(self, value: float):
        self.proto.maxDrivewayLongitudinalOffsetPercentage = value

    @property
    def minDrivewayLateralOffsetPercentage(self) -> float:
        return self.proto.minDrivewayLateralOffsetPercentage

    @minDrivewayLateralOffsetPercentage.setter
    def minDrivewayLateralOffsetPercentage(self, value: float):
        self.proto.minDrivewayLateralOffsetPercentage = value

    @property
    def maxDrivewayLateralOffsetPercentage(self) -> float:
        return self.proto.maxDrivewayLateralOffsetPercentage

    @maxDrivewayLateralOffsetPercentage.setter
    def maxDrivewayLateralOffsetPercentage(self, value: float):
        self.proto.maxDrivewayLateralOffsetPercentage = value

    @property
    def vehicleDepartsDrivewayProbability(self) -> float:
        return self.proto.vehicleDepartsDrivewayProbability

    @vehicleDepartsDrivewayProbability.setter
    def vehicleDepartsDrivewayProbability(self, value: float):
        self.proto.vehicleDepartsDrivewayProbability = value

    @property
    def minEgoSpawnDistFromDriveway(self) -> float:
        return self.proto.minEgoSpawnDistFromDriveway

    @minEgoSpawnDistFromDriveway.setter
    def minEgoSpawnDistFromDriveway(self, value: float):
        self.proto.minEgoSpawnDistFromDriveway = value

    @property
    def maxEgoSpawnDistFromDriveway(self) -> float:
        return self.proto.maxEgoSpawnDistFromDriveway

    @maxEgoSpawnDistFromDriveway.setter
    def maxEgoSpawnDistFromDriveway(self, value: float):
        self.proto.maxEgoSpawnDistFromDriveway = value

    @property
    def drivewayVehiclesFacingRoadProbability(self) -> float:
        return self.proto.drivewayVehiclesFacingRoadProbability

    @drivewayVehiclesFacingRoadProbability.setter
    def drivewayVehiclesFacingRoadProbability(self, value: float):
        self.proto.drivewayVehiclesFacingRoadProbability = value

    @property
    def enableVehicleOcclusions(self) -> bool:
        return self.proto.enableVehicleOcclusions

    @enableVehicleOcclusions.setter
    def enableVehicleOcclusions(self, value: bool):
        self.proto.enableVehicleOcclusions = value

    @property
    def enablePropOcclusions(self) -> bool:
        return self.proto.enablePropOcclusions

    @enablePropOcclusions.setter
    def enablePropOcclusions(self, value: bool):
        self.proto.enablePropOcclusions = value

    @property
    def propOcclusionSpacingDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._propOcclusionSpacingDist

    @propOcclusionSpacingDist.setter
    def propOcclusionSpacingDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.propOcclusionSpacingDist.CopyFrom(value.proto)

        self._propOcclusionSpacingDist = value
        self._propOcclusionSpacingDist._update_proto_references(self.proto.propOcclusionSpacingDist)

    @property
    def propOcclusionCountDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._propOcclusionCountDist

    @propOcclusionCountDist.setter
    def propOcclusionCountDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self.proto.propOcclusionCountDist.CopyFrom(value.proto)

        self._propOcclusionCountDist = value
        self._propOcclusionCountDist._update_proto_references(self.proto.propOcclusionCountDist)

    @property
    def occlusionOffsetDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._occlusionOffsetDist

    @occlusionOffsetDist.setter
    def occlusionOffsetDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.occlusionOffsetDist.CopyFrom(value.proto)

        self._occlusionOffsetDist = value
        self._occlusionOffsetDist._update_proto_references(self.proto.occlusionOffsetDist)

    @property
    def egoSpawnLocationProbability(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._egoSpawnLocationProbability

    @egoSpawnLocationProbability.setter
    def egoSpawnLocationProbability(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.egoSpawnLocationProbability.CopyFrom(value.proto)

        self._egoSpawnLocationProbability = value
        self._egoSpawnLocationProbability._update_proto_references(self.proto.egoSpawnLocationProbability)

    @property
    def excludeDrivewayRoadType(self) -> bool:
        return self.proto.excludeDrivewayRoadType

    @excludeDrivewayRoadType.setter
    def excludeDrivewayRoadType(self, value: bool):
        self.proto.excludeDrivewayRoadType = value

    @property
    def excludeDrivewayParkingEntryRoadType(self) -> bool:
        return self.proto.excludeDrivewayParkingEntryRoadType

    @excludeDrivewayParkingEntryRoadType.setter
    def excludeDrivewayParkingEntryRoadType(self, value: bool):
        self.proto.excludeDrivewayParkingEntryRoadType = value

    @property
    def placeEgoOnClosestCrossRoadLane(self) -> bool:
        return self.proto.placeEgoOnClosestCrossRoadLane

    @placeEgoOnClosestCrossRoadLane.setter
    def placeEgoOnClosestCrossRoadLane(self, value: bool):
        self.proto.placeEgoOnClosestCrossRoadLane = value

    @property
    def useBrakeUntilEgoTimeToAgent(self) -> bool:
        return self.proto.useBrakeUntilEgoTimeToAgent

    @useBrakeUntilEgoTimeToAgent.setter
    def useBrakeUntilEgoTimeToAgent(self, value: bool):
        self.proto.useBrakeUntilEgoTimeToAgent = value

    @property
    def brakeUntilEgoTimeToAgentS(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._brakeUntilEgoTimeToAgentS

    @brakeUntilEgoTimeToAgentS.setter
    def brakeUntilEgoTimeToAgentS(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.brakeUntilEgoTimeToAgentS.CopyFrom(value.proto)

        self._brakeUntilEgoTimeToAgentS = value
        self._brakeUntilEgoTimeToAgentS._update_proto_references(self.proto.brakeUntilEgoTimeToAgentS)

    def _update_proto_references(self, proto: pd_spawn_pb2.DrivewayScenarioGeneratorInfo):
        self.proto = proto
        self._propOcclusionSpacingDist._update_proto_references(proto.propOcclusionSpacingDist)
        self._propOcclusionCountDist._update_proto_references(proto.propOcclusionCountDist)
        self._occlusionOffsetDist._update_proto_references(proto.occlusionOffsetDist)
        self._egoSpawnLocationProbability._update_proto_references(proto.egoSpawnLocationProbability)
        self._brakeUntilEgoTimeToAgentS._update_proto_references(proto.brakeUntilEgoTimeToAgentS)


@register_wrapper(proto_type=pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo)
class AllVehicleTestScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        leftOfEgo: :attr:`leftOfEgo`
        rightOfEgo: :attr:`rightOfEgo`
        renderVehiclesBehindEgo: :attr:`renderVehiclesBehindEgo`
        egoSpeed: :attr:`egoSpeed`
        egoStart_t: :attr:`egoStart_t`
        testVehiclesSpeed: :attr:`testVehiclesSpeed`
        startSeparationS: :attr:`startSeparationS`
        vehicleExclusionList: :attr:`vehicleExclusionList`
        includeOnlyVehiclesInExclusionList: :attr:`includeOnlyVehiclesInExclusionList`
        scenarioType: :attr:`scenarioType`
        assetIncludeList: :attr:`assetIncludeList`
        assetExcludeList: :attr:`assetExcludeList`
        excludeStaticVehicles: :attr:`excludeStaticVehicles`
        excludeMovingVehicles: :attr:`excludeMovingVehicles`
        articulatedTrailerTest: :attr:`articulatedTrailerTest`
    Attributes:
        leftOfEgo: Default: True
        rightOfEgo: Default: True
        renderVehiclesBehindEgo: Default: True
        egoSpeed: Default: 15.0
        egoStart_t: Default: 1.0
        testVehiclesSpeed: Default: 2.0
        startSeparationS: Default: 0.0
        vehicleExclusionList:
        includeOnlyVehiclesInExclusionList: Default: 0
        scenarioType: Default: 0
        assetIncludeList:
        assetExcludeList:
        excludeStaticVehicles: Default: False
        excludeMovingVehicles: Default: False
        articulatedTrailerTest: option to render all articulated trailers specified by the include/exclude options
            trailers will spawn attached to ego vehicle model specified in spawn config
            setting this to true will prevent spawning of moving non trailers and non towing vehicles
            excludeMovingVehicles needs to be false
            Default: False"""

    _proto_message = pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo] = None,
        leftOfEgo: bool = None,
        rightOfEgo: bool = None,
        renderVehiclesBehindEgo: bool = None,
        egoSpeed: float = None,
        egoStart_t: float = None,
        testVehiclesSpeed: float = None,
        startSeparationS: float = None,
        vehicleExclusionList: List[str] = None,
        includeOnlyVehiclesInExclusionList: int = None,
        scenarioType: int = None,
        assetIncludeList: List[str] = None,
        assetExcludeList: List[str] = None,
        excludeStaticVehicles: bool = None,
        excludeMovingVehicles: bool = None,
        articulatedTrailerTest: bool = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo()
        self.proto = proto
        if leftOfEgo is not None:
            self.leftOfEgo = leftOfEgo
        if rightOfEgo is not None:
            self.rightOfEgo = rightOfEgo
        if renderVehiclesBehindEgo is not None:
            self.renderVehiclesBehindEgo = renderVehiclesBehindEgo
        if egoSpeed is not None:
            self.egoSpeed = egoSpeed
        if egoStart_t is not None:
            self.egoStart_t = egoStart_t
        if testVehiclesSpeed is not None:
            self.testVehiclesSpeed = testVehiclesSpeed
        if startSeparationS is not None:
            self.startSeparationS = startSeparationS
        self._vehicleExclusionList = ProtoListWrapper(
            container=[str(v) for v in proto.vehicleExclusionList], attr_name="vehicleExclusionList", list_owner=self
        )
        if vehicleExclusionList is not None:
            self.vehicleExclusionList = vehicleExclusionList
        if includeOnlyVehiclesInExclusionList is not None:
            self.includeOnlyVehiclesInExclusionList = includeOnlyVehiclesInExclusionList
        if scenarioType is not None:
            self.scenarioType = scenarioType
        self._assetIncludeList = ProtoListWrapper(
            container=[str(v) for v in proto.assetIncludeList], attr_name="assetIncludeList", list_owner=self
        )
        if assetIncludeList is not None:
            self.assetIncludeList = assetIncludeList
        self._assetExcludeList = ProtoListWrapper(
            container=[str(v) for v in proto.assetExcludeList], attr_name="assetExcludeList", list_owner=self
        )
        if assetExcludeList is not None:
            self.assetExcludeList = assetExcludeList
        if excludeStaticVehicles is not None:
            self.excludeStaticVehicles = excludeStaticVehicles
        if excludeMovingVehicles is not None:
            self.excludeMovingVehicles = excludeMovingVehicles
        if articulatedTrailerTest is not None:
            self.articulatedTrailerTest = articulatedTrailerTest

    @property
    def leftOfEgo(self) -> bool:
        return self.proto.leftOfEgo

    @leftOfEgo.setter
    def leftOfEgo(self, value: bool):
        self.proto.leftOfEgo = value

    @property
    def rightOfEgo(self) -> bool:
        return self.proto.rightOfEgo

    @rightOfEgo.setter
    def rightOfEgo(self, value: bool):
        self.proto.rightOfEgo = value

    @property
    def renderVehiclesBehindEgo(self) -> bool:
        return self.proto.renderVehiclesBehindEgo

    @renderVehiclesBehindEgo.setter
    def renderVehiclesBehindEgo(self, value: bool):
        self.proto.renderVehiclesBehindEgo = value

    @property
    def egoSpeed(self) -> float:
        return self.proto.egoSpeed

    @egoSpeed.setter
    def egoSpeed(self, value: float):
        self.proto.egoSpeed = value

    @property
    def egoStart_t(self) -> float:
        return self.proto.egoStart_t

    @egoStart_t.setter
    def egoStart_t(self, value: float):
        self.proto.egoStart_t = value

    @property
    def testVehiclesSpeed(self) -> float:
        return self.proto.testVehiclesSpeed

    @testVehiclesSpeed.setter
    def testVehiclesSpeed(self, value: float):
        self.proto.testVehiclesSpeed = value

    @property
    def startSeparationS(self) -> float:
        return self.proto.startSeparationS

    @startSeparationS.setter
    def startSeparationS(self, value: float):
        self.proto.startSeparationS = value

    @property
    def vehicleExclusionList(self) -> List[str]:
        return self._vehicleExclusionList

    @vehicleExclusionList.setter
    def vehicleExclusionList(self, value: List[str]):
        self._vehicleExclusionList.clear()
        for v in value:
            self._vehicleExclusionList.append(v)

    @property
    def includeOnlyVehiclesInExclusionList(self) -> int:
        return self.proto.includeOnlyVehiclesInExclusionList

    @includeOnlyVehiclesInExclusionList.setter
    def includeOnlyVehiclesInExclusionList(self, value: int):
        self.proto.includeOnlyVehiclesInExclusionList = value

    @property
    def scenarioType(self) -> int:
        return self.proto.scenarioType

    @scenarioType.setter
    def scenarioType(self, value: int):
        self.proto.scenarioType = value

    @property
    def assetIncludeList(self) -> List[str]:
        return self._assetIncludeList

    @assetIncludeList.setter
    def assetIncludeList(self, value: List[str]):
        self._assetIncludeList.clear()
        for v in value:
            self._assetIncludeList.append(v)

    @property
    def assetExcludeList(self) -> List[str]:
        return self._assetExcludeList

    @assetExcludeList.setter
    def assetExcludeList(self, value: List[str]):
        self._assetExcludeList.clear()
        for v in value:
            self._assetExcludeList.append(v)

    @property
    def excludeStaticVehicles(self) -> bool:
        return self.proto.excludeStaticVehicles

    @excludeStaticVehicles.setter
    def excludeStaticVehicles(self, value: bool):
        self.proto.excludeStaticVehicles = value

    @property
    def excludeMovingVehicles(self) -> bool:
        return self.proto.excludeMovingVehicles

    @excludeMovingVehicles.setter
    def excludeMovingVehicles(self, value: bool):
        self.proto.excludeMovingVehicles = value

    @property
    def articulatedTrailerTest(self) -> bool:
        return self.proto.articulatedTrailerTest

    @articulatedTrailerTest.setter
    def articulatedTrailerTest(self, value: bool):
        self.proto.articulatedTrailerTest = value

    def _update_proto_references(self, proto: pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.CurveScenarioGeneratorInfo)
class CurveScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        minCurvature: :attr:`minCurvature`
        maxCurvature: :attr:`maxCurvature`
        minSectionLength: :attr:`minSectionLength`
        minLongitudinalOffset: :attr:`minLongitudinalOffset`
        maxLongitudinalOffset: :attr:`maxLongitudinalOffset`
        placeOccluders: :attr:`placeOccluders`
        occludedVehicleType: :attr:`occludedVehicleType`
    Attributes:
        minCurvature: Default: 0.001
        maxCurvature: Default: 0.1
        minSectionLength: Default: 5.0
        minLongitudinalOffset: Default: -50.0
        maxLongitudinalOffset: Default: -20.0
        placeOccluders: Default: True
        occludedVehicleType: Default: :attr:`VehicleType.UNDEFINED`"""

    _proto_message = pd_spawn_pb2.CurveScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.CurveScenarioGeneratorInfo] = None,
        minCurvature: float = None,
        maxCurvature: float = None,
        minSectionLength: float = None,
        minLongitudinalOffset: float = None,
        maxLongitudinalOffset: float = None,
        placeOccluders: bool = None,
        occludedVehicleType: VehicleType = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.CurveScenarioGeneratorInfo()
        self.proto = proto
        if minCurvature is not None:
            self.minCurvature = minCurvature
        if maxCurvature is not None:
            self.maxCurvature = maxCurvature
        if minSectionLength is not None:
            self.minSectionLength = minSectionLength
        if minLongitudinalOffset is not None:
            self.minLongitudinalOffset = minLongitudinalOffset
        if maxLongitudinalOffset is not None:
            self.maxLongitudinalOffset = maxLongitudinalOffset
        if placeOccluders is not None:
            self.placeOccluders = placeOccluders
        if occludedVehicleType is not None:
            self.occludedVehicleType = occludedVehicleType

    @property
    def minCurvature(self) -> float:
        return self.proto.minCurvature

    @minCurvature.setter
    def minCurvature(self, value: float):
        self.proto.minCurvature = value

    @property
    def maxCurvature(self) -> float:
        return self.proto.maxCurvature

    @maxCurvature.setter
    def maxCurvature(self, value: float):
        self.proto.maxCurvature = value

    @property
    def minSectionLength(self) -> float:
        return self.proto.minSectionLength

    @minSectionLength.setter
    def minSectionLength(self, value: float):
        self.proto.minSectionLength = value

    @property
    def minLongitudinalOffset(self) -> float:
        return self.proto.minLongitudinalOffset

    @minLongitudinalOffset.setter
    def minLongitudinalOffset(self, value: float):
        self.proto.minLongitudinalOffset = value

    @property
    def maxLongitudinalOffset(self) -> float:
        return self.proto.maxLongitudinalOffset

    @maxLongitudinalOffset.setter
    def maxLongitudinalOffset(self, value: float):
        self.proto.maxLongitudinalOffset = value

    @property
    def placeOccluders(self) -> bool:
        return self.proto.placeOccluders

    @placeOccluders.setter
    def placeOccluders(self, value: bool):
        self.proto.placeOccluders = value

    @property
    def occludedVehicleType(self) -> VehicleType:
        return self.proto.occludedVehicleType

    @occludedVehicleType.setter
    def occludedVehicleType(self, value: VehicleType):
        self.proto.occludedVehicleType = value

    def _update_proto_references(self, proto: pd_spawn_pb2.CurveScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.ParkingScenarioGeneratorInfo)
class ParkingScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        parkingTypeDistribution: :attr:`parkingTypeDistribution`
        egoParkPerturbationAngle: :attr:`egoParkPerturbationAngle`
        egoParkPerturbationLongitudinalOffset: :attr:`egoParkPerturbationLongitudinalOffset`
        egoParkPerturbationLateralOffset: :attr:`egoParkPerturbationLateralOffset`
        pullOutProbability: :attr:`pullOutProbability`
        noseInProbability: :attr:`noseInProbability`
        timeToParkingSpace: :attr:`timeToParkingSpace`
        parkingSpacePedestrianDensity: :attr:`parkingSpacePedestrianDensity`
        maxPedsInParkingSpaces: :attr:`maxPedsInParkingSpaces`
        aisleLateralOffsetNoseIn: :attr:`aisleLateralOffsetNoseIn`
        aisleLateralOffsetBackIn: :attr:`aisleLateralOffsetBackIn`
        exitAfterParking: :attr:`exitAfterParking`
        exitStraight: :attr:`exitStraight`
        placeVehicleInFrontOfParallelSpot: :attr:`placeVehicleInFrontOfParallelSpot`
        perpendicularOnRoadProbability: :attr:`perpendicularOnRoadProbability`
    Attributes:
        parkingTypeDistribution:
        egoParkPerturbationAngle:
        egoParkPerturbationLongitudinalOffset:
        egoParkPerturbationLateralOffset:
        pullOutProbability:
        noseInProbability:
        timeToParkingSpace:
        parkingSpacePedestrianDensity:
        maxPedsInParkingSpaces: Default: 50
        aisleLateralOffsetNoseIn:
        aisleLateralOffsetBackIn:
        exitAfterParking: Default: False
        exitStraight: Default: False
        placeVehicleInFrontOfParallelSpot: Default: False
        perpendicularOnRoadProbability: Default: 0.5"""

    _proto_message = pd_spawn_pb2.ParkingScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.ParkingScenarioGeneratorInfo] = None,
        parkingTypeDistribution: _pd_distributions_pb2.EnumDistribution = None,
        egoParkPerturbationAngle: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        egoParkPerturbationLongitudinalOffset: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        egoParkPerturbationLateralOffset: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        pullOutProbability: float = None,
        noseInProbability: float = None,
        timeToParkingSpace: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        parkingSpacePedestrianDensity: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        maxPedsInParkingSpaces: int = None,
        aisleLateralOffsetNoseIn: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        aisleLateralOffsetBackIn: _pd_unified_generator_pb2.CenterSpreadConfig = None,
        exitAfterParking: bool = None,
        exitStraight: bool = None,
        placeVehicleInFrontOfParallelSpot: bool = None,
        perpendicularOnRoadProbability: float = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.ParkingScenarioGeneratorInfo()
        self.proto = proto
        self._parkingTypeDistribution = get_wrapper(proto_type=proto.parkingTypeDistribution.__class__)(
            proto=proto.parkingTypeDistribution
        )
        self._egoParkPerturbationAngle = get_wrapper(proto_type=proto.egoParkPerturbationAngle.__class__)(
            proto=proto.egoParkPerturbationAngle
        )
        self._egoParkPerturbationLongitudinalOffset = get_wrapper(
            proto_type=proto.egoParkPerturbationLongitudinalOffset.__class__
        )(proto=proto.egoParkPerturbationLongitudinalOffset)
        self._egoParkPerturbationLateralOffset = get_wrapper(
            proto_type=proto.egoParkPerturbationLateralOffset.__class__
        )(proto=proto.egoParkPerturbationLateralOffset)
        self._timeToParkingSpace = get_wrapper(proto_type=proto.timeToParkingSpace.__class__)(
            proto=proto.timeToParkingSpace
        )
        self._parkingSpacePedestrianDensity = get_wrapper(proto_type=proto.parkingSpacePedestrianDensity.__class__)(
            proto=proto.parkingSpacePedestrianDensity
        )
        self._aisleLateralOffsetNoseIn = get_wrapper(proto_type=proto.aisleLateralOffsetNoseIn.__class__)(
            proto=proto.aisleLateralOffsetNoseIn
        )
        self._aisleLateralOffsetBackIn = get_wrapper(proto_type=proto.aisleLateralOffsetBackIn.__class__)(
            proto=proto.aisleLateralOffsetBackIn
        )
        if parkingTypeDistribution is not None:
            self.parkingTypeDistribution = parkingTypeDistribution
        if egoParkPerturbationAngle is not None:
            self.egoParkPerturbationAngle = egoParkPerturbationAngle
        if egoParkPerturbationLongitudinalOffset is not None:
            self.egoParkPerturbationLongitudinalOffset = egoParkPerturbationLongitudinalOffset
        if egoParkPerturbationLateralOffset is not None:
            self.egoParkPerturbationLateralOffset = egoParkPerturbationLateralOffset
        if pullOutProbability is not None:
            self.pullOutProbability = pullOutProbability
        if noseInProbability is not None:
            self.noseInProbability = noseInProbability
        if timeToParkingSpace is not None:
            self.timeToParkingSpace = timeToParkingSpace
        if parkingSpacePedestrianDensity is not None:
            self.parkingSpacePedestrianDensity = parkingSpacePedestrianDensity
        if maxPedsInParkingSpaces is not None:
            self.maxPedsInParkingSpaces = maxPedsInParkingSpaces
        if aisleLateralOffsetNoseIn is not None:
            self.aisleLateralOffsetNoseIn = aisleLateralOffsetNoseIn
        if aisleLateralOffsetBackIn is not None:
            self.aisleLateralOffsetBackIn = aisleLateralOffsetBackIn
        if exitAfterParking is not None:
            self.exitAfterParking = exitAfterParking
        if exitStraight is not None:
            self.exitStraight = exitStraight
        if placeVehicleInFrontOfParallelSpot is not None:
            self.placeVehicleInFrontOfParallelSpot = placeVehicleInFrontOfParallelSpot
        if perpendicularOnRoadProbability is not None:
            self.perpendicularOnRoadProbability = perpendicularOnRoadProbability

    @property
    def parkingTypeDistribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._parkingTypeDistribution

    @parkingTypeDistribution.setter
    def parkingTypeDistribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self.proto.parkingTypeDistribution.CopyFrom(value.proto)

        self._parkingTypeDistribution = value
        self._parkingTypeDistribution._update_proto_references(self.proto.parkingTypeDistribution)

    @property
    def egoParkPerturbationAngle(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationAngle

    @egoParkPerturbationAngle.setter
    def egoParkPerturbationAngle(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.egoParkPerturbationAngle.CopyFrom(value.proto)

        self._egoParkPerturbationAngle = value
        self._egoParkPerturbationAngle._update_proto_references(self.proto.egoParkPerturbationAngle)

    @property
    def egoParkPerturbationLongitudinalOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationLongitudinalOffset

    @egoParkPerturbationLongitudinalOffset.setter
    def egoParkPerturbationLongitudinalOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.egoParkPerturbationLongitudinalOffset.CopyFrom(value.proto)

        self._egoParkPerturbationLongitudinalOffset = value
        self._egoParkPerturbationLongitudinalOffset._update_proto_references(
            self.proto.egoParkPerturbationLongitudinalOffset
        )

    @property
    def egoParkPerturbationLateralOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationLateralOffset

    @egoParkPerturbationLateralOffset.setter
    def egoParkPerturbationLateralOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.egoParkPerturbationLateralOffset.CopyFrom(value.proto)

        self._egoParkPerturbationLateralOffset = value
        self._egoParkPerturbationLateralOffset._update_proto_references(self.proto.egoParkPerturbationLateralOffset)

    @property
    def pullOutProbability(self) -> float:
        return self.proto.pullOutProbability

    @pullOutProbability.setter
    def pullOutProbability(self, value: float):
        self.proto.pullOutProbability = value

    @property
    def noseInProbability(self) -> float:
        return self.proto.noseInProbability

    @noseInProbability.setter
    def noseInProbability(self, value: float):
        self.proto.noseInProbability = value

    @property
    def timeToParkingSpace(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._timeToParkingSpace

    @timeToParkingSpace.setter
    def timeToParkingSpace(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.timeToParkingSpace.CopyFrom(value.proto)

        self._timeToParkingSpace = value
        self._timeToParkingSpace._update_proto_references(self.proto.timeToParkingSpace)

    @property
    def parkingSpacePedestrianDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._parkingSpacePedestrianDensity

    @parkingSpacePedestrianDensity.setter
    def parkingSpacePedestrianDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.parkingSpacePedestrianDensity.CopyFrom(value.proto)

        self._parkingSpacePedestrianDensity = value
        self._parkingSpacePedestrianDensity._update_proto_references(self.proto.parkingSpacePedestrianDensity)

    @property
    def maxPedsInParkingSpaces(self) -> int:
        return self.proto.maxPedsInParkingSpaces

    @maxPedsInParkingSpaces.setter
    def maxPedsInParkingSpaces(self, value: int):
        self.proto.maxPedsInParkingSpaces = value

    @property
    def aisleLateralOffsetNoseIn(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._aisleLateralOffsetNoseIn

    @aisleLateralOffsetNoseIn.setter
    def aisleLateralOffsetNoseIn(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.aisleLateralOffsetNoseIn.CopyFrom(value.proto)

        self._aisleLateralOffsetNoseIn = value
        self._aisleLateralOffsetNoseIn._update_proto_references(self.proto.aisleLateralOffsetNoseIn)

    @property
    def aisleLateralOffsetBackIn(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._aisleLateralOffsetBackIn

    @aisleLateralOffsetBackIn.setter
    def aisleLateralOffsetBackIn(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self.proto.aisleLateralOffsetBackIn.CopyFrom(value.proto)

        self._aisleLateralOffsetBackIn = value
        self._aisleLateralOffsetBackIn._update_proto_references(self.proto.aisleLateralOffsetBackIn)

    @property
    def exitAfterParking(self) -> bool:
        return self.proto.exitAfterParking

    @exitAfterParking.setter
    def exitAfterParking(self, value: bool):
        self.proto.exitAfterParking = value

    @property
    def exitStraight(self) -> bool:
        return self.proto.exitStraight

    @exitStraight.setter
    def exitStraight(self, value: bool):
        self.proto.exitStraight = value

    @property
    def placeVehicleInFrontOfParallelSpot(self) -> bool:
        return self.proto.placeVehicleInFrontOfParallelSpot

    @placeVehicleInFrontOfParallelSpot.setter
    def placeVehicleInFrontOfParallelSpot(self, value: bool):
        self.proto.placeVehicleInFrontOfParallelSpot = value

    @property
    def perpendicularOnRoadProbability(self) -> float:
        return self.proto.perpendicularOnRoadProbability

    @perpendicularOnRoadProbability.setter
    def perpendicularOnRoadProbability(self, value: float):
        self.proto.perpendicularOnRoadProbability = value

    def _update_proto_references(self, proto: pd_spawn_pb2.ParkingScenarioGeneratorInfo):
        self.proto = proto
        self._parkingTypeDistribution._update_proto_references(proto.parkingTypeDistribution)
        self._egoParkPerturbationAngle._update_proto_references(proto.egoParkPerturbationAngle)
        self._egoParkPerturbationLongitudinalOffset._update_proto_references(
            proto.egoParkPerturbationLongitudinalOffset
        )
        self._egoParkPerturbationLateralOffset._update_proto_references(proto.egoParkPerturbationLateralOffset)
        self._timeToParkingSpace._update_proto_references(proto.timeToParkingSpace)
        self._parkingSpacePedestrianDensity._update_proto_references(proto.parkingSpacePedestrianDensity)
        self._aisleLateralOffsetNoseIn._update_proto_references(proto.aisleLateralOffsetNoseIn)
        self._aisleLateralOffsetBackIn._update_proto_references(proto.aisleLateralOffsetBackIn)


@register_wrapper(proto_type=pd_spawn_pb2.DroneFlightScenarioGeneratorInfo)
class DroneFlightScenarioGeneratorInfo(ProtoMessageClass):
    """
    Args:
        maxRadiusFromTarget: :attr:`maxRadiusFromTarget`
        descentPathName: :attr:`descentPathName`
    Attributes:
        maxRadiusFromTarget:
        descentPathName:"""

    _proto_message = pd_spawn_pb2.DroneFlightScenarioGeneratorInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.DroneFlightScenarioGeneratorInfo] = None,
        maxRadiusFromTarget: float = None,
        descentPathName: str = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.DroneFlightScenarioGeneratorInfo()
        self.proto = proto
        if maxRadiusFromTarget is not None:
            self.maxRadiusFromTarget = maxRadiusFromTarget
        if descentPathName is not None:
            self.descentPathName = descentPathName

    @property
    def maxRadiusFromTarget(self) -> float:
        return self.proto.maxRadiusFromTarget

    @maxRadiusFromTarget.setter
    def maxRadiusFromTarget(self, value: float):
        self.proto.maxRadiusFromTarget = value

    @property
    def descentPathName(self) -> str:
        return self.proto.descentPathName

    @descentPathName.setter
    def descentPathName(self, value: str):
        self.proto.descentPathName = value

    def _update_proto_references(self, proto: pd_spawn_pb2.DroneFlightScenarioGeneratorInfo):
        self.proto = proto


@register_wrapper(proto_type=pd_spawn_pb2.GeneratorConfigPreset)
class GeneratorConfigPreset(ProtoMessageClass):
    """Config wrapper

    Args:
        random_generator: :attr:`random_generator`
        junction_generator: :attr:`junction_generator`
        voi_generator: :attr:`voi_generator`
        kitti_generator: :attr:`kitti_generator`
        position_generator: :attr:`position_generator`
        lane_generator: :attr:`lane_generator`
        static_cam_generator: :attr:`static_cam_generator`
        jaywalking_generator: :attr:`jaywalking_generator`
        prop_generator: :attr:`prop_generator`
        debris_generator: :attr:`debris_generator`
        driveway_generator: :attr:`driveway_generator`
        all_vehicle_test_generator: :attr:`all_vehicle_test_generator`
        curve_generator: :attr:`curve_generator`
        parking_generator: :attr:`parking_generator`
        drone_generator: :attr:`drone_generator`
        unified_generator: :attr:`unified_generator`
    Attributes:
        random_generator:
        junction_generator:
        voi_generator:
        kitti_generator:
        position_generator:
        lane_generator:
        static_cam_generator:
        jaywalking_generator:
        prop_generator:
        debris_generator:
        driveway_generator:
        all_vehicle_test_generator:
        curve_generator:
        parking_generator:
        drone_generator:
        unified_generator:"""

    _proto_message = pd_spawn_pb2.GeneratorConfigPreset

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.GeneratorConfigPreset] = None,
        random_generator: RandomLaneScenarioGeneratorInfo = None,
        junction_generator: JunctionScenarioGeneratorInfo = None,
        voi_generator: VehicleOfInterestScenarioGeneratorInfo = None,
        kitti_generator: KittiScenarioGeneratorInfo = None,
        position_generator: VehiclePositionScenarioGeneratorInfo = None,
        lane_generator: LaneTypeScenarioGeneratorInfo = None,
        static_cam_generator: StaticCamScenarioGeneratorInfo = None,
        jaywalking_generator: JaywalkingScenarioGeneratorInfo = None,
        prop_generator: PropScenarioGeneratorInfo = None,
        debris_generator: DebrisScenarioGeneratorInfo = None,
        driveway_generator: DrivewayScenarioGeneratorInfo = None,
        all_vehicle_test_generator: AllVehicleTestScenarioGeneratorInfo = None,
        curve_generator: CurveScenarioGeneratorInfo = None,
        parking_generator: ParkingScenarioGeneratorInfo = None,
        drone_generator: DroneFlightScenarioGeneratorInfo = None,
        unified_generator: _pd_unified_generator_pb2.UnifiedGeneratorParameters = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.GeneratorConfigPreset()
        self.proto = proto
        self._random_generator = get_wrapper(proto_type=proto.random_generator.__class__)(proto=proto.random_generator)
        self._junction_generator = get_wrapper(proto_type=proto.junction_generator.__class__)(
            proto=proto.junction_generator
        )
        self._voi_generator = get_wrapper(proto_type=proto.voi_generator.__class__)(proto=proto.voi_generator)
        self._kitti_generator = get_wrapper(proto_type=proto.kitti_generator.__class__)(proto=proto.kitti_generator)
        self._position_generator = get_wrapper(proto_type=proto.position_generator.__class__)(
            proto=proto.position_generator
        )
        self._lane_generator = get_wrapper(proto_type=proto.lane_generator.__class__)(proto=proto.lane_generator)
        self._static_cam_generator = get_wrapper(proto_type=proto.static_cam_generator.__class__)(
            proto=proto.static_cam_generator
        )
        self._jaywalking_generator = get_wrapper(proto_type=proto.jaywalking_generator.__class__)(
            proto=proto.jaywalking_generator
        )
        self._prop_generator = get_wrapper(proto_type=proto.prop_generator.__class__)(proto=proto.prop_generator)
        self._debris_generator = get_wrapper(proto_type=proto.debris_generator.__class__)(proto=proto.debris_generator)
        self._driveway_generator = get_wrapper(proto_type=proto.driveway_generator.__class__)(
            proto=proto.driveway_generator
        )
        self._all_vehicle_test_generator = get_wrapper(proto_type=proto.all_vehicle_test_generator.__class__)(
            proto=proto.all_vehicle_test_generator
        )
        self._curve_generator = get_wrapper(proto_type=proto.curve_generator.__class__)(proto=proto.curve_generator)
        self._parking_generator = get_wrapper(proto_type=proto.parking_generator.__class__)(
            proto=proto.parking_generator
        )
        self._drone_generator = get_wrapper(proto_type=proto.drone_generator.__class__)(proto=proto.drone_generator)
        self._unified_generator = get_wrapper(proto_type=proto.unified_generator.__class__)(
            proto=proto.unified_generator
        )
        if random_generator is not None:
            self.random_generator = random_generator
        if junction_generator is not None:
            self.junction_generator = junction_generator
        if voi_generator is not None:
            self.voi_generator = voi_generator
        if kitti_generator is not None:
            self.kitti_generator = kitti_generator
        if position_generator is not None:
            self.position_generator = position_generator
        if lane_generator is not None:
            self.lane_generator = lane_generator
        if static_cam_generator is not None:
            self.static_cam_generator = static_cam_generator
        if jaywalking_generator is not None:
            self.jaywalking_generator = jaywalking_generator
        if prop_generator is not None:
            self.prop_generator = prop_generator
        if debris_generator is not None:
            self.debris_generator = debris_generator
        if driveway_generator is not None:
            self.driveway_generator = driveway_generator
        if all_vehicle_test_generator is not None:
            self.all_vehicle_test_generator = all_vehicle_test_generator
        if curve_generator is not None:
            self.curve_generator = curve_generator
        if parking_generator is not None:
            self.parking_generator = parking_generator
        if drone_generator is not None:
            self.drone_generator = drone_generator
        if unified_generator is not None:
            self.unified_generator = unified_generator

    @property
    def random_generator(self) -> RandomLaneScenarioGeneratorInfo:
        return self._random_generator

    @random_generator.setter
    def random_generator(self, value: RandomLaneScenarioGeneratorInfo):
        self.proto.random_generator.CopyFrom(value.proto)

        self._random_generator = value
        self._random_generator._update_proto_references(self.proto.random_generator)

    @property
    def junction_generator(self) -> JunctionScenarioGeneratorInfo:
        return self._junction_generator

    @junction_generator.setter
    def junction_generator(self, value: JunctionScenarioGeneratorInfo):
        self.proto.junction_generator.CopyFrom(value.proto)

        self._junction_generator = value
        self._junction_generator._update_proto_references(self.proto.junction_generator)

    @property
    def voi_generator(self) -> VehicleOfInterestScenarioGeneratorInfo:
        return self._voi_generator

    @voi_generator.setter
    def voi_generator(self, value: VehicleOfInterestScenarioGeneratorInfo):
        self.proto.voi_generator.CopyFrom(value.proto)

        self._voi_generator = value
        self._voi_generator._update_proto_references(self.proto.voi_generator)

    @property
    def kitti_generator(self) -> KittiScenarioGeneratorInfo:
        return self._kitti_generator

    @kitti_generator.setter
    def kitti_generator(self, value: KittiScenarioGeneratorInfo):
        self.proto.kitti_generator.CopyFrom(value.proto)

        self._kitti_generator = value
        self._kitti_generator._update_proto_references(self.proto.kitti_generator)

    @property
    def position_generator(self) -> VehiclePositionScenarioGeneratorInfo:
        return self._position_generator

    @position_generator.setter
    def position_generator(self, value: VehiclePositionScenarioGeneratorInfo):
        self.proto.position_generator.CopyFrom(value.proto)

        self._position_generator = value
        self._position_generator._update_proto_references(self.proto.position_generator)

    @property
    def lane_generator(self) -> LaneTypeScenarioGeneratorInfo:
        return self._lane_generator

    @lane_generator.setter
    def lane_generator(self, value: LaneTypeScenarioGeneratorInfo):
        self.proto.lane_generator.CopyFrom(value.proto)

        self._lane_generator = value
        self._lane_generator._update_proto_references(self.proto.lane_generator)

    @property
    def static_cam_generator(self) -> StaticCamScenarioGeneratorInfo:
        return self._static_cam_generator

    @static_cam_generator.setter
    def static_cam_generator(self, value: StaticCamScenarioGeneratorInfo):
        self.proto.static_cam_generator.CopyFrom(value.proto)

        self._static_cam_generator = value
        self._static_cam_generator._update_proto_references(self.proto.static_cam_generator)

    @property
    def jaywalking_generator(self) -> JaywalkingScenarioGeneratorInfo:
        return self._jaywalking_generator

    @jaywalking_generator.setter
    def jaywalking_generator(self, value: JaywalkingScenarioGeneratorInfo):
        self.proto.jaywalking_generator.CopyFrom(value.proto)

        self._jaywalking_generator = value
        self._jaywalking_generator._update_proto_references(self.proto.jaywalking_generator)

    @property
    def prop_generator(self) -> PropScenarioGeneratorInfo:
        return self._prop_generator

    @prop_generator.setter
    def prop_generator(self, value: PropScenarioGeneratorInfo):
        self.proto.prop_generator.CopyFrom(value.proto)

        self._prop_generator = value
        self._prop_generator._update_proto_references(self.proto.prop_generator)

    @property
    def debris_generator(self) -> DebrisScenarioGeneratorInfo:
        return self._debris_generator

    @debris_generator.setter
    def debris_generator(self, value: DebrisScenarioGeneratorInfo):
        self.proto.debris_generator.CopyFrom(value.proto)

        self._debris_generator = value
        self._debris_generator._update_proto_references(self.proto.debris_generator)

    @property
    def driveway_generator(self) -> DrivewayScenarioGeneratorInfo:
        return self._driveway_generator

    @driveway_generator.setter
    def driveway_generator(self, value: DrivewayScenarioGeneratorInfo):
        self.proto.driveway_generator.CopyFrom(value.proto)

        self._driveway_generator = value
        self._driveway_generator._update_proto_references(self.proto.driveway_generator)

    @property
    def all_vehicle_test_generator(self) -> AllVehicleTestScenarioGeneratorInfo:
        return self._all_vehicle_test_generator

    @all_vehicle_test_generator.setter
    def all_vehicle_test_generator(self, value: AllVehicleTestScenarioGeneratorInfo):
        self.proto.all_vehicle_test_generator.CopyFrom(value.proto)

        self._all_vehicle_test_generator = value
        self._all_vehicle_test_generator._update_proto_references(self.proto.all_vehicle_test_generator)

    @property
    def curve_generator(self) -> CurveScenarioGeneratorInfo:
        return self._curve_generator

    @curve_generator.setter
    def curve_generator(self, value: CurveScenarioGeneratorInfo):
        self.proto.curve_generator.CopyFrom(value.proto)

        self._curve_generator = value
        self._curve_generator._update_proto_references(self.proto.curve_generator)

    @property
    def parking_generator(self) -> ParkingScenarioGeneratorInfo:
        return self._parking_generator

    @parking_generator.setter
    def parking_generator(self, value: ParkingScenarioGeneratorInfo):
        self.proto.parking_generator.CopyFrom(value.proto)

        self._parking_generator = value
        self._parking_generator._update_proto_references(self.proto.parking_generator)

    @property
    def drone_generator(self) -> DroneFlightScenarioGeneratorInfo:
        return self._drone_generator

    @drone_generator.setter
    def drone_generator(self, value: DroneFlightScenarioGeneratorInfo):
        self.proto.drone_generator.CopyFrom(value.proto)

        self._drone_generator = value
        self._drone_generator._update_proto_references(self.proto.drone_generator)

    @property
    def unified_generator(self) -> _pd_unified_generator_pb2.UnifiedGeneratorParameters:
        return self._unified_generator

    @unified_generator.setter
    def unified_generator(self, value: _pd_unified_generator_pb2.UnifiedGeneratorParameters):
        self.proto.unified_generator.CopyFrom(value.proto)

        self._unified_generator = value
        self._unified_generator._update_proto_references(self.proto.unified_generator)

    def _update_proto_references(self, proto: pd_spawn_pb2.GeneratorConfigPreset):
        self.proto = proto
        self._random_generator._update_proto_references(proto.random_generator)
        self._junction_generator._update_proto_references(proto.junction_generator)
        self._voi_generator._update_proto_references(proto.voi_generator)
        self._kitti_generator._update_proto_references(proto.kitti_generator)
        self._position_generator._update_proto_references(proto.position_generator)
        self._lane_generator._update_proto_references(proto.lane_generator)
        self._static_cam_generator._update_proto_references(proto.static_cam_generator)
        self._jaywalking_generator._update_proto_references(proto.jaywalking_generator)
        self._prop_generator._update_proto_references(proto.prop_generator)
        self._debris_generator._update_proto_references(proto.debris_generator)
        self._driveway_generator._update_proto_references(proto.driveway_generator)
        self._all_vehicle_test_generator._update_proto_references(proto.all_vehicle_test_generator)
        self._curve_generator._update_proto_references(proto.curve_generator)
        self._parking_generator._update_proto_references(proto.parking_generator)
        self._drone_generator._update_proto_references(proto.drone_generator)
        self._unified_generator._update_proto_references(proto.unified_generator)


@register_wrapper(proto_type=pd_spawn_pb2.GeneratorConfig)
class GeneratorConfig(ProtoMessageClass):
    """Root generator message, stores weights and presets

    Args:
        preset_distribution: :attr:`preset_distribution`
        presets: :attr:`presets`
    Attributes:
        preset_distribution:
        presets:"""

    _proto_message = pd_spawn_pb2.GeneratorConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_spawn_pb2.GeneratorConfig] = None,
        preset_distribution: _pd_distributions_pb2.CategoricalDistribution = None,
        presets: List[GeneratorConfigPreset] = None,
    ):
        if proto is None:
            proto = pd_spawn_pb2.GeneratorConfig()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(
            proto=proto.preset_distribution
        )
        self._presets = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets],
            attr_name="presets",
            list_owner=self,
        )
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution
        if presets is not None:
            self.presets = presets

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self.proto.preset_distribution.CopyFrom(value.proto)

        self._preset_distribution = value
        self._preset_distribution._update_proto_references(self.proto.preset_distribution)

    @property
    def presets(self) -> List[GeneratorConfigPreset]:
        return self._presets

    @presets.setter
    def presets(self, value: List[GeneratorConfigPreset]):
        self._presets.clear()
        for v in value:
            self._presets.append(v)

    def _update_proto_references(self, proto: pd_spawn_pb2.GeneratorConfig):
        self.proto = proto
        self._preset_distribution._update_proto_references(proto.preset_distribution)
        for i, v in enumerate(self.presets):
            v._update_proto_references(self.proto.presets[i])
