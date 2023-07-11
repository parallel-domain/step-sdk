from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

AVERAGE_FILTER: DenoiseFilter
BILATERAL_FILTER: DenoiseFilter
DESCRIPTOR: _descriptor.FileDescriptor
FAST_MEDIAN_FILTER: DenoiseFilter
MEDIAN_FILTER: DenoiseFilter

class AlbedoWeights(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ...) -> None: ...

class AliceLidarModel(_message.Message):
    __slots__ = ["dense_radian_spacing", "horizontal_spacing", "max_azimuth_angle", "max_dense_elevation_angle", "max_elevation_angle", "min_azimuth_angle", "min_dense_elevation_angle", "min_elevation_angle", "number_points", "sparse_radian_spacing"]
    DENSE_RADIAN_SPACING_FIELD_NUMBER: ClassVar[int]
    HORIZONTAL_SPACING_FIELD_NUMBER: ClassVar[int]
    MAX_AZIMUTH_ANGLE_FIELD_NUMBER: ClassVar[int]
    MAX_DENSE_ELEVATION_ANGLE_FIELD_NUMBER: ClassVar[int]
    MAX_ELEVATION_ANGLE_FIELD_NUMBER: ClassVar[int]
    MIN_AZIMUTH_ANGLE_FIELD_NUMBER: ClassVar[int]
    MIN_DENSE_ELEVATION_ANGLE_FIELD_NUMBER: ClassVar[int]
    MIN_ELEVATION_ANGLE_FIELD_NUMBER: ClassVar[int]
    NUMBER_POINTS_FIELD_NUMBER: ClassVar[int]
    SPARSE_RADIAN_SPACING_FIELD_NUMBER: ClassVar[int]
    dense_radian_spacing: float
    horizontal_spacing: float
    max_azimuth_angle: float
    max_dense_elevation_angle: float
    max_elevation_angle: float
    min_azimuth_angle: float
    min_dense_elevation_angle: float
    min_elevation_angle: float
    number_points: int
    sparse_radian_spacing: float
    def __init__(self, number_points: Optional[int] = ..., min_elevation_angle: Optional[float] = ..., max_elevation_angle: Optional[float] = ..., min_dense_elevation_angle: Optional[float] = ..., max_dense_elevation_angle: Optional[float] = ..., min_azimuth_angle: Optional[float] = ..., max_azimuth_angle: Optional[float] = ..., sparse_radian_spacing: Optional[float] = ..., dense_radian_spacing: Optional[float] = ..., horizontal_spacing: Optional[float] = ...) -> None: ...

class CameraIntrinsic(_message.Message):
    __slots__ = ["capture_backwardmotionvectors", "capture_basecolor", "capture_depth", "capture_detections", "capture_instance", "capture_motionvectors", "capture_normals", "capture_properties", "capture_rgb", "capture_segmentation", "distortion_lookup_table", "distortion_params", "enable_streaming", "fov", "height", "lut", "lut_weight", "noise_params", "post_process", "post_process_params", "supersample", "time_offset", "transmit_gray", "width"]
    CAPTURE_BACKWARDMOTIONVECTORS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_BASECOLOR_FIELD_NUMBER: ClassVar[int]
    CAPTURE_DEPTH_FIELD_NUMBER: ClassVar[int]
    CAPTURE_DETECTIONS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_INSTANCE_FIELD_NUMBER: ClassVar[int]
    CAPTURE_MOTIONVECTORS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_NORMALS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_PROPERTIES_FIELD_NUMBER: ClassVar[int]
    CAPTURE_RGB_FIELD_NUMBER: ClassVar[int]
    CAPTURE_SEGMENTATION_FIELD_NUMBER: ClassVar[int]
    DISTORTION_LOOKUP_TABLE_FIELD_NUMBER: ClassVar[int]
    DISTORTION_PARAMS_FIELD_NUMBER: ClassVar[int]
    ENABLE_STREAMING_FIELD_NUMBER: ClassVar[int]
    FOV_FIELD_NUMBER: ClassVar[int]
    HEIGHT_FIELD_NUMBER: ClassVar[int]
    LUT_FIELD_NUMBER: ClassVar[int]
    LUT_WEIGHT_FIELD_NUMBER: ClassVar[int]
    NOISE_PARAMS_FIELD_NUMBER: ClassVar[int]
    POST_PROCESS_FIELD_NUMBER: ClassVar[int]
    POST_PROCESS_PARAMS_FIELD_NUMBER: ClassVar[int]
    SUPERSAMPLE_FIELD_NUMBER: ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: ClassVar[int]
    TRANSMIT_GRAY_FIELD_NUMBER: ClassVar[int]
    WIDTH_FIELD_NUMBER: ClassVar[int]
    capture_backwardmotionvectors: bool
    capture_basecolor: bool
    capture_depth: bool
    capture_detections: bool
    capture_instance: bool
    capture_motionvectors: bool
    capture_normals: bool
    capture_properties: bool
    capture_rgb: bool
    capture_segmentation: bool
    distortion_lookup_table: str
    distortion_params: DistortionParams
    enable_streaming: bool
    fov: float
    height: int
    lut: str
    lut_weight: float
    noise_params: NoiseParams
    post_process: _containers.RepeatedCompositeFieldContainer[PostProcessNode]
    post_process_params: PostProcessParams
    supersample: float
    time_offset: float
    transmit_gray: bool
    width: int
    def __init__(self, width: Optional[int] = ..., height: Optional[int] = ..., fov: Optional[float] = ..., supersample: Optional[float] = ..., capture_rgb: bool = ..., capture_depth: bool = ..., capture_normals: bool = ..., capture_segmentation: bool = ..., capture_instance: bool = ..., capture_detections: bool = ..., capture_motionvectors: bool = ..., lut: Optional[str] = ..., lut_weight: Optional[float] = ..., post_process_params: Optional[Union[PostProcessParams, Mapping]] = ..., post_process: Optional[Iterable[Union[PostProcessNode, Mapping]]] = ..., distortion_params: Optional[Union[DistortionParams, Mapping]] = ..., noise_params: Optional[Union[NoiseParams, Mapping]] = ..., enable_streaming: bool = ..., transmit_gray: bool = ..., distortion_lookup_table: Optional[str] = ..., capture_basecolor: bool = ..., capture_properties: bool = ..., time_offset: Optional[float] = ..., capture_backwardmotionvectors: bool = ...) -> None: ...

class DistortionParams(_message.Message):
    __slots__ = ["cx", "cy", "fisheye_model", "fx", "fy", "is_fisheye", "k1", "k2", "k3", "k4", "k5", "k6", "p1", "p2", "skew"]
    CX_FIELD_NUMBER: ClassVar[int]
    CY_FIELD_NUMBER: ClassVar[int]
    FISHEYE_MODEL_FIELD_NUMBER: ClassVar[int]
    FX_FIELD_NUMBER: ClassVar[int]
    FY_FIELD_NUMBER: ClassVar[int]
    IS_FISHEYE_FIELD_NUMBER: ClassVar[int]
    K1_FIELD_NUMBER: ClassVar[int]
    K2_FIELD_NUMBER: ClassVar[int]
    K3_FIELD_NUMBER: ClassVar[int]
    K4_FIELD_NUMBER: ClassVar[int]
    K5_FIELD_NUMBER: ClassVar[int]
    K6_FIELD_NUMBER: ClassVar[int]
    P1_FIELD_NUMBER: ClassVar[int]
    P2_FIELD_NUMBER: ClassVar[int]
    SKEW_FIELD_NUMBER: ClassVar[int]
    cx: float
    cy: float
    fisheye_model: int
    fx: float
    fy: float
    is_fisheye: bool
    k1: float
    k2: float
    k3: float
    k4: float
    k5: float
    k6: float
    p1: float
    p2: float
    skew: float
    def __init__(self, k1: Optional[float] = ..., k2: Optional[float] = ..., k3: Optional[float] = ..., k4: Optional[float] = ..., k5: Optional[float] = ..., k6: Optional[float] = ..., p1: Optional[float] = ..., p2: Optional[float] = ..., skew: Optional[float] = ..., is_fisheye: bool = ..., fx: Optional[float] = ..., fy: Optional[float] = ..., cx: Optional[float] = ..., cy: Optional[float] = ..., fisheye_model: Optional[int] = ...) -> None: ...

class LidarBeam(_message.Message):
    __slots__ = ["azimuth", "elevation", "id"]
    AZIMUTH_FIELD_NUMBER: ClassVar[int]
    ELEVATION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    azimuth: float
    elevation: float
    id: int
    def __init__(self, id: Optional[int] = ..., azimuth: Optional[float] = ..., elevation: Optional[float] = ...) -> None: ...

class LidarIntensityParams(_message.Message):
    __slots__ = ["albedo_weights", "beam_intensity", "emissive_gate", "intensity_metallic_scale", "intensity_roughness_scale", "intensity_specular_scale", "max_albedo", "max_attenuation_distance", "max_emissive_rate", "retro_intensity_enhance", "retro_range_noise_stddev", "retroreflection_noise_mean", "retroreflection_noise_stddev", "strong_retro_intensity_enhance"]
    ALBEDO_WEIGHTS_FIELD_NUMBER: ClassVar[int]
    BEAM_INTENSITY_FIELD_NUMBER: ClassVar[int]
    EMISSIVE_GATE_FIELD_NUMBER: ClassVar[int]
    INTENSITY_METALLIC_SCALE_FIELD_NUMBER: ClassVar[int]
    INTENSITY_ROUGHNESS_SCALE_FIELD_NUMBER: ClassVar[int]
    INTENSITY_SPECULAR_SCALE_FIELD_NUMBER: ClassVar[int]
    MAX_ALBEDO_FIELD_NUMBER: ClassVar[int]
    MAX_ATTENUATION_DISTANCE_FIELD_NUMBER: ClassVar[int]
    MAX_EMISSIVE_RATE_FIELD_NUMBER: ClassVar[int]
    RETROREFLECTION_NOISE_MEAN_FIELD_NUMBER: ClassVar[int]
    RETROREFLECTION_NOISE_STDDEV_FIELD_NUMBER: ClassVar[int]
    RETRO_INTENSITY_ENHANCE_FIELD_NUMBER: ClassVar[int]
    RETRO_RANGE_NOISE_STDDEV_FIELD_NUMBER: ClassVar[int]
    STRONG_RETRO_INTENSITY_ENHANCE_FIELD_NUMBER: ClassVar[int]
    albedo_weights: AlbedoWeights
    beam_intensity: float
    emissive_gate: float
    intensity_metallic_scale: float
    intensity_roughness_scale: float
    intensity_specular_scale: float
    max_albedo: float
    max_attenuation_distance: float
    max_emissive_rate: float
    retro_intensity_enhance: float
    retro_range_noise_stddev: float
    retroreflection_noise_mean: float
    retroreflection_noise_stddev: float
    strong_retro_intensity_enhance: float
    def __init__(self, retro_range_noise_stddev: Optional[float] = ..., retroreflection_noise_mean: Optional[float] = ..., retroreflection_noise_stddev: Optional[float] = ..., max_attenuation_distance: Optional[float] = ..., retro_intensity_enhance: Optional[float] = ..., intensity_specular_scale: Optional[float] = ..., intensity_roughness_scale: Optional[float] = ..., beam_intensity: Optional[float] = ..., albedo_weights: Optional[Union[AlbedoWeights, Mapping]] = ..., max_albedo: Optional[float] = ..., strong_retro_intensity_enhance: Optional[float] = ..., intensity_metallic_scale: Optional[float] = ..., emissive_gate: Optional[float] = ..., max_emissive_rate: Optional[float] = ...) -> None: ...

class LidarIntrinsic(_message.Message):
    __slots__ = ["alice_lidar_model", "azimuth_max", "azimuth_min", "beam_data", "capture_backwardmotionvectors", "capture_depth", "capture_detections", "capture_instance", "capture_intensity", "capture_motionvectors", "capture_normals", "capture_properties", "capture_rgb", "capture_segmentation", "intensity_params", "maximum_cutoff_prob", "maximum_offset", "maximum_range_cutoff", "merge_returns", "minimum_cutoff_prob", "minimum_noise", "minimum_offset", "minimum_range_cutoff", "multi_returns", "pattern", "range_noise_mean", "range_noise_stddev", "rotation_rate", "sample_rate", "time_offset"]
    ALICE_LIDAR_MODEL_FIELD_NUMBER: ClassVar[int]
    AZIMUTH_MAX_FIELD_NUMBER: ClassVar[int]
    AZIMUTH_MIN_FIELD_NUMBER: ClassVar[int]
    BEAM_DATA_FIELD_NUMBER: ClassVar[int]
    CAPTURE_BACKWARDMOTIONVECTORS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_DEPTH_FIELD_NUMBER: ClassVar[int]
    CAPTURE_DETECTIONS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_INSTANCE_FIELD_NUMBER: ClassVar[int]
    CAPTURE_INTENSITY_FIELD_NUMBER: ClassVar[int]
    CAPTURE_MOTIONVECTORS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_NORMALS_FIELD_NUMBER: ClassVar[int]
    CAPTURE_PROPERTIES_FIELD_NUMBER: ClassVar[int]
    CAPTURE_RGB_FIELD_NUMBER: ClassVar[int]
    CAPTURE_SEGMENTATION_FIELD_NUMBER: ClassVar[int]
    INTENSITY_PARAMS_FIELD_NUMBER: ClassVar[int]
    MAXIMUM_CUTOFF_PROB_FIELD_NUMBER: ClassVar[int]
    MAXIMUM_OFFSET_FIELD_NUMBER: ClassVar[int]
    MAXIMUM_RANGE_CUTOFF_FIELD_NUMBER: ClassVar[int]
    MERGE_RETURNS_FIELD_NUMBER: ClassVar[int]
    MINIMUM_CUTOFF_PROB_FIELD_NUMBER: ClassVar[int]
    MINIMUM_NOISE_FIELD_NUMBER: ClassVar[int]
    MINIMUM_OFFSET_FIELD_NUMBER: ClassVar[int]
    MINIMUM_RANGE_CUTOFF_FIELD_NUMBER: ClassVar[int]
    MULTI_RETURNS_FIELD_NUMBER: ClassVar[int]
    PATTERN_FIELD_NUMBER: ClassVar[int]
    RANGE_NOISE_MEAN_FIELD_NUMBER: ClassVar[int]
    RANGE_NOISE_STDDEV_FIELD_NUMBER: ClassVar[int]
    ROTATION_RATE_FIELD_NUMBER: ClassVar[int]
    SAMPLE_RATE_FIELD_NUMBER: ClassVar[int]
    TIME_OFFSET_FIELD_NUMBER: ClassVar[int]
    alice_lidar_model: AliceLidarModel
    azimuth_max: float
    azimuth_min: float
    beam_data: _containers.RepeatedCompositeFieldContainer[LidarBeam]
    capture_backwardmotionvectors: bool
    capture_depth: bool
    capture_detections: bool
    capture_instance: bool
    capture_intensity: bool
    capture_motionvectors: bool
    capture_normals: bool
    capture_properties: bool
    capture_rgb: bool
    capture_segmentation: bool
    intensity_params: LidarIntensityParams
    maximum_cutoff_prob: float
    maximum_offset: float
    maximum_range_cutoff: float
    merge_returns: int
    minimum_cutoff_prob: float
    minimum_noise: float
    minimum_offset: float
    minimum_range_cutoff: float
    multi_returns: int
    pattern: str
    range_noise_mean: float
    range_noise_stddev: float
    rotation_rate: float
    sample_rate: float
    time_offset: float
    def __init__(self, sample_rate: Optional[float] = ..., rotation_rate: Optional[float] = ..., azimuth_min: Optional[float] = ..., azimuth_max: Optional[float] = ..., beam_data: Optional[Iterable[Union[LidarBeam, Mapping]]] = ..., capture_rgb: bool = ..., capture_intensity: bool = ..., capture_depth: bool = ..., capture_normals: bool = ..., capture_segmentation: bool = ..., capture_instance: bool = ..., capture_detections: bool = ..., capture_motionvectors: bool = ..., minimum_range_cutoff: Optional[float] = ..., maximum_range_cutoff: Optional[float] = ..., minimum_cutoff_prob: Optional[float] = ..., maximum_cutoff_prob: Optional[float] = ..., minimum_offset: Optional[float] = ..., maximum_offset: Optional[float] = ..., minimum_noise: Optional[float] = ..., range_noise_mean: Optional[float] = ..., range_noise_stddev: Optional[float] = ..., intensity_params: Optional[Union[LidarIntensityParams, Mapping]] = ..., alice_lidar_model: Optional[Union[AliceLidarModel, Mapping]] = ..., pattern: Optional[str] = ..., time_offset: Optional[float] = ..., multi_returns: Optional[int] = ..., merge_returns: Optional[int] = ..., capture_properties: bool = ..., capture_backwardmotionvectors: bool = ...) -> None: ...

class LidarNoiseParams(_message.Message):
    __slots__ = ["max_dist", "max_offset", "max_prob", "min_dist", "min_noise", "min_offset", "min_prob"]
    MAX_DIST_FIELD_NUMBER: ClassVar[int]
    MAX_OFFSET_FIELD_NUMBER: ClassVar[int]
    MAX_PROB_FIELD_NUMBER: ClassVar[int]
    MIN_DIST_FIELD_NUMBER: ClassVar[int]
    MIN_NOISE_FIELD_NUMBER: ClassVar[int]
    MIN_OFFSET_FIELD_NUMBER: ClassVar[int]
    MIN_PROB_FIELD_NUMBER: ClassVar[int]
    max_dist: float
    max_offset: float
    max_prob: float
    min_dist: float
    min_noise: float
    min_offset: float
    min_prob: float
    def __init__(self, min_dist: Optional[float] = ..., max_dist: Optional[float] = ..., min_prob: Optional[float] = ..., max_prob: Optional[float] = ..., min_offset: Optional[float] = ..., max_offset: Optional[float] = ..., min_noise: Optional[float] = ...) -> None: ...

class NoiseParams(_message.Message):
    __slots__ = ["bilateral_sigma_d", "bilateral_sigma_r", "denoise_filter", "denoise_filter_size", "enable_auto_iso", "enable_auto_noise", "enable_bayer", "enable_denoise", "enable_gauss_noise", "enable_poisson_noise", "fstop", "gauss_noise_sigma", "is_using_iso", "iso_level", "max_exposure_time", "poisson_noise_lambda", "post_amplifier_noise", "pre_amplifier_noise", "quantum_efficiency", "signal_amount"]
    BILATERAL_SIGMA_D_FIELD_NUMBER: ClassVar[int]
    BILATERAL_SIGMA_R_FIELD_NUMBER: ClassVar[int]
    DENOISE_FILTER_FIELD_NUMBER: ClassVar[int]
    DENOISE_FILTER_SIZE_FIELD_NUMBER: ClassVar[int]
    ENABLE_AUTO_ISO_FIELD_NUMBER: ClassVar[int]
    ENABLE_AUTO_NOISE_FIELD_NUMBER: ClassVar[int]
    ENABLE_BAYER_FIELD_NUMBER: ClassVar[int]
    ENABLE_DENOISE_FIELD_NUMBER: ClassVar[int]
    ENABLE_GAUSS_NOISE_FIELD_NUMBER: ClassVar[int]
    ENABLE_POISSON_NOISE_FIELD_NUMBER: ClassVar[int]
    FSTOP_FIELD_NUMBER: ClassVar[int]
    GAUSS_NOISE_SIGMA_FIELD_NUMBER: ClassVar[int]
    ISO_LEVEL_FIELD_NUMBER: ClassVar[int]
    IS_USING_ISO_FIELD_NUMBER: ClassVar[int]
    MAX_EXPOSURE_TIME_FIELD_NUMBER: ClassVar[int]
    POISSON_NOISE_LAMBDA_FIELD_NUMBER: ClassVar[int]
    POST_AMPLIFIER_NOISE_FIELD_NUMBER: ClassVar[int]
    PRE_AMPLIFIER_NOISE_FIELD_NUMBER: ClassVar[int]
    QUANTUM_EFFICIENCY_FIELD_NUMBER: ClassVar[int]
    SIGNAL_AMOUNT_FIELD_NUMBER: ClassVar[int]
    bilateral_sigma_d: float
    bilateral_sigma_r: float
    denoise_filter: DenoiseFilter
    denoise_filter_size: int
    enable_auto_iso: bool
    enable_auto_noise: bool
    enable_bayer: bool
    enable_denoise: bool
    enable_gauss_noise: bool
    enable_poisson_noise: bool
    fstop: float
    gauss_noise_sigma: float
    is_using_iso: bool
    iso_level: int
    max_exposure_time: float
    poisson_noise_lambda: float
    post_amplifier_noise: float
    pre_amplifier_noise: float
    quantum_efficiency: float
    signal_amount: int
    def __init__(self, enable_bayer: bool = ..., enable_gauss_noise: bool = ..., enable_poisson_noise: bool = ..., enable_denoise: bool = ..., gauss_noise_sigma: Optional[float] = ..., poisson_noise_lambda: Optional[float] = ..., denoise_filter: Optional[Union[DenoiseFilter, str]] = ..., denoise_filter_size: Optional[int] = ..., bilateral_sigma_d: Optional[float] = ..., bilateral_sigma_r: Optional[float] = ..., enable_auto_noise: bool = ..., signal_amount: Optional[int] = ..., pre_amplifier_noise: Optional[float] = ..., post_amplifier_noise: Optional[float] = ..., is_using_iso: bool = ..., iso_level: Optional[int] = ..., enable_auto_iso: bool = ..., fstop: Optional[float] = ..., max_exposure_time: Optional[float] = ..., quantum_efficiency: Optional[float] = ...) -> None: ...

class PostProcessNode(_message.Message):
    __slots__ = ["material", "weight"]
    MATERIAL_FIELD_NUMBER: ClassVar[int]
    WEIGHT_FIELD_NUMBER: ClassVar[int]
    material: str
    weight: float
    def __init__(self, material: Optional[str] = ..., weight: Optional[float] = ...) -> None: ...

class PostProcessParams(_message.Message):
    __slots__ = ["dof_depth_blur_amount", "dof_depth_blur_radius", "dof_focal_distance", "exposure_compensation", "exposure_max_ev100", "exposure_metering_mask", "exposure_min_ev100", "exposure_speed_down", "exposure_speed_up", "motion_blur_amount", "motion_blur_max", "vignette_intensity"]
    DOF_DEPTH_BLUR_AMOUNT_FIELD_NUMBER: ClassVar[int]
    DOF_DEPTH_BLUR_RADIUS_FIELD_NUMBER: ClassVar[int]
    DOF_FOCAL_DISTANCE_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_COMPENSATION_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_MAX_EV100_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_METERING_MASK_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_MIN_EV100_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_SPEED_DOWN_FIELD_NUMBER: ClassVar[int]
    EXPOSURE_SPEED_UP_FIELD_NUMBER: ClassVar[int]
    MOTION_BLUR_AMOUNT_FIELD_NUMBER: ClassVar[int]
    MOTION_BLUR_MAX_FIELD_NUMBER: ClassVar[int]
    VIGNETTE_INTENSITY_FIELD_NUMBER: ClassVar[int]
    dof_depth_blur_amount: float
    dof_depth_blur_radius: float
    dof_focal_distance: float
    exposure_compensation: float
    exposure_max_ev100: float
    exposure_metering_mask: str
    exposure_min_ev100: float
    exposure_speed_down: float
    exposure_speed_up: float
    motion_blur_amount: float
    motion_blur_max: float
    vignette_intensity: float
    def __init__(self, exposure_compensation: Optional[float] = ..., exposure_speed_up: Optional[float] = ..., exposure_speed_down: Optional[float] = ..., exposure_min_ev100: Optional[float] = ..., exposure_max_ev100: Optional[float] = ..., exposure_metering_mask: Optional[str] = ..., motion_blur_amount: Optional[float] = ..., motion_blur_max: Optional[float] = ..., dof_focal_distance: Optional[float] = ..., dof_depth_blur_amount: Optional[float] = ..., dof_depth_blur_radius: Optional[float] = ..., vignette_intensity: Optional[float] = ...) -> None: ...

class RadarBasicParameters(_message.Message):
    __slots__ = ["azimuth_accuracy", "azimuth_fov", "azimuth_resolution", "doppler_resolution", "elevation_accuracy", "elevation_fov", "elevation_resolution", "max_doppler", "max_range", "number_rays_per_frame", "prf_profile_file", "radar_output_2d", "range_resolution", "use_random_raycast"]
    AZIMUTH_ACCURACY_FIELD_NUMBER: ClassVar[int]
    AZIMUTH_FOV_FIELD_NUMBER: ClassVar[int]
    AZIMUTH_RESOLUTION_FIELD_NUMBER: ClassVar[int]
    DOPPLER_RESOLUTION_FIELD_NUMBER: ClassVar[int]
    ELEVATION_ACCURACY_FIELD_NUMBER: ClassVar[int]
    ELEVATION_FOV_FIELD_NUMBER: ClassVar[int]
    ELEVATION_RESOLUTION_FIELD_NUMBER: ClassVar[int]
    MAX_DOPPLER_FIELD_NUMBER: ClassVar[int]
    MAX_RANGE_FIELD_NUMBER: ClassVar[int]
    NUMBER_RAYS_PER_FRAME_FIELD_NUMBER: ClassVar[int]
    PRF_PROFILE_FILE_FIELD_NUMBER: ClassVar[int]
    RADAR_OUTPUT_2D_FIELD_NUMBER: ClassVar[int]
    RANGE_RESOLUTION_FIELD_NUMBER: ClassVar[int]
    USE_RANDOM_RAYCAST_FIELD_NUMBER: ClassVar[int]
    azimuth_accuracy: float
    azimuth_fov: float
    azimuth_resolution: float
    doppler_resolution: float
    elevation_accuracy: float
    elevation_fov: float
    elevation_resolution: float
    max_doppler: float
    max_range: float
    number_rays_per_frame: int
    prf_profile_file: str
    radar_output_2d: bool
    range_resolution: float
    use_random_raycast: bool
    def __init__(self, max_range: Optional[float] = ..., range_resolution: Optional[float] = ..., max_doppler: Optional[float] = ..., doppler_resolution: Optional[float] = ..., azimuth_fov: Optional[float] = ..., azimuth_resolution: Optional[float] = ..., elevation_fov: Optional[float] = ..., elevation_resolution: Optional[float] = ..., radar_output_2d: bool = ..., use_random_raycast: bool = ..., number_rays_per_frame: Optional[int] = ..., azimuth_accuracy: Optional[float] = ..., elevation_accuracy: Optional[float] = ..., prf_profile_file: Optional[str] = ...) -> None: ...

class RadarDetectorParameters(_message.Message):
    __slots__ = ["detector_constant_gain", "detector_radiometric_decay", "detector_radiometric_gain", "detector_type"]
    DETECTOR_CONSTANT_GAIN_FIELD_NUMBER: ClassVar[int]
    DETECTOR_RADIOMETRIC_DECAY_FIELD_NUMBER: ClassVar[int]
    DETECTOR_RADIOMETRIC_GAIN_FIELD_NUMBER: ClassVar[int]
    DETECTOR_TYPE_FIELD_NUMBER: ClassVar[int]
    detector_constant_gain: float
    detector_radiometric_decay: float
    detector_radiometric_gain: float
    detector_type: str
    def __init__(self, detector_type: Optional[str] = ..., detector_constant_gain: Optional[float] = ..., detector_radiometric_gain: Optional[float] = ..., detector_radiometric_decay: Optional[float] = ...) -> None: ...

class RadarEnergyParameters(_message.Message):
    __slots__ = ["beam_pattern_file", "enable_beam_pattern", "gain_jitter_std", "nominal_gain", "radiometric_coefficient"]
    BEAM_PATTERN_FILE_FIELD_NUMBER: ClassVar[int]
    ENABLE_BEAM_PATTERN_FIELD_NUMBER: ClassVar[int]
    GAIN_JITTER_STD_FIELD_NUMBER: ClassVar[int]
    NOMINAL_GAIN_FIELD_NUMBER: ClassVar[int]
    RADIOMETRIC_COEFFICIENT_FIELD_NUMBER: ClassVar[int]
    beam_pattern_file: str
    enable_beam_pattern: bool
    gain_jitter_std: float
    nominal_gain: float
    radiometric_coefficient: float
    def __init__(self, nominal_gain: Optional[float] = ..., gain_jitter_std: Optional[float] = ..., radiometric_coefficient: Optional[float] = ..., beam_pattern_file: Optional[str] = ..., enable_beam_pattern: bool = ...) -> None: ...

class RadarIntrinsic(_message.Message):
    __slots__ = ["basic_parameters", "detector_parameters", "energy_parameters", "noise_parameters"]
    BASIC_PARAMETERS_FIELD_NUMBER: ClassVar[int]
    DETECTOR_PARAMETERS_FIELD_NUMBER: ClassVar[int]
    ENERGY_PARAMETERS_FIELD_NUMBER: ClassVar[int]
    NOISE_PARAMETERS_FIELD_NUMBER: ClassVar[int]
    basic_parameters: RadarBasicParameters
    detector_parameters: RadarDetectorParameters
    energy_parameters: RadarEnergyParameters
    noise_parameters: RadarNoiseParameters
    def __init__(self, basic_parameters: Optional[Union[RadarBasicParameters, Mapping]] = ..., energy_parameters: Optional[Union[RadarEnergyParameters, Mapping]] = ..., noise_parameters: Optional[Union[RadarNoiseParameters, Mapping]] = ..., detector_parameters: Optional[Union[RadarDetectorParameters, Mapping]] = ...) -> None: ...

class RadarNoiseParameters(_message.Message):
    __slots__ = ["enable_doa_noise", "enable_thermal_noise", "thermal_noise_mean", "thermal_noise_std"]
    ENABLE_DOA_NOISE_FIELD_NUMBER: ClassVar[int]
    ENABLE_THERMAL_NOISE_FIELD_NUMBER: ClassVar[int]
    THERMAL_NOISE_MEAN_FIELD_NUMBER: ClassVar[int]
    THERMAL_NOISE_STD_FIELD_NUMBER: ClassVar[int]
    enable_doa_noise: bool
    enable_thermal_noise: bool
    thermal_noise_mean: float
    thermal_noise_std: float
    def __init__(self, enable_thermal_noise: bool = ..., thermal_noise_std: Optional[float] = ..., thermal_noise_mean: Optional[float] = ..., enable_doa_noise: bool = ...) -> None: ...

class SensorConfig(_message.Message):
    __slots__ = ["camera_intrinsic", "display_name", "lidar_intrinsic", "radar_intrinsic", "sensor_extrinsic"]
    CAMERA_INTRINSIC_FIELD_NUMBER: ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: ClassVar[int]
    LIDAR_INTRINSIC_FIELD_NUMBER: ClassVar[int]
    RADAR_INTRINSIC_FIELD_NUMBER: ClassVar[int]
    SENSOR_EXTRINSIC_FIELD_NUMBER: ClassVar[int]
    camera_intrinsic: CameraIntrinsic
    display_name: str
    lidar_intrinsic: LidarIntrinsic
    radar_intrinsic: RadarIntrinsic
    sensor_extrinsic: SensorExtrinsic
    def __init__(self, display_name: Optional[str] = ..., camera_intrinsic: Optional[Union[CameraIntrinsic, Mapping]] = ..., lidar_intrinsic: Optional[Union[LidarIntrinsic, Mapping]] = ..., radar_intrinsic: Optional[Union[RadarIntrinsic, Mapping]] = ..., sensor_extrinsic: Optional[Union[SensorExtrinsic, Mapping]] = ...) -> None: ...

class SensorExtrinsic(_message.Message):
    __slots__ = ["attach_socket", "follow_rotation", "lock_to_yaw", "pitch", "roll", "x", "y", "yaw", "z"]
    ATTACH_SOCKET_FIELD_NUMBER: ClassVar[int]
    FOLLOW_ROTATION_FIELD_NUMBER: ClassVar[int]
    LOCK_TO_YAW_FIELD_NUMBER: ClassVar[int]
    PITCH_FIELD_NUMBER: ClassVar[int]
    ROLL_FIELD_NUMBER: ClassVar[int]
    X_FIELD_NUMBER: ClassVar[int]
    YAW_FIELD_NUMBER: ClassVar[int]
    Y_FIELD_NUMBER: ClassVar[int]
    Z_FIELD_NUMBER: ClassVar[int]
    attach_socket: str
    follow_rotation: bool
    lock_to_yaw: bool
    pitch: float
    roll: float
    x: float
    y: float
    yaw: float
    z: float
    def __init__(self, yaw: Optional[float] = ..., pitch: Optional[float] = ..., roll: Optional[float] = ..., x: Optional[float] = ..., y: Optional[float] = ..., z: Optional[float] = ..., lock_to_yaw: bool = ..., attach_socket: Optional[str] = ..., follow_rotation: bool = ...) -> None: ...

class SensorList(_message.Message):
    __slots__ = ["sensors"]
    SENSORS_FIELD_NUMBER: ClassVar[int]
    sensors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sensors: Optional[Iterable[str]] = ...) -> None: ...

class SensorRigConfig(_message.Message):
    __slots__ = ["default_sensor_splits_list", "sensor_configs", "sensor_rig_artifact_uid"]
    DEFAULT_SENSOR_SPLITS_LIST_FIELD_NUMBER: ClassVar[int]
    SENSOR_CONFIGS_FIELD_NUMBER: ClassVar[int]
    SENSOR_RIG_ARTIFACT_UID_FIELD_NUMBER: ClassVar[int]
    default_sensor_splits_list: _containers.RepeatedCompositeFieldContainer[SensorList]
    sensor_configs: _containers.RepeatedCompositeFieldContainer[SensorConfig]
    sensor_rig_artifact_uid: str
    def __init__(self, sensor_configs: Optional[Iterable[Union[SensorConfig, Mapping]]] = ..., sensor_rig_artifact_uid: Optional[str] = ..., default_sensor_splits_list: Optional[Iterable[Union[SensorList, Mapping]]] = ...) -> None: ...

class DenoiseFilter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
