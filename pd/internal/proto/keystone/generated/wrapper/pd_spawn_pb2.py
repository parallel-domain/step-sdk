from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_spawn_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_spawn_pb2.AgentStateProbabilityConfig)
class AgentStateProbabilityConfig(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.AgentStateProbabilityConfig

    def __init__(self, *, proto: Optional[pd_spawn_pb2.AgentStateProbabilityConfig]=None, allowedAfter: Optional[float]=None, maxPerScene: Optional[int]=None, probability: Optional[float]=None, probabilitySpread: Optional[float]=None, stateName: Optional[str]=None, time: Optional[float]=None, timeSpread: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.AgentStateProbabilityConfig()
        self.proto = proto
        if allowedAfter is not None:
            self.allowedAfter = allowedAfter
        if maxPerScene is not None:
            self.maxPerScene = maxPerScene
        if probability is not None:
            self.probability = probability
        if probabilitySpread is not None:
            self.probabilitySpread = probabilitySpread
        if stateName is not None:
            self.stateName = stateName
        if time is not None:
            self.time = time
        if timeSpread is not None:
            self.timeSpread = timeSpread

    @property
    def allowedAfter(self) -> float:
        return self.proto.allowedAfter

    @allowedAfter.setter
    def allowedAfter(self, value: float):
        self.proto.allowedAfter = value

    @property
    def maxPerScene(self) -> int:
        return self.proto.maxPerScene

    @maxPerScene.setter
    def maxPerScene(self, value: int):
        self.proto.maxPerScene = value

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
    def stateName(self) -> str:
        return self.proto.stateName

    @stateName.setter
    def stateName(self, value: str):
        self.proto.stateName = value

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

@register_wrapper(proto_type=pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo)
class AllVehicleTestScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo]=None, articulatedTrailerTest: Optional[bool]=None, assetExcludeList: Optional[List[str]]=None, assetIncludeList: Optional[List[str]]=None, egoSpeed: Optional[float]=None, egoStart_t: Optional[float]=None, excludeMovingVehicles: Optional[bool]=None, excludeStaticVehicles: Optional[bool]=None, includeOnlyVehiclesInExclusionList: Optional[int]=None, leftOfEgo: Optional[bool]=None, renderVehiclesBehindEgo: Optional[bool]=None, rightOfEgo: Optional[bool]=None, scenarioType: Optional[int]=None, startSeparationS: Optional[float]=None, testVehiclesSpeed: Optional[float]=None, vehicleExclusionList: Optional[List[str]]=None):
        if proto is None:
            proto = pd_spawn_pb2.AllVehicleTestScenarioGeneratorInfo()
        self.proto = proto
        self._assetExcludeList = ProtoListWrapper(container=[str(v) for v in proto.assetExcludeList], attr_name='assetExcludeList', list_owner=proto)
        self._assetIncludeList = ProtoListWrapper(container=[str(v) for v in proto.assetIncludeList], attr_name='assetIncludeList', list_owner=proto)
        self._vehicleExclusionList = ProtoListWrapper(container=[str(v) for v in proto.vehicleExclusionList], attr_name='vehicleExclusionList', list_owner=proto)
        if articulatedTrailerTest is not None:
            self.articulatedTrailerTest = articulatedTrailerTest
        if assetExcludeList is not None:
            self.assetExcludeList = assetExcludeList
        if assetIncludeList is not None:
            self.assetIncludeList = assetIncludeList
        if egoSpeed is not None:
            self.egoSpeed = egoSpeed
        if egoStart_t is not None:
            self.egoStart_t = egoStart_t
        if excludeMovingVehicles is not None:
            self.excludeMovingVehicles = excludeMovingVehicles
        if excludeStaticVehicles is not None:
            self.excludeStaticVehicles = excludeStaticVehicles
        if includeOnlyVehiclesInExclusionList is not None:
            self.includeOnlyVehiclesInExclusionList = includeOnlyVehiclesInExclusionList
        if leftOfEgo is not None:
            self.leftOfEgo = leftOfEgo
        if renderVehiclesBehindEgo is not None:
            self.renderVehiclesBehindEgo = renderVehiclesBehindEgo
        if rightOfEgo is not None:
            self.rightOfEgo = rightOfEgo
        if scenarioType is not None:
            self.scenarioType = scenarioType
        if startSeparationS is not None:
            self.startSeparationS = startSeparationS
        if testVehiclesSpeed is not None:
            self.testVehiclesSpeed = testVehiclesSpeed
        if vehicleExclusionList is not None:
            self.vehicleExclusionList = vehicleExclusionList

    @property
    def articulatedTrailerTest(self) -> bool:
        return self.proto.articulatedTrailerTest

    @articulatedTrailerTest.setter
    def articulatedTrailerTest(self, value: bool):
        self.proto.articulatedTrailerTest = value

    @property
    def assetExcludeList(self) -> List[str]:
        return self._assetExcludeList

    @assetExcludeList.setter
    def assetExcludeList(self, value: List[str]):
        self._assetExcludeList.clear()
        for v in value:
            self._assetExcludeList.append(v)

    @property
    def assetIncludeList(self) -> List[str]:
        return self._assetIncludeList

    @assetIncludeList.setter
    def assetIncludeList(self, value: List[str]):
        self._assetIncludeList.clear()
        for v in value:
            self._assetIncludeList.append(v)

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
    def excludeMovingVehicles(self) -> bool:
        return self.proto.excludeMovingVehicles

    @excludeMovingVehicles.setter
    def excludeMovingVehicles(self, value: bool):
        self.proto.excludeMovingVehicles = value

    @property
    def excludeStaticVehicles(self) -> bool:
        return self.proto.excludeStaticVehicles

    @excludeStaticVehicles.setter
    def excludeStaticVehicles(self, value: bool):
        self.proto.excludeStaticVehicles = value

    @property
    def includeOnlyVehiclesInExclusionList(self) -> int:
        return self.proto.includeOnlyVehiclesInExclusionList

    @includeOnlyVehiclesInExclusionList.setter
    def includeOnlyVehiclesInExclusionList(self, value: int):
        self.proto.includeOnlyVehiclesInExclusionList = value

    @property
    def leftOfEgo(self) -> bool:
        return self.proto.leftOfEgo

    @leftOfEgo.setter
    def leftOfEgo(self, value: bool):
        self.proto.leftOfEgo = value

    @property
    def renderVehiclesBehindEgo(self) -> bool:
        return self.proto.renderVehiclesBehindEgo

    @renderVehiclesBehindEgo.setter
    def renderVehiclesBehindEgo(self, value: bool):
        self.proto.renderVehiclesBehindEgo = value

    @property
    def rightOfEgo(self) -> bool:
        return self.proto.rightOfEgo

    @rightOfEgo.setter
    def rightOfEgo(self, value: bool):
        self.proto.rightOfEgo = value

    @property
    def scenarioType(self) -> int:
        return self.proto.scenarioType

    @scenarioType.setter
    def scenarioType(self, value: int):
        self.proto.scenarioType = value

    @property
    def startSeparationS(self) -> float:
        return self.proto.startSeparationS

    @startSeparationS.setter
    def startSeparationS(self, value: float):
        self.proto.startSeparationS = value

    @property
    def testVehiclesSpeed(self) -> float:
        return self.proto.testVehiclesSpeed

    @testVehiclesSpeed.setter
    def testVehiclesSpeed(self, value: float):
        self.proto.testVehiclesSpeed = value

    @property
    def vehicleExclusionList(self) -> List[str]:
        return self._vehicleExclusionList

    @vehicleExclusionList.setter
    def vehicleExclusionList(self, value: List[str]):
        self._vehicleExclusionList.clear()
        for v in value:
            self._vehicleExclusionList.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.CurveScenarioGeneratorInfo)
class CurveScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.CurveScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.CurveScenarioGeneratorInfo]=None, maxCurvature: Optional[float]=None, maxLongitudinalOffset: Optional[float]=None, minCurvature: Optional[float]=None, minLongitudinalOffset: Optional[float]=None, minSectionLength: Optional[float]=None, occludedVehicleType: Optional[VehicleType]=None, placeOccluders: Optional[bool]=None):
        if proto is None:
            proto = pd_spawn_pb2.CurveScenarioGeneratorInfo()
        self.proto = proto
        if maxCurvature is not None:
            self.maxCurvature = maxCurvature
        if maxLongitudinalOffset is not None:
            self.maxLongitudinalOffset = maxLongitudinalOffset
        if minCurvature is not None:
            self.minCurvature = minCurvature
        if minLongitudinalOffset is not None:
            self.minLongitudinalOffset = minLongitudinalOffset
        if minSectionLength is not None:
            self.minSectionLength = minSectionLength
        if occludedVehicleType is not None:
            self.occludedVehicleType = occludedVehicleType
        if placeOccluders is not None:
            self.placeOccluders = placeOccluders

    @property
    def maxCurvature(self) -> float:
        return self.proto.maxCurvature

    @maxCurvature.setter
    def maxCurvature(self, value: float):
        self.proto.maxCurvature = value

    @property
    def maxLongitudinalOffset(self) -> float:
        return self.proto.maxLongitudinalOffset

    @maxLongitudinalOffset.setter
    def maxLongitudinalOffset(self, value: float):
        self.proto.maxLongitudinalOffset = value

    @property
    def minCurvature(self) -> float:
        return self.proto.minCurvature

    @minCurvature.setter
    def minCurvature(self, value: float):
        self.proto.minCurvature = value

    @property
    def minLongitudinalOffset(self) -> float:
        return self.proto.minLongitudinalOffset

    @minLongitudinalOffset.setter
    def minLongitudinalOffset(self, value: float):
        self.proto.minLongitudinalOffset = value

    @property
    def minSectionLength(self) -> float:
        return self.proto.minSectionLength

    @minSectionLength.setter
    def minSectionLength(self, value: float):
        self.proto.minSectionLength = value

    @property
    def occludedVehicleType(self) -> int:
        return self.proto.occludedVehicleType

    @occludedVehicleType.setter
    def occludedVehicleType(self, value: int):
        self.proto.occludedVehicleType = value

    @property
    def placeOccluders(self) -> bool:
        return self.proto.placeOccluders

    @placeOccluders.setter
    def placeOccluders(self, value: bool):
        self.proto.placeOccluders = value

@register_wrapper(proto_type=pd_spawn_pb2.DebrisScenarioGeneratorInfo)
class DebrisScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.DebrisScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.DebrisScenarioGeneratorInfo]=None, foliageCenterBias: Optional[float]=None, foliageDebrisAssetRemoveTag: Optional[str]=None, foliageDebrisAssetTag: Optional[str]=None, foliageDensity: Optional[float]=None, largeDebrisAssetRemoveTag: Optional[str]=None, largeDebrisAssetTag: Optional[str]=None, largeDebrisCenterBias: Optional[float]=None, largeDebrisDensity: Optional[float]=None, maxFoliageDistance: Optional[float]=None, maxLargeDebrisDistance: Optional[float]=None, maxSmallDebrisDistance: Optional[float]=None, minDistanceFromLaneEdgeForShortDebris: Optional[float]=None, minFoliageDistance: Optional[float]=None, minHeightDebrisToPlaceAtLaneEdges: Optional[float]=None, minLargeDebrisDistance: Optional[float]=None, minSmallDebrisDistance: Optional[float]=None, smallDebrisAssetRemoveTag: Optional[str]=None, smallDebrisAssetTag: Optional[str]=None, smallDebrisCenterBias: Optional[float]=None, smallDebrisDensity: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.DebrisScenarioGeneratorInfo()
        self.proto = proto
        if foliageCenterBias is not None:
            self.foliageCenterBias = foliageCenterBias
        if foliageDebrisAssetRemoveTag is not None:
            self.foliageDebrisAssetRemoveTag = foliageDebrisAssetRemoveTag
        if foliageDebrisAssetTag is not None:
            self.foliageDebrisAssetTag = foliageDebrisAssetTag
        if foliageDensity is not None:
            self.foliageDensity = foliageDensity
        if largeDebrisAssetRemoveTag is not None:
            self.largeDebrisAssetRemoveTag = largeDebrisAssetRemoveTag
        if largeDebrisAssetTag is not None:
            self.largeDebrisAssetTag = largeDebrisAssetTag
        if largeDebrisCenterBias is not None:
            self.largeDebrisCenterBias = largeDebrisCenterBias
        if largeDebrisDensity is not None:
            self.largeDebrisDensity = largeDebrisDensity
        if maxFoliageDistance is not None:
            self.maxFoliageDistance = maxFoliageDistance
        if maxLargeDebrisDistance is not None:
            self.maxLargeDebrisDistance = maxLargeDebrisDistance
        if maxSmallDebrisDistance is not None:
            self.maxSmallDebrisDistance = maxSmallDebrisDistance
        if minDistanceFromLaneEdgeForShortDebris is not None:
            self.minDistanceFromLaneEdgeForShortDebris = minDistanceFromLaneEdgeForShortDebris
        if minFoliageDistance is not None:
            self.minFoliageDistance = minFoliageDistance
        if minHeightDebrisToPlaceAtLaneEdges is not None:
            self.minHeightDebrisToPlaceAtLaneEdges = minHeightDebrisToPlaceAtLaneEdges
        if minLargeDebrisDistance is not None:
            self.minLargeDebrisDistance = minLargeDebrisDistance
        if minSmallDebrisDistance is not None:
            self.minSmallDebrisDistance = minSmallDebrisDistance
        if smallDebrisAssetRemoveTag is not None:
            self.smallDebrisAssetRemoveTag = smallDebrisAssetRemoveTag
        if smallDebrisAssetTag is not None:
            self.smallDebrisAssetTag = smallDebrisAssetTag
        if smallDebrisCenterBias is not None:
            self.smallDebrisCenterBias = smallDebrisCenterBias
        if smallDebrisDensity is not None:
            self.smallDebrisDensity = smallDebrisDensity

    @property
    def foliageCenterBias(self) -> float:
        return self.proto.foliageCenterBias

    @foliageCenterBias.setter
    def foliageCenterBias(self, value: float):
        self.proto.foliageCenterBias = value

    @property
    def foliageDebrisAssetRemoveTag(self) -> str:
        return self.proto.foliageDebrisAssetRemoveTag

    @foliageDebrisAssetRemoveTag.setter
    def foliageDebrisAssetRemoveTag(self, value: str):
        self.proto.foliageDebrisAssetRemoveTag = value

    @property
    def foliageDebrisAssetTag(self) -> str:
        return self.proto.foliageDebrisAssetTag

    @foliageDebrisAssetTag.setter
    def foliageDebrisAssetTag(self, value: str):
        self.proto.foliageDebrisAssetTag = value

    @property
    def foliageDensity(self) -> float:
        return self.proto.foliageDensity

    @foliageDensity.setter
    def foliageDensity(self, value: float):
        self.proto.foliageDensity = value

    @property
    def largeDebrisAssetRemoveTag(self) -> str:
        return self.proto.largeDebrisAssetRemoveTag

    @largeDebrisAssetRemoveTag.setter
    def largeDebrisAssetRemoveTag(self, value: str):
        self.proto.largeDebrisAssetRemoveTag = value

    @property
    def largeDebrisAssetTag(self) -> str:
        return self.proto.largeDebrisAssetTag

    @largeDebrisAssetTag.setter
    def largeDebrisAssetTag(self, value: str):
        self.proto.largeDebrisAssetTag = value

    @property
    def largeDebrisCenterBias(self) -> float:
        return self.proto.largeDebrisCenterBias

    @largeDebrisCenterBias.setter
    def largeDebrisCenterBias(self, value: float):
        self.proto.largeDebrisCenterBias = value

    @property
    def largeDebrisDensity(self) -> float:
        return self.proto.largeDebrisDensity

    @largeDebrisDensity.setter
    def largeDebrisDensity(self, value: float):
        self.proto.largeDebrisDensity = value

    @property
    def maxFoliageDistance(self) -> float:
        return self.proto.maxFoliageDistance

    @maxFoliageDistance.setter
    def maxFoliageDistance(self, value: float):
        self.proto.maxFoliageDistance = value

    @property
    def maxLargeDebrisDistance(self) -> float:
        return self.proto.maxLargeDebrisDistance

    @maxLargeDebrisDistance.setter
    def maxLargeDebrisDistance(self, value: float):
        self.proto.maxLargeDebrisDistance = value

    @property
    def maxSmallDebrisDistance(self) -> float:
        return self.proto.maxSmallDebrisDistance

    @maxSmallDebrisDistance.setter
    def maxSmallDebrisDistance(self, value: float):
        self.proto.maxSmallDebrisDistance = value

    @property
    def minDistanceFromLaneEdgeForShortDebris(self) -> float:
        return self.proto.minDistanceFromLaneEdgeForShortDebris

    @minDistanceFromLaneEdgeForShortDebris.setter
    def minDistanceFromLaneEdgeForShortDebris(self, value: float):
        self.proto.minDistanceFromLaneEdgeForShortDebris = value

    @property
    def minFoliageDistance(self) -> float:
        return self.proto.minFoliageDistance

    @minFoliageDistance.setter
    def minFoliageDistance(self, value: float):
        self.proto.minFoliageDistance = value

    @property
    def minHeightDebrisToPlaceAtLaneEdges(self) -> float:
        return self.proto.minHeightDebrisToPlaceAtLaneEdges

    @minHeightDebrisToPlaceAtLaneEdges.setter
    def minHeightDebrisToPlaceAtLaneEdges(self, value: float):
        self.proto.minHeightDebrisToPlaceAtLaneEdges = value

    @property
    def minLargeDebrisDistance(self) -> float:
        return self.proto.minLargeDebrisDistance

    @minLargeDebrisDistance.setter
    def minLargeDebrisDistance(self, value: float):
        self.proto.minLargeDebrisDistance = value

    @property
    def minSmallDebrisDistance(self) -> float:
        return self.proto.minSmallDebrisDistance

    @minSmallDebrisDistance.setter
    def minSmallDebrisDistance(self, value: float):
        self.proto.minSmallDebrisDistance = value

    @property
    def smallDebrisAssetRemoveTag(self) -> str:
        return self.proto.smallDebrisAssetRemoveTag

    @smallDebrisAssetRemoveTag.setter
    def smallDebrisAssetRemoveTag(self, value: str):
        self.proto.smallDebrisAssetRemoveTag = value

    @property
    def smallDebrisAssetTag(self) -> str:
        return self.proto.smallDebrisAssetTag

    @smallDebrisAssetTag.setter
    def smallDebrisAssetTag(self, value: str):
        self.proto.smallDebrisAssetTag = value

    @property
    def smallDebrisCenterBias(self) -> float:
        return self.proto.smallDebrisCenterBias

    @smallDebrisCenterBias.setter
    def smallDebrisCenterBias(self, value: float):
        self.proto.smallDebrisCenterBias = value

    @property
    def smallDebrisDensity(self) -> float:
        return self.proto.smallDebrisDensity

    @smallDebrisDensity.setter
    def smallDebrisDensity(self, value: float):
        self.proto.smallDebrisDensity = value

@register_wrapper(proto_type=pd_spawn_pb2.DrivewayScenarioGeneratorInfo)
class DrivewayScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.DrivewayScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.DrivewayScenarioGeneratorInfo]=None, brakeUntilEgoTimeToAgentS: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, drivewayVehiclesFacingRoadProbability: Optional[float]=None, egoSpawnLocationProbability: Optional[_pd_distributions_pb2.EnumDistribution]=None, enablePropOcclusions: Optional[bool]=None, enableVehicleOcclusions: Optional[bool]=None, excludeDrivewayParkingEntryRoadType: Optional[bool]=None, excludeDrivewayRoadType: Optional[bool]=None, maxDrivewayLateralOffsetPercentage: Optional[float]=None, maxDrivewayLongitudinalOffsetPercentage: Optional[float]=None, maxEgoSpawnDistFromDriveway: Optional[float]=None, minDrivewayLateralOffsetPercentage: Optional[float]=None, minDrivewayLongitudinalOffsetPercentage: Optional[float]=None, minEgoSpawnDistFromDriveway: Optional[float]=None, occlusionOffsetDist: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, placeEgoOnClosestCrossRoadLane: Optional[bool]=None, propOcclusionCountDist: Optional[_pd_unified_generator_pb2.CenterSpreadConfigInt]=None, propOcclusionSpacingDist: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, useBrakeUntilEgoTimeToAgent: Optional[bool]=None, vehicleDepartsDrivewayProbability: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.DrivewayScenarioGeneratorInfo()
        self.proto = proto
        self._brakeUntilEgoTimeToAgentS = get_wrapper(proto_type=proto.brakeUntilEgoTimeToAgentS.__class__)(proto=proto.brakeUntilEgoTimeToAgentS)
        self._egoSpawnLocationProbability = get_wrapper(proto_type=proto.egoSpawnLocationProbability.__class__)(proto=proto.egoSpawnLocationProbability)
        self._occlusionOffsetDist = get_wrapper(proto_type=proto.occlusionOffsetDist.__class__)(proto=proto.occlusionOffsetDist)
        self._propOcclusionCountDist = get_wrapper(proto_type=proto.propOcclusionCountDist.__class__)(proto=proto.propOcclusionCountDist)
        self._propOcclusionSpacingDist = get_wrapper(proto_type=proto.propOcclusionSpacingDist.__class__)(proto=proto.propOcclusionSpacingDist)
        if brakeUntilEgoTimeToAgentS is not None:
            self.brakeUntilEgoTimeToAgentS = brakeUntilEgoTimeToAgentS
        if drivewayVehiclesFacingRoadProbability is not None:
            self.drivewayVehiclesFacingRoadProbability = drivewayVehiclesFacingRoadProbability
        if egoSpawnLocationProbability is not None:
            self.egoSpawnLocationProbability = egoSpawnLocationProbability
        if enablePropOcclusions is not None:
            self.enablePropOcclusions = enablePropOcclusions
        if enableVehicleOcclusions is not None:
            self.enableVehicleOcclusions = enableVehicleOcclusions
        if excludeDrivewayParkingEntryRoadType is not None:
            self.excludeDrivewayParkingEntryRoadType = excludeDrivewayParkingEntryRoadType
        if excludeDrivewayRoadType is not None:
            self.excludeDrivewayRoadType = excludeDrivewayRoadType
        if maxDrivewayLateralOffsetPercentage is not None:
            self.maxDrivewayLateralOffsetPercentage = maxDrivewayLateralOffsetPercentage
        if maxDrivewayLongitudinalOffsetPercentage is not None:
            self.maxDrivewayLongitudinalOffsetPercentage = maxDrivewayLongitudinalOffsetPercentage
        if maxEgoSpawnDistFromDriveway is not None:
            self.maxEgoSpawnDistFromDriveway = maxEgoSpawnDistFromDriveway
        if minDrivewayLateralOffsetPercentage is not None:
            self.minDrivewayLateralOffsetPercentage = minDrivewayLateralOffsetPercentage
        if minDrivewayLongitudinalOffsetPercentage is not None:
            self.minDrivewayLongitudinalOffsetPercentage = minDrivewayLongitudinalOffsetPercentage
        if minEgoSpawnDistFromDriveway is not None:
            self.minEgoSpawnDistFromDriveway = minEgoSpawnDistFromDriveway
        if occlusionOffsetDist is not None:
            self.occlusionOffsetDist = occlusionOffsetDist
        if placeEgoOnClosestCrossRoadLane is not None:
            self.placeEgoOnClosestCrossRoadLane = placeEgoOnClosestCrossRoadLane
        if propOcclusionCountDist is not None:
            self.propOcclusionCountDist = propOcclusionCountDist
        if propOcclusionSpacingDist is not None:
            self.propOcclusionSpacingDist = propOcclusionSpacingDist
        if useBrakeUntilEgoTimeToAgent is not None:
            self.useBrakeUntilEgoTimeToAgent = useBrakeUntilEgoTimeToAgent
        if vehicleDepartsDrivewayProbability is not None:
            self.vehicleDepartsDrivewayProbability = vehicleDepartsDrivewayProbability

    @property
    def brakeUntilEgoTimeToAgentS(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._brakeUntilEgoTimeToAgentS

    @brakeUntilEgoTimeToAgentS.setter
    def brakeUntilEgoTimeToAgentS(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._brakeUntilEgoTimeToAgentS.proto.CopyFrom(value.proto)

    @property
    def drivewayVehiclesFacingRoadProbability(self) -> float:
        return self.proto.drivewayVehiclesFacingRoadProbability

    @drivewayVehiclesFacingRoadProbability.setter
    def drivewayVehiclesFacingRoadProbability(self, value: float):
        self.proto.drivewayVehiclesFacingRoadProbability = value

    @property
    def egoSpawnLocationProbability(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._egoSpawnLocationProbability

    @egoSpawnLocationProbability.setter
    def egoSpawnLocationProbability(self, value: _pd_distributions_pb2.EnumDistribution):
        self._egoSpawnLocationProbability.proto.CopyFrom(value.proto)

    @property
    def enablePropOcclusions(self) -> bool:
        return self.proto.enablePropOcclusions

    @enablePropOcclusions.setter
    def enablePropOcclusions(self, value: bool):
        self.proto.enablePropOcclusions = value

    @property
    def enableVehicleOcclusions(self) -> bool:
        return self.proto.enableVehicleOcclusions

    @enableVehicleOcclusions.setter
    def enableVehicleOcclusions(self, value: bool):
        self.proto.enableVehicleOcclusions = value

    @property
    def excludeDrivewayParkingEntryRoadType(self) -> bool:
        return self.proto.excludeDrivewayParkingEntryRoadType

    @excludeDrivewayParkingEntryRoadType.setter
    def excludeDrivewayParkingEntryRoadType(self, value: bool):
        self.proto.excludeDrivewayParkingEntryRoadType = value

    @property
    def excludeDrivewayRoadType(self) -> bool:
        return self.proto.excludeDrivewayRoadType

    @excludeDrivewayRoadType.setter
    def excludeDrivewayRoadType(self, value: bool):
        self.proto.excludeDrivewayRoadType = value

    @property
    def maxDrivewayLateralOffsetPercentage(self) -> float:
        return self.proto.maxDrivewayLateralOffsetPercentage

    @maxDrivewayLateralOffsetPercentage.setter
    def maxDrivewayLateralOffsetPercentage(self, value: float):
        self.proto.maxDrivewayLateralOffsetPercentage = value

    @property
    def maxDrivewayLongitudinalOffsetPercentage(self) -> float:
        return self.proto.maxDrivewayLongitudinalOffsetPercentage

    @maxDrivewayLongitudinalOffsetPercentage.setter
    def maxDrivewayLongitudinalOffsetPercentage(self, value: float):
        self.proto.maxDrivewayLongitudinalOffsetPercentage = value

    @property
    def maxEgoSpawnDistFromDriveway(self) -> float:
        return self.proto.maxEgoSpawnDistFromDriveway

    @maxEgoSpawnDistFromDriveway.setter
    def maxEgoSpawnDistFromDriveway(self, value: float):
        self.proto.maxEgoSpawnDistFromDriveway = value

    @property
    def minDrivewayLateralOffsetPercentage(self) -> float:
        return self.proto.minDrivewayLateralOffsetPercentage

    @minDrivewayLateralOffsetPercentage.setter
    def minDrivewayLateralOffsetPercentage(self, value: float):
        self.proto.minDrivewayLateralOffsetPercentage = value

    @property
    def minDrivewayLongitudinalOffsetPercentage(self) -> float:
        return self.proto.minDrivewayLongitudinalOffsetPercentage

    @minDrivewayLongitudinalOffsetPercentage.setter
    def minDrivewayLongitudinalOffsetPercentage(self, value: float):
        self.proto.minDrivewayLongitudinalOffsetPercentage = value

    @property
    def minEgoSpawnDistFromDriveway(self) -> float:
        return self.proto.minEgoSpawnDistFromDriveway

    @minEgoSpawnDistFromDriveway.setter
    def minEgoSpawnDistFromDriveway(self, value: float):
        self.proto.minEgoSpawnDistFromDriveway = value

    @property
    def occlusionOffsetDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._occlusionOffsetDist

    @occlusionOffsetDist.setter
    def occlusionOffsetDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._occlusionOffsetDist.proto.CopyFrom(value.proto)

    @property
    def placeEgoOnClosestCrossRoadLane(self) -> bool:
        return self.proto.placeEgoOnClosestCrossRoadLane

    @placeEgoOnClosestCrossRoadLane.setter
    def placeEgoOnClosestCrossRoadLane(self, value: bool):
        self.proto.placeEgoOnClosestCrossRoadLane = value

    @property
    def propOcclusionCountDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._propOcclusionCountDist

    @propOcclusionCountDist.setter
    def propOcclusionCountDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self._propOcclusionCountDist.proto.CopyFrom(value.proto)

    @property
    def propOcclusionSpacingDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._propOcclusionSpacingDist

    @propOcclusionSpacingDist.setter
    def propOcclusionSpacingDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._propOcclusionSpacingDist.proto.CopyFrom(value.proto)

    @property
    def useBrakeUntilEgoTimeToAgent(self) -> bool:
        return self.proto.useBrakeUntilEgoTimeToAgent

    @useBrakeUntilEgoTimeToAgent.setter
    def useBrakeUntilEgoTimeToAgent(self, value: bool):
        self.proto.useBrakeUntilEgoTimeToAgent = value

    @property
    def vehicleDepartsDrivewayProbability(self) -> float:
        return self.proto.vehicleDepartsDrivewayProbability

    @vehicleDepartsDrivewayProbability.setter
    def vehicleDepartsDrivewayProbability(self, value: float):
        self.proto.vehicleDepartsDrivewayProbability = value

@register_wrapper(proto_type=pd_spawn_pb2.DroneFlightScenarioGeneratorInfo)
class DroneFlightScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.DroneFlightScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.DroneFlightScenarioGeneratorInfo]=None, descentPathName: Optional[str]=None, maxRadiusFromTarget: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.DroneFlightScenarioGeneratorInfo()
        self.proto = proto
        if descentPathName is not None:
            self.descentPathName = descentPathName
        if maxRadiusFromTarget is not None:
            self.maxRadiusFromTarget = maxRadiusFromTarget

    @property
    def descentPathName(self) -> str:
        return self.proto.descentPathName

    @descentPathName.setter
    def descentPathName(self, value: str):
        self.proto.descentPathName = value

    @property
    def maxRadiusFromTarget(self) -> float:
        return self.proto.maxRadiusFromTarget

    @maxRadiusFromTarget.setter
    def maxRadiusFromTarget(self, value: float):
        self.proto.maxRadiusFromTarget = value

@register_wrapper(proto_type=pd_spawn_pb2.GeneratorConfig)
class GeneratorConfig(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.GeneratorConfig

    def __init__(self, *, proto: Optional[pd_spawn_pb2.GeneratorConfig]=None, preset_distribution: Optional[_pd_distributions_pb2.CategoricalDistribution]=None, presets: Optional[List[GeneratorConfigPreset]]=None):
        if proto is None:
            proto = pd_spawn_pb2.GeneratorConfig()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(proto=proto.preset_distribution)
        self._presets = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets], attr_name='presets', list_owner=proto)
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution
        if presets is not None:
            self.presets = presets

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self._preset_distribution.proto.CopyFrom(value.proto)

    @property
    def presets(self) -> List[GeneratorConfigPreset]:
        return self._presets

    @presets.setter
    def presets(self, value: List[GeneratorConfigPreset]):
        self._presets.clear()
        for v in value:
            self._presets.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.GeneratorConfigPreset)
class GeneratorConfigPreset(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.GeneratorConfigPreset

    def __init__(self, *, proto: Optional[pd_spawn_pb2.GeneratorConfigPreset]=None, all_vehicle_test_generator: Optional[AllVehicleTestScenarioGeneratorInfo]=None, curve_generator: Optional[CurveScenarioGeneratorInfo]=None, debris_generator: Optional[DebrisScenarioGeneratorInfo]=None, driveway_generator: Optional[DrivewayScenarioGeneratorInfo]=None, drone_generator: Optional[DroneFlightScenarioGeneratorInfo]=None, jaywalking_generator: Optional[JaywalkingScenarioGeneratorInfo]=None, junction_generator: Optional[JunctionScenarioGeneratorInfo]=None, kitti_generator: Optional[KittiScenarioGeneratorInfo]=None, lane_generator: Optional[LaneTypeScenarioGeneratorInfo]=None, parking_generator: Optional[ParkingScenarioGeneratorInfo]=None, position_generator: Optional[VehiclePositionScenarioGeneratorInfo]=None, prop_generator: Optional[PropScenarioGeneratorInfo]=None, random_generator: Optional[RandomLaneScenarioGeneratorInfo]=None, static_cam_generator: Optional[StaticCamScenarioGeneratorInfo]=None, unified_generator: Optional[_pd_unified_generator_pb2.UnifiedGeneratorParameters]=None, voi_generator: Optional[VehicleOfInterestScenarioGeneratorInfo]=None):
        if proto is None:
            proto = pd_spawn_pb2.GeneratorConfigPreset()
        self.proto = proto
        self._all_vehicle_test_generator = get_wrapper(proto_type=proto.all_vehicle_test_generator.__class__)(proto=proto.all_vehicle_test_generator)
        self._curve_generator = get_wrapper(proto_type=proto.curve_generator.__class__)(proto=proto.curve_generator)
        self._debris_generator = get_wrapper(proto_type=proto.debris_generator.__class__)(proto=proto.debris_generator)
        self._driveway_generator = get_wrapper(proto_type=proto.driveway_generator.__class__)(proto=proto.driveway_generator)
        self._drone_generator = get_wrapper(proto_type=proto.drone_generator.__class__)(proto=proto.drone_generator)
        self._jaywalking_generator = get_wrapper(proto_type=proto.jaywalking_generator.__class__)(proto=proto.jaywalking_generator)
        self._junction_generator = get_wrapper(proto_type=proto.junction_generator.__class__)(proto=proto.junction_generator)
        self._kitti_generator = get_wrapper(proto_type=proto.kitti_generator.__class__)(proto=proto.kitti_generator)
        self._lane_generator = get_wrapper(proto_type=proto.lane_generator.__class__)(proto=proto.lane_generator)
        self._parking_generator = get_wrapper(proto_type=proto.parking_generator.__class__)(proto=proto.parking_generator)
        self._position_generator = get_wrapper(proto_type=proto.position_generator.__class__)(proto=proto.position_generator)
        self._prop_generator = get_wrapper(proto_type=proto.prop_generator.__class__)(proto=proto.prop_generator)
        self._random_generator = get_wrapper(proto_type=proto.random_generator.__class__)(proto=proto.random_generator)
        self._static_cam_generator = get_wrapper(proto_type=proto.static_cam_generator.__class__)(proto=proto.static_cam_generator)
        self._unified_generator = get_wrapper(proto_type=proto.unified_generator.__class__)(proto=proto.unified_generator)
        self._voi_generator = get_wrapper(proto_type=proto.voi_generator.__class__)(proto=proto.voi_generator)
        if all_vehicle_test_generator is not None:
            self.all_vehicle_test_generator = all_vehicle_test_generator
        if curve_generator is not None:
            self.curve_generator = curve_generator
        if debris_generator is not None:
            self.debris_generator = debris_generator
        if driveway_generator is not None:
            self.driveway_generator = driveway_generator
        if drone_generator is not None:
            self.drone_generator = drone_generator
        if jaywalking_generator is not None:
            self.jaywalking_generator = jaywalking_generator
        if junction_generator is not None:
            self.junction_generator = junction_generator
        if kitti_generator is not None:
            self.kitti_generator = kitti_generator
        if lane_generator is not None:
            self.lane_generator = lane_generator
        if parking_generator is not None:
            self.parking_generator = parking_generator
        if position_generator is not None:
            self.position_generator = position_generator
        if prop_generator is not None:
            self.prop_generator = prop_generator
        if random_generator is not None:
            self.random_generator = random_generator
        if static_cam_generator is not None:
            self.static_cam_generator = static_cam_generator
        if unified_generator is not None:
            self.unified_generator = unified_generator
        if voi_generator is not None:
            self.voi_generator = voi_generator

    @property
    def all_vehicle_test_generator(self) -> AllVehicleTestScenarioGeneratorInfo:
        return self._all_vehicle_test_generator

    @all_vehicle_test_generator.setter
    def all_vehicle_test_generator(self, value: AllVehicleTestScenarioGeneratorInfo):
        self._all_vehicle_test_generator.proto.CopyFrom(value.proto)

    @property
    def curve_generator(self) -> CurveScenarioGeneratorInfo:
        return self._curve_generator

    @curve_generator.setter
    def curve_generator(self, value: CurveScenarioGeneratorInfo):
        self._curve_generator.proto.CopyFrom(value.proto)

    @property
    def debris_generator(self) -> DebrisScenarioGeneratorInfo:
        return self._debris_generator

    @debris_generator.setter
    def debris_generator(self, value: DebrisScenarioGeneratorInfo):
        self._debris_generator.proto.CopyFrom(value.proto)

    @property
    def driveway_generator(self) -> DrivewayScenarioGeneratorInfo:
        return self._driveway_generator

    @driveway_generator.setter
    def driveway_generator(self, value: DrivewayScenarioGeneratorInfo):
        self._driveway_generator.proto.CopyFrom(value.proto)

    @property
    def drone_generator(self) -> DroneFlightScenarioGeneratorInfo:
        return self._drone_generator

    @drone_generator.setter
    def drone_generator(self, value: DroneFlightScenarioGeneratorInfo):
        self._drone_generator.proto.CopyFrom(value.proto)

    @property
    def jaywalking_generator(self) -> JaywalkingScenarioGeneratorInfo:
        return self._jaywalking_generator

    @jaywalking_generator.setter
    def jaywalking_generator(self, value: JaywalkingScenarioGeneratorInfo):
        self._jaywalking_generator.proto.CopyFrom(value.proto)

    @property
    def junction_generator(self) -> JunctionScenarioGeneratorInfo:
        return self._junction_generator

    @junction_generator.setter
    def junction_generator(self, value: JunctionScenarioGeneratorInfo):
        self._junction_generator.proto.CopyFrom(value.proto)

    @property
    def kitti_generator(self) -> KittiScenarioGeneratorInfo:
        return self._kitti_generator

    @kitti_generator.setter
    def kitti_generator(self, value: KittiScenarioGeneratorInfo):
        self._kitti_generator.proto.CopyFrom(value.proto)

    @property
    def lane_generator(self) -> LaneTypeScenarioGeneratorInfo:
        return self._lane_generator

    @lane_generator.setter
    def lane_generator(self, value: LaneTypeScenarioGeneratorInfo):
        self._lane_generator.proto.CopyFrom(value.proto)

    @property
    def parking_generator(self) -> ParkingScenarioGeneratorInfo:
        return self._parking_generator

    @parking_generator.setter
    def parking_generator(self, value: ParkingScenarioGeneratorInfo):
        self._parking_generator.proto.CopyFrom(value.proto)

    @property
    def position_generator(self) -> VehiclePositionScenarioGeneratorInfo:
        return self._position_generator

    @position_generator.setter
    def position_generator(self, value: VehiclePositionScenarioGeneratorInfo):
        self._position_generator.proto.CopyFrom(value.proto)

    @property
    def prop_generator(self) -> PropScenarioGeneratorInfo:
        return self._prop_generator

    @prop_generator.setter
    def prop_generator(self, value: PropScenarioGeneratorInfo):
        self._prop_generator.proto.CopyFrom(value.proto)

    @property
    def random_generator(self) -> RandomLaneScenarioGeneratorInfo:
        return self._random_generator

    @random_generator.setter
    def random_generator(self, value: RandomLaneScenarioGeneratorInfo):
        self._random_generator.proto.CopyFrom(value.proto)

    @property
    def static_cam_generator(self) -> StaticCamScenarioGeneratorInfo:
        return self._static_cam_generator

    @static_cam_generator.setter
    def static_cam_generator(self, value: StaticCamScenarioGeneratorInfo):
        self._static_cam_generator.proto.CopyFrom(value.proto)

    @property
    def unified_generator(self) -> _pd_unified_generator_pb2.UnifiedGeneratorParameters:
        return self._unified_generator

    @unified_generator.setter
    def unified_generator(self, value: _pd_unified_generator_pb2.UnifiedGeneratorParameters):
        self._unified_generator.proto.CopyFrom(value.proto)

    @property
    def voi_generator(self) -> VehicleOfInterestScenarioGeneratorInfo:
        return self._voi_generator

    @voi_generator.setter
    def voi_generator(self, value: VehicleOfInterestScenarioGeneratorInfo):
        self._voi_generator.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.JaywalkingScenarioGeneratorInfo)
class JaywalkingScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.JaywalkingScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.JaywalkingScenarioGeneratorInfo]=None, animalProbability: Optional[float]=None, coneDensity: Optional[float]=None, generateOccluders: Optional[bool]=None, jaywalkerConeAngle: Optional[float]=None, jaywalkerEgoCarlengths: Optional[float]=None, jaywalkerFinalRadiusSpread: Optional[float]=None, jaywalkerMaxDistance: Optional[float]=None, jaywalkerMinDistance: Optional[float]=None, jaywalkerNumber: Optional[int]=None, jaywalkerRoadDistanceMax: Optional[float]=None, jaywalkerRoadDistanceMin: Optional[float]=None, placeCarOccluders: Optional[bool]=None, placePropOccluders: Optional[bool]=None, signal_light_distribution: Optional[_pd_unified_generator_pb2.SignalLightDistribution]=None, vehicleOccluderPreference: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.JaywalkingScenarioGeneratorInfo()
        self.proto = proto
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(proto=proto.signal_light_distribution)
        if animalProbability is not None:
            self.animalProbability = animalProbability
        if coneDensity is not None:
            self.coneDensity = coneDensity
        if generateOccluders is not None:
            self.generateOccluders = generateOccluders
        if jaywalkerConeAngle is not None:
            self.jaywalkerConeAngle = jaywalkerConeAngle
        if jaywalkerEgoCarlengths is not None:
            self.jaywalkerEgoCarlengths = jaywalkerEgoCarlengths
        if jaywalkerFinalRadiusSpread is not None:
            self.jaywalkerFinalRadiusSpread = jaywalkerFinalRadiusSpread
        if jaywalkerMaxDistance is not None:
            self.jaywalkerMaxDistance = jaywalkerMaxDistance
        if jaywalkerMinDistance is not None:
            self.jaywalkerMinDistance = jaywalkerMinDistance
        if jaywalkerNumber is not None:
            self.jaywalkerNumber = jaywalkerNumber
        if jaywalkerRoadDistanceMax is not None:
            self.jaywalkerRoadDistanceMax = jaywalkerRoadDistanceMax
        if jaywalkerRoadDistanceMin is not None:
            self.jaywalkerRoadDistanceMin = jaywalkerRoadDistanceMin
        if placeCarOccluders is not None:
            self.placeCarOccluders = placeCarOccluders
        if placePropOccluders is not None:
            self.placePropOccluders = placePropOccluders
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution
        if vehicleOccluderPreference is not None:
            self.vehicleOccluderPreference = vehicleOccluderPreference

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
    def generateOccluders(self) -> bool:
        return self.proto.generateOccluders

    @generateOccluders.setter
    def generateOccluders(self, value: bool):
        self.proto.generateOccluders = value

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
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self._signal_light_distribution.proto.CopyFrom(value.proto)

    @property
    def vehicleOccluderPreference(self) -> float:
        return self.proto.vehicleOccluderPreference

    @vehicleOccluderPreference.setter
    def vehicleOccluderPreference(self, value: float):
        self.proto.vehicleOccluderPreference = value

@register_wrapper(proto_type=pd_spawn_pb2.JunctionScenarioGenerator)
class JunctionScenarioGenerator(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.JunctionScenarioGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.JunctionScenarioGenerator]=None, crowd_density: Optional[float]=None, junction_id: Optional[int]=None, junction_ids: Optional[List[int]]=None, max_distance_to_junction: Optional[float]=None, min_distance_to_junction: Optional[float]=None, signal_light_distribution: Optional[_pd_unified_generator_pb2.SignalLightDistribution]=None, turn_type_distribution: Optional[_pd_unified_generator_pb2.TurnTypeDistribution]=None):
        if proto is None:
            proto = pd_spawn_pb2.JunctionScenarioGenerator()
        self.proto = proto
        self._junction_ids = ProtoListWrapper(container=[int(v) for v in proto.junction_ids], attr_name='junction_ids', list_owner=proto)
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(proto=proto.signal_light_distribution)
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(proto=proto.turn_type_distribution)
        if crowd_density is not None:
            self.crowd_density = crowd_density
        if junction_id is not None:
            self.junction_id = junction_id
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution

    @property
    def crowd_density(self) -> float:
        return self.proto.crowd_density

    @crowd_density.setter
    def crowd_density(self, value: float):
        self.proto.crowd_density = value

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
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self._signal_light_distribution.proto.CopyFrom(value.proto)

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self._turn_type_distribution.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.JunctionScenarioGeneratorInfo)
class JunctionScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.JunctionScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.JunctionScenarioGeneratorInfo]=None, allow_crossing_peds: Optional[bool]=None, cone_placement_freq: Optional[float]=None, cone_placement_max_dist: Optional[float]=None, control_type_distribution: Optional[_pd_distributions_pb2.EnumDistribution]=None, cross_road_speed_limit_mps: Optional[_pd_unified_generator_pb2.MinMaxConfigFloat]=None, crowd_density: Optional[float]=None, ego_stopped_at_junction: Optional[bool]=None, enable_prop_occlusions: Optional[bool]=None, enable_vehicle_occlusions: Optional[bool]=None, force_cross_traffic: Optional[bool]=None, geometry_type_distribution: Optional[_pd_distributions_pb2.EnumDistribution]=None, junction_id: Optional[int]=None, junction_ids: Optional[List[int]]=None, max_distance_to_junction: Optional[float]=None, min_distance_to_junction: Optional[float]=None, occlusion_offset_dist: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, prop_occlusion_count_dist: Optional[_pd_unified_generator_pb2.CenterSpreadConfigInt]=None, prop_occlusion_spacing_dist: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, road_type_distribution: Optional[_pd_distributions_pb2.EnumDistribution]=None, signal_light_distribution: Optional[_pd_unified_generator_pb2.SignalLightDistribution]=None, turn_type_distribution: Optional[_pd_unified_generator_pb2.TurnTypeDistribution]=None, use_cross_road_speed_limit: Optional[bool]=None, use_only_cross_roads_with_straight_turn_type: Optional[bool]=None):
        if proto is None:
            proto = pd_spawn_pb2.JunctionScenarioGeneratorInfo()
        self.proto = proto
        self._control_type_distribution = get_wrapper(proto_type=proto.control_type_distribution.__class__)(proto=proto.control_type_distribution)
        self._cross_road_speed_limit_mps = get_wrapper(proto_type=proto.cross_road_speed_limit_mps.__class__)(proto=proto.cross_road_speed_limit_mps)
        self._geometry_type_distribution = get_wrapper(proto_type=proto.geometry_type_distribution.__class__)(proto=proto.geometry_type_distribution)
        self._junction_ids = ProtoListWrapper(container=[int(v) for v in proto.junction_ids], attr_name='junction_ids', list_owner=proto)
        self._occlusion_offset_dist = get_wrapper(proto_type=proto.occlusion_offset_dist.__class__)(proto=proto.occlusion_offset_dist)
        self._prop_occlusion_count_dist = get_wrapper(proto_type=proto.prop_occlusion_count_dist.__class__)(proto=proto.prop_occlusion_count_dist)
        self._prop_occlusion_spacing_dist = get_wrapper(proto_type=proto.prop_occlusion_spacing_dist.__class__)(proto=proto.prop_occlusion_spacing_dist)
        self._road_type_distribution = get_wrapper(proto_type=proto.road_type_distribution.__class__)(proto=proto.road_type_distribution)
        self._signal_light_distribution = get_wrapper(proto_type=proto.signal_light_distribution.__class__)(proto=proto.signal_light_distribution)
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(proto=proto.turn_type_distribution)
        if allow_crossing_peds is not None:
            self.allow_crossing_peds = allow_crossing_peds
        if cone_placement_freq is not None:
            self.cone_placement_freq = cone_placement_freq
        if cone_placement_max_dist is not None:
            self.cone_placement_max_dist = cone_placement_max_dist
        if control_type_distribution is not None:
            self.control_type_distribution = control_type_distribution
        if cross_road_speed_limit_mps is not None:
            self.cross_road_speed_limit_mps = cross_road_speed_limit_mps
        if crowd_density is not None:
            self.crowd_density = crowd_density
        if ego_stopped_at_junction is not None:
            self.ego_stopped_at_junction = ego_stopped_at_junction
        if enable_prop_occlusions is not None:
            self.enable_prop_occlusions = enable_prop_occlusions
        if enable_vehicle_occlusions is not None:
            self.enable_vehicle_occlusions = enable_vehicle_occlusions
        if force_cross_traffic is not None:
            self.force_cross_traffic = force_cross_traffic
        if geometry_type_distribution is not None:
            self.geometry_type_distribution = geometry_type_distribution
        if junction_id is not None:
            self.junction_id = junction_id
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if occlusion_offset_dist is not None:
            self.occlusion_offset_dist = occlusion_offset_dist
        if prop_occlusion_count_dist is not None:
            self.prop_occlusion_count_dist = prop_occlusion_count_dist
        if prop_occlusion_spacing_dist is not None:
            self.prop_occlusion_spacing_dist = prop_occlusion_spacing_dist
        if road_type_distribution is not None:
            self.road_type_distribution = road_type_distribution
        if signal_light_distribution is not None:
            self.signal_light_distribution = signal_light_distribution
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution
        if use_cross_road_speed_limit is not None:
            self.use_cross_road_speed_limit = use_cross_road_speed_limit
        if use_only_cross_roads_with_straight_turn_type is not None:
            self.use_only_cross_roads_with_straight_turn_type = use_only_cross_roads_with_straight_turn_type

    @property
    def allow_crossing_peds(self) -> bool:
        return self.proto.allow_crossing_peds

    @allow_crossing_peds.setter
    def allow_crossing_peds(self, value: bool):
        self.proto.allow_crossing_peds = value

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

    @property
    def control_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._control_type_distribution

    @control_type_distribution.setter
    def control_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self._control_type_distribution.proto.CopyFrom(value.proto)

    @property
    def cross_road_speed_limit_mps(self) -> _pd_unified_generator_pb2.MinMaxConfigFloat:
        return self._cross_road_speed_limit_mps

    @cross_road_speed_limit_mps.setter
    def cross_road_speed_limit_mps(self, value: _pd_unified_generator_pb2.MinMaxConfigFloat):
        self._cross_road_speed_limit_mps.proto.CopyFrom(value.proto)

    @property
    def crowd_density(self) -> float:
        return self.proto.crowd_density

    @crowd_density.setter
    def crowd_density(self, value: float):
        self.proto.crowd_density = value

    @property
    def ego_stopped_at_junction(self) -> bool:
        return self.proto.ego_stopped_at_junction

    @ego_stopped_at_junction.setter
    def ego_stopped_at_junction(self, value: bool):
        self.proto.ego_stopped_at_junction = value

    @property
    def enable_prop_occlusions(self) -> bool:
        return self.proto.enable_prop_occlusions

    @enable_prop_occlusions.setter
    def enable_prop_occlusions(self, value: bool):
        self.proto.enable_prop_occlusions = value

    @property
    def enable_vehicle_occlusions(self) -> bool:
        return self.proto.enable_vehicle_occlusions

    @enable_vehicle_occlusions.setter
    def enable_vehicle_occlusions(self, value: bool):
        self.proto.enable_vehicle_occlusions = value

    @property
    def force_cross_traffic(self) -> bool:
        return self.proto.force_cross_traffic

    @force_cross_traffic.setter
    def force_cross_traffic(self, value: bool):
        self.proto.force_cross_traffic = value

    @property
    def geometry_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._geometry_type_distribution

    @geometry_type_distribution.setter
    def geometry_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self._geometry_type_distribution.proto.CopyFrom(value.proto)

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
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def occlusion_offset_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._occlusion_offset_dist

    @occlusion_offset_dist.setter
    def occlusion_offset_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._occlusion_offset_dist.proto.CopyFrom(value.proto)

    @property
    def prop_occlusion_count_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._prop_occlusion_count_dist

    @prop_occlusion_count_dist.setter
    def prop_occlusion_count_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self._prop_occlusion_count_dist.proto.CopyFrom(value.proto)

    @property
    def prop_occlusion_spacing_dist(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._prop_occlusion_spacing_dist

    @prop_occlusion_spacing_dist.setter
    def prop_occlusion_spacing_dist(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._prop_occlusion_spacing_dist.proto.CopyFrom(value.proto)

    @property
    def road_type_distribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._road_type_distribution

    @road_type_distribution.setter
    def road_type_distribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self._road_type_distribution.proto.CopyFrom(value.proto)

    @property
    def signal_light_distribution(self) -> _pd_unified_generator_pb2.SignalLightDistribution:
        return self._signal_light_distribution

    @signal_light_distribution.setter
    def signal_light_distribution(self, value: _pd_unified_generator_pb2.SignalLightDistribution):
        self._signal_light_distribution.proto.CopyFrom(value.proto)

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self._turn_type_distribution.proto.CopyFrom(value.proto)

    @property
    def use_cross_road_speed_limit(self) -> bool:
        return self.proto.use_cross_road_speed_limit

    @use_cross_road_speed_limit.setter
    def use_cross_road_speed_limit(self, value: bool):
        self.proto.use_cross_road_speed_limit = value

    @property
    def use_only_cross_roads_with_straight_turn_type(self) -> bool:
        return self.proto.use_only_cross_roads_with_straight_turn_type

    @use_only_cross_roads_with_straight_turn_type.setter
    def use_only_cross_roads_with_straight_turn_type(self, value: bool):
        self.proto.use_only_cross_roads_with_straight_turn_type = value

@register_wrapper(proto_type=pd_spawn_pb2.KittiScenarioGenerator)
class KittiScenarioGenerator(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.KittiScenarioGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.KittiScenarioGenerator]=None, max_distance_to_junction: Optional[float]=None, min_distance_to_junction: Optional[float]=None, turn_type_distribution: Optional[_pd_unified_generator_pb2.TurnTypeDistribution]=None):
        if proto is None:
            proto = pd_spawn_pb2.KittiScenarioGenerator()
        self.proto = proto
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(proto=proto.turn_type_distribution)
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self._turn_type_distribution.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.KittiScenarioGeneratorInfo)
class KittiScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.KittiScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.KittiScenarioGeneratorInfo]=None, max_distance_to_junction: Optional[float]=None, min_distance_to_junction: Optional[float]=None, turn_type_distribution: Optional[_pd_unified_generator_pb2.TurnTypeDistribution]=None):
        if proto is None:
            proto = pd_spawn_pb2.KittiScenarioGeneratorInfo()
        self.proto = proto
        self._turn_type_distribution = get_wrapper(proto_type=proto.turn_type_distribution.__class__)(proto=proto.turn_type_distribution)
        if max_distance_to_junction is not None:
            self.max_distance_to_junction = max_distance_to_junction
        if min_distance_to_junction is not None:
            self.min_distance_to_junction = min_distance_to_junction
        if turn_type_distribution is not None:
            self.turn_type_distribution = turn_type_distribution

    @property
    def max_distance_to_junction(self) -> float:
        return self.proto.max_distance_to_junction

    @max_distance_to_junction.setter
    def max_distance_to_junction(self, value: float):
        self.proto.max_distance_to_junction = value

    @property
    def min_distance_to_junction(self) -> float:
        return self.proto.min_distance_to_junction

    @min_distance_to_junction.setter
    def min_distance_to_junction(self, value: float):
        self.proto.min_distance_to_junction = value

    @property
    def turn_type_distribution(self) -> _pd_unified_generator_pb2.TurnTypeDistribution:
        return self._turn_type_distribution

    @turn_type_distribution.setter
    def turn_type_distribution(self, value: _pd_unified_generator_pb2.TurnTypeDistribution):
        self._turn_type_distribution.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.LaneTypeScenarioGeneratorInfo)
class LaneTypeScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.LaneTypeScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.LaneTypeScenarioGeneratorInfo]=None, asset_search_radius: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, asset_tags: Optional[str]=None, dead_zone: Optional[float]=None, dead_zone_spread: Optional[float]=None, lane_type: Optional[int]=None, num_instances: Optional[_pd_unified_generator_pb2.MinMaxConfigInt]=None):
        if proto is None:
            proto = pd_spawn_pb2.LaneTypeScenarioGeneratorInfo()
        self.proto = proto
        self._asset_search_radius = get_wrapper(proto_type=proto.asset_search_radius.__class__)(proto=proto.asset_search_radius)
        self._num_instances = get_wrapper(proto_type=proto.num_instances.__class__)(proto=proto.num_instances)
        if asset_search_radius is not None:
            self.asset_search_radius = asset_search_radius
        if asset_tags is not None:
            self.asset_tags = asset_tags
        if dead_zone is not None:
            self.dead_zone = dead_zone
        if dead_zone_spread is not None:
            self.dead_zone_spread = dead_zone_spread
        if lane_type is not None:
            self.lane_type = lane_type
        if num_instances is not None:
            self.num_instances = num_instances

    @property
    def asset_search_radius(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._asset_search_radius

    @asset_search_radius.setter
    def asset_search_radius(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._asset_search_radius.proto.CopyFrom(value.proto)

    @property
    def asset_tags(self) -> str:
        return self.proto.asset_tags

    @asset_tags.setter
    def asset_tags(self, value: str):
        self.proto.asset_tags = value

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
    def lane_type(self) -> int:
        return self.proto.lane_type

    @lane_type.setter
    def lane_type(self, value: int):
        self.proto.lane_type = value

    @property
    def num_instances(self) -> _pd_unified_generator_pb2.MinMaxConfigInt:
        return self._num_instances

    @num_instances.setter
    def num_instances(self, value: _pd_unified_generator_pb2.MinMaxConfigInt):
        self._num_instances.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.ParkingScenarioGeneratorInfo)
class ParkingScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.ParkingScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.ParkingScenarioGeneratorInfo]=None, aisleLateralOffsetBackIn: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, aisleLateralOffsetNoseIn: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, egoParkPerturbationAngle: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, egoParkPerturbationLateralOffset: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, egoParkPerturbationLongitudinalOffset: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, exitAfterParking: Optional[bool]=None, exitStraight: Optional[bool]=None, maxPedsInParkingSpaces: Optional[int]=None, noseInProbability: Optional[float]=None, parkingSpacePedestrianDensity: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, parkingTypeDistribution: Optional[_pd_distributions_pb2.EnumDistribution]=None, perpendicularOnRoadProbability: Optional[float]=None, placeVehicleInFrontOfParallelSpot: Optional[bool]=None, pullOutProbability: Optional[float]=None, timeToParkingSpace: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None):
        if proto is None:
            proto = pd_spawn_pb2.ParkingScenarioGeneratorInfo()
        self.proto = proto
        self._aisleLateralOffsetBackIn = get_wrapper(proto_type=proto.aisleLateralOffsetBackIn.__class__)(proto=proto.aisleLateralOffsetBackIn)
        self._aisleLateralOffsetNoseIn = get_wrapper(proto_type=proto.aisleLateralOffsetNoseIn.__class__)(proto=proto.aisleLateralOffsetNoseIn)
        self._egoParkPerturbationAngle = get_wrapper(proto_type=proto.egoParkPerturbationAngle.__class__)(proto=proto.egoParkPerturbationAngle)
        self._egoParkPerturbationLateralOffset = get_wrapper(proto_type=proto.egoParkPerturbationLateralOffset.__class__)(proto=proto.egoParkPerturbationLateralOffset)
        self._egoParkPerturbationLongitudinalOffset = get_wrapper(proto_type=proto.egoParkPerturbationLongitudinalOffset.__class__)(proto=proto.egoParkPerturbationLongitudinalOffset)
        self._parkingSpacePedestrianDensity = get_wrapper(proto_type=proto.parkingSpacePedestrianDensity.__class__)(proto=proto.parkingSpacePedestrianDensity)
        self._parkingTypeDistribution = get_wrapper(proto_type=proto.parkingTypeDistribution.__class__)(proto=proto.parkingTypeDistribution)
        self._timeToParkingSpace = get_wrapper(proto_type=proto.timeToParkingSpace.__class__)(proto=proto.timeToParkingSpace)
        if aisleLateralOffsetBackIn is not None:
            self.aisleLateralOffsetBackIn = aisleLateralOffsetBackIn
        if aisleLateralOffsetNoseIn is not None:
            self.aisleLateralOffsetNoseIn = aisleLateralOffsetNoseIn
        if egoParkPerturbationAngle is not None:
            self.egoParkPerturbationAngle = egoParkPerturbationAngle
        if egoParkPerturbationLateralOffset is not None:
            self.egoParkPerturbationLateralOffset = egoParkPerturbationLateralOffset
        if egoParkPerturbationLongitudinalOffset is not None:
            self.egoParkPerturbationLongitudinalOffset = egoParkPerturbationLongitudinalOffset
        if exitAfterParking is not None:
            self.exitAfterParking = exitAfterParking
        if exitStraight is not None:
            self.exitStraight = exitStraight
        if maxPedsInParkingSpaces is not None:
            self.maxPedsInParkingSpaces = maxPedsInParkingSpaces
        if noseInProbability is not None:
            self.noseInProbability = noseInProbability
        if parkingSpacePedestrianDensity is not None:
            self.parkingSpacePedestrianDensity = parkingSpacePedestrianDensity
        if parkingTypeDistribution is not None:
            self.parkingTypeDistribution = parkingTypeDistribution
        if perpendicularOnRoadProbability is not None:
            self.perpendicularOnRoadProbability = perpendicularOnRoadProbability
        if placeVehicleInFrontOfParallelSpot is not None:
            self.placeVehicleInFrontOfParallelSpot = placeVehicleInFrontOfParallelSpot
        if pullOutProbability is not None:
            self.pullOutProbability = pullOutProbability
        if timeToParkingSpace is not None:
            self.timeToParkingSpace = timeToParkingSpace

    @property
    def aisleLateralOffsetBackIn(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._aisleLateralOffsetBackIn

    @aisleLateralOffsetBackIn.setter
    def aisleLateralOffsetBackIn(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._aisleLateralOffsetBackIn.proto.CopyFrom(value.proto)

    @property
    def aisleLateralOffsetNoseIn(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._aisleLateralOffsetNoseIn

    @aisleLateralOffsetNoseIn.setter
    def aisleLateralOffsetNoseIn(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._aisleLateralOffsetNoseIn.proto.CopyFrom(value.proto)

    @property
    def egoParkPerturbationAngle(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationAngle

    @egoParkPerturbationAngle.setter
    def egoParkPerturbationAngle(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._egoParkPerturbationAngle.proto.CopyFrom(value.proto)

    @property
    def egoParkPerturbationLateralOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationLateralOffset

    @egoParkPerturbationLateralOffset.setter
    def egoParkPerturbationLateralOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._egoParkPerturbationLateralOffset.proto.CopyFrom(value.proto)

    @property
    def egoParkPerturbationLongitudinalOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._egoParkPerturbationLongitudinalOffset

    @egoParkPerturbationLongitudinalOffset.setter
    def egoParkPerturbationLongitudinalOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._egoParkPerturbationLongitudinalOffset.proto.CopyFrom(value.proto)

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
    def maxPedsInParkingSpaces(self) -> int:
        return self.proto.maxPedsInParkingSpaces

    @maxPedsInParkingSpaces.setter
    def maxPedsInParkingSpaces(self, value: int):
        self.proto.maxPedsInParkingSpaces = value

    @property
    def noseInProbability(self) -> float:
        return self.proto.noseInProbability

    @noseInProbability.setter
    def noseInProbability(self, value: float):
        self.proto.noseInProbability = value

    @property
    def parkingSpacePedestrianDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._parkingSpacePedestrianDensity

    @parkingSpacePedestrianDensity.setter
    def parkingSpacePedestrianDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._parkingSpacePedestrianDensity.proto.CopyFrom(value.proto)

    @property
    def parkingTypeDistribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._parkingTypeDistribution

    @parkingTypeDistribution.setter
    def parkingTypeDistribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self._parkingTypeDistribution.proto.CopyFrom(value.proto)

    @property
    def perpendicularOnRoadProbability(self) -> float:
        return self.proto.perpendicularOnRoadProbability

    @perpendicularOnRoadProbability.setter
    def perpendicularOnRoadProbability(self, value: float):
        self.proto.perpendicularOnRoadProbability = value

    @property
    def placeVehicleInFrontOfParallelSpot(self) -> bool:
        return self.proto.placeVehicleInFrontOfParallelSpot

    @placeVehicleInFrontOfParallelSpot.setter
    def placeVehicleInFrontOfParallelSpot(self, value: bool):
        self.proto.placeVehicleInFrontOfParallelSpot = value

    @property
    def pullOutProbability(self) -> float:
        return self.proto.pullOutProbability

    @pullOutProbability.setter
    def pullOutProbability(self, value: float):
        self.proto.pullOutProbability = value

    @property
    def timeToParkingSpace(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._timeToParkingSpace

    @timeToParkingSpace.setter
    def timeToParkingSpace(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._timeToParkingSpace.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.PositionGenerator)
class PositionGenerator(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.PositionGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.PositionGenerator]=None, ego_behind_star: Optional[bool]=None, face_same_direction: Optional[bool]=None, junction_ids: Optional[List[int]]=None, radius_to_star_max: Optional[float]=None, radius_to_star_min: Optional[float]=None, star_vehicles: Optional[List[str]]=None):
        if proto is None:
            proto = pd_spawn_pb2.PositionGenerator()
        self.proto = proto
        self._junction_ids = ProtoListWrapper(container=[int(v) for v in proto.junction_ids], attr_name='junction_ids', list_owner=proto)
        self._star_vehicles = ProtoListWrapper(container=[str(v) for v in proto.star_vehicles], attr_name='star_vehicles', list_owner=proto)
        if ego_behind_star is not None:
            self.ego_behind_star = ego_behind_star
        if face_same_direction is not None:
            self.face_same_direction = face_same_direction
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if radius_to_star_max is not None:
            self.radius_to_star_max = radius_to_star_max
        if radius_to_star_min is not None:
            self.radius_to_star_min = radius_to_star_min
        if star_vehicles is not None:
            self.star_vehicles = star_vehicles

    @property
    def ego_behind_star(self) -> bool:
        return self.proto.ego_behind_star

    @ego_behind_star.setter
    def ego_behind_star(self, value: bool):
        self.proto.ego_behind_star = value

    @property
    def face_same_direction(self) -> bool:
        return self.proto.face_same_direction

    @face_same_direction.setter
    def face_same_direction(self, value: bool):
        self.proto.face_same_direction = value

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

    @property
    def radius_to_star_max(self) -> float:
        return self.proto.radius_to_star_max

    @radius_to_star_max.setter
    def radius_to_star_max(self, value: float):
        self.proto.radius_to_star_max = value

    @property
    def radius_to_star_min(self) -> float:
        return self.proto.radius_to_star_min

    @radius_to_star_min.setter
    def radius_to_star_min(self, value: float):
        self.proto.radius_to_star_min = value

    @property
    def star_vehicles(self) -> List[str]:
        return self._star_vehicles

    @star_vehicles.setter
    def star_vehicles(self, value: List[str]):
        self._star_vehicles.clear()
        for v in value:
            self._star_vehicles.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.PropScenarioGeneratorInfo)
class PropScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.PropScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.PropScenarioGeneratorInfo]=None, closureConeLength: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, closureConeLengthForSingleLaneClosure: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, closureConeSpacing: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, coneAssetTag: Optional[str]=None, coneSpacing: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, initialMessageBoardAssetTag: Optional[str]=None, initialMessageBoardRightAssetTag: Optional[str]=None, intermediateMessageBoardAngleVariation: Optional[float]=None, intermediateMessageBoardAssetTag: Optional[str]=None, intermediateMessageBoardRightAssetTag: Optional[str]=None, leadConeLength: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, leadConeLengthForSingleLaneClosure: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, leadConeSpacing: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, maxConeAngleDeviation: Optional[float]=None, maxConeSpacingDeviationPercent: Optional[float]=None, maxLanesToClose: Optional[int]=None, maxLateralClosureConeSpacingDeviation: Optional[float]=None, maxLateralLeadConeSpacingDeviation: Optional[float]=None, maxLateralTaperConeSpacingDeviation: Optional[float]=None, minLanesToClose: Optional[int]=None, minTaperLength: Optional[float]=None, missing_cone_chance: Optional[float]=None, num_fallen_cone_groups: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, placeClosureCones: Optional[bool]=None, placeIntermediateMessageBoards: Optional[bool]=None, placeIntermediateMessageBoardsProbability: Optional[float]=None, placeLeadCones: Optional[bool]=None, placeMessageBoard: Optional[bool]=None, propMaxDistance: Optional[float]=None, propMinDistance: Optional[float]=None, propTag: Optional[str]=None, propVehicleTag: Optional[str]=None, reduce_spawn_to_zero_at_construction_range: Optional[float]=None, rightSideClosureProbability: Optional[float]=None, scenario_cull_on_bad_cone_fov: Optional[float]=None, scenario_cull_on_bad_cone_los: Optional[bool]=None, size_fallen_cone_groups: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, suffix_fallen_cone_assets: Optional[str]=None, taperLengthScaleFactor: Optional[float]=None, taperLengthSpeedSpreadPercent: Optional[float]=None, taperLowerSpeedThreshold: Optional[float]=None, taperSlowFormulaDemoninator: Optional[float]=None, taperUpperSpeedThreshold: Optional[float]=None, vehiclePlacementProbability: Optional[float]=None):
        if proto is None:
            proto = pd_spawn_pb2.PropScenarioGeneratorInfo()
        self.proto = proto
        self._closureConeLength = get_wrapper(proto_type=proto.closureConeLength.__class__)(proto=proto.closureConeLength)
        self._closureConeLengthForSingleLaneClosure = get_wrapper(proto_type=proto.closureConeLengthForSingleLaneClosure.__class__)(proto=proto.closureConeLengthForSingleLaneClosure)
        self._closureConeSpacing = get_wrapper(proto_type=proto.closureConeSpacing.__class__)(proto=proto.closureConeSpacing)
        self._coneSpacing = get_wrapper(proto_type=proto.coneSpacing.__class__)(proto=proto.coneSpacing)
        self._leadConeLength = get_wrapper(proto_type=proto.leadConeLength.__class__)(proto=proto.leadConeLength)
        self._leadConeLengthForSingleLaneClosure = get_wrapper(proto_type=proto.leadConeLengthForSingleLaneClosure.__class__)(proto=proto.leadConeLengthForSingleLaneClosure)
        self._leadConeSpacing = get_wrapper(proto_type=proto.leadConeSpacing.__class__)(proto=proto.leadConeSpacing)
        self._num_fallen_cone_groups = get_wrapper(proto_type=proto.num_fallen_cone_groups.__class__)(proto=proto.num_fallen_cone_groups)
        self._size_fallen_cone_groups = get_wrapper(proto_type=proto.size_fallen_cone_groups.__class__)(proto=proto.size_fallen_cone_groups)
        if closureConeLength is not None:
            self.closureConeLength = closureConeLength
        if closureConeLengthForSingleLaneClosure is not None:
            self.closureConeLengthForSingleLaneClosure = closureConeLengthForSingleLaneClosure
        if closureConeSpacing is not None:
            self.closureConeSpacing = closureConeSpacing
        if coneAssetTag is not None:
            self.coneAssetTag = coneAssetTag
        if coneSpacing is not None:
            self.coneSpacing = coneSpacing
        if initialMessageBoardAssetTag is not None:
            self.initialMessageBoardAssetTag = initialMessageBoardAssetTag
        if initialMessageBoardRightAssetTag is not None:
            self.initialMessageBoardRightAssetTag = initialMessageBoardRightAssetTag
        if intermediateMessageBoardAngleVariation is not None:
            self.intermediateMessageBoardAngleVariation = intermediateMessageBoardAngleVariation
        if intermediateMessageBoardAssetTag is not None:
            self.intermediateMessageBoardAssetTag = intermediateMessageBoardAssetTag
        if intermediateMessageBoardRightAssetTag is not None:
            self.intermediateMessageBoardRightAssetTag = intermediateMessageBoardRightAssetTag
        if leadConeLength is not None:
            self.leadConeLength = leadConeLength
        if leadConeLengthForSingleLaneClosure is not None:
            self.leadConeLengthForSingleLaneClosure = leadConeLengthForSingleLaneClosure
        if leadConeSpacing is not None:
            self.leadConeSpacing = leadConeSpacing
        if maxConeAngleDeviation is not None:
            self.maxConeAngleDeviation = maxConeAngleDeviation
        if maxConeSpacingDeviationPercent is not None:
            self.maxConeSpacingDeviationPercent = maxConeSpacingDeviationPercent
        if maxLanesToClose is not None:
            self.maxLanesToClose = maxLanesToClose
        if maxLateralClosureConeSpacingDeviation is not None:
            self.maxLateralClosureConeSpacingDeviation = maxLateralClosureConeSpacingDeviation
        if maxLateralLeadConeSpacingDeviation is not None:
            self.maxLateralLeadConeSpacingDeviation = maxLateralLeadConeSpacingDeviation
        if maxLateralTaperConeSpacingDeviation is not None:
            self.maxLateralTaperConeSpacingDeviation = maxLateralTaperConeSpacingDeviation
        if minLanesToClose is not None:
            self.minLanesToClose = minLanesToClose
        if minTaperLength is not None:
            self.minTaperLength = minTaperLength
        if missing_cone_chance is not None:
            self.missing_cone_chance = missing_cone_chance
        if num_fallen_cone_groups is not None:
            self.num_fallen_cone_groups = num_fallen_cone_groups
        if placeClosureCones is not None:
            self.placeClosureCones = placeClosureCones
        if placeIntermediateMessageBoards is not None:
            self.placeIntermediateMessageBoards = placeIntermediateMessageBoards
        if placeIntermediateMessageBoardsProbability is not None:
            self.placeIntermediateMessageBoardsProbability = placeIntermediateMessageBoardsProbability
        if placeLeadCones is not None:
            self.placeLeadCones = placeLeadCones
        if placeMessageBoard is not None:
            self.placeMessageBoard = placeMessageBoard
        if propMaxDistance is not None:
            self.propMaxDistance = propMaxDistance
        if propMinDistance is not None:
            self.propMinDistance = propMinDistance
        if propTag is not None:
            self.propTag = propTag
        if propVehicleTag is not None:
            self.propVehicleTag = propVehicleTag
        if reduce_spawn_to_zero_at_construction_range is not None:
            self.reduce_spawn_to_zero_at_construction_range = reduce_spawn_to_zero_at_construction_range
        if rightSideClosureProbability is not None:
            self.rightSideClosureProbability = rightSideClosureProbability
        if scenario_cull_on_bad_cone_fov is not None:
            self.scenario_cull_on_bad_cone_fov = scenario_cull_on_bad_cone_fov
        if scenario_cull_on_bad_cone_los is not None:
            self.scenario_cull_on_bad_cone_los = scenario_cull_on_bad_cone_los
        if size_fallen_cone_groups is not None:
            self.size_fallen_cone_groups = size_fallen_cone_groups
        if suffix_fallen_cone_assets is not None:
            self.suffix_fallen_cone_assets = suffix_fallen_cone_assets
        if taperLengthScaleFactor is not None:
            self.taperLengthScaleFactor = taperLengthScaleFactor
        if taperLengthSpeedSpreadPercent is not None:
            self.taperLengthSpeedSpreadPercent = taperLengthSpeedSpreadPercent
        if taperLowerSpeedThreshold is not None:
            self.taperLowerSpeedThreshold = taperLowerSpeedThreshold
        if taperSlowFormulaDemoninator is not None:
            self.taperSlowFormulaDemoninator = taperSlowFormulaDemoninator
        if taperUpperSpeedThreshold is not None:
            self.taperUpperSpeedThreshold = taperUpperSpeedThreshold
        if vehiclePlacementProbability is not None:
            self.vehiclePlacementProbability = vehiclePlacementProbability

    @property
    def closureConeLength(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeLength

    @closureConeLength.setter
    def closureConeLength(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._closureConeLength.proto.CopyFrom(value.proto)

    @property
    def closureConeLengthForSingleLaneClosure(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeLengthForSingleLaneClosure

    @closureConeLengthForSingleLaneClosure.setter
    def closureConeLengthForSingleLaneClosure(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._closureConeLengthForSingleLaneClosure.proto.CopyFrom(value.proto)

    @property
    def closureConeSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._closureConeSpacing

    @closureConeSpacing.setter
    def closureConeSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._closureConeSpacing.proto.CopyFrom(value.proto)

    @property
    def coneAssetTag(self) -> str:
        return self.proto.coneAssetTag

    @coneAssetTag.setter
    def coneAssetTag(self, value: str):
        self.proto.coneAssetTag = value

    @property
    def coneSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._coneSpacing

    @coneSpacing.setter
    def coneSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._coneSpacing.proto.CopyFrom(value.proto)

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
    def intermediateMessageBoardAngleVariation(self) -> float:
        return self.proto.intermediateMessageBoardAngleVariation

    @intermediateMessageBoardAngleVariation.setter
    def intermediateMessageBoardAngleVariation(self, value: float):
        self.proto.intermediateMessageBoardAngleVariation = value

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
    def leadConeLength(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeLength

    @leadConeLength.setter
    def leadConeLength(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._leadConeLength.proto.CopyFrom(value.proto)

    @property
    def leadConeLengthForSingleLaneClosure(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeLengthForSingleLaneClosure

    @leadConeLengthForSingleLaneClosure.setter
    def leadConeLengthForSingleLaneClosure(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._leadConeLengthForSingleLaneClosure.proto.CopyFrom(value.proto)

    @property
    def leadConeSpacing(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._leadConeSpacing

    @leadConeSpacing.setter
    def leadConeSpacing(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._leadConeSpacing.proto.CopyFrom(value.proto)

    @property
    def maxConeAngleDeviation(self) -> float:
        return self.proto.maxConeAngleDeviation

    @maxConeAngleDeviation.setter
    def maxConeAngleDeviation(self, value: float):
        self.proto.maxConeAngleDeviation = value

    @property
    def maxConeSpacingDeviationPercent(self) -> float:
        return self.proto.maxConeSpacingDeviationPercent

    @maxConeSpacingDeviationPercent.setter
    def maxConeSpacingDeviationPercent(self, value: float):
        self.proto.maxConeSpacingDeviationPercent = value

    @property
    def maxLanesToClose(self) -> int:
        return self.proto.maxLanesToClose

    @maxLanesToClose.setter
    def maxLanesToClose(self, value: int):
        self.proto.maxLanesToClose = value

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
    def maxLateralTaperConeSpacingDeviation(self) -> float:
        return self.proto.maxLateralTaperConeSpacingDeviation

    @maxLateralTaperConeSpacingDeviation.setter
    def maxLateralTaperConeSpacingDeviation(self, value: float):
        self.proto.maxLateralTaperConeSpacingDeviation = value

    @property
    def minLanesToClose(self) -> int:
        return self.proto.minLanesToClose

    @minLanesToClose.setter
    def minLanesToClose(self, value: int):
        self.proto.minLanesToClose = value

    @property
    def minTaperLength(self) -> float:
        return self.proto.minTaperLength

    @minTaperLength.setter
    def minTaperLength(self, value: float):
        self.proto.minTaperLength = value

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
        self._num_fallen_cone_groups.proto.CopyFrom(value.proto)

    @property
    def placeClosureCones(self) -> bool:
        return self.proto.placeClosureCones

    @placeClosureCones.setter
    def placeClosureCones(self, value: bool):
        self.proto.placeClosureCones = value

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
    def placeLeadCones(self) -> bool:
        return self.proto.placeLeadCones

    @placeLeadCones.setter
    def placeLeadCones(self, value: bool):
        self.proto.placeLeadCones = value

    @property
    def placeMessageBoard(self) -> bool:
        return self.proto.placeMessageBoard

    @placeMessageBoard.setter
    def placeMessageBoard(self, value: bool):
        self.proto.placeMessageBoard = value

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
    def propTag(self) -> str:
        return self.proto.propTag

    @propTag.setter
    def propTag(self, value: str):
        self.proto.propTag = value

    @property
    def propVehicleTag(self) -> str:
        return self.proto.propVehicleTag

    @propVehicleTag.setter
    def propVehicleTag(self, value: str):
        self.proto.propVehicleTag = value

    @property
    def reduce_spawn_to_zero_at_construction_range(self) -> float:
        return self.proto.reduce_spawn_to_zero_at_construction_range

    @reduce_spawn_to_zero_at_construction_range.setter
    def reduce_spawn_to_zero_at_construction_range(self, value: float):
        self.proto.reduce_spawn_to_zero_at_construction_range = value

    @property
    def rightSideClosureProbability(self) -> float:
        return self.proto.rightSideClosureProbability

    @rightSideClosureProbability.setter
    def rightSideClosureProbability(self, value: float):
        self.proto.rightSideClosureProbability = value

    @property
    def scenario_cull_on_bad_cone_fov(self) -> float:
        return self.proto.scenario_cull_on_bad_cone_fov

    @scenario_cull_on_bad_cone_fov.setter
    def scenario_cull_on_bad_cone_fov(self, value: float):
        self.proto.scenario_cull_on_bad_cone_fov = value

    @property
    def scenario_cull_on_bad_cone_los(self) -> bool:
        return self.proto.scenario_cull_on_bad_cone_los

    @scenario_cull_on_bad_cone_los.setter
    def scenario_cull_on_bad_cone_los(self, value: bool):
        self.proto.scenario_cull_on_bad_cone_los = value

    @property
    def size_fallen_cone_groups(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._size_fallen_cone_groups

    @size_fallen_cone_groups.setter
    def size_fallen_cone_groups(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._size_fallen_cone_groups.proto.CopyFrom(value.proto)

    @property
    def suffix_fallen_cone_assets(self) -> str:
        return self.proto.suffix_fallen_cone_assets

    @suffix_fallen_cone_assets.setter
    def suffix_fallen_cone_assets(self, value: str):
        self.proto.suffix_fallen_cone_assets = value

    @property
    def taperLengthScaleFactor(self) -> float:
        return self.proto.taperLengthScaleFactor

    @taperLengthScaleFactor.setter
    def taperLengthScaleFactor(self, value: float):
        self.proto.taperLengthScaleFactor = value

    @property
    def taperLengthSpeedSpreadPercent(self) -> float:
        return self.proto.taperLengthSpeedSpreadPercent

    @taperLengthSpeedSpreadPercent.setter
    def taperLengthSpeedSpreadPercent(self, value: float):
        self.proto.taperLengthSpeedSpreadPercent = value

    @property
    def taperLowerSpeedThreshold(self) -> float:
        return self.proto.taperLowerSpeedThreshold

    @taperLowerSpeedThreshold.setter
    def taperLowerSpeedThreshold(self, value: float):
        self.proto.taperLowerSpeedThreshold = value

    @property
    def taperSlowFormulaDemoninator(self) -> float:
        return self.proto.taperSlowFormulaDemoninator

    @taperSlowFormulaDemoninator.setter
    def taperSlowFormulaDemoninator(self, value: float):
        self.proto.taperSlowFormulaDemoninator = value

    @property
    def taperUpperSpeedThreshold(self) -> float:
        return self.proto.taperUpperSpeedThreshold

    @taperUpperSpeedThreshold.setter
    def taperUpperSpeedThreshold(self, value: float):
        self.proto.taperUpperSpeedThreshold = value

    @property
    def vehiclePlacementProbability(self) -> float:
        return self.proto.vehiclePlacementProbability

    @vehiclePlacementProbability.setter
    def vehiclePlacementProbability(self, value: float):
        self.proto.vehiclePlacementProbability = value

@register_wrapper(proto_type=pd_spawn_pb2.RandomLaneScenarioGeneratorInfo)
class RandomLaneScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.RandomLaneScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.RandomLaneScenarioGeneratorInfo]=None):
        if proto is None:
            proto = pd_spawn_pb2.RandomLaneScenarioGeneratorInfo()
        self.proto = proto

@register_wrapper(proto_type=pd_spawn_pb2.RandomScenarioGenerator)
class RandomScenarioGenerator(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.RandomScenarioGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.RandomScenarioGenerator]=None):
        if proto is None:
            proto = pd_spawn_pb2.RandomScenarioGenerator()
        self.proto = proto

@register_wrapper(proto_type=pd_spawn_pb2.SpawnConfig)
class SpawnConfig(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.SpawnConfig

    def __init__(self, *, proto: Optional[pd_spawn_pb2.SpawnConfig]=None, preset_distribution: Optional[_pd_distributions_pb2.CategoricalDistribution]=None, presets: Optional[List[SpawnConfigPreset]]=None):
        if proto is None:
            proto = pd_spawn_pb2.SpawnConfig()
        self.proto = proto
        self._preset_distribution = get_wrapper(proto_type=proto.preset_distribution.__class__)(proto=proto.preset_distribution)
        self._presets = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.presets], attr_name='presets', list_owner=proto)
        if preset_distribution is not None:
            self.preset_distribution = preset_distribution
        if presets is not None:
            self.presets = presets

    @property
    def preset_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._preset_distribution

    @preset_distribution.setter
    def preset_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self._preset_distribution.proto.CopyFrom(value.proto)

    @property
    def presets(self) -> List[SpawnConfigPreset]:
        return self._presets

    @presets.setter
    def presets(self, value: List[SpawnConfigPreset]):
        self._presets.clear()
        for v in value:
            self._presets.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.SpawnConfigPreset)
class SpawnConfigPreset(ProtoMessageClass):

    @register_wrapper(proto_type=pd_spawn_pb2.SpawnConfigPreset.RoadType)
    class RoadType(ProtoEnumClass):
        _proto_message = pd_spawn_pb2.SpawnConfigPreset.RoadType
        DRIVEWAY: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.DRIVEWAY
        MOTORWAY: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.MOTORWAY
        MOTORWAY_LINK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.MOTORWAY_LINK
        PARKING_AISLE: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.PARKING_AISLE
        PRIMARY: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.PRIMARY
        PRIMARY_LINK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.PRIMARY_LINK
        RESIDENTIAL: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.RESIDENTIAL
        SECONDARY: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.SECONDARY
        SECONDARY_LINK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.SECONDARY_LINK
        SERVICE: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.SERVICE
        TERTIARY: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.TERTIARY
        TERTIARY_LINK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.TERTIARY_LINK
        TRUNK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.TRUNK
        TRUNK_LINK: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.TRUNK_LINK
        UNCLASSIFIED: pd_spawn_pb2.SpawnConfigPreset.RoadType = pd_spawn_pb2.SpawnConfigPreset.RoadType.UNCLASSIFIED
    _proto_message = pd_spawn_pb2.SpawnConfigPreset

    def __init__(self, *, proto: Optional[pd_spawn_pb2.SpawnConfigPreset]=None, agentStateProbabilities: Optional[List[AgentStateProbabilityConfig]]=None, aggression: Optional[float]=None, aggressionSpread: Optional[float]=None, alignEgoPedestrianToLane: Optional[bool]=None, animalSpeciesAllowed: Optional[str]=None, applyProceedOutOfTurnProbabilityToEgo: Optional[bool]=None, applyRollingStopToEgo: Optional[bool]=None, applyStopLineOffsetToEgo: Optional[bool]=None, bicyclesOnlyInBikeLanes: Optional[bool]=None, crosswalkSignDensity: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, disableAccessories: Optional[bool]=None, disableOccupants: Optional[bool]=None, egoForceMinLengthBehind: Optional[bool]=None, egoIgnoreObstacleTypes: Optional[List[str]]=None, egoLaneChangeChance: Optional[float]=None, egoLaneChangeChanceSpread: Optional[float]=None, egoLaneChangeCooldown: Optional[float]=None, egoLaneChangeCooldownSpread: Optional[float]=None, egoMinDistToEdge: Optional[float]=None, egoMinDistToEdgeSpread: Optional[float]=None, egoMinLaneCountDist: Optional[_pd_unified_generator_pb2.CenterSpreadConfigInt]=None, egoMinPathLength: Optional[float]=None, egoMinPathLengthSpread: Optional[float]=None, egoPedestrianExclusionRadius: Optional[float]=None, egoPedestrianExclusionRadiusSpread: Optional[float]=None, egoPedestrians: Optional[bool]=None, egoRoadTypes: Optional[List[SpawnConfigPreset.RoadType]]=None, egoVehicleModel: Optional[str]=None, ego_parking_space_decoration_params: Optional[_pd_unified_generator_pb2.ObjectDecorationParams]=None, emergencyLightsOnProbability: Optional[float]=None, emergencyLightsOnProbabilitySpread: Optional[float]=None, enableCrosswalkPlacement: Optional[bool]=None, enableDrivewayPlacement: Optional[bool]=None, enableDynamicLaneSelection: Optional[bool]=None, enableJunctionPlacement: Optional[bool]=None, instanceParallelParkingMarkers: Optional[bool]=None, instanceParallelParkingSpaces: Optional[bool]=None, junction_generator: Optional[JunctionScenarioGenerator]=None, kitti_generator: Optional[KittiScenarioGenerator]=None, laneChangeChance: Optional[float]=None, laneChangeChanceSpread: Optional[float]=None, laneChangeCooldown: Optional[float]=None, laneChangeCooldownSpread: Optional[float]=None, laneDriftAmp: Optional[float]=None, laneDriftAmpSpread: Optional[float]=None, laneDriftScale: Optional[float]=None, laneDriftScaleSpread: Optional[float]=None, laneOffset: Optional[float]=None, laneOffsetSpread: Optional[float]=None, laneStartOffset: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, largeVehicleTurnRadiusMultiple: Optional[float]=None, lightFlashingPeriod: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, lightIlluminatedPercentage: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, markerDataMap: Optional[Dict[str, _pd_unified_generator_pb2.RoadMarkingData]]=None, minNumberOfAnimals: Optional[int]=None, minNumberOfPedestrians: Optional[int]=None, numberOfAnimals: Optional[int]=None, numberOfPedestrians: Optional[int]=None, object_decoration_params: Optional[_pd_unified_generator_pb2.ObjectDecorationParams]=None, object_decoration_radius: Optional[float]=None, parkedVehicleSpawnProbability: Optional[float]=None, parkedVehicleSpawnProbabilitySpread: Optional[float]=None, parkedVehicleSpawnRadius: Optional[float]=None, parkingTypeDistribution: Optional[_pd_unified_generator_pb2.ParkingTypeDistribution]=None, parking_space_data: Optional[_pd_unified_generator_pb2.ParkingSpaceData]=None, pedestrianColorOverrideChance: Optional[float]=None, pedestrianColorOverrideChanceSpread: Optional[float]=None, pedestrianColorOverrideRGB: Optional[List[float]]=None, pedestrianIdleProbability: Optional[float]=None, pedestrianIdleProbabilitySpread: Optional[float]=None, pedestrianJaywalkAngle: Optional[float]=None, pedestrianJaywalkLookAhead: Optional[float]=None, pedestrianJaywalkRadius: Optional[float]=None, pedestrianSpawnMinEdgeDistance: Optional[float]=None, pedestrianSpawnRadius: Optional[float]=None, pedestrianSpawnTightness: Optional[float]=None, pedestrianVelocity: Optional[float]=None, pedestrianVelocitySpread: Optional[float]=None, pedestriansDynamicPathing: Optional[bool]=None, pedestriansSpawnInParkingLot: Optional[bool]=None, position_generator: Optional[PositionGenerator]=None, proceedOutOfTurnProbability: Optional[float]=None, random_generator: Optional[RandomScenarioGenerator]=None, randomizeVehicleParts: Optional[bool]=None, region: Optional[str]=None, restrictLargeVehicleLaneCurvature: Optional[bool]=None, rollingStop: Optional[_pd_unified_generator_pb2.CenterSpreadProbabilityConfig]=None, searchRadius: Optional[float]=None, signDensity: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, spawnPedestriansOnRoad: Optional[bool]=None, spawnTrailerOnEgoProbability: Optional[float]=None, spawnTrailerProbabilities: Optional[Dict[str, float]]=None, startSeparation: Optional[float]=None, startSeparationSpread: Optional[float]=None, startSeparationTime: Optional[Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]]=None, startVelocity: Optional[float]=None, startVelocitySpread: Optional[float]=None, stopLineOffset: Optional[_pd_unified_generator_pb2.CenterSpreadProbabilityConfig]=None, targetSeparation: Optional[float]=None, targetSeparationSpread: Optional[float]=None, targetSeparationTime: Optional[Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]]=None, targetVelocity: Optional[float]=None, targetVelocitySpread: Optional[float]=None, turnTypeDistribution: Optional[_pd_distributions_pb2.EnumDistribution]=None, useStaticTrailers: Optional[bool]=None, vehicleDensityModifier: Optional[float]=None, vehicleDistribution: Optional[Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]]=None, vehicleRoadTypes: Optional[List[SpawnConfigPreset.RoadType]]=None, voi_generator: Optional[VehicleOfInterestGenerator]=None):
        if proto is None:
            proto = pd_spawn_pb2.SpawnConfigPreset()
        self.proto = proto
        self._agentStateProbabilities = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.agentStateProbabilities], attr_name='agentStateProbabilities', list_owner=proto)
        self._crosswalkSignDensity = get_wrapper(proto_type=proto.crosswalkSignDensity.__class__)(proto=proto.crosswalkSignDensity)
        self._egoIgnoreObstacleTypes = ProtoListWrapper(container=[str(v) for v in proto.egoIgnoreObstacleTypes], attr_name='egoIgnoreObstacleTypes', list_owner=proto)
        self._egoMinLaneCountDist = get_wrapper(proto_type=proto.egoMinLaneCountDist.__class__)(proto=proto.egoMinLaneCountDist)
        self._egoRoadTypes = ProtoListWrapper(container=[int(v) for v in proto.egoRoadTypes], attr_name='egoRoadTypes', list_owner=proto)
        self._ego_parking_space_decoration_params = get_wrapper(proto_type=proto.ego_parking_space_decoration_params.__class__)(proto=proto.ego_parking_space_decoration_params)
        self._junction_generator = get_wrapper(proto_type=proto.junction_generator.__class__)(proto=proto.junction_generator)
        self._kitti_generator = get_wrapper(proto_type=proto.kitti_generator.__class__)(proto=proto.kitti_generator)
        self._laneStartOffset = get_wrapper(proto_type=proto.laneStartOffset.__class__)(proto=proto.laneStartOffset)
        self._lightFlashingPeriod = get_wrapper(proto_type=proto.lightFlashingPeriod.__class__)(proto=proto.lightFlashingPeriod)
        self._lightIlluminatedPercentage = get_wrapper(proto_type=proto.lightIlluminatedPercentage.__class__)(proto=proto.lightIlluminatedPercentage)
        self._markerDataMap = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.markerDataMap.items()}, attr_name='markerDataMap', dict_owner=proto)
        self._object_decoration_params = get_wrapper(proto_type=proto.object_decoration_params.__class__)(proto=proto.object_decoration_params)
        self._parkingTypeDistribution = get_wrapper(proto_type=proto.parkingTypeDistribution.__class__)(proto=proto.parkingTypeDistribution)
        self._parking_space_data = get_wrapper(proto_type=proto.parking_space_data.__class__)(proto=proto.parking_space_data)
        self._pedestrianColorOverrideRGB = ProtoListWrapper(container=[float(v) for v in proto.pedestrianColorOverrideRGB], attr_name='pedestrianColorOverrideRGB', list_owner=proto)
        self._position_generator = get_wrapper(proto_type=proto.position_generator.__class__)(proto=proto.position_generator)
        self._random_generator = get_wrapper(proto_type=proto.random_generator.__class__)(proto=proto.random_generator)
        self._rollingStop = get_wrapper(proto_type=proto.rollingStop.__class__)(proto=proto.rollingStop)
        self._signDensity = get_wrapper(proto_type=proto.signDensity.__class__)(proto=proto.signDensity)
        self._spawnTrailerProbabilities = ProtoDictWrapper(container={k: float(v) for (k, v) in proto.spawnTrailerProbabilities.items()}, attr_name='spawnTrailerProbabilities', dict_owner=proto)
        self._startSeparationTime = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.startSeparationTime.items()}, attr_name='startSeparationTime', dict_owner=proto)
        self._stopLineOffset = get_wrapper(proto_type=proto.stopLineOffset.__class__)(proto=proto.stopLineOffset)
        self._targetSeparationTime = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.targetSeparationTime.items()}, attr_name='targetSeparationTime', dict_owner=proto)
        self._turnTypeDistribution = get_wrapper(proto_type=proto.turnTypeDistribution.__class__)(proto=proto.turnTypeDistribution)
        self._vehicleDistribution = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicleDistribution.items()}, attr_name='vehicleDistribution', dict_owner=proto)
        self._vehicleRoadTypes = ProtoListWrapper(container=[int(v) for v in proto.vehicleRoadTypes], attr_name='vehicleRoadTypes', list_owner=proto)
        self._voi_generator = get_wrapper(proto_type=proto.voi_generator.__class__)(proto=proto.voi_generator)
        if agentStateProbabilities is not None:
            self.agentStateProbabilities = agentStateProbabilities
        if aggression is not None:
            self.aggression = aggression
        if aggressionSpread is not None:
            self.aggressionSpread = aggressionSpread
        if alignEgoPedestrianToLane is not None:
            self.alignEgoPedestrianToLane = alignEgoPedestrianToLane
        if animalSpeciesAllowed is not None:
            self.animalSpeciesAllowed = animalSpeciesAllowed
        if applyProceedOutOfTurnProbabilityToEgo is not None:
            self.applyProceedOutOfTurnProbabilityToEgo = applyProceedOutOfTurnProbabilityToEgo
        if applyRollingStopToEgo is not None:
            self.applyRollingStopToEgo = applyRollingStopToEgo
        if applyStopLineOffsetToEgo is not None:
            self.applyStopLineOffsetToEgo = applyStopLineOffsetToEgo
        if bicyclesOnlyInBikeLanes is not None:
            self.bicyclesOnlyInBikeLanes = bicyclesOnlyInBikeLanes
        if crosswalkSignDensity is not None:
            self.crosswalkSignDensity = crosswalkSignDensity
        if disableAccessories is not None:
            self.disableAccessories = disableAccessories
        if disableOccupants is not None:
            self.disableOccupants = disableOccupants
        if egoForceMinLengthBehind is not None:
            self.egoForceMinLengthBehind = egoForceMinLengthBehind
        if egoIgnoreObstacleTypes is not None:
            self.egoIgnoreObstacleTypes = egoIgnoreObstacleTypes
        if egoLaneChangeChance is not None:
            self.egoLaneChangeChance = egoLaneChangeChance
        if egoLaneChangeChanceSpread is not None:
            self.egoLaneChangeChanceSpread = egoLaneChangeChanceSpread
        if egoLaneChangeCooldown is not None:
            self.egoLaneChangeCooldown = egoLaneChangeCooldown
        if egoLaneChangeCooldownSpread is not None:
            self.egoLaneChangeCooldownSpread = egoLaneChangeCooldownSpread
        if egoMinDistToEdge is not None:
            self.egoMinDistToEdge = egoMinDistToEdge
        if egoMinDistToEdgeSpread is not None:
            self.egoMinDistToEdgeSpread = egoMinDistToEdgeSpread
        if egoMinLaneCountDist is not None:
            self.egoMinLaneCountDist = egoMinLaneCountDist
        if egoMinPathLength is not None:
            self.egoMinPathLength = egoMinPathLength
        if egoMinPathLengthSpread is not None:
            self.egoMinPathLengthSpread = egoMinPathLengthSpread
        if egoPedestrianExclusionRadius is not None:
            self.egoPedestrianExclusionRadius = egoPedestrianExclusionRadius
        if egoPedestrianExclusionRadiusSpread is not None:
            self.egoPedestrianExclusionRadiusSpread = egoPedestrianExclusionRadiusSpread
        if egoPedestrians is not None:
            self.egoPedestrians = egoPedestrians
        if egoRoadTypes is not None:
            self.egoRoadTypes = egoRoadTypes
        if egoVehicleModel is not None:
            self.egoVehicleModel = egoVehicleModel
        if ego_parking_space_decoration_params is not None:
            self.ego_parking_space_decoration_params = ego_parking_space_decoration_params
        if emergencyLightsOnProbability is not None:
            self.emergencyLightsOnProbability = emergencyLightsOnProbability
        if emergencyLightsOnProbabilitySpread is not None:
            self.emergencyLightsOnProbabilitySpread = emergencyLightsOnProbabilitySpread
        if enableCrosswalkPlacement is not None:
            self.enableCrosswalkPlacement = enableCrosswalkPlacement
        if enableDrivewayPlacement is not None:
            self.enableDrivewayPlacement = enableDrivewayPlacement
        if enableDynamicLaneSelection is not None:
            self.enableDynamicLaneSelection = enableDynamicLaneSelection
        if enableJunctionPlacement is not None:
            self.enableJunctionPlacement = enableJunctionPlacement
        if instanceParallelParkingMarkers is not None:
            self.instanceParallelParkingMarkers = instanceParallelParkingMarkers
        if instanceParallelParkingSpaces is not None:
            self.instanceParallelParkingSpaces = instanceParallelParkingSpaces
        if junction_generator is not None:
            self.junction_generator = junction_generator
        if kitti_generator is not None:
            self.kitti_generator = kitti_generator
        if laneChangeChance is not None:
            self.laneChangeChance = laneChangeChance
        if laneChangeChanceSpread is not None:
            self.laneChangeChanceSpread = laneChangeChanceSpread
        if laneChangeCooldown is not None:
            self.laneChangeCooldown = laneChangeCooldown
        if laneChangeCooldownSpread is not None:
            self.laneChangeCooldownSpread = laneChangeCooldownSpread
        if laneDriftAmp is not None:
            self.laneDriftAmp = laneDriftAmp
        if laneDriftAmpSpread is not None:
            self.laneDriftAmpSpread = laneDriftAmpSpread
        if laneDriftScale is not None:
            self.laneDriftScale = laneDriftScale
        if laneDriftScaleSpread is not None:
            self.laneDriftScaleSpread = laneDriftScaleSpread
        if laneOffset is not None:
            self.laneOffset = laneOffset
        if laneOffsetSpread is not None:
            self.laneOffsetSpread = laneOffsetSpread
        if laneStartOffset is not None:
            self.laneStartOffset = laneStartOffset
        if largeVehicleTurnRadiusMultiple is not None:
            self.largeVehicleTurnRadiusMultiple = largeVehicleTurnRadiusMultiple
        if lightFlashingPeriod is not None:
            self.lightFlashingPeriod = lightFlashingPeriod
        if lightIlluminatedPercentage is not None:
            self.lightIlluminatedPercentage = lightIlluminatedPercentage
        if markerDataMap is not None:
            self.markerDataMap = markerDataMap
        if minNumberOfAnimals is not None:
            self.minNumberOfAnimals = minNumberOfAnimals
        if minNumberOfPedestrians is not None:
            self.minNumberOfPedestrians = minNumberOfPedestrians
        if numberOfAnimals is not None:
            self.numberOfAnimals = numberOfAnimals
        if numberOfPedestrians is not None:
            self.numberOfPedestrians = numberOfPedestrians
        if object_decoration_params is not None:
            self.object_decoration_params = object_decoration_params
        if object_decoration_radius is not None:
            self.object_decoration_radius = object_decoration_radius
        if parkedVehicleSpawnProbability is not None:
            self.parkedVehicleSpawnProbability = parkedVehicleSpawnProbability
        if parkedVehicleSpawnProbabilitySpread is not None:
            self.parkedVehicleSpawnProbabilitySpread = parkedVehicleSpawnProbabilitySpread
        if parkedVehicleSpawnRadius is not None:
            self.parkedVehicleSpawnRadius = parkedVehicleSpawnRadius
        if parkingTypeDistribution is not None:
            self.parkingTypeDistribution = parkingTypeDistribution
        if parking_space_data is not None:
            self.parking_space_data = parking_space_data
        if pedestrianColorOverrideChance is not None:
            self.pedestrianColorOverrideChance = pedestrianColorOverrideChance
        if pedestrianColorOverrideChanceSpread is not None:
            self.pedestrianColorOverrideChanceSpread = pedestrianColorOverrideChanceSpread
        if pedestrianColorOverrideRGB is not None:
            self.pedestrianColorOverrideRGB = pedestrianColorOverrideRGB
        if pedestrianIdleProbability is not None:
            self.pedestrianIdleProbability = pedestrianIdleProbability
        if pedestrianIdleProbabilitySpread is not None:
            self.pedestrianIdleProbabilitySpread = pedestrianIdleProbabilitySpread
        if pedestrianJaywalkAngle is not None:
            self.pedestrianJaywalkAngle = pedestrianJaywalkAngle
        if pedestrianJaywalkLookAhead is not None:
            self.pedestrianJaywalkLookAhead = pedestrianJaywalkLookAhead
        if pedestrianJaywalkRadius is not None:
            self.pedestrianJaywalkRadius = pedestrianJaywalkRadius
        if pedestrianSpawnMinEdgeDistance is not None:
            self.pedestrianSpawnMinEdgeDistance = pedestrianSpawnMinEdgeDistance
        if pedestrianSpawnRadius is not None:
            self.pedestrianSpawnRadius = pedestrianSpawnRadius
        if pedestrianSpawnTightness is not None:
            self.pedestrianSpawnTightness = pedestrianSpawnTightness
        if pedestrianVelocity is not None:
            self.pedestrianVelocity = pedestrianVelocity
        if pedestrianVelocitySpread is not None:
            self.pedestrianVelocitySpread = pedestrianVelocitySpread
        if pedestriansDynamicPathing is not None:
            self.pedestriansDynamicPathing = pedestriansDynamicPathing
        if pedestriansSpawnInParkingLot is not None:
            self.pedestriansSpawnInParkingLot = pedestriansSpawnInParkingLot
        if position_generator is not None:
            self.position_generator = position_generator
        if proceedOutOfTurnProbability is not None:
            self.proceedOutOfTurnProbability = proceedOutOfTurnProbability
        if random_generator is not None:
            self.random_generator = random_generator
        if randomizeVehicleParts is not None:
            self.randomizeVehicleParts = randomizeVehicleParts
        if region is not None:
            self.region = region
        if restrictLargeVehicleLaneCurvature is not None:
            self.restrictLargeVehicleLaneCurvature = restrictLargeVehicleLaneCurvature
        if rollingStop is not None:
            self.rollingStop = rollingStop
        if searchRadius is not None:
            self.searchRadius = searchRadius
        if signDensity is not None:
            self.signDensity = signDensity
        if spawnPedestriansOnRoad is not None:
            self.spawnPedestriansOnRoad = spawnPedestriansOnRoad
        if spawnTrailerOnEgoProbability is not None:
            self.spawnTrailerOnEgoProbability = spawnTrailerOnEgoProbability
        if spawnTrailerProbabilities is not None:
            self.spawnTrailerProbabilities = spawnTrailerProbabilities
        if startSeparation is not None:
            self.startSeparation = startSeparation
        if startSeparationSpread is not None:
            self.startSeparationSpread = startSeparationSpread
        if startSeparationTime is not None:
            self.startSeparationTime = startSeparationTime
        if startVelocity is not None:
            self.startVelocity = startVelocity
        if startVelocitySpread is not None:
            self.startVelocitySpread = startVelocitySpread
        if stopLineOffset is not None:
            self.stopLineOffset = stopLineOffset
        if targetSeparation is not None:
            self.targetSeparation = targetSeparation
        if targetSeparationSpread is not None:
            self.targetSeparationSpread = targetSeparationSpread
        if targetSeparationTime is not None:
            self.targetSeparationTime = targetSeparationTime
        if targetVelocity is not None:
            self.targetVelocity = targetVelocity
        if targetVelocitySpread is not None:
            self.targetVelocitySpread = targetVelocitySpread
        if turnTypeDistribution is not None:
            self.turnTypeDistribution = turnTypeDistribution
        if useStaticTrailers is not None:
            self.useStaticTrailers = useStaticTrailers
        if vehicleDensityModifier is not None:
            self.vehicleDensityModifier = vehicleDensityModifier
        if vehicleDistribution is not None:
            self.vehicleDistribution = vehicleDistribution
        if vehicleRoadTypes is not None:
            self.vehicleRoadTypes = vehicleRoadTypes
        if voi_generator is not None:
            self.voi_generator = voi_generator

    @property
    def agentStateProbabilities(self) -> List[AgentStateProbabilityConfig]:
        return self._agentStateProbabilities

    @agentStateProbabilities.setter
    def agentStateProbabilities(self, value: List[AgentStateProbabilityConfig]):
        self._agentStateProbabilities.clear()
        for v in value:
            self._agentStateProbabilities.append(v)

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
    def alignEgoPedestrianToLane(self) -> bool:
        return self.proto.alignEgoPedestrianToLane

    @alignEgoPedestrianToLane.setter
    def alignEgoPedestrianToLane(self, value: bool):
        self.proto.alignEgoPedestrianToLane = value

    @property
    def animalSpeciesAllowed(self) -> str:
        return self.proto.animalSpeciesAllowed

    @animalSpeciesAllowed.setter
    def animalSpeciesAllowed(self, value: str):
        self.proto.animalSpeciesAllowed = value

    @property
    def applyProceedOutOfTurnProbabilityToEgo(self) -> bool:
        return self.proto.applyProceedOutOfTurnProbabilityToEgo

    @applyProceedOutOfTurnProbabilityToEgo.setter
    def applyProceedOutOfTurnProbabilityToEgo(self, value: bool):
        self.proto.applyProceedOutOfTurnProbabilityToEgo = value

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
    def bicyclesOnlyInBikeLanes(self) -> bool:
        return self.proto.bicyclesOnlyInBikeLanes

    @bicyclesOnlyInBikeLanes.setter
    def bicyclesOnlyInBikeLanes(self, value: bool):
        self.proto.bicyclesOnlyInBikeLanes = value

    @property
    def crosswalkSignDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._crosswalkSignDensity

    @crosswalkSignDensity.setter
    def crosswalkSignDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._crosswalkSignDensity.proto.CopyFrom(value.proto)

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
    def egoForceMinLengthBehind(self) -> bool:
        return self.proto.egoForceMinLengthBehind

    @egoForceMinLengthBehind.setter
    def egoForceMinLengthBehind(self, value: bool):
        self.proto.egoForceMinLengthBehind = value

    @property
    def egoIgnoreObstacleTypes(self) -> List[str]:
        return self._egoIgnoreObstacleTypes

    @egoIgnoreObstacleTypes.setter
    def egoIgnoreObstacleTypes(self, value: List[str]):
        self._egoIgnoreObstacleTypes.clear()
        for v in value:
            self._egoIgnoreObstacleTypes.append(v)

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
    def egoMinLaneCountDist(self) -> _pd_unified_generator_pb2.CenterSpreadConfigInt:
        return self._egoMinLaneCountDist

    @egoMinLaneCountDist.setter
    def egoMinLaneCountDist(self, value: _pd_unified_generator_pb2.CenterSpreadConfigInt):
        self._egoMinLaneCountDist.proto.CopyFrom(value.proto)

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
    def egoPedestrians(self) -> bool:
        return self.proto.egoPedestrians

    @egoPedestrians.setter
    def egoPedestrians(self, value: bool):
        self.proto.egoPedestrians = value

    @property
    def egoRoadTypes(self) -> int:
        return self._egoRoadTypes

    @egoRoadTypes.setter
    def egoRoadTypes(self, value: int):
        self._egoRoadTypes.clear()
        for v in value:
            self._egoRoadTypes.append(v)

    @property
    def egoVehicleModel(self) -> str:
        return self.proto.egoVehicleModel

    @egoVehicleModel.setter
    def egoVehicleModel(self, value: str):
        self.proto.egoVehicleModel = value

    @property
    def ego_parking_space_decoration_params(self) -> _pd_unified_generator_pb2.ObjectDecorationParams:
        return self._ego_parking_space_decoration_params

    @ego_parking_space_decoration_params.setter
    def ego_parking_space_decoration_params(self, value: _pd_unified_generator_pb2.ObjectDecorationParams):
        self._ego_parking_space_decoration_params.proto.CopyFrom(value.proto)

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
    def enableCrosswalkPlacement(self) -> bool:
        return self.proto.enableCrosswalkPlacement

    @enableCrosswalkPlacement.setter
    def enableCrosswalkPlacement(self, value: bool):
        self.proto.enableCrosswalkPlacement = value

    @property
    def enableDrivewayPlacement(self) -> bool:
        return self.proto.enableDrivewayPlacement

    @enableDrivewayPlacement.setter
    def enableDrivewayPlacement(self, value: bool):
        self.proto.enableDrivewayPlacement = value

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
    def instanceParallelParkingMarkers(self) -> bool:
        return self.proto.instanceParallelParkingMarkers

    @instanceParallelParkingMarkers.setter
    def instanceParallelParkingMarkers(self, value: bool):
        self.proto.instanceParallelParkingMarkers = value

    @property
    def instanceParallelParkingSpaces(self) -> bool:
        return self.proto.instanceParallelParkingSpaces

    @instanceParallelParkingSpaces.setter
    def instanceParallelParkingSpaces(self, value: bool):
        self.proto.instanceParallelParkingSpaces = value

    @property
    def junction_generator(self) -> JunctionScenarioGenerator:
        return self._junction_generator

    @junction_generator.setter
    def junction_generator(self, value: JunctionScenarioGenerator):
        self._junction_generator.proto.CopyFrom(value.proto)

    @property
    def kitti_generator(self) -> KittiScenarioGenerator:
        return self._kitti_generator

    @kitti_generator.setter
    def kitti_generator(self, value: KittiScenarioGenerator):
        self._kitti_generator.proto.CopyFrom(value.proto)

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
    def laneStartOffset(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._laneStartOffset

    @laneStartOffset.setter
    def laneStartOffset(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._laneStartOffset.proto.CopyFrom(value.proto)

    @property
    def largeVehicleTurnRadiusMultiple(self) -> float:
        return self.proto.largeVehicleTurnRadiusMultiple

    @largeVehicleTurnRadiusMultiple.setter
    def largeVehicleTurnRadiusMultiple(self, value: float):
        self.proto.largeVehicleTurnRadiusMultiple = value

    @property
    def lightFlashingPeriod(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._lightFlashingPeriod

    @lightFlashingPeriod.setter
    def lightFlashingPeriod(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._lightFlashingPeriod.proto.CopyFrom(value.proto)

    @property
    def lightIlluminatedPercentage(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._lightIlluminatedPercentage

    @lightIlluminatedPercentage.setter
    def lightIlluminatedPercentage(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._lightIlluminatedPercentage.proto.CopyFrom(value.proto)

    @property
    def markerDataMap(self) -> Dict[str, _pd_unified_generator_pb2.RoadMarkingData]:
        return self._markerDataMap

    @markerDataMap.setter
    def markerDataMap(self, value: Dict[str, _pd_unified_generator_pb2.RoadMarkingData]):
        self._markerDataMap.clear()
        self._markerDataMap.update(value)

    @property
    def minNumberOfAnimals(self) -> int:
        return self.proto.minNumberOfAnimals

    @minNumberOfAnimals.setter
    def minNumberOfAnimals(self, value: int):
        self.proto.minNumberOfAnimals = value

    @property
    def minNumberOfPedestrians(self) -> int:
        return self.proto.minNumberOfPedestrians

    @minNumberOfPedestrians.setter
    def minNumberOfPedestrians(self, value: int):
        self.proto.minNumberOfPedestrians = value

    @property
    def numberOfAnimals(self) -> int:
        return self.proto.numberOfAnimals

    @numberOfAnimals.setter
    def numberOfAnimals(self, value: int):
        self.proto.numberOfAnimals = value

    @property
    def numberOfPedestrians(self) -> int:
        return self.proto.numberOfPedestrians

    @numberOfPedestrians.setter
    def numberOfPedestrians(self, value: int):
        self.proto.numberOfPedestrians = value

    @property
    def object_decoration_params(self) -> _pd_unified_generator_pb2.ObjectDecorationParams:
        return self._object_decoration_params

    @object_decoration_params.setter
    def object_decoration_params(self, value: _pd_unified_generator_pb2.ObjectDecorationParams):
        self._object_decoration_params.proto.CopyFrom(value.proto)

    @property
    def object_decoration_radius(self) -> float:
        return self.proto.object_decoration_radius

    @object_decoration_radius.setter
    def object_decoration_radius(self, value: float):
        self.proto.object_decoration_radius = value

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
    def parkingTypeDistribution(self) -> _pd_unified_generator_pb2.ParkingTypeDistribution:
        return self._parkingTypeDistribution

    @parkingTypeDistribution.setter
    def parkingTypeDistribution(self, value: _pd_unified_generator_pb2.ParkingTypeDistribution):
        self._parkingTypeDistribution.proto.CopyFrom(value.proto)

    @property
    def parking_space_data(self) -> _pd_unified_generator_pb2.ParkingSpaceData:
        return self._parking_space_data

    @parking_space_data.setter
    def parking_space_data(self, value: _pd_unified_generator_pb2.ParkingSpaceData):
        self._parking_space_data.proto.CopyFrom(value.proto)

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
    def pedestrianIdleProbability(self) -> float:
        return self.proto.pedestrianIdleProbability

    @pedestrianIdleProbability.setter
    def pedestrianIdleProbability(self, value: float):
        self.proto.pedestrianIdleProbability = value

    @property
    def pedestrianIdleProbabilitySpread(self) -> float:
        return self.proto.pedestrianIdleProbabilitySpread

    @pedestrianIdleProbabilitySpread.setter
    def pedestrianIdleProbabilitySpread(self, value: float):
        self.proto.pedestrianIdleProbabilitySpread = value

    @property
    def pedestrianJaywalkAngle(self) -> float:
        return self.proto.pedestrianJaywalkAngle

    @pedestrianJaywalkAngle.setter
    def pedestrianJaywalkAngle(self, value: float):
        self.proto.pedestrianJaywalkAngle = value

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
    def pedestrianSpawnMinEdgeDistance(self) -> float:
        return self.proto.pedestrianSpawnMinEdgeDistance

    @pedestrianSpawnMinEdgeDistance.setter
    def pedestrianSpawnMinEdgeDistance(self, value: float):
        self.proto.pedestrianSpawnMinEdgeDistance = value

    @property
    def pedestrianSpawnRadius(self) -> float:
        return self.proto.pedestrianSpawnRadius

    @pedestrianSpawnRadius.setter
    def pedestrianSpawnRadius(self, value: float):
        self.proto.pedestrianSpawnRadius = value

    @property
    def pedestrianSpawnTightness(self) -> float:
        return self.proto.pedestrianSpawnTightness

    @pedestrianSpawnTightness.setter
    def pedestrianSpawnTightness(self, value: float):
        self.proto.pedestrianSpawnTightness = value

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
    def pedestriansDynamicPathing(self) -> bool:
        return self.proto.pedestriansDynamicPathing

    @pedestriansDynamicPathing.setter
    def pedestriansDynamicPathing(self, value: bool):
        self.proto.pedestriansDynamicPathing = value

    @property
    def pedestriansSpawnInParkingLot(self) -> bool:
        return self.proto.pedestriansSpawnInParkingLot

    @pedestriansSpawnInParkingLot.setter
    def pedestriansSpawnInParkingLot(self, value: bool):
        self.proto.pedestriansSpawnInParkingLot = value

    @property
    def position_generator(self) -> PositionGenerator:
        return self._position_generator

    @position_generator.setter
    def position_generator(self, value: PositionGenerator):
        self._position_generator.proto.CopyFrom(value.proto)

    @property
    def proceedOutOfTurnProbability(self) -> float:
        return self.proto.proceedOutOfTurnProbability

    @proceedOutOfTurnProbability.setter
    def proceedOutOfTurnProbability(self, value: float):
        self.proto.proceedOutOfTurnProbability = value

    @property
    def random_generator(self) -> RandomScenarioGenerator:
        return self._random_generator

    @random_generator.setter
    def random_generator(self, value: RandomScenarioGenerator):
        self._random_generator.proto.CopyFrom(value.proto)

    @property
    def randomizeVehicleParts(self) -> bool:
        return self.proto.randomizeVehicleParts

    @randomizeVehicleParts.setter
    def randomizeVehicleParts(self, value: bool):
        self.proto.randomizeVehicleParts = value

    @property
    def region(self) -> str:
        return self.proto.region

    @region.setter
    def region(self, value: str):
        self.proto.region = value

    @property
    def restrictLargeVehicleLaneCurvature(self) -> bool:
        return self.proto.restrictLargeVehicleLaneCurvature

    @restrictLargeVehicleLaneCurvature.setter
    def restrictLargeVehicleLaneCurvature(self, value: bool):
        self.proto.restrictLargeVehicleLaneCurvature = value

    @property
    def rollingStop(self) -> _pd_unified_generator_pb2.CenterSpreadProbabilityConfig:
        return self._rollingStop

    @rollingStop.setter
    def rollingStop(self, value: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig):
        self._rollingStop.proto.CopyFrom(value.proto)

    @property
    def searchRadius(self) -> float:
        return self.proto.searchRadius

    @searchRadius.setter
    def searchRadius(self, value: float):
        self.proto.searchRadius = value

    @property
    def signDensity(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._signDensity

    @signDensity.setter
    def signDensity(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._signDensity.proto.CopyFrom(value.proto)

    @property
    def spawnPedestriansOnRoad(self) -> bool:
        return self.proto.spawnPedestriansOnRoad

    @spawnPedestriansOnRoad.setter
    def spawnPedestriansOnRoad(self, value: bool):
        self.proto.spawnPedestriansOnRoad = value

    @property
    def spawnTrailerOnEgoProbability(self) -> float:
        return self.proto.spawnTrailerOnEgoProbability

    @spawnTrailerOnEgoProbability.setter
    def spawnTrailerOnEgoProbability(self, value: float):
        self.proto.spawnTrailerOnEgoProbability = value

    @property
    def spawnTrailerProbabilities(self) -> Dict[str, float]:
        return self._spawnTrailerProbabilities

    @spawnTrailerProbabilities.setter
    def spawnTrailerProbabilities(self, value: Dict[str, float]):
        self._spawnTrailerProbabilities.clear()
        self._spawnTrailerProbabilities.update(value)

    @property
    def startSeparation(self) -> float:
        return self.proto.startSeparation

    @startSeparation.setter
    def startSeparation(self, value: float):
        self.proto.startSeparation = value

    @property
    def startSeparationSpread(self) -> float:
        return self.proto.startSeparationSpread

    @startSeparationSpread.setter
    def startSeparationSpread(self, value: float):
        self.proto.startSeparationSpread = value

    @property
    def startSeparationTime(self) -> Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]:
        return self._startSeparationTime

    @startSeparationTime.setter
    def startSeparationTime(self, value: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]):
        self._startSeparationTime.clear()
        self._startSeparationTime.update(value)

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
    def stopLineOffset(self) -> _pd_unified_generator_pb2.CenterSpreadProbabilityConfig:
        return self._stopLineOffset

    @stopLineOffset.setter
    def stopLineOffset(self, value: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig):
        self._stopLineOffset.proto.CopyFrom(value.proto)

    @property
    def targetSeparation(self) -> float:
        return self.proto.targetSeparation

    @targetSeparation.setter
    def targetSeparation(self, value: float):
        self.proto.targetSeparation = value

    @property
    def targetSeparationSpread(self) -> float:
        return self.proto.targetSeparationSpread

    @targetSeparationSpread.setter
    def targetSeparationSpread(self, value: float):
        self.proto.targetSeparationSpread = value

    @property
    def targetSeparationTime(self) -> Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]:
        return self._targetSeparationTime

    @targetSeparationTime.setter
    def targetSeparationTime(self, value: Dict[str, _pd_unified_generator_pb2.CenterSpreadConfig]):
        self._targetSeparationTime.clear()
        self._targetSeparationTime.update(value)

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
    def turnTypeDistribution(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._turnTypeDistribution

    @turnTypeDistribution.setter
    def turnTypeDistribution(self, value: _pd_distributions_pb2.EnumDistribution):
        self._turnTypeDistribution.proto.CopyFrom(value.proto)

    @property
    def useStaticTrailers(self) -> bool:
        return self.proto.useStaticTrailers

    @useStaticTrailers.setter
    def useStaticTrailers(self, value: bool):
        self.proto.useStaticTrailers = value

    @property
    def vehicleDensityModifier(self) -> float:
        return self.proto.vehicleDensityModifier

    @vehicleDensityModifier.setter
    def vehicleDensityModifier(self, value: float):
        self.proto.vehicleDensityModifier = value

    @property
    def vehicleDistribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicleDistribution

    @vehicleDistribution.setter
    def vehicleDistribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicleDistribution.clear()
        self._vehicleDistribution.update(value)

    @property
    def vehicleRoadTypes(self) -> int:
        return self._vehicleRoadTypes

    @vehicleRoadTypes.setter
    def vehicleRoadTypes(self, value: int):
        self._vehicleRoadTypes.clear()
        for v in value:
            self._vehicleRoadTypes.append(v)

    @property
    def voi_generator(self) -> VehicleOfInterestGenerator:
        return self._voi_generator

    @voi_generator.setter
    def voi_generator(self, value: VehicleOfInterestGenerator):
        self._voi_generator.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_spawn_pb2.StaticCamScenarioGeneratorInfo)
class StaticCamScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.StaticCamScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.StaticCamScenarioGeneratorInfo]=None, distance_from_junction: Optional[float]=None, distance_from_junction_spread: Optional[float]=None, elevation: Optional[float]=None, elevation_spread: Optional[float]=None):
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

@register_wrapper(proto_type=pd_spawn_pb2.VehicleOfInterestGenerator)
class VehicleOfInterestGenerator(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.VehicleOfInterestGenerator

    def __init__(self, *, proto: Optional[pd_spawn_pb2.VehicleOfInterestGenerator]=None, include_opposite_lanes: Optional[bool]=None, max_distance_back: Optional[float]=None, max_distance_front: Optional[float]=None, max_number_of_vehicles: Optional[int]=None, min_number_of_vehicles: Optional[int]=None, vehicle_list: Optional[List[str]]=None):
        if proto is None:
            proto = pd_spawn_pb2.VehicleOfInterestGenerator()
        self.proto = proto
        self._vehicle_list = ProtoListWrapper(container=[str(v) for v in proto.vehicle_list], attr_name='vehicle_list', list_owner=proto)
        if include_opposite_lanes is not None:
            self.include_opposite_lanes = include_opposite_lanes
        if max_distance_back is not None:
            self.max_distance_back = max_distance_back
        if max_distance_front is not None:
            self.max_distance_front = max_distance_front
        if max_number_of_vehicles is not None:
            self.max_number_of_vehicles = max_number_of_vehicles
        if min_number_of_vehicles is not None:
            self.min_number_of_vehicles = min_number_of_vehicles
        if vehicle_list is not None:
            self.vehicle_list = vehicle_list

    @property
    def include_opposite_lanes(self) -> bool:
        return self.proto.include_opposite_lanes

    @include_opposite_lanes.setter
    def include_opposite_lanes(self, value: bool):
        self.proto.include_opposite_lanes = value

    @property
    def max_distance_back(self) -> float:
        return self.proto.max_distance_back

    @max_distance_back.setter
    def max_distance_back(self, value: float):
        self.proto.max_distance_back = value

    @property
    def max_distance_front(self) -> float:
        return self.proto.max_distance_front

    @max_distance_front.setter
    def max_distance_front(self, value: float):
        self.proto.max_distance_front = value

    @property
    def max_number_of_vehicles(self) -> int:
        return self.proto.max_number_of_vehicles

    @max_number_of_vehicles.setter
    def max_number_of_vehicles(self, value: int):
        self.proto.max_number_of_vehicles = value

    @property
    def min_number_of_vehicles(self) -> int:
        return self.proto.min_number_of_vehicles

    @min_number_of_vehicles.setter
    def min_number_of_vehicles(self, value: int):
        self.proto.min_number_of_vehicles = value

    @property
    def vehicle_list(self) -> List[str]:
        return self._vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, value: List[str]):
        self._vehicle_list.clear()
        for v in value:
            self._vehicle_list.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo)
class VehicleOfInterestScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo]=None, include_opposite_lanes: Optional[bool]=None, max_distance_back: Optional[float]=None, max_distance_front: Optional[float]=None, max_number_of_vehicles: Optional[int]=None, min_number_of_vehicles: Optional[int]=None, vehicle_list: Optional[List[str]]=None):
        if proto is None:
            proto = pd_spawn_pb2.VehicleOfInterestScenarioGeneratorInfo()
        self.proto = proto
        self._vehicle_list = ProtoListWrapper(container=[str(v) for v in proto.vehicle_list], attr_name='vehicle_list', list_owner=proto)
        if include_opposite_lanes is not None:
            self.include_opposite_lanes = include_opposite_lanes
        if max_distance_back is not None:
            self.max_distance_back = max_distance_back
        if max_distance_front is not None:
            self.max_distance_front = max_distance_front
        if max_number_of_vehicles is not None:
            self.max_number_of_vehicles = max_number_of_vehicles
        if min_number_of_vehicles is not None:
            self.min_number_of_vehicles = min_number_of_vehicles
        if vehicle_list is not None:
            self.vehicle_list = vehicle_list

    @property
    def include_opposite_lanes(self) -> bool:
        return self.proto.include_opposite_lanes

    @include_opposite_lanes.setter
    def include_opposite_lanes(self, value: bool):
        self.proto.include_opposite_lanes = value

    @property
    def max_distance_back(self) -> float:
        return self.proto.max_distance_back

    @max_distance_back.setter
    def max_distance_back(self, value: float):
        self.proto.max_distance_back = value

    @property
    def max_distance_front(self) -> float:
        return self.proto.max_distance_front

    @max_distance_front.setter
    def max_distance_front(self, value: float):
        self.proto.max_distance_front = value

    @property
    def max_number_of_vehicles(self) -> int:
        return self.proto.max_number_of_vehicles

    @max_number_of_vehicles.setter
    def max_number_of_vehicles(self, value: int):
        self.proto.max_number_of_vehicles = value

    @property
    def min_number_of_vehicles(self) -> int:
        return self.proto.min_number_of_vehicles

    @min_number_of_vehicles.setter
    def min_number_of_vehicles(self, value: int):
        self.proto.min_number_of_vehicles = value

    @property
    def vehicle_list(self) -> List[str]:
        return self._vehicle_list

    @vehicle_list.setter
    def vehicle_list(self, value: List[str]):
        self._vehicle_list.clear()
        for v in value:
            self._vehicle_list.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo)
class VehiclePositionScenarioGeneratorInfo(ProtoMessageClass):
    _proto_message = pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo

    def __init__(self, *, proto: Optional[pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo]=None, ego_behind_star: Optional[bool]=None, ego_in_star_adjacent_lane: Optional[bool]=None, emergency_vehicle_asset_tag: Optional[str]=None, emergency_vehicle_country_tag: Optional[str]=None, emergency_vehicle_distance_behind_star: Optional[float]=None, emergency_vehicle_spawn_behind_star_probability: Optional[_pd_unified_generator_pb2.CenterSpreadConfig]=None, face_same_direction: Optional[bool]=None, junction_ids: Optional[List[int]]=None, max_attempts_to_place_each_ped: Optional[int]=None, max_attempts_to_place_each_star: Optional[int]=None, max_emergency_vehicles_per_star: Optional[int]=None, max_lane_recursions_to_check_ego_adjacency: Optional[int]=None, max_peds_no_stars: Optional[int]=None, max_peds_per_star: Optional[int]=None, min_emergency_vehicles_per_star: Optional[int]=None, min_peds_no_stars: Optional[int]=None, min_peds_per_star: Optional[int]=None, num_stars_in_scene_max: Optional[int]=None, num_stars_in_scene_min: Optional[int]=None, ped_pose_distribution: Optional[_pd_distributions_pb2.CategoricalDistribution]=None, peds_around_star_vehicle: Optional[bool]=None, place_on_shoulder: Optional[bool]=None, radius_to_star_max: Optional[float]=None, radius_to_star_min: Optional[float]=None, reduce_spawn_to_zero_at_star_range: Optional[float]=None, scenario_fov_cull_limit: Optional[float]=None, scenario_los_cull: Optional[bool]=None, shoulder_peds_max_distance_from_ref: Optional[float]=None, star_on_same_road: Optional[bool]=None, star_vehicle_peds_max_distance: Optional[float]=None, star_vehicle_peds_max_distance_from_driveable_lane: Optional[float]=None, star_vehicle_peds_min_distance: Optional[float]=None, star_vehicle_peds_place_between_ego_and_star: Optional[bool]=None, star_vehicle_peds_social_distancing: Optional[float]=None, star_vehicles: Optional[List[str]]=None):
        if proto is None:
            proto = pd_spawn_pb2.VehiclePositionScenarioGeneratorInfo()
        self.proto = proto
        self._emergency_vehicle_spawn_behind_star_probability = get_wrapper(proto_type=proto.emergency_vehicle_spawn_behind_star_probability.__class__)(proto=proto.emergency_vehicle_spawn_behind_star_probability)
        self._junction_ids = ProtoListWrapper(container=[int(v) for v in proto.junction_ids], attr_name='junction_ids', list_owner=proto)
        self._ped_pose_distribution = get_wrapper(proto_type=proto.ped_pose_distribution.__class__)(proto=proto.ped_pose_distribution)
        self._star_vehicles = ProtoListWrapper(container=[str(v) for v in proto.star_vehicles], attr_name='star_vehicles', list_owner=proto)
        if ego_behind_star is not None:
            self.ego_behind_star = ego_behind_star
        if ego_in_star_adjacent_lane is not None:
            self.ego_in_star_adjacent_lane = ego_in_star_adjacent_lane
        if emergency_vehicle_asset_tag is not None:
            self.emergency_vehicle_asset_tag = emergency_vehicle_asset_tag
        if emergency_vehicle_country_tag is not None:
            self.emergency_vehicle_country_tag = emergency_vehicle_country_tag
        if emergency_vehicle_distance_behind_star is not None:
            self.emergency_vehicle_distance_behind_star = emergency_vehicle_distance_behind_star
        if emergency_vehicle_spawn_behind_star_probability is not None:
            self.emergency_vehicle_spawn_behind_star_probability = emergency_vehicle_spawn_behind_star_probability
        if face_same_direction is not None:
            self.face_same_direction = face_same_direction
        if junction_ids is not None:
            self.junction_ids = junction_ids
        if max_attempts_to_place_each_ped is not None:
            self.max_attempts_to_place_each_ped = max_attempts_to_place_each_ped
        if max_attempts_to_place_each_star is not None:
            self.max_attempts_to_place_each_star = max_attempts_to_place_each_star
        if max_emergency_vehicles_per_star is not None:
            self.max_emergency_vehicles_per_star = max_emergency_vehicles_per_star
        if max_lane_recursions_to_check_ego_adjacency is not None:
            self.max_lane_recursions_to_check_ego_adjacency = max_lane_recursions_to_check_ego_adjacency
        if max_peds_no_stars is not None:
            self.max_peds_no_stars = max_peds_no_stars
        if max_peds_per_star is not None:
            self.max_peds_per_star = max_peds_per_star
        if min_emergency_vehicles_per_star is not None:
            self.min_emergency_vehicles_per_star = min_emergency_vehicles_per_star
        if min_peds_no_stars is not None:
            self.min_peds_no_stars = min_peds_no_stars
        if min_peds_per_star is not None:
            self.min_peds_per_star = min_peds_per_star
        if num_stars_in_scene_max is not None:
            self.num_stars_in_scene_max = num_stars_in_scene_max
        if num_stars_in_scene_min is not None:
            self.num_stars_in_scene_min = num_stars_in_scene_min
        if ped_pose_distribution is not None:
            self.ped_pose_distribution = ped_pose_distribution
        if peds_around_star_vehicle is not None:
            self.peds_around_star_vehicle = peds_around_star_vehicle
        if place_on_shoulder is not None:
            self.place_on_shoulder = place_on_shoulder
        if radius_to_star_max is not None:
            self.radius_to_star_max = radius_to_star_max
        if radius_to_star_min is not None:
            self.radius_to_star_min = radius_to_star_min
        if reduce_spawn_to_zero_at_star_range is not None:
            self.reduce_spawn_to_zero_at_star_range = reduce_spawn_to_zero_at_star_range
        if scenario_fov_cull_limit is not None:
            self.scenario_fov_cull_limit = scenario_fov_cull_limit
        if scenario_los_cull is not None:
            self.scenario_los_cull = scenario_los_cull
        if shoulder_peds_max_distance_from_ref is not None:
            self.shoulder_peds_max_distance_from_ref = shoulder_peds_max_distance_from_ref
        if star_on_same_road is not None:
            self.star_on_same_road = star_on_same_road
        if star_vehicle_peds_max_distance is not None:
            self.star_vehicle_peds_max_distance = star_vehicle_peds_max_distance
        if star_vehicle_peds_max_distance_from_driveable_lane is not None:
            self.star_vehicle_peds_max_distance_from_driveable_lane = star_vehicle_peds_max_distance_from_driveable_lane
        if star_vehicle_peds_min_distance is not None:
            self.star_vehicle_peds_min_distance = star_vehicle_peds_min_distance
        if star_vehicle_peds_place_between_ego_and_star is not None:
            self.star_vehicle_peds_place_between_ego_and_star = star_vehicle_peds_place_between_ego_and_star
        if star_vehicle_peds_social_distancing is not None:
            self.star_vehicle_peds_social_distancing = star_vehicle_peds_social_distancing
        if star_vehicles is not None:
            self.star_vehicles = star_vehicles

    @property
    def ego_behind_star(self) -> bool:
        return self.proto.ego_behind_star

    @ego_behind_star.setter
    def ego_behind_star(self, value: bool):
        self.proto.ego_behind_star = value

    @property
    def ego_in_star_adjacent_lane(self) -> bool:
        return self.proto.ego_in_star_adjacent_lane

    @ego_in_star_adjacent_lane.setter
    def ego_in_star_adjacent_lane(self, value: bool):
        self.proto.ego_in_star_adjacent_lane = value

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

    @property
    def emergency_vehicle_distance_behind_star(self) -> float:
        return self.proto.emergency_vehicle_distance_behind_star

    @emergency_vehicle_distance_behind_star.setter
    def emergency_vehicle_distance_behind_star(self, value: float):
        self.proto.emergency_vehicle_distance_behind_star = value

    @property
    def emergency_vehicle_spawn_behind_star_probability(self) -> _pd_unified_generator_pb2.CenterSpreadConfig:
        return self._emergency_vehicle_spawn_behind_star_probability

    @emergency_vehicle_spawn_behind_star_probability.setter
    def emergency_vehicle_spawn_behind_star_probability(self, value: _pd_unified_generator_pb2.CenterSpreadConfig):
        self._emergency_vehicle_spawn_behind_star_probability.proto.CopyFrom(value.proto)

    @property
    def face_same_direction(self) -> bool:
        return self.proto.face_same_direction

    @face_same_direction.setter
    def face_same_direction(self, value: bool):
        self.proto.face_same_direction = value

    @property
    def junction_ids(self) -> List[int]:
        return self._junction_ids

    @junction_ids.setter
    def junction_ids(self, value: List[int]):
        self._junction_ids.clear()
        for v in value:
            self._junction_ids.append(v)

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
    def max_emergency_vehicles_per_star(self) -> int:
        return self.proto.max_emergency_vehicles_per_star

    @max_emergency_vehicles_per_star.setter
    def max_emergency_vehicles_per_star(self, value: int):
        self.proto.max_emergency_vehicles_per_star = value

    @property
    def max_lane_recursions_to_check_ego_adjacency(self) -> int:
        return self.proto.max_lane_recursions_to_check_ego_adjacency

    @max_lane_recursions_to_check_ego_adjacency.setter
    def max_lane_recursions_to_check_ego_adjacency(self, value: int):
        self.proto.max_lane_recursions_to_check_ego_adjacency = value

    @property
    def max_peds_no_stars(self) -> int:
        return self.proto.max_peds_no_stars

    @max_peds_no_stars.setter
    def max_peds_no_stars(self, value: int):
        self.proto.max_peds_no_stars = value

    @property
    def max_peds_per_star(self) -> int:
        return self.proto.max_peds_per_star

    @max_peds_per_star.setter
    def max_peds_per_star(self, value: int):
        self.proto.max_peds_per_star = value

    @property
    def min_emergency_vehicles_per_star(self) -> int:
        return self.proto.min_emergency_vehicles_per_star

    @min_emergency_vehicles_per_star.setter
    def min_emergency_vehicles_per_star(self, value: int):
        self.proto.min_emergency_vehicles_per_star = value

    @property
    def min_peds_no_stars(self) -> int:
        return self.proto.min_peds_no_stars

    @min_peds_no_stars.setter
    def min_peds_no_stars(self, value: int):
        self.proto.min_peds_no_stars = value

    @property
    def min_peds_per_star(self) -> int:
        return self.proto.min_peds_per_star

    @min_peds_per_star.setter
    def min_peds_per_star(self, value: int):
        self.proto.min_peds_per_star = value

    @property
    def num_stars_in_scene_max(self) -> int:
        return self.proto.num_stars_in_scene_max

    @num_stars_in_scene_max.setter
    def num_stars_in_scene_max(self, value: int):
        self.proto.num_stars_in_scene_max = value

    @property
    def num_stars_in_scene_min(self) -> int:
        return self.proto.num_stars_in_scene_min

    @num_stars_in_scene_min.setter
    def num_stars_in_scene_min(self, value: int):
        self.proto.num_stars_in_scene_min = value

    @property
    def ped_pose_distribution(self) -> _pd_distributions_pb2.CategoricalDistribution:
        return self._ped_pose_distribution

    @ped_pose_distribution.setter
    def ped_pose_distribution(self, value: _pd_distributions_pb2.CategoricalDistribution):
        self._ped_pose_distribution.proto.CopyFrom(value.proto)

    @property
    def peds_around_star_vehicle(self) -> bool:
        return self.proto.peds_around_star_vehicle

    @peds_around_star_vehicle.setter
    def peds_around_star_vehicle(self, value: bool):
        self.proto.peds_around_star_vehicle = value

    @property
    def place_on_shoulder(self) -> bool:
        return self.proto.place_on_shoulder

    @place_on_shoulder.setter
    def place_on_shoulder(self, value: bool):
        self.proto.place_on_shoulder = value

    @property
    def radius_to_star_max(self) -> float:
        return self.proto.radius_to_star_max

    @radius_to_star_max.setter
    def radius_to_star_max(self, value: float):
        self.proto.radius_to_star_max = value

    @property
    def radius_to_star_min(self) -> float:
        return self.proto.radius_to_star_min

    @radius_to_star_min.setter
    def radius_to_star_min(self, value: float):
        self.proto.radius_to_star_min = value

    @property
    def reduce_spawn_to_zero_at_star_range(self) -> float:
        return self.proto.reduce_spawn_to_zero_at_star_range

    @reduce_spawn_to_zero_at_star_range.setter
    def reduce_spawn_to_zero_at_star_range(self, value: float):
        self.proto.reduce_spawn_to_zero_at_star_range = value

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
    def shoulder_peds_max_distance_from_ref(self) -> float:
        return self.proto.shoulder_peds_max_distance_from_ref

    @shoulder_peds_max_distance_from_ref.setter
    def shoulder_peds_max_distance_from_ref(self, value: float):
        self.proto.shoulder_peds_max_distance_from_ref = value

    @property
    def star_on_same_road(self) -> bool:
        return self.proto.star_on_same_road

    @star_on_same_road.setter
    def star_on_same_road(self, value: bool):
        self.proto.star_on_same_road = value

    @property
    def star_vehicle_peds_max_distance(self) -> float:
        return self.proto.star_vehicle_peds_max_distance

    @star_vehicle_peds_max_distance.setter
    def star_vehicle_peds_max_distance(self, value: float):
        self.proto.star_vehicle_peds_max_distance = value

    @property
    def star_vehicle_peds_max_distance_from_driveable_lane(self) -> float:
        return self.proto.star_vehicle_peds_max_distance_from_driveable_lane

    @star_vehicle_peds_max_distance_from_driveable_lane.setter
    def star_vehicle_peds_max_distance_from_driveable_lane(self, value: float):
        self.proto.star_vehicle_peds_max_distance_from_driveable_lane = value

    @property
    def star_vehicle_peds_min_distance(self) -> float:
        return self.proto.star_vehicle_peds_min_distance

    @star_vehicle_peds_min_distance.setter
    def star_vehicle_peds_min_distance(self, value: float):
        self.proto.star_vehicle_peds_min_distance = value

    @property
    def star_vehicle_peds_place_between_ego_and_star(self) -> bool:
        return self.proto.star_vehicle_peds_place_between_ego_and_star

    @star_vehicle_peds_place_between_ego_and_star.setter
    def star_vehicle_peds_place_between_ego_and_star(self, value: bool):
        self.proto.star_vehicle_peds_place_between_ego_and_star = value

    @property
    def star_vehicle_peds_social_distancing(self) -> float:
        return self.proto.star_vehicle_peds_social_distancing

    @star_vehicle_peds_social_distancing.setter
    def star_vehicle_peds_social_distancing(self, value: float):
        self.proto.star_vehicle_peds_social_distancing = value

    @property
    def star_vehicles(self) -> List[str]:
        return self._star_vehicles

    @star_vehicles.setter
    def star_vehicles(self, value: List[str]):
        self._star_vehicles.clear()
        for v in value:
            self._star_vehicles.append(v)

@register_wrapper(proto_type=pd_spawn_pb2.VehicleType)
class VehicleType(ProtoEnumClass):
    _proto_message = pd_spawn_pb2.VehicleType
    BICYCLE: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.BICYCLE
    BUS: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.BUS
    CARAVAN: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.CARAVAN
    COMPACT: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.COMPACT
    FULLSIZE: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.FULLSIZE
    MIDSIZE: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.MIDSIZE
    MOTORCYCLE: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.MOTORCYCLE
    SUV: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.SUV
    TRAILER: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.TRAILER
    TRAIN: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.TRAIN
    TRUCK: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.TRUCK
    UNDEFINED: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.UNDEFINED
    VAN: pd_spawn_pb2.VehicleType = pd_spawn_pb2.VehicleType.VAN