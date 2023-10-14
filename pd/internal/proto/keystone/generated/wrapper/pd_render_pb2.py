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
    pd_render_pb2
)
from . import (
    pd_sensor_pb2 as _pd_sensor_pb2
)


@register_wrapper(proto_type=pd_render_pb2.KeystoneAttributes)
class KeystoneAttributes(ProtoMessageClass):
    """
    Args:
        group: :attr:`group`
    Attributes:
        group:"""

    _proto_message = pd_render_pb2.KeystoneAttributes

    def __init__(self, *, proto: Optional[pd_render_pb2.KeystoneAttributes] = None, group: str = None):
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

    def _update_proto_references(self, proto: pd_render_pb2.KeystoneAttributes):
        self.proto = proto


@register_wrapper(proto_type=pd_render_pb2.RenderInfo)
class RenderInfo(ProtoMessageClass):
    """
    Args:
        artifact_key: :attr:`artifact_key`
        output_artifact_uid: :attr:`output_artifact_uid`
        state_file_archive_artifact_uid: :attr:`state_file_archive_artifact_uid`
        code_build_artifact_uid: :attr:`code_build_artifact_uid`
        image_generator_core_artifact_uid: :attr:`image_generator_core_artifact_uid`
        level_pak_artifact_uid: :attr:`level_pak_artifact_uid`
        sensor_rig: :attr:`sensor_rig`
        sensor_splits_list: :attr:`sensor_splits_list`
        use_high_gpu_mem_render_node: :attr:`use_high_gpu_mem_render_node`
        annotate_wing_mirrors_2d: :attr:`annotate_wing_mirrors_2d`
        annotate_wing_mirrors_3d: :attr:`annotate_wing_mirrors_3d`
        annotate_accessories_2d: :attr:`annotate_accessories_2d`
        annotate_accessories_3d: :attr:`annotate_accessories_3d`
        apply_lidar_noise: :attr:`apply_lidar_noise`
        bbox_2d_only_visible_pixels: :attr:`bbox_2d_only_visible_pixels`
        capture_all_frames: :attr:`capture_all_frames`
        keep_glass_transparent: :attr:`keep_glass_transparent`
        hide_all_volumetrics: :attr:`hide_all_volumetrics`
        merge_bikes_riders_3d: :attr:`merge_bikes_riders_3d`
        output_instance_point_caches: :attr:`output_instance_point_caches`
        use_instance_point_caches: :attr:`use_instance_point_caches`
        output_telemetry: :attr:`output_telemetry`
        output_truncated_3d_annotations: :attr:`output_truncated_3d_annotations`
        physical_ground_truth: :attr:`physical_ground_truth`
        volumetric_density_scale: :attr:`volumetric_density_scale`
        render_ego_vehicle: :attr:`render_ego_vehicle`
        use_opaque_glass: :attr:`use_opaque_glass`
        vehicle_color_offset: :attr:`vehicle_color_offset`
        hide_crosswalk_segmentation_mesh: :attr:`hide_crosswalk_segmentation_mesh`
        disable_reflection: :attr:`disable_reflection`
        disable_specular: :attr:`disable_specular`
        box_non_visible_signal_bulbs: :attr:`box_non_visible_signal_bulbs`
        enable_radar_debug: :attr:`enable_radar_debug`
        environment_mode: :attr:`environment_mode`
        environment_attr_list: :attr:`environment_attr_list`
        start_scene: :attr:`start_scene`
        end_scene: :attr:`end_scene`
        batch_size: :attr:`batch_size`
        generate_previews: :attr:`generate_previews`
        capture_rate: :attr:`capture_rate`
        new_data_pipeline: :attr:`new_data_pipeline`
        use_linux: :attr:`use_linux`
        use_lidar_rolling_shutter: :attr:`use_lidar_rolling_shutter`
    Attributes:
        artifact_key:
        output_artifact_uid:
        state_file_archive_artifact_uid:
        code_build_artifact_uid:
        image_generator_core_artifact_uid:
        level_pak_artifact_uid:
        sensor_rig:
        sensor_splits_list:
        use_high_gpu_mem_render_node: Parameter used to control which instance type to set when rendering. This
            is a temporary parameter and will be depreciated once PD-15262 is done.
        annotate_wing_mirrors_2d:
        annotate_wing_mirrors_3d:
        annotate_accessories_2d:
        annotate_accessories_3d:
        apply_lidar_noise:
        bbox_2d_only_visible_pixels:
        capture_all_frames:
        keep_glass_transparent:
        hide_all_volumetrics:
        merge_bikes_riders_3d:
        output_instance_point_caches:
        use_instance_point_caches:
        output_telemetry:
        output_truncated_3d_annotations:
        physical_ground_truth:
        volumetric_density_scale:
        render_ego_vehicle:
        use_opaque_glass:
        vehicle_color_offset:
        hide_crosswalk_segmentation_mesh:
        disable_reflection:
        disable_specular:
        box_non_visible_signal_bulbs:
        enable_radar_debug:
        environment_mode:
        environment_attr_list:
        start_scene:
        end_scene:
        batch_size:
        generate_previews:
        capture_rate:
        new_data_pipeline: Set to True to enable the updated data pipeline
            from the IG
        use_linux: Set use_linux to True if you want to run a render on Linux instead of Windows
        use_lidar_rolling_shutter: Whether to use rolling shutter effects in the LiDAR rendering
            For batch mode we should disable the LiDAR rolling shutter"""

    class EnvironmentMode(ProtoEnumClass):
        NONE = 0
        SPREAD = 1
        CYCLE = 2
        RANDOM = 3

    @register_wrapper(proto_type=pd_render_pb2.RenderInfo.Environment)
    class Environment(ProtoMessageClass):
        """
        Args:
            environment_attr: :attr:`environment_attr`
        Attributes:
            environment_attr:"""

        _proto_message = pd_render_pb2.RenderInfo.Environment

        def __init__(
            self,
            *,
            proto: Optional[pd_render_pb2.RenderInfo.Environment] = None,
            environment_attr: Dict[str, str] = None,
        ):
            if proto is None:
                proto = pd_render_pb2.RenderInfo.Environment()
            self.proto = proto
            self._environment_attr = ProtoDictWrapper(
                container={k: str(v) for (k, v) in proto.environment_attr.items()},
                attr_name="environment_attr",
                dict_owner=self,
            )
            if environment_attr is not None:
                self.environment_attr = environment_attr

        @property
        def environment_attr(self) -> Dict[str, str]:
            return self._environment_attr

        @environment_attr.setter
        def environment_attr(self, value: Dict[str, str]):
            self._environment_attr.clear()
            self._environment_attr.update(value)

        def _update_proto_references(self, proto: pd_render_pb2.RenderInfo.Environment):
            self.proto = proto

    _proto_message = pd_render_pb2.RenderInfo

    def __init__(
        self,
        *,
        proto: Optional[pd_render_pb2.RenderInfo] = None,
        artifact_key: str = None,
        output_artifact_uid: str = None,
        state_file_archive_artifact_uid: str = None,
        code_build_artifact_uid: str = None,
        image_generator_core_artifact_uid: str = None,
        level_pak_artifact_uid: Dict[str, str] = None,
        sensor_rig: _pd_sensor_pb2.SensorRigConfig = None,
        sensor_splits_list: List[_pd_sensor_pb2.SensorList] = None,
        use_high_gpu_mem_render_node: bool = None,
        annotate_wing_mirrors_2d: bool = None,
        annotate_wing_mirrors_3d: bool = None,
        annotate_accessories_2d: bool = None,
        annotate_accessories_3d: bool = None,
        apply_lidar_noise: bool = None,
        bbox_2d_only_visible_pixels: bool = None,
        capture_all_frames: bool = None,
        keep_glass_transparent: bool = None,
        hide_all_volumetrics: bool = None,
        merge_bikes_riders_3d: bool = None,
        output_instance_point_caches: bool = None,
        use_instance_point_caches: bool = None,
        output_telemetry: bool = None,
        output_truncated_3d_annotations: bool = None,
        physical_ground_truth: bool = None,
        volumetric_density_scale: float = None,
        render_ego_vehicle: bool = None,
        use_opaque_glass: int = None,
        vehicle_color_offset: int = None,
        hide_crosswalk_segmentation_mesh: bool = None,
        disable_reflection: bool = None,
        disable_specular: bool = None,
        box_non_visible_signal_bulbs: bool = None,
        enable_radar_debug: bool = None,
        environment_mode: RenderInfo.EnvironmentMode = None,
        environment_attr_list: List[RenderInfo.Environment] = None,
        start_scene: int = None,
        end_scene: int = None,
        batch_size: int = None,
        generate_previews: bool = None,
        capture_rate: int = None,
        new_data_pipeline: bool = None,
        use_linux: bool = None,
        use_lidar_rolling_shutter: bool = None,
    ):
        if proto is None:
            proto = pd_render_pb2.RenderInfo()
        self.proto = proto
        self._sensor_rig = get_wrapper(proto_type=proto.sensor_rig.__class__)(proto=proto.sensor_rig)
        self._sensor_splits_list = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensor_splits_list],
            attr_name="sensor_splits_list",
            list_owner=self,
        )
        self._environment_attr_list = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.environment_attr_list],
            attr_name="environment_attr_list",
            list_owner=self,
        )
        if artifact_key is not None:
            self.artifact_key = artifact_key
        if output_artifact_uid is not None:
            self.output_artifact_uid = output_artifact_uid
        if state_file_archive_artifact_uid is not None:
            self.state_file_archive_artifact_uid = state_file_archive_artifact_uid
        if code_build_artifact_uid is not None:
            self.code_build_artifact_uid = code_build_artifact_uid
        if image_generator_core_artifact_uid is not None:
            self.image_generator_core_artifact_uid = image_generator_core_artifact_uid
        self._level_pak_artifact_uid = ProtoDictWrapper(
            container={k: str(v) for (k, v) in proto.level_pak_artifact_uid.items()},
            attr_name="level_pak_artifact_uid",
            dict_owner=self,
        )
        if level_pak_artifact_uid is not None:
            self.level_pak_artifact_uid = level_pak_artifact_uid
        if sensor_rig is not None:
            self.sensor_rig = sensor_rig
        if sensor_splits_list is not None:
            self.sensor_splits_list = sensor_splits_list
        if use_high_gpu_mem_render_node is not None:
            self.use_high_gpu_mem_render_node = use_high_gpu_mem_render_node
        if annotate_wing_mirrors_2d is not None:
            self.annotate_wing_mirrors_2d = annotate_wing_mirrors_2d
        if annotate_wing_mirrors_3d is not None:
            self.annotate_wing_mirrors_3d = annotate_wing_mirrors_3d
        if annotate_accessories_2d is not None:
            self.annotate_accessories_2d = annotate_accessories_2d
        if annotate_accessories_3d is not None:
            self.annotate_accessories_3d = annotate_accessories_3d
        if apply_lidar_noise is not None:
            self.apply_lidar_noise = apply_lidar_noise
        if bbox_2d_only_visible_pixels is not None:
            self.bbox_2d_only_visible_pixels = bbox_2d_only_visible_pixels
        if capture_all_frames is not None:
            self.capture_all_frames = capture_all_frames
        if keep_glass_transparent is not None:
            self.keep_glass_transparent = keep_glass_transparent
        if hide_all_volumetrics is not None:
            self.hide_all_volumetrics = hide_all_volumetrics
        if merge_bikes_riders_3d is not None:
            self.merge_bikes_riders_3d = merge_bikes_riders_3d
        if output_instance_point_caches is not None:
            self.output_instance_point_caches = output_instance_point_caches
        if use_instance_point_caches is not None:
            self.use_instance_point_caches = use_instance_point_caches
        if output_telemetry is not None:
            self.output_telemetry = output_telemetry
        if output_truncated_3d_annotations is not None:
            self.output_truncated_3d_annotations = output_truncated_3d_annotations
        if physical_ground_truth is not None:
            self.physical_ground_truth = physical_ground_truth
        if volumetric_density_scale is not None:
            self.volumetric_density_scale = volumetric_density_scale
        if render_ego_vehicle is not None:
            self.render_ego_vehicle = render_ego_vehicle
        if use_opaque_glass is not None:
            self.use_opaque_glass = use_opaque_glass
        if vehicle_color_offset is not None:
            self.vehicle_color_offset = vehicle_color_offset
        if hide_crosswalk_segmentation_mesh is not None:
            self.hide_crosswalk_segmentation_mesh = hide_crosswalk_segmentation_mesh
        if disable_reflection is not None:
            self.disable_reflection = disable_reflection
        if disable_specular is not None:
            self.disable_specular = disable_specular
        if box_non_visible_signal_bulbs is not None:
            self.box_non_visible_signal_bulbs = box_non_visible_signal_bulbs
        if enable_radar_debug is not None:
            self.enable_radar_debug = enable_radar_debug
        if environment_mode is not None:
            self.environment_mode = environment_mode
        if environment_attr_list is not None:
            self.environment_attr_list = environment_attr_list
        if start_scene is not None:
            self.start_scene = start_scene
        if end_scene is not None:
            self.end_scene = end_scene
        if batch_size is not None:
            self.batch_size = batch_size
        if generate_previews is not None:
            self.generate_previews = generate_previews
        if capture_rate is not None:
            self.capture_rate = capture_rate
        if new_data_pipeline is not None:
            self.new_data_pipeline = new_data_pipeline
        if use_linux is not None:
            self.use_linux = use_linux
        if use_lidar_rolling_shutter is not None:
            self.use_lidar_rolling_shutter = use_lidar_rolling_shutter

    @property
    def artifact_key(self) -> str:
        return self.proto.artifact_key

    @artifact_key.setter
    def artifact_key(self, value: str):
        self.proto.artifact_key = value

    @property
    def output_artifact_uid(self) -> str:
        return self.proto.output_artifact_uid

    @output_artifact_uid.setter
    def output_artifact_uid(self, value: str):
        self.proto.output_artifact_uid = value

    @property
    def state_file_archive_artifact_uid(self) -> str:
        return self.proto.state_file_archive_artifact_uid

    @state_file_archive_artifact_uid.setter
    def state_file_archive_artifact_uid(self, value: str):
        self.proto.state_file_archive_artifact_uid = value

    @property
    def code_build_artifact_uid(self) -> str:
        return self.proto.code_build_artifact_uid

    @code_build_artifact_uid.setter
    def code_build_artifact_uid(self, value: str):
        self.proto.code_build_artifact_uid = value

    @property
    def image_generator_core_artifact_uid(self) -> str:
        return self.proto.image_generator_core_artifact_uid

    @image_generator_core_artifact_uid.setter
    def image_generator_core_artifact_uid(self, value: str):
        self.proto.image_generator_core_artifact_uid = value

    @property
    def level_pak_artifact_uid(self) -> Dict[str, str]:
        return self._level_pak_artifact_uid

    @level_pak_artifact_uid.setter
    def level_pak_artifact_uid(self, value: Dict[str, str]):
        self._level_pak_artifact_uid.clear()
        self._level_pak_artifact_uid.update(value)

    @property
    def sensor_rig(self) -> _pd_sensor_pb2.SensorRigConfig:
        return self._sensor_rig

    @sensor_rig.setter
    def sensor_rig(self, value: _pd_sensor_pb2.SensorRigConfig):
        self.proto.sensor_rig.CopyFrom(value.proto)

        self._sensor_rig = value
        self._sensor_rig._update_proto_references(self.proto.sensor_rig)

    @property
    def sensor_splits_list(self) -> List[_pd_sensor_pb2.SensorList]:
        return self._sensor_splits_list

    @sensor_splits_list.setter
    def sensor_splits_list(self, value: List[_pd_sensor_pb2.SensorList]):
        self._sensor_splits_list.clear()
        for v in value:
            self._sensor_splits_list.append(v)

    @property
    def use_high_gpu_mem_render_node(self) -> bool:
        return self.proto.use_high_gpu_mem_render_node

    @use_high_gpu_mem_render_node.setter
    def use_high_gpu_mem_render_node(self, value: bool):
        self.proto.use_high_gpu_mem_render_node = value

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
    def apply_lidar_noise(self) -> bool:
        return self.proto.apply_lidar_noise

    @apply_lidar_noise.setter
    def apply_lidar_noise(self, value: bool):
        self.proto.apply_lidar_noise = value

    @property
    def bbox_2d_only_visible_pixels(self) -> bool:
        return self.proto.bbox_2d_only_visible_pixels

    @bbox_2d_only_visible_pixels.setter
    def bbox_2d_only_visible_pixels(self, value: bool):
        self.proto.bbox_2d_only_visible_pixels = value

    @property
    def capture_all_frames(self) -> bool:
        return self.proto.capture_all_frames

    @capture_all_frames.setter
    def capture_all_frames(self, value: bool):
        self.proto.capture_all_frames = value

    @property
    def keep_glass_transparent(self) -> bool:
        return self.proto.keep_glass_transparent

    @keep_glass_transparent.setter
    def keep_glass_transparent(self, value: bool):
        self.proto.keep_glass_transparent = value

    @property
    def hide_all_volumetrics(self) -> bool:
        return self.proto.hide_all_volumetrics

    @hide_all_volumetrics.setter
    def hide_all_volumetrics(self, value: bool):
        self.proto.hide_all_volumetrics = value

    @property
    def merge_bikes_riders_3d(self) -> bool:
        return self.proto.merge_bikes_riders_3d

    @merge_bikes_riders_3d.setter
    def merge_bikes_riders_3d(self, value: bool):
        self.proto.merge_bikes_riders_3d = value

    @property
    def output_instance_point_caches(self) -> bool:
        return self.proto.output_instance_point_caches

    @output_instance_point_caches.setter
    def output_instance_point_caches(self, value: bool):
        self.proto.output_instance_point_caches = value

    @property
    def use_instance_point_caches(self) -> bool:
        return self.proto.use_instance_point_caches

    @use_instance_point_caches.setter
    def use_instance_point_caches(self, value: bool):
        self.proto.use_instance_point_caches = value

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
    def volumetric_density_scale(self) -> float:
        return self.proto.volumetric_density_scale

    @volumetric_density_scale.setter
    def volumetric_density_scale(self, value: float):
        self.proto.volumetric_density_scale = value

    @property
    def render_ego_vehicle(self) -> bool:
        return self.proto.render_ego_vehicle

    @render_ego_vehicle.setter
    def render_ego_vehicle(self, value: bool):
        self.proto.render_ego_vehicle = value

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
    def hide_crosswalk_segmentation_mesh(self) -> bool:
        return self.proto.hide_crosswalk_segmentation_mesh

    @hide_crosswalk_segmentation_mesh.setter
    def hide_crosswalk_segmentation_mesh(self, value: bool):
        self.proto.hide_crosswalk_segmentation_mesh = value

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
    def box_non_visible_signal_bulbs(self) -> bool:
        return self.proto.box_non_visible_signal_bulbs

    @box_non_visible_signal_bulbs.setter
    def box_non_visible_signal_bulbs(self, value: bool):
        self.proto.box_non_visible_signal_bulbs = value

    @property
    def enable_radar_debug(self) -> bool:
        return self.proto.enable_radar_debug

    @enable_radar_debug.setter
    def enable_radar_debug(self, value: bool):
        self.proto.enable_radar_debug = value

    @property
    def environment_mode(self) -> RenderInfo.EnvironmentMode:
        return self.proto.environment_mode

    @environment_mode.setter
    def environment_mode(self, value: RenderInfo.EnvironmentMode):
        self.proto.environment_mode = value

    @property
    def environment_attr_list(self) -> List[RenderInfo.Environment]:
        return self._environment_attr_list

    @environment_attr_list.setter
    def environment_attr_list(self, value: List[RenderInfo.Environment]):
        self._environment_attr_list.clear()
        for v in value:
            self._environment_attr_list.append(v)

    @property
    def start_scene(self) -> int:
        return self.proto.start_scene

    @start_scene.setter
    def start_scene(self, value: int):
        self.proto.start_scene = value

    @property
    def end_scene(self) -> int:
        return self.proto.end_scene

    @end_scene.setter
    def end_scene(self, value: int):
        self.proto.end_scene = value

    @property
    def batch_size(self) -> int:
        return self.proto.batch_size

    @batch_size.setter
    def batch_size(self, value: int):
        self.proto.batch_size = value

    @property
    def generate_previews(self) -> bool:
        return self.proto.generate_previews

    @generate_previews.setter
    def generate_previews(self, value: bool):
        self.proto.generate_previews = value

    @property
    def capture_rate(self) -> int:
        return self.proto.capture_rate

    @capture_rate.setter
    def capture_rate(self, value: int):
        self.proto.capture_rate = value

    @property
    def new_data_pipeline(self) -> bool:
        return self.proto.new_data_pipeline

    @new_data_pipeline.setter
    def new_data_pipeline(self, value: bool):
        self.proto.new_data_pipeline = value

    @property
    def use_linux(self) -> bool:
        return self.proto.use_linux

    @use_linux.setter
    def use_linux(self, value: bool):
        self.proto.use_linux = value

    @property
    def use_lidar_rolling_shutter(self) -> bool:
        return self.proto.use_lidar_rolling_shutter

    @use_lidar_rolling_shutter.setter
    def use_lidar_rolling_shutter(self, value: bool):
        self.proto.use_lidar_rolling_shutter = value

    def _update_proto_references(self, proto: pd_render_pb2.RenderInfo):
        self.proto = proto
        self._sensor_rig._update_proto_references(proto.sensor_rig)
        for i, v in enumerate(self.sensor_splits_list):
            v._update_proto_references(self.proto.sensor_splits_list[i])
        for i, v in enumerate(self.environment_attr_list):
            v._update_proto_references(self.proto.environment_attr_list[i])
