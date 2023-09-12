from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_step_batch_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_step_batch_pb2 as _pd_step_batch_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_step_batch_pb2.LocationOverride)
class LocationOverride(ProtoMessageClass):
    _proto_message = pd_step_batch_pb2.LocationOverride

    def __init__(self, *, proto: Optional[pd_step_batch_pb2.LocationOverride]=None, location: Optional[str]=None, location_uuid: Optional[str]=None):
        if proto is None:
            proto = pd_step_batch_pb2.LocationOverride()
        self.proto = proto
        if location is not None:
            self.location = location
        if location_uuid is not None:
            self.location_uuid = location_uuid

    @property
    def location(self) -> str:
        return self.proto.location

    @location.setter
    def location(self, value: str):
        self.proto.location = value

    @property
    def location_uuid(self) -> str:
        return self.proto.location_uuid

    @location_uuid.setter
    def location_uuid(self, value: str):
        self.proto.location_uuid = value

    def _update_proto_references(self, proto: pd_step_batch_pb2.LocationOverride):
        self.proto = proto

@register_wrapper(proto_type=pd_step_batch_pb2.StepBatch)
class StepBatch(ProtoMessageClass):
    _proto_message = pd_step_batch_pb2.StepBatch

    def __init__(self, *, proto: Optional[pd_step_batch_pb2.StepBatch]=None, batch_size: Optional[int]=None, check_offroad_vehicles: Optional[bool]=None, end_skip_frames: Optional[int]=None, generate_name: Optional[str]=None, location_overrides: Optional[List[LocationOverride]]=None, merge_batches: Optional[bool]=None, module_name: Optional[str]=None, name: Optional[str]=None, num_frames: Optional[int]=None, num_retries: Optional[int]=None, num_scenarios: Optional[int]=None, org: Optional[str]=None, output_artifact_uid: Optional[str]=None, output_offset: Optional[int]=None, scenario_container: Optional[str]=None, scenario_seed: Optional[int]=None, sim_capture_rate: Optional[int]=None, sim_settle_frames: Optional[int]=None, sim_terminate_on_collision_within_radius_m: Optional[float]=None, sim_terminate_on_drone_flight_path_end: Optional[bool]=None, sim_terminate_on_pedestrian_collision_within_radius_m: Optional[float]=None, sim_update_time: Optional[float]=None, start_skip_frames: Optional[int]=None):
        if proto is None:
            proto = pd_step_batch_pb2.StepBatch()
        self.proto = proto
        self._location_overrides = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.location_overrides], attr_name='location_overrides', list_owner=self)
        if batch_size is not None:
            self.batch_size = batch_size
        if check_offroad_vehicles is not None:
            self.check_offroad_vehicles = check_offroad_vehicles
        if end_skip_frames is not None:
            self.end_skip_frames = end_skip_frames
        if generate_name is not None:
            self.generate_name = generate_name
        if location_overrides is not None:
            self.location_overrides = location_overrides
        if merge_batches is not None:
            self.merge_batches = merge_batches
        if module_name is not None:
            self.module_name = module_name
        if name is not None:
            self.name = name
        if num_frames is not None:
            self.num_frames = num_frames
        if num_retries is not None:
            self.num_retries = num_retries
        if num_scenarios is not None:
            self.num_scenarios = num_scenarios
        if org is not None:
            self.org = org
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if output_offset is not None:
            self.output_offset = output_offset
        if scenario_container is not None:
            self.scenario_container = scenario_container
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
    def generate_name(self) -> str:
        return self.proto.generate_name

    @generate_name.setter
    def generate_name(self, value: str):
        self.proto.generate_name = value

    @property
    def location_overrides(self) -> List[LocationOverride]:
        return self._location_overrides

    @location_overrides.setter
    def location_overrides(self, value: List[LocationOverride]):
        self._location_overrides.clear()
        for v in value:
            self._location_overrides.append(v)

    @property
    def merge_batches(self) -> bool:
        return self.proto.merge_batches

    @merge_batches.setter
    def merge_batches(self, value: bool):
        self.proto.merge_batches = value

    @property
    def module_name(self) -> str:
        return self.proto.module_name

    @module_name.setter
    def module_name(self, value: str):
        self.proto.module_name = value

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

    @property
    def org(self) -> str:
        return self.proto.org

    @org.setter
    def org(self, value: str):
        self.proto.org = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def output_offset(self) -> int:
        return self.proto.output_offset

    @output_offset.setter
    def output_offset(self, value: int):
        self.proto.output_offset = value

    @property
    def scenario_container(self) -> str:
        return self.proto.scenario_container

    @scenario_container.setter
    def scenario_container(self, value: str):
        self.proto.scenario_container = value

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
    def start_skip_frames(self) -> int:
        return self.proto.start_skip_frames

    @start_skip_frames.setter
    def start_skip_frames(self, value: int):
        self.proto.start_skip_frames = value

    def _update_proto_references(self, proto: pd_step_batch_pb2.StepBatch):
        self.proto = proto
        for i, v in enumerate(self.location_overrides):
            v._update_proto_references(self.proto.location_overrides[i])