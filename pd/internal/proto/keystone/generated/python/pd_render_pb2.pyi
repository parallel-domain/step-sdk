import pd_sensor_pb2 as _pd_sensor_pb2
from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor
KEYSTONE_ATTRIBUTES_FIELD_NUMBER: ClassVar[int]
keystone_attributes: _descriptor.FieldDescriptor

class KeystoneAttributes(_message.Message):
    __slots__ = ["group"]
    GROUP_FIELD_NUMBER: ClassVar[int]
    group: str
    def __init__(self, group: Optional[str] = ...) -> None: ...

class RenderInfo(_message.Message):
    __slots__ = ["annotate_accessories_2d", "annotate_accessories_3d", "annotate_wing_mirrors_2d", "annotate_wing_mirrors_3d", "apply_lidar_noise", "artifact_key", "batch_size", "bbox_2d_only_visible_pixels", "box_non_visible_signal_bulbs", "capture_all_frames", "capture_rate", "code_build_artifact_uid", "disable_reflection", "disable_specular", "enable_radar_debug", "end_scene", "environment_attr_list", "environment_mode", "generate_previews", "hide_all_volumetrics", "hide_crosswalk_segmentation_mesh", "image_generator_core_artifact_uid", "keep_glass_transparent", "level_pak_artifact_uid", "merge_bikes_riders_3d", "new_data_pipeline", "output_artifact_uid", "output_instance_point_caches", "output_telemetry", "output_truncated_3d_annotations", "physical_ground_truth", "render_ego_vehicle", "sensor_rig", "sensor_splits_list", "start_scene", "state_file_archive_artifact_uid", "use_high_gpu_mem_render_node", "use_instance_point_caches", "use_opaque_glass", "vehicle_color_offset", "volumetric_density_scale"]
    class EnvironmentMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Environment(_message.Message):
        __slots__ = ["environment_attr"]
        class EnvironmentAttrEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: ClassVar[int]
            VALUE_FIELD_NUMBER: ClassVar[int]
            key: str
            value: str
            def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
        ENVIRONMENT_ATTR_FIELD_NUMBER: ClassVar[int]
        environment_attr: _containers.ScalarMap[str, str]
        def __init__(self, environment_attr: Optional[Mapping[str, str]] = ...) -> None: ...
    class LevelPakArtifactUidEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    ANNOTATE_ACCESSORIES_2D_FIELD_NUMBER: ClassVar[int]
    ANNOTATE_ACCESSORIES_3D_FIELD_NUMBER: ClassVar[int]
    ANNOTATE_WING_MIRRORS_2D_FIELD_NUMBER: ClassVar[int]
    ANNOTATE_WING_MIRRORS_3D_FIELD_NUMBER: ClassVar[int]
    APPLY_LIDAR_NOISE_FIELD_NUMBER: ClassVar[int]
    ARTIFACT_KEY_FIELD_NUMBER: ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: ClassVar[int]
    BBOX_2D_ONLY_VISIBLE_PIXELS_FIELD_NUMBER: ClassVar[int]
    BOX_NON_VISIBLE_SIGNAL_BULBS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_ALL_FRAMES_FIELD_NUMBER: ClassVar[int]
    CAPTURE_RATE_FIELD_NUMBER: ClassVar[int]
    CODE_BUILD_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    CYCLE: RenderInfo.EnvironmentMode
    DISABLE_REFLECTION_FIELD_NUMBER: ClassVar[int]
    DISABLE_SPECULAR_FIELD_NUMBER: ClassVar[int]
    ENABLE_RADAR_DEBUG_FIELD_NUMBER: ClassVar[int]
    END_SCENE_FIELD_NUMBER: ClassVar[int]
    ENVIRONMENT_ATTR_LIST_FIELD_NUMBER: ClassVar[int]
    ENVIRONMENT_MODE_FIELD_NUMBER: ClassVar[int]
    GENERATE_PREVIEWS_FIELD_NUMBER: ClassVar[int]
    HIDE_ALL_VOLUMETRICS_FIELD_NUMBER: ClassVar[int]
    HIDE_CROSSWALK_SEGMENTATION_MESH_FIELD_NUMBER: ClassVar[int]
    IMAGE_GENERATOR_CORE_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    KEEP_GLASS_TRANSPARENT_FIELD_NUMBER: ClassVar[int]
    LEVEL_PAK_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    MERGE_BIKES_RIDERS_3D_FIELD_NUMBER: ClassVar[int]
    NEW_DATA_PIPELINE_FIELD_NUMBER: ClassVar[int]
    NONE: RenderInfo.EnvironmentMode
    OUTPUT_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    OUTPUT_INSTANCE_POINT_CACHES_FIELD_NUMBER: ClassVar[int]
    OUTPUT_TELEMETRY_FIELD_NUMBER: ClassVar[int]
    OUTPUT_TRUNCATED_3D_ANNOTATIONS_FIELD_NUMBER: ClassVar[int]
    PHYSICAL_GROUND_TRUTH_FIELD_NUMBER: ClassVar[int]
    RANDOM: RenderInfo.EnvironmentMode
    RENDER_EGO_VEHICLE_FIELD_NUMBER: ClassVar[int]
    SENSOR_RIG_FIELD_NUMBER: ClassVar[int]
    SENSOR_SPLITS_LIST_FIELD_NUMBER: ClassVar[int]
    SPREAD: RenderInfo.EnvironmentMode
    START_SCENE_FIELD_NUMBER: ClassVar[int]
    STATE_FILE_ARCHIVE_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    USE_HIGH_GPU_MEM_RENDER_NODE_FIELD_NUMBER: ClassVar[int]
    USE_INSTANCE_POINT_CACHES_FIELD_NUMBER: ClassVar[int]
    USE_OPAQUE_GLASS_FIELD_NUMBER: ClassVar[int]
    VEHICLE_COLOR_OFFSET_FIELD_NUMBER: ClassVar[int]
    VOLUMETRIC_DENSITY_SCALE_FIELD_NUMBER: ClassVar[int]
    annotate_accessories_2d: bool
    annotate_accessories_3d: bool
    annotate_wing_mirrors_2d: bool
    annotate_wing_mirrors_3d: bool
    apply_lidar_noise: bool
    artifact_key: str
    batch_size: int
    bbox_2d_only_visible_pixels: bool
    box_non_visible_signal_bulbs: bool
    capture_all_frames: bool
    capture_rate: int
    code_build_artifact_uid: str
    disable_reflection: bool
    disable_specular: bool
    enable_radar_debug: bool
    end_scene: int
    environment_attr_list: _containers.RepeatedCompositeFieldContainer[RenderInfo.Environment]
    environment_mode: RenderInfo.EnvironmentMode
    generate_previews: bool
    hide_all_volumetrics: bool
    hide_crosswalk_segmentation_mesh: bool
    image_generator_core_artifact_uid: str
    keep_glass_transparent: bool
    level_pak_artifact_uid: _containers.ScalarMap[str, str]
    merge_bikes_riders_3d: bool
    new_data_pipeline: bool
    output_artifact_uid: str
    output_instance_point_caches: bool
    output_telemetry: bool
    output_truncated_3d_annotations: bool
    physical_ground_truth: bool
    render_ego_vehicle: bool
    sensor_rig: _pd_sensor_pb2.SensorRigConfig
    sensor_splits_list: _containers.RepeatedCompositeFieldContainer[_pd_sensor_pb2.SensorList]
    start_scene: int
    state_file_archive_artifact_uid: str
    use_high_gpu_mem_render_node: bool
    use_instance_point_caches: bool
    use_opaque_glass: int
    vehicle_color_offset: int
    volumetric_density_scale: float
    def __init__(self, artifact_key: Optional[str] = ..., output_artifact_uid: Optional[str] = ..., state_file_archive_artifact_uid: Optional[str] = ..., code_build_artifact_uid: Optional[str] = ..., image_generator_core_artifact_uid: Optional[str] = ..., level_pak_artifact_uid: Optional[Mapping[str, str]] = ..., sensor_rig: Optional[Union[_pd_sensor_pb2.SensorRigConfig, Mapping]] = ..., sensor_splits_list: Optional[Iterable[Union[_pd_sensor_pb2.SensorList, Mapping]]] = ..., use_high_gpu_mem_render_node: bool = ..., annotate_wing_mirrors_2d: bool = ..., annotate_wing_mirrors_3d: bool = ..., annotate_accessories_2d: bool = ..., annotate_accessories_3d: bool = ..., apply_lidar_noise: bool = ..., bbox_2d_only_visible_pixels: bool = ..., capture_all_frames: bool = ..., keep_glass_transparent: bool = ..., hide_all_volumetrics: bool = ..., merge_bikes_riders_3d: bool = ..., output_instance_point_caches: bool = ..., use_instance_point_caches: bool = ..., output_telemetry: bool = ..., output_truncated_3d_annotations: bool = ..., physical_ground_truth: bool = ..., volumetric_density_scale: Optional[float] = ..., render_ego_vehicle: bool = ..., use_opaque_glass: Optional[int] = ..., vehicle_color_offset: Optional[int] = ..., hide_crosswalk_segmentation_mesh: bool = ..., disable_reflection: bool = ..., disable_specular: bool = ..., box_non_visible_signal_bulbs: bool = ..., enable_radar_debug: bool = ..., environment_mode: Optional[Union[RenderInfo.EnvironmentMode, str]] = ..., environment_attr_list: Optional[Iterable[Union[RenderInfo.Environment, Mapping]]] = ..., start_scene: Optional[int] = ..., end_scene: Optional[int] = ..., batch_size: Optional[int] = ..., generate_previews: bool = ..., capture_rate: Optional[int] = ..., new_data_pipeline: bool = ...) -> None: ...
