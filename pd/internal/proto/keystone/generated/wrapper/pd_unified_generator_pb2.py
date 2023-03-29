from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_unified_generator_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_unified_generator_pb2.AbsolutePositionRequest)
class AbsolutePositionRequest(ProtoMessageClass):
    """
    Description: Uses specific coordinates for initial pose

    Args:
        position:
              Description:
                  XYZ Position to spawn at.
              Range:
                  Position existing on map
              Required:
                  Yes
        rotation:
              Description:
                  3x3 Rotation matrix for spawning agent.
              Required:
                  No, if not specified will determine the rotation based on the lane and position
        lane_id:
              Description:
                  Lane ID to spawn in (UMD)
              Range:
                  Lane id of lane specified by position
              Required:
                  No, if agent is a vehicle. The lane id will be retrieved from the vehicle's position. Yes, if agent is not a vehicle.
"""
    _proto_message = pd_unified_generator_pb2.AbsolutePositionRequest

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.AbsolutePositionRequest]=None, lane_id: Optional[int]=None, position: Optional[_pd_types_pb2.Float3]=None, rotation: Optional[_pd_types_pb2.Float3x3]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.AbsolutePositionRequest()
        self.proto = proto
        self._position = get_wrapper(proto_type=proto.position.__class__)(proto=proto.position)
        self._rotation = get_wrapper(proto_type=proto.rotation.__class__)(proto=proto.rotation)
        if lane_id is not None:
            self.lane_id = lane_id
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation

    @property
    def lane_id(self) -> int:
        return self.proto.lane_id

    @lane_id.setter
    def lane_id(self, value: int):
        self.proto.lane_id = value

    @property
    def position(self) -> _pd_types_pb2.Float3:
        return self._position

    @position.setter
    def position(self, value: _pd_types_pb2.Float3):
        self._position.proto.CopyFrom(value.proto)

    @property
    def rotation(self) -> _pd_types_pb2.Float3x3:
        return self._rotation

    @rotation.setter
    def rotation(self, value: _pd_types_pb2.Float3x3):
        self._rotation.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.AgentSpawnData)
class AgentSpawnData(ProtoMessageClass):
    """
    Contains spawn data that applies across agent types

    Args:
        tags:
              Tags we want to apply to this agent
"""
    _proto_message = pd_unified_generator_pb2.AgentSpawnData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.AgentSpawnData]=None, tags: Optional[List[SpecialAgentTag]]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.AgentSpawnData()
        self.proto = proto
        self._tags = ProtoListWrapper(container=[int(v) for v in proto.tags], attr_name='tags', list_owner=proto)
        if tags is not None:
            self.tags = tags

    @property
    def tags(self) -> int:
        return self._tags

    @tags.setter
    def tags(self, value: int):
        self._tags.clear()
        for v in value:
            self._tags.append(v)

@register_wrapper(proto_type=pd_unified_generator_pb2.AtomicGeneratorParameters)
class AtomicGeneratorParameters(ProtoMessageClass):
    """
    Description: Parent type for each atomic.

    Args:
"""
    _proto_message = pd_unified_generator_pb2.AtomicGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.AtomicGeneratorParameters]=None, debris: Optional[DebrisGeneratorParameters]=None, drone: Optional[DroneGeneratorParameters]=None, ego_agent: Optional[EgoAgentGeneratorParameters]=None, parked_vehicles: Optional[ParkedVehicleGeneratorParameters]=None, pedestrian: Optional[PedestrianGeneratorParameters]=None, random_pedestrian: Optional[RandomPedestrianGeneratorParameters]=None, static_agent: Optional[StaticAgentGeneratorParameters]=None, traffic: Optional[TrafficGeneratorParameters]=None, vehicle: Optional[VehicleGeneratorParameters]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.AtomicGeneratorParameters()
        self.proto = proto
        self._debris = get_wrapper(proto_type=proto.debris.__class__)(proto=proto.debris)
        self._drone = get_wrapper(proto_type=proto.drone.__class__)(proto=proto.drone)
        self._ego_agent = get_wrapper(proto_type=proto.ego_agent.__class__)(proto=proto.ego_agent)
        self._parked_vehicles = get_wrapper(proto_type=proto.parked_vehicles.__class__)(proto=proto.parked_vehicles)
        self._pedestrian = get_wrapper(proto_type=proto.pedestrian.__class__)(proto=proto.pedestrian)
        self._random_pedestrian = get_wrapper(proto_type=proto.random_pedestrian.__class__)(proto=proto.random_pedestrian)
        self._static_agent = get_wrapper(proto_type=proto.static_agent.__class__)(proto=proto.static_agent)
        self._traffic = get_wrapper(proto_type=proto.traffic.__class__)(proto=proto.traffic)
        self._vehicle = get_wrapper(proto_type=proto.vehicle.__class__)(proto=proto.vehicle)
        if debris is not None:
            self.debris = debris
        if drone is not None:
            self.drone = drone
        if ego_agent is not None:
            self.ego_agent = ego_agent
        if parked_vehicles is not None:
            self.parked_vehicles = parked_vehicles
        if pedestrian is not None:
            self.pedestrian = pedestrian
        if random_pedestrian is not None:
            self.random_pedestrian = random_pedestrian
        if static_agent is not None:
            self.static_agent = static_agent
        if traffic is not None:
            self.traffic = traffic
        if vehicle is not None:
            self.vehicle = vehicle

    @property
    def debris(self) -> DebrisGeneratorParameters:
        return self._debris

    @debris.setter
    def debris(self, value: DebrisGeneratorParameters):
        self._debris.proto.CopyFrom(value.proto)

    @property
    def drone(self) -> DroneGeneratorParameters:
        return self._drone

    @drone.setter
    def drone(self, value: DroneGeneratorParameters):
        self._drone.proto.CopyFrom(value.proto)

    @property
    def ego_agent(self) -> EgoAgentGeneratorParameters:
        return self._ego_agent

    @ego_agent.setter
    def ego_agent(self, value: EgoAgentGeneratorParameters):
        self._ego_agent.proto.CopyFrom(value.proto)

    @property
    def parked_vehicles(self) -> ParkedVehicleGeneratorParameters:
        return self._parked_vehicles

    @parked_vehicles.setter
    def parked_vehicles(self, value: ParkedVehicleGeneratorParameters):
        self._parked_vehicles.proto.CopyFrom(value.proto)

    @property
    def pedestrian(self) -> PedestrianGeneratorParameters:
        return self._pedestrian

    @pedestrian.setter
    def pedestrian(self, value: PedestrianGeneratorParameters):
        self._pedestrian.proto.CopyFrom(value.proto)

    @property
    def random_pedestrian(self) -> RandomPedestrianGeneratorParameters:
        return self._random_pedestrian

    @random_pedestrian.setter
    def random_pedestrian(self, value: RandomPedestrianGeneratorParameters):
        self._random_pedestrian.proto.CopyFrom(value.proto)

    @property
    def static_agent(self) -> StaticAgentGeneratorParameters:
        return self._static_agent

    @static_agent.setter
    def static_agent(self, value: StaticAgentGeneratorParameters):
        self._static_agent.proto.CopyFrom(value.proto)

    @property
    def traffic(self) -> TrafficGeneratorParameters:
        return self._traffic

    @traffic.setter
    def traffic(self, value: TrafficGeneratorParameters):
        self._traffic.proto.CopyFrom(value.proto)

    @property
    def vehicle(self) -> VehicleGeneratorParameters:
        return self._vehicle

    @vehicle.setter
    def vehicle(self, value: VehicleGeneratorParameters):
        self._vehicle.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadConfig)
class CenterSpreadConfig(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.CenterSpreadConfig

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.CenterSpreadConfig]=None, center: Optional[float]=None, spread: Optional[float]=None):
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

@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadConfigInt)
class CenterSpreadConfigInt(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.CenterSpreadConfigInt

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.CenterSpreadConfigInt]=None, center: Optional[int]=None, spread: Optional[int]=None):
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

@register_wrapper(proto_type=pd_unified_generator_pb2.CenterSpreadProbabilityConfig)
class CenterSpreadProbabilityConfig(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.CenterSpreadProbabilityConfig

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.CenterSpreadProbabilityConfig]=None, center: Optional[float]=None, probability: Optional[float]=None, spread: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.CenterSpreadProbabilityConfig()
        self.proto = proto
        if center is not None:
            self.center = center
        if probability is not None:
            self.probability = probability
        if spread is not None:
            self.spread = spread

    @property
    def center(self) -> float:
        return self.proto.center

    @center.setter
    def center(self, value: float):
        self.proto.center = value

    @property
    def probability(self) -> float:
        return self.proto.probability

    @probability.setter
    def probability(self, value: float):
        self.proto.probability = value

    @property
    def spread(self) -> float:
        return self.proto.spread

    @spread.setter
    def spread(self, value: float):
        self.proto.spread = value

@register_wrapper(proto_type=pd_unified_generator_pb2.DebrisGeneratorParameters)
class DebrisGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places debris into the world. Requires ego atomic.

    Args:
        spawn_probability:
              Description:
                  For every possible spawn location, use the probability to determine if object actually spawns. (i.e controls density)
              Range:
                  `0.0` to `1.0`, where `1.0` is the most dense
              Required:
                  No, will use default value if not specified
        debris_center_bias:
              Description:
                  Determines where in the lane we want to spawn on
              Range:
                  `-1.0` to `1.0`, where `1.0` is spawning toward center of lane, `-1.0` is spawning towards edges of lane, `0.0` is evenly spaced.
              Required:
                  No, uses `0.0` if not specified
        min_debris_distance:
              Description:
                  Minimum spawning distance from ego
              Range:
                  Greater than or equal to `0.0`
              Required:
                  No, uses `0.0` if not specified
        max_debris_distance:
              Description:
                  Maximum spawning distance
              Range:
                  Must be greater than `min_debris_distance`
              Required:
                  No, uses default value if not specified
        debris_asset_tag:
              Description:
                  Comma separated list of asset names from asset registry to spawn with this generator.
                  Example: "trash_bottle_tall_01,trash_box_amazon_01"
                  Each asset has an equal chance of being spawned.
              Required:
                  No, uses default value if not specified
        debris_asset_remove_tag:
              Description:
                  Removes any assets present in `debris_asset_tag`
              Required:
                  No
        position_request:
              Description:
                  Determines the spawn radius of debris (see `LocationRelativePositionRequest`)
              Range:
                  Only works with `LocationRelativePositionRequest`
              Required:
                  Yes
        asset_distribution:
              Description:
                  Specifies the likelihood of each asset when spawning. Asset names must exist in asset registry.
                  If specified, `debris_asset_tag` and `debris_asset_remove_tag` are ignored
              Required:
                  No, if not specified we use the list generated from `debris_asset_tag`
"""
    _proto_message = pd_unified_generator_pb2.DebrisGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.DebrisGeneratorParameters]=None, asset_distribution: Optional[Dict[str, float]]=None, debris_asset_remove_tag: Optional[str]=None, debris_asset_tag: Optional[str]=None, debris_center_bias: Optional[float]=None, max_debris_distance: Optional[float]=None, min_debris_distance: Optional[float]=None, position_request: Optional[PositionRequest]=None, spawn_probability: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.DebrisGeneratorParameters()
        self.proto = proto
        self._asset_distribution = ProtoDictWrapper(container={k: float(v) for (k, v) in proto.asset_distribution.items()}, attr_name='asset_distribution', dict_owner=proto)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        if asset_distribution is not None:
            self.asset_distribution = asset_distribution
        if debris_asset_remove_tag is not None:
            self.debris_asset_remove_tag = debris_asset_remove_tag
        if debris_asset_tag is not None:
            self.debris_asset_tag = debris_asset_tag
        if debris_center_bias is not None:
            self.debris_center_bias = debris_center_bias
        if max_debris_distance is not None:
            self.max_debris_distance = max_debris_distance
        if min_debris_distance is not None:
            self.min_debris_distance = min_debris_distance
        if position_request is not None:
            self.position_request = position_request
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability

    @property
    def asset_distribution(self) -> Dict[str, float]:
        return self._asset_distribution

    @asset_distribution.setter
    def asset_distribution(self, value: Dict[str, float]):
        self._asset_distribution.clear()
        self._asset_distribution.update(value)

    @property
    def debris_asset_remove_tag(self) -> str:
        return self.proto.debris_asset_remove_tag

    @debris_asset_remove_tag.setter
    def debris_asset_remove_tag(self, value: str):
        self.proto.debris_asset_remove_tag = value

    @property
    def debris_asset_tag(self) -> str:
        return self.proto.debris_asset_tag

    @debris_asset_tag.setter
    def debris_asset_tag(self, value: str):
        self.proto.debris_asset_tag = value

    @property
    def debris_center_bias(self) -> float:
        return self.proto.debris_center_bias

    @debris_center_bias.setter
    def debris_center_bias(self, value: float):
        self.proto.debris_center_bias = value

    @property
    def max_debris_distance(self) -> float:
        return self.proto.max_debris_distance

    @max_debris_distance.setter
    def max_debris_distance(self, value: float):
        self.proto.max_debris_distance = value

    @property
    def min_debris_distance(self) -> float:
        return self.proto.min_debris_distance

    @min_debris_distance.setter
    def min_debris_distance(self, value: float):
        self.proto.min_debris_distance = value

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def spawn_probability(self) -> float:
        return self.proto.spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: float):
        self.proto.spawn_probability = value

@register_wrapper(proto_type=pd_unified_generator_pb2.DefaultAtomicGeneratorParameters)
class DefaultAtomicGeneratorParameters(ProtoMessageClass):
    """
    Description: Contains parameters applied to all atomics within UnifiedGeneratorParameters

    Args:
        vehicle_distribution:
              Description:
                  Default vehicle distribution. If the vehicle distribution is not set for an atomic, it will fall back to this distribution.
              Required:
                  No. If not specified, will fall back to atomic-specific default
"""
    _proto_message = pd_unified_generator_pb2.DefaultAtomicGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.DefaultAtomicGeneratorParameters]=None, vehicle_distribution: Optional[Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.DefaultAtomicGeneratorParameters()
        self.proto = proto
        self._vehicle_distribution = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()}, attr_name='vehicle_distribution', dict_owner=proto)
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

@register_wrapper(proto_type=pd_unified_generator_pb2.DroneGeneratorParameters)
class DroneGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Not implemented

    Args:
        position_request:
              Description:
                  Determines where the drone will spawn. Note: Will use position request result as the ground end of the flight path
              Required:
                  Yes
        drone_spawn_data:
              Description:
                  This contains parameters that control drone/drone related behavior
              Required:
                  No, will use defaults specified in `DroneSpawnData`
"""
    _proto_message = pd_unified_generator_pb2.DroneGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.DroneGeneratorParameters]=None, drone_spawn_data: Optional[DroneSpawnData]=None, position_request: Optional[PositionRequest]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.DroneGeneratorParameters()
        self.proto = proto
        self._drone_spawn_data = get_wrapper(proto_type=proto.drone_spawn_data.__class__)(proto=proto.drone_spawn_data)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        if drone_spawn_data is not None:
            self.drone_spawn_data = drone_spawn_data
        if position_request is not None:
            self.position_request = position_request

    @property
    def drone_spawn_data(self) -> DroneSpawnData:
        return self._drone_spawn_data

    @drone_spawn_data.setter
    def drone_spawn_data(self, value: DroneSpawnData):
        self._drone_spawn_data.proto.CopyFrom(value.proto)

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.DroneSpawnData)
class DroneSpawnData(ProtoMessageClass):
    """
    Description: This contains parameters that control drone/drone related behavior

    Args:
        ascend_probability:
              Ascend or descend
        ground_asset_probability:
              Probability of having a ground asset at flight path ground end
        ground_assets:
              List of ground assets to choose from
        flight_path_dir:
              Directory where flight path csv is stored
        agent_spawn_data:
              Common spawn data across agent types
        height_offset:
              How far up to offset flight path bottom from ground/top of asset
        ground_asset_height_offset:
              Height offset for the ground asset itself. used to address z fighting
"""
    _proto_message = pd_unified_generator_pb2.DroneSpawnData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.DroneSpawnData]=None, agent_spawn_data: Optional[AgentSpawnData]=None, ascend_probability: Optional[float]=None, flight_path_dir: Optional[str]=None, ground_asset_height_offset: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, ground_asset_probability: Optional[float]=None, ground_assets: Optional[List[str]]=None, height_offset: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.DroneSpawnData()
        self.proto = proto
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        self._ground_asset_height_offset = get_wrapper(proto_type=proto.ground_asset_height_offset.__class__)(proto=proto.ground_asset_height_offset)
        self._ground_assets = ProtoListWrapper(container=[str(v) for v in proto.ground_assets], attr_name='ground_assets', list_owner=proto)
        self._height_offset = get_wrapper(proto_type=proto.height_offset.__class__)(proto=proto.height_offset)
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data
        if ascend_probability is not None:
            self.ascend_probability = ascend_probability
        if flight_path_dir is not None:
            self.flight_path_dir = flight_path_dir
        if ground_asset_height_offset is not None:
            self.ground_asset_height_offset = ground_asset_height_offset
        if ground_asset_probability is not None:
            self.ground_asset_probability = ground_asset_probability
        if ground_assets is not None:
            self.ground_assets = ground_assets
        if height_offset is not None:
            self.height_offset = height_offset

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self._agent_spawn_data.proto.CopyFrom(value.proto)

    @property
    def ascend_probability(self) -> float:
        return self.proto.ascend_probability

    @ascend_probability.setter
    def ascend_probability(self, value: float):
        self.proto.ascend_probability = value

    @property
    def flight_path_dir(self) -> str:
        return self.proto.flight_path_dir

    @flight_path_dir.setter
    def flight_path_dir(self, value: str):
        self.proto.flight_path_dir = value

    @property
    def ground_asset_height_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._ground_asset_height_offset

    @ground_asset_height_offset.setter
    def ground_asset_height_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._ground_asset_height_offset.proto.CopyFrom(value.proto)

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
    def height_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._height_offset

    @height_offset.setter
    def height_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._height_offset.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.EgoAgentGeneratorParameters)
class EgoAgentGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places an ego sensor in the world. Required for every scenario. Only works with VEHICLE agent_type, other agent types not implemented yet

    Args:
        agent_type:
              Description:
                  Determines what the ego sensor is attached to
              Required:
                  No, will default to `AgentType.VEHICLE`
        ego_model:
              Description:
                  If AgentType is VEHICLE, determines what vehicle type the ego sensor attaches to. Must be a vehicle model from asset registry.
              Required:
                  No, will default to `suv_medium_02`.
        position_request:
              Description:
                  Determines where the ego vehicle will spawn
              Required:
                  Yes
        vehicle_spawn_data:
              Description:
                  Used if `agent_type` is `AgentType.VEHICLE`
              Required:
                  No, will use defaults specified in `VehicleSpawnData`
        pedestrian_spawn_data:
              Description:
                  Used if `agent_type` is `AgentType.PEDESTRIAN`
              Required:
                  No, will use defaults specified in `PedestrianSpawnData`
        drone_spawn_data:
              Description:
                  Used if `agent_type` is `AgentType.DRONE`
              Required:
                  No, will use defaults specified in `DroneSpawnData`
"""
    _proto_message = pd_unified_generator_pb2.EgoAgentGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.EgoAgentGeneratorParameters]=None, agent_type: Optional[AgentType]=None, drone_spawn_data: Optional[DroneSpawnData]=None, ego_model: Optional[str]=None, pedestrian_spawn_data: Optional[PedestrianSpawnData]=None, position_request: Optional[PositionRequest]=None, vehicle_spawn_data: Optional[VehicleSpawnData]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.EgoAgentGeneratorParameters()
        self.proto = proto
        self._drone_spawn_data = get_wrapper(proto_type=proto.drone_spawn_data.__class__)(proto=proto.drone_spawn_data)
        self._pedestrian_spawn_data = get_wrapper(proto_type=proto.pedestrian_spawn_data.__class__)(proto=proto.pedestrian_spawn_data)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(proto=proto.vehicle_spawn_data)
        if agent_type is not None:
            self.agent_type = agent_type
        if drone_spawn_data is not None:
            self.drone_spawn_data = drone_spawn_data
        if ego_model is not None:
            self.ego_model = ego_model
        if pedestrian_spawn_data is not None:
            self.pedestrian_spawn_data = pedestrian_spawn_data
        if position_request is not None:
            self.position_request = position_request
        if vehicle_spawn_data is not None:
            self.vehicle_spawn_data = vehicle_spawn_data

    @property
    def agent_type(self) -> int:
        return self.proto.agent_type

    @agent_type.setter
    def agent_type(self, value: int):
        self.proto.agent_type = value

    @property
    def drone_spawn_data(self) -> DroneSpawnData:
        return self._drone_spawn_data

    @drone_spawn_data.setter
    def drone_spawn_data(self, value: DroneSpawnData):
        self._drone_spawn_data.proto.CopyFrom(value.proto)

    @property
    def ego_model(self) -> str:
        return self.proto.ego_model

    @ego_model.setter
    def ego_model(self, value: str):
        self.proto.ego_model = value

    @property
    def pedestrian_spawn_data(self) -> PedestrianSpawnData:
        return self._pedestrian_spawn_data

    @pedestrian_spawn_data.setter
    def pedestrian_spawn_data(self, value: PedestrianSpawnData):
        self._pedestrian_spawn_data.proto.CopyFrom(value.proto)

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self._vehicle_spawn_data.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.EnvironmentParameters)
class EnvironmentParameters(ProtoMessageClass):
    """
    Description: Contains parameters that modify map

    Args:
        sign_spawn_probability:
              Description:
                  Specifies the spawn probability of spawning in an available spot for signs. (i.e. controls density)
                  Only affects maps that begin with "SIGNAGE_".
              Range:
                  `0.0` to `1.0`
              Required:
                  No, will use default 0 values
        crosswalk_sign_spawn_probability:
              Description:
                  Probability of spawning crosswalk signs in crosswalk signs slots
                  Crosswalk signs are placed in or near crosswalks on the road for extra indication of the crosswalk
                  to vehicles.
                  Only affects maps that begin with "SIGNAGE_".
              Range:
                  `0.0` to `1.0`
              Required:
                  No, will use default 0 values
        marker_data_map:
              Description:
                  Specifies road markings (e.g. parallel/perpendicular parking space lines, parking space texture, etc.)
              Required:
                  No, uses default values for the RoadMarkingData types specified below::

                    "parking_spot_config"     {marker_type = MI_pavement_01, rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
                    "parking_lot_marker"      {marker_type = "DOUBLE_SQUARE", rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
                    "parallel_parking_marker" {rgb = {1.0f, 1.0f, 1.0f}, wear = 0.0f}
        region:
              Description:
                  Specifies what country signs are from.
                  Only affects ISA maps::

                    {
                        "Belgium"
                        "Bulgaria"
                        "Czechia"
                        "Denmark"
                        "Germany"
                        "Estonia"
                        "Ireland"
                        "Greece"
                        "Spain"
                        "France"
                        "Croatia"
                        "Italy"
                        "Cyprus"
                        "Latvia"
                        "Lithuania"
                        "Luxembourg"
                        "Hungary"
                        "Malta"
                        "Netherlands"
                        "Austria"
                        "Poland"
                        "Portugal"
                        "Romania"
                        "Slovenia"
                        "Slovakia"
                        "Finland"
                        "Sweden"
                        "Norway"
                        "Switzerland"
                    }
              Required:
                  No
"""
    _proto_message = pd_unified_generator_pb2.EnvironmentParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.EnvironmentParameters]=None, crosswalk_sign_spawn_probability: Optional[CenterSpreadConfig]=None, marker_data_map: Optional[Dict[str, RoadMarkingData]]=None, region: Optional[_pd_distributions_pb2.EnumDistribution]=None, sign_spawn_probability: Optional[CenterSpreadConfig]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.EnvironmentParameters()
        self.proto = proto
        self._crosswalk_sign_spawn_probability = get_wrapper(proto_type=proto.crosswalk_sign_spawn_probability.__class__)(proto=proto.crosswalk_sign_spawn_probability)
        self._marker_data_map = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.marker_data_map.items()}, attr_name='marker_data_map', dict_owner=proto)
        self._region = get_wrapper(proto_type=proto.region.__class__)(proto=proto.region)
        self._sign_spawn_probability = get_wrapper(proto_type=proto.sign_spawn_probability.__class__)(proto=proto.sign_spawn_probability)
        if crosswalk_sign_spawn_probability is not None:
            self.crosswalk_sign_spawn_probability = crosswalk_sign_spawn_probability
        if marker_data_map is not None:
            self.marker_data_map = marker_data_map
        if region is not None:
            self.region = region
        if sign_spawn_probability is not None:
            self.sign_spawn_probability = sign_spawn_probability

    @property
    def crosswalk_sign_spawn_probability(self) -> CenterSpreadConfig:
        return self._crosswalk_sign_spawn_probability

    @crosswalk_sign_spawn_probability.setter
    def crosswalk_sign_spawn_probability(self, value: CenterSpreadConfig):
        self._crosswalk_sign_spawn_probability.proto.CopyFrom(value.proto)

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
        self._region.proto.CopyFrom(value.proto)

    @property
    def sign_spawn_probability(self) -> CenterSpreadConfig:
        return self._sign_spawn_probability

    @sign_spawn_probability.setter
    def sign_spawn_probability(self, value: CenterSpreadConfig):
        self._sign_spawn_probability.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.FloatArray)
class FloatArray(ProtoMessageClass):
    """
    Description: Used to describe RGB value in RoadMarkingData

    Args:
"""
    _proto_message = pd_unified_generator_pb2.FloatArray

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.FloatArray]=None, data: Optional[List[float]]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.FloatArray()
        self.proto = proto
        self._data = ProtoListWrapper(container=[float(v) for v in proto.data], attr_name='data', list_owner=proto)
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

@register_wrapper(proto_type=pd_unified_generator_pb2.JunctionSpawnPolicy)
class JunctionSpawnPolicy(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.JunctionSpawnPolicy

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.JunctionSpawnPolicy]=None, distance_to_junction: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.JunctionSpawnPolicy()
        self.proto = proto
        self._distance_to_junction = get_wrapper(proto_type=proto.distance_to_junction.__class__)(proto=proto.distance_to_junction)
        if distance_to_junction is not None:
            self.distance_to_junction = distance_to_junction

    @property
    def distance_to_junction(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._distance_to_junction

    @distance_to_junction.setter
    def distance_to_junction(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._distance_to_junction.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.LaneCurvatureSpawnPolicy)
class LaneCurvatureSpawnPolicy(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.LaneCurvatureSpawnPolicy

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.LaneCurvatureSpawnPolicy]=None, curvature_bounds: Optional[MinMaxConfigFloat]=None, min_section_length: Optional[float]=None):
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
        self._curvature_bounds.proto.CopyFrom(value.proto)

    @property
    def min_section_length(self) -> float:
        return self.proto.min_section_length

    @min_section_length.setter
    def min_section_length(self, value: float):
        self.proto.min_section_length = value

@register_wrapper(proto_type=pd_unified_generator_pb2.LaneSpawnPolicy)
class LaneSpawnPolicy(ProtoMessageClass):
    """
    Description: Specifies lanes to spawn at

    Args:
        min_num_lanes_in_same_direction:
              Description:
                  Minimum number of lanes in the same direction as the selected lane
              Range:
                  Greater than to equal to `0.0`
              Required:
                  No, will use default 0 values
        lane_type:
              Description:
                  Specifies lane types to spawn at and their probabilities
              Range:
                  LaneType, which includes::

                    {
                        "Drivable"     (regular driving lanes/roads),
                        "NonDrivable"  (driveways),
                        "Parking"      (parallel parking lanes that run along drivable lanes),
                        "Shoulder"     (highway shoulder lanes),
                        "Biking"       (bike lanes, typically narrower than Drivable),
                        "Crosswalk"    (crosswalk, pedestrian crossings in junction),
                        "ParkingAisle" (aisle lanes in parking lots),
                        "ParkingSpace" (parking lot perpendicular spaces),
                        "Sidewalk"     (sidewalks, not including pedestrian crossings in junctions)
                    }
              Required:
                  No
        min_num_lanes_in_opposite_direction:
              Description:
                  Minimum number of lanes in the opposite direction as the selected lane
              Range:
                  Greater than or equal to `0`
              Required:
                  No, will use default value
        lateral_offset:
              Description:
                  Lateral offset as a percentage of half lane width.
                  Positive means offset to the right. Negative means offset to the left.
              Range:
                  `-1.0` to `1.0`
              Required:
                  No, will default to 0 values
        bicycles_only_in_bike_lanes:
              Description:
                  Specifies if bicycles should only spawn in bike lanes
              Required:
                  No, will use default value
        nearby_asset_policy:
              Description:
                  Option to spawn near map assets
              Required:
                  No
        road_type:
              Description:
                  Specifies road types to spawn at and their probabilities.
                  Recommended guidance:
                  If specifying highway scenes, set this parameter to `{"Motorway": 1.0}`.
                  For other placements, leave empty and use lane_type instead.
              Range:
                  RoadType, which includes::

                    {
                        "Motorway"      (highway roads)
                        "Residential"   (non-highway and non-parking roads)
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
                    }
              Required:
                  No, if not specified will spawn on any valid road type depending on agent type
        min_path_length:
              Description:
                  Specifies a map of desired minimum path lengths based on lane type.
                  The length is from the beginning of the lane.
              Required:
                  No, will default to 0
        min_length_behind:
              Description:
                  Specifies a map of desired minimum path lengths behind the agent based on lane type.
                  The length is the distance behind the agent's location to the world edge.
              Required:
                  No, will default to 0
"""
    _proto_message = pd_unified_generator_pb2.LaneSpawnPolicy

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.LaneSpawnPolicy]=None, bicycles_only_in_bike_lanes: Optional[bool]=None, lane_type: Optional[_pd_distributions_pb2.EnumDistribution]=None, lateral_offset: Optional[CenterSpreadConfig]=None, min_length_behind: Optional[Dict[str, CenterSpreadConfig]]=None, min_num_lanes_in_opposite_direction: Optional[int]=None, min_num_lanes_in_same_direction: Optional[int]=None, min_path_length: Optional[Dict[str, CenterSpreadConfig]]=None, nearby_asset_policy: Optional[NearbyAssetPolicy]=None, position_of_interest_policy: Optional[List[PositionOfInterestPolicy]]=None, road_type: Optional[_pd_distributions_pb2.EnumDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.LaneSpawnPolicy()
        self.proto = proto
        self._lane_type = get_wrapper(proto_type=proto.lane_type.__class__)(proto=proto.lane_type)
        self._lateral_offset = get_wrapper(proto_type=proto.lateral_offset.__class__)(proto=proto.lateral_offset)
        self._min_length_behind = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.min_length_behind.items()}, attr_name='min_length_behind', dict_owner=proto)
        self._min_path_length = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.min_path_length.items()}, attr_name='min_path_length', dict_owner=proto)
        self._nearby_asset_policy = get_wrapper(proto_type=proto.nearby_asset_policy.__class__)(proto=proto.nearby_asset_policy)
        self._position_of_interest_policy = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.position_of_interest_policy], attr_name='position_of_interest_policy', list_owner=proto)
        self._road_type = get_wrapper(proto_type=proto.road_type.__class__)(proto=proto.road_type)
        if bicycles_only_in_bike_lanes is not None:
            self.bicycles_only_in_bike_lanes = bicycles_only_in_bike_lanes
        if lane_type is not None:
            self.lane_type = lane_type
        if lateral_offset is not None:
            self.lateral_offset = lateral_offset
        if min_length_behind is not None:
            self.min_length_behind = min_length_behind
        if min_num_lanes_in_opposite_direction is not None:
            self.min_num_lanes_in_opposite_direction = min_num_lanes_in_opposite_direction
        if min_num_lanes_in_same_direction is not None:
            self.min_num_lanes_in_same_direction = min_num_lanes_in_same_direction
        if min_path_length is not None:
            self.min_path_length = min_path_length
        if nearby_asset_policy is not None:
            self.nearby_asset_policy = nearby_asset_policy
        if position_of_interest_policy is not None:
            self.position_of_interest_policy = position_of_interest_policy
        if road_type is not None:
            self.road_type = road_type

    @property
    def bicycles_only_in_bike_lanes(self) -> bool:
        return self.proto.bicycles_only_in_bike_lanes

    @bicycles_only_in_bike_lanes.setter
    def bicycles_only_in_bike_lanes(self, value: bool):
        self.proto.bicycles_only_in_bike_lanes = value

    @property
    def lane_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._lane_type

    @lane_type.setter
    def lane_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self._lane_type.proto.CopyFrom(value.proto)

    @property
    def lateral_offset(self) -> CenterSpreadConfig:
        return self._lateral_offset

    @lateral_offset.setter
    def lateral_offset(self, value: CenterSpreadConfig):
        self._lateral_offset.proto.CopyFrom(value.proto)

    @property
    def min_length_behind(self) -> Dict[str, CenterSpreadConfig]:
        return self._min_length_behind

    @min_length_behind.setter
    def min_length_behind(self, value: Dict[str, CenterSpreadConfig]):
        self._min_length_behind.clear()
        self._min_length_behind.update(value)

    @property
    def min_num_lanes_in_opposite_direction(self) -> int:
        return self.proto.min_num_lanes_in_opposite_direction

    @min_num_lanes_in_opposite_direction.setter
    def min_num_lanes_in_opposite_direction(self, value: int):
        self.proto.min_num_lanes_in_opposite_direction = value

    @property
    def min_num_lanes_in_same_direction(self) -> int:
        return self.proto.min_num_lanes_in_same_direction

    @min_num_lanes_in_same_direction.setter
    def min_num_lanes_in_same_direction(self, value: int):
        self.proto.min_num_lanes_in_same_direction = value

    @property
    def min_path_length(self) -> Dict[str, CenterSpreadConfig]:
        return self._min_path_length

    @min_path_length.setter
    def min_path_length(self, value: Dict[str, CenterSpreadConfig]):
        self._min_path_length.clear()
        self._min_path_length.update(value)

    @property
    def nearby_asset_policy(self) -> NearbyAssetPolicy:
        return self._nearby_asset_policy

    @nearby_asset_policy.setter
    def nearby_asset_policy(self, value: NearbyAssetPolicy):
        self._nearby_asset_policy.proto.CopyFrom(value.proto)

    @property
    def position_of_interest_policy(self) -> List[PositionOfInterestPolicy]:
        return self._position_of_interest_policy

    @position_of_interest_policy.setter
    def position_of_interest_policy(self, value: List[PositionOfInterestPolicy]):
        self._position_of_interest_policy.clear()
        for v in value:
            self._position_of_interest_policy.append(v)

    @property
    def road_type(self) -> _pd_distributions_pb2.EnumDistribution:
        return self._road_type

    @road_type.setter
    def road_type(self, value: _pd_distributions_pb2.EnumDistribution):
        self._road_type.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.LocationRelativePositionRequest)
class LocationRelativePositionRequest(ProtoMessageClass):
    """
    Description: Gives a location relative to tagged agent (i.e. EGO or STAR). Requires tagged agent to be placed first, otherwise will return error.

    Args:
        agent_tags:
              Description:
                  Tag of agent to spawn relative to
              Required:
                  Yes
        max_spawn_radius:
              Description:
                  The max spawn radius specifies viable spawn locations from the origin, which is the position of tagged agent
              Range:
                  Must be greater than `0.0`
              Required:
                  No, will use default value if not specified
        lane_spawn_policy:
              Description:
                  Specifies lane criteria for viable spawn lanes
              Required:
                  No
"""
    _proto_message = pd_unified_generator_pb2.LocationRelativePositionRequest

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.LocationRelativePositionRequest]=None, agent_tags: Optional[List[SpecialAgentTag]]=None, lane_spawn_policy: Optional[LaneSpawnPolicy]=None, max_spawn_radius: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.LocationRelativePositionRequest()
        self.proto = proto
        self._agent_tags = ProtoListWrapper(container=[int(v) for v in proto.agent_tags], attr_name='agent_tags', list_owner=proto)
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(proto=proto.lane_spawn_policy)
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy
        if max_spawn_radius is not None:
            self.max_spawn_radius = max_spawn_radius

    @property
    def agent_tags(self) -> int:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: int):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self._lane_spawn_policy.proto.CopyFrom(value.proto)

    @property
    def max_spawn_radius(self) -> float:
        return self.proto.max_spawn_radius

    @max_spawn_radius.setter
    def max_spawn_radius(self, value: float):
        self.proto.max_spawn_radius = value

@register_wrapper(proto_type=pd_unified_generator_pb2.MinMaxConfigFloat)
class MinMaxConfigFloat(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.MinMaxConfigFloat

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.MinMaxConfigFloat]=None, max: Optional[float]=None, min: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.MinMaxConfigFloat()
        self.proto = proto
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self) -> float:
        return self.proto.max

    @max.setter
    def max(self, value: float):
        self.proto.max = value

    @property
    def min(self) -> float:
        return self.proto.min

    @min.setter
    def min(self, value: float):
        self.proto.min = value

@register_wrapper(proto_type=pd_unified_generator_pb2.MinMaxConfigInt)
class MinMaxConfigInt(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.MinMaxConfigInt

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.MinMaxConfigInt]=None, max: Optional[int]=None, min: Optional[int]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.MinMaxConfigInt()
        self.proto = proto
        if max is not None:
            self.max = max
        if min is not None:
            self.min = min

    @property
    def max(self) -> int:
        return self.proto.max

    @max.setter
    def max(self, value: int):
        self.proto.max = value

    @property
    def min(self) -> int:
        return self.proto.min

    @min.setter
    def min(self, value: int):
        self.proto.min = value

@register_wrapper(proto_type=pd_unified_generator_pb2.NearbyAssetPolicy)
class NearbyAssetPolicy(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.NearbyAssetPolicy

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.NearbyAssetPolicy]=None, asset_tags: Optional[List[str]]=None, num_assets: Optional[MinMaxConfigInt]=None, search_radius: Optional[CenterSpreadConfig]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.NearbyAssetPolicy()
        self.proto = proto
        self._asset_tags = ProtoListWrapper(container=[str(v) for v in proto.asset_tags], attr_name='asset_tags', list_owner=proto)
        self._num_assets = get_wrapper(proto_type=proto.num_assets.__class__)(proto=proto.num_assets)
        self._search_radius = get_wrapper(proto_type=proto.search_radius.__class__)(proto=proto.search_radius)
        if asset_tags is not None:
            self.asset_tags = asset_tags
        if num_assets is not None:
            self.num_assets = num_assets
        if search_radius is not None:
            self.search_radius = search_radius

    @property
    def asset_tags(self) -> List[str]:
        return self._asset_tags

    @asset_tags.setter
    def asset_tags(self, value: List[str]):
        self._asset_tags.clear()
        for v in value:
            self._asset_tags.append(v)

    @property
    def num_assets(self) -> MinMaxConfigInt:
        return self._num_assets

    @num_assets.setter
    def num_assets(self, value: MinMaxConfigInt):
        self._num_assets.proto.CopyFrom(value.proto)

    @property
    def search_radius(self) -> CenterSpreadConfig:
        return self._search_radius

    @search_radius.setter
    def search_radius(self, value: CenterSpreadConfig):
        self._search_radius.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.ParkedVehicleGeneratorParameters)
class ParkedVehicleGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places a parked vehicle into the world. Requires ego atomic.

    Args:
        position_request:
              Description:
                  Determines the spawn radius of parked vehicles (see `LocationRelativePositionRequest`)
              Range:
                  Only works with `LocationRelativePositionRequest`
              Required:
                  Yes
        spawn_probability:
              Description:
                  For every available parking space within the spawn radius, the generator will use this probability to determine if a
                  parked vehicle should spawn there, (i.e. controls density)
              Required:
                  No, if not specified will use default probability: `{center=0.5, spread=0}`
        vehicle_distribution:
              Description:
                  Likelihood of vehicle types spawning
              Required:
                  No, if not specified, will use these defaults::

                    MIDSIZE	    0.181
                    COMPACT	    0.177
                    BUS	        0.019
                    TRUCK	    0.038
                    SUV	        0.197
                    VAN     	0.066
                    BICYCLE	    0.061
                    MOTORCYCLE	0.068
                    CARAVAN/RV	0.009
                    FULLSIZE	0.184
"""
    _proto_message = pd_unified_generator_pb2.ParkedVehicleGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.ParkedVehicleGeneratorParameters]=None, position_request: Optional[PositionRequest]=None, spawn_probability: Optional[CenterSpreadConfig]=None, vehicle_distribution: Optional[Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.ParkedVehicleGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._spawn_probability = get_wrapper(proto_type=proto.spawn_probability.__class__)(proto=proto.spawn_probability)
        self._vehicle_distribution = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()}, attr_name='vehicle_distribution', dict_owner=proto)
        if position_request is not None:
            self.position_request = position_request
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def spawn_probability(self) -> CenterSpreadConfig:
        return self._spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: CenterSpreadConfig):
        self._spawn_probability.proto.CopyFrom(value.proto)

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

@register_wrapper(proto_type=pd_unified_generator_pb2.ParkingTypeDistribution)
class ParkingTypeDistribution(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.ParkingTypeDistribution

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.ParkingTypeDistribution]=None, forward: Optional[float]=None, parallel: Optional[float]=None, reverse: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.ParkingTypeDistribution()
        self.proto = proto
        if forward is not None:
            self.forward = forward
        if parallel is not None:
            self.parallel = parallel
        if reverse is not None:
            self.reverse = reverse

    @property
    def forward(self) -> float:
        return self.proto.forward

    @forward.setter
    def forward(self, value: float):
        self.proto.forward = value

    @property
    def parallel(self) -> float:
        return self.proto.parallel

    @parallel.setter
    def parallel(self, value: float):
        self.proto.parallel = value

    @property
    def reverse(self) -> float:
        return self.proto.reverse

    @reverse.setter
    def reverse(self, value: float):
        self.proto.reverse = value

@register_wrapper(proto_type=pd_unified_generator_pb2.PathTimeRelativePositionRequest)
class PathTimeRelativePositionRequest(ProtoMessageClass):
    """
    Description:
        Sets an intersection point that the placed agent and the tagged agent's (i.e. EGO or STAR) will cross, as well
        as a path for the placed agent. Requires tagged agent to be placed first, otherwise will return error.
        Only works on Drivable lane type, and only works with vehicles relative to other vehicles

    Args:
        agent_tags:
              Description:
                  Tag of agent to spawn relative to
              Required:
                  Yes
        time_to_path:
              Description:
                  Time for agent being placed to reach intersection point
              Range:
                  Distribution must sample from nonzero values
              Required:
                  No, will default to 0 values. Note: If both time_to_path and time_along_path are 0 or not specified, user must specify longitudinal_offset_m and/or lateral_offset_m.
        time_along_path:
              Description:
                  Time for agent specified by agent_tag to reach intersection point
              Range:
                  Distribution must sample from nonzero values
              Required:
                  No, will default to 0 values. Note: If both time_to_path and time_along_path are 0 or not specified, user must specify longitudinal_offset_m and/or lateral_offset_m.
        incident_angle:
              Description:
                  Angle to cross paths at
              Range:
                  Valid angle in rad
              Required:
                  No, if not specified then will intersect at any angle
"""
    _proto_message = pd_unified_generator_pb2.PathTimeRelativePositionRequest

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.PathTimeRelativePositionRequest]=None, agent_tags: Optional[List[SpecialAgentTag]]=None, incident_angle: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, time_along_path: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, time_to_path: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.PathTimeRelativePositionRequest()
        self.proto = proto
        self._agent_tags = ProtoListWrapper(container=[int(v) for v in proto.agent_tags], attr_name='agent_tags', list_owner=proto)
        self._incident_angle = get_wrapper(proto_type=proto.incident_angle.__class__)(proto=proto.incident_angle)
        self._time_along_path = get_wrapper(proto_type=proto.time_along_path.__class__)(proto=proto.time_along_path)
        self._time_to_path = get_wrapper(proto_type=proto.time_to_path.__class__)(proto=proto.time_to_path)
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if incident_angle is not None:
            self.incident_angle = incident_angle
        if time_along_path is not None:
            self.time_along_path = time_along_path
        if time_to_path is not None:
            self.time_to_path = time_to_path

    @property
    def agent_tags(self) -> int:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: int):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    @property
    def incident_angle(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._incident_angle

    @incident_angle.setter
    def incident_angle(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._incident_angle.proto.CopyFrom(value.proto)

    @property
    def time_along_path(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._time_along_path

    @time_along_path.setter
    def time_along_path(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._time_along_path.proto.CopyFrom(value.proto)

    @property
    def time_to_path(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._time_to_path

    @time_to_path.setter
    def time_to_path(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._time_to_path.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.PedestrianGeneratorParameters)
class PedestrianGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places a single pedestrian into the world. Requires ego atomic.

    Args:
        position_request:
              Description:
                  Determines where the pedestrian will spawn
              Range:
                  Any `PositionRequest` except `PathTimeRelativePositionRequest`
              Required:
                  Yes
        ped_spawn_data:
              Description:
                  This contains parameters that control pedestrian spawning and movement behavior
              Required:
                  No, will use defaults specified in `PedestrianSpawnData`
"""
    _proto_message = pd_unified_generator_pb2.PedestrianGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.PedestrianGeneratorParameters]=None, ped_spawn_data: Optional[PedestrianSpawnData]=None, position_request: Optional[PositionRequest]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.PedestrianGeneratorParameters()
        self.proto = proto
        self._ped_spawn_data = get_wrapper(proto_type=proto.ped_spawn_data.__class__)(proto=proto.ped_spawn_data)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        if ped_spawn_data is not None:
            self.ped_spawn_data = ped_spawn_data
        if position_request is not None:
            self.position_request = position_request

    @property
    def ped_spawn_data(self) -> PedestrianSpawnData:
        return self._ped_spawn_data

    @ped_spawn_data.setter
    def ped_spawn_data(self, value: PedestrianSpawnData):
        self._ped_spawn_data.proto.CopyFrom(value.proto)

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.PedestrianSpawnData)
class PedestrianSpawnData(ProtoMessageClass):
    """
    Description: This contains parameters that control pedestrian/pedestrian related behavior

    Args:
        pedestrian_color_override_probability:
              Description:
                  Specifies probability of overriding color of pedestrian's clothes to RGB color specified by pedestrian_color_override_rgb
              Range:
                  Greater than or equal to 0
              Required:
                  No, will default to 0 values
        pedestrian_color_override_rgb:
              Description:
                  Specifies color to override pedestrian's clothes with if determining an override should happen
              Range:
                  Valid RGB color
              Required:
                  No, will use default 0 values if this field is required
        pedestrians_dynamic_pathing:
              Description:
                  Specifies whether pedestrian should use dynamic pathing or not.
                  If true, determines path to take during sim and can change depending on location.
                  If false, uses a predetermined path to take during scenario generation.
              Required:
                  No, will use default value
        orient_to_velocity:
              Description:
                  Specifies whether pedestrian should face the direction of movement
              Required:
                  No, will use default value
        check_occupancy:
              Description:
                  Specifies whether or not we check if the area we are trying to spawn in is occupied.
              Required:
                  No, will use default value
        jaywalker_ego_fwd_offset:
              Description:
                  Specifies how far ahead the jaywalker should be from the tagged vehicle.
                  If ped_behavior is not set to JAYWALKING, this field will be ignored.
              Range:
                  Greater than or equal to 0
              Required:
                  No, will use default value
        agent_spawn_data:
              Description:
                  Specifies spawn data that applies across agent types
              Required:
                  No
        ped_behavior:
              Description:
                  Specifies desired behavior of pedestrian
              Required:
                  No, will default to NORMAL for PedestrianBehavior
        asset_name:
              Description:
                  Asset name of pedestrian, must be an asset from asset registry.
              Required:
                  Yes
        speed:
              Description:
                  Speed of pedestrian
              Range:
                  Greater than or equal to 0
              Required:
                  No, will use default value
"""
    _proto_message = pd_unified_generator_pb2.PedestrianSpawnData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.PedestrianSpawnData]=None, agent_spawn_data: Optional[AgentSpawnData]=None, asset_name: Optional[str]=None, check_occupancy: Optional[bool]=None, jaywalker_ego_fwd_offset: Optional[float]=None, orient_to_velocity: Optional[bool]=None, ped_behavior: Optional[PedestrianBehavior]=None, pedestrian_color_override_probability: Optional[CenterSpreadConfig]=None, pedestrian_color_override_rgb: Optional[_pd_types_pb2.Float3]=None, pedestrians_dynamic_pathing: Optional[bool]=None, speed: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.PedestrianSpawnData()
        self.proto = proto
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        self._pedestrian_color_override_probability = get_wrapper(proto_type=proto.pedestrian_color_override_probability.__class__)(proto=proto.pedestrian_color_override_probability)
        self._pedestrian_color_override_rgb = get_wrapper(proto_type=proto.pedestrian_color_override_rgb.__class__)(proto=proto.pedestrian_color_override_rgb)
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data
        if asset_name is not None:
            self.asset_name = asset_name
        if check_occupancy is not None:
            self.check_occupancy = check_occupancy
        if jaywalker_ego_fwd_offset is not None:
            self.jaywalker_ego_fwd_offset = jaywalker_ego_fwd_offset
        if orient_to_velocity is not None:
            self.orient_to_velocity = orient_to_velocity
        if ped_behavior is not None:
            self.ped_behavior = ped_behavior
        if pedestrian_color_override_probability is not None:
            self.pedestrian_color_override_probability = pedestrian_color_override_probability
        if pedestrian_color_override_rgb is not None:
            self.pedestrian_color_override_rgb = pedestrian_color_override_rgb
        if pedestrians_dynamic_pathing is not None:
            self.pedestrians_dynamic_pathing = pedestrians_dynamic_pathing
        if speed is not None:
            self.speed = speed

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self._agent_spawn_data.proto.CopyFrom(value.proto)

    @property
    def asset_name(self) -> str:
        return self.proto.asset_name

    @asset_name.setter
    def asset_name(self, value: str):
        self.proto.asset_name = value

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
    def orient_to_velocity(self) -> bool:
        return self.proto.orient_to_velocity

    @orient_to_velocity.setter
    def orient_to_velocity(self, value: bool):
        self.proto.orient_to_velocity = value

    @property
    def ped_behavior(self) -> int:
        return self.proto.ped_behavior

    @ped_behavior.setter
    def ped_behavior(self, value: int):
        self.proto.ped_behavior = value

    @property
    def pedestrian_color_override_probability(self) -> CenterSpreadConfig:
        return self._pedestrian_color_override_probability

    @pedestrian_color_override_probability.setter
    def pedestrian_color_override_probability(self, value: CenterSpreadConfig):
        self._pedestrian_color_override_probability.proto.CopyFrom(value.proto)

    @property
    def pedestrian_color_override_rgb(self) -> _pd_types_pb2.Float3:
        return self._pedestrian_color_override_rgb

    @pedestrian_color_override_rgb.setter
    def pedestrian_color_override_rgb(self, value: _pd_types_pb2.Float3):
        self._pedestrian_color_override_rgb.proto.CopyFrom(value.proto)

    @property
    def pedestrians_dynamic_pathing(self) -> bool:
        return self.proto.pedestrians_dynamic_pathing

    @pedestrians_dynamic_pathing.setter
    def pedestrians_dynamic_pathing(self, value: bool):
        self.proto.pedestrians_dynamic_pathing = value

    @property
    def speed(self) -> float:
        return self.proto.speed

    @speed.setter
    def speed(self, value: float):
        self.proto.speed = value

@register_wrapper(proto_type=pd_unified_generator_pb2.PositionOfInterestPolicy)
class PositionOfInterestPolicy(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.PositionOfInterestPolicy

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.PositionOfInterestPolicy]=None, junction_spawn_policy: Optional[JunctionSpawnPolicy]=None, lane_curvature_spawn_policy: Optional[LaneCurvatureSpawnPolicy]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.PositionOfInterestPolicy()
        self.proto = proto
        self._junction_spawn_policy = get_wrapper(proto_type=proto.junction_spawn_policy.__class__)(proto=proto.junction_spawn_policy)
        self._lane_curvature_spawn_policy = get_wrapper(proto_type=proto.lane_curvature_spawn_policy.__class__)(proto=proto.lane_curvature_spawn_policy)
        if junction_spawn_policy is not None:
            self.junction_spawn_policy = junction_spawn_policy
        if lane_curvature_spawn_policy is not None:
            self.lane_curvature_spawn_policy = lane_curvature_spawn_policy

    @property
    def junction_spawn_policy(self) -> JunctionSpawnPolicy:
        return self._junction_spawn_policy

    @junction_spawn_policy.setter
    def junction_spawn_policy(self, value: JunctionSpawnPolicy):
        self._junction_spawn_policy.proto.CopyFrom(value.proto)

    @property
    def lane_curvature_spawn_policy(self) -> LaneCurvatureSpawnPolicy:
        return self._lane_curvature_spawn_policy

    @lane_curvature_spawn_policy.setter
    def lane_curvature_spawn_policy(self, value: LaneCurvatureSpawnPolicy):
        self._lane_curvature_spawn_policy.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.PositionRequest)
class PositionRequest(ProtoMessageClass):
    """
    Description: Determines pose of agents, or spawn center for multiple agents

    Args:
        longitudinal_offset:
              Description:
                  Only applied after initial pose is determined by position_type.
                  Determines how much farther ahead along a lane to move the returned pose
              Required:
                  No, will default to `0.0`
        lateral_offset:
              Description:
                  Only applied after initial pose is determined by position_type.
                  Determines how much farther to the left (negative for right) we want to move the returned pose
              Required:
                  No, will default to `0.0`
        yaw_offset:
              Description:
                  Only applied after initial pose is determined by position_type.
                  Determines how much to rotate pose about Z axis (points up in right handed coordinate system)
                  Example: 90 degrees would rotate pose to the left.
              Required:
                  No, will default to `0.0`
        position_type:
              Description:
                  Determines initial pose
              Required:
                  Yes
"""
    _proto_message = pd_unified_generator_pb2.PositionRequest

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.PositionRequest]=None, absolute_position_request: Optional[AbsolutePositionRequest]=None, lane_spawn_policy: Optional[LaneSpawnPolicy]=None, lateral_offset: Optional[CenterSpreadConfig]=None, location_relative_position_request: Optional[LocationRelativePositionRequest]=None, longitudinal_offset: Optional[CenterSpreadConfig]=None, path_time_relative_position_request: Optional[PathTimeRelativePositionRequest]=None, road_pitch_position_request: Optional[RoadPitchPositionRequest]=None, yaw_offset: Optional[CenterSpreadConfig]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.PositionRequest()
        self.proto = proto
        self._absolute_position_request = get_wrapper(proto_type=proto.absolute_position_request.__class__)(proto=proto.absolute_position_request)
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(proto=proto.lane_spawn_policy)
        self._lateral_offset = get_wrapper(proto_type=proto.lateral_offset.__class__)(proto=proto.lateral_offset)
        self._location_relative_position_request = get_wrapper(proto_type=proto.location_relative_position_request.__class__)(proto=proto.location_relative_position_request)
        self._longitudinal_offset = get_wrapper(proto_type=proto.longitudinal_offset.__class__)(proto=proto.longitudinal_offset)
        self._path_time_relative_position_request = get_wrapper(proto_type=proto.path_time_relative_position_request.__class__)(proto=proto.path_time_relative_position_request)
        self._road_pitch_position_request = get_wrapper(proto_type=proto.road_pitch_position_request.__class__)(proto=proto.road_pitch_position_request)
        self._yaw_offset = get_wrapper(proto_type=proto.yaw_offset.__class__)(proto=proto.yaw_offset)
        if absolute_position_request is not None:
            self.absolute_position_request = absolute_position_request
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy
        if lateral_offset is not None:
            self.lateral_offset = lateral_offset
        if location_relative_position_request is not None:
            self.location_relative_position_request = location_relative_position_request
        if longitudinal_offset is not None:
            self.longitudinal_offset = longitudinal_offset
        if path_time_relative_position_request is not None:
            self.path_time_relative_position_request = path_time_relative_position_request
        if road_pitch_position_request is not None:
            self.road_pitch_position_request = road_pitch_position_request
        if yaw_offset is not None:
            self.yaw_offset = yaw_offset

    @property
    def absolute_position_request(self) -> AbsolutePositionRequest:
        return self._absolute_position_request

    @absolute_position_request.setter
    def absolute_position_request(self, value: AbsolutePositionRequest):
        self._absolute_position_request.proto.CopyFrom(value.proto)

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self._lane_spawn_policy.proto.CopyFrom(value.proto)

    @property
    def lateral_offset(self) -> CenterSpreadConfig:
        return self._lateral_offset

    @lateral_offset.setter
    def lateral_offset(self, value: CenterSpreadConfig):
        self._lateral_offset.proto.CopyFrom(value.proto)

    @property
    def location_relative_position_request(self) -> LocationRelativePositionRequest:
        return self._location_relative_position_request

    @location_relative_position_request.setter
    def location_relative_position_request(self, value: LocationRelativePositionRequest):
        self._location_relative_position_request.proto.CopyFrom(value.proto)

    @property
    def longitudinal_offset(self) -> CenterSpreadConfig:
        return self._longitudinal_offset

    @longitudinal_offset.setter
    def longitudinal_offset(self, value: CenterSpreadConfig):
        self._longitudinal_offset.proto.CopyFrom(value.proto)

    @property
    def path_time_relative_position_request(self) -> PathTimeRelativePositionRequest:
        return self._path_time_relative_position_request

    @path_time_relative_position_request.setter
    def path_time_relative_position_request(self, value: PathTimeRelativePositionRequest):
        self._path_time_relative_position_request.proto.CopyFrom(value.proto)

    @property
    def road_pitch_position_request(self) -> RoadPitchPositionRequest:
        return self._road_pitch_position_request

    @road_pitch_position_request.setter
    def road_pitch_position_request(self, value: RoadPitchPositionRequest):
        self._road_pitch_position_request.proto.CopyFrom(value.proto)

    @property
    def yaw_offset(self) -> CenterSpreadConfig:
        return self._yaw_offset

    @yaw_offset.setter
    def yaw_offset(self, value: CenterSpreadConfig):
        self._yaw_offset.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.RandomPedestrianGeneratorParameters)
class RandomPedestrianGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places multiple pedestrians (i.e. a crowd) into the world. Requires ego atomic.

    Args:
        speed_range:
              Description:
                  Speed of each pedestrian is set randomly within this range
              Range:
                  Min > `0`, Max > Min
              Required:
                  No, if not specified then will use range `{0.5, 1.5}`
        position_request:
              Description:
                  Determines the center of where the pedestrians will spawn. Radius controlled by `LocationRelativePositionRequest`
              Required:
                  Yes
        num_of_pedestrians_range:
              Description:
                  Number of pedestrians to generate is selected randomly within this range.
                  If `min_radius_between_pedestrians` is high and the determined number of pedestrians can't be placed, scenario generation will fail.
              Range:
                  Min > `0`, Max > Min
              Required:
                  Yes
        min_radius_between_pedestrians:
              Description:
                  Specifies how much space should be between individual pedestrians.
                  The higher the value, the more spaced out the pedestrians will be from each other.
              Range:
                  Greater than `0.0`
              Required:
                  No, if not specified will use default value
        ped_spawn_data:
              Description:
                  This contains parameters that control pedestrian and pedestrian related behavior
              Required:
                  No, will use defaults specified in `PedestrianSpawnData`
"""
    _proto_message = pd_unified_generator_pb2.RandomPedestrianGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.RandomPedestrianGeneratorParameters]=None, min_radius_between_pedestrians: Optional[float]=None, num_of_pedestrians_range: Optional[MinMaxConfigInt]=None, ped_spawn_data: Optional[PedestrianSpawnData]=None, position_request: Optional[PositionRequest]=None, speed_range: Optional[MinMaxConfigFloat]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.RandomPedestrianGeneratorParameters()
        self.proto = proto
        self._num_of_pedestrians_range = get_wrapper(proto_type=proto.num_of_pedestrians_range.__class__)(proto=proto.num_of_pedestrians_range)
        self._ped_spawn_data = get_wrapper(proto_type=proto.ped_spawn_data.__class__)(proto=proto.ped_spawn_data)
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._speed_range = get_wrapper(proto_type=proto.speed_range.__class__)(proto=proto.speed_range)
        if min_radius_between_pedestrians is not None:
            self.min_radius_between_pedestrians = min_radius_between_pedestrians
        if num_of_pedestrians_range is not None:
            self.num_of_pedestrians_range = num_of_pedestrians_range
        if ped_spawn_data is not None:
            self.ped_spawn_data = ped_spawn_data
        if position_request is not None:
            self.position_request = position_request
        if speed_range is not None:
            self.speed_range = speed_range

    @property
    def min_radius_between_pedestrians(self) -> float:
        return self.proto.min_radius_between_pedestrians

    @min_radius_between_pedestrians.setter
    def min_radius_between_pedestrians(self, value: float):
        self.proto.min_radius_between_pedestrians = value

    @property
    def num_of_pedestrians_range(self) -> MinMaxConfigInt:
        return self._num_of_pedestrians_range

    @num_of_pedestrians_range.setter
    def num_of_pedestrians_range(self, value: MinMaxConfigInt):
        self._num_of_pedestrians_range.proto.CopyFrom(value.proto)

    @property
    def ped_spawn_data(self) -> PedestrianSpawnData:
        return self._ped_spawn_data

    @ped_spawn_data.setter
    def ped_spawn_data(self, value: PedestrianSpawnData):
        self._ped_spawn_data.proto.CopyFrom(value.proto)

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def speed_range(self) -> MinMaxConfigFloat:
        return self._speed_range

    @speed_range.setter
    def speed_range(self, value: MinMaxConfigFloat):
        self._speed_range.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.RoadMarkingData)
class RoadMarkingData(ProtoMessageClass):
    """
    Description: This contains parameters that control appearance of road markings

    Args:
        use_preset:
              Description:
                  Not implemented yet.
                  Specifies whether to use RGB values from asset registry.
              Required:
                  No, will use default value
        override_colors:
              Description:
                  Specifies RGB color to override with
              Range:
                  3 dimensional array with values from `0-1`, i.e. `[0.2, 0.2, 0.2]`
              Required:
                  No, will use default values specified in marker_data_map
        preset_colors:
              Description:
                  Not implemented yet. Colors specified in asset registry to use for road markings used if `use_preset` is set to `True`.
              Required:
                  No
        marker_types:
              Description:
                  Specifies a marker name.
                  The available options are specific to which key it is under in marker_data_map.
              Range:
                  Parking space markers include::

                    {
                        "Single",
                        "Dashed",
                        "Double Open",      (parallel lines)
                        "Double Squared",   (parallel lines closed at the end with a line, resembling long rectangles)
                        "Double Round",     (parallel lines closed at the end with a semi-circle)
                        "T"
                    }
                  Parking surface markers include::

                    {
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
                    }
              Required:
                  No, will use default values specified in marker_data_map
        wear:
              Description:
                  Determines how "worn down" the markings are. `1.0` is most worn down, `0.0` is no wear
              Range:
                  `0.0` to `1.0`
              Required:
                  No, will use default 0 values
"""
    _proto_message = pd_unified_generator_pb2.RoadMarkingData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.RoadMarkingData]=None, marker_types: Optional[List[str]]=None, override_colors: Optional[List[FloatArray]]=None, preset_colors: Optional[List[str]]=None, use_preset: Optional[bool]=None, wear: Optional[CenterSpreadConfig]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.RoadMarkingData()
        self.proto = proto
        self._marker_types = ProtoListWrapper(container=[str(v) for v in proto.marker_types], attr_name='marker_types', list_owner=proto)
        self._override_colors = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.override_colors], attr_name='override_colors', list_owner=proto)
        self._preset_colors = ProtoListWrapper(container=[str(v) for v in proto.preset_colors], attr_name='preset_colors', list_owner=proto)
        self._wear = get_wrapper(proto_type=proto.wear.__class__)(proto=proto.wear)
        if marker_types is not None:
            self.marker_types = marker_types
        if override_colors is not None:
            self.override_colors = override_colors
        if preset_colors is not None:
            self.preset_colors = preset_colors
        if use_preset is not None:
            self.use_preset = use_preset
        if wear is not None:
            self.wear = wear

    @property
    def marker_types(self) -> List[str]:
        return self._marker_types

    @marker_types.setter
    def marker_types(self, value: List[str]):
        self._marker_types.clear()
        for v in value:
            self._marker_types.append(v)

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
    def use_preset(self) -> bool:
        return self.proto.use_preset

    @use_preset.setter
    def use_preset(self, value: bool):
        self.proto.use_preset = value

    @property
    def wear(self) -> CenterSpreadConfig:
        return self._wear

    @wear.setter
    def wear(self, value: CenterSpreadConfig):
        self._wear.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.RoadPitchPositionRequest)
class RoadPitchPositionRequest(ProtoMessageClass):
    """
    Description: Gives a position based on desired road pitch angle to spawn at

    Args:
"""
    _proto_message = pd_unified_generator_pb2.RoadPitchPositionRequest

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.RoadPitchPositionRequest]=None, bin_pitch_points: Optional[bool]=None, bin_width: Optional[float]=None, lane_spawn_policy: Optional[LaneSpawnPolicy]=None, road_pitch: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.RoadPitchPositionRequest()
        self.proto = proto
        self._lane_spawn_policy = get_wrapper(proto_type=proto.lane_spawn_policy.__class__)(proto=proto.lane_spawn_policy)
        self._road_pitch = get_wrapper(proto_type=proto.road_pitch.__class__)(proto=proto.road_pitch)
        if bin_pitch_points is not None:
            self.bin_pitch_points = bin_pitch_points
        if bin_width is not None:
            self.bin_width = bin_width
        if lane_spawn_policy is not None:
            self.lane_spawn_policy = lane_spawn_policy
        if road_pitch is not None:
            self.road_pitch = road_pitch

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

    @property
    def lane_spawn_policy(self) -> LaneSpawnPolicy:
        return self._lane_spawn_policy

    @lane_spawn_policy.setter
    def lane_spawn_policy(self, value: LaneSpawnPolicy):
        self._lane_spawn_policy.proto.CopyFrom(value.proto)

    @property
    def road_pitch(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._road_pitch

    @road_pitch.setter
    def road_pitch(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._road_pitch.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.SignalLightDistribution)
class SignalLightDistribution(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.SignalLightDistribution

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.SignalLightDistribution]=None, green: Optional[float]=None, red: Optional[float]=None, yellow: Optional[float]=None):
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

@register_wrapper(proto_type=pd_unified_generator_pb2.StaticAgentGeneratorParameters)
class StaticAgentGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places a static agent into the world. Requires ego atomic.

    Args:
        position_request:
              Description:
                  Determines where the static agent will spawn
              Required:
                  Yes
        model:
              Description:
                  The asset name of the static agent we want to place
              Required:
                  Yes
"""
    _proto_message = pd_unified_generator_pb2.StaticAgentGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.StaticAgentGeneratorParameters]=None, model: Optional[str]=None, position_request: Optional[PositionRequest]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.StaticAgentGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        if model is not None:
            self.model = model
        if position_request is not None:
            self.position_request = position_request

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
        self._position_request.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.TrafficGeneratorParameters)
class TrafficGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places multiple vehicles into the world. Requires ego atomic.

    Args:
        position_request:
              Description:
                  Determines the spawn radius of vehicles (see `LocationRelativePositionRequest`)
              Range:
                  Only works with `LocationRelativePositionRequest`
              Required:
                  Yes
        spawn_probability:
              Description:
                  Within spawn radius, probability that a vehicle will spawn in an available spot. (i.e. controls density)
              Range:
                  `0.0` to `1.0`, with `1.0` being the most dense. Recommended to use `0.8` for high density.
              Required:
                  No, will use default value if not specified
        vehicle_spawn_data:
              Description:
                  This contains parameters that control vehicle and vehicle related behavior
              Required:
                  No, will use defaults specified in `VehicleSpawnData`
        vehicle_distribution:
              Description:
                  Likelihood of vehicles spawning
              Required:
                  No. If not specified, will default to::

                    MIDSIZE 0.181
                    COMPACT 0.177
                    BUS 0.019
                    TRUCK 0.038
                    SUV 0.197
                    VAN 0.066
                    BICYCLE 0.061
                    MOTORCYCLE  0.068
                    CARAVAN/RV  0.009
                    FULLSIZE  0.184
        start_separation_time_map:
              Description:
                  Recommended to leave as default. Map of vehicle type to their start separation time distributions.
                  Uses initial speed * separation time to determine distance between vehicles.
              Required:
                  No, if not specified will use defaults, see map below::

                    {"bicycle", {0.7f, 1.7f}},
                    {"heavy", {2.5f, 3.5f}},
                    {"heavy_nondriven", {2.5f, 3.5f}},
                    {"light", {0.7f, 1.7f}},
                    {"light_nondriven", {0.7f, 1.7f}},
                    {"medium", {1.5f, 2.5f}},
                    {"medium_nondriven", {1.5f, 2.5f}},
                    {"motorcycle", {0.7f, 1.7f}}
        target_separation_time_map:
              Description:
                  Map of vehicle type to their target separation time distributions
              Required:
                  No, if not specified it will use the values provided in `start_separation_time_map`.
"""
    _proto_message = pd_unified_generator_pb2.TrafficGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.TrafficGeneratorParameters]=None, position_request: Optional[PositionRequest]=None, spawn_probability: Optional[float]=None, start_separation_time_map: Optional[Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]]=None, target_separation_time_map: Optional[Dict[str, _pd_distributions_pb2.ContinousUniformDistribution]]=None, vehicle_distribution: Optional[Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]]=None, vehicle_spawn_data: Optional[VehicleSpawnData]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.TrafficGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._start_separation_time_map = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.start_separation_time_map.items()}, attr_name='start_separation_time_map', dict_owner=proto)
        self._target_separation_time_map = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.target_separation_time_map.items()}, attr_name='target_separation_time_map', dict_owner=proto)
        self._vehicle_distribution = ProtoDictWrapper(container={k: get_wrapper(proto_type=v.__class__)(proto=v) for (k, v) in proto.vehicle_distribution.items()}, attr_name='vehicle_distribution', dict_owner=proto)
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(proto=proto.vehicle_spawn_data)
        if position_request is not None:
            self.position_request = position_request
        if spawn_probability is not None:
            self.spawn_probability = spawn_probability
        if start_separation_time_map is not None:
            self.start_separation_time_map = start_separation_time_map
        if target_separation_time_map is not None:
            self.target_separation_time_map = target_separation_time_map
        if vehicle_distribution is not None:
            self.vehicle_distribution = vehicle_distribution
        if vehicle_spawn_data is not None:
            self.vehicle_spawn_data = vehicle_spawn_data

    @property
    def position_request(self) -> PositionRequest:
        return self._position_request

    @position_request.setter
    def position_request(self, value: PositionRequest):
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def spawn_probability(self) -> float:
        return self.proto.spawn_probability

    @spawn_probability.setter
    def spawn_probability(self, value: float):
        self.proto.spawn_probability = value

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

    @property
    def vehicle_distribution(self) -> Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]:
        return self._vehicle_distribution

    @vehicle_distribution.setter
    def vehicle_distribution(self, value: Dict[str, _pd_distributions_pb2.VehicleCategoryWeight]):
        self._vehicle_distribution.clear()
        self._vehicle_distribution.update(value)

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self._vehicle_spawn_data.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.TurnTypeDistribution)
class TurnTypeDistribution(ProtoMessageClass):
    _proto_message = pd_unified_generator_pb2.TurnTypeDistribution

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.TurnTypeDistribution]=None, left: Optional[float]=None, right: Optional[float]=None, straight: Optional[float]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.TurnTypeDistribution()
        self.proto = proto
        if left is not None:
            self.left = left
        if right is not None:
            self.right = right
        if straight is not None:
            self.straight = straight

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

    @property
    def straight(self) -> float:
        return self.proto.straight

    @straight.setter
    def straight(self, value: float):
        self.proto.straight = value

@register_wrapper(proto_type=pd_unified_generator_pb2.UnifiedGeneratorParameters)
class UnifiedGeneratorParameters(ProtoMessageClass):
    """
    Description:
        Wrapper for all scenario parameters. Applied once per location specified in scenario generation. 

    Args:
        atomics:
              Description:
                  Determines which atomic generators are used for the scenario.
              Required:
                  Yes, if none, nothing will be generated.
        use_merge_batches:
              Description:
                  Combines multiple scenes into a single scene for rendering efficiency
              Required:
                  No, will use default value.
        default_params:
              Description:
                  Contains parameters that apply to all atomic generators
              Required:
                  No, if not specified it will use atomic-specific defaults
        environment_params:
              Description:
                  Contains parameters that modify the map
              Required:
                  No, if not specified, will use what comes by default with each map
"""
    _proto_message = pd_unified_generator_pb2.UnifiedGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.UnifiedGeneratorParameters]=None, atomics: Optional[List[AtomicGeneratorParameters]]=None, default_params: Optional[DefaultAtomicGeneratorParameters]=None, environment_params: Optional[EnvironmentParameters]=None, use_merge_batches: Optional[bool]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.UnifiedGeneratorParameters()
        self.proto = proto
        self._atomics = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.atomics], attr_name='atomics', list_owner=proto)
        self._default_params = get_wrapper(proto_type=proto.default_params.__class__)(proto=proto.default_params)
        self._environment_params = get_wrapper(proto_type=proto.environment_params.__class__)(proto=proto.environment_params)
        if atomics is not None:
            self.atomics = atomics
        if default_params is not None:
            self.default_params = default_params
        if environment_params is not None:
            self.environment_params = environment_params
        if use_merge_batches is not None:
            self.use_merge_batches = use_merge_batches

    @property
    def atomics(self) -> List[AtomicGeneratorParameters]:
        return self._atomics

    @atomics.setter
    def atomics(self, value: List[AtomicGeneratorParameters]):
        self._atomics.clear()
        for v in value:
            self._atomics.append(v)

    @property
    def default_params(self) -> DefaultAtomicGeneratorParameters:
        return self._default_params

    @default_params.setter
    def default_params(self, value: DefaultAtomicGeneratorParameters):
        self._default_params.proto.CopyFrom(value.proto)

    @property
    def environment_params(self) -> EnvironmentParameters:
        return self._environment_params

    @environment_params.setter
    def environment_params(self, value: EnvironmentParameters):
        self._environment_params.proto.CopyFrom(value.proto)

    @property
    def use_merge_batches(self) -> bool:
        return self.proto.use_merge_batches

    @use_merge_batches.setter
    def use_merge_batches(self, value: bool):
        self.proto.use_merge_batches = value

@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleBehavior)
class VehicleBehavior(ProtoMessageClass):
    """
    Description: This contains parameters that control vehicle behavior (i.e. lane change, speed, etc.)

    Args:
        start_speed:
              Description:
                  Specifies start speed of vehicle
              Range:
                  Greater than or equal to `0.0`
              Required:
                  No, will use default 0 values
        target_speed:
              Description:
                  Specifies target speed of vehicle (i.e. speed vehicle tries to achieve while scenario is running). Note: If there is a speed limit, speed will not go greater than it, unless specified by ignore_speed_limit
              Range:
                  Greater than to equal to `0.0`
              Required:
                  No, will use default 0 values
        ignore_speed_limit:
              Description:
                  Specifies whether vehicle should ignore the speed limit specified on roads.
                  If true, then vehicle will use the target_speed specified even if it over the speed limit
              Required:
                  No, will use default value
        lane_offset:
              Description:
                  Specifies lane offset in percentage of lane width in vehicle's motion plan, relative to lane center line.
                  Positive means offset to the right. Negative means offset to the left.
              Range:
                  `-1.0` to `1.0`
              Required:
                  No, will use default 0 values
        lane_drift_scale:
              Description:
                  The slight weaving of vehicles within their lanes is modelled as a perlin noise driven wave that has an amplitude and frequency.
                  Tunes the frequency of the motion line/perlin noise wave.
                  Larger values result in lower frequency.
              Required:
                  No, will use default 0 values
        lane_drift_amplitude:
              Description:
                  The slight weaving of vehicles within their lanes is modelled as a perlin noise driven wave that has an amplitude and frequency.
                  Tunes the amplitude of the motion line/perlin noise wave.
              Range:
                  No specified range. Note: large values are not recommended as it would look unrealistic
              Required:
                  No, will use default 0 values
        lane_change_probability:
              Description:
                  Specifies probability of making a lane change
              Range:
                  `0.0` to `1.0`
              Required:
                  No, will use default 0 values
        lane_change_cooldown:
              Description:
                  Specifies how long we don't want to consider a lane change for
              Range:
                  Greater than or equal to `0.0`
              Required:
                  No, will use default 0 values
        enable_dynamic_lane_selection:
              Description:
                  If true, randomly selects lanes to spawn in during simulation.
                  If false, randomly selects lanes to spawn in during scenario generation.
              Required:
                  No, will use default value
        start_gear:
              Description:
                  Specifies what to set the vehicle's gear to
              Required:
                  No, will use default value
        start_separation_time:
              Description:
                  Used to calculate lane spacing when spawning vehicles.
              Range:
                  Greater than or equal to `0.0`
              Required:
                  No, will use default 0 values
        target_separation_time:
              Description:
                  Used to calculate longitudinal distance vehicles try to maintain between each other
              Range:
                  Greater than or equal to 0
              Required:
                  No, will use default 0 values
        vehicle_aggression:
              Description:
                  Specifies how aggressive vehicle should be (i.e. aggressive lane changes, turns).
                  Specifically, this is the amount the target speed is increased by.
              Range:
                  Greater than or equal to 0
              Required:
                  No, will use default 0 values
        ignore_obstacle_types:
              Description:
                  Specifies whether vehicle should ignore obstacle types
              Required:
                  No, if not specified will not ignore any obstacles
"""
    _proto_message = pd_unified_generator_pb2.VehicleBehavior

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.VehicleBehavior]=None, enable_dynamic_lane_selection: Optional[bool]=None, ignore_obstacle_types: Optional[List[ObstacleType]]=None, ignore_speed_limit: Optional[bool]=None, lane_change_cooldown: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, lane_change_probability: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, lane_drift_amplitude: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, lane_drift_scale: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, lane_offset: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, start_gear: Optional[Gear]=None, start_separation_time: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, start_speed: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, target_separation_time: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, target_speed: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, vehicle_aggression: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None, vehicle_behavior_type: Optional[VehicleBehaviorType]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleBehavior()
        self.proto = proto
        self._ignore_obstacle_types = ProtoListWrapper(container=[int(v) for v in proto.ignore_obstacle_types], attr_name='ignore_obstacle_types', list_owner=proto)
        self._lane_change_cooldown = get_wrapper(proto_type=proto.lane_change_cooldown.__class__)(proto=proto.lane_change_cooldown)
        self._lane_change_probability = get_wrapper(proto_type=proto.lane_change_probability.__class__)(proto=proto.lane_change_probability)
        self._lane_drift_amplitude = get_wrapper(proto_type=proto.lane_drift_amplitude.__class__)(proto=proto.lane_drift_amplitude)
        self._lane_drift_scale = get_wrapper(proto_type=proto.lane_drift_scale.__class__)(proto=proto.lane_drift_scale)
        self._lane_offset = get_wrapper(proto_type=proto.lane_offset.__class__)(proto=proto.lane_offset)
        self._start_separation_time = get_wrapper(proto_type=proto.start_separation_time.__class__)(proto=proto.start_separation_time)
        self._start_speed = get_wrapper(proto_type=proto.start_speed.__class__)(proto=proto.start_speed)
        self._target_separation_time = get_wrapper(proto_type=proto.target_separation_time.__class__)(proto=proto.target_separation_time)
        self._target_speed = get_wrapper(proto_type=proto.target_speed.__class__)(proto=proto.target_speed)
        self._vehicle_aggression = get_wrapper(proto_type=proto.vehicle_aggression.__class__)(proto=proto.vehicle_aggression)
        if enable_dynamic_lane_selection is not None:
            self.enable_dynamic_lane_selection = enable_dynamic_lane_selection
        if ignore_obstacle_types is not None:
            self.ignore_obstacle_types = ignore_obstacle_types
        if ignore_speed_limit is not None:
            self.ignore_speed_limit = ignore_speed_limit
        if lane_change_cooldown is not None:
            self.lane_change_cooldown = lane_change_cooldown
        if lane_change_probability is not None:
            self.lane_change_probability = lane_change_probability
        if lane_drift_amplitude is not None:
            self.lane_drift_amplitude = lane_drift_amplitude
        if lane_drift_scale is not None:
            self.lane_drift_scale = lane_drift_scale
        if lane_offset is not None:
            self.lane_offset = lane_offset
        if start_gear is not None:
            self.start_gear = start_gear
        if start_separation_time is not None:
            self.start_separation_time = start_separation_time
        if start_speed is not None:
            self.start_speed = start_speed
        if target_separation_time is not None:
            self.target_separation_time = target_separation_time
        if target_speed is not None:
            self.target_speed = target_speed
        if vehicle_aggression is not None:
            self.vehicle_aggression = vehicle_aggression
        if vehicle_behavior_type is not None:
            self.vehicle_behavior_type = vehicle_behavior_type

    @property
    def enable_dynamic_lane_selection(self) -> bool:
        return self.proto.enable_dynamic_lane_selection

    @enable_dynamic_lane_selection.setter
    def enable_dynamic_lane_selection(self, value: bool):
        self.proto.enable_dynamic_lane_selection = value

    @property
    def ignore_obstacle_types(self) -> int:
        return self._ignore_obstacle_types

    @ignore_obstacle_types.setter
    def ignore_obstacle_types(self, value: int):
        self._ignore_obstacle_types.clear()
        for v in value:
            self._ignore_obstacle_types.append(v)

    @property
    def ignore_speed_limit(self) -> bool:
        return self.proto.ignore_speed_limit

    @ignore_speed_limit.setter
    def ignore_speed_limit(self, value: bool):
        self.proto.ignore_speed_limit = value

    @property
    def lane_change_cooldown(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_change_cooldown

    @lane_change_cooldown.setter
    def lane_change_cooldown(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._lane_change_cooldown.proto.CopyFrom(value.proto)

    @property
    def lane_change_probability(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_change_probability

    @lane_change_probability.setter
    def lane_change_probability(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._lane_change_probability.proto.CopyFrom(value.proto)

    @property
    def lane_drift_amplitude(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_drift_amplitude

    @lane_drift_amplitude.setter
    def lane_drift_amplitude(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._lane_drift_amplitude.proto.CopyFrom(value.proto)

    @property
    def lane_drift_scale(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_drift_scale

    @lane_drift_scale.setter
    def lane_drift_scale(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._lane_drift_scale.proto.CopyFrom(value.proto)

    @property
    def lane_offset(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._lane_offset

    @lane_offset.setter
    def lane_offset(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._lane_offset.proto.CopyFrom(value.proto)

    @property
    def start_gear(self) -> int:
        return self.proto.start_gear

    @start_gear.setter
    def start_gear(self, value: int):
        self.proto.start_gear = value

    @property
    def start_separation_time(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._start_separation_time

    @start_separation_time.setter
    def start_separation_time(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._start_separation_time.proto.CopyFrom(value.proto)

    @property
    def start_speed(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._start_speed

    @start_speed.setter
    def start_speed(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._start_speed.proto.CopyFrom(value.proto)

    @property
    def target_separation_time(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._target_separation_time

    @target_separation_time.setter
    def target_separation_time(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._target_separation_time.proto.CopyFrom(value.proto)

    @property
    def target_speed(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._target_speed

    @target_speed.setter
    def target_speed(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._target_speed.proto.CopyFrom(value.proto)

    @property
    def vehicle_aggression(self) -> _pd_distributions_pb2.ContinousUniformDistribution:
        return self._vehicle_aggression

    @vehicle_aggression.setter
    def vehicle_aggression(self, value: _pd_distributions_pb2.ContinousUniformDistribution):
        self._vehicle_aggression.proto.CopyFrom(value.proto)

    @property
    def vehicle_behavior_type(self) -> int:
        return self.proto.vehicle_behavior_type

    @vehicle_behavior_type.setter
    def vehicle_behavior_type(self, value: int):
        self.proto.vehicle_behavior_type = value

@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleGeneratorParameters)
class VehicleGeneratorParameters(AtomicGeneratorMessage):
    """
    Description: Places a single vehicle into the world. Requires ego atomic.

    Args:
        model:
              Description:
                  Vehicle asset name we want to spawn. Vehicle model must be in asset registry.
              Required:
                  Yes
        position_request:
              Description:
                  Determines where the vehicle will spawn
              Required:
                  Yes
        vehicle_spawn_data:
              Description:
                  Controls the single vehicle's spawning characteristics and movement behavior
              Required:
                  No, will use defaults specified in `VehicleSpawnData`
"""
    _proto_message = pd_unified_generator_pb2.VehicleGeneratorParameters

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.VehicleGeneratorParameters]=None, model: Optional[str]=None, position_request: Optional[PositionRequest]=None, vehicle_spawn_data: Optional[VehicleSpawnData]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleGeneratorParameters()
        self.proto = proto
        self._position_request = get_wrapper(proto_type=proto.position_request.__class__)(proto=proto.position_request)
        self._vehicle_spawn_data = get_wrapper(proto_type=proto.vehicle_spawn_data.__class__)(proto=proto.vehicle_spawn_data)
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
        self._position_request.proto.CopyFrom(value.proto)

    @property
    def vehicle_spawn_data(self) -> VehicleSpawnData:
        return self._vehicle_spawn_data

    @vehicle_spawn_data.setter
    def vehicle_spawn_data(self, value: VehicleSpawnData):
        self._vehicle_spawn_data.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.VehiclePeripheral)
class VehiclePeripheral(ProtoMessageClass):
    """
    Description: This contains parameters that control vehicle peripheral behavior (i.e. accessory data, color, occupants, etc.)

    Args:
        spawn_trailer_probability:
              `[0.0-1.0]` chance of spawning with articulated trailer attached
        trailer_initial_yaw:
              Trailer angle when spawned, in radians
        disable_occupants:
              Disables occupants in vehicles
        disable_accessories:
              Not implemented yet
        randomize_vehicle_parts:
              Toggle for blueprint feature to randomize color based on agent id
        emergency_light_probability:
              Chance of turning on emergency lights for police/service vehicles
              Ignored if the vehicle has no emergency lights
"""
    _proto_message = pd_unified_generator_pb2.VehiclePeripheral

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.VehiclePeripheral]=None, disable_accessories: Optional[bool]=None, disable_occupants: Optional[bool]=None, emergency_light_probability: Optional[float]=None, randomize_vehicle_parts: Optional[bool]=None, spawn_trailer_probability: Optional[float]=None, trailer_initial_yaw: Optional[_pd_distributions_pb2.ContinousUniformDistribution]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.VehiclePeripheral()
        self.proto = proto
        self._trailer_initial_yaw = get_wrapper(proto_type=proto.trailer_initial_yaw.__class__)(proto=proto.trailer_initial_yaw)
        if disable_accessories is not None:
            self.disable_accessories = disable_accessories
        if disable_occupants is not None:
            self.disable_occupants = disable_occupants
        if emergency_light_probability is not None:
            self.emergency_light_probability = emergency_light_probability
        if randomize_vehicle_parts is not None:
            self.randomize_vehicle_parts = randomize_vehicle_parts
        if spawn_trailer_probability is not None:
            self.spawn_trailer_probability = spawn_trailer_probability
        if trailer_initial_yaw is not None:
            self.trailer_initial_yaw = trailer_initial_yaw

    @property
    def disable_accessories(self) -> bool:
        return self.proto.disable_accessories

    @disable_accessories.setter
    def disable_accessories(self, value: bool):
        self.proto.disable_accessories = value

    @property
    def disable_occupants(self) -> bool:
        return self.proto.disable_occupants

    @disable_occupants.setter
    def disable_occupants(self, value: bool):
        self.proto.disable_occupants = value

    @property
    def emergency_light_probability(self) -> float:
        return self.proto.emergency_light_probability

    @emergency_light_probability.setter
    def emergency_light_probability(self, value: float):
        self.proto.emergency_light_probability = value

    @property
    def randomize_vehicle_parts(self) -> bool:
        return self.proto.randomize_vehicle_parts

    @randomize_vehicle_parts.setter
    def randomize_vehicle_parts(self, value: bool):
        self.proto.randomize_vehicle_parts = value

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
        self._trailer_initial_yaw.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleSpawnData)
class VehicleSpawnData(ProtoMessageClass):
    """
    Description: Controls the vehicle's spawning characteristics and movement behavior

    Args:
        vehicle_behavior:
              Description:
                  Specifies parameters that control vehicle behavior (i.e. lane change, speed, etc.)
              Required:
                  No
        vehicle_peripheral:
              Description:
                  Specifies that control vehicle peripheral behavior (i.e. accessory data, color, occupants, etc.)
              Required:
                  No
        agent_spawn_data:
              Description:
                  Specifies spawn data that applies across agent types
              Required:
                  No
        prevent_spawn_in_redlight:
              Description:
                  Specified if vehicle should be prevented from spawning in a junction lane that has a red light at the start of scenario
              Required:
                  No, will use default value
"""
    _proto_message = pd_unified_generator_pb2.VehicleSpawnData

    def __init__(self, *, proto: Optional[pd_unified_generator_pb2.VehicleSpawnData]=None, agent_spawn_data: Optional[AgentSpawnData]=None, prevent_spawn_in_redlight: Optional[bool]=None, vehicle_behavior: Optional[VehicleBehavior]=None, vehicle_peripheral: Optional[VehiclePeripheral]=None):
        if proto is None:
            proto = pd_unified_generator_pb2.VehicleSpawnData()
        self.proto = proto
        self._agent_spawn_data = get_wrapper(proto_type=proto.agent_spawn_data.__class__)(proto=proto.agent_spawn_data)
        self._vehicle_behavior = get_wrapper(proto_type=proto.vehicle_behavior.__class__)(proto=proto.vehicle_behavior)
        self._vehicle_peripheral = get_wrapper(proto_type=proto.vehicle_peripheral.__class__)(proto=proto.vehicle_peripheral)
        if agent_spawn_data is not None:
            self.agent_spawn_data = agent_spawn_data
        if prevent_spawn_in_redlight is not None:
            self.prevent_spawn_in_redlight = prevent_spawn_in_redlight
        if vehicle_behavior is not None:
            self.vehicle_behavior = vehicle_behavior
        if vehicle_peripheral is not None:
            self.vehicle_peripheral = vehicle_peripheral

    @property
    def agent_spawn_data(self) -> AgentSpawnData:
        return self._agent_spawn_data

    @agent_spawn_data.setter
    def agent_spawn_data(self, value: AgentSpawnData):
        self._agent_spawn_data.proto.CopyFrom(value.proto)

    @property
    def prevent_spawn_in_redlight(self) -> bool:
        return self.proto.prevent_spawn_in_redlight

    @prevent_spawn_in_redlight.setter
    def prevent_spawn_in_redlight(self, value: bool):
        self.proto.prevent_spawn_in_redlight = value

    @property
    def vehicle_behavior(self) -> VehicleBehavior:
        return self._vehicle_behavior

    @vehicle_behavior.setter
    def vehicle_behavior(self, value: VehicleBehavior):
        self._vehicle_behavior.proto.CopyFrom(value.proto)

    @property
    def vehicle_peripheral(self) -> VehiclePeripheral:
        return self._vehicle_peripheral

    @vehicle_peripheral.setter
    def vehicle_peripheral(self, value: VehiclePeripheral):
        self._vehicle_peripheral.proto.CopyFrom(value.proto)

@register_wrapper(proto_type=pd_unified_generator_pb2.AgentType)
class AgentType(ProtoEnumClass):
    _proto_message = pd_unified_generator_pb2.AgentType
    ANIMAL: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.ANIMAL
    DRONE: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.DRONE
    PARKED_VEHICLE: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.PARKED_VEHICLE
    PEDESTRIAN: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.PEDESTRIAN
    STATIC_OBJECT: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.STATIC_OBJECT
    TRAILER_VEHICLE: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.TRAILER_VEHICLE
    UNSPECIFIED: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.UNSPECIFIED
    VEHICLE: pd_unified_generator_pb2.AgentType = pd_unified_generator_pb2.AgentType.VEHICLE

@register_wrapper(proto_type=pd_unified_generator_pb2.ObstacleType)
class ObstacleType(ProtoEnumClass):
    """
    Description: This contains the different obstacle types

    Args:
"""
    _proto_message = pd_unified_generator_pb2.ObstacleType
    BLOCKED_LANE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.BLOCKED_LANE
    CROSSTRAFFIC: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.CROSSTRAFFIC
    END_OF_LANE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.END_OF_LANE
    FORWARD_AGENT: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.FORWARD_AGENT
    LANE_CLOSURE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.LANE_CLOSURE
    LINEAR_MOVER: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.LINEAR_MOVER
    MERGE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.MERGE
    ONCOMING_AGENT: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.ONCOMING_AGENT
    PATH_END: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.PATH_END
    REVERSE_DISTANCE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.REVERSE_DISTANCE
    ROUTE_LENGTH: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.ROUTE_LENGTH
    STOP_LINE: pd_unified_generator_pb2.ObstacleType = pd_unified_generator_pb2.ObstacleType.STOP_LINE

@register_wrapper(proto_type=pd_unified_generator_pb2.Gear)
class Gear(ProtoEnumClass):
    """
    Description: This contains the different types of gears for vehicles

    Args:
"""
    _proto_message = pd_unified_generator_pb2.Gear
    DRIVE: pd_unified_generator_pb2.Gear = pd_unified_generator_pb2.Gear.DRIVE
    NEUTRAL: pd_unified_generator_pb2.Gear = pd_unified_generator_pb2.Gear.NEUTRAL
    PARKED: pd_unified_generator_pb2.Gear = pd_unified_generator_pb2.Gear.PARKED
    REVERSE: pd_unified_generator_pb2.Gear = pd_unified_generator_pb2.Gear.REVERSE

@register_wrapper(proto_type=pd_unified_generator_pb2.VehicleBehaviorType)
class VehicleBehaviorType(ProtoEnumClass):
    """
    Enum to drive vehicle behavior

    Args:
        DEFAULT:
              Normal behavior of lane following
        OFF:
              Stopped, engine off, lights off
        PARKING:
              Will try to park if spawned in appropriate location for parking
"""
    _proto_message = pd_unified_generator_pb2.VehicleBehaviorType
    DEFAULT: pd_unified_generator_pb2.VehicleBehaviorType = pd_unified_generator_pb2.VehicleBehaviorType.DEFAULT
    OFF: pd_unified_generator_pb2.VehicleBehaviorType = pd_unified_generator_pb2.VehicleBehaviorType.OFF
    PARKING: pd_unified_generator_pb2.VehicleBehaviorType = pd_unified_generator_pb2.VehicleBehaviorType.PARKING

@register_wrapper(proto_type=pd_unified_generator_pb2.PedestrianBehavior)
class PedestrianBehavior(ProtoEnumClass):
    """
    Description: This contains parameters that control pedestrian behavior

    Args:
        NORMAL:
              Description: Walks on sidewalks/crosswalks and only crosses roads at crosswalks
        STATIC:
              Description: Stays in place
        JAYWALKER:
              Description: Jaywalking behavior (e.g. crosses the road at a non-crosswalk)
"""
    _proto_message = pd_unified_generator_pb2.PedestrianBehavior
    JAYWALKER: pd_unified_generator_pb2.PedestrianBehavior = pd_unified_generator_pb2.PedestrianBehavior.JAYWALKER
    NORMAL: pd_unified_generator_pb2.PedestrianBehavior = pd_unified_generator_pb2.PedestrianBehavior.NORMAL
    STATIC: pd_unified_generator_pb2.PedestrianBehavior = pd_unified_generator_pb2.PedestrianBehavior.STATIC

@register_wrapper(proto_type=pd_unified_generator_pb2.SpecialAgentTag)
class SpecialAgentTag(ProtoEnumClass):
    """
    Special Tag used in relative position requests.

    Args:
"""
    _proto_message = pd_unified_generator_pb2.SpecialAgentTag
    EGO: pd_unified_generator_pb2.SpecialAgentTag = pd_unified_generator_pb2.SpecialAgentTag.EGO
    STAR: pd_unified_generator_pb2.SpecialAgentTag = pd_unified_generator_pb2.SpecialAgentTag.STAR