import pd_distributions_pb2 as _pd_distributions_pb2
import pd_unified_generator_pb2 as _pd_unified_generator_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

BICYCLE: VehicleType
BUS: VehicleType
CARAVAN: VehicleType
COMPACT: VehicleType
DESCRIPTOR: _descriptor.FileDescriptor
FULLSIZE: VehicleType
MIDSIZE: VehicleType
MOTORCYCLE: VehicleType
SUV: VehicleType
TRAILER: VehicleType
TRAIN: VehicleType
TRUCK: VehicleType
UNDEFINED: VehicleType
VAN: VehicleType

class AgentStateProbabilityConfig(_message.Message):
    __slots__ = ["allowedAfter", "maxPerScene", "probability", "probabilitySpread", "stateName", "time", "timeSpread"]
    ALLOWEDAFTER_FIELD_NUMBER: ClassVar[int]
    MAXPERSCENE_FIELD_NUMBER: ClassVar[int]
    PROBABILITYSPREAD_FIELD_NUMBER: ClassVar[int]
    PROBABILITY_FIELD_NUMBER: ClassVar[int]
    STATENAME_FIELD_NUMBER: ClassVar[int]
    TIMESPREAD_FIELD_NUMBER: ClassVar[int]
    TIME_FIELD_NUMBER: ClassVar[int]
    allowedAfter: float
    maxPerScene: int
    probability: float
    probabilitySpread: float
    stateName: str
    time: float
    timeSpread: float
    def __init__(self, stateName: Optional[str] = ..., probability: Optional[float] = ..., probabilitySpread: Optional[float] = ..., time: Optional[float] = ..., timeSpread: Optional[float] = ..., maxPerScene: Optional[int] = ..., allowedAfter: Optional[float] = ...) -> None: ...

class AllVehicleTestScenarioGeneratorInfo(_message.Message):
    __slots__ = ["articulatedTrailerTest", "assetExcludeList", "assetIncludeList", "egoSpeed", "egoStart_t", "excludeMovingVehicles", "excludeStaticVehicles", "includeOnlyVehiclesInExclusionList", "leftOfEgo", "renderVehiclesBehindEgo", "rightOfEgo", "scenarioType", "startSeparationS", "testVehiclesSpeed", "vehicleExclusionList"]
    ARTICULATEDTRAILERTEST_FIELD_NUMBER: ClassVar[int]
    ASSETEXCLUDELIST_FIELD_NUMBER: ClassVar[int]
    ASSETINCLUDELIST_FIELD_NUMBER: ClassVar[int]
    EGOSPEED_FIELD_NUMBER: ClassVar[int]
    EGOSTART_T_FIELD_NUMBER: ClassVar[int]
    EXCLUDEMOVINGVEHICLES_FIELD_NUMBER: ClassVar[int]
    EXCLUDESTATICVEHICLES_FIELD_NUMBER: ClassVar[int]
    INCLUDEONLYVEHICLESINEXCLUSIONLIST_FIELD_NUMBER: ClassVar[int]
    LEFTOFEGO_FIELD_NUMBER: ClassVar[int]
    RENDERVEHICLESBEHINDEGO_FIELD_NUMBER: ClassVar[int]
    RIGHTOFEGO_FIELD_NUMBER: ClassVar[int]
    SCENARIOTYPE_FIELD_NUMBER: ClassVar[int]
    STARTSEPARATIONS_FIELD_NUMBER: ClassVar[int]
    TESTVEHICLESSPEED_FIELD_NUMBER: ClassVar[int]
    VEHICLEEXCLUSIONLIST_FIELD_NUMBER: ClassVar[int]
    articulatedTrailerTest: bool
    assetExcludeList: _containers.RepeatedScalarFieldContainer[str]
    assetIncludeList: _containers.RepeatedScalarFieldContainer[str]
    egoSpeed: float
    egoStart_t: float
    excludeMovingVehicles: bool
    excludeStaticVehicles: bool
    includeOnlyVehiclesInExclusionList: int
    leftOfEgo: bool
    renderVehiclesBehindEgo: bool
    rightOfEgo: bool
    scenarioType: int
    startSeparationS: float
    testVehiclesSpeed: float
    vehicleExclusionList: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, leftOfEgo: bool = ..., rightOfEgo: bool = ..., renderVehiclesBehindEgo: bool = ..., egoSpeed: Optional[float] = ..., egoStart_t: Optional[float] = ..., testVehiclesSpeed: Optional[float] = ..., startSeparationS: Optional[float] = ..., vehicleExclusionList: Optional[Iterable[str]] = ..., includeOnlyVehiclesInExclusionList: Optional[int] = ..., scenarioType: Optional[int] = ..., assetIncludeList: Optional[Iterable[str]] = ..., assetExcludeList: Optional[Iterable[str]] = ..., excludeStaticVehicles: bool = ..., excludeMovingVehicles: bool = ..., articulatedTrailerTest: bool = ...) -> None: ...

class CurveScenarioGeneratorInfo(_message.Message):
    __slots__ = ["maxCurvature", "maxLongitudinalOffset", "minCurvature", "minLongitudinalOffset", "minSectionLength", "occludedVehicleType", "placeOccluders"]
    MAXCURVATURE_FIELD_NUMBER: ClassVar[int]
    MAXLONGITUDINALOFFSET_FIELD_NUMBER: ClassVar[int]
    MINCURVATURE_FIELD_NUMBER: ClassVar[int]
    MINLONGITUDINALOFFSET_FIELD_NUMBER: ClassVar[int]
    MINSECTIONLENGTH_FIELD_NUMBER: ClassVar[int]
    OCCLUDEDVEHICLETYPE_FIELD_NUMBER: ClassVar[int]
    PLACEOCCLUDERS_FIELD_NUMBER: ClassVar[int]
    maxCurvature: float
    maxLongitudinalOffset: float
    minCurvature: float
    minLongitudinalOffset: float
    minSectionLength: float
    occludedVehicleType: VehicleType
    placeOccluders: bool
    def __init__(self, minCurvature: Optional[float] = ..., maxCurvature: Optional[float] = ..., minSectionLength: Optional[float] = ..., minLongitudinalOffset: Optional[float] = ..., maxLongitudinalOffset: Optional[float] = ..., placeOccluders: bool = ..., occludedVehicleType: Optional[Union[VehicleType, str]] = ...) -> None: ...

class DebrisScenarioGeneratorInfo(_message.Message):
    __slots__ = ["foliageCenterBias", "foliageDebrisAssetRemoveTag", "foliageDebrisAssetTag", "foliageDensity", "largeDebrisAssetRemoveTag", "largeDebrisAssetTag", "largeDebrisCenterBias", "largeDebrisDensity", "maxFoliageDistance", "maxLargeDebrisDistance", "maxSmallDebrisDistance", "minDistanceFromLaneEdgeForShortDebris", "minFoliageDistance", "minHeightDebrisToPlaceAtLaneEdges", "minLargeDebrisDistance", "minSmallDebrisDistance", "smallDebrisAssetRemoveTag", "smallDebrisAssetTag", "smallDebrisCenterBias", "smallDebrisDensity"]
    FOLIAGECENTERBIAS_FIELD_NUMBER: ClassVar[int]
    FOLIAGEDEBRISASSETREMOVETAG_FIELD_NUMBER: ClassVar[int]
    FOLIAGEDEBRISASSETTAG_FIELD_NUMBER: ClassVar[int]
    FOLIAGEDENSITY_FIELD_NUMBER: ClassVar[int]
    LARGEDEBRISASSETREMOVETAG_FIELD_NUMBER: ClassVar[int]
    LARGEDEBRISASSETTAG_FIELD_NUMBER: ClassVar[int]
    LARGEDEBRISCENTERBIAS_FIELD_NUMBER: ClassVar[int]
    LARGEDEBRISDENSITY_FIELD_NUMBER: ClassVar[int]
    MAXFOLIAGEDISTANCE_FIELD_NUMBER: ClassVar[int]
    MAXLARGEDEBRISDISTANCE_FIELD_NUMBER: ClassVar[int]
    MAXSMALLDEBRISDISTANCE_FIELD_NUMBER: ClassVar[int]
    MINDISTANCEFROMLANEEDGEFORSHORTDEBRIS_FIELD_NUMBER: ClassVar[int]
    MINFOLIAGEDISTANCE_FIELD_NUMBER: ClassVar[int]
    MINHEIGHTDEBRISTOPLACEATLANEEDGES_FIELD_NUMBER: ClassVar[int]
    MINLARGEDEBRISDISTANCE_FIELD_NUMBER: ClassVar[int]
    MINSMALLDEBRISDISTANCE_FIELD_NUMBER: ClassVar[int]
    SMALLDEBRISASSETREMOVETAG_FIELD_NUMBER: ClassVar[int]
    SMALLDEBRISASSETTAG_FIELD_NUMBER: ClassVar[int]
    SMALLDEBRISCENTERBIAS_FIELD_NUMBER: ClassVar[int]
    SMALLDEBRISDENSITY_FIELD_NUMBER: ClassVar[int]
    foliageCenterBias: float
    foliageDebrisAssetRemoveTag: str
    foliageDebrisAssetTag: str
    foliageDensity: float
    largeDebrisAssetRemoveTag: str
    largeDebrisAssetTag: str
    largeDebrisCenterBias: float
    largeDebrisDensity: float
    maxFoliageDistance: float
    maxLargeDebrisDistance: float
    maxSmallDebrisDistance: float
    minDistanceFromLaneEdgeForShortDebris: float
    minFoliageDistance: float
    minHeightDebrisToPlaceAtLaneEdges: float
    minLargeDebrisDistance: float
    minSmallDebrisDistance: float
    smallDebrisAssetRemoveTag: str
    smallDebrisAssetTag: str
    smallDebrisCenterBias: float
    smallDebrisDensity: float
    def __init__(self, smallDebrisDensity: Optional[float] = ..., largeDebrisDensity: Optional[float] = ..., foliageDensity: Optional[float] = ..., smallDebrisCenterBias: Optional[float] = ..., largeDebrisCenterBias: Optional[float] = ..., foliageCenterBias: Optional[float] = ..., minFoliageDistance: Optional[float] = ..., maxFoliageDistance: Optional[float] = ..., minLargeDebrisDistance: Optional[float] = ..., maxLargeDebrisDistance: Optional[float] = ..., minSmallDebrisDistance: Optional[float] = ..., maxSmallDebrisDistance: Optional[float] = ..., smallDebrisAssetTag: Optional[str] = ..., largeDebrisAssetTag: Optional[str] = ..., foliageDebrisAssetTag: Optional[str] = ..., smallDebrisAssetRemoveTag: Optional[str] = ..., largeDebrisAssetRemoveTag: Optional[str] = ..., foliageDebrisAssetRemoveTag: Optional[str] = ..., minHeightDebrisToPlaceAtLaneEdges: Optional[float] = ..., minDistanceFromLaneEdgeForShortDebris: Optional[float] = ...) -> None: ...

class DrivewayScenarioGeneratorInfo(_message.Message):
    __slots__ = ["brakeUntilEgoTimeToAgentS", "drivewayVehiclesFacingRoadProbability", "egoSpawnLocationProbability", "enablePropOcclusions", "enableVehicleOcclusions", "excludeDrivewayParkingEntryRoadType", "excludeDrivewayRoadType", "maxDrivewayLateralOffsetPercentage", "maxDrivewayLongitudinalOffsetPercentage", "maxEgoSpawnDistFromDriveway", "minDrivewayLateralOffsetPercentage", "minDrivewayLongitudinalOffsetPercentage", "minEgoSpawnDistFromDriveway", "occlusionOffsetDist", "placeEgoOnClosestCrossRoadLane", "propOcclusionCountDist", "propOcclusionSpacingDist", "useBrakeUntilEgoTimeToAgent", "vehicleDepartsDrivewayProbability"]
    BRAKEUNTILEGOTIMETOAGENTS_FIELD_NUMBER: ClassVar[int]
    DRIVEWAYVEHICLESFACINGROADPROBABILITY_FIELD_NUMBER: ClassVar[int]
    EGOSPAWNLOCATIONPROBABILITY_FIELD_NUMBER: ClassVar[int]
    ENABLEPROPOCCLUSIONS_FIELD_NUMBER: ClassVar[int]
    ENABLEVEHICLEOCCLUSIONS_FIELD_NUMBER: ClassVar[int]
    EXCLUDEDRIVEWAYPARKINGENTRYROADTYPE_FIELD_NUMBER: ClassVar[int]
    EXCLUDEDRIVEWAYROADTYPE_FIELD_NUMBER: ClassVar[int]
    MAXDRIVEWAYLATERALOFFSETPERCENTAGE_FIELD_NUMBER: ClassVar[int]
    MAXDRIVEWAYLONGITUDINALOFFSETPERCENTAGE_FIELD_NUMBER: ClassVar[int]
    MAXEGOSPAWNDISTFROMDRIVEWAY_FIELD_NUMBER: ClassVar[int]
    MINDRIVEWAYLATERALOFFSETPERCENTAGE_FIELD_NUMBER: ClassVar[int]
    MINDRIVEWAYLONGITUDINALOFFSETPERCENTAGE_FIELD_NUMBER: ClassVar[int]
    MINEGOSPAWNDISTFROMDRIVEWAY_FIELD_NUMBER: ClassVar[int]
    OCCLUSIONOFFSETDIST_FIELD_NUMBER: ClassVar[int]
    PLACEEGOONCLOSESTCROSSROADLANE_FIELD_NUMBER: ClassVar[int]
    PROPOCCLUSIONCOUNTDIST_FIELD_NUMBER: ClassVar[int]
    PROPOCCLUSIONSPACINGDIST_FIELD_NUMBER: ClassVar[int]
    USEBRAKEUNTILEGOTIMETOAGENT_FIELD_NUMBER: ClassVar[int]
    VEHICLEDEPARTSDRIVEWAYPROBABILITY_FIELD_NUMBER: ClassVar[int]
    brakeUntilEgoTimeToAgentS: _pd_unified_generator_pb2.CenterSpreadConfig
    drivewayVehiclesFacingRoadProbability: float
    egoSpawnLocationProbability: _pd_distributions_pb2.EnumDistribution
    enablePropOcclusions: bool
    enableVehicleOcclusions: bool
    excludeDrivewayParkingEntryRoadType: bool
    excludeDrivewayRoadType: bool
    maxDrivewayLateralOffsetPercentage: float
    maxDrivewayLongitudinalOffsetPercentage: float
    maxEgoSpawnDistFromDriveway: float
    minDrivewayLateralOffsetPercentage: float
    minDrivewayLongitudinalOffsetPercentage: float
    minEgoSpawnDistFromDriveway: float
    occlusionOffsetDist: _pd_unified_generator_pb2.CenterSpreadConfig
    placeEgoOnClosestCrossRoadLane: bool
    propOcclusionCountDist: _pd_unified_generator_pb2.CenterSpreadConfigInt
    propOcclusionSpacingDist: _pd_unified_generator_pb2.CenterSpreadConfig
    useBrakeUntilEgoTimeToAgent: bool
    vehicleDepartsDrivewayProbability: float
    def __init__(self, minDrivewayLongitudinalOffsetPercentage: Optional[float] = ..., maxDrivewayLongitudinalOffsetPercentage: Optional[float] = ..., minDrivewayLateralOffsetPercentage: Optional[float] = ..., maxDrivewayLateralOffsetPercentage: Optional[float] = ..., vehicleDepartsDrivewayProbability: Optional[float] = ..., minEgoSpawnDistFromDriveway: Optional[float] = ..., maxEgoSpawnDistFromDriveway: Optional[float] = ..., drivewayVehiclesFacingRoadProbability: Optional[float] = ..., enableVehicleOcclusions: bool = ..., enablePropOcclusions: bool = ..., propOcclusionSpacingDist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., propOcclusionCountDist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfigInt, Mapping]] = ..., occlusionOffsetDist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., egoSpawnLocationProbability: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., excludeDrivewayRoadType: bool = ..., excludeDrivewayParkingEntryRoadType: bool = ..., placeEgoOnClosestCrossRoadLane: bool = ..., useBrakeUntilEgoTimeToAgent: bool = ..., brakeUntilEgoTimeToAgentS: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ...) -> None: ...

class DroneFlightScenarioGeneratorInfo(_message.Message):
    __slots__ = ["descentPathName", "maxRadiusFromTarget"]
    DESCENTPATHNAME_FIELD_NUMBER: ClassVar[int]
    MAXRADIUSFROMTARGET_FIELD_NUMBER: ClassVar[int]
    descentPathName: str
    maxRadiusFromTarget: float
    def __init__(self, maxRadiusFromTarget: Optional[float] = ..., descentPathName: Optional[str] = ...) -> None: ...

class GeneratorConfig(_message.Message):
    __slots__ = ["preset_distribution", "presets"]
    PRESETS_FIELD_NUMBER: ClassVar[int]
    PRESET_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    preset_distribution: _pd_distributions_pb2.CategoricalDistribution
    presets: _containers.RepeatedCompositeFieldContainer[GeneratorConfigPreset]
    def __init__(self, preset_distribution: Optional[Union[_pd_distributions_pb2.CategoricalDistribution, Mapping]] = ..., presets: Optional[Iterable[Union[GeneratorConfigPreset, Mapping]]] = ...) -> None: ...

class GeneratorConfigPreset(_message.Message):
    __slots__ = ["all_vehicle_test_generator", "curve_generator", "debris_generator", "driveway_generator", "drone_generator", "jaywalking_generator", "junction_generator", "kitti_generator", "lane_generator", "parking_generator", "position_generator", "prop_generator", "random_generator", "static_cam_generator", "unified_generator", "voi_generator"]
    ALL_VEHICLE_TEST_GENERATOR_FIELD_NUMBER: ClassVar[int]
    CURVE_GENERATOR_FIELD_NUMBER: ClassVar[int]
    DEBRIS_GENERATOR_FIELD_NUMBER: ClassVar[int]
    DRIVEWAY_GENERATOR_FIELD_NUMBER: ClassVar[int]
    DRONE_GENERATOR_FIELD_NUMBER: ClassVar[int]
    JAYWALKING_GENERATOR_FIELD_NUMBER: ClassVar[int]
    JUNCTION_GENERATOR_FIELD_NUMBER: ClassVar[int]
    KITTI_GENERATOR_FIELD_NUMBER: ClassVar[int]
    LANE_GENERATOR_FIELD_NUMBER: ClassVar[int]
    PARKING_GENERATOR_FIELD_NUMBER: ClassVar[int]
    POSITION_GENERATOR_FIELD_NUMBER: ClassVar[int]
    PROP_GENERATOR_FIELD_NUMBER: ClassVar[int]
    RANDOM_GENERATOR_FIELD_NUMBER: ClassVar[int]
    STATIC_CAM_GENERATOR_FIELD_NUMBER: ClassVar[int]
    UNIFIED_GENERATOR_FIELD_NUMBER: ClassVar[int]
    VOI_GENERATOR_FIELD_NUMBER: ClassVar[int]
    all_vehicle_test_generator: AllVehicleTestScenarioGeneratorInfo
    curve_generator: CurveScenarioGeneratorInfo
    debris_generator: DebrisScenarioGeneratorInfo
    driveway_generator: DrivewayScenarioGeneratorInfo
    drone_generator: DroneFlightScenarioGeneratorInfo
    jaywalking_generator: JaywalkingScenarioGeneratorInfo
    junction_generator: JunctionScenarioGeneratorInfo
    kitti_generator: KittiScenarioGeneratorInfo
    lane_generator: LaneTypeScenarioGeneratorInfo
    parking_generator: ParkingScenarioGeneratorInfo
    position_generator: VehiclePositionScenarioGeneratorInfo
    prop_generator: PropScenarioGeneratorInfo
    random_generator: RandomLaneScenarioGeneratorInfo
    static_cam_generator: StaticCamScenarioGeneratorInfo
    unified_generator: _pd_unified_generator_pb2.UnifiedGeneratorParameters
    voi_generator: VehicleOfInterestScenarioGeneratorInfo
    def __init__(self, random_generator: Optional[Union[RandomLaneScenarioGeneratorInfo, Mapping]] = ..., junction_generator: Optional[Union[JunctionScenarioGeneratorInfo, Mapping]] = ..., voi_generator: Optional[Union[VehicleOfInterestScenarioGeneratorInfo, Mapping]] = ..., kitti_generator: Optional[Union[KittiScenarioGeneratorInfo, Mapping]] = ..., position_generator: Optional[Union[VehiclePositionScenarioGeneratorInfo, Mapping]] = ..., lane_generator: Optional[Union[LaneTypeScenarioGeneratorInfo, Mapping]] = ..., static_cam_generator: Optional[Union[StaticCamScenarioGeneratorInfo, Mapping]] = ..., jaywalking_generator: Optional[Union[JaywalkingScenarioGeneratorInfo, Mapping]] = ..., prop_generator: Optional[Union[PropScenarioGeneratorInfo, Mapping]] = ..., debris_generator: Optional[Union[DebrisScenarioGeneratorInfo, Mapping]] = ..., driveway_generator: Optional[Union[DrivewayScenarioGeneratorInfo, Mapping]] = ..., all_vehicle_test_generator: Optional[Union[AllVehicleTestScenarioGeneratorInfo, Mapping]] = ..., curve_generator: Optional[Union[CurveScenarioGeneratorInfo, Mapping]] = ..., parking_generator: Optional[Union[ParkingScenarioGeneratorInfo, Mapping]] = ..., drone_generator: Optional[Union[DroneFlightScenarioGeneratorInfo, Mapping]] = ..., unified_generator: Optional[Union[_pd_unified_generator_pb2.UnifiedGeneratorParameters, Mapping]] = ...) -> None: ...

class JaywalkingScenarioGeneratorInfo(_message.Message):
    __slots__ = ["animalProbability", "coneDensity", "generateOccluders", "jaywalkerConeAngle", "jaywalkerEgoCarlengths", "jaywalkerFinalRadiusSpread", "jaywalkerMaxDistance", "jaywalkerMinDistance", "jaywalkerNumber", "jaywalkerRoadDistanceMax", "jaywalkerRoadDistanceMin", "placeCarOccluders", "placePropOccluders", "signal_light_distribution", "vehicleOccluderPreference"]
    ANIMALPROBABILITY_FIELD_NUMBER: ClassVar[int]
    CONEDENSITY_FIELD_NUMBER: ClassVar[int]
    GENERATEOCCLUDERS_FIELD_NUMBER: ClassVar[int]
    JAYWALKERCONEANGLE_FIELD_NUMBER: ClassVar[int]
    JAYWALKEREGOCARLENGTHS_FIELD_NUMBER: ClassVar[int]
    JAYWALKERFINALRADIUSSPREAD_FIELD_NUMBER: ClassVar[int]
    JAYWALKERMAXDISTANCE_FIELD_NUMBER: ClassVar[int]
    JAYWALKERMINDISTANCE_FIELD_NUMBER: ClassVar[int]
    JAYWALKERNUMBER_FIELD_NUMBER: ClassVar[int]
    JAYWALKERROADDISTANCEMAX_FIELD_NUMBER: ClassVar[int]
    JAYWALKERROADDISTANCEMIN_FIELD_NUMBER: ClassVar[int]
    PLACECAROCCLUDERS_FIELD_NUMBER: ClassVar[int]
    PLACEPROPOCCLUDERS_FIELD_NUMBER: ClassVar[int]
    SIGNAL_LIGHT_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    VEHICLEOCCLUDERPREFERENCE_FIELD_NUMBER: ClassVar[int]
    animalProbability: float
    coneDensity: float
    generateOccluders: bool
    jaywalkerConeAngle: float
    jaywalkerEgoCarlengths: float
    jaywalkerFinalRadiusSpread: float
    jaywalkerMaxDistance: float
    jaywalkerMinDistance: float
    jaywalkerNumber: int
    jaywalkerRoadDistanceMax: float
    jaywalkerRoadDistanceMin: float
    placeCarOccluders: bool
    placePropOccluders: bool
    signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution
    vehicleOccluderPreference: float
    def __init__(self, jaywalkerMaxDistance: Optional[float] = ..., jaywalkerMinDistance: Optional[float] = ..., jaywalkerConeAngle: Optional[float] = ..., jaywalkerEgoCarlengths: Optional[float] = ..., jaywalkerFinalRadiusSpread: Optional[float] = ..., jaywalkerNumber: Optional[int] = ..., jaywalkerRoadDistanceMax: Optional[float] = ..., jaywalkerRoadDistanceMin: Optional[float] = ..., generateOccluders: bool = ..., placeCarOccluders: bool = ..., placePropOccluders: bool = ..., animalProbability: Optional[float] = ..., coneDensity: Optional[float] = ..., vehicleOccluderPreference: Optional[float] = ..., signal_light_distribution: Optional[Union[_pd_unified_generator_pb2.SignalLightDistribution, Mapping]] = ...) -> None: ...

class JunctionScenarioGenerator(_message.Message):
    __slots__ = ["crowd_density", "junction_id", "junction_ids", "max_distance_to_junction", "min_distance_to_junction", "signal_light_distribution", "turn_type_distribution"]
    CROWD_DENSITY_FIELD_NUMBER: ClassVar[int]
    JUNCTION_IDS_FIELD_NUMBER: ClassVar[int]
    JUNCTION_ID_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    MIN_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    SIGNAL_LIGHT_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    TURN_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    crowd_density: float
    junction_id: int
    junction_ids: _containers.RepeatedScalarFieldContainer[int]
    max_distance_to_junction: float
    min_distance_to_junction: float
    signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution
    turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution
    def __init__(self, min_distance_to_junction: Optional[float] = ..., max_distance_to_junction: Optional[float] = ..., crowd_density: Optional[float] = ..., signal_light_distribution: Optional[Union[_pd_unified_generator_pb2.SignalLightDistribution, Mapping]] = ..., turn_type_distribution: Optional[Union[_pd_unified_generator_pb2.TurnTypeDistribution, Mapping]] = ..., junction_id: Optional[int] = ..., junction_ids: Optional[Iterable[int]] = ...) -> None: ...

class JunctionScenarioGeneratorInfo(_message.Message):
    __slots__ = ["allow_crossing_peds", "cone_placement_freq", "cone_placement_max_dist", "control_type_distribution", "cross_road_speed_limit_mps", "crowd_density", "ego_stopped_at_junction", "enable_prop_occlusions", "enable_vehicle_occlusions", "force_cross_traffic", "geometry_type_distribution", "junction_id", "junction_ids", "max_distance_to_junction", "min_distance_to_junction", "occlusion_offset_dist", "prop_occlusion_count_dist", "prop_occlusion_spacing_dist", "road_type_distribution", "signal_light_distribution", "turn_type_distribution", "use_cross_road_speed_limit", "use_only_cross_roads_with_straight_turn_type"]
    ALLOW_CROSSING_PEDS_FIELD_NUMBER: ClassVar[int]
    CONE_PLACEMENT_FREQ_FIELD_NUMBER: ClassVar[int]
    CONE_PLACEMENT_MAX_DIST_FIELD_NUMBER: ClassVar[int]
    CONTROL_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    CROSS_ROAD_SPEED_LIMIT_MPS_FIELD_NUMBER: ClassVar[int]
    CROWD_DENSITY_FIELD_NUMBER: ClassVar[int]
    EGO_STOPPED_AT_JUNCTION_FIELD_NUMBER: ClassVar[int]
    ENABLE_PROP_OCCLUSIONS_FIELD_NUMBER: ClassVar[int]
    ENABLE_VEHICLE_OCCLUSIONS_FIELD_NUMBER: ClassVar[int]
    FORCE_CROSS_TRAFFIC_FIELD_NUMBER: ClassVar[int]
    GEOMETRY_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    JUNCTION_IDS_FIELD_NUMBER: ClassVar[int]
    JUNCTION_ID_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    MIN_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    OCCLUSION_OFFSET_DIST_FIELD_NUMBER: ClassVar[int]
    PROP_OCCLUSION_COUNT_DIST_FIELD_NUMBER: ClassVar[int]
    PROP_OCCLUSION_SPACING_DIST_FIELD_NUMBER: ClassVar[int]
    ROAD_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    SIGNAL_LIGHT_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    TURN_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    USE_CROSS_ROAD_SPEED_LIMIT_FIELD_NUMBER: ClassVar[int]
    USE_ONLY_CROSS_ROADS_WITH_STRAIGHT_TURN_TYPE_FIELD_NUMBER: ClassVar[int]
    allow_crossing_peds: bool
    cone_placement_freq: float
    cone_placement_max_dist: float
    control_type_distribution: _pd_distributions_pb2.EnumDistribution
    cross_road_speed_limit_mps: _pd_unified_generator_pb2.MinMaxConfigFloat
    crowd_density: float
    ego_stopped_at_junction: bool
    enable_prop_occlusions: bool
    enable_vehicle_occlusions: bool
    force_cross_traffic: bool
    geometry_type_distribution: _pd_distributions_pb2.EnumDistribution
    junction_id: int
    junction_ids: _containers.RepeatedScalarFieldContainer[int]
    max_distance_to_junction: float
    min_distance_to_junction: float
    occlusion_offset_dist: _pd_unified_generator_pb2.CenterSpreadConfig
    prop_occlusion_count_dist: _pd_unified_generator_pb2.CenterSpreadConfigInt
    prop_occlusion_spacing_dist: _pd_unified_generator_pb2.CenterSpreadConfig
    road_type_distribution: _pd_distributions_pb2.EnumDistribution
    signal_light_distribution: _pd_unified_generator_pb2.SignalLightDistribution
    turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution
    use_cross_road_speed_limit: bool
    use_only_cross_roads_with_straight_turn_type: bool
    def __init__(self, min_distance_to_junction: Optional[float] = ..., max_distance_to_junction: Optional[float] = ..., signal_light_distribution: Optional[Union[_pd_unified_generator_pb2.SignalLightDistribution, Mapping]] = ..., turn_type_distribution: Optional[Union[_pd_unified_generator_pb2.TurnTypeDistribution, Mapping]] = ..., junction_id: Optional[int] = ..., junction_ids: Optional[Iterable[int]] = ..., crowd_density: Optional[float] = ..., force_cross_traffic: bool = ..., control_type_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., geometry_type_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., road_type_distribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., allow_crossing_peds: bool = ..., enable_vehicle_occlusions: bool = ..., enable_prop_occlusions: bool = ..., prop_occlusion_spacing_dist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., prop_occlusion_count_dist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfigInt, Mapping]] = ..., occlusion_offset_dist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., use_cross_road_speed_limit: bool = ..., cross_road_speed_limit_mps: Optional[Union[_pd_unified_generator_pb2.MinMaxConfigFloat, Mapping]] = ..., use_only_cross_roads_with_straight_turn_type: bool = ..., ego_stopped_at_junction: bool = ..., cone_placement_freq: Optional[float] = ..., cone_placement_max_dist: Optional[float] = ...) -> None: ...

class KittiScenarioGenerator(_message.Message):
    __slots__ = ["max_distance_to_junction", "min_distance_to_junction", "turn_type_distribution"]
    MAX_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    MIN_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    TURN_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    max_distance_to_junction: float
    min_distance_to_junction: float
    turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution
    def __init__(self, min_distance_to_junction: Optional[float] = ..., max_distance_to_junction: Optional[float] = ..., turn_type_distribution: Optional[Union[_pd_unified_generator_pb2.TurnTypeDistribution, Mapping]] = ...) -> None: ...

class KittiScenarioGeneratorInfo(_message.Message):
    __slots__ = ["max_distance_to_junction", "min_distance_to_junction", "turn_type_distribution"]
    MAX_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    MIN_DISTANCE_TO_JUNCTION_FIELD_NUMBER: ClassVar[int]
    TURN_TYPE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    max_distance_to_junction: float
    min_distance_to_junction: float
    turn_type_distribution: _pd_unified_generator_pb2.TurnTypeDistribution
    def __init__(self, min_distance_to_junction: Optional[float] = ..., max_distance_to_junction: Optional[float] = ..., turn_type_distribution: Optional[Union[_pd_unified_generator_pb2.TurnTypeDistribution, Mapping]] = ...) -> None: ...

class LaneTypeScenarioGeneratorInfo(_message.Message):
    __slots__ = ["asset_search_radius", "asset_tags", "dead_zone", "dead_zone_spread", "lane_type", "num_instances"]
    ASSET_SEARCH_RADIUS_FIELD_NUMBER: ClassVar[int]
    ASSET_TAGS_FIELD_NUMBER: ClassVar[int]
    DEAD_ZONE_FIELD_NUMBER: ClassVar[int]
    DEAD_ZONE_SPREAD_FIELD_NUMBER: ClassVar[int]
    LANE_TYPE_FIELD_NUMBER: ClassVar[int]
    NUM_INSTANCES_FIELD_NUMBER: ClassVar[int]
    asset_search_radius: _pd_unified_generator_pb2.CenterSpreadConfig
    asset_tags: str
    dead_zone: float
    dead_zone_spread: float
    lane_type: int
    num_instances: _pd_unified_generator_pb2.MinMaxConfigInt
    def __init__(self, lane_type: Optional[int] = ..., dead_zone: Optional[float] = ..., dead_zone_spread: Optional[float] = ..., asset_tags: Optional[str] = ..., asset_search_radius: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., num_instances: Optional[Union[_pd_unified_generator_pb2.MinMaxConfigInt, Mapping]] = ...) -> None: ...

class ParkingScenarioGeneratorInfo(_message.Message):
    __slots__ = ["aisleLateralOffsetBackIn", "aisleLateralOffsetNoseIn", "egoParkPerturbationAngle", "egoParkPerturbationLateralOffset", "egoParkPerturbationLongitudinalOffset", "exitAfterParking", "exitStraight", "maxPedsInParkingSpaces", "noseInProbability", "parkingSpacePedestrianDensity", "parkingTypeDistribution", "perpendicularOnRoadProbability", "placeVehicleInFrontOfParallelSpot", "pullOutProbability", "timeToParkingSpace"]
    AISLELATERALOFFSETBACKIN_FIELD_NUMBER: ClassVar[int]
    AISLELATERALOFFSETNOSEIN_FIELD_NUMBER: ClassVar[int]
    EGOPARKPERTURBATIONANGLE_FIELD_NUMBER: ClassVar[int]
    EGOPARKPERTURBATIONLATERALOFFSET_FIELD_NUMBER: ClassVar[int]
    EGOPARKPERTURBATIONLONGITUDINALOFFSET_FIELD_NUMBER: ClassVar[int]
    EXITAFTERPARKING_FIELD_NUMBER: ClassVar[int]
    EXITSTRAIGHT_FIELD_NUMBER: ClassVar[int]
    MAXPEDSINPARKINGSPACES_FIELD_NUMBER: ClassVar[int]
    NOSEINPROBABILITY_FIELD_NUMBER: ClassVar[int]
    PARKINGSPACEPEDESTRIANDENSITY_FIELD_NUMBER: ClassVar[int]
    PARKINGTYPEDISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    PERPENDICULARONROADPROBABILITY_FIELD_NUMBER: ClassVar[int]
    PLACEVEHICLEINFRONTOFPARALLELSPOT_FIELD_NUMBER: ClassVar[int]
    PULLOUTPROBABILITY_FIELD_NUMBER: ClassVar[int]
    TIMETOPARKINGSPACE_FIELD_NUMBER: ClassVar[int]
    aisleLateralOffsetBackIn: _pd_unified_generator_pb2.CenterSpreadConfig
    aisleLateralOffsetNoseIn: _pd_unified_generator_pb2.CenterSpreadConfig
    egoParkPerturbationAngle: _pd_unified_generator_pb2.CenterSpreadConfig
    egoParkPerturbationLateralOffset: _pd_unified_generator_pb2.CenterSpreadConfig
    egoParkPerturbationLongitudinalOffset: _pd_unified_generator_pb2.CenterSpreadConfig
    exitAfterParking: bool
    exitStraight: bool
    maxPedsInParkingSpaces: int
    noseInProbability: float
    parkingSpacePedestrianDensity: _pd_unified_generator_pb2.CenterSpreadConfig
    parkingTypeDistribution: _pd_distributions_pb2.EnumDistribution
    perpendicularOnRoadProbability: float
    placeVehicleInFrontOfParallelSpot: bool
    pullOutProbability: float
    timeToParkingSpace: _pd_unified_generator_pb2.CenterSpreadConfig
    def __init__(self, parkingTypeDistribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., egoParkPerturbationAngle: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., egoParkPerturbationLongitudinalOffset: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., egoParkPerturbationLateralOffset: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., pullOutProbability: Optional[float] = ..., noseInProbability: Optional[float] = ..., timeToParkingSpace: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., parkingSpacePedestrianDensity: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., maxPedsInParkingSpaces: Optional[int] = ..., aisleLateralOffsetNoseIn: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., aisleLateralOffsetBackIn: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., exitAfterParking: bool = ..., exitStraight: bool = ..., placeVehicleInFrontOfParallelSpot: bool = ..., perpendicularOnRoadProbability: Optional[float] = ...) -> None: ...

class PositionGenerator(_message.Message):
    __slots__ = ["ego_behind_star", "face_same_direction", "junction_ids", "radius_to_star_max", "radius_to_star_min", "star_vehicles"]
    EGO_BEHIND_STAR_FIELD_NUMBER: ClassVar[int]
    FACE_SAME_DIRECTION_FIELD_NUMBER: ClassVar[int]
    JUNCTION_IDS_FIELD_NUMBER: ClassVar[int]
    RADIUS_TO_STAR_MAX_FIELD_NUMBER: ClassVar[int]
    RADIUS_TO_STAR_MIN_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLES_FIELD_NUMBER: ClassVar[int]
    ego_behind_star: bool
    face_same_direction: bool
    junction_ids: _containers.RepeatedScalarFieldContainer[int]
    radius_to_star_max: float
    radius_to_star_min: float
    star_vehicles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, radius_to_star_min: Optional[float] = ..., radius_to_star_max: Optional[float] = ..., star_vehicles: Optional[Iterable[str]] = ..., junction_ids: Optional[Iterable[int]] = ..., face_same_direction: bool = ..., ego_behind_star: bool = ...) -> None: ...

class PropScenarioGeneratorInfo(_message.Message):
    __slots__ = ["closureConeLength", "closureConeLengthForSingleLaneClosure", "closureConeSpacing", "coneAssetTag", "coneSpacing", "initialMessageBoardAssetTag", "initialMessageBoardRightAssetTag", "intermediateMessageBoardAngleVariation", "intermediateMessageBoardAssetTag", "intermediateMessageBoardRightAssetTag", "leadConeLength", "leadConeLengthForSingleLaneClosure", "leadConeSpacing", "maxConeAngleDeviation", "maxConeSpacingDeviationPercent", "maxLanesToClose", "maxLateralClosureConeSpacingDeviation", "maxLateralLeadConeSpacingDeviation", "maxLateralTaperConeSpacingDeviation", "minLanesToClose", "minTaperLength", "missing_cone_chance", "num_fallen_cone_groups", "placeClosureCones", "placeIntermediateMessageBoards", "placeIntermediateMessageBoardsProbability", "placeLeadCones", "placeMessageBoard", "propMaxDistance", "propMinDistance", "propTag", "propVehicleTag", "reduce_spawn_to_zero_at_construction_range", "rightSideClosureProbability", "scenario_cull_on_bad_cone_fov", "scenario_cull_on_bad_cone_los", "size_fallen_cone_groups", "suffix_fallen_cone_assets", "taperLengthScaleFactor", "taperLengthSpeedSpreadPercent", "taperLowerSpeedThreshold", "taperSlowFormulaDemoninator", "taperUpperSpeedThreshold", "vehiclePlacementProbability"]
    CLOSURECONELENGTHFORSINGLELANECLOSURE_FIELD_NUMBER: ClassVar[int]
    CLOSURECONELENGTH_FIELD_NUMBER: ClassVar[int]
    CLOSURECONESPACING_FIELD_NUMBER: ClassVar[int]
    CONEASSETTAG_FIELD_NUMBER: ClassVar[int]
    CONESPACING_FIELD_NUMBER: ClassVar[int]
    INITIALMESSAGEBOARDASSETTAG_FIELD_NUMBER: ClassVar[int]
    INITIALMESSAGEBOARDRIGHTASSETTAG_FIELD_NUMBER: ClassVar[int]
    INTERMEDIATEMESSAGEBOARDANGLEVARIATION_FIELD_NUMBER: ClassVar[int]
    INTERMEDIATEMESSAGEBOARDASSETTAG_FIELD_NUMBER: ClassVar[int]
    INTERMEDIATEMESSAGEBOARDRIGHTASSETTAG_FIELD_NUMBER: ClassVar[int]
    LEADCONELENGTHFORSINGLELANECLOSURE_FIELD_NUMBER: ClassVar[int]
    LEADCONELENGTH_FIELD_NUMBER: ClassVar[int]
    LEADCONESPACING_FIELD_NUMBER: ClassVar[int]
    MAXCONEANGLEDEVIATION_FIELD_NUMBER: ClassVar[int]
    MAXCONESPACINGDEVIATIONPERCENT_FIELD_NUMBER: ClassVar[int]
    MAXLANESTOCLOSE_FIELD_NUMBER: ClassVar[int]
    MAXLATERALCLOSURECONESPACINGDEVIATION_FIELD_NUMBER: ClassVar[int]
    MAXLATERALLEADCONESPACINGDEVIATION_FIELD_NUMBER: ClassVar[int]
    MAXLATERALTAPERCONESPACINGDEVIATION_FIELD_NUMBER: ClassVar[int]
    MINLANESTOCLOSE_FIELD_NUMBER: ClassVar[int]
    MINTAPERLENGTH_FIELD_NUMBER: ClassVar[int]
    MISSING_CONE_CHANCE_FIELD_NUMBER: ClassVar[int]
    NUM_FALLEN_CONE_GROUPS_FIELD_NUMBER: ClassVar[int]
    PLACECLOSURECONES_FIELD_NUMBER: ClassVar[int]
    PLACEINTERMEDIATEMESSAGEBOARDSPROBABILITY_FIELD_NUMBER: ClassVar[int]
    PLACEINTERMEDIATEMESSAGEBOARDS_FIELD_NUMBER: ClassVar[int]
    PLACELEADCONES_FIELD_NUMBER: ClassVar[int]
    PLACEMESSAGEBOARD_FIELD_NUMBER: ClassVar[int]
    PROPMAXDISTANCE_FIELD_NUMBER: ClassVar[int]
    PROPMINDISTANCE_FIELD_NUMBER: ClassVar[int]
    PROPTAG_FIELD_NUMBER: ClassVar[int]
    PROPVEHICLETAG_FIELD_NUMBER: ClassVar[int]
    REDUCE_SPAWN_TO_ZERO_AT_CONSTRUCTION_RANGE_FIELD_NUMBER: ClassVar[int]
    RIGHTSIDECLOSUREPROBABILITY_FIELD_NUMBER: ClassVar[int]
    SCENARIO_CULL_ON_BAD_CONE_FOV_FIELD_NUMBER: ClassVar[int]
    SCENARIO_CULL_ON_BAD_CONE_LOS_FIELD_NUMBER: ClassVar[int]
    SIZE_FALLEN_CONE_GROUPS_FIELD_NUMBER: ClassVar[int]
    SUFFIX_FALLEN_CONE_ASSETS_FIELD_NUMBER: ClassVar[int]
    TAPERLENGTHSCALEFACTOR_FIELD_NUMBER: ClassVar[int]
    TAPERLENGTHSPEEDSPREADPERCENT_FIELD_NUMBER: ClassVar[int]
    TAPERLOWERSPEEDTHRESHOLD_FIELD_NUMBER: ClassVar[int]
    TAPERSLOWFORMULADEMONINATOR_FIELD_NUMBER: ClassVar[int]
    TAPERUPPERSPEEDTHRESHOLD_FIELD_NUMBER: ClassVar[int]
    VEHICLEPLACEMENTPROBABILITY_FIELD_NUMBER: ClassVar[int]
    closureConeLength: _pd_unified_generator_pb2.CenterSpreadConfig
    closureConeLengthForSingleLaneClosure: _pd_unified_generator_pb2.CenterSpreadConfig
    closureConeSpacing: _pd_unified_generator_pb2.CenterSpreadConfig
    coneAssetTag: str
    coneSpacing: _pd_unified_generator_pb2.CenterSpreadConfig
    initialMessageBoardAssetTag: str
    initialMessageBoardRightAssetTag: str
    intermediateMessageBoardAngleVariation: float
    intermediateMessageBoardAssetTag: str
    intermediateMessageBoardRightAssetTag: str
    leadConeLength: _pd_unified_generator_pb2.CenterSpreadConfig
    leadConeLengthForSingleLaneClosure: _pd_unified_generator_pb2.CenterSpreadConfig
    leadConeSpacing: _pd_unified_generator_pb2.CenterSpreadConfig
    maxConeAngleDeviation: float
    maxConeSpacingDeviationPercent: float
    maxLanesToClose: int
    maxLateralClosureConeSpacingDeviation: float
    maxLateralLeadConeSpacingDeviation: float
    maxLateralTaperConeSpacingDeviation: float
    minLanesToClose: int
    minTaperLength: float
    missing_cone_chance: float
    num_fallen_cone_groups: _pd_unified_generator_pb2.CenterSpreadConfig
    placeClosureCones: bool
    placeIntermediateMessageBoards: bool
    placeIntermediateMessageBoardsProbability: float
    placeLeadCones: bool
    placeMessageBoard: bool
    propMaxDistance: float
    propMinDistance: float
    propTag: str
    propVehicleTag: str
    reduce_spawn_to_zero_at_construction_range: float
    rightSideClosureProbability: float
    scenario_cull_on_bad_cone_fov: float
    scenario_cull_on_bad_cone_los: bool
    size_fallen_cone_groups: _pd_unified_generator_pb2.CenterSpreadConfig
    suffix_fallen_cone_assets: str
    taperLengthScaleFactor: float
    taperLengthSpeedSpreadPercent: float
    taperLowerSpeedThreshold: float
    taperSlowFormulaDemoninator: float
    taperUpperSpeedThreshold: float
    vehiclePlacementProbability: float
    def __init__(self, propMaxDistance: Optional[float] = ..., propMinDistance: Optional[float] = ..., placeMessageBoard: bool = ..., initialMessageBoardAssetTag: Optional[str] = ..., initialMessageBoardRightAssetTag: Optional[str] = ..., placeIntermediateMessageBoards: bool = ..., placeIntermediateMessageBoardsProbability: Optional[float] = ..., intermediateMessageBoardAssetTag: Optional[str] = ..., intermediateMessageBoardRightAssetTag: Optional[str] = ..., intermediateMessageBoardAngleVariation: Optional[float] = ..., coneSpacing: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., maxConeSpacingDeviationPercent: Optional[float] = ..., maxLateralTaperConeSpacingDeviation: Optional[float] = ..., maxLateralClosureConeSpacingDeviation: Optional[float] = ..., maxLateralLeadConeSpacingDeviation: Optional[float] = ..., maxConeAngleDeviation: Optional[float] = ..., coneAssetTag: Optional[str] = ..., taperLowerSpeedThreshold: Optional[float] = ..., taperUpperSpeedThreshold: Optional[float] = ..., taperSlowFormulaDemoninator: Optional[float] = ..., minTaperLength: Optional[float] = ..., taperLengthSpeedSpreadPercent: Optional[float] = ..., taperLengthScaleFactor: Optional[float] = ..., minLanesToClose: Optional[int] = ..., maxLanesToClose: Optional[int] = ..., placeLeadCones: bool = ..., leadConeLength: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., leadConeLengthForSingleLaneClosure: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., placeClosureCones: bool = ..., closureConeLength: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., closureConeLengthForSingleLaneClosure: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., rightSideClosureProbability: Optional[float] = ..., propVehicleTag: Optional[str] = ..., propTag: Optional[str] = ..., leadConeSpacing: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., closureConeSpacing: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., scenario_cull_on_bad_cone_los: bool = ..., scenario_cull_on_bad_cone_fov: Optional[float] = ..., reduce_spawn_to_zero_at_construction_range: Optional[float] = ..., missing_cone_chance: Optional[float] = ..., num_fallen_cone_groups: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., size_fallen_cone_groups: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., suffix_fallen_cone_assets: Optional[str] = ..., vehiclePlacementProbability: Optional[float] = ...) -> None: ...

class RandomLaneScenarioGeneratorInfo(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RandomScenarioGenerator(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SpawnConfig(_message.Message):
    __slots__ = ["preset_distribution", "presets"]
    PRESETS_FIELD_NUMBER: ClassVar[int]
    PRESET_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    preset_distribution: _pd_distributions_pb2.CategoricalDistribution
    presets: _containers.RepeatedCompositeFieldContainer[SpawnConfigPreset]
    def __init__(self, preset_distribution: Optional[Union[_pd_distributions_pb2.CategoricalDistribution, Mapping]] = ..., presets: Optional[Iterable[Union[SpawnConfigPreset, Mapping]]] = ...) -> None: ...

class SpawnConfigPreset(_message.Message):
    __slots__ = ["agentStateProbabilities", "aggression", "aggressionSpread", "alignEgoPedestrianToLane", "animalSpeciesAllowed", "applyProceedOutOfTurnProbabilityToEgo", "applyRollingStopToEgo", "applyStopLineOffsetToEgo", "bicyclesOnlyInBikeLanes", "crosswalkSignDensity", "disableAccessories", "disableOccupants", "egoForceMinLengthBehind", "egoIgnoreObstacleTypes", "egoLaneChangeChance", "egoLaneChangeChanceSpread", "egoLaneChangeCooldown", "egoLaneChangeCooldownSpread", "egoMinDistToEdge", "egoMinDistToEdgeSpread", "egoMinLaneCountDist", "egoMinPathLength", "egoMinPathLengthSpread", "egoPedestrianExclusionRadius", "egoPedestrianExclusionRadiusSpread", "egoPedestrians", "egoRoadTypes", "egoVehicleModel", "emergencyLightsOnProbability", "emergencyLightsOnProbabilitySpread", "enableCrosswalkPlacement", "enableDrivewayPlacement", "enableDynamicLaneSelection", "enableJunctionPlacement", "instanceParallelParkingMarkers", "instanceParallelParkingSpaces", "junction_generator", "kitti_generator", "laneChangeChance", "laneChangeChanceSpread", "laneChangeCooldown", "laneChangeCooldownSpread", "laneDriftAmp", "laneDriftAmpSpread", "laneDriftScale", "laneDriftScaleSpread", "laneOffset", "laneOffsetSpread", "laneStartOffset", "largeVehicleTurnRadiusMultiple", "lightFlashingPeriod", "lightIlluminatedPercentage", "markerDataMap", "minNumberOfAnimals", "minNumberOfPedestrians", "numberOfAnimals", "numberOfPedestrians", "objectDecorations", "parkedVehicleSpawnProbability", "parkedVehicleSpawnProbabilitySpread", "parkedVehicleSpawnRadius", "parkingTypeDistribution", "parking_space_data", "pedestrianColorOverrideChance", "pedestrianColorOverrideChanceSpread", "pedestrianColorOverrideRGB", "pedestrianIdleProbability", "pedestrianIdleProbabilitySpread", "pedestrianJaywalkAngle", "pedestrianJaywalkLookAhead", "pedestrianJaywalkRadius", "pedestrianSpawnMinEdgeDistance", "pedestrianSpawnRadius", "pedestrianSpawnTightness", "pedestrianVelocity", "pedestrianVelocitySpread", "pedestriansDynamicPathing", "pedestriansSpawnInParkingLot", "position_generator", "proceedOutOfTurnProbability", "random_generator", "randomizeVehicleParts", "region", "restrictLargeVehicleLaneCurvature", "rollingStop", "searchRadius", "signDensity", "spawnPedestriansOnRoad", "spawnTrailerOnEgoProbability", "spawnTrailerProbabilities", "startSeparation", "startSeparationSpread", "startSeparationTime", "startVelocity", "startVelocitySpread", "stopLineOffset", "targetSeparation", "targetSeparationSpread", "targetSeparationTime", "targetVelocity", "targetVelocitySpread", "turnTypeDistribution", "useStaticTrailers", "vehicleDensityModifier", "vehicleDistribution", "vehicleRoadTypes", "voi_generator"]
    class RoadType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class MarkerDataMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_unified_generator_pb2.RoadMarkingData
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_unified_generator_pb2.RoadMarkingData, Mapping]] = ...) -> None: ...
    class SpawnTrailerProbabilitiesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: float
        def __init__(self, key: Optional[str] = ..., value: Optional[float] = ...) -> None: ...
    class StartSeparationTimeEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_unified_generator_pb2.CenterSpreadConfig
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ...) -> None: ...
    class TargetSeparationTimeEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_unified_generator_pb2.CenterSpreadConfig
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ...) -> None: ...
    class VehicleDistributionEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _pd_distributions_pb2.VehicleCategoryWeight
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_pd_distributions_pb2.VehicleCategoryWeight, Mapping]] = ...) -> None: ...
    AGENTSTATEPROBABILITIES_FIELD_NUMBER: ClassVar[int]
    AGGRESSIONSPREAD_FIELD_NUMBER: ClassVar[int]
    AGGRESSION_FIELD_NUMBER: ClassVar[int]
    ALIGNEGOPEDESTRIANTOLANE_FIELD_NUMBER: ClassVar[int]
    ANIMALSPECIESALLOWED_FIELD_NUMBER: ClassVar[int]
    APPLYPROCEEDOUTOFTURNPROBABILITYTOEGO_FIELD_NUMBER: ClassVar[int]
    APPLYROLLINGSTOPTOEGO_FIELD_NUMBER: ClassVar[int]
    APPLYSTOPLINEOFFSETTOEGO_FIELD_NUMBER: ClassVar[int]
    BICYCLESONLYINBIKELANES_FIELD_NUMBER: ClassVar[int]
    CROSSWALKSIGNDENSITY_FIELD_NUMBER: ClassVar[int]
    DISABLEACCESSORIES_FIELD_NUMBER: ClassVar[int]
    DISABLEOCCUPANTS_FIELD_NUMBER: ClassVar[int]
    DRIVEWAY: SpawnConfigPreset.RoadType
    EGOFORCEMINLENGTHBEHIND_FIELD_NUMBER: ClassVar[int]
    EGOIGNOREOBSTACLETYPES_FIELD_NUMBER: ClassVar[int]
    EGOLANECHANGECHANCESPREAD_FIELD_NUMBER: ClassVar[int]
    EGOLANECHANGECHANCE_FIELD_NUMBER: ClassVar[int]
    EGOLANECHANGECOOLDOWNSPREAD_FIELD_NUMBER: ClassVar[int]
    EGOLANECHANGECOOLDOWN_FIELD_NUMBER: ClassVar[int]
    EGOMINDISTTOEDGESPREAD_FIELD_NUMBER: ClassVar[int]
    EGOMINDISTTOEDGE_FIELD_NUMBER: ClassVar[int]
    EGOMINLANECOUNTDIST_FIELD_NUMBER: ClassVar[int]
    EGOMINPATHLENGTHSPREAD_FIELD_NUMBER: ClassVar[int]
    EGOMINPATHLENGTH_FIELD_NUMBER: ClassVar[int]
    EGOPEDESTRIANEXCLUSIONRADIUSSPREAD_FIELD_NUMBER: ClassVar[int]
    EGOPEDESTRIANEXCLUSIONRADIUS_FIELD_NUMBER: ClassVar[int]
    EGOPEDESTRIANS_FIELD_NUMBER: ClassVar[int]
    EGOROADTYPES_FIELD_NUMBER: ClassVar[int]
    EGOVEHICLEMODEL_FIELD_NUMBER: ClassVar[int]
    EMERGENCYLIGHTSONPROBABILITYSPREAD_FIELD_NUMBER: ClassVar[int]
    EMERGENCYLIGHTSONPROBABILITY_FIELD_NUMBER: ClassVar[int]
    ENABLECROSSWALKPLACEMENT_FIELD_NUMBER: ClassVar[int]
    ENABLEDRIVEWAYPLACEMENT_FIELD_NUMBER: ClassVar[int]
    ENABLEDYNAMICLANESELECTION_FIELD_NUMBER: ClassVar[int]
    ENABLEJUNCTIONPLACEMENT_FIELD_NUMBER: ClassVar[int]
    INSTANCEPARALLELPARKINGMARKERS_FIELD_NUMBER: ClassVar[int]
    INSTANCEPARALLELPARKINGSPACES_FIELD_NUMBER: ClassVar[int]
    JUNCTION_GENERATOR_FIELD_NUMBER: ClassVar[int]
    KITTI_GENERATOR_FIELD_NUMBER: ClassVar[int]
    LANECHANGECHANCESPREAD_FIELD_NUMBER: ClassVar[int]
    LANECHANGECHANCE_FIELD_NUMBER: ClassVar[int]
    LANECHANGECOOLDOWNSPREAD_FIELD_NUMBER: ClassVar[int]
    LANECHANGECOOLDOWN_FIELD_NUMBER: ClassVar[int]
    LANEDRIFTAMPSPREAD_FIELD_NUMBER: ClassVar[int]
    LANEDRIFTAMP_FIELD_NUMBER: ClassVar[int]
    LANEDRIFTSCALESPREAD_FIELD_NUMBER: ClassVar[int]
    LANEDRIFTSCALE_FIELD_NUMBER: ClassVar[int]
    LANEOFFSETSPREAD_FIELD_NUMBER: ClassVar[int]
    LANEOFFSET_FIELD_NUMBER: ClassVar[int]
    LANESTARTOFFSET_FIELD_NUMBER: ClassVar[int]
    LARGEVEHICLETURNRADIUSMULTIPLE_FIELD_NUMBER: ClassVar[int]
    LIGHTFLASHINGPERIOD_FIELD_NUMBER: ClassVar[int]
    LIGHTILLUMINATEDPERCENTAGE_FIELD_NUMBER: ClassVar[int]
    MARKERDATAMAP_FIELD_NUMBER: ClassVar[int]
    MINNUMBEROFANIMALS_FIELD_NUMBER: ClassVar[int]
    MINNUMBEROFPEDESTRIANS_FIELD_NUMBER: ClassVar[int]
    MOTORWAY: SpawnConfigPreset.RoadType
    MOTORWAY_LINK: SpawnConfigPreset.RoadType
    NUMBEROFANIMALS_FIELD_NUMBER: ClassVar[int]
    NUMBEROFPEDESTRIANS_FIELD_NUMBER: ClassVar[int]
    OBJECTDECORATIONS_FIELD_NUMBER: ClassVar[int]
    PARKEDVEHICLESPAWNPROBABILITYSPREAD_FIELD_NUMBER: ClassVar[int]
    PARKEDVEHICLESPAWNPROBABILITY_FIELD_NUMBER: ClassVar[int]
    PARKEDVEHICLESPAWNRADIUS_FIELD_NUMBER: ClassVar[int]
    PARKINGTYPEDISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    PARKING_AISLE: SpawnConfigPreset.RoadType
    PARKING_SPACE_DATA_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANCOLOROVERRIDECHANCESPREAD_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANCOLOROVERRIDECHANCE_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANCOLOROVERRIDERGB_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANIDLEPROBABILITYSPREAD_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANIDLEPROBABILITY_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANJAYWALKANGLE_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANJAYWALKLOOKAHEAD_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANJAYWALKRADIUS_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANSDYNAMICPATHING_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANSPAWNMINEDGEDISTANCE_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANSPAWNRADIUS_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANSPAWNTIGHTNESS_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANSSPAWNINPARKINGLOT_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANVELOCITYSPREAD_FIELD_NUMBER: ClassVar[int]
    PEDESTRIANVELOCITY_FIELD_NUMBER: ClassVar[int]
    POSITION_GENERATOR_FIELD_NUMBER: ClassVar[int]
    PRIMARY: SpawnConfigPreset.RoadType
    PRIMARY_LINK: SpawnConfigPreset.RoadType
    PROCEEDOUTOFTURNPROBABILITY_FIELD_NUMBER: ClassVar[int]
    RANDOMIZEVEHICLEPARTS_FIELD_NUMBER: ClassVar[int]
    RANDOM_GENERATOR_FIELD_NUMBER: ClassVar[int]
    REGION_FIELD_NUMBER: ClassVar[int]
    RESIDENTIAL: SpawnConfigPreset.RoadType
    RESTRICTLARGEVEHICLELANECURVATURE_FIELD_NUMBER: ClassVar[int]
    ROLLINGSTOP_FIELD_NUMBER: ClassVar[int]
    SEARCHRADIUS_FIELD_NUMBER: ClassVar[int]
    SECONDARY: SpawnConfigPreset.RoadType
    SECONDARY_LINK: SpawnConfigPreset.RoadType
    SERVICE: SpawnConfigPreset.RoadType
    SIGNDENSITY_FIELD_NUMBER: ClassVar[int]
    SPAWNPEDESTRIANSONROAD_FIELD_NUMBER: ClassVar[int]
    SPAWNTRAILERONEGOPROBABILITY_FIELD_NUMBER: ClassVar[int]
    SPAWNTRAILERPROBABILITIES_FIELD_NUMBER: ClassVar[int]
    STARTSEPARATIONSPREAD_FIELD_NUMBER: ClassVar[int]
    STARTSEPARATIONTIME_FIELD_NUMBER: ClassVar[int]
    STARTSEPARATION_FIELD_NUMBER: ClassVar[int]
    STARTVELOCITYSPREAD_FIELD_NUMBER: ClassVar[int]
    STARTVELOCITY_FIELD_NUMBER: ClassVar[int]
    STOPLINEOFFSET_FIELD_NUMBER: ClassVar[int]
    TARGETSEPARATIONSPREAD_FIELD_NUMBER: ClassVar[int]
    TARGETSEPARATIONTIME_FIELD_NUMBER: ClassVar[int]
    TARGETSEPARATION_FIELD_NUMBER: ClassVar[int]
    TARGETVELOCITYSPREAD_FIELD_NUMBER: ClassVar[int]
    TARGETVELOCITY_FIELD_NUMBER: ClassVar[int]
    TERTIARY: SpawnConfigPreset.RoadType
    TERTIARY_LINK: SpawnConfigPreset.RoadType
    TRUNK: SpawnConfigPreset.RoadType
    TRUNK_LINK: SpawnConfigPreset.RoadType
    TURNTYPEDISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    UNCLASSIFIED: SpawnConfigPreset.RoadType
    USESTATICTRAILERS_FIELD_NUMBER: ClassVar[int]
    VEHICLEDENSITYMODIFIER_FIELD_NUMBER: ClassVar[int]
    VEHICLEDISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    VEHICLEROADTYPES_FIELD_NUMBER: ClassVar[int]
    VOI_GENERATOR_FIELD_NUMBER: ClassVar[int]
    agentStateProbabilities: _containers.RepeatedCompositeFieldContainer[AgentStateProbabilityConfig]
    aggression: float
    aggressionSpread: float
    alignEgoPedestrianToLane: bool
    animalSpeciesAllowed: str
    applyProceedOutOfTurnProbabilityToEgo: bool
    applyRollingStopToEgo: bool
    applyStopLineOffsetToEgo: bool
    bicyclesOnlyInBikeLanes: bool
    crosswalkSignDensity: _pd_unified_generator_pb2.CenterSpreadConfig
    disableAccessories: bool
    disableOccupants: bool
    egoForceMinLengthBehind: bool
    egoIgnoreObstacleTypes: _containers.RepeatedScalarFieldContainer[str]
    egoLaneChangeChance: float
    egoLaneChangeChanceSpread: float
    egoLaneChangeCooldown: float
    egoLaneChangeCooldownSpread: float
    egoMinDistToEdge: float
    egoMinDistToEdgeSpread: float
    egoMinLaneCountDist: _pd_unified_generator_pb2.CenterSpreadConfigInt
    egoMinPathLength: float
    egoMinPathLengthSpread: float
    egoPedestrianExclusionRadius: float
    egoPedestrianExclusionRadiusSpread: float
    egoPedestrians: bool
    egoRoadTypes: _containers.RepeatedScalarFieldContainer[SpawnConfigPreset.RoadType]
    egoVehicleModel: str
    emergencyLightsOnProbability: float
    emergencyLightsOnProbabilitySpread: float
    enableCrosswalkPlacement: bool
    enableDrivewayPlacement: bool
    enableDynamicLaneSelection: bool
    enableJunctionPlacement: bool
    instanceParallelParkingMarkers: bool
    instanceParallelParkingSpaces: bool
    junction_generator: JunctionScenarioGenerator
    kitti_generator: KittiScenarioGenerator
    laneChangeChance: float
    laneChangeChanceSpread: float
    laneChangeCooldown: float
    laneChangeCooldownSpread: float
    laneDriftAmp: float
    laneDriftAmpSpread: float
    laneDriftScale: float
    laneDriftScaleSpread: float
    laneOffset: float
    laneOffsetSpread: float
    laneStartOffset: _pd_unified_generator_pb2.CenterSpreadConfig
    largeVehicleTurnRadiusMultiple: float
    lightFlashingPeriod: _pd_unified_generator_pb2.CenterSpreadConfig
    lightIlluminatedPercentage: _pd_unified_generator_pb2.CenterSpreadConfig
    markerDataMap: _containers.MessageMap[str, _pd_unified_generator_pb2.RoadMarkingData]
    minNumberOfAnimals: int
    minNumberOfPedestrians: int
    numberOfAnimals: int
    numberOfPedestrians: int
    objectDecorations: _containers.RepeatedCompositeFieldContainer[_pd_unified_generator_pb2.ObjectDecorations]
    parkedVehicleSpawnProbability: float
    parkedVehicleSpawnProbabilitySpread: float
    parkedVehicleSpawnRadius: float
    parkingTypeDistribution: _pd_unified_generator_pb2.ParkingTypeDistribution
    parking_space_data: _pd_unified_generator_pb2.ParkingSpaceData
    pedestrianColorOverrideChance: float
    pedestrianColorOverrideChanceSpread: float
    pedestrianColorOverrideRGB: _containers.RepeatedScalarFieldContainer[float]
    pedestrianIdleProbability: float
    pedestrianIdleProbabilitySpread: float
    pedestrianJaywalkAngle: float
    pedestrianJaywalkLookAhead: float
    pedestrianJaywalkRadius: float
    pedestrianSpawnMinEdgeDistance: float
    pedestrianSpawnRadius: float
    pedestrianSpawnTightness: float
    pedestrianVelocity: float
    pedestrianVelocitySpread: float
    pedestriansDynamicPathing: bool
    pedestriansSpawnInParkingLot: bool
    position_generator: PositionGenerator
    proceedOutOfTurnProbability: float
    random_generator: RandomScenarioGenerator
    randomizeVehicleParts: bool
    region: str
    restrictLargeVehicleLaneCurvature: bool
    rollingStop: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig
    searchRadius: float
    signDensity: _pd_unified_generator_pb2.CenterSpreadConfig
    spawnPedestriansOnRoad: bool
    spawnTrailerOnEgoProbability: float
    spawnTrailerProbabilities: _containers.ScalarMap[str, float]
    startSeparation: float
    startSeparationSpread: float
    startSeparationTime: _containers.MessageMap[str, _pd_unified_generator_pb2.CenterSpreadConfig]
    startVelocity: float
    startVelocitySpread: float
    stopLineOffset: _pd_unified_generator_pb2.CenterSpreadProbabilityConfig
    targetSeparation: float
    targetSeparationSpread: float
    targetSeparationTime: _containers.MessageMap[str, _pd_unified_generator_pb2.CenterSpreadConfig]
    targetVelocity: float
    targetVelocitySpread: float
    turnTypeDistribution: _pd_distributions_pb2.EnumDistribution
    useStaticTrailers: bool
    vehicleDensityModifier: float
    vehicleDistribution: _containers.MessageMap[str, _pd_distributions_pb2.VehicleCategoryWeight]
    vehicleRoadTypes: _containers.RepeatedScalarFieldContainer[SpawnConfigPreset.RoadType]
    voi_generator: VehicleOfInterestGenerator
    def __init__(self, random_generator: Optional[Union[RandomScenarioGenerator, Mapping]] = ..., junction_generator: Optional[Union[JunctionScenarioGenerator, Mapping]] = ..., voi_generator: Optional[Union[VehicleOfInterestGenerator, Mapping]] = ..., kitti_generator: Optional[Union[KittiScenarioGenerator, Mapping]] = ..., position_generator: Optional[Union[PositionGenerator, Mapping]] = ..., searchRadius: Optional[float] = ..., startVelocity: Optional[float] = ..., startVelocitySpread: Optional[float] = ..., startSeparation: Optional[float] = ..., startSeparationSpread: Optional[float] = ..., targetVelocity: Optional[float] = ..., targetVelocitySpread: Optional[float] = ..., targetSeparation: Optional[float] = ..., targetSeparationSpread: Optional[float] = ..., vehicleDensityModifier: Optional[float] = ..., aggression: Optional[float] = ..., aggressionSpread: Optional[float] = ..., laneOffset: Optional[float] = ..., laneOffsetSpread: Optional[float] = ..., laneDriftAmp: Optional[float] = ..., laneDriftAmpSpread: Optional[float] = ..., laneDriftScale: Optional[float] = ..., laneDriftScaleSpread: Optional[float] = ..., pedestrianSpawnRadius: Optional[float] = ..., pedestrianVelocity: Optional[float] = ..., pedestrianVelocitySpread: Optional[float] = ..., numberOfPedestrians: Optional[int] = ..., numberOfAnimals: Optional[int] = ..., enableCrosswalkPlacement: bool = ..., enableDynamicLaneSelection: bool = ..., enableJunctionPlacement: bool = ..., egoRoadTypes: Optional[Iterable[Union[SpawnConfigPreset.RoadType, str]]] = ..., vehicleRoadTypes: Optional[Iterable[Union[SpawnConfigPreset.RoadType, str]]] = ..., bicyclesOnlyInBikeLanes: bool = ..., egoLaneChangeChance: Optional[float] = ..., egoLaneChangeChanceSpread: Optional[float] = ..., egoLaneChangeCooldown: Optional[float] = ..., egoLaneChangeCooldownSpread: Optional[float] = ..., egoPedestrians: bool = ..., spawnPedestriansOnRoad: bool = ..., pedestrianIdleProbability: Optional[float] = ..., pedestrianIdleProbabilitySpread: Optional[float] = ..., egoPedestrianExclusionRadius: Optional[float] = ..., egoPedestrianExclusionRadiusSpread: Optional[float] = ..., disableAccessories: bool = ..., disableOccupants: bool = ..., alignEgoPedestrianToLane: bool = ..., emergencyLightsOnProbability: Optional[float] = ..., emergencyLightsOnProbabilitySpread: Optional[float] = ..., parkingTypeDistribution: Optional[Union[_pd_unified_generator_pb2.ParkingTypeDistribution, Mapping]] = ..., parkedVehicleSpawnProbability: Optional[float] = ..., parkedVehicleSpawnProbabilitySpread: Optional[float] = ..., parkedVehicleSpawnRadius: Optional[float] = ..., egoMinDistToEdge: Optional[float] = ..., egoMinDistToEdgeSpread: Optional[float] = ..., egoMinPathLength: Optional[float] = ..., egoMinPathLengthSpread: Optional[float] = ..., egoForceMinLengthBehind: bool = ..., laneChangeChance: Optional[float] = ..., laneChangeChanceSpread: Optional[float] = ..., laneChangeCooldown: Optional[float] = ..., laneChangeCooldownSpread: Optional[float] = ..., egoVehicleModel: Optional[str] = ..., pedestrianColorOverrideChance: Optional[float] = ..., pedestrianColorOverrideChanceSpread: Optional[float] = ..., pedestrianColorOverrideRGB: Optional[Iterable[float]] = ..., vehicleDistribution: Optional[Mapping[str, _pd_distributions_pb2.VehicleCategoryWeight]] = ..., rollingStop: Optional[Union[_pd_unified_generator_pb2.CenterSpreadProbabilityConfig, Mapping]] = ..., stopLineOffset: Optional[Union[_pd_unified_generator_pb2.CenterSpreadProbabilityConfig, Mapping]] = ..., proceedOutOfTurnProbability: Optional[float] = ..., agentStateProbabilities: Optional[Iterable[Union[AgentStateProbabilityConfig, Mapping]]] = ..., pedestrianJaywalkLookAhead: Optional[float] = ..., pedestrianJaywalkRadius: Optional[float] = ..., pedestrianJaywalkAngle: Optional[float] = ..., pedestrianSpawnTightness: Optional[float] = ..., pedestrianSpawnMinEdgeDistance: Optional[float] = ..., enableDrivewayPlacement: bool = ..., turnTypeDistribution: Optional[Union[_pd_distributions_pb2.EnumDistribution, Mapping]] = ..., startSeparationTime: Optional[Mapping[str, _pd_unified_generator_pb2.CenterSpreadConfig]] = ..., targetSeparationTime: Optional[Mapping[str, _pd_unified_generator_pb2.CenterSpreadConfig]] = ..., egoMinLaneCountDist: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfigInt, Mapping]] = ..., laneStartOffset: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., applyRollingStopToEgo: bool = ..., applyStopLineOffsetToEgo: bool = ..., applyProceedOutOfTurnProbabilityToEgo: bool = ..., signDensity: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., crosswalkSignDensity: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., egoIgnoreObstacleTypes: Optional[Iterable[str]] = ..., markerDataMap: Optional[Mapping[str, _pd_unified_generator_pb2.RoadMarkingData]] = ..., randomizeVehicleParts: bool = ..., instanceParallelParkingSpaces: bool = ..., instanceParallelParkingMarkers: bool = ..., region: Optional[str] = ..., spawnTrailerProbabilities: Optional[Mapping[str, float]] = ..., spawnTrailerOnEgoProbability: Optional[float] = ..., minNumberOfPedestrians: Optional[int] = ..., pedestriansSpawnInParkingLot: bool = ..., lightFlashingPeriod: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., lightIlluminatedPercentage: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., pedestriansDynamicPathing: bool = ..., useStaticTrailers: bool = ..., minNumberOfAnimals: Optional[int] = ..., animalSpeciesAllowed: Optional[str] = ..., restrictLargeVehicleLaneCurvature: bool = ..., largeVehicleTurnRadiusMultiple: Optional[float] = ..., parking_space_data: Optional[Union[_pd_unified_generator_pb2.ParkingSpaceData, Mapping]] = ..., objectDecorations: Optional[Iterable[Union[_pd_unified_generator_pb2.ObjectDecorations, Mapping]]] = ...) -> None: ...

class StaticCamScenarioGeneratorInfo(_message.Message):
    __slots__ = ["distance_from_junction", "distance_from_junction_spread", "elevation", "elevation_spread"]
    DISTANCE_FROM_JUNCTION_FIELD_NUMBER: ClassVar[int]
    DISTANCE_FROM_JUNCTION_SPREAD_FIELD_NUMBER: ClassVar[int]
    ELEVATION_FIELD_NUMBER: ClassVar[int]
    ELEVATION_SPREAD_FIELD_NUMBER: ClassVar[int]
    distance_from_junction: float
    distance_from_junction_spread: float
    elevation: float
    elevation_spread: float
    def __init__(self, distance_from_junction: Optional[float] = ..., distance_from_junction_spread: Optional[float] = ..., elevation: Optional[float] = ..., elevation_spread: Optional[float] = ...) -> None: ...

class VehicleOfInterestGenerator(_message.Message):
    __slots__ = ["include_opposite_lanes", "max_distance_back", "max_distance_front", "max_number_of_vehicles", "min_number_of_vehicles", "vehicle_list"]
    INCLUDE_OPPOSITE_LANES_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_BACK_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_FRONT_FIELD_NUMBER: ClassVar[int]
    MAX_NUMBER_OF_VEHICLES_FIELD_NUMBER: ClassVar[int]
    MIN_NUMBER_OF_VEHICLES_FIELD_NUMBER: ClassVar[int]
    VEHICLE_LIST_FIELD_NUMBER: ClassVar[int]
    include_opposite_lanes: bool
    max_distance_back: float
    max_distance_front: float
    max_number_of_vehicles: int
    min_number_of_vehicles: int
    vehicle_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vehicle_list: Optional[Iterable[str]] = ..., max_distance_front: Optional[float] = ..., max_distance_back: Optional[float] = ..., min_number_of_vehicles: Optional[int] = ..., max_number_of_vehicles: Optional[int] = ..., include_opposite_lanes: bool = ...) -> None: ...

class VehicleOfInterestScenarioGeneratorInfo(_message.Message):
    __slots__ = ["include_opposite_lanes", "max_distance_back", "max_distance_front", "max_number_of_vehicles", "min_number_of_vehicles", "vehicle_list"]
    INCLUDE_OPPOSITE_LANES_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_BACK_FIELD_NUMBER: ClassVar[int]
    MAX_DISTANCE_FRONT_FIELD_NUMBER: ClassVar[int]
    MAX_NUMBER_OF_VEHICLES_FIELD_NUMBER: ClassVar[int]
    MIN_NUMBER_OF_VEHICLES_FIELD_NUMBER: ClassVar[int]
    VEHICLE_LIST_FIELD_NUMBER: ClassVar[int]
    include_opposite_lanes: bool
    max_distance_back: float
    max_distance_front: float
    max_number_of_vehicles: int
    min_number_of_vehicles: int
    vehicle_list: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, vehicle_list: Optional[Iterable[str]] = ..., max_distance_front: Optional[float] = ..., max_distance_back: Optional[float] = ..., min_number_of_vehicles: Optional[int] = ..., max_number_of_vehicles: Optional[int] = ..., include_opposite_lanes: bool = ...) -> None: ...

class VehiclePositionScenarioGeneratorInfo(_message.Message):
    __slots__ = ["ego_behind_star", "ego_in_star_adjacent_lane", "emergency_vehicle_asset_tag", "emergency_vehicle_country_tag", "emergency_vehicle_distance_behind_star", "emergency_vehicle_spawn_behind_star_probability", "face_same_direction", "junction_ids", "max_attempts_to_place_each_ped", "max_attempts_to_place_each_star", "max_emergency_vehicles_per_star", "max_lane_recursions_to_check_ego_adjacency", "max_peds_no_stars", "max_peds_per_star", "min_emergency_vehicles_per_star", "min_peds_no_stars", "min_peds_per_star", "num_stars_in_scene_max", "num_stars_in_scene_min", "ped_pose_distribution", "peds_around_star_vehicle", "place_on_shoulder", "radius_to_star_max", "radius_to_star_min", "reduce_spawn_to_zero_at_star_range", "scenario_fov_cull_limit", "scenario_los_cull", "shoulder_peds_max_distance_from_ref", "star_on_same_road", "star_vehicle_peds_max_distance", "star_vehicle_peds_max_distance_from_driveable_lane", "star_vehicle_peds_min_distance", "star_vehicle_peds_place_between_ego_and_star", "star_vehicle_peds_social_distancing", "star_vehicles"]
    EGO_BEHIND_STAR_FIELD_NUMBER: ClassVar[int]
    EGO_IN_STAR_ADJACENT_LANE_FIELD_NUMBER: ClassVar[int]
    EMERGENCY_VEHICLE_ASSET_TAG_FIELD_NUMBER: ClassVar[int]
    EMERGENCY_VEHICLE_COUNTRY_TAG_FIELD_NUMBER: ClassVar[int]
    EMERGENCY_VEHICLE_DISTANCE_BEHIND_STAR_FIELD_NUMBER: ClassVar[int]
    EMERGENCY_VEHICLE_SPAWN_BEHIND_STAR_PROBABILITY_FIELD_NUMBER: ClassVar[int]
    FACE_SAME_DIRECTION_FIELD_NUMBER: ClassVar[int]
    JUNCTION_IDS_FIELD_NUMBER: ClassVar[int]
    MAX_ATTEMPTS_TO_PLACE_EACH_PED_FIELD_NUMBER: ClassVar[int]
    MAX_ATTEMPTS_TO_PLACE_EACH_STAR_FIELD_NUMBER: ClassVar[int]
    MAX_EMERGENCY_VEHICLES_PER_STAR_FIELD_NUMBER: ClassVar[int]
    MAX_LANE_RECURSIONS_TO_CHECK_EGO_ADJACENCY_FIELD_NUMBER: ClassVar[int]
    MAX_PEDS_NO_STARS_FIELD_NUMBER: ClassVar[int]
    MAX_PEDS_PER_STAR_FIELD_NUMBER: ClassVar[int]
    MIN_EMERGENCY_VEHICLES_PER_STAR_FIELD_NUMBER: ClassVar[int]
    MIN_PEDS_NO_STARS_FIELD_NUMBER: ClassVar[int]
    MIN_PEDS_PER_STAR_FIELD_NUMBER: ClassVar[int]
    NUM_STARS_IN_SCENE_MAX_FIELD_NUMBER: ClassVar[int]
    NUM_STARS_IN_SCENE_MIN_FIELD_NUMBER: ClassVar[int]
    PEDS_AROUND_STAR_VEHICLE_FIELD_NUMBER: ClassVar[int]
    PED_POSE_DISTRIBUTION_FIELD_NUMBER: ClassVar[int]
    PLACE_ON_SHOULDER_FIELD_NUMBER: ClassVar[int]
    RADIUS_TO_STAR_MAX_FIELD_NUMBER: ClassVar[int]
    RADIUS_TO_STAR_MIN_FIELD_NUMBER: ClassVar[int]
    REDUCE_SPAWN_TO_ZERO_AT_STAR_RANGE_FIELD_NUMBER: ClassVar[int]
    SCENARIO_FOV_CULL_LIMIT_FIELD_NUMBER: ClassVar[int]
    SCENARIO_LOS_CULL_FIELD_NUMBER: ClassVar[int]
    SHOULDER_PEDS_MAX_DISTANCE_FROM_REF_FIELD_NUMBER: ClassVar[int]
    STAR_ON_SAME_ROAD_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLES_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLE_PEDS_MAX_DISTANCE_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLE_PEDS_MAX_DISTANCE_FROM_DRIVEABLE_LANE_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLE_PEDS_MIN_DISTANCE_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLE_PEDS_PLACE_BETWEEN_EGO_AND_STAR_FIELD_NUMBER: ClassVar[int]
    STAR_VEHICLE_PEDS_SOCIAL_DISTANCING_FIELD_NUMBER: ClassVar[int]
    ego_behind_star: bool
    ego_in_star_adjacent_lane: bool
    emergency_vehicle_asset_tag: str
    emergency_vehicle_country_tag: str
    emergency_vehicle_distance_behind_star: float
    emergency_vehicle_spawn_behind_star_probability: _pd_unified_generator_pb2.CenterSpreadConfig
    face_same_direction: bool
    junction_ids: _containers.RepeatedScalarFieldContainer[int]
    max_attempts_to_place_each_ped: int
    max_attempts_to_place_each_star: int
    max_emergency_vehicles_per_star: int
    max_lane_recursions_to_check_ego_adjacency: int
    max_peds_no_stars: int
    max_peds_per_star: int
    min_emergency_vehicles_per_star: int
    min_peds_no_stars: int
    min_peds_per_star: int
    num_stars_in_scene_max: int
    num_stars_in_scene_min: int
    ped_pose_distribution: _pd_distributions_pb2.CategoricalDistribution
    peds_around_star_vehicle: bool
    place_on_shoulder: bool
    radius_to_star_max: float
    radius_to_star_min: float
    reduce_spawn_to_zero_at_star_range: float
    scenario_fov_cull_limit: float
    scenario_los_cull: bool
    shoulder_peds_max_distance_from_ref: float
    star_on_same_road: bool
    star_vehicle_peds_max_distance: float
    star_vehicle_peds_max_distance_from_driveable_lane: float
    star_vehicle_peds_min_distance: float
    star_vehicle_peds_place_between_ego_and_star: bool
    star_vehicle_peds_social_distancing: float
    star_vehicles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, radius_to_star_min: Optional[float] = ..., radius_to_star_max: Optional[float] = ..., star_vehicles: Optional[Iterable[str]] = ..., junction_ids: Optional[Iterable[int]] = ..., face_same_direction: bool = ..., ego_behind_star: bool = ..., place_on_shoulder: bool = ..., peds_around_star_vehicle: bool = ..., num_stars_in_scene_min: Optional[int] = ..., num_stars_in_scene_max: Optional[int] = ..., star_on_same_road: bool = ..., ego_in_star_adjacent_lane: bool = ..., star_vehicle_peds_min_distance: Optional[float] = ..., star_vehicle_peds_max_distance: Optional[float] = ..., star_vehicle_peds_social_distancing: Optional[float] = ..., star_vehicle_peds_place_between_ego_and_star: bool = ..., star_vehicle_peds_max_distance_from_driveable_lane: Optional[float] = ..., shoulder_peds_max_distance_from_ref: Optional[float] = ..., min_peds_per_star: Optional[int] = ..., max_peds_per_star: Optional[int] = ..., min_peds_no_stars: Optional[int] = ..., max_peds_no_stars: Optional[int] = ..., max_attempts_to_place_each_ped: Optional[int] = ..., max_attempts_to_place_each_star: Optional[int] = ..., max_lane_recursions_to_check_ego_adjacency: Optional[int] = ..., scenario_fov_cull_limit: Optional[float] = ..., scenario_los_cull: bool = ..., reduce_spawn_to_zero_at_star_range: Optional[float] = ..., ped_pose_distribution: Optional[Union[_pd_distributions_pb2.CategoricalDistribution, Mapping]] = ..., emergency_vehicle_spawn_behind_star_probability: Optional[Union[_pd_unified_generator_pb2.CenterSpreadConfig, Mapping]] = ..., emergency_vehicle_distance_behind_star: Optional[float] = ..., min_emergency_vehicles_per_star: Optional[int] = ..., max_emergency_vehicles_per_star: Optional[int] = ..., emergency_vehicle_asset_tag: Optional[str] = ..., emergency_vehicle_country_tag: Optional[str] = ...) -> None: ...

class VehicleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
