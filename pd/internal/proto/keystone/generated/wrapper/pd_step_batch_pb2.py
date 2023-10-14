from __future__ import annotations
from typing import List, Optional
from .utils import (
    register_wrapper,
    get_wrapper,
    ProtoMessageClass,
    ProtoListWrapper
)
from ..python import (
    pd_step_batch_pb2
)


@register_wrapper(proto_type=pd_step_batch_pb2.LocationOverride)
class LocationOverride(ProtoMessageClass):
    """
    Args:
        location: :attr:`location`
        location_uuid: :attr:`location_uuid`
    Attributes:
        location:
        location_uuid:"""

    _proto_message = pd_step_batch_pb2.LocationOverride

    def __init__(
        self,
        *,
        proto: Optional[pd_step_batch_pb2.LocationOverride] = None,
        location: str = None,
        location_uuid: str = None,
    ):
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
    """
    Args:
        name: :attr:`name`
        output_artifact_uid: :attr:`output_artifact_uid`
        scenario_container: :attr:`scenario_container`
        module_name: :attr:`module_name`
        generate_name: :attr:`generate_name`
        org: :attr:`org`
        num_scenarios: :attr:`num_scenarios`
        scenario_seed: :attr:`scenario_seed`
        batch_size: :attr:`batch_size`
        output_offset: :attr:`output_offset`
        merge_batches: :attr:`merge_batches`
        num_frames: :attr:`num_frames`
        sim_settle_frames: :attr:`sim_settle_frames`
        start_skip_frames: :attr:`start_skip_frames`
        end_skip_frames: :attr:`end_skip_frames`
        sim_capture_rate: :attr:`sim_capture_rate`
        sim_update_time: :attr:`sim_update_time`
        num_retries: :attr:`num_retries`
        sim_terminate_on_collision_within_radius_m: :attr:`sim_terminate_on_collision_within_radius_m`
        sim_terminate_on_pedestrian_collision_within_radius_m: :attr:`sim_terminate_on_pedestrian_collision_within_radius_m`
        check_offroad_vehicles: :attr:`check_offroad_vehicles`
        sim_terminate_on_drone_flight_path_end: :attr:`sim_terminate_on_drone_flight_path_end`
        location_overrides: :attr:`location_overrides`
    Attributes:
        name: Human readable name for this job
        output_artifact_uid: Output artifact for build results
        scenario_container: Container image
        module_name:
        generate_name:
        org:
        num_scenarios:
        scenario_seed:
        batch_size: Batches
        output_offset:
        merge_batches:
        num_frames: Scenario configuration parameters
        sim_settle_frames:
        start_skip_frames:
        end_skip_frames:
        sim_capture_rate:
        sim_update_time:
        num_retries: Checks
        sim_terminate_on_collision_within_radius_m:
        sim_terminate_on_pedestrian_collision_within_radius_m:
        check_offroad_vehicles:
        sim_terminate_on_drone_flight_path_end:
        location_overrides: Location overrides"""

    _proto_message = pd_step_batch_pb2.StepBatch

    def __init__(
        self,
        *,
        proto: Optional[pd_step_batch_pb2.StepBatch] = None,
        name: str = None,
        output_artifact_uid: str = None,
        scenario_container: str = None,
        module_name: str = None,
        generate_name: str = None,
        org: str = None,
        num_scenarios: int = None,
        scenario_seed: int = None,
        batch_size: int = None,
        output_offset: int = None,
        merge_batches: bool = None,
        num_frames: int = None,
        sim_settle_frames: int = None,
        start_skip_frames: int = None,
        end_skip_frames: int = None,
        sim_capture_rate: int = None,
        sim_update_time: float = None,
        num_retries: int = None,
        sim_terminate_on_collision_within_radius_m: float = None,
        sim_terminate_on_pedestrian_collision_within_radius_m: float = None,
        check_offroad_vehicles: bool = None,
        sim_terminate_on_drone_flight_path_end: bool = None,
        location_overrides: List[LocationOverride] = None,
    ):
        if proto is None:
            proto = pd_step_batch_pb2.StepBatch()
        self.proto = proto
        self._location_overrides = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.location_overrides],
            attr_name="location_overrides",
            list_owner=self,
        )
        if name is not None:
            self.name = name
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if scenario_container is not None:
            self.scenario_container = scenario_container
        if module_name is not None:
            self.module_name = module_name
        if generate_name is not None:
            self.generate_name = generate_name
        if org is not None:
            self.org = org
        if num_scenarios is not None:
            self.num_scenarios = num_scenarios
        if scenario_seed is not None:
            self.scenario_seed = scenario_seed
        if batch_size is not None:
            self.batch_size = batch_size
        if output_offset is not None:
            self.output_offset = output_offset
        if merge_batches is not None:
            self.merge_batches = merge_batches
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
        if num_retries is not None:
            self.num_retries = num_retries
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
        if location_overrides is not None:
            self.location_overrides = location_overrides

    @property
    def name(self) -> str:
        return self.proto.name

    @name.setter
    def name(self, value: str):
        self.proto.name = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def scenario_container(self) -> str:
        return self.proto.scenario_container

    @scenario_container.setter
    def scenario_container(self, value: str):
        self.proto.scenario_container = value

    @property
    def module_name(self) -> str:
        return self.proto.module_name

    @module_name.setter
    def module_name(self, value: str):
        self.proto.module_name = value

    @property
    def generate_name(self) -> str:
        return self.proto.generate_name

    @generate_name.setter
    def generate_name(self, value: str):
        self.proto.generate_name = value

    @property
    def org(self) -> str:
        return self.proto.org

    @org.setter
    def org(self, value: str):
        self.proto.org = value

    @property
    def num_scenarios(self) -> int:
        return self.proto.num_scenarios

    @num_scenarios.setter
    def num_scenarios(self, value: int):
        self.proto.num_scenarios = value

    @property
    def scenario_seed(self) -> int:
        return self.proto.scenario_seed

    @scenario_seed.setter
    def scenario_seed(self, value: int):
        self.proto.scenario_seed = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

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
    def num_retries(self) -> int:
        return self.proto.num_retries

    @num_retries.setter
    def num_retries(self, value: int):
        self.proto.num_retries = value

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

    @property
    def location_overrides(self) -> List[LocationOverride]:
        return self._location_overrides

    @location_overrides.setter
    def location_overrides(self, value: List[LocationOverride]):
        self._location_overrides.clear()
        for v in value:
            self._location_overrides.append(v)

    def _update_proto_references(self, proto: pd_step_batch_pb2.StepBatch):
        self.proto = proto
        for i, v in enumerate(self.location_overrides):
            v._update_proto_references(self.proto.location_overrides[i])
