from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoEnumClass,
    ProtoListWrapper
)
from ..python import (
    pd_scenario_pb2
)
from . import (
    pd_environments_pb2 as _pd_environments_pb2,
    pd_spawn_pb2 as _pd_spawn_pb2
)


@register_wrapper(proto_type=pd_scenario_pb2.VelocityKey)
class VelocityKey(ProtoMessageClass):
    """
    Args:
        t: :attr:`t`
        velocity: :attr:`velocity`
    Attributes:
        t:
        velocity:"""

    _proto_message = pd_scenario_pb2.VelocityKey

    def __init__(
        self, *, proto: Optional[pd_scenario_pb2.VelocityKey] = None, t: float = None, velocity: List[float] = None
    ):
        if proto is None:
            proto = pd_scenario_pb2.VelocityKey()
        self.proto = proto
        if t is not None:
            self.t = t
        self._velocity = ProtoListWrapper(
            container=[float(v) for v in proto.velocity], attr_name="velocity", list_owner=self
        )
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


@register_wrapper(proto_type=pd_scenario_pb2.LinearMover)
class LinearMover(ProtoMessageClass):
    """
    Args:
        agent_id: :attr:`agent_id`
        model: :attr:`model`
        orient_to_velocity: :attr:`orient_to_velocity`
        origin: :attr:`origin`
        rotation: :attr:`rotation`
        velocity_keys: :attr:`velocity_keys`
    Attributes:
        agent_id:
        model:
        orient_to_velocity:
        origin:
        rotation:
        velocity_keys:"""

    _proto_message = pd_scenario_pb2.LinearMover

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.LinearMover] = None,
        agent_id: int = None,
        model: str = None,
        orient_to_velocity: bool = None,
        origin: List[float] = None,
        rotation: List[float] = None,
        velocity_keys: List[VelocityKey] = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.LinearMover()
        self.proto = proto
        self._velocity_keys = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.velocity_keys],
            attr_name="velocity_keys",
            list_owner=self,
        )
        if agent_id is not None:
            self.agent_id = agent_id
        if model is not None:
            self.model = model
        if orient_to_velocity is not None:
            self.orient_to_velocity = orient_to_velocity
        self._origin = ProtoListWrapper(container=[float(v) for v in proto.origin], attr_name="origin", list_owner=self)
        if origin is not None:
            self.origin = origin
        self._rotation = ProtoListWrapper(
            container=[float(v) for v in proto.rotation], attr_name="rotation", list_owner=self
        )
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


@register_wrapper(proto_type=pd_scenario_pb2.Vehicle)
class Vehicle(ProtoMessageClass):
    """
    Args:
        agent_id: :attr:`agent_id`
        sensors: :attr:`sensors`
        color: :attr:`color`
        vehicle_actor: :attr:`vehicle_actor`
        vehicle_type: :attr:`vehicle_type`
        position: :attr:`position`
        velocity: :attr:`velocity`
        lane_path: :attr:`lane_path`
        target_velocity: :attr:`target_velocity`
        target_separation: :attr:`target_separation`
        aggression: :attr:`aggression`
        lane_drift_amp: :attr:`lane_drift_amp`
        lane_drift_scale: :attr:`lane_drift_scale`
        lane_offset: :attr:`lane_offset`
        lane_shift_amount: :attr:`lane_shift_amount`
        lane_shift_speed: :attr:`lane_shift_speed`
        lane_shift_time: :attr:`lane_shift_time`
        brake_until_time: :attr:`brake_until_time`
        constant_accelerate: :attr:`constant_accelerate`
        enable_merge_detection: :attr:`enable_merge_detection`
        ignore_obstacles: :attr:`ignore_obstacles`
        ignore_speed_limit: :attr:`ignore_speed_limit`
    Attributes:
        agent_id:
        sensors:
        color:
        vehicle_actor:
        vehicle_type:
        position:
        velocity:
        lane_path:
        target_velocity:
        target_separation:
        aggression:
        lane_drift_amp:
        lane_drift_scale:
        lane_offset:
        lane_shift_amount:
        lane_shift_speed:
        lane_shift_time:
        brake_until_time:
        constant_accelerate:
        enable_merge_detection:
        ignore_obstacles:
        ignore_speed_limit:"""

    _proto_message = pd_scenario_pb2.Vehicle

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.Vehicle] = None,
        agent_id: int = None,
        sensors: bool = None,
        color: str = None,
        vehicle_actor: str = None,
        vehicle_type: str = None,
        position: List[float] = None,
        velocity: float = None,
        lane_path: List[int] = None,
        target_velocity: float = None,
        target_separation: float = None,
        aggression: float = None,
        lane_drift_amp: float = None,
        lane_drift_scale: float = None,
        lane_offset: float = None,
        lane_shift_amount: float = None,
        lane_shift_speed: float = None,
        lane_shift_time: float = None,
        brake_until_time: float = None,
        constant_accelerate: float = None,
        enable_merge_detection: bool = None,
        ignore_obstacles: bool = None,
        ignore_speed_limit: bool = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.Vehicle()
        self.proto = proto
        if agent_id is not None:
            self.agent_id = agent_id
        if sensors is not None:
            self.sensors = sensors
        if color is not None:
            self.color = color
        if vehicle_actor is not None:
            self.vehicle_actor = vehicle_actor
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        self._position = ProtoListWrapper(
            container=[float(v) for v in proto.position], attr_name="position", list_owner=self
        )
        if position is not None:
            self.position = position
        if velocity is not None:
            self.velocity = velocity
        self._lane_path = ProtoListWrapper(
            container=[int(v) for v in proto.lane_path], attr_name="lane_path", list_owner=self
        )
        if lane_path is not None:
            self.lane_path = lane_path
        if target_velocity is not None:
            self.target_velocity = target_velocity
        if target_separation is not None:
            self.target_separation = target_separation
        if aggression is not None:
            self.aggression = aggression
        if lane_drift_amp is not None:
            self.lane_drift_amp = lane_drift_amp
        if lane_drift_scale is not None:
            self.lane_drift_scale = lane_drift_scale
        if lane_offset is not None:
            self.lane_offset = lane_offset
        if lane_shift_amount is not None:
            self.lane_shift_amount = lane_shift_amount
        if lane_shift_speed is not None:
            self.lane_shift_speed = lane_shift_speed
        if lane_shift_time is not None:
            self.lane_shift_time = lane_shift_time
        if brake_until_time is not None:
            self.brake_until_time = brake_until_time
        if constant_accelerate is not None:
            self.constant_accelerate = constant_accelerate
        if enable_merge_detection is not None:
            self.enable_merge_detection = enable_merge_detection
        if ignore_obstacles is not None:
            self.ignore_obstacles = ignore_obstacles
        if ignore_speed_limit is not None:
            self.ignore_speed_limit = ignore_speed_limit

    @property
    def agent_id(self) -> int:
        return self.proto.agent_id

    @agent_id.setter
    def agent_id(self, value: int):
        self.proto.agent_id = value

    @property
    def sensors(self) -> bool:
        return self.proto.sensors

    @sensors.setter
    def sensors(self, value: bool):
        self.proto.sensors = value

    @property
    def color(self) -> str:
        return self.proto.color

    @color.setter
    def color(self, value: str):
        self.proto.color = value

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
    def position(self) -> List[float]:
        return self._position

    @position.setter
    def position(self, value: List[float]):
        self._position.clear()
        for v in value:
            self._position.append(v)

    @property
    def velocity(self) -> float:
        return self.proto.velocity

    @velocity.setter
    def velocity(self, value: float):
        self.proto.velocity = value

    @property
    def lane_path(self) -> List[int]:
        return self._lane_path

    @lane_path.setter
    def lane_path(self, value: List[int]):
        self._lane_path.clear()
        for v in value:
            self._lane_path.append(v)

    @property
    def target_velocity(self) -> float:
        return self.proto.target_velocity

    @target_velocity.setter
    def target_velocity(self, value: float):
        self.proto.target_velocity = value

    @property
    def target_separation(self) -> float:
        return self.proto.target_separation

    @target_separation.setter
    def target_separation(self, value: float):
        self.proto.target_separation = value

    @property
    def aggression(self) -> float:
        return self.proto.aggression

    @aggression.setter
    def aggression(self, value: float):
        self.proto.aggression = value

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
    def brake_until_time(self) -> float:
        return self.proto.brake_until_time

    @brake_until_time.setter
    def brake_until_time(self, value: float):
        self.proto.brake_until_time = value

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

    def _update_proto_references(self, proto: pd_scenario_pb2.Vehicle):
        self.proto = proto


@register_wrapper(proto_type=pd_scenario_pb2.Sensor)
class Sensor(ProtoMessageClass):
    """
    Args:
        agent_id: :attr:`agent_id`
        origin: :attr:`origin`
        rotation: :attr:`rotation`
    Attributes:
        agent_id:
        origin:
        rotation:"""

    _proto_message = pd_scenario_pb2.Sensor

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.Sensor] = None,
        agent_id: int = None,
        origin: List[float] = None,
        rotation: List[float] = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.Sensor()
        self.proto = proto
        if agent_id is not None:
            self.agent_id = agent_id
        self._origin = ProtoListWrapper(container=[float(v) for v in proto.origin], attr_name="origin", list_owner=self)
        if origin is not None:
            self.origin = origin
        self._rotation = ProtoListWrapper(
            container=[float(v) for v in proto.rotation], attr_name="rotation", list_owner=self
        )
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


@register_wrapper(proto_type=pd_scenario_pb2.ScenarioLocation)
class ScenarioLocation(ProtoMessageClass):
    """
    Args:
        location: :attr:`location`
        location_guid: :attr:`location_guid`
        num_scenarios: :attr:`num_scenarios`
        num_retries: :attr:`num_retries`
        generator_config: :attr:`generator_config`
    Attributes:
        location:
        location_guid:
        num_scenarios:
        num_retries:
        generator_config:"""

    _proto_message = pd_scenario_pb2.ScenarioLocation

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.ScenarioLocation] = None,
        location: str = None,
        location_guid: str = None,
        num_scenarios: int = None,
        num_retries: int = None,
        generator_config: _pd_spawn_pb2.GeneratorConfig = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioLocation()
        self.proto = proto
        self._generator_config = get_wrapper(proto_type=proto.generator_config.__class__)(proto=proto.generator_config)
        if location is not None:
            self.location = location
        if location_guid is not None:
            self.location_guid = location_guid
        if num_scenarios is not None:
            self.num_scenarios = num_scenarios
        if num_retries is not None:
            self.num_retries = num_retries
        if generator_config is not None:
            self.generator_config = generator_config

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
    def num_scenarios(self) -> int:
        return self.proto.num_scenarios

    @num_scenarios.setter
    def num_scenarios(self, value: int):
        self.proto.num_scenarios = value

    @property
    def num_retries(self) -> int:
        return self.proto.num_retries

    @num_retries.setter
    def num_retries(self, value: int):
        self.proto.num_retries = value

    @property
    def generator_config(self) -> _pd_spawn_pb2.GeneratorConfig:
        return self._generator_config

    @generator_config.setter
    def generator_config(self, value: _pd_spawn_pb2.GeneratorConfig):
        self.proto.generator_config.CopyFrom(value.proto)

        self._generator_config = value
        self._generator_config._update_proto_references(self.proto.generator_config)

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioLocation):
        self.proto = proto
        self._generator_config._update_proto_references(proto.generator_config)


@register_wrapper(proto_type=pd_scenario_pb2.ScenarioGenConfig)
class ScenarioGenConfig(ProtoMessageClass):
    """
    Args:
        num_frames: :attr:`num_frames`
        sim_settle_frames: :attr:`sim_settle_frames`
        start_skip_frames: :attr:`start_skip_frames`
        end_skip_frames: :attr:`end_skip_frames`
        sim_capture_rate: :attr:`sim_capture_rate`
        sim_update_time: :attr:`sim_update_time`
        scenario_seed: :attr:`scenario_seed`
        output_offset: :attr:`output_offset`
        merge_batches: :attr:`merge_batches`
        batch_size: :attr:`batch_size`
        environment: :attr:`environment`
        spawn_config: :attr:`spawn_config`
        sim_terminate_on_collision_within_radius_m: :attr:`sim_terminate_on_collision_within_radius_m`
        sim_terminate_on_pedestrian_collision_within_radius_m: :attr:`sim_terminate_on_pedestrian_collision_within_radius_m`
        check_offroad_vehicles: :attr:`check_offroad_vehicles`
        sim_terminate_on_drone_flight_path_end: :attr:`sim_terminate_on_drone_flight_path_end`
    Attributes:
        num_frames:
        sim_settle_frames:
        start_skip_frames:
        end_skip_frames:
        sim_capture_rate:
        sim_update_time:
        scenario_seed:
        output_offset:
        merge_batches:
        batch_size:
        environment:
        spawn_config:
        sim_terminate_on_collision_within_radius_m:
        sim_terminate_on_pedestrian_collision_within_radius_m:
        check_offroad_vehicles:
        sim_terminate_on_drone_flight_path_end:"""

    _proto_message = pd_scenario_pb2.ScenarioGenConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.ScenarioGenConfig] = None,
        num_frames: int = None,
        sim_settle_frames: int = None,
        start_skip_frames: int = None,
        end_skip_frames: int = None,
        sim_capture_rate: int = None,
        sim_update_time: float = None,
        scenario_seed: int = None,
        output_offset: int = None,
        merge_batches: bool = None,
        batch_size: int = None,
        environment: _pd_environments_pb2.EnvironmentDefinition = None,
        spawn_config: _pd_spawn_pb2.SpawnConfig = None,
        sim_terminate_on_collision_within_radius_m: float = None,
        sim_terminate_on_pedestrian_collision_within_radius_m: float = None,
        check_offroad_vehicles: bool = None,
        sim_terminate_on_drone_flight_path_end: bool = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioGenConfig()
        self.proto = proto
        self._environment = get_wrapper(proto_type=proto.environment.__class__)(proto=proto.environment)
        self._spawn_config = get_wrapper(proto_type=proto.spawn_config.__class__)(proto=proto.spawn_config)
        if num_frames is not None:
            self.num_frames = num_frames
        if sim_settle_frames is not None:
            self.sim_settle_frames = sim_settle_frames
        if start_skip_frames is not None:
            self.start_skip_frames = start_skip_frames
        if end_skip_frames is not None:
            self.end_skip_frames = end_skip_frames
        if sim_capture_rate is not None:
            self.sim_capture_rate = sim_capture_rate
        if sim_update_time is not None:
            self.sim_update_time = sim_update_time
        if scenario_seed is not None:
            self.scenario_seed = scenario_seed
        if output_offset is not None:
            self.output_offset = output_offset
        if merge_batches is not None:
            self.merge_batches = merge_batches
        if batch_size is not None:
            self.batch_size = batch_size
        if environment is not None:
            self.environment = environment
        if spawn_config is not None:
            self.spawn_config = spawn_config
        if sim_terminate_on_collision_within_radius_m is not None:
            self.sim_terminate_on_collision_within_radius_m = sim_terminate_on_collision_within_radius_m
        if sim_terminate_on_pedestrian_collision_within_radius_m is not None:
            self.sim_terminate_on_pedestrian_collision_within_radius_m = (
                sim_terminate_on_pedestrian_collision_within_radius_m
            )
        if check_offroad_vehicles is not None:
            self.check_offroad_vehicles = check_offroad_vehicles
        if sim_terminate_on_drone_flight_path_end is not None:
            self.sim_terminate_on_drone_flight_path_end = sim_terminate_on_drone_flight_path_end

    @property
    def num_frames(self) -> int:
        return self.proto.num_frames

    @num_frames.setter
    def num_frames(self, value: int):
        self.proto.num_frames = value

    @property
    def sim_settle_frames(self) -> int:
        return self.proto.sim_settle_frames

    @sim_settle_frames.setter
    def sim_settle_frames(self, value: int):
        self.proto.sim_settle_frames = value

    @property
    def start_skip_frames(self) -> int:
        return self.proto.start_skip_frames

    @start_skip_frames.setter
    def start_skip_frames(self, value: int):
        self.proto.start_skip_frames = value

    @property
    def end_skip_frames(self) -> int:
        return self.proto.end_skip_frames

    @end_skip_frames.setter
    def end_skip_frames(self, value: int):
        self.proto.end_skip_frames = value

    @property
    def sim_capture_rate(self) -> int:
        return self.proto.sim_capture_rate

    @sim_capture_rate.setter
    def sim_capture_rate(self, value: int):
        self.proto.sim_capture_rate = value

    @property
    def sim_update_time(self) -> float:
        return self.proto.sim_update_time

    @sim_update_time.setter
    def sim_update_time(self, value: float):
        self.proto.sim_update_time = value

    @property
    def scenario_seed(self) -> int:
        return self.proto.scenario_seed

    @scenario_seed.setter
    def scenario_seed(self, value: int):
        self.proto.scenario_seed = value

    @property
    def output_offset(self) -> int:
        return self.proto.output_offset

    @output_offset.setter
    def output_offset(self, value: int):
        self.proto.output_offset = value

    @property
    def merge_batches(self) -> bool:
        return self.proto.merge_batches

    @merge_batches.setter
    def merge_batches(self, value: bool):
        self.proto.merge_batches = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def environment(self) -> _pd_environments_pb2.EnvironmentDefinition:
        return self._environment

    @environment.setter
    def environment(self, value: _pd_environments_pb2.EnvironmentDefinition):
        self.proto.environment.CopyFrom(value.proto)

        self._environment = value
        self._environment._update_proto_references(self.proto.environment)

    @property
    def spawn_config(self) -> _pd_spawn_pb2.SpawnConfig:
        return self._spawn_config

    @spawn_config.setter
    def spawn_config(self, value: _pd_spawn_pb2.SpawnConfig):
        self.proto.spawn_config.CopyFrom(value.proto)

        self._spawn_config = value
        self._spawn_config._update_proto_references(self.proto.spawn_config)

    @property
    def sim_terminate_on_collision_within_radius_m(self) -> float:
        return self.proto.sim_terminate_on_collision_within_radius_m

    @sim_terminate_on_collision_within_radius_m.setter
    def sim_terminate_on_collision_within_radius_m(self, value: float):
        self.proto.sim_terminate_on_collision_within_radius_m = value

    @property
    def sim_terminate_on_pedestrian_collision_within_radius_m(self) -> float:
        return self.proto.sim_terminate_on_pedestrian_collision_within_radius_m

    @sim_terminate_on_pedestrian_collision_within_radius_m.setter
    def sim_terminate_on_pedestrian_collision_within_radius_m(self, value: float):
        self.proto.sim_terminate_on_pedestrian_collision_within_radius_m = value

    @property
    def check_offroad_vehicles(self) -> bool:
        return self.proto.check_offroad_vehicles

    @check_offroad_vehicles.setter
    def check_offroad_vehicles(self, value: bool):
        self.proto.check_offroad_vehicles = value

    @property
    def sim_terminate_on_drone_flight_path_end(self) -> bool:
        return self.proto.sim_terminate_on_drone_flight_path_end

    @sim_terminate_on_drone_flight_path_end.setter
    def sim_terminate_on_drone_flight_path_end(self, value: bool):
        self.proto.sim_terminate_on_drone_flight_path_end = value

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioGenConfig):
        self.proto = proto
        self._environment._update_proto_references(proto.environment)
        self._spawn_config._update_proto_references(proto.spawn_config)


@register_wrapper(proto_type=pd_scenario_pb2.AgentTag)
class AgentTag(ProtoMessageClass):
    """
    Args:
        agent_id: :attr:`agent_id`
        tags: :attr:`tags`
    Attributes:
        agent_id:
        tags:"""

    _proto_message = pd_scenario_pb2.AgentTag

    def __init__(
        self, *, proto: Optional[pd_scenario_pb2.AgentTag] = None, agent_id: int = None, tags: List[str] = None
    ):
        if proto is None:
            proto = pd_scenario_pb2.AgentTag()
        self.proto = proto
        if agent_id is not None:
            self.agent_id = agent_id
        self._tags = ProtoListWrapper(container=[str(v) for v in proto.tags], attr_name="tags", list_owner=self)
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


@register_wrapper(proto_type=pd_scenario_pb2.ScenarioDefinition)
class ScenarioDefinition(ProtoMessageClass):
    """
    Args:
        name: :attr:`name`
        num_frames: :attr:`num_frames`
        skip_frames: :attr:`skip_frames`
        current_time: :attr:`current_time`
        sim_update_time: :attr:`sim_update_time`
        output_frame_skip: :attr:`output_frame_skip`
        world: :attr:`world`
        lighting: :attr:`lighting`
        fog_intensity: :attr:`fog_intensity`
        rain_intensity: :attr:`rain_intensity`
        wetness: :attr:`wetness`
        street_lights: :attr:`street_lights`
        headlights: :attr:`headlights`
        linear_movers: :attr:`linear_movers`
        vehicles: :attr:`vehicles`
        sensors: :attr:`sensors`
        performance_feature: :attr:`performance_feature`
        anti_aliasing: :attr:`anti_aliasing`
        config_blob: :attr:`config_blob`
        agent_tags: :attr:`agent_tags`
    Attributes:
        name:
        num_frames:
        skip_frames:
        current_time:
        sim_update_time:
        output_frame_skip:
        world:
        lighting:
        fog_intensity:
        rain_intensity:
        wetness:
        street_lights:
        headlights:
        linear_movers:
        vehicles:
        sensors:
        performance_feature:
        anti_aliasing:
        config_blob: Json blob used to transfer values from the spawn config, or other 'setup' into scenario during runtime.
        agent_tags: Structure used to pass information to the encoder from the scenario generation."""

    class PerformanceFeature(ProtoEnumClass):
        HighFidelityMode = 0
        PerformanceMode = 1

    _proto_message = pd_scenario_pb2.ScenarioDefinition

    def __init__(
        self,
        *,
        proto: Optional[pd_scenario_pb2.ScenarioDefinition] = None,
        name: str = None,
        num_frames: int = None,
        skip_frames: int = None,
        current_time: float = None,
        sim_update_time: float = None,
        output_frame_skip: int = None,
        world: str = None,
        lighting: str = None,
        fog_intensity: float = None,
        rain_intensity: float = None,
        wetness: float = None,
        street_lights: float = None,
        headlights: bool = None,
        linear_movers: List[LinearMover] = None,
        vehicles: List[Vehicle] = None,
        sensors: List[Sensor] = None,
        performance_feature: ScenarioDefinition.PerformanceFeature = None,
        anti_aliasing: int = None,
        config_blob: str = None,
        agent_tags: List[AgentTag] = None,
    ):
        if proto is None:
            proto = pd_scenario_pb2.ScenarioDefinition()
        self.proto = proto
        self._linear_movers = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.linear_movers],
            attr_name="linear_movers",
            list_owner=self,
        )
        self._vehicles = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.vehicles],
            attr_name="vehicles",
            list_owner=self,
        )
        self._sensors = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensors],
            attr_name="sensors",
            list_owner=self,
        )
        self._agent_tags = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.agent_tags],
            attr_name="agent_tags",
            list_owner=self,
        )
        if name is not None:
            self.name = name
        if num_frames is not None:
            self.num_frames = num_frames
        if skip_frames is not None:
            self.skip_frames = skip_frames
        if current_time is not None:
            self.current_time = current_time
        if sim_update_time is not None:
            self.sim_update_time = sim_update_time
        if output_frame_skip is not None:
            self.output_frame_skip = output_frame_skip
        if world is not None:
            self.world = world
        if lighting is not None:
            self.lighting = lighting
        if fog_intensity is not None:
            self.fog_intensity = fog_intensity
        if rain_intensity is not None:
            self.rain_intensity = rain_intensity
        if wetness is not None:
            self.wetness = wetness
        if street_lights is not None:
            self.street_lights = street_lights
        if headlights is not None:
            self.headlights = headlights
        if linear_movers is not None:
            self.linear_movers = linear_movers
        if vehicles is not None:
            self.vehicles = vehicles
        if sensors is not None:
            self.sensors = sensors
        if performance_feature is not None:
            self.performance_feature = performance_feature
        if anti_aliasing is not None:
            self.anti_aliasing = anti_aliasing
        if config_blob is not None:
            self.config_blob = config_blob
        if agent_tags is not None:
            self.agent_tags = agent_tags

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
    def skip_frames(self) -> int:
        return self.proto.skip_frames

    @skip_frames.setter
    def skip_frames(self, value: int):
        self.proto.skip_frames = value

    @property
    def current_time(self) -> float:
        return self.proto.current_time

    @current_time.setter
    def current_time(self, value: float):
        self.proto.current_time = value

    @property
    def sim_update_time(self) -> float:
        return self.proto.sim_update_time

    @sim_update_time.setter
    def sim_update_time(self, value: float):
        self.proto.sim_update_time = value

    @property
    def output_frame_skip(self) -> int:
        return self.proto.output_frame_skip

    @output_frame_skip.setter
    def output_frame_skip(self, value: int):
        self.proto.output_frame_skip = value

    @property
    def world(self) -> str:
        return self.proto.world

    @world.setter
    def world(self, value: str):
        self.proto.world = value

    @property
    def lighting(self) -> str:
        return self.proto.lighting

    @lighting.setter
    def lighting(self, value: str):
        self.proto.lighting = value

    @property
    def fog_intensity(self) -> float:
        return self.proto.fog_intensity

    @fog_intensity.setter
    def fog_intensity(self, value: float):
        self.proto.fog_intensity = value

    @property
    def rain_intensity(self) -> float:
        return self.proto.rain_intensity

    @rain_intensity.setter
    def rain_intensity(self, value: float):
        self.proto.rain_intensity = value

    @property
    def wetness(self) -> float:
        return self.proto.wetness

    @wetness.setter
    def wetness(self, value: float):
        self.proto.wetness = value

    @property
    def street_lights(self) -> float:
        return self.proto.street_lights

    @street_lights.setter
    def street_lights(self, value: float):
        self.proto.street_lights = value

    @property
    def headlights(self) -> bool:
        return self.proto.headlights

    @headlights.setter
    def headlights(self, value: bool):
        self.proto.headlights = value

    @property
    def linear_movers(self) -> List[LinearMover]:
        return self._linear_movers

    @linear_movers.setter
    def linear_movers(self, value: List[LinearMover]):
        self._linear_movers.clear()
        for v in value:
            self._linear_movers.append(v)

    @property
    def vehicles(self) -> List[Vehicle]:
        return self._vehicles

    @vehicles.setter
    def vehicles(self, value: List[Vehicle]):
        self._vehicles.clear()
        for v in value:
            self._vehicles.append(v)

    @property
    def sensors(self) -> List[Sensor]:
        return self._sensors

    @sensors.setter
    def sensors(self, value: List[Sensor]):
        self._sensors.clear()
        for v in value:
            self._sensors.append(v)

    @property
    def performance_feature(self) -> ScenarioDefinition.PerformanceFeature:
        return self.proto.performance_feature

    @performance_feature.setter
    def performance_feature(self, value: ScenarioDefinition.PerformanceFeature):
        self.proto.performance_feature = value

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
    def agent_tags(self) -> List[AgentTag]:
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, value: List[AgentTag]):
        self._agent_tags.clear()
        for v in value:
            self._agent_tags.append(v)

    def _update_proto_references(self, proto: pd_scenario_pb2.ScenarioDefinition):
        self.proto = proto
        for i, v in enumerate(self.linear_movers):
            v._update_proto_references(self.proto.linear_movers[i])
        for i, v in enumerate(self.vehicles):
            v._update_proto_references(self.proto.vehicles[i])
        for i, v in enumerate(self.sensors):
            v._update_proto_references(self.proto.sensors[i])
        for i, v in enumerate(self.agent_tags):
            v._update_proto_references(self.proto.agent_tags[i])
