from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_render_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_render_pb2.KeystoneAttributes)
class KeystoneAttributes(ProtoMessageClass):
    _proto_message = pd_render_pb2.KeystoneAttributes

    def __init__(self, *, proto: Optional[pd_render_pb2.KeystoneAttributes]=None, group: Optional[str]=None):
        if proto is None:
            proto = pd_render_pb2.KeystoneAttributes()
        self.proto = proto
        if group is not None:
            self.group = group

    @property
    def group(self) -> str:
        return self.proto.group

    @group.setter
    def group(self, value: str):
        self.proto.group = value

@register_wrapper(proto_type=pd_render_pb2.RenderInfo)
class RenderInfo(ProtoMessageClass):

    @register_wrapper(proto_type=pd_render_pb2.RenderInfo.EnvironmentMode)
    class EnvironmentMode(ProtoEnumClass):
        _proto_message = pd_render_pb2.RenderInfo.EnvironmentMode
        CYCLE: pd_render_pb2.RenderInfo.EnvironmentMode = pd_render_pb2.RenderInfo.EnvironmentMode.CYCLE
        NONE: pd_render_pb2.RenderInfo.EnvironmentMode = pd_render_pb2.RenderInfo.EnvironmentMode.NONE
        RANDOM: pd_render_pb2.RenderInfo.EnvironmentMode = pd_render_pb2.RenderInfo.EnvironmentMode.RANDOM
        SPREAD: pd_render_pb2.RenderInfo.EnvironmentMode = pd_render_pb2.RenderInfo.EnvironmentMode.SPREAD
    _proto_message = pd_render_pb2.RenderInfo

    def __init__(self, *, proto: Optional[pd_render_pb2.RenderInfo]=None, annotate_accessories_2d: Optional[bool]=None, annotate_accessories_3d: Optional[bool]=None, annotate_wing_mirrors_2d: Optional[bool]=None, annotate_wing_mirrors_3d: Optional[bool]=None, apply_lidar_noise: Optional[bool]=None, artifact_key: Optional[str]=None, batch_size: Optional[int]=None, bbox_2d_only_visible_pixels: Optional[bool]=None, box_non_visible_signal_bulbs: Optional[bool]=None, capture_all_frames: Optional[bool]=None, capture_rate: Optional[int]=None, code_build_artifact_uid: Optional[str]=None, disable_reflection: Optional[bool]=None, disable_specular: Optional[bool]=None, enable_radar_debug: Optional[bool]=None, end_scene: Optional[int]=None, environment_attr_list: Optional[List[RenderInfo.Environment]]=None, environment_mode: Optional[RenderInfo.EnvironmentMode]=None, generate_previews: Optional[bool]=None, hide_all_volumetrics: Optional[bool]=None, hide_crosswalk_segmentation_mesh: Optional[bool]=None, image_generator_core_artifact_uid: Optional[str]=None, keep_glass_transparent: Optional[bool]=None, level_pak_artifact_uid: Optional[Dict[str, str]]=None, merge_bikes_riders_3d: Optional[bool]=None, new_data_pipeline: Optional[bool]=None, output_artifact_uid: Optional[str]=None, output_instance_point_caches: Optional[bool]=None, output_telemetry: Optional[bool]=None, output_truncated_3d_annotations: Optional[bool]=None, physical_ground_truth: Optional[bool]=None, render_ego_vehicle: Optional[bool]=None, sensor_rig: Optional[_pd_sensor_pb2.SensorRigConfig]=None, sensor_splits_list: Optional[List[_pd_sensor_pb2.SensorList]]=None, start_scene: Optional[int]=None, state_file_archive_artifact_uid: Optional[str]=None, use_high_gpu_mem_render_node: Optional[bool]=None, use_instance_point_caches: Optional[bool]=None, use_linux: Optional[bool]=None, use_opaque_glass: Optional[int]=None, vehicle_color_offset: Optional[int]=None, volumetric_density_scale: Optional[float]=None):
        if proto is None:
            proto = pd_render_pb2.RenderInfo()
        self.proto = proto
        self._environment_attr_list = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.environment_attr_list], attr_name='environment_attr_list', list_owner=proto)
        self._level_pak_artifact_uid = ProtoDictWrapper(container={k: str(v) for (k, v) in proto.level_pak_artifact_uid.items()}, attr_name='level_pak_artifact_uid', dict_owner=proto)
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        self._sensor_splits_list = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensor_splits_list], attr_name='sensor_splits_list', list_owner=proto)
        if annotate_accessories_2d is not None:
            self.annotate_accessories_2d = annotate_accessories_2d
        if annotate_accessories_3d is not None:
            self.annotate_accessories_3d = annotate_accessories_3d
        if annotate_wing_mirrors_2d is not None:
            self.annotate_wing_mirrors_2d = annotate_wing_mirrors_2d
        if annotate_wing_mirrors_3d is not None:
            self.annotate_wing_mirrors_3d = annotate_wing_mirrors_3d
        if apply_lidar_noise is not None:
            self.apply_lidar_noise = apply_lidar_noise
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if batch_size is not None:
            self.batch_size = batch_size
        if bbox_2d_only_visible_pixels is not None:
            self.bbox_2d_only_visible_pixels = bbox_2d_only_visible_pixels
        if box_non_visible_signal_bulbs is not None:
            self.box_non_visible_signal_bulbs = box_non_visible_signal_bulbs
        if capture_all_frames is not None:
            self.capture_all_frames = capture_all_frames
        if capture_rate is not None:
            self.capture_rate = capture_rate
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if disable_reflection is not None:
            self.disable_reflection = disable_reflection
        if disable_specular is not None:
            self.disable_specular = disable_specular
        if enable_radar_debug is not None:
            self.enable_radar_debug = enable_radar_debug
        if end_scene is not None:
            self.end_scene = end_scene
        if environment_attr_list is not None:
            self.environment_attr_list = environment_attr_list
        if environment_mode is not None:
            self.environment_mode = environment_mode
        if generate_previews is not None:
            self.generate_previews = generate_previews
        if hide_all_volumetrics is not None:
            self.hide_all_volumetrics = hide_all_volumetrics
        if hide_crosswalk_segmentation_mesh is not None:
            self.hide_crosswalk_segmentation_mesh = hide_crosswalk_segmentation_mesh
        if image_generator_core_artifact_uid is not None:
            self.image_generator_core_artifact_uid = image_generator_core_artifact_uid
        if keep_glass_transparent is not None:
            self.keep_glass_transparent = keep_glass_transparent
        if level_pak_artifact_uid is not None:
            self.level_pak_artifact_uid = level_pak_artifact_uid
        if merge_bikes_riders_3d is not None:
            self.merge_bikes_riders_3d = merge_bikes_riders_3d
        if new_data_pipeline is not None:
            self.new_data_pipeline = new_data_pipeline
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if output_instance_point_caches is not None:
            self.output_instance_point_caches = output_instance_point_caches
        if output_telemetry is not None:
            self.output_telemetry = output_telemetry
        if output_truncated_3d_annotations is not None:
            self.output_truncated_3d_annotations = output_truncated_3d_annotations
        if physical_ground_truth is not None:
            self.physical_ground_truth = physical_ground_truth
        if render_ego_vehicle is not None:
            self.render_ego_vehicle = render_ego_vehicle
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig
        if sensor_splits_list is not None:
            self.sensor_splits_list = sensor_splits_list
        if start_scene is not None:
            self.start_scene = start_scene
        if state_file_archive_artifact_uid is not None:
            self.state_file_archive_artifact_uid = state_file_archive_artifact_uid
        if use_high_gpu_mem_render_node is not None:
            self.use_high_gpu_mem_render_node = use_high_gpu_mem_render_node
        if use_instance_point_caches is not None:
            self.use_instance_point_caches = use_instance_point_caches
        if use_linux is not None:
            self.use_linux = use_linux
        if use_opaque_glass is not None:
            self.use_opaque_glass = use_opaque_glass
        if vehicle_color_offset is not None:
            self.vehicle_color_offset = vehicle_color_offset
        if volumetric_density_scale is not None:
            self.volumetric_density_scale = volumetric_density_scale

    @property
    def annotate_accessories_2d(self) -> bool:
        return self.proto.annotate_accessories_2d

    @annotate_accessories_2d.setter
    def annotate_accessories_2d(self, value: bool):
        self.proto.annotate_accessories_2d = value

    @property
    def annotate_accessories_3d(self) -> bool:
        return self.proto.annotate_accessories_3d

    @annotate_accessories_3d.setter
    def annotate_accessories_3d(self, value: bool):
        self.proto.annotate_accessories_3d = value

    @property
    def annotate_wing_mirrors_2d(self) -> bool:
        return self.proto.annotate_wing_mirrors_2d

    @annotate_wing_mirrors_2d.setter
    def annotate_wing_mirrors_2d(self, value: bool):
        self.proto.annotate_wing_mirrors_2d = value

    @property
    def annotate_wing_mirrors_3d(self) -> bool:
        return self.proto.annotate_wing_mirrors_3d

    @annotate_wing_mirrors_3d.setter
    def annotate_wing_mirrors_3d(self, value: bool):
        self.proto.annotate_wing_mirrors_3d = value

    @property
    def apply_lidar_noise(self) -> bool:
        return self.proto.apply_lidar_noise

    @apply_lidar_noise.setter
    def apply_lidar_noise(self, value: bool):
        self.proto.apply_lidar_noise = value

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def bbox_2d_only_visible_pixels(self) -> bool:
        return self.proto.bbox_2d_only_visible_pixels

    @bbox_2d_only_visible_pixels.setter
    def bbox_2d_only_visible_pixels(self, value: bool):
        self.proto.bbox_2d_only_visible_pixels = value

    @property
    def box_non_visible_signal_bulbs(self) -> bool:
        return self.proto.box_non_visible_signal_bulbs

    @box_non_visible_signal_bulbs.setter
    def box_non_visible_signal_bulbs(self, value: bool):
        self.proto.box_non_visible_signal_bulbs = value

    @property
    def capture_all_frames(self) -> bool:
        return self.proto.capture_all_frames

    @capture_all_frames.setter
    def capture_all_frames(self, value: bool):
        self.proto.capture_all_frames = value

    @property
    def capture_rate(self) -> int:
        return self.proto.capture_rate

    @capture_rate.setter
    def capture_rate(self, value: int):
        self.proto.capture_rate = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def disable_reflection(self) -> bool:
        return self.proto.disable_reflection

    @disable_reflection.setter
    def disable_reflection(self, value: bool):
        self.proto.disable_reflection = value

    @property
    def disable_specular(self) -> bool:
        return self.proto.disable_specular

    @disable_specular.setter
    def disable_specular(self, value: bool):
        self.proto.disable_specular = value

    @property
    def enable_radar_debug(self) -> bool:
        return self.proto.enable_radar_debug

    @enable_radar_debug.setter
    def enable_radar_debug(self, value: bool):
        self.proto.enable_radar_debug = value

    @property
    def end_scene(self) -> int:
        return self.proto.end_scene

    @end_scene.setter
    def end_scene(self, value: int):
        self.proto.end_scene = value

    @property
    def environment_attr_list(self) -> List[RenderInfo.Environment]:
        return self._environment_attr_list

    @environment_attr_list.setter
    def environment_attr_list(self, value: List[RenderInfo.Environment]):
        self._environment_attr_list.clear()
        for v in value:
            self._environment_attr_list.append(v)

    @property
    def environment_mode(self) -> int:
        return self.proto.environment_mode

    @environment_mode.setter
    def environment_mode(self, value: int):
        self.proto.environment_mode = value

    @property
    def generate_previews(self) -> bool:
        return self.proto.generate_previews

    @generate_previews.setter
    def generate_previews(self, value: bool):
        self.proto.generate_previews = value

    @property
    def hide_all_volumetrics(self) -> bool:
        return self.proto.hide_all_volumetrics

    @hide_all_volumetrics.setter
    def hide_all_volumetrics(self, value: bool):
        self.proto.hide_all_volumetrics = value

    @property
    def hide_crosswalk_segmentation_mesh(self) -> bool:
        return self.proto.hide_crosswalk_segmentation_mesh

    @hide_crosswalk_segmentation_mesh.setter
    def hide_crosswalk_segmentation_mesh(self, value: bool):
        self.proto.hide_crosswalk_segmentation_mesh = value

    @property
    def image_generator_core_artifact_uid(self) -> str:
        return self.proto.image_generator_core_artifact_uid

    @image_generator_core_artifact_uid.setter
    def image_generator_core_artifact_uid(self, value: str):
        self.proto.image_generator_core_artifact_uid = value

    @property
    def keep_glass_transparent(self) -> bool:
        return self.proto.keep_glass_transparent

    @keep_glass_transparent.setter
    def keep_glass_transparent(self, value: bool):
        self.proto.keep_glass_transparent = value

    @property
    def level_pak_artifact_uid(self) -> Dict[str, str]:
        return self._level_pak_artifact_uid

    @level_pak_artifact_uid.setter
    def level_pak_artifact_uid(self, value: Dict[str, str]):
        self._level_pak_artifact_uid.clear()
        self._level_pak_artifact_uid.update(value)

    @property
    def merge_bikes_riders_3d(self) -> bool:
        return self.proto.merge_bikes_riders_3d

    @merge_bikes_riders_3d.setter
    def merge_bikes_riders_3d(self, value: bool):
        self.proto.merge_bikes_riders_3d = value

    @property
    def new_data_pipeline(self) -> bool:
        return self.proto.new_data_pipeline

    @new_data_pipeline.setter
    def new_data_pipeline(self, value: bool):
        self.proto.new_data_pipeline = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def output_instance_point_caches(self) -> bool:
        return self.proto.output_instance_point_caches

    @output_instance_point_caches.setter
    def output_instance_point_caches(self, value: bool):
        self.proto.output_instance_point_caches = value

    @property
    def output_telemetry(self) -> bool:
        return self.proto.output_telemetry

    @output_telemetry.setter
    def output_telemetry(self, value: bool):
        self.proto.output_telemetry = value

    @property
    def output_truncated_3d_annotations(self) -> bool:
        return self.proto.output_truncated_3d_annotations

    @output_truncated_3d_annotations.setter
    def output_truncated_3d_annotations(self, value: bool):
        self.proto.output_truncated_3d_annotations = value

    @property
    def physical_ground_truth(self) -> bool:
        return self.proto.physical_ground_truth

    @physical_ground_truth.setter
    def physical_ground_truth(self, value: bool):
        self.proto.physical_ground_truth = value

    @property
    def render_ego_vehicle(self) -> bool:
        return self.proto.render_ego_vehicle

    @render_ego_vehicle.setter
    def render_ego_vehicle(self, value: bool):
        self.proto.render_ego_vehicle = value

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self._sensor_rig.proto.CopyFrom(value.proto)

    @property
    def sensor_splits_list(self) -> List[_pd_sensor_pb2.SensorList]:
        return self._sensor_splits_list

    @sensor_splits_list.setter
    def sensor_splits_list(self, value: List[_pd_sensor_pb2.SensorList]):
        self._sensor_splits_list.clear()
        for v in value:
            self._sensor_splits_list.append(v)

    @property
    def start_scene(self) -> int:
        return self.proto.start_scene

    @start_scene.setter
    def start_scene(self, value: int):
        self.proto.start_scene = value

    @property
    def state_file_archive_artifact_uid(self) -> str:
        return self.proto.state_file_archive_artifact_uid

    @state_file_archive_artifact_uid.setter
    def state_file_archive_artifact_uid(self, value: str):
        self.proto.state_file_archive_artifact_uid = value

    @property
    def use_high_gpu_mem_render_node(self) -> bool:
        return self.proto.use_high_gpu_mem_render_node

    @use_high_gpu_mem_render_node.setter
    def use_high_gpu_mem_render_node(self, value: bool):
        self.proto.use_high_gpu_mem_render_node = value

    @property
    def use_instance_point_caches(self) -> bool:
        return self.proto.use_instance_point_caches

    @use_instance_point_caches.setter
    def use_instance_point_caches(self, value: bool):
        self.proto.use_instance_point_caches = value

    @property
    def use_linux(self) -> bool:
        return self.proto.use_linux

    @use_linux.setter
    def use_linux(self, value: bool):
        self.proto.use_linux = value

    @property
    def use_opaque_glass(self) -> int:
        return self.proto.use_opaque_glass

    @use_opaque_glass.setter
    def use_opaque_glass(self, value: int):
        self.proto.use_opaque_glass = value

    @property
    def vehicle_color_offset(self) -> int:
        return self.proto.vehicle_color_offset

    @vehicle_color_offset.setter
    def vehicle_color_offset(self, value: int):
        self.proto.vehicle_color_offset = value

    @property
    def volumetric_density_scale(self) -> float:
        return self.proto.volumetric_density_scale

    @volumetric_density_scale.setter
    def volumetric_density_scale(self, value: float):
        self.proto.volumetric_density_scale = value