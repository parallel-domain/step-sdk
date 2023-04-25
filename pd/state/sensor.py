# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Camera and LiDAR sensor configuration

This set of dataclass wrappers is used to create camera and lidar sensor
representations.

Additionally, we support loading sensor definitions from a JSON file via the
:func:`sensors_from_json` function.
"""

from dataclasses import dataclass, field
from abc import ABC
from enum import IntEnum, Enum, auto
from typing import List, Dict, Optional, Union, Any, Tuple
import json
from pathlib import Path
import logging

import numpy as np

from pd.state.pose6d import Pose6D
from pd.core.errors import PdError
from pd.internal.labels import id_to_color_lookup, id_to_label


logger = logging.getLogger(__name__)


@dataclass
class Sensor(ABC):
    """
    Base container for Sensors
    """

    name: str
    """Sensor's name"""

    pose: Union[Pose6D, np.ndarray]
    """
    Sensor's pose in the agent's coordinate system

    Value must be a valid :class:`Pose6D` object or a 4x4 transformation matrix
    """

    lock_to_yaw: bool = field(default=False, init=False)
    """
    Lock yaw to agent only
    
    Setting this flag to true will cause the yaw value of the sensor orientation to be locked to the agent
    but leave the pitch and roll values as zero with respect to the world frame
    """

    attach_socket: Optional[str] = field(default=None, init=False)
    """
    Attach sensor to the given socket on mesh
    """

    follow_rotation: bool = field(default=True, init=False)


#############################
# CameraSensor
#############################

@dataclass
class PostProcessMaterial:
    material: str
    weight: float = 0.0


class DenoiseFilter(IntEnum):
    AverageFilter = 0
    MedianFilter = 1
    FastMedianFilter = 2
    BilateralFilter = 3


@dataclass
class NoiseParams:
    enable_bayer: bool = False
    enable_gauss_noise: bool = False
    enable_poisson_noise: bool = False
    enable_denoise: bool = False

    gauss_noise_sigma: float = 0.0
    poisson_noise_lambda: float = 0.0

    denoise_filter: DenoiseFilter = DenoiseFilter.AverageFilter
    denoise_filter_size: int = 0
    bilateral_sigma_d: float = 0.0
    bilateral_sigma_r: float = 0.0

    enable_auto_noise: bool = False
    signal_amount: int = 0
    pre_amplifier_noise: float = 0.0
    post_amplifier_noise: float = 0.0

    is_using_iso: bool = False
    iso_level: int = 0

    enable_auto_iso: bool = False
    fstop: float = 0.0
    max_exposure_time: float = 0.0
    quantum_efficiency: float = 0.0


@dataclass
class DistortionParams:
    k1: float = 0.0
    k2: float = 0.0
    k3: float = 0.0
    k4: float = 0.0
    k5: float = 0.0
    k6: float = 0.0
    p1: float = 0.0
    p2: float = 0.0
    skew: float = 0.0
    is_fisheye: bool = False
    fx: float = 0.0
    fy: float = 0.0
    cx: float = 0.0
    cy: float = 0.0


@dataclass
class TonemapCurve:
    slope: float = 0.66
    toe: float = 0.52
    shoulder: float = 0.49
    black_clip: float = 0.0
    white_clip: float = 0.08


@dataclass
class PostProcessParams:
    exposure_compensation: float = -100.0
    """
    Auto exposure histogram setting for exposure compensation

    When set to 0, there will be no adjustment, -1 is two times darker, -2 is four times darker,
    1 is two times brighter, and 2 is four times brighter.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    Set to -100 to disable this parameter so that it will use the default value set by the location level.
    """

    exposure_speed_up: float = 0.0
    """
    Auto exposure histogram setting for exposure speed up

    The speed at which the adaptation occurs from a dark environment to a bright environment.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    """

    exposure_speed_down: float = 0.0
    """
    Auto exposure histogram setting for exposure speed down

    The speed at which adaptation occurs from a bright environment to a dark environment.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    """

    exposure_min_ev100: float = -100.0
    """
    Auto exposure histogram setting for min ev100

    The minimum brightness for auto exposure adaptation, expressed in pixel luminance (cd/m2).
    Value is typically negative and should be less than or equal to Max EV100.
    As this value increases, the scene view gets darker.
    If Min EV100 is equal to Max EV100, auto exposure is disabled.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    Set to -100 to disable this parameter so that it will use the default value set by the location level
    """

    exposure_max_ev100: float = -100.0
    """
    Auto exposure histogram setting for max ev100

    The maximum brightness for auto exposure adaptation, expressed in pixel luminance (cd/m2).
    Value is typically positive and should be greater than or equal to Min EV100.
    As this value decreases, the scene view gets brighter.
    If Max EV100 is equal to Min EV100, auto exposure is disabled.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    Set to -100 to disable this parameter so that it will use the default value set by the location level
    """

    exposure_metering_mask: Optional[str] = None
    """
    Auto exposure histogram setting for metering mask (internal-use)

    Use your own texture mask to meter exposure.
    Bright spots on the mask will have high influence on auto exposure metering, and dark spots will have low influence.
    See `Unreal documentation <https://docs.unrealengine.com/4.27/en-US/RenderingAndGraphics/PostProcessEffects/AutomaticExposure/>`_ for more information.
    """

    motion_blur_amount: float = 1.5
    motion_blur_max: float = 5.0
    dof_focal_distance: float = -1.0
    dof_depth_blur_amount: float = 0.0
    dof_depth_blur_radius: float = -1.0
    vignette_intensity: float = 0.0
    tone_curve: Optional[TonemapCurve] = None
    exposure_compensation_curve: Optional[str] = None


@dataclass
class CameraSensor(Sensor):
    """
    Describes the intrinsic and extrinsic parameters of a camera sensor
    """
    width: int
    height: int

    field_of_view_degrees: float = 0.0
    """
    Field of view in degrees

    Specifies field of view in degrees for the larger image dimension.
    I.e. if width>height, this determines the horizontal (left to right) field of view.
    If height>width, this determines the vertical (top to down) field of view.
    This value is only used if the focal lengths in :class:`DistortionParams` are not set.
    Square pixels are assumed when this value is in effect (i.e. fx=fy).
    """

    supersample: float = 1.0
    capture_rgb: bool = False
    capture_depth: bool = False
    capture_normals: bool = False
    capture_segmentation: bool = False
    capture_instances: bool = False
    capture_motionvectors: bool = False
    capture_backwardmotionvectors: bool = False
    capture_basecolor : bool = False
    capture_properties : bool = False

    enable_streaming: bool = False

    lut: Optional[str] = None
    lut_weight: float = 1.0

    distortion_params: Optional[DistortionParams] = None
    noise_params: Optional[NoiseParams] = None
    post_process_params: Optional[PostProcessParams] = None
    post_process_materials: List[PostProcessMaterial] = field(default_factory=list)

    transmit_gray: bool = False

    fisheye_model: int = 0
    """
    Camera sensor model

    0 - no fisheye
    1 - Kannala fisheye model (OpenCV)
    2 - Atan distorted Kannala fisheye model
    3 - Use Distortion LUT
    4 - Panoramic camera with spherical perspective
    5 - Panoramic camera with cylindrical perspective
    6 - Orthographic camera
    """

    distortion_lookup_table: Optional[str] = None

    time_offset : float = 0.0
    """Offset capture time in ms"""


#############################
# LiDARSensor
#############################

@dataclass
class LiDARBeam:
    id: int
    azimuth: float
    elevation: float


@dataclass
class LiDARIntensityParams:
    retro_range_noise_stddev: float = 0.1
    """Bump the depth noise for retroreflective beams"""

    retroreflection_noise_mean: float = 0.0
    """Noise for refroreflective intensity"""

    retroreflection_noise_stddev: float = 0.1

    max_attenuation_distance_metres: float = 220.0

    retro_intensity_enhance: float = 1.5
    """
    Reflection intensity enhance when the beam hits a retroreflective surface,
    the default value is 1.5, which means the intensity is 50% stronger than the general
    """

    intensity_specular_scale: float = 2.0
    """
    Because the LiDAR beams are infrared light, the specular of the object's surface would
    be higher than the visible light. The default value of it should be 4.0, because in
    Engine code, F=50*SpecularColor=50*0.08*BaseColor=4.0*BaseColor, where 4.0 is the specular scale we used.
    """

    intensity_roughness_scale: float = 1.5
    """
    Because the LiDAR beams are infrared light, the beam would be spread more than the visible light.
    By scaling up roughness to 1.5, we could let the beam spread more.
    """

    beam_intensity: float = 2.0
    """The intensity of the beam. It could be used to scale the final intensity to a reasonable range"""

    albedo_weights: Tuple[float, float, float] = field(default=(0., 0., 0.))
    """
    The weights of rgb channels to compose the surface albedo for LiDAR beams.
    Because the LiDAR beams are infrared light, the weight of red should be heavier than green and blue.
    So the default value is { 1.0f, 0.8f, 0.4f }
    """

    max_albedo: float = 2.2
    """Max surface albedo value, prevent too bright"""

    strong_retro_intensity_enhance: float = 0.9
    """Enhance when the beam hits a traffic sign"""

    intensity_metallic_scale: float = 1.0
    """Scale the metallic"""

    emissive_gate: float = 100.0
    """At least how much emissive value will enhance the intensity"""

    max_emissive_rate: float = 10.0
    """The emissive will be less than (max_emissive_rate * emissive_gate)"""


@dataclass
class LiDARSensor(Sensor):
    """
    Describes the intrinsic and extrinsic parameters of a LiDAR sensor
    """
    sample_rate: float
    rotation_rate: float

    beam_data: List[LiDARBeam] = field(default_factory=list)

    azimuth_min: float = 0.0
    azimuth_max: float = 0.0
    elevation_delta: float = 0.0

    capture_rgb: bool = False
    capture_depth: bool = False
    capture_normals: bool = False
    capture_segmentation: bool = False
    capture_instances: bool = False
    capture_motionvectors: bool = False

    minimum_range_cutoff: float = 15.0
    """All samples with lower range will not be culled by the range based culling"""

    maximum_range_cutoff: float = 235.0
    """All samples with greater range will always be culled by range culling"""

    minimum_cutoff_prob: float = 0.07
    """Minimum culling probability, range [0.0, 1.0]"""

    maximum_cutoff_prob: float = 0.95
    """Maximum culling probability, range [0.0, 1.0]"""

    minimum_offset: float = 0.002
    maximum_offset: float = 0.02
    minimum_noise: float = 0.001
    range_noise_mean: float = 0.0
    range_noise_stddev: float = 0.005

    intensity_params: Optional[LiDARIntensityParams] = None

    pattern: Optional[str] = None

    time_offset_ms: float = 0.0
    """Offset capture time in ms"""


@dataclass
class SensorData:
    """
    Holds camera sensor data returned from server
    """

    width: int
    """Width of the image"""

    height: int
    """Height of the image"""

    data: np.ndarray
    """Raw numpy data"""

    @property
    def data_as_rgb(self) -> np.ndarray:
        """
        Returns data array as a 3-channel RGB buffer
        """
        return self.data[:, :, :3]

    @property
    def data_as_depth(self) -> np.ndarray:
        """
        Returns data array as a single-channel float32 depth buffer
        """
        return self.data.view('<f4').squeeze(axis=2)

    @property
    def data_as_segmentation_ids(self) -> np.ndarray:
        """
        Returns data array as a single-channel 2D buffer where each pixel
        maps to its uint8 segmentation id
        """
        return self.data[:, :, 0]

    @property
    def data_as_segmentation_labels(self) -> np.ndarray:
        """
        Returns a 2D array where each pixel maps to a segmentation label string
        """
        id_to_label_lookup = np.ndarray(shape=(256,), dtype=object)
        for id, label in id_to_label.items():
            id_to_label_lookup[id] = label.name
        return id_to_label_lookup[self.data_as_segmentation_ids]

    @property
    def data_as_segmentation_rgb(self) -> np.ndarray:
        """
        Returns data array as an RGB segmentation image
        """
        return id_to_color_lookup[self.data_as_segmentation_ids]

    @property
    def data_as_instance_ids(self) -> np.ndarray:
        """
        Returns data array as a single-channel 2D buffer where each pixel
        maps to its uint16 instance id
        """
        ret = self.data.view(dtype=np.uint16)  # read as two-channel uint16
        ret = ret[:, :, 0]  # only first channel is valid
        return ret

    @property
    def data_as_instance_rgb(self) -> np.ndarray:
        """
        Returns data array as an RGB instances image.
        """
        # Instance id to color map
        import cv2
        np.random.seed(1234)
        random_ids = np.random.randint(0, 256, 65536, dtype=np.uint8)
        instance_id_to_color_lookup = cv2.applyColorMap(random_ids, cv2.COLORMAP_JET).reshape(-1, 3).astype(np.float32)
        instance_id_to_color_lookup[0][:] = 0  # sets black color for null instance id

        # Generates instances rgb image
        instance_image_rgb = instance_id_to_color_lookup[self.data_as_instance_ids]
        return instance_image_rgb.astype(np.uint8)

    def get_data_as_merged_instance_rgb(self, rgb: np.ndarray) -> np.ndarray:
        """
        Returns data array as an RGB instances image.
        The instance image is merged with a given rgb image

        Args:
            rgb: The rgb image with which to merge the instance image
        """
        instance_image_rgb = self.data_as_instance_rgb.astype(np.float64)
        # Height and width must match, channels can be 3 (color) or 1 (grayscale)
        if rgb.shape[:2] != instance_image_rgb.shape[:2]:
            raise PdError(f"Rgb image size {str(rgb.shape[:2])} must match the instances "
                          f"image size {str(instance_image_rgb.shape[:2])}")
        # Generates instance id alpha mask
        # Alpha mask has a non-zero alpha value for every non-zero pixel in instances rgb image
        # Lastly, broadcasts alpha to match dims of rgb image
        alpha = np.sum(instance_image_rgb, axis=2)
        alpha[alpha > 0] = 0.5
        alpha = np.expand_dims(alpha, axis=2)
        alpha = np.broadcast_to(alpha, shape=instance_image_rgb.shape)
        # Generates output image by combining rgb image with instances image
        output_img = rgb * (1-alpha) + instance_image_rgb * alpha
        return output_img.astype(np.uint8)

    @property
    def data_as_surface_normals(self) -> np.ndarray:
        """
        Returns data array as a buffer containing surface normal vectors

        Returned buffer is a numpy.float64 matrix of shape `(H X W x 3)`, where `H` is the height and `W` is the width
        of corresponding camera image. The third axis contains the x, y and z normal direction of the surface sampled
        by the pixel in the camera coordinate system.
        """
        quantized_norms = self.data[:, :, :3]
        quantized_norms_f = quantized_norms.astype(np.float64)
        dequantized_norms_f = ((quantized_norms_f / 255) - 0.5) * 2
        dequantized_norms_f = dequantized_norms_f / np.linalg.norm(dequantized_norms_f, axis=-1, keepdims=True)
        return dequantized_norms_f


@dataclass
class LidarSensorData:
    """
    Holds LiDAR sensor data returned from server
    """
    num_points: int
    data: np.ndarray


class SensorBuffer(IntEnum):
    """
    Enumerates annotation buffer type
    """
    RGB = 0
    DEPTH = 1
    NORMALS = 2
    SEGMENTATION = 3
    INSTANCES = 4


#############################
# Sensor Rigs
#############################

class SensorRig(Enum):
    """
    Enumerates default sensor rigs available in the SDK
    """
    BAREBONES_RGB = 'barebones_rgb'
    BAREBONES_ALL = 'barebones_all'
    DEMO_RIG_SIMPLE_FRONT_ALL = 'demo_rig_simple_front_all'
    MINIMAL = 'minimal'


class PdBadSensorConfigError(PdError):
    """
    Error indicating a bad sensor config
    """
    pass


def sensors_from_json(json_dict: Dict[Any, Any]) -> List[Sensor]:
    """
    Load sensors from a sensor rig JSON file
    """
    sensors = []

    for sensor_config in json_dict['sensor_configs']:
        # Sensor name
        if 'display_name' not in sensor_config:
            raise PdBadSensorConfigError("Missing sensor name")
        name = sensor_config['display_name']

        # Sensor pose
        if 'sensor_extrinsic' not in sensor_config:
            raise PdBadSensorConfigError("Missing sensor extrinsics")
        _ext = sensor_config["sensor_extrinsic"]
        try:
            pose = Pose6D.from_rpy_angles(
                x_metres=_ext["x"], y_metres=_ext["y"], z_metres=_ext["z"],
                roll_degrees=_ext["roll"], pitch_degrees=_ext["pitch"], yaw_degrees=_ext["yaw"]
            )
        except KeyError as e:
            raise PdBadSensorConfigError(str(e))

        # Sensor details
        if 'sensor_intrinsic' in sensor_config or 'camera_intrinsic' in sensor_config:
            # Camera sensor
            camera_intrinsic = sensor_config.get('sensor_intrinsic', {})
            camera_intrinsic.update(sensor_config.get('camera_intrinsic', {}))
            try:
                sensor = CameraSensor(
                    name=name,
                    pose=pose,
                    width=camera_intrinsic['width'],
                    height=camera_intrinsic['height']
                )
            except KeyError as e:
                raise PdBadSensorConfigError(str(e))
            sensor.field_of_view_degrees = camera_intrinsic.get('fov', sensor.field_of_view_degrees)
            sensor.supersample = camera_intrinsic.get('supersample', sensor.supersample)
            sensor.capture_rgb = camera_intrinsic.get('capture_rgb', sensor.capture_rgb)
            sensor.capture_depth = camera_intrinsic.get('capture_depth', sensor.capture_depth)
            sensor.capture_normals = camera_intrinsic.get('capture_normals', sensor.capture_normals)
            sensor.capture_segmentation = camera_intrinsic.get('capture_segmentation', sensor.capture_segmentation)
            sensor.capture_instances = camera_intrinsic.get('capture_instance', sensor.capture_instances)
            sensor.capture_motionvectors = camera_intrinsic.get('capture_motionvectors', sensor.capture_motionvectors)
            sensor.capture_backwardmotionvectors = camera_intrinsic.get('capture_backwardmotionvectors', sensor.capture_backwardmotionvectors)
            sensor.capture_basecolor = camera_intrinsic.get('capture_basecolor', sensor.capture_basecolor)
            sensor.capture_properties = camera_intrinsic.get('capture_properties', sensor.capture_properties)
            if camera_intrinsic.get('capture_detections', False):
                logger.warning(f"'capture_detections' is not currently supported and will have no effect for sensor '{sensor.name}'.")
            sensor.enable_streaming = camera_intrinsic.get('enable_streaming', sensor.enable_streaming)
            sensor.distortion_lookup_table = camera_intrinsic.get('distortion_lookup_table', sensor.distortion_lookup_table) or None
            sensor.lut = camera_intrinsic.get('lut', sensor.lut)
            sensor.lut_weight = camera_intrinsic.get('lut_weight', sensor.lut_weight)
            sensor.time_offset = camera_intrinsic.get('time_offset', sensor.time_offset)
            if 'distortion_params' in camera_intrinsic:
                d = camera_intrinsic['distortion_params']
                sensor.distortion_params = DistortionParams()
                p = sensor.distortion_params
                p.k1 = d.get('k1', p.k1)
                p.k2 = d.get('k2', p.k2)
                p.k3 = d.get('k3', p.k3)
                p.k4 = d.get('k4', p.k4)
                p.k5 = d.get('k5', p.k5)
                p.k6 = d.get('k6', p.k6)
                p.p1 = d.get('p1', p.p1)
                p.p2 = d.get('p2', p.p2)
                p.skew = d.get('skew', p.skew)
                p.is_fisheye = d.get('is_fisheye', p.is_fisheye)
                p.fx = d.get('fx', p.fx)
                p.fy = d.get('fy', p.fy)
                p.cx = d.get('cx', p.cx)
                p.cy = d.get('cy', p.cy)
                sensor.fisheye_model = d.get('fisheye_model', sensor.fisheye_model)
            if 'noise_params' in camera_intrinsic:
                denoise_filter_lut = {
                    "AVERAGE_FILTER": DenoiseFilter.AverageFilter,
                    "MEDIAN_FILTER": DenoiseFilter.MedianFilter,
                    "FAST_MEDIAN_FILTER": DenoiseFilter.FastMedianFilter,
                    "BILATERAL_FILTER": DenoiseFilter.BilateralFilter,
                }
                d = camera_intrinsic['noise_params']
                sensor.noise_params = NoiseParams()
                p = sensor.noise_params
                p.enable_bayer = d.get('enable_bayer', p.enable_bayer)
                p.enable_gauss_noise = d.get('enable_gauss_noise', p.enable_gauss_noise)
                p.enable_poisson_noise = d.get('enable_poisson_noise', p.enable_poisson_noise)
                p.enable_denoise = d.get('enable_denoise', p.enable_denoise)
                p.gauss_noise_sigma = d.get('gauss_noise_sigma', p.gauss_noise_sigma)
                p.poisson_noise_lambda = d.get('poisson_noise_lambda', p.poisson_noise_lambda)
                if 'denoise_filter' in d:
                    p.denoise_filter = denoise_filter_lut[d.get('denoise_filter')]
                p.denoise_filter_size = d.get('denoise_filter_size', p.denoise_filter_size)
                p.bilateral_sigma_d = d.get('bilateral_sigma_d', p.bilateral_sigma_d)
                p.bilateral_sigma_r = d.get('bilateral_sigma_r', p.bilateral_sigma_r)
                p.enable_auto_noise = d.get('enable_auto_noise', p.enable_auto_noise)
                p.signal_amount = d.get('signal_amount', p.signal_amount)
                p.pre_amplifier_noise = d.get('pre_amplifier_noise', p.pre_amplifier_noise)
                p.post_amplifier_noise = d.get('post_amplifier_noise', p.post_amplifier_noise)
                p.is_using_iso = d.get('is_using_iso', p.is_using_iso)
                p.iso_level = d.get('iso_level', p.iso_level)
                p.enable_auto_iso = d.get('enable_auto_iso', p.enable_auto_iso)
                p.fstop = d.get('fstop', p.fstop)
                p.max_exposure_time = d.get('max_exposure_time', p.max_exposure_time)
                p.quantum_efficiency = d.get('quantum_efficiency', p.quantum_efficiency)
            if 'post_process_params' in camera_intrinsic:
                d = camera_intrinsic['post_process_params']
                sensor.post_process_params = PostProcessParams()
                p = sensor.post_process_params
                p.exposure_compensation = d.get('exposure_compensation', p.exposure_compensation)
                p.exposure_speed_up = d.get('exposure_speed_up', p.exposure_speed_up)
                p.exposure_speed_down = d.get('exposure_speed_down', p.exposure_speed_down)
                p.exposure_min_ev100 = d.get('exposure_min_ev100', p.exposure_min_ev100)
                p.exposure_max_ev100 = d.get('exposure_max_ev100', p.exposure_max_ev100)
                p.exposure_compensation_curve = d.get('exposure_compensation_curve', p.exposure_compensation_curve)
                p.exposure_metering_mask = d.get('exposure_metering_mask', p.exposure_metering_mask)
                p.motion_blur_amount = d.get('motion_blur_amount', p.motion_blur_amount)
                p.motion_blur_max = d.get('motion_blur_max', p.motion_blur_max)
                p.dof_focal_distance = d.get('dof_focal_distance', p.dof_focal_distance)
                p.dof_depth_blur_amount = d.get('dof_depth_blur_amount', p.dof_depth_blur_amount)
                p.dof_depth_blur_radius = d.get('dof_depth_blur_radius', p.dof_depth_blur_radius)
                p.vignette_intensity = d.get('vignette_intensity', p.vignette_intensity)
                if 'tone_curve' in d:
                    p.tone_curve = TonemapCurve();
                    tone = d['tone_curve']
                    p.tone_curve.slope = tone.get("slope", p.tone_curve.slope)
                    p.tone_curve.toe = tone.get("toe", p.tone_curve.toe)
                    p.tone_curve.shoulder = tone.get("shoulder", p.tone_curve.shoulder)
                    p.tone_curve.white_clip = tone.get("white_clip", p.tone_curve.white_clip)
                    p.tone_curve.black_clip =tone.get("black_clip", p.tone_curve.black_clip)
            if 'post_process' in camera_intrinsic:
                for d in camera_intrinsic['post_process']:
                    sensor.post_process_materials.append(
                        PostProcessMaterial(material=d['material'], weight=d['weight'])
                    )
            sensors.append(sensor)
        elif 'lidar_intrinsic' in sensor_config:
            # Lidar sensor
            lidar_intrinsic = sensor_config['lidar_intrinsic']
            try:
                sensor = LiDARSensor(
                    name=name,
                    pose=pose,
                    sample_rate=lidar_intrinsic['sample_rate'],
                    rotation_rate=lidar_intrinsic['rotation_rate']
                )
            except KeyError as e:
                raise PdBadSensorConfigError(str(e))
            if 'beam_data' in lidar_intrinsic:
                beam_data = lidar_intrinsic['beam_data']
                for d in beam_data:
                    sensor.beam_data.append(
                        LiDARBeam(
                            id=d['id'],
                            azimuth=d['azimuth'],
                            elevation=d['elevation']
                        )
                    )
            sensor.azimuth_min = lidar_intrinsic.get('azimuth_min', sensor.azimuth_min)
            sensor.azimuth_max = lidar_intrinsic.get('azimuth_max', sensor.azimuth_max)
            sensor.capture_rgb = lidar_intrinsic.get('capture_rgb', sensor.capture_rgb)
            sensor.capture_depth = lidar_intrinsic.get('capture_depth', sensor.capture_depth)
            sensor.capture_normals = lidar_intrinsic.get('capture_normals', sensor.capture_normals)
            sensor.capture_segmentation = lidar_intrinsic.get('capture_segmentation', sensor.capture_segmentation)
            sensor.capture_instances = lidar_intrinsic.get('capture_instance', sensor.capture_instances)
            sensor.capture_motionvectors = lidar_intrinsic.get('capture_motionvectors', sensor.capture_motionvectors)
            if lidar_intrinsic.get('capture_detections', False):
                logger.warning(f"'capture_detections' is not currently supported and will have no effect for sensor '{sensor.name}'.")
            sensors.append(sensor)
        else:
            raise PdBadSensorConfigError("Missing sensor intrinsics")

        sensor.attach_socket = _ext.get('attach_socket', sensor.attach_socket) or None
        sensor.follow_rotation = _ext.get('follow_rotation', sensor.follow_rotation)

    return sensors


def load_sensor_rig(name_or_path: Union[SensorRig, str]) -> List[Sensor]:
    """
    Load a JSON sensor rig specification as its Python equivalent objects

    Args:
        name_or_path: Name of sensor rig or path to the sensor rig file.
                      Use name for loading umd maps provided with the SDK.
                      Use full path for loading umd maps provided separately from the SDK.

    Returns:
        List of sensors
    """
    import pd.internal.sensor_rigs as sensor_rigs_package
    base_rig_path = Path(sensor_rigs_package.__file__).resolve().parent
    if isinstance(name_or_path, SensorRig):
        file_name = name_or_path.value
    elif isinstance(name_or_path, str):
        file_name = name_or_path
    else:
        raise TypeError("Invalid type for sensor rig 'name'")
    # First try internal sensor rigs
    sensor_rig_path = base_rig_path / f"{file_name}.json"
    if not sensor_rig_path.exists():
        # Second try custom file path
        sensor_rig_path = Path(name_or_path)
        if not sensor_rig_path.exists():
            raise PdError(f"Failed to find sensor rig {name_or_path}")
    with open(sensor_rig_path) as sensor_rig_file:
        sensor_rig_json = json.load(sensor_rig_file)
        return sensors_from_json(sensor_rig_json)
