from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_scenario_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_scenario_pb2.AgentTag)
class AgentTag(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.AgentTag

    def __init__(self, *, proto: Optional[pd_scenario_pb2.AgentTag]=None, agent_id: Optional[int]=None, tags: Optional[List[str]]=None):
        if proto is None:
            proto = pd_scenario_pb2.AgentTag()
        self.proto = proto
        self._tags = ProtoListWrapper(container=[str(v) for v in proto.tags], attr_name='tags', list_owner=self)
        if agent_id is not None:
            self.agent_id = agent_id
        if tags is not None:
            self.tags = tags

    @property
    def agent_id(self) -> int:
        return self.proto.agent_id

    @agent_id.setter
    def agent_id(self, value: int):
        self.proto.agent_id = value

    @property
    def tags(self) -> List[str]:
        return self._tags

    @tags.setter
    def tags(self, value: List[str]):
        self._tags.clear()
        for v in value:
            self._tags.append(v)

    def _update_proto_references(self, proto: pd_scenario_pb2.AgentTag):
        self.proto = proto

@register_wrapper(proto_type=pd_scenario_pb2.LinearMover)
class LinearMover(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.LinearMover

    def __init__(self, *, proto: Optional[pd_scenario_pb2.LinearMover]=None, agent_id: Optional[int]=None, model: Optional[str]=None, orient_to_velocity: Optional[bool]=None, origin: Optional[List[float]]=None, rotation: Optional[List[float]]=None, velocity_keys: Optional[List[VelocityKey]]=None):
        if proto is None:
            proto = pd_scenario_pb2.LinearMover()
        self.proto = proto
        self._origin = ProtoListWrapper(container=[float(v) for v in proto.origin], attr_name='origin', list_owner=self)
        self._rotation = ProtoListWrapper(container=[float(v) for v in proto.rotation], attr_name='rotation', list_owner=self)
        self._velocity_keys = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.velocity_keys], attr_name='velocity_keys', list_owner=self)
        if agent_id is not None:
            self.agent_id = agent_id
        if model is not None:
            self.model = model
        if orient_to_velocity is not None:
            self.orient_to_velocity = orient_to_velocity
        if origin is not None:
            self.origin = origin
        if rotation is not None:
            self.rotation = rotation
        if velocity_keys is not None:
            self.velocity_keys = velocity_keys

    @property
    def agent_id(self) -> int:
        return self.proto.agent_id

    @agent_id.setter
    def agent_id(self, value: int):
        self.proto.agent_id = value

    @property
    def model(self) -> str:
        return self.proto.model

    @model.setter
    def model(self, value: str):
        self.proto.model = value

    @property
    def orient_to_velocity(self) -> bool:
        return self.proto.orient_to_velocity

    @orient_to_velocity.setter
    def orient_to_velocity(self, value: bool):
        self.proto.orient_to_velocity = value

    @property
    def origin(self) -> List[float]:
        return self._origin

    @origin.setter
    def origin(self, value: List[float]):
        self._origin.clear()
        for v in value:
            self._origin.append(v)

    @property
    def rotation(self) -> List[float]:
        return self._rotation

    @rotation.setter
    def rotation(self, value: List[float]):
        self._rotation.clear()
        for v in value:
            self._rotation.append(v)

    @property
    def velocity_keys(self) -> List[VelocityKey]:
        return self._velocity_keys

    @velocity_keys.setter
    def velocity_keys(self, value: List[VelocityKey]):
        self._velocity_keys.clear()
        for v in value:
            self._velocity_keys.append(v)

    def _update_proto_references(self, proto: pd_scenario_pb2.LinearMover):
        self.proto = proto
        for i, v in enumerate(self.velocity_keys):
            v._update_proto_references(self.proto.velocity_keys[i])

@register_wrapper(proto_type=pd_scenario_pb2.ScenarioDefinition)
class ScenarioDefinition(ProtoMessageClass):

    @register_wrapper(proto_type=pd_scenario_pb2.ScenarioDefinition.PerformanceFeature)
    class PerformanceFeature(ProtoEnumClass):
        _proto_message = pd_scenario_pb2.ScenarioDefinition.PerformanceFeature
    _proto_message = pd_scenario_pb2.ScenarioDefinition

    def __init__(self, *, proto: Optional[pd_scenario_pb2.ScenarioDefinition]=None, HighFidelityMode: Optional[ScenarioDefinition.PerformanceFeature]=None, PerformanceMode: Optional[ScenarioDefinition.PerformanceFeature]=None, agent_tags: Optional[List[AgentTag]]=None, anti_aliasing: Optional[int]=None, config_blob: Optional[str]=None, current_time: Optional[float]=None, fog_intensity: Optional[float]=None, headlights: Optional[bool]=None, lighting: Optional[str]=None, linear_movers: Optional[List[LinearMover]]=None, name: Optional[str]=None, num_frames: Optional[int]=None, output_frame_skip: Optional[int]=None, performance_feature: Optional[ScenarioDefinition.PerformanceFeature]=None, rain_intensity: Optional[float]=None, sensors: Optional[List[Sensor]]=None, sim_update_time: Optional[float]=None, skip_frames: Optional[int]=None, street_lights: Optional[float]=None, vehicles: Optional[List[Vehicle]]=None, wetness: Optional[float]=None, world: Optional[str]=None):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioDefinition()
        self.proto = proto
        self._agent_tags = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.agent_tags], attr_name='agent_tags', list_owner=self)
        self._linear_movers = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.linear_movers], attr_name='linear_movers', list_owner=self)
        self._sensors = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensors], attr_name='sensors', list_owner=self)
        self._vehicles = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.vehicles], attr_name='vehicles', list_owner=self)
        if HighFidelityMode is not None:
            self.HighFidelityMode = HighFidelityMode
        if PerformanceMode is not None:
            self.PerformanceMode = PerformanceMode
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if anti_aliasing is not None:
            self.anti_aliasing = anti_aliasing
        if config_blob is not None:
            self.config_blob = config_blob
        if current_time is not None:
            self.current_time = current_time
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if headlights is not None:
            self.headlights = headlights
        if lighting is not None:
            self.lighting = lighting
        if linear_movers is not None:
            self.linear_movers = linear_movers
        if name is not None:
            self.name = name
        if num_frames is not None:
            self.num_frames = num_frames
        if output_frame_skip is not None:
            self.output_frame_skip = output_frame_skip
        if performance_feature is not None:
            self.performance_feature = performance_feature
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if sensors is not None:
            self.sensors = sensors
        if sim_update_time is not None:
            self.sim_update_time = sim_update_time
        if skip_frames is not None:
            self.skip_frames = skip_frames
        if street_lights is not None:
            self.street_lights = street_lights
        if vehicles is not None:
            self.vehicles = vehicles
        if wetness is not None:
            self.wetness = wetness
        if world is not None:
            self.world = world

    @property
    def HighFidelityMode(self) -> int:
        return self.proto.HighFidelityMode

    @HighFidelityMode.setter
    def HighFidelityMode(self, value: int):
        self.proto.HighFidelityMode = value

    @property
    def PerformanceMode(self) -> int:
        return self.proto.PerformanceMode

    @PerformanceMode.setter
    def PerformanceMode(self, value: int):
        self.proto.PerformanceMode = value

    @property
    def agent_tags(self) -> List[AgentTag]:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: List[AgentTag]):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    @property
    def anti_aliasing(self) -> int:
        return self.proto.anti_aliasing

    @anti_aliasing.setter
    def anti_aliasing(self, value: int):
        self.proto.anti_aliasing = value

    @property
    def config_blob(self) -> str:
        return self.proto.config_blob

    @config_blob.setter
    def config_blob(self, value: str):
        self.proto.config_blob = value

    @property
    def current_time(self) -> float:
        return self.proto.current_time

    @current_time.setter
    def current_time(self, value: float):
        self.proto.current_time = value

    @property
    def fog_intensity(self) -> float:
        return self.proto.fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: float):
        self.proto.fog_intensity = value

    @property
    def headlights(self) -> bool:
        return self.proto.headlights

    @headlights.setter
    def headlights(self, value: bool):
        self.proto.headlights = value

    @property
    def lighting(self) -> str:
        return self.proto.lighting

    @lighting.setter
    def lighting(self, value: str):
        self.proto.lighting = value

    @property
    def linear_movers(self) -> List[LinearMover]:
        return self._linear_movers

    @linear_movers.setter
    def linear_movers(self, value: List[LinearMover]):
        self._linear_movers.clear()
        for v in value:
            self._linear_movers.append(v)

    @property
    def name(self) -> str:
        return self.proto.name

    @name.setter
    def name(self, value: str):
        self.proto.name = value

    @property
    def num_frames(self) -> int:
        return self.proto.num_frames

    @num_frames.setter
    def num_frames(self, value: int):
        self.proto.num_frames = value

    @property
    def output_frame_skip(self) -> int:
        return self.proto.output_frame_skip

    @output_frame_skip.setter
    def output_frame_skip(self, value: int):
        self.proto.output_frame_skip = value

    @property
    def performance_feature(self) -> int:
        return self.proto.performance_feature

    @performance_feature.setter
    def performance_feature(self, value: int):
        self.proto.performance_feature = value

    @property
    def rain_intensity(self) -> float:
        return self.proto.rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: float):
        self.proto.rain_intensity = value

    @property
    def sensors(self) -> List[Sensor]:
        return self._sensors

    @sensors.setter
    def sensors(self, value: List[Sensor]):
        self._sensors.clear()
        for v in value:
            self._sensors.append(v)

    @property
    def sim_update_time(self) -> float:
        return self.proto.sim_update_time

    @sim_update_time.setter
    def sim_update_time(self, value: float):
        self.proto.sim_update_time = value

    @property
    def skip_frames(self) -> int:
        return self.proto.skip_frames

    @skip_frames.setter
    def skip_frames(self, value: int):
        self.proto.skip_frames = value

    @property
    def street_lights(self) -> float:
        return self.proto.street_lights

    @street_lights.setter
    def street_lights(self, value: float):
        self.proto.street_lights = value

    @property
    def vehicles(self) -> List[Vehicle]:
        return self._vehicles

    @vehicles.setter
    def vehicles(self, value: List[Vehicle]):
        self._vehicles.clear()
        for v in value:
            self._vehicles.append(v)

    @property
    def wetness(self) -> float:
        return self.proto.wetness

    @wetness.setter
    def wetness(self, value: float):
        self.proto.wetness = value

    @property
    def world(self) -> str:
        return self.proto.world

    @world.setter
    def world(self, value: str):
        self.proto.world = value

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioDefinition):
        self.proto = proto
        for i, v in enumerate(self.agent_tags):
            v._update_proto_references(self.proto.agent_tags[i])
        for i, v in enumerate(self.linear_movers):
            v._update_proto_references(self.proto.linear_movers[i])
        for i, v in enumerate(self.sensors):
            v._update_proto_references(self.proto.sensors[i])
        for i, v in enumerate(self.vehicles):
            v._update_proto_references(self.proto.vehicles[i])

@register_wrapper(proto_type=pd_scenario_pb2.ScenarioGenConfig)
class ScenarioGenConfig(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.ScenarioGenConfig

    def __init__(self, *, proto: Optional[pd_scenario_pb2.ScenarioGenConfig]=None, batch_size: Optional[int]=None, check_offroad_vehicles: Optional[bool]=None, end_skip_frames: Optional[int]=None, environment: Optional[_pd_environments_pb2.EnvironmentDefinition]=None, merge_batches: Optional[bool]=None, num_frames: Optional[int]=None, output_offset: Optional[int]=None, scenario_seed: Optional[int]=None, sim_capture_rate: Optional[int]=None, sim_settle_frames: Optional[int]=None, sim_terminate_on_collision_within_radius_m: Optional[float]=None, sim_terminate_on_drone_flight_path_end: Optional[bool]=None, sim_terminate_on_pedestrian_collision_within_radius_m: Optional[float]=None, sim_update_time: Optional[float]=None, spawn_config: Optional[_pd_spawn_pb2.SpawnConfig]=None, start_skip_frames: Optional[int]=None):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioGenConfig()
        self.proto = proto
        self._environment = get_wrapper(proto_type=proto.environment.__class__)(proto=proto.environment)
        self._spawn_config = get_wrapper(proto_type=proto.spawn_config.__class__)(proto=proto.spawn_config)
        if batch_size is not None:
            self.batch_size = batch_size
        if check_offroad_vehicles is not None:
            self.check_offroad_vehicles = check_offroad_vehicles
        if end_skip_frames is not None:
            self.end_skip_frames = end_skip_frames
        if environment is not None:
            self.environment = environment
        if merge_batches is not None:
            self.merge_batches = merge_batches
        if num_frames is not None:
            self.num_frames = num_frames
        if output_offset is not None:
            self.output_offset = output_offset
        if scenario_seed is not None:
            self.scenario_seed = scenario_seed
        if sim_capture_rate is not None:
            self.sim_capture_rate = sim_capture_rate
        if sim_settle_frames is not None:
            self.sim_settle_frames = sim_settle_frames
        if sim_terminate_on_collision_within_radius_m is not None:
            self.sim_terminate_on_collision_within_radius_m = sim_terminate_on_collision_within_radius_m
        if sim_terminate_on_drone_flight_path_end is not None:
            self.sim_terminate_on_drone_flight_path_end = sim_terminate_on_drone_flight_path_end
        if sim_terminate_on_pedestrian_collision_within_radius_m is not None:
            self.sim_terminate_on_pedestrian_collision_within_radius_m = sim_terminate_on_pedestrian_collision_within_radius_m
        if sim_update_time is not None:
            self.sim_update_time = sim_update_time
        if spawn_config is not None:
            self.spawn_config = spawn_config
        if start_skip_frames is not None:
            self.start_skip_frames = start_skip_frames

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def check_offroad_vehicles(self) -> bool:
        return self.proto.check_offroad_vehicles

    @check_offroad_vehicles.setter
    def check_offroad_vehicles(self, value: bool):
        self.proto.check_offroad_vehicles = value

    @property
    def end_skip_frames(self) -> int:
        return self.proto.end_skip_frames

    @end_skip_frames.setter
    def end_skip_frames(self, value: int):
        self.proto.end_skip_frames = value

    @property
    def environment(self) -> _pd_environments_pb2.EnvironmentDefinition:
        return self._environment

    @environment.setter
    def environment(self, value: _pd_environments_pb2.EnvironmentDefinition):
        self.proto.environment.CopyFrom(value.proto)
        
        self._environment = value
        self._environment._update_proto_references(self.proto.environment)

    @property
    def merge_batches(self) -> bool:
        return self.proto.merge_batches

    @merge_batches.setter
    def merge_batches(self, value: bool):
        self.proto.merge_batches = value

    @property
    def num_frames(self) -> int:
        return self.proto.num_frames

    @num_frames.setter
    def num_frames(self, value: int):
        self.proto.num_frames = value

    @property
    def output_offset(self) -> int:
        return self.proto.output_offset

    @output_offset.setter
    def output_offset(self, value: int):
        self.proto.output_offset = value

    @property
    def scenario_seed(self) -> int:
        return self.proto.scenario_seed

    @scenario_seed.setter
    def scenario_seed(self, value: int):
        self.proto.scenario_seed = value

    @property
    def sim_capture_rate(self) -> int:
        return self.proto.sim_capture_rate

    @sim_capture_rate.setter
    def sim_capture_rate(self, value: int):
        self.proto.sim_capture_rate = value

    @property
    def sim_settle_frames(self) -> int:
        return self.proto.sim_settle_frames

    @sim_settle_frames.setter
    def sim_settle_frames(self, value: int):
        self.proto.sim_settle_frames = value

    @property
    def sim_terminate_on_collision_within_radius_m(self) -> float:
        return self.proto.sim_terminate_on_collision_within_radius_m

    @sim_terminate_on_collision_within_radius_m.setter
    def sim_terminate_on_collision_within_radius_m(self, value: float):
        self.proto.sim_terminate_on_collision_within_radius_m = value

    @property
    def sim_terminate_on_drone_flight_path_end(self) -> bool:
        return self.proto.sim_terminate_on_drone_flight_path_end

    @sim_terminate_on_drone_flight_path_end.setter
    def sim_terminate_on_drone_flight_path_end(self, value: bool):
        self.proto.sim_terminate_on_drone_flight_path_end = value

    @property
    def sim_terminate_on_pedestrian_collision_within_radius_m(self) -> float:
        return self.proto.sim_terminate_on_pedestrian_collision_within_radius_m

    @sim_terminate_on_pedestrian_collision_within_radius_m.setter
    def sim_terminate_on_pedestrian_collision_within_radius_m(self, value: float):
        self.proto.sim_terminate_on_pedestrian_collision_within_radius_m = value

    @property
    def sim_update_time(self) -> float:
        return self.proto.sim_update_time

    @sim_update_time.setter
    def sim_update_time(self, value: float):
        self.proto.sim_update_time = value

    @property
    def spawn_config(self) -> _pd_spawn_pb2.SpawnConfig:
        return self._spawn_config

    @spawn_config.setter
    def spawn_config(self, value: _pd_spawn_pb2.SpawnConfig):
        self.proto.spawn_config.CopyFrom(value.proto)
        
        self._spawn_config = value
        self._spawn_config._update_proto_references(self.proto.spawn_config)

    @property
    def start_skip_frames(self) -> int:
        return self.proto.start_skip_frames

    @start_skip_frames.setter
    def start_skip_frames(self, value: int):
        self.proto.start_skip_frames = value

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioGenConfig):
        self.proto = proto
        self._environment._update_proto_references(proto.environment)
        self._spawn_config._update_proto_references(proto.spawn_config)

@register_wrapper(proto_type=pd_scenario_pb2.ScenarioLocation)
class ScenarioLocation(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.ScenarioLocation

    def __init__(self, *, proto: Optional[pd_scenario_pb2.ScenarioLocation]=None, generator_config: Optional[_pd_spawn_pb2.GeneratorConfig]=None, location: Optional[str]=None, location_guid: Optional[str]=None, num_retries: Optional[int]=None, num_scenarios: Optional[int]=None):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioLocation()
        self.proto = proto
        self._generator_config = get_wrapper(proto_type=proto.generator_config.__class__)(proto=proto.generator_config)
        if generator_config is not None:
            self.generator_config = generator_config
        if location is not None:
            self.location = location
        if location_guid is not None:
            self.location_guid = location_guid
        if num_retries is not None:
            self.num_retries = num_retries
        if num_scenarios is not None:
            self.num_scenarios = num_scenarios

    @property
    def generator_config(self) -> _pd_spawn_pb2.GeneratorConfig:
        return self._generator_config

    @generator_config.setter
    def generator_config(self, value: _pd_spawn_pb2.GeneratorConfig):
        self.proto.generator_config.CopyFrom(value.proto)
        
        self._generator_config = value
        self._generator_config._update_proto_references(self.proto.generator_config)

    @property
    def location(self) -> str:
        return self.proto.location

    @location.setter
    def location(self, value: str):
        self.proto.location = value

    @property
    def location_guid(self) -> str:
        return self.proto.location_guid

    @location_guid.setter
    def location_guid(self, value: str):
        self.proto.location_guid = value

    @property
    def num_retries(self) -> int:
        return self.proto.num_retries

    @num_retries.setter
    def num_retries(self, value: int):
        self.proto.num_retries = value

    @property
    def num_scenarios(self) -> int:
        return self.proto.num_scenarios

    @num_scenarios.setter
    def num_scenarios(self, value: int):
        self.proto.num_scenarios = value

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioLocation):
        self.proto = proto
        self._generator_config._update_proto_references(proto.generator_config)

@register_wrapper(proto_type=pd_scenario_pb2.Sensor)
class Sensor(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.Sensor

    def __init__(self, *, proto: Optional[pd_scenario_pb2.Sensor]=None, agent_id: Optional[int]=None, origin: Optional[List[float]]=None, rotation: Optional[List[float]]=None):
        if proto is None:
            proto = pd_scenario_pb2.Sensor()
        self.proto = proto
        self._origin = ProtoListWrapper(container=[float(v) for v in proto.origin], attr_name='origin', list_owner=self)
        self._rotation = ProtoListWrapper(container=[float(v) for v in proto.rotation], attr_name='rotation', list_owner=self)
        if agent_id is not None:
            self.agent_id = agent_id
        if origin is not None:
            self.origin = origin
        if rotation is not None:
            self.rotation = rotation

    @property
    def agent_id(self) -> int:
        return self.proto.agent_id

    @agent_id.setter
    def agent_id(self, value: int):
        self.proto.agent_id = value

    @property
    def origin(self) -> List[float]:
        return self._origin

    @origin.setter
    def origin(self, value: List[float]):
        self._origin.clear()
        for v in value:
            self._origin.append(v)

    @property
    def rotation(self) -> List[float]:
        return self._rotation

    @rotation.setter
    def rotation(self, value: List[float]):
        self._rotation.clear()
        for v in value:
            self._rotation.append(v)

    def _update_proto_references(self, proto: pd_scenario_pb2.Sensor):
        self.proto = proto

@register_wrapper(proto_type=pd_scenario_pb2.Vehicle)
class Vehicle(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.Vehicle

    def __init__(self, *, proto: Optional[pd_scenario_pb2.Vehicle]=None, agent_id: Optional[int]=None, aggression: Optional[float]=None, brake_until_time: Optional[float]=None, color: Optional[str]=None, constant_accelerate: Optional[float]=None, enable_merge_detection: Optional[bool]=None, ignore_obstacles: Optional[bool]=None, ignore_speed_limit: Optional[bool]=None, lane_drift_amp: Optional[float]=None, lane_drift_scale: Optional[float]=None, lane_offset: Optional[float]=None, lane_path: Optional[List[int]]=None, lane_shift_amount: Optional[float]=None, lane_shift_speed: Optional[float]=None, lane_shift_time: Optional[float]=None, position: Optional[List[float]]=None, sensors: Optional[bool]=None, target_separation: Optional[float]=None, target_velocity: Optional[float]=None, vehicle_actor: Optional[str]=None, vehicle_type: Optional[str]=None, velocity: Optional[float]=None):
        if proto is None:
            proto = pd_scenario_pb2.Vehicle()
        self.proto = proto
        self._lane_path = ProtoListWrapper(container=[int(v) for v in proto.lane_path], attr_name='lane_path', list_owner=self)
        self._position = ProtoListWrapper(container=[float(v) for v in proto.position], attr_name='position', list_owner=self)
        if agent_id is not None:
            self.agent_id = agent_id
        if aggression is not None:
            self.aggression = aggression
        if brake_until_time is not None:
            self.brake_until_time = brake_until_time
        if color is not None:
            self.color = color
        if constant_accelerate is not None:
            self.constant_accelerate = constant_accelerate
        if enable_merge_detection is not None:
            self.enable_merge_detection = enable_merge_detection
        if ignore_obstacles is not None:
            self.ignore_obstacles = ignore_obstacles
        if ignore_speed_limit is not None:
            self.ignore_speed_limit = ignore_speed_limit
        if lane_drift_amp is not None:
            self.lane_drift_amp = lane_drift_amp
        if lane_drift_scale is not None:
            self.lane_drift_scale = lane_drift_scale
        if lane_offset is not None:
            self.lane_offset = lane_offset
        if lane_path is not None:
            self.lane_path = lane_path
        if lane_shift_amount is not None:
            self.lane_shift_amount = lane_shift_amount
        if lane_shift_speed is not None:
            self.lane_shift_speed = lane_shift_speed
        if lane_shift_time is not None:
            self.lane_shift_time = lane_shift_time
        if position is not None:
            self.position = position
        if sensors is not None:
            self.sensors = sensors
        if target_separation is not None:
            self.target_separation = target_separation
        if target_velocity is not None:
            self.target_velocity = target_velocity
        if vehicle_actor is not None:
            self.vehicle_actor = vehicle_actor
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if velocity is not None:
            self.velocity = velocity

    @property
    def agent_id(self) -> int:
        return self.proto.agent_id

    @agent_id.setter
    def agent_id(self, value: int):
        self.proto.agent_id = value

    @property
    def aggression(self) -> float:
        return self.proto.aggression

    @aggression.setter
    def aggression(self, value: float):
        self.proto.aggression = value

    @property
    def brake_until_time(self) -> float:
        return self.proto.brake_until_time

    @brake_until_time.setter
    def brake_until_time(self, value: float):
        self.proto.brake_until_time = value

    @property
    def color(self) -> str:
        return self.proto.color

    @color.setter
    def color(self, value: str):
        self.proto.color = value

    @property
    def constant_accelerate(self) -> float:
        return self.proto.constant_accelerate

    @constant_accelerate.setter
    def constant_accelerate(self, value: float):
        self.proto.constant_accelerate = value

    @property
    def enable_merge_detection(self) -> bool:
        return self.proto.enable_merge_detection

    @enable_merge_detection.setter
    def enable_merge_detection(self, value: bool):
        self.proto.enable_merge_detection = value

    @property
    def ignore_obstacles(self) -> bool:
        return self.proto.ignore_obstacles

    @ignore_obstacles.setter
    def ignore_obstacles(self, value: bool):
        self.proto.ignore_obstacles = value

    @property
    def ignore_speed_limit(self) -> bool:
        return self.proto.ignore_speed_limit

    @ignore_speed_limit.setter
    def ignore_speed_limit(self, value: bool):
        self.proto.ignore_speed_limit = value

    @property
    def lane_drift_amp(self) -> float:
        return self.proto.lane_drift_amp

    @lane_drift_amp.setter
    def lane_drift_amp(self, value: float):
        self.proto.lane_drift_amp = value

    @property
    def lane_drift_scale(self) -> float:
        return self.proto.lane_drift_scale

    @lane_drift_scale.setter
    def lane_drift_scale(self, value: float):
        self.proto.lane_drift_scale = value

    @property
    def lane_offset(self) -> float:
        return self.proto.lane_offset

    @lane_offset.setter
    def lane_offset(self, value: float):
        self.proto.lane_offset = value

    @property
    def lane_path(self) -> List[int]:
        return self._lane_path

    @lane_path.setter
    def lane_path(self, value: List[int]):
        self._lane_path.clear()
        for v in value:
            self._lane_path.append(v)

    @property
    def lane_shift_amount(self) -> float:
        return self.proto.lane_shift_amount

    @lane_shift_amount.setter
    def lane_shift_amount(self, value: float):
        self.proto.lane_shift_amount = value

    @property
    def lane_shift_speed(self) -> float:
        return self.proto.lane_shift_speed

    @lane_shift_speed.setter
    def lane_shift_speed(self, value: float):
        self.proto.lane_shift_speed = value

    @property
    def lane_shift_time(self) -> float:
        return self.proto.lane_shift_time

    @lane_shift_time.setter
    def lane_shift_time(self, value: float):
        self.proto.lane_shift_time = value

    @property
    def position(self) -> List[float]:
        return self._position

    @position.setter
    def position(self, value: List[float]):
        self._position.clear()
        for v in value:
            self._position.append(v)

    @property
    def sensors(self) -> bool:
        return self.proto.sensors

    @sensors.setter
    def sensors(self, value: bool):
        self.proto.sensors = value

    @property
    def target_separation(self) -> float:
        return self.proto.target_separation

    @target_separation.setter
    def target_separation(self, value: float):
        self.proto.target_separation = value

    @property
    def target_velocity(self) -> float:
        return self.proto.target_velocity

    @target_velocity.setter
    def target_velocity(self, value: float):
        self.proto.target_velocity = value

    @property
    def vehicle_actor(self) -> str:
        return self.proto.vehicle_actor

    @vehicle_actor.setter
    def vehicle_actor(self, value: str):
        self.proto.vehicle_actor = value

    @property
    def vehicle_type(self) -> str:
        return self.proto.vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value: str):
        self.proto.vehicle_type = value

    @property
    def velocity(self) -> float:
        return self.proto.velocity

    @velocity.setter
    def velocity(self, value: float):
        self.proto.velocity = value

    def _update_proto_references(self, proto: pd_scenario_pb2.Vehicle):
        self.proto = proto

@register_wrapper(proto_type=pd_scenario_pb2.VelocityKey)
class VelocityKey(ProtoMessageClass):
    _proto_message = pd_scenario_pb2.VelocityKey

    def __init__(self, *, proto: Optional[pd_scenario_pb2.VelocityKey]=None, t: Optional[float]=None, velocity: Optional[List[float]]=None):
        if proto is None:
            proto = pd_scenario_pb2.VelocityKey()
        self.proto = proto
        self._velocity = ProtoListWrapper(container=[float(v) for v in proto.velocity], attr_name='velocity', list_owner=self)
        if t is not None:
            self.t = t
        if velocity is not None:
            self.velocity = velocity

    @property
    def t(self) -> float:
        return self.proto.t

    @t.setter
    def t(self, value: float):
        self.proto.t = value

    @property
    def velocity(self) -> List[float]:
        return self._velocity

    @velocity.setter
    def velocity(self, value: List[float]):
        self._velocity.clear()
        for v in value:
            self._velocity.append(v)

    def _update_proto_references(self, proto: pd_scenario_pb2.VelocityKey):
        self.proto = proto