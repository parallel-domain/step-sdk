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
    pd_sensor_pb2
)


class DenoiseFilter(ProtoEnumClass):
    """The type of denoising filter applied to an image."""

    AVERAGE_FILTER = 0
    "Denoising filter using `average` method."
    MEDIAN_FILTER = 1
    "Denoising filter using `median` method."
    FAST_MEDIAN_FILTER = 2
    "Denoising filter using `fast median` method."
    BILATERAL_FILTER = 3
    "Denoising filter using `bilateral` method."


@register_wrapper(proto_type=pd_sensor_pb2.LidarBeam)
class LidarBeam(ProtoMessageClass):
    """
    Object that stores information about an individual lidar beam.

    Args:
        id: :attr:`id`
        azimuth: :attr:`azimuth`
        elevation: :attr:`elevation`
    Attributes:
        id: The integer ID of the lidar beam.
        azimuth: The azimuth of the lidar beam.
        elevation: The elevation of the lidar beam."""

    _proto_message = pd_sensor_pb2.LidarBeam

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.LidarBeam] = None,
        id: int = None,
        azimuth: float = None,
        elevation: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.LidarBeam()
        self.proto = proto
        if id is not None:
            self.id = id
        if azimuth is not None:
            self.azimuth = azimuth
        if elevation is not None:
            self.elevation = elevation

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    @property
    def azimuth(self) -> float:
        return self.proto.azimuth

    @azimuth.setter
    def azimuth(self, value: float):
        self.proto.azimuth = value

    @property
    def elevation(self) -> float:
        return self.proto.elevation

    @elevation.setter
    def elevation(self, value: float):
        self.proto.elevation = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarBeam):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.LidarNoiseParams)
class LidarNoiseParams(ProtoMessageClass):
    """
    Parameters which control the noise applied to Lidar sensors.

    Args:
        min_dist: :attr:`min_dist`
        max_dist: :attr:`max_dist`
        min_prob: :attr:`min_prob`
        max_prob: :attr:`max_prob`
        min_offset: :attr:`min_offset`
        max_offset: :attr:`max_offset`
        min_noise: :attr:`min_noise`
    Attributes:
        min_dist: The minimum distance at which noise is applied to Lidar returns.
        max_dist: The maximum distance at which noise is applied to Lidar returns.
        min_prob: The minimum probability that a particular Lidar beam will be subjected to noise.
        max_prob: The maximum probability that a particular Lidar beam will be subjected to noise.
        min_offset: Minimum offset of the applied noise.
        max_offset: Maximum offset of the applied noise.
        min_noise: The minimum amount of noise applied to a Lidar beam."""

    _proto_message = pd_sensor_pb2.LidarNoiseParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.LidarNoiseParams] = None,
        min_dist: float = None,
        max_dist: float = None,
        min_prob: float = None,
        max_prob: float = None,
        min_offset: float = None,
        max_offset: float = None,
        min_noise: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.LidarNoiseParams()
        self.proto = proto
        if min_dist is not None:
            self.min_dist = min_dist
        if max_dist is not None:
            self.max_dist = max_dist
        if min_prob is not None:
            self.min_prob = min_prob
        if max_prob is not None:
            self.max_prob = max_prob
        if min_offset is not None:
            self.min_offset = min_offset
        if max_offset is not None:
            self.max_offset = max_offset
        if min_noise is not None:
            self.min_noise = min_noise

    @property
    def min_dist(self) -> float:
        return self.proto.min_dist

    @min_dist.setter
    def min_dist(self, value: float):
        self.proto.min_dist = value

    @property
    def max_dist(self) -> float:
        return self.proto.max_dist

    @max_dist.setter
    def max_dist(self, value: float):
        self.proto.max_dist = value

    @property
    def min_prob(self) -> float:
        return self.proto.min_prob

    @min_prob.setter
    def min_prob(self, value: float):
        self.proto.min_prob = value

    @property
    def max_prob(self) -> float:
        return self.proto.max_prob

    @max_prob.setter
    def max_prob(self, value: float):
        self.proto.max_prob = value

    @property
    def min_offset(self) -> float:
        return self.proto.min_offset

    @min_offset.setter
    def min_offset(self, value: float):
        self.proto.min_offset = value

    @property
    def max_offset(self) -> float:
        return self.proto.max_offset

    @max_offset.setter
    def max_offset(self, value: float):
        self.proto.max_offset = value

    @property
    def min_noise(self) -> float:
        return self.proto.min_noise

    @min_noise.setter
    def min_noise(self, value: float):
        self.proto.min_noise = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarNoiseParams):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.AlbedoWeights)
class AlbedoWeights(ProtoMessageClass):
    """
    The weights of rgb channels used to compose the surface albedo for LiDAR beams

    Args:
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
    Attributes:
        x: R channel weight.
            Default: 1.0
        y: G channel weight.
            Default: 0.8
        z: B channel weight.
            Default: 0.4"""

    _proto_message = pd_sensor_pb2.AlbedoWeights

    def __init__(
        self, *, proto: Optional[pd_sensor_pb2.AlbedoWeights] = None, x: float = None, y: float = None, z: float = None
    ):
        if proto is None:
            proto = pd_sensor_pb2.AlbedoWeights()
        self.proto = proto
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def x(self) -> float:
        return self.proto.x

    @x.setter
    def x(self, value: float):
        self.proto.x = value

    @property
    def y(self) -> float:
        return self.proto.y

    @y.setter
    def y(self, value: float):
        self.proto.y = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    def _update_proto_references(self, proto: pd_sensor_pb2.AlbedoWeights):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.LidarIntensityParams)
class LidarIntensityParams(ProtoMessageClass):
    """
    Parameters which control the intensity manipulations applied to Lidar sensors

    Args:
        retro_range_noise_stddev: :attr:`retro_range_noise_stddev`
        retroreflection_noise_mean: :attr:`retroreflection_noise_mean`
        retroreflection_noise_stddev: :attr:`retroreflection_noise_stddev`
        max_attenuation_distance: :attr:`max_attenuation_distance`
        retro_intensity_enhance: :attr:`retro_intensity_enhance`
        intensity_specular_scale: :attr:`intensity_specular_scale`
        intensity_roughness_scale: :attr:`intensity_roughness_scale`
        beam_intensity: :attr:`beam_intensity`
        albedo_weights: :attr:`albedo_weights`
        max_albedo: :attr:`max_albedo`
        strong_retro_intensity_enhance: :attr:`strong_retro_intensity_enhance`
        intensity_metallic_scale: :attr:`intensity_metallic_scale`
        emissive_gate: :attr:`emissive_gate`
        max_emissive_rate: :attr:`max_emissive_rate`
    Attributes:
        retro_range_noise_stddev: Manipulates the depth noise for retro-reflective lidar beams.
            Default: 0.1
        retroreflection_noise_mean: Mean of noise applied to retro-reflective lidar beams.
            Default: 0.0
        retroreflection_noise_stddev: Standard Deviation of noise applied to retro-reflective lidar beams.
            Default: 0.1
        max_attenuation_distance: Maximum distance at which attenuation is applied in meters
            Default: 220.0
        retro_intensity_enhance: Amount by which reflection intensity is enhanced when the beam hits a retroreflective surface. If a value of 1.5 is set,
            the intensity will be 50% stronger.
            Default: 1.5
        intensity_specular_scale: Because the LiDAR beams are infrared light, the specular of the object's surface is higher than with visible light.
            This value adjusts the specular value.
            Default: 2.0
        intensity_roughness_scale: Because the LiDAR beams are infrared light, return beam is scattered more than with visible light.
            This value adjusts the beam spread.
            Default: 1.5
        beam_intensity: Intensity of the beam.
            Default: 2.0
        albedo_weights: The weights of rgb channels used to compose the surface albedo for LiDAR beams.
            Because the LiDAR beams are infrared light, the weight of red should be heavier than green and blue.
        max_albedo: Max surface albedo value, prevents the surface from being too bright.
            Default: 2.2
        strong_retro_intensity_enhance: Parameter that controls how much reflected intensity is enhanced when the beam hits a traffic sign.
            Default: 1.5
        intensity_metallic_scale: Parameter that scales metallic values of surfaces for lidar returns.
            Default: 1.5
        emissive_gate: Parameter that governs how much emissive values will enhance the intensity of lidar returns.
            Default: 100.0
        max_emissive_rate: Maximum emissive value will be :attr:`max_emissive_rate` * :attr:`emissive_gate`
            Default: 10.0"""

    _proto_message = pd_sensor_pb2.LidarIntensityParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.LidarIntensityParams] = None,
        retro_range_noise_stddev: float = None,
        retroreflection_noise_mean: float = None,
        retroreflection_noise_stddev: float = None,
        max_attenuation_distance: float = None,
        retro_intensity_enhance: float = None,
        intensity_specular_scale: float = None,
        intensity_roughness_scale: float = None,
        beam_intensity: float = None,
        albedo_weights: AlbedoWeights = None,
        max_albedo: float = None,
        strong_retro_intensity_enhance: float = None,
        intensity_metallic_scale: float = None,
        emissive_gate: float = None,
        max_emissive_rate: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.LidarIntensityParams()
        self.proto = proto
        self._albedo_weights = get_wrapper(proto_type=proto.albedo_weights.__class__)(proto=proto.albedo_weights)
        if retro_range_noise_stddev is not None:
            self.retro_range_noise_stddev = retro_range_noise_stddev
        if retroreflection_noise_mean is not None:
            self.retroreflection_noise_mean = retroreflection_noise_mean
        if retroreflection_noise_stddev is not None:
            self.retroreflection_noise_stddev = retroreflection_noise_stddev
        if max_attenuation_distance is not None:
            self.max_attenuation_distance = max_attenuation_distance
        if retro_intensity_enhance is not None:
            self.retro_intensity_enhance = retro_intensity_enhance
        if intensity_specular_scale is not None:
            self.intensity_specular_scale = intensity_specular_scale
        if intensity_roughness_scale is not None:
            self.intensity_roughness_scale = intensity_roughness_scale
        if beam_intensity is not None:
            self.beam_intensity = beam_intensity
        if albedo_weights is not None:
            self.albedo_weights = albedo_weights
        if max_albedo is not None:
            self.max_albedo = max_albedo
        if strong_retro_intensity_enhance is not None:
            self.strong_retro_intensity_enhance = strong_retro_intensity_enhance
        if intensity_metallic_scale is not None:
            self.intensity_metallic_scale = intensity_metallic_scale
        if emissive_gate is not None:
            self.emissive_gate = emissive_gate
        if max_emissive_rate is not None:
            self.max_emissive_rate = max_emissive_rate

    @property
    def retro_range_noise_stddev(self) -> float:
        return self.proto.retro_range_noise_stddev

    @retro_range_noise_stddev.setter
    def retro_range_noise_stddev(self, value: float):
        self.proto.retro_range_noise_stddev = value

    @property
    def retroreflection_noise_mean(self) -> float:
        return self.proto.retroreflection_noise_mean

    @retroreflection_noise_mean.setter
    def retroreflection_noise_mean(self, value: float):
        self.proto.retroreflection_noise_mean = value

    @property
    def retroreflection_noise_stddev(self) -> float:
        return self.proto.retroreflection_noise_stddev

    @retroreflection_noise_stddev.setter
    def retroreflection_noise_stddev(self, value: float):
        self.proto.retroreflection_noise_stddev = value

    @property
    def max_attenuation_distance(self) -> float:
        return self.proto.max_attenuation_distance

    @max_attenuation_distance.setter
    def max_attenuation_distance(self, value: float):
        self.proto.max_attenuation_distance = value

    @property
    def retro_intensity_enhance(self) -> float:
        return self.proto.retro_intensity_enhance

    @retro_intensity_enhance.setter
    def retro_intensity_enhance(self, value: float):
        self.proto.retro_intensity_enhance = value

    @property
    def intensity_specular_scale(self) -> float:
        return self.proto.intensity_specular_scale

    @intensity_specular_scale.setter
    def intensity_specular_scale(self, value: float):
        self.proto.intensity_specular_scale = value

    @property
    def intensity_roughness_scale(self) -> float:
        return self.proto.intensity_roughness_scale

    @intensity_roughness_scale.setter
    def intensity_roughness_scale(self, value: float):
        self.proto.intensity_roughness_scale = value

    @property
    def beam_intensity(self) -> float:
        return self.proto.beam_intensity

    @beam_intensity.setter
    def beam_intensity(self, value: float):
        self.proto.beam_intensity = value

    @property
    def albedo_weights(self) -> AlbedoWeights:
        return self._albedo_weights

    @albedo_weights.setter
    def albedo_weights(self, value: AlbedoWeights):
        self.proto.albedo_weights.CopyFrom(value.proto)

        self._albedo_weights = value
        self._albedo_weights._update_proto_references(self.proto.albedo_weights)

    @property
    def max_albedo(self) -> float:
        return self.proto.max_albedo

    @max_albedo.setter
    def max_albedo(self, value: float):
        self.proto.max_albedo = value

    @property
    def strong_retro_intensity_enhance(self) -> float:
        return self.proto.strong_retro_intensity_enhance

    @strong_retro_intensity_enhance.setter
    def strong_retro_intensity_enhance(self, value: float):
        self.proto.strong_retro_intensity_enhance = value

    @property
    def intensity_metallic_scale(self) -> float:
        return self.proto.intensity_metallic_scale

    @intensity_metallic_scale.setter
    def intensity_metallic_scale(self, value: float):
        self.proto.intensity_metallic_scale = value

    @property
    def emissive_gate(self) -> float:
        return self.proto.emissive_gate

    @emissive_gate.setter
    def emissive_gate(self, value: float):
        self.proto.emissive_gate = value

    @property
    def max_emissive_rate(self) -> float:
        return self.proto.max_emissive_rate

    @max_emissive_rate.setter
    def max_emissive_rate(self, value: float):
        self.proto.max_emissive_rate = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarIntensityParams):
        self.proto = proto
        self._albedo_weights._update_proto_references(proto.albedo_weights)


@register_wrapper(proto_type=pd_sensor_pb2.AliceLidarModel)
class AliceLidarModel(ProtoMessageClass):
    """
    Args:
        number_points: :attr:`number_points`
        min_elevation_angle: :attr:`min_elevation_angle`
        max_elevation_angle: :attr:`max_elevation_angle`
        min_dense_elevation_angle: :attr:`min_dense_elevation_angle`
        max_dense_elevation_angle: :attr:`max_dense_elevation_angle`
        min_azimuth_angle: :attr:`min_azimuth_angle`
        max_azimuth_angle: :attr:`max_azimuth_angle`
        sparse_radian_spacing: :attr:`sparse_radian_spacing`
        dense_radian_spacing: :attr:`dense_radian_spacing`
        horizontal_spacing: :attr:`horizontal_spacing`
    Attributes:
        number_points:
        min_elevation_angle:
        max_elevation_angle:
        min_dense_elevation_angle:
        max_dense_elevation_angle:
        min_azimuth_angle:
        max_azimuth_angle:
        sparse_radian_spacing:
        dense_radian_spacing:
        horizontal_spacing:"""

    _proto_message = pd_sensor_pb2.AliceLidarModel

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.AliceLidarModel] = None,
        number_points: int = None,
        min_elevation_angle: float = None,
        max_elevation_angle: float = None,
        min_dense_elevation_angle: float = None,
        max_dense_elevation_angle: float = None,
        min_azimuth_angle: float = None,
        max_azimuth_angle: float = None,
        sparse_radian_spacing: float = None,
        dense_radian_spacing: float = None,
        horizontal_spacing: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.AliceLidarModel()
        self.proto = proto
        if number_points is not None:
            self.number_points = number_points
        if min_elevation_angle is not None:
            self.min_elevation_angle = min_elevation_angle
        if max_elevation_angle is not None:
            self.max_elevation_angle = max_elevation_angle
        if min_dense_elevation_angle is not None:
            self.min_dense_elevation_angle = min_dense_elevation_angle
        if max_dense_elevation_angle is not None:
            self.max_dense_elevation_angle = max_dense_elevation_angle
        if min_azimuth_angle is not None:
            self.min_azimuth_angle = min_azimuth_angle
        if max_azimuth_angle is not None:
            self.max_azimuth_angle = max_azimuth_angle
        if sparse_radian_spacing is not None:
            self.sparse_radian_spacing = sparse_radian_spacing
        if dense_radian_spacing is not None:
            self.dense_radian_spacing = dense_radian_spacing
        if horizontal_spacing is not None:
            self.horizontal_spacing = horizontal_spacing

    @property
    def number_points(self) -> int:
        return self.proto.number_points

    @number_points.setter
    def number_points(self, value: int):
        self.proto.number_points = value

    @property
    def min_elevation_angle(self) -> float:
        return self.proto.min_elevation_angle

    @min_elevation_angle.setter
    def min_elevation_angle(self, value: float):
        self.proto.min_elevation_angle = value

    @property
    def max_elevation_angle(self) -> float:
        return self.proto.max_elevation_angle

    @max_elevation_angle.setter
    def max_elevation_angle(self, value: float):
        self.proto.max_elevation_angle = value

    @property
    def min_dense_elevation_angle(self) -> float:
        return self.proto.min_dense_elevation_angle

    @min_dense_elevation_angle.setter
    def min_dense_elevation_angle(self, value: float):
        self.proto.min_dense_elevation_angle = value

    @property
    def max_dense_elevation_angle(self) -> float:
        return self.proto.max_dense_elevation_angle

    @max_dense_elevation_angle.setter
    def max_dense_elevation_angle(self, value: float):
        self.proto.max_dense_elevation_angle = value

    @property
    def min_azimuth_angle(self) -> float:
        return self.proto.min_azimuth_angle

    @min_azimuth_angle.setter
    def min_azimuth_angle(self, value: float):
        self.proto.min_azimuth_angle = value

    @property
    def max_azimuth_angle(self) -> float:
        return self.proto.max_azimuth_angle

    @max_azimuth_angle.setter
    def max_azimuth_angle(self, value: float):
        self.proto.max_azimuth_angle = value

    @property
    def sparse_radian_spacing(self) -> float:
        return self.proto.sparse_radian_spacing

    @sparse_radian_spacing.setter
    def sparse_radian_spacing(self, value: float):
        self.proto.sparse_radian_spacing = value

    @property
    def dense_radian_spacing(self) -> float:
        return self.proto.dense_radian_spacing

    @dense_radian_spacing.setter
    def dense_radian_spacing(self, value: float):
        self.proto.dense_radian_spacing = value

    @property
    def horizontal_spacing(self) -> float:
        return self.proto.horizontal_spacing

    @horizontal_spacing.setter
    def horizontal_spacing(self, value: float):
        self.proto.horizontal_spacing = value

    def _update_proto_references(self, proto: pd_sensor_pb2.AliceLidarModel):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.LidarIntrinsic)
class LidarIntrinsic(ProtoMessageClass):
    """
    Intrinsic parameters of a Lidar sensor.

    Args:
        sample_rate: :attr:`sample_rate`
        rotation_rate: :attr:`rotation_rate`
        azimuth_min: :attr:`azimuth_min`
        azimuth_max: :attr:`azimuth_max`
        elevation_delta: :attr:`elevation_delta`
        beam_data: :attr:`beam_data`
        capture_rgb: :attr:`capture_rgb`
        capture_intensity: :attr:`capture_intensity`
        capture_depth: :attr:`capture_depth`
        capture_normals: :attr:`capture_normals`
        capture_segmentation: :attr:`capture_segmentation`
        capture_instance: :attr:`capture_instance`
        capture_detections: :attr:`capture_detections`
        capture_motionvectors: :attr:`capture_motionvectors`
        minimum_range_cutoff: :attr:`minimum_range_cutoff`
        maximum_range_cutoff: :attr:`maximum_range_cutoff`
        minimum_cutoff_prob: :attr:`minimum_cutoff_prob`
        maximum_cutoff_prob: :attr:`maximum_cutoff_prob`
        minimum_offset: :attr:`minimum_offset`
        maximum_offset: :attr:`maximum_offset`
        minimum_noise: :attr:`minimum_noise`
        range_noise_mean: :attr:`range_noise_mean`
        range_noise_stddev: :attr:`range_noise_stddev`
        intensity_params: :attr:`intensity_params`
        alice_lidar_model: :attr:`alice_lidar_model`
        pattern: :attr:`pattern`
        time_offset: :attr:`time_offset`
        multi_returns: :attr:`multi_returns`
        multi_returns_angle: :attr:`multi_returns_angle`
        merge_returns: :attr:`merge_returns`
        capture_properties: :attr:`capture_properties`
        capture_backwardmotionvectors: :attr:`capture_backwardmotionvectors`
    Attributes:
        sample_rate: The sampling rate of the lidar.
        rotation_rate: The rotation rate of the lidar.
        azimuth_min: The minimum azimuth value of the lidar.
        azimuth_max: The maximum azimuth value of the lidar.
        elevation_delta: The elevation delta of the lidar.
        beam_data: List of information about the beams that make up the lidar sensor.
        capture_rgb: Flag to control whether RGB data is captured.
        capture_intensity: Flag to control whether intensity data is captured.
        capture_depth: Flag to control whether depth data is captured.
        capture_normals: Flag to control whether surface normal data is captured.
        capture_segmentation: Flag to control whether semantic segmentation data is captured.
        capture_instance: Flag to control whether instance segmentation data is captured.
        capture_detections: Flag to control whether bounding box data is captured.
        capture_motionvectors: Flag to control whether motion vector data is captured.
        minimum_range_cutoff: All returns with closer than this value will not be culled by the range based culling.
            Default: 60.0
        maximum_range_cutoff: All samples farther than this value will always be culled by range based culling.
            Default: 150.0
        minimum_cutoff_prob: The minimum culling probability.
            Default: 0.0
        maximum_cutoff_prob: The maximum culling probability.
            Default: 0.95
        minimum_offset: Minimum offset.
            Default: 0.002
        maximum_offset: Maximum offset.
            Default: 0.02
        minimum_noise: Minimum amount of noise applied to the lidar return.
            Default: 0.001
        range_noise_mean: Mean of the range based noise applied to the lidar returns.
            Default: 0.0
        range_noise_stddev: Standard deviation of the range based noise applied to the lidar returns.
            Default: 0.005
        intensity_params: Parameters which govern the intensity of the lidar sensor.
        alice_lidar_model:
        pattern:
        time_offset: The time offset of the lidar scan pattern.
        multi_returns: How many returns will be added.
        multi_returns_angle: The angles between multiple returns.
            Default: 0.00035
        merge_returns: Controls whether to merge returns into one return or dual returns.
        capture_properties: Flag to control whether material property data is captured.
        capture_backwardmotionvectors: Flag to control whether backwards motion vector data is captured."""

    _proto_message = pd_sensor_pb2.LidarIntrinsic

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.LidarIntrinsic] = None,
        sample_rate: float = None,
        rotation_rate: float = None,
        azimuth_min: float = None,
        azimuth_max: float = None,
        elevation_delta: float = None,
        beam_data: List[LidarBeam] = None,
        capture_rgb: bool = None,
        capture_intensity: bool = None,
        capture_depth: bool = None,
        capture_normals: bool = None,
        capture_segmentation: bool = None,
        capture_instance: bool = None,
        capture_detections: bool = None,
        capture_motionvectors: bool = None,
        minimum_range_cutoff: float = None,
        maximum_range_cutoff: float = None,
        minimum_cutoff_prob: float = None,
        maximum_cutoff_prob: float = None,
        minimum_offset: float = None,
        maximum_offset: float = None,
        minimum_noise: float = None,
        range_noise_mean: float = None,
        range_noise_stddev: float = None,
        intensity_params: LidarIntensityParams = None,
        alice_lidar_model: AliceLidarModel = None,
        pattern: str = None,
        time_offset: float = None,
        multi_returns: int = None,
        multi_returns_angle: float = None,
        merge_returns: int = None,
        capture_properties: bool = None,
        capture_backwardmotionvectors: bool = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.LidarIntrinsic()
        self.proto = proto
        self._beam_data = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.beam_data],
            attr_name="beam_data",
            list_owner=self,
        )
        self._intensity_params = get_wrapper(proto_type=proto.intensity_params.__class__)(proto=proto.intensity_params)
        self._alice_lidar_model = get_wrapper(proto_type=proto.alice_lidar_model.__class__)(
            proto=proto.alice_lidar_model
        )
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if rotation_rate is not None:
            self.rotation_rate = rotation_rate
        if azimuth_min is not None:
            self.azimuth_min = azimuth_min
        if azimuth_max is not None:
            self.azimuth_max = azimuth_max
        if elevation_delta is not None:
            self.elevation_delta = elevation_delta
        if beam_data is not None:
            self.beam_data = beam_data
        if capture_rgb is not None:
            self.capture_rgb = capture_rgb
        if capture_intensity is not None:
            self.capture_intensity = capture_intensity
        if capture_depth is not None:
            self.capture_depth = capture_depth
        if capture_normals is not None:
            self.capture_normals = capture_normals
        if capture_segmentation is not None:
            self.capture_segmentation = capture_segmentation
        if capture_instance is not None:
            self.capture_instance = capture_instance
        if capture_detections is not None:
            self.capture_detections = capture_detections
        if capture_motionvectors is not None:
            self.capture_motionvectors = capture_motionvectors
        if minimum_range_cutoff is not None:
            self.minimum_range_cutoff = minimum_range_cutoff
        if maximum_range_cutoff is not None:
            self.maximum_range_cutoff = maximum_range_cutoff
        if minimum_cutoff_prob is not None:
            self.minimum_cutoff_prob = minimum_cutoff_prob
        if maximum_cutoff_prob is not None:
            self.maximum_cutoff_prob = maximum_cutoff_prob
        if minimum_offset is not None:
            self.minimum_offset = minimum_offset
        if maximum_offset is not None:
            self.maximum_offset = maximum_offset
        if minimum_noise is not None:
            self.minimum_noise = minimum_noise
        if range_noise_mean is not None:
            self.range_noise_mean = range_noise_mean
        if range_noise_stddev is not None:
            self.range_noise_stddev = range_noise_stddev
        if intensity_params is not None:
            self.intensity_params = intensity_params
        if alice_lidar_model is not None:
            self.alice_lidar_model = alice_lidar_model
        if pattern is not None:
            self.pattern = pattern
        if time_offset is not None:
            self.time_offset = time_offset
        if multi_returns is not None:
            self.multi_returns = multi_returns
        if multi_returns_angle is not None:
            self.multi_returns_angle = multi_returns_angle
        if merge_returns is not None:
            self.merge_returns = merge_returns
        if capture_properties is not None:
            self.capture_properties = capture_properties
        if capture_backwardmotionvectors is not None:
            self.capture_backwardmotionvectors = capture_backwardmotionvectors

    @property
    def sample_rate(self) -> float:
        return self.proto.sample_rate

    @sample_rate.setter
    def sample_rate(self, value: float):
        self.proto.sample_rate = value

    @property
    def rotation_rate(self) -> float:
        return self.proto.rotation_rate

    @rotation_rate.setter
    def rotation_rate(self, value: float):
        self.proto.rotation_rate = value

    @property
    def azimuth_min(self) -> float:
        return self.proto.azimuth_min

    @azimuth_min.setter
    def azimuth_min(self, value: float):
        self.proto.azimuth_min = value

    @property
    def azimuth_max(self) -> float:
        return self.proto.azimuth_max

    @azimuth_max.setter
    def azimuth_max(self, value: float):
        self.proto.azimuth_max = value

    @property
    def elevation_delta(self) -> float:
        return self.proto.elevation_delta

    @elevation_delta.setter
    def elevation_delta(self, value: float):
        self.proto.elevation_delta = value

    @property
    def beam_data(self) -> List[LidarBeam]:
        return self._beam_data

    @beam_data.setter
    def beam_data(self, value: List[LidarBeam]):
        self._beam_data.clear()
        for v in value:
            self._beam_data.append(v)

    @property
    def capture_rgb(self) -> bool:
        return self.proto.capture_rgb

    @capture_rgb.setter
    def capture_rgb(self, value: bool):
        self.proto.capture_rgb = value

    @property
    def capture_intensity(self) -> bool:
        return self.proto.capture_intensity

    @capture_intensity.setter
    def capture_intensity(self, value: bool):
        self.proto.capture_intensity = value

    @property
    def capture_depth(self) -> bool:
        return self.proto.capture_depth

    @capture_depth.setter
    def capture_depth(self, value: bool):
        self.proto.capture_depth = value

    @property
    def capture_normals(self) -> bool:
        return self.proto.capture_normals

    @capture_normals.setter
    def capture_normals(self, value: bool):
        self.proto.capture_normals = value

    @property
    def capture_segmentation(self) -> bool:
        return self.proto.capture_segmentation

    @capture_segmentation.setter
    def capture_segmentation(self, value: bool):
        self.proto.capture_segmentation = value

    @property
    def capture_instance(self) -> bool:
        return self.proto.capture_instance

    @capture_instance.setter
    def capture_instance(self, value: bool):
        self.proto.capture_instance = value

    @property
    def capture_detections(self) -> bool:
        return self.proto.capture_detections

    @capture_detections.setter
    def capture_detections(self, value: bool):
        self.proto.capture_detections = value

    @property
    def capture_motionvectors(self) -> bool:
        return self.proto.capture_motionvectors

    @capture_motionvectors.setter
    def capture_motionvectors(self, value: bool):
        self.proto.capture_motionvectors = value

    @property
    def minimum_range_cutoff(self) -> float:
        return self.proto.minimum_range_cutoff

    @minimum_range_cutoff.setter
    def minimum_range_cutoff(self, value: float):
        self.proto.minimum_range_cutoff = value

    @property
    def maximum_range_cutoff(self) -> float:
        return self.proto.maximum_range_cutoff

    @maximum_range_cutoff.setter
    def maximum_range_cutoff(self, value: float):
        self.proto.maximum_range_cutoff = value

    @property
    def minimum_cutoff_prob(self) -> float:
        return self.proto.minimum_cutoff_prob

    @minimum_cutoff_prob.setter
    def minimum_cutoff_prob(self, value: float):
        self.proto.minimum_cutoff_prob = value

    @property
    def maximum_cutoff_prob(self) -> float:
        return self.proto.maximum_cutoff_prob

    @maximum_cutoff_prob.setter
    def maximum_cutoff_prob(self, value: float):
        self.proto.maximum_cutoff_prob = value

    @property
    def minimum_offset(self) -> float:
        return self.proto.minimum_offset

    @minimum_offset.setter
    def minimum_offset(self, value: float):
        self.proto.minimum_offset = value

    @property
    def maximum_offset(self) -> float:
        return self.proto.maximum_offset

    @maximum_offset.setter
    def maximum_offset(self, value: float):
        self.proto.maximum_offset = value

    @property
    def minimum_noise(self) -> float:
        return self.proto.minimum_noise

    @minimum_noise.setter
    def minimum_noise(self, value: float):
        self.proto.minimum_noise = value

    @property
    def range_noise_mean(self) -> float:
        return self.proto.range_noise_mean

    @range_noise_mean.setter
    def range_noise_mean(self, value: float):
        self.proto.range_noise_mean = value

    @property
    def range_noise_stddev(self) -> float:
        return self.proto.range_noise_stddev

    @range_noise_stddev.setter
    def range_noise_stddev(self, value: float):
        self.proto.range_noise_stddev = value

    @property
    def intensity_params(self) -> LidarIntensityParams:
        return self._intensity_params

    @intensity_params.setter
    def intensity_params(self, value: LidarIntensityParams):
        self.proto.intensity_params.CopyFrom(value.proto)

        self._intensity_params = value
        self._intensity_params._update_proto_references(self.proto.intensity_params)

    @property
    def alice_lidar_model(self) -> AliceLidarModel:
        return self._alice_lidar_model

    @alice_lidar_model.setter
    def alice_lidar_model(self, value: AliceLidarModel):
        self.proto.alice_lidar_model.CopyFrom(value.proto)

        self._alice_lidar_model = value
        self._alice_lidar_model._update_proto_references(self.proto.alice_lidar_model)

    @property
    def pattern(self) -> str:
        return self.proto.pattern

    @pattern.setter
    def pattern(self, value: str):
        self.proto.pattern = value

    @property
    def time_offset(self) -> float:
        return self.proto.time_offset

    @time_offset.setter
    def time_offset(self, value: float):
        self.proto.time_offset = value

    @property
    def multi_returns(self) -> int:
        return self.proto.multi_returns

    @multi_returns.setter
    def multi_returns(self, value: int):
        self.proto.multi_returns = value

    @property
    def multi_returns_angle(self) -> float:
        return self.proto.multi_returns_angle

    @multi_returns_angle.setter
    def multi_returns_angle(self, value: float):
        self.proto.multi_returns_angle = value

    @property
    def merge_returns(self) -> int:
        return self.proto.merge_returns

    @merge_returns.setter
    def merge_returns(self, value: int):
        self.proto.merge_returns = value

    @property
    def capture_properties(self) -> bool:
        return self.proto.capture_properties

    @capture_properties.setter
    def capture_properties(self, value: bool):
        self.proto.capture_properties = value

    @property
    def capture_backwardmotionvectors(self) -> bool:
        return self.proto.capture_backwardmotionvectors

    @capture_backwardmotionvectors.setter
    def capture_backwardmotionvectors(self, value: bool):
        self.proto.capture_backwardmotionvectors = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarIntrinsic):
        self.proto = proto
        for i, v in enumerate(self.beam_data):
            v._update_proto_references(self.proto.beam_data[i])
        self._intensity_params._update_proto_references(proto.intensity_params)
        self._alice_lidar_model._update_proto_references(proto.alice_lidar_model)


@register_wrapper(proto_type=pd_sensor_pb2.DistortionParams)
class DistortionParams(ProtoMessageClass):
    """
    Parameters that control the lens distortion applied to RGB camera sensors

    Args:
        k1: :attr:`k1`
        k2: :attr:`k2`
        k3: :attr:`k3`
        k4: :attr:`k4`
        k5: :attr:`k5`
        k6: :attr:`k6`
        p1: :attr:`p1`
        p2: :attr:`p2`
        skew: :attr:`skew`
        is_fisheye: :attr:`is_fisheye`
        fx: :attr:`fx`
        fy: :attr:`fy`
        cx: :attr:`cx`
        cy: :attr:`cy`
        fisheye_model: :attr:`fisheye_model`
    Attributes:
        k1: Radial distortion parameter `k1` if the Brown Conrady or OpenCV Fisheye models are specified in :attr:`fisheye_model`, ignored otherwise.
        k2: Radial distortion parameter `k2` if the Brown Conrady or OpenCV Fisheye models are specified in :attr:`fisheye_model`, ignored otherwise.
        k3: Radial distortion parameter `k3` if the Brown Conrady or OpenCV Fisheye models are specified in :attr:`fisheye_model`, ignored otherwise.
        k4: Radial distortion parameter `k4` if the Brown Conrady or OpenCV Fisheye models are specified in :attr:`fisheye_model`, ignored otherwise.
        k5: Radial distortion parameter `k5` if the Brown Conrady model is specified in :attr:`fisheye_model`. Ignored otherwise.
        k6: Radial distortion parameter `k6` if the Brown Conrady model is specified in :attr:`fisheye_model`. Ignored otherwise.
        p1: Tangential distortion parameter `p1` if the Brown Conrady model is specified in :attr:`fisheye_model`. Ignored otherwise.
        p2: Tangential distortion parameter `p2` if the Brown Conrady model is specified in :attr:`fisheye_model`. Ignored otherwise.
        skew: Parameter controlling the skew distortion that is applied to the camera.
        is_fisheye: DEPRECATED
        fx: The horizontal focal length of the camera.
        fy: Vertical focal length of the camera.
        cx: Distortion center of the image along the horizontal axis.
        cy: Distortion center of the image along the vertical axis.
        fisheye_model: The type of fisheye cameras being replicated. The following are valid values::

                0 - Pinhole Camera if :attr:`k1`,:attr:`k2`,:attr:`p1`,:attr:`p2`[,:attr:`k3`[,:attr:`k4`,:attr:`k5`,:attr:`k6`]] not specified or Brown Conrady Distortion if distortion parameters are specified
                1 - OpenCV Fisheye Distortion
                3 - PD Fisheye Distortion
                6 - Orthographic Projection"""

    _proto_message = pd_sensor_pb2.DistortionParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.DistortionParams] = None,
        k1: float = None,
        k2: float = None,
        k3: float = None,
        k4: float = None,
        k5: float = None,
        k6: float = None,
        p1: float = None,
        p2: float = None,
        skew: float = None,
        is_fisheye: bool = None,
        fx: float = None,
        fy: float = None,
        cx: float = None,
        cy: float = None,
        fisheye_model: int = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.DistortionParams()
        self.proto = proto
        if k1 is not None:
            self.k1 = k1
        if k2 is not None:
            self.k2 = k2
        if k3 is not None:
            self.k3 = k3
        if k4 is not None:
            self.k4 = k4
        if k5 is not None:
            self.k5 = k5
        if k6 is not None:
            self.k6 = k6
        if p1 is not None:
            self.p1 = p1
        if p2 is not None:
            self.p2 = p2
        if skew is not None:
            self.skew = skew
        if is_fisheye is not None:
            self.is_fisheye = is_fisheye
        if fx is not None:
            self.fx = fx
        if fy is not None:
            self.fy = fy
        if cx is not None:
            self.cx = cx
        if cy is not None:
            self.cy = cy
        if fisheye_model is not None:
            self.fisheye_model = fisheye_model

    @property
    def k1(self) -> float:
        return self.proto.k1

    @k1.setter
    def k1(self, value: float):
        self.proto.k1 = value

    @property
    def k2(self) -> float:
        return self.proto.k2

    @k2.setter
    def k2(self, value: float):
        self.proto.k2 = value

    @property
    def k3(self) -> float:
        return self.proto.k3

    @k3.setter
    def k3(self, value: float):
        self.proto.k3 = value

    @property
    def k4(self) -> float:
        return self.proto.k4

    @k4.setter
    def k4(self, value: float):
        self.proto.k4 = value

    @property
    def k5(self) -> float:
        return self.proto.k5

    @k5.setter
    def k5(self, value: float):
        self.proto.k5 = value

    @property
    def k6(self) -> float:
        return self.proto.k6

    @k6.setter
    def k6(self, value: float):
        self.proto.k6 = value

    @property
    def p1(self) -> float:
        return self.proto.p1

    @p1.setter
    def p1(self, value: float):
        self.proto.p1 = value

    @property
    def p2(self) -> float:
        return self.proto.p2

    @p2.setter
    def p2(self, value: float):
        self.proto.p2 = value

    @property
    def skew(self) -> float:
        return self.proto.skew

    @skew.setter
    def skew(self, value: float):
        self.proto.skew = value

    @property
    def is_fisheye(self) -> bool:
        return self.proto.is_fisheye

    @is_fisheye.setter
    def is_fisheye(self, value: bool):
        self.proto.is_fisheye = value

    @property
    def fx(self) -> float:
        return self.proto.fx

    @fx.setter
    def fx(self, value: float):
        self.proto.fx = value

    @property
    def fy(self) -> float:
        return self.proto.fy

    @fy.setter
    def fy(self, value: float):
        self.proto.fy = value

    @property
    def cx(self) -> float:
        return self.proto.cx

    @cx.setter
    def cx(self, value: float):
        self.proto.cx = value

    @property
    def cy(self) -> float:
        return self.proto.cy

    @cy.setter
    def cy(self, value: float):
        self.proto.cy = value

    @property
    def fisheye_model(self) -> int:
        return self.proto.fisheye_model

    @fisheye_model.setter
    def fisheye_model(self, value: int):
        self.proto.fisheye_model = value

    def _update_proto_references(self, proto: pd_sensor_pb2.DistortionParams):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.PostProcessNode)
class PostProcessNode(ProtoMessageClass):
    """
    Node which carries out post processing on a rendered image.

    Args:
        material: :attr:`material`
        weight: :attr:`weight`
    Attributes:
        material: The material to be applied in post processing.
        weight: The weight of the post processing to be applied."""

    _proto_message = pd_sensor_pb2.PostProcessNode

    def __init__(
        self, *, proto: Optional[pd_sensor_pb2.PostProcessNode] = None, material: str = None, weight: float = None
    ):
        if proto is None:
            proto = pd_sensor_pb2.PostProcessNode()
        self.proto = proto
        if material is not None:
            self.material = material
        if weight is not None:
            self.weight = weight

    @property
    def material(self) -> str:
        return self.proto.material

    @material.setter
    def material(self, value: str):
        self.proto.material = value

    @property
    def weight(self) -> float:
        return self.proto.weight

    @weight.setter
    def weight(self, value: float):
        self.proto.weight = value

    def _update_proto_references(self, proto: pd_sensor_pb2.PostProcessNode):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.PostProcessParams)
class PostProcessParams(ProtoMessageClass):
    """
    Parameters that control the post processing applied to rgb camera sensor data.

    Args:
        exposure_compensation: :attr:`exposure_compensation`
        exposure_speed_up: :attr:`exposure_speed_up`
        exposure_speed_down: :attr:`exposure_speed_down`
        exposure_min_ev100: :attr:`exposure_min_ev100`
        exposure_max_ev100: :attr:`exposure_max_ev100`
        exposure_metering_mask: :attr:`exposure_metering_mask`
        motion_blur_amount: :attr:`motion_blur_amount`
        motion_blur_max: :attr:`motion_blur_max`
        dof_focal_distance: :attr:`dof_focal_distance`
        dof_depth_blur_amount: :attr:`dof_depth_blur_amount`
        dof_depth_blur_radius: :attr:`dof_depth_blur_radius`
        vignette_intensity: :attr:`vignette_intensity`
        tone_curve: :attr:`tone_curve`
        exposure_compensation_curve: :attr:`exposure_compensation_curve`
    Attributes:
        exposure_compensation: Logarithmic adjustment for exposure. When set to 0, there will be no adjustment, -1 is two times darker,
            -2 is four times darker, 1 is two times brighter, and 2 is four times brighter
            Default: -100.0
        exposure_speed_up: Speeds up eye adaptation in f-stops per second.
        exposure_speed_down: Slows down eye adaptation in f-stops per second.
        exposure_min_ev100: The minimum brightness limit for auto exposure adaptation, expressed in pixel luminance (cd/m2). Value is typically
            negative and should be less than or equal to Max EV100. As this value increases, the scene view gets darker.
            If Min EV100 is equal to Max EV100, auto exposure is disabled.
            Default: -100.0
        exposure_max_ev100: The maximum brightness limit for auto exposure adaptation, expressed in pixel luminance (cd/m2). Value should be
            positive and should be greater than or equal to Min EV100. As this value decreases, the scene view gets brighter.
            If Max EV100 is equal to Min EV100, auto exposure is disabled.
            Default: -100.0
        exposure_metering_mask: Texture in unreal syntax. Bright spots on the mask will have high influence on auto exposure metering,
            and dark spots will have low influence.
        motion_blur_amount: Motion blur amount expressed in screen percentage (exposure will affect the final outcome).
            Default: 1.5
        motion_blur_max: Maximum motion blue amount in screen percentage.
            Default: 5.0
        dof_focal_distance: Focal distance (in cm) to near focal plane.
            Default: -1.0
        dof_depth_blur_amount: Distance (in km) where we blur to 50%.
        dof_depth_blur_radius: Radius of how many pixels to blur.
            Default: -1.0
        vignette_intensity: Strength of vignette applied.
        tone_curve: Type of tone curve applied to the image.
        exposure_compensation_curve: Curve in unreal syntax. The X and Y-axis values in the Curve graph translate to the Average Scene EV100 and
            Exposure Compensation (Curve) values"""

    _proto_message = pd_sensor_pb2.PostProcessParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.PostProcessParams] = None,
        exposure_compensation: float = None,
        exposure_speed_up: float = None,
        exposure_speed_down: float = None,
        exposure_min_ev100: float = None,
        exposure_max_ev100: float = None,
        exposure_metering_mask: str = None,
        motion_blur_amount: float = None,
        motion_blur_max: float = None,
        dof_focal_distance: float = None,
        dof_depth_blur_amount: float = None,
        dof_depth_blur_radius: float = None,
        vignette_intensity: float = None,
        tone_curve: ToneCurveParams = None,
        exposure_compensation_curve: str = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.PostProcessParams()
        self.proto = proto
        self._tone_curve = get_wrapper(proto_type=proto.tone_curve.__class__)(proto=proto.tone_curve)
        if exposure_compensation is not None:
            self.exposure_compensation = exposure_compensation
        if exposure_speed_up is not None:
            self.exposure_speed_up = exposure_speed_up
        if exposure_speed_down is not None:
            self.exposure_speed_down = exposure_speed_down
        if exposure_min_ev100 is not None:
            self.exposure_min_ev100 = exposure_min_ev100
        if exposure_max_ev100 is not None:
            self.exposure_max_ev100 = exposure_max_ev100
        if exposure_metering_mask is not None:
            self.exposure_metering_mask = exposure_metering_mask
        if motion_blur_amount is not None:
            self.motion_blur_amount = motion_blur_amount
        if motion_blur_max is not None:
            self.motion_blur_max = motion_blur_max
        if dof_focal_distance is not None:
            self.dof_focal_distance = dof_focal_distance
        if dof_depth_blur_amount is not None:
            self.dof_depth_blur_amount = dof_depth_blur_amount
        if dof_depth_blur_radius is not None:
            self.dof_depth_blur_radius = dof_depth_blur_radius
        if vignette_intensity is not None:
            self.vignette_intensity = vignette_intensity
        if tone_curve is not None:
            self.tone_curve = tone_curve
        if exposure_compensation_curve is not None:
            self.exposure_compensation_curve = exposure_compensation_curve

    @property
    def exposure_compensation(self) -> float:
        return self.proto.exposure_compensation

    @exposure_compensation.setter
    def exposure_compensation(self, value: float):
        self.proto.exposure_compensation = value

    @property
    def exposure_speed_up(self) -> float:
        return self.proto.exposure_speed_up

    @exposure_speed_up.setter
    def exposure_speed_up(self, value: float):
        self.proto.exposure_speed_up = value

    @property
    def exposure_speed_down(self) -> float:
        return self.proto.exposure_speed_down

    @exposure_speed_down.setter
    def exposure_speed_down(self, value: float):
        self.proto.exposure_speed_down = value

    @property
    def exposure_min_ev100(self) -> float:
        return self.proto.exposure_min_ev100

    @exposure_min_ev100.setter
    def exposure_min_ev100(self, value: float):
        self.proto.exposure_min_ev100 = value

    @property
    def exposure_max_ev100(self) -> float:
        return self.proto.exposure_max_ev100

    @exposure_max_ev100.setter
    def exposure_max_ev100(self, value: float):
        self.proto.exposure_max_ev100 = value

    @property
    def exposure_metering_mask(self) -> str:
        return self.proto.exposure_metering_mask

    @exposure_metering_mask.setter
    def exposure_metering_mask(self, value: str):
        self.proto.exposure_metering_mask = value

    @property
    def motion_blur_amount(self) -> float:
        return self.proto.motion_blur_amount

    @motion_blur_amount.setter
    def motion_blur_amount(self, value: float):
        self.proto.motion_blur_amount = value

    @property
    def motion_blur_max(self) -> float:
        return self.proto.motion_blur_max

    @motion_blur_max.setter
    def motion_blur_max(self, value: float):
        self.proto.motion_blur_max = value

    @property
    def dof_focal_distance(self) -> float:
        return self.proto.dof_focal_distance

    @dof_focal_distance.setter
    def dof_focal_distance(self, value: float):
        self.proto.dof_focal_distance = value

    @property
    def dof_depth_blur_amount(self) -> float:
        return self.proto.dof_depth_blur_amount

    @dof_depth_blur_amount.setter
    def dof_depth_blur_amount(self, value: float):
        self.proto.dof_depth_blur_amount = value

    @property
    def dof_depth_blur_radius(self) -> float:
        return self.proto.dof_depth_blur_radius

    @dof_depth_blur_radius.setter
    def dof_depth_blur_radius(self, value: float):
        self.proto.dof_depth_blur_radius = value

    @property
    def vignette_intensity(self) -> float:
        return self.proto.vignette_intensity

    @vignette_intensity.setter
    def vignette_intensity(self, value: float):
        self.proto.vignette_intensity = value

    @property
    def tone_curve(self) -> ToneCurveParams:
        return self._tone_curve

    @tone_curve.setter
    def tone_curve(self, value: ToneCurveParams):
        self.proto.tone_curve.CopyFrom(value.proto)

        self._tone_curve = value
        self._tone_curve._update_proto_references(self.proto.tone_curve)

    @property
    def exposure_compensation_curve(self) -> str:
        return self.proto.exposure_compensation_curve

    @exposure_compensation_curve.setter
    def exposure_compensation_curve(self, value: str):
        self.proto.exposure_compensation_curve = value

    def _update_proto_references(self, proto: pd_sensor_pb2.PostProcessParams):
        self.proto = proto
        self._tone_curve._update_proto_references(proto.tone_curve)


@register_wrapper(proto_type=pd_sensor_pb2.ToneCurveParams)
class ToneCurveParams(ProtoMessageClass):
    """
    Parameters that control the tone curve applied to the image.

    Args:
        slope: :attr:`slope`
        toe: :attr:`toe`
        shoulder: :attr:`shoulder`
        black_clip: :attr:`black_clip`
        white_clip: :attr:`white_clip`
    Attributes:
        slope: A slope tone curve.
            Default: 0.66
        toe: A toe tone curve.
            Default: 0.52
        shoulder: A shoulder tone curve.
            Default: 0.49
        black_clip: A black_clip tone curve.
            Default: 0.0
        white_clip: A white_clip tone curve.
            Default: 0.08"""

    _proto_message = pd_sensor_pb2.ToneCurveParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.ToneCurveParams] = None,
        slope: float = None,
        toe: float = None,
        shoulder: float = None,
        black_clip: float = None,
        white_clip: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.ToneCurveParams()
        self.proto = proto
        if slope is not None:
            self.slope = slope
        if toe is not None:
            self.toe = toe
        if shoulder is not None:
            self.shoulder = shoulder
        if black_clip is not None:
            self.black_clip = black_clip
        if white_clip is not None:
            self.white_clip = white_clip

    @property
    def slope(self) -> float:
        return self.proto.slope

    @slope.setter
    def slope(self, value: float):
        self.proto.slope = value

    @property
    def toe(self) -> float:
        return self.proto.toe

    @toe.setter
    def toe(self, value: float):
        self.proto.toe = value

    @property
    def shoulder(self) -> float:
        return self.proto.shoulder

    @shoulder.setter
    def shoulder(self, value: float):
        self.proto.shoulder = value

    @property
    def black_clip(self) -> float:
        return self.proto.black_clip

    @black_clip.setter
    def black_clip(self, value: float):
        self.proto.black_clip = value

    @property
    def white_clip(self) -> float:
        return self.proto.white_clip

    @white_clip.setter
    def white_clip(self, value: float):
        self.proto.white_clip = value

    def _update_proto_references(self, proto: pd_sensor_pb2.ToneCurveParams):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.NoiseParams)
class NoiseParams(ProtoMessageClass):
    """
    Args:
        enable_bayer: :attr:`enable_bayer`
        enable_gauss_noise: :attr:`enable_gauss_noise`
        enable_poisson_noise: :attr:`enable_poisson_noise`
        enable_denoise: :attr:`enable_denoise`
        gauss_noise_sigma: :attr:`gauss_noise_sigma`
        poisson_noise_lambda: :attr:`poisson_noise_lambda`
        denoise_filter: :attr:`denoise_filter`
        denoise_filter_size: :attr:`denoise_filter_size`
        bilateral_sigma_d: :attr:`bilateral_sigma_d`
        bilateral_sigma_r: :attr:`bilateral_sigma_r`
        enable_auto_noise: :attr:`enable_auto_noise`
        signal_amount: :attr:`signal_amount`
        pre_amplifier_noise: :attr:`pre_amplifier_noise`
        post_amplifier_noise: :attr:`post_amplifier_noise`
        is_using_iso: :attr:`is_using_iso`
        iso_level: :attr:`iso_level`
        enable_auto_iso: :attr:`enable_auto_iso`
        fstop: :attr:`fstop`
        max_exposure_time: :attr:`max_exposure_time`
        quantum_efficiency: :attr:`quantum_efficiency`
    Attributes:
        enable_bayer: Flag to enable Bayer noise, also known as RGGB noise, simulates the noise patterns present when using a Bayer filter
            to capture color images. This filter is a common way to capture color in digital cameras. It shows up as a colors
            shifting away from pixels.
            Default: True
        enable_gauss_noise: Flag to enable Gaussian noise, also known as white noise, simulates electronic interference caused by thermal
            vibrations. This type of noise is tied to the temperature of the sensor and the brightness of the scene being
            captured - this adds noise uniformly on the image
            Default: True
        enable_poisson_noise: Flag to enable Poisson Noise. Simulates the probability of photons being collected by the sensor. This is the most
            common form of noise in an image, unless it is a low-light capture. Poisson noise is a good way to simulate the
            natural behavior of photons in an image. This adds more noise to brighter areas, less to darker areas.
            Default: True
        enable_denoise: Flag to add a denoise pass to mimic a real sensor’s stack.
            Default: True
        gauss_noise_sigma: Sigma applied when Gauss Noise is activated. Larger values result in noisier images.
            Default: 0.025
        poisson_noise_lambda: Lambda applied to poisson noise. Smaller values result in noisier images.
            Default: 1000.0
        denoise_filter: Type of denoising filter applied.
            Default: :attr:`DenoiseFilter.MEDIAN_FILTER`
        denoise_filter_size: Only applies to Bilateral denoising filter. Represents how many pixels to sample.
            Default: 3
        bilateral_sigma_d: Spatial `sigma_d` of bilateral denoising filter.
            Default: 3.0
        bilateral_sigma_r: `sigma_r` of bilateral denoising filter.
            Default: 20.0
        enable_auto_noise: Boolean to enable automatic setting of noise parameters based on exposure value.
            Default: True
        signal_amount: Signal amount.
            Default: 5223
        pre_amplifier_noise: Pre-amplifier noise.
            Default: 7.63
        post_amplifier_noise: Post-amplifier noise.
            Default: 247.5
        is_using_iso: Boolean flag to control whether ISO is used to adjust noise parameters
            Default: True
        iso_level: ISO level of the camera.
            Default: 800
        enable_auto_iso: Controls whether IDO is used to scale noise parameters.
        fstop: F-Stop of the camera.
            Default: 1.0
        max_exposure_time: Inverse of the minimum shutter speed.
            Default: 0.033
        quantum_efficiency: Used when calculating auto ISO defaults.
            Default: 0.7"""

    _proto_message = pd_sensor_pb2.NoiseParams

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.NoiseParams] = None,
        enable_bayer: bool = None,
        enable_gauss_noise: bool = None,
        enable_poisson_noise: bool = None,
        enable_denoise: bool = None,
        gauss_noise_sigma: float = None,
        poisson_noise_lambda: float = None,
        denoise_filter: DenoiseFilter = None,
        denoise_filter_size: int = None,
        bilateral_sigma_d: float = None,
        bilateral_sigma_r: float = None,
        enable_auto_noise: bool = None,
        signal_amount: int = None,
        pre_amplifier_noise: float = None,
        post_amplifier_noise: float = None,
        is_using_iso: bool = None,
        iso_level: int = None,
        enable_auto_iso: bool = None,
        fstop: float = None,
        max_exposure_time: float = None,
        quantum_efficiency: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.NoiseParams()
        self.proto = proto
        if enable_bayer is not None:
            self.enable_bayer = enable_bayer
        if enable_gauss_noise is not None:
            self.enable_gauss_noise = enable_gauss_noise
        if enable_poisson_noise is not None:
            self.enable_poisson_noise = enable_poisson_noise
        if enable_denoise is not None:
            self.enable_denoise = enable_denoise
        if gauss_noise_sigma is not None:
            self.gauss_noise_sigma = gauss_noise_sigma
        if poisson_noise_lambda is not None:
            self.poisson_noise_lambda = poisson_noise_lambda
        if denoise_filter is not None:
            self.denoise_filter = denoise_filter
        if denoise_filter_size is not None:
            self.denoise_filter_size = denoise_filter_size
        if bilateral_sigma_d is not None:
            self.bilateral_sigma_d = bilateral_sigma_d
        if bilateral_sigma_r is not None:
            self.bilateral_sigma_r = bilateral_sigma_r
        if enable_auto_noise is not None:
            self.enable_auto_noise = enable_auto_noise
        if signal_amount is not None:
            self.signal_amount = signal_amount
        if pre_amplifier_noise is not None:
            self.pre_amplifier_noise = pre_amplifier_noise
        if post_amplifier_noise is not None:
            self.post_amplifier_noise = post_amplifier_noise
        if is_using_iso is not None:
            self.is_using_iso = is_using_iso
        if iso_level is not None:
            self.iso_level = iso_level
        if enable_auto_iso is not None:
            self.enable_auto_iso = enable_auto_iso
        if fstop is not None:
            self.fstop = fstop
        if max_exposure_time is not None:
            self.max_exposure_time = max_exposure_time
        if quantum_efficiency is not None:
            self.quantum_efficiency = quantum_efficiency

    @property
    def enable_bayer(self) -> bool:
        return self.proto.enable_bayer

    @enable_bayer.setter
    def enable_bayer(self, value: bool):
        self.proto.enable_bayer = value

    @property
    def enable_gauss_noise(self) -> bool:
        return self.proto.enable_gauss_noise

    @enable_gauss_noise.setter
    def enable_gauss_noise(self, value: bool):
        self.proto.enable_gauss_noise = value

    @property
    def enable_poisson_noise(self) -> bool:
        return self.proto.enable_poisson_noise

    @enable_poisson_noise.setter
    def enable_poisson_noise(self, value: bool):
        self.proto.enable_poisson_noise = value

    @property
    def enable_denoise(self) -> bool:
        return self.proto.enable_denoise

    @enable_denoise.setter
    def enable_denoise(self, value: bool):
        self.proto.enable_denoise = value

    @property
    def gauss_noise_sigma(self) -> float:
        return self.proto.gauss_noise_sigma

    @gauss_noise_sigma.setter
    def gauss_noise_sigma(self, value: float):
        self.proto.gauss_noise_sigma = value

    @property
    def poisson_noise_lambda(self) -> float:
        return self.proto.poisson_noise_lambda

    @poisson_noise_lambda.setter
    def poisson_noise_lambda(self, value: float):
        self.proto.poisson_noise_lambda = value

    @property
    def denoise_filter(self) -> DenoiseFilter:
        return self.proto.denoise_filter

    @denoise_filter.setter
    def denoise_filter(self, value: DenoiseFilter):
        self.proto.denoise_filter = value

    @property
    def denoise_filter_size(self) -> int:
        return self.proto.denoise_filter_size

    @denoise_filter_size.setter
    def denoise_filter_size(self, value: int):
        self.proto.denoise_filter_size = value

    @property
    def bilateral_sigma_d(self) -> float:
        return self.proto.bilateral_sigma_d

    @bilateral_sigma_d.setter
    def bilateral_sigma_d(self, value: float):
        self.proto.bilateral_sigma_d = value

    @property
    def bilateral_sigma_r(self) -> float:
        return self.proto.bilateral_sigma_r

    @bilateral_sigma_r.setter
    def bilateral_sigma_r(self, value: float):
        self.proto.bilateral_sigma_r = value

    @property
    def enable_auto_noise(self) -> bool:
        return self.proto.enable_auto_noise

    @enable_auto_noise.setter
    def enable_auto_noise(self, value: bool):
        self.proto.enable_auto_noise = value

    @property
    def signal_amount(self) -> int:
        return self.proto.signal_amount

    @signal_amount.setter
    def signal_amount(self, value: int):
        self.proto.signal_amount = value

    @property
    def pre_amplifier_noise(self) -> float:
        return self.proto.pre_amplifier_noise

    @pre_amplifier_noise.setter
    def pre_amplifier_noise(self, value: float):
        self.proto.pre_amplifier_noise = value

    @property
    def post_amplifier_noise(self) -> float:
        return self.proto.post_amplifier_noise

    @post_amplifier_noise.setter
    def post_amplifier_noise(self, value: float):
        self.proto.post_amplifier_noise = value

    @property
    def is_using_iso(self) -> bool:
        return self.proto.is_using_iso

    @is_using_iso.setter
    def is_using_iso(self, value: bool):
        self.proto.is_using_iso = value

    @property
    def iso_level(self) -> int:
        return self.proto.iso_level

    @iso_level.setter
    def iso_level(self, value: int):
        self.proto.iso_level = value

    @property
    def enable_auto_iso(self) -> bool:
        return self.proto.enable_auto_iso

    @enable_auto_iso.setter
    def enable_auto_iso(self, value: bool):
        self.proto.enable_auto_iso = value

    @property
    def fstop(self) -> float:
        return self.proto.fstop

    @fstop.setter
    def fstop(self, value: float):
        self.proto.fstop = value

    @property
    def max_exposure_time(self) -> float:
        return self.proto.max_exposure_time

    @max_exposure_time.setter
    def max_exposure_time(self, value: float):
        self.proto.max_exposure_time = value

    @property
    def quantum_efficiency(self) -> float:
        return self.proto.quantum_efficiency

    @quantum_efficiency.setter
    def quantum_efficiency(self, value: float):
        self.proto.quantum_efficiency = value

    def _update_proto_references(self, proto: pd_sensor_pb2.NoiseParams):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.CameraIntrinsic)
class CameraIntrinsic(ProtoMessageClass):
    """
    Parameters which control the intrinsics of an rgb camera sensor.

    Args:
        width: :attr:`width`
        height: :attr:`height`
        fov: :attr:`fov`
        supersample: :attr:`supersample`
        capture_rgb: :attr:`capture_rgb`
        capture_depth: :attr:`capture_depth`
        capture_normals: :attr:`capture_normals`
        capture_segmentation: :attr:`capture_segmentation`
        capture_instance: :attr:`capture_instance`
        capture_detections: :attr:`capture_detections`
        capture_motionvectors: :attr:`capture_motionvectors`
        lut: :attr:`lut`
        lut_weight: :attr:`lut_weight`
        post_process_params: :attr:`post_process_params`
        post_process: :attr:`post_process`
        distortion_params: :attr:`distortion_params`
        noise_params: :attr:`noise_params`
        enable_streaming: :attr:`enable_streaming`
        transmit_gray: :attr:`transmit_gray`
        distortion_lookup_table: :attr:`distortion_lookup_table`
        capture_basecolor: :attr:`capture_basecolor`
        capture_properties: :attr:`capture_properties`
        time_offset: :attr:`time_offset`
        capture_backwardmotionvectors: :attr:`capture_backwardmotionvectors`
    Attributes:
        width: Width of the image in pixels
        height: Height of the image in pixels.
        fov: Field of view of the camera in degrees. Ignored when `fx`, `fy`, `cx` and `cy` are set in :obj:`DistortionParams`.
        supersample: Supersampling to apply during rendering.  Supersampling is ignored on pinhole cameras.
        capture_rgb: Flag to control whether RGB data is captured.
        capture_depth: Flag to control whether depth data is captured.
        capture_normals: Flag to control whether surface normal data is captured.
        capture_segmentation: Flag to control whether semantic segmentation data is captured.
        capture_instance: Flag to control whether instance segmentation data is captured.
        capture_detections: Flag to control whether bounding box data is captured.
        capture_motionvectors: Flag to control whether motion vector data is captured.
        lut: Path to color adjustment map in unreal syntax.
        lut_weight: Scale factor when applying :attr:`lut`.
            Default: 1.0
        post_process_params: Post processing parameters to apply to the rendered image.
        post_process: Array of ‘post_process_entries’, each of which has an unreal material path and a weight (to blend with the previous
            image). “material” is the path in unreal syntax and “weight” is the blend weight (0->1).
        distortion_params: The distortion parameters to apply to the image.
        noise_params: The noise parameters to apply to the image.
        enable_streaming:
        transmit_gray: Control whether the returned image is grayscale.
        distortion_lookup_table: Path to the distortion lookup table if a lookup table is required by :obj:`DistortionParams`.
        capture_basecolor: Flag to control whether base color data is captured.
        capture_properties: Flag to control whether material propety data is captured.
        time_offset: Time offset of captured images.
        capture_backwardmotionvectors: Flag to control whether backwards motion vector data is captured."""

    _proto_message = pd_sensor_pb2.CameraIntrinsic

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.CameraIntrinsic] = None,
        width: int = None,
        height: int = None,
        fov: float = None,
        supersample: float = None,
        capture_rgb: bool = None,
        capture_depth: bool = None,
        capture_normals: bool = None,
        capture_segmentation: bool = None,
        capture_instance: bool = None,
        capture_detections: bool = None,
        capture_motionvectors: bool = None,
        lut: str = None,
        lut_weight: float = None,
        post_process_params: PostProcessParams = None,
        post_process: List[PostProcessNode] = None,
        distortion_params: DistortionParams = None,
        noise_params: NoiseParams = None,
        enable_streaming: bool = None,
        transmit_gray: bool = None,
        distortion_lookup_table: str = None,
        capture_basecolor: bool = None,
        capture_properties: bool = None,
        time_offset: float = None,
        capture_backwardmotionvectors: bool = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.CameraIntrinsic()
        self.proto = proto
        self._post_process_params = get_wrapper(proto_type=proto.post_process_params.__class__)(
            proto=proto.post_process_params
        )
        self._post_process = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.post_process],
            attr_name="post_process",
            list_owner=self,
        )
        self._distortion_params = get_wrapper(proto_type=proto.distortion_params.__class__)(
            proto=proto.distortion_params
        )
        self._noise_params = get_wrapper(proto_type=proto.noise_params.__class__)(proto=proto.noise_params)
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if fov is not None:
            self.fov = fov
        if supersample is not None:
            self.supersample = supersample
        if capture_rgb is not None:
            self.capture_rgb = capture_rgb
        if capture_depth is not None:
            self.capture_depth = capture_depth
        if capture_normals is not None:
            self.capture_normals = capture_normals
        if capture_segmentation is not None:
            self.capture_segmentation = capture_segmentation
        if capture_instance is not None:
            self.capture_instance = capture_instance
        if capture_detections is not None:
            self.capture_detections = capture_detections
        if capture_motionvectors is not None:
            self.capture_motionvectors = capture_motionvectors
        if lut is not None:
            self.lut = lut
        if lut_weight is not None:
            self.lut_weight = lut_weight
        if post_process_params is not None:
            self.post_process_params = post_process_params
        if post_process is not None:
            self.post_process = post_process
        if distortion_params is not None:
            self.distortion_params = distortion_params
        if noise_params is not None:
            self.noise_params = noise_params
        if enable_streaming is not None:
            self.enable_streaming = enable_streaming
        if transmit_gray is not None:
            self.transmit_gray = transmit_gray
        if distortion_lookup_table is not None:
            self.distortion_lookup_table = distortion_lookup_table
        if capture_basecolor is not None:
            self.capture_basecolor = capture_basecolor
        if capture_properties is not None:
            self.capture_properties = capture_properties
        if time_offset is not None:
            self.time_offset = time_offset
        if capture_backwardmotionvectors is not None:
            self.capture_backwardmotionvectors = capture_backwardmotionvectors

    @property
    def width(self) -> int:
        return self.proto.width

    @width.setter
    def width(self, value: int):
        self.proto.width = value

    @property
    def height(self) -> int:
        return self.proto.height

    @height.setter
    def height(self, value: int):
        self.proto.height = value

    @property
    def fov(self) -> float:
        return self.proto.fov

    @fov.setter
    def fov(self, value: float):
        self.proto.fov = value

    @property
    def supersample(self) -> float:
        return self.proto.supersample

    @supersample.setter
    def supersample(self, value: float):
        self.proto.supersample = value

    @property
    def capture_rgb(self) -> bool:
        return self.proto.capture_rgb

    @capture_rgb.setter
    def capture_rgb(self, value: bool):
        self.proto.capture_rgb = value

    @property
    def capture_depth(self) -> bool:
        return self.proto.capture_depth

    @capture_depth.setter
    def capture_depth(self, value: bool):
        self.proto.capture_depth = value

    @property
    def capture_normals(self) -> bool:
        return self.proto.capture_normals

    @capture_normals.setter
    def capture_normals(self, value: bool):
        self.proto.capture_normals = value

    @property
    def capture_segmentation(self) -> bool:
        return self.proto.capture_segmentation

    @capture_segmentation.setter
    def capture_segmentation(self, value: bool):
        self.proto.capture_segmentation = value

    @property
    def capture_instance(self) -> bool:
        return self.proto.capture_instance

    @capture_instance.setter
    def capture_instance(self, value: bool):
        self.proto.capture_instance = value

    @property
    def capture_detections(self) -> bool:
        return self.proto.capture_detections

    @capture_detections.setter
    def capture_detections(self, value: bool):
        self.proto.capture_detections = value

    @property
    def capture_motionvectors(self) -> bool:
        return self.proto.capture_motionvectors

    @capture_motionvectors.setter
    def capture_motionvectors(self, value: bool):
        self.proto.capture_motionvectors = value

    @property
    def lut(self) -> str:
        return self.proto.lut

    @lut.setter
    def lut(self, value: str):
        self.proto.lut = value

    @property
    def lut_weight(self) -> float:
        return self.proto.lut_weight

    @lut_weight.setter
    def lut_weight(self, value: float):
        self.proto.lut_weight = value

    @property
    def post_process_params(self) -> PostProcessParams:
        return self._post_process_params

    @post_process_params.setter
    def post_process_params(self, value: PostProcessParams):
        self.proto.post_process_params.CopyFrom(value.proto)

        self._post_process_params = value
        self._post_process_params._update_proto_references(self.proto.post_process_params)

    @property
    def post_process(self) -> List[PostProcessNode]:
        return self._post_process

    @post_process.setter
    def post_process(self, value: List[PostProcessNode]):
        self._post_process.clear()
        for v in value:
            self._post_process.append(v)

    @property
    def distortion_params(self) -> DistortionParams:
        return self._distortion_params

    @distortion_params.setter
    def distortion_params(self, value: DistortionParams):
        self.proto.distortion_params.CopyFrom(value.proto)

        self._distortion_params = value
        self._distortion_params._update_proto_references(self.proto.distortion_params)

    @property
    def noise_params(self) -> NoiseParams:
        return self._noise_params

    @noise_params.setter
    def noise_params(self, value: NoiseParams):
        self.proto.noise_params.CopyFrom(value.proto)

        self._noise_params = value
        self._noise_params._update_proto_references(self.proto.noise_params)

    @property
    def enable_streaming(self) -> bool:
        return self.proto.enable_streaming

    @enable_streaming.setter
    def enable_streaming(self, value: bool):
        self.proto.enable_streaming = value

    @property
    def transmit_gray(self) -> bool:
        return self.proto.transmit_gray

    @transmit_gray.setter
    def transmit_gray(self, value: bool):
        self.proto.transmit_gray = value

    @property
    def distortion_lookup_table(self) -> str:
        return self.proto.distortion_lookup_table

    @distortion_lookup_table.setter
    def distortion_lookup_table(self, value: str):
        self.proto.distortion_lookup_table = value

    @property
    def capture_basecolor(self) -> bool:
        return self.proto.capture_basecolor

    @capture_basecolor.setter
    def capture_basecolor(self, value: bool):
        self.proto.capture_basecolor = value

    @property
    def capture_properties(self) -> bool:
        return self.proto.capture_properties

    @capture_properties.setter
    def capture_properties(self, value: bool):
        self.proto.capture_properties = value

    @property
    def time_offset(self) -> float:
        return self.proto.time_offset

    @time_offset.setter
    def time_offset(self, value: float):
        self.proto.time_offset = value

    @property
    def capture_backwardmotionvectors(self) -> bool:
        return self.proto.capture_backwardmotionvectors

    @capture_backwardmotionvectors.setter
    def capture_backwardmotionvectors(self, value: bool):
        self.proto.capture_backwardmotionvectors = value

    def _update_proto_references(self, proto: pd_sensor_pb2.CameraIntrinsic):
        self.proto = proto
        self._post_process_params._update_proto_references(proto.post_process_params)
        for i, v in enumerate(self.post_process):
            v._update_proto_references(self.proto.post_process[i])
        self._distortion_params._update_proto_references(proto.distortion_params)
        self._noise_params._update_proto_references(proto.noise_params)


@register_wrapper(proto_type=pd_sensor_pb2.RadarBasicParameters)
class RadarBasicParameters(ProtoMessageClass):
    """
    Args:
        max_range: :attr:`max_range`
        range_resolution: :attr:`range_resolution`
        max_doppler: :attr:`max_doppler`
        doppler_resolution: :attr:`doppler_resolution`
        azimuth_fov: :attr:`azimuth_fov`
        azimuth_resolution: :attr:`azimuth_resolution`
        elevation_fov: :attr:`elevation_fov`
        elevation_resolution: :attr:`elevation_resolution`
        radar_output_2d: :attr:`radar_output_2d`
        use_random_raycast: :attr:`use_random_raycast`
        number_rays_per_frame: :attr:`number_rays_per_frame`
        azimuth_accuracy: :attr:`azimuth_accuracy`
        elevation_accuracy: :attr:`elevation_accuracy`
        prf_profile_file: :attr:`prf_profile_file`
    Attributes:
        max_range: Default: 204.8
        range_resolution: Default: 0.8
        max_doppler: Default: 30.0
        doppler_resolution: Default: 0.2
        azimuth_fov: Default: 110.0
        azimuth_resolution: Default: 1.0
        elevation_fov: Default: 32.0
        elevation_resolution: Default: 2.0
        radar_output_2d: Default: False
        use_random_raycast: Default: True
        number_rays_per_frame: Default: 30000
        azimuth_accuracy: Default: 0.5
        elevation_accuracy: Default: 1.0
        prf_profile_file:"""

    _proto_message = pd_sensor_pb2.RadarBasicParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.RadarBasicParameters] = None,
        max_range: float = None,
        range_resolution: float = None,
        max_doppler: float = None,
        doppler_resolution: float = None,
        azimuth_fov: float = None,
        azimuth_resolution: float = None,
        elevation_fov: float = None,
        elevation_resolution: float = None,
        radar_output_2d: bool = None,
        use_random_raycast: bool = None,
        number_rays_per_frame: int = None,
        azimuth_accuracy: float = None,
        elevation_accuracy: float = None,
        prf_profile_file: str = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.RadarBasicParameters()
        self.proto = proto
        if max_range is not None:
            self.max_range = max_range
        if range_resolution is not None:
            self.range_resolution = range_resolution
        if max_doppler is not None:
            self.max_doppler = max_doppler
        if doppler_resolution is not None:
            self.doppler_resolution = doppler_resolution
        if azimuth_fov is not None:
            self.azimuth_fov = azimuth_fov
        if azimuth_resolution is not None:
            self.azimuth_resolution = azimuth_resolution
        if elevation_fov is not None:
            self.elevation_fov = elevation_fov
        if elevation_resolution is not None:
            self.elevation_resolution = elevation_resolution
        if radar_output_2d is not None:
            self.radar_output_2d = radar_output_2d
        if use_random_raycast is not None:
            self.use_random_raycast = use_random_raycast
        if number_rays_per_frame is not None:
            self.number_rays_per_frame = number_rays_per_frame
        if azimuth_accuracy is not None:
            self.azimuth_accuracy = azimuth_accuracy
        if elevation_accuracy is not None:
            self.elevation_accuracy = elevation_accuracy
        if prf_profile_file is not None:
            self.prf_profile_file = prf_profile_file

    @property
    def max_range(self) -> float:
        return self.proto.max_range

    @max_range.setter
    def max_range(self, value: float):
        self.proto.max_range = value

    @property
    def range_resolution(self) -> float:
        return self.proto.range_resolution

    @range_resolution.setter
    def range_resolution(self, value: float):
        self.proto.range_resolution = value

    @property
    def max_doppler(self) -> float:
        return self.proto.max_doppler

    @max_doppler.setter
    def max_doppler(self, value: float):
        self.proto.max_doppler = value

    @property
    def doppler_resolution(self) -> float:
        return self.proto.doppler_resolution

    @doppler_resolution.setter
    def doppler_resolution(self, value: float):
        self.proto.doppler_resolution = value

    @property
    def azimuth_fov(self) -> float:
        return self.proto.azimuth_fov

    @azimuth_fov.setter
    def azimuth_fov(self, value: float):
        self.proto.azimuth_fov = value

    @property
    def azimuth_resolution(self) -> float:
        return self.proto.azimuth_resolution

    @azimuth_resolution.setter
    def azimuth_resolution(self, value: float):
        self.proto.azimuth_resolution = value

    @property
    def elevation_fov(self) -> float:
        return self.proto.elevation_fov

    @elevation_fov.setter
    def elevation_fov(self, value: float):
        self.proto.elevation_fov = value

    @property
    def elevation_resolution(self) -> float:
        return self.proto.elevation_resolution

    @elevation_resolution.setter
    def elevation_resolution(self, value: float):
        self.proto.elevation_resolution = value

    @property
    def radar_output_2d(self) -> bool:
        return self.proto.radar_output_2d

    @radar_output_2d.setter
    def radar_output_2d(self, value: bool):
        self.proto.radar_output_2d = value

    @property
    def use_random_raycast(self) -> bool:
        return self.proto.use_random_raycast

    @use_random_raycast.setter
    def use_random_raycast(self, value: bool):
        self.proto.use_random_raycast = value

    @property
    def number_rays_per_frame(self) -> int:
        return self.proto.number_rays_per_frame

    @number_rays_per_frame.setter
    def number_rays_per_frame(self, value: int):
        self.proto.number_rays_per_frame = value

    @property
    def azimuth_accuracy(self) -> float:
        return self.proto.azimuth_accuracy

    @azimuth_accuracy.setter
    def azimuth_accuracy(self, value: float):
        self.proto.azimuth_accuracy = value

    @property
    def elevation_accuracy(self) -> float:
        return self.proto.elevation_accuracy

    @elevation_accuracy.setter
    def elevation_accuracy(self, value: float):
        self.proto.elevation_accuracy = value

    @property
    def prf_profile_file(self) -> str:
        return self.proto.prf_profile_file

    @prf_profile_file.setter
    def prf_profile_file(self, value: str):
        self.proto.prf_profile_file = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarBasicParameters):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.RadarEnergyParameters)
class RadarEnergyParameters(ProtoMessageClass):
    """
    Args:
        nominal_gain: :attr:`nominal_gain`
        gain_jitter_std: :attr:`gain_jitter_std`
        radiometric_coefficient: :attr:`radiometric_coefficient`
        beam_pattern_file_path: :attr:`beam_pattern_file_path`
        enable_beam_pattern: :attr:`enable_beam_pattern`
    Attributes:
        nominal_gain: Default: 120.0
        gain_jitter_std: Default: 5.0
        radiometric_coefficient: Default: 4.0
        beam_pattern_file_path: Default: ../tools/beam_pattern_77ghz_radians.csv
        enable_beam_pattern: Default: True"""

    _proto_message = pd_sensor_pb2.RadarEnergyParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.RadarEnergyParameters] = None,
        nominal_gain: float = None,
        gain_jitter_std: float = None,
        radiometric_coefficient: float = None,
        beam_pattern_file_path: str = None,
        enable_beam_pattern: bool = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.RadarEnergyParameters()
        self.proto = proto
        if nominal_gain is not None:
            self.nominal_gain = nominal_gain
        if gain_jitter_std is not None:
            self.gain_jitter_std = gain_jitter_std
        if radiometric_coefficient is not None:
            self.radiometric_coefficient = radiometric_coefficient
        if beam_pattern_file_path is not None:
            self.beam_pattern_file_path = beam_pattern_file_path
        if enable_beam_pattern is not None:
            self.enable_beam_pattern = enable_beam_pattern

    @property
    def nominal_gain(self) -> float:
        return self.proto.nominal_gain

    @nominal_gain.setter
    def nominal_gain(self, value: float):
        self.proto.nominal_gain = value

    @property
    def gain_jitter_std(self) -> float:
        return self.proto.gain_jitter_std

    @gain_jitter_std.setter
    def gain_jitter_std(self, value: float):
        self.proto.gain_jitter_std = value

    @property
    def radiometric_coefficient(self) -> float:
        return self.proto.radiometric_coefficient

    @radiometric_coefficient.setter
    def radiometric_coefficient(self, value: float):
        self.proto.radiometric_coefficient = value

    @property
    def beam_pattern_file_path(self) -> str:
        return self.proto.beam_pattern_file_path

    @beam_pattern_file_path.setter
    def beam_pattern_file_path(self, value: str):
        self.proto.beam_pattern_file_path = value

    @property
    def enable_beam_pattern(self) -> bool:
        return self.proto.enable_beam_pattern

    @enable_beam_pattern.setter
    def enable_beam_pattern(self, value: bool):
        self.proto.enable_beam_pattern = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarEnergyParameters):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.RadarNoiseParameters)
class RadarNoiseParameters(ProtoMessageClass):
    """
    Args:
        enable_thermal_noise: :attr:`enable_thermal_noise`
        thermal_noise_std: :attr:`thermal_noise_std`
        thermal_noise_mean: :attr:`thermal_noise_mean`
        enable_doa_noise: :attr:`enable_doa_noise`
    Attributes:
        enable_thermal_noise: Default: True
        thermal_noise_std: Default: 3.0
        thermal_noise_mean: Default: 15.0
        enable_doa_noise: Default: True"""

    _proto_message = pd_sensor_pb2.RadarNoiseParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.RadarNoiseParameters] = None,
        enable_thermal_noise: bool = None,
        thermal_noise_std: float = None,
        thermal_noise_mean: float = None,
        enable_doa_noise: bool = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.RadarNoiseParameters()
        self.proto = proto
        if enable_thermal_noise is not None:
            self.enable_thermal_noise = enable_thermal_noise
        if thermal_noise_std is not None:
            self.thermal_noise_std = thermal_noise_std
        if thermal_noise_mean is not None:
            self.thermal_noise_mean = thermal_noise_mean
        if enable_doa_noise is not None:
            self.enable_doa_noise = enable_doa_noise

    @property
    def enable_thermal_noise(self) -> bool:
        return self.proto.enable_thermal_noise

    @enable_thermal_noise.setter
    def enable_thermal_noise(self, value: bool):
        self.proto.enable_thermal_noise = value

    @property
    def thermal_noise_std(self) -> float:
        return self.proto.thermal_noise_std

    @thermal_noise_std.setter
    def thermal_noise_std(self, value: float):
        self.proto.thermal_noise_std = value

    @property
    def thermal_noise_mean(self) -> float:
        return self.proto.thermal_noise_mean

    @thermal_noise_mean.setter
    def thermal_noise_mean(self, value: float):
        self.proto.thermal_noise_mean = value

    @property
    def enable_doa_noise(self) -> bool:
        return self.proto.enable_doa_noise

    @enable_doa_noise.setter
    def enable_doa_noise(self, value: bool):
        self.proto.enable_doa_noise = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarNoiseParameters):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.RadarDetectorParameters)
class RadarDetectorParameters(ProtoMessageClass):
    """
    Args:
        detector_type: :attr:`detector_type`
        detector_constant_gain: :attr:`detector_constant_gain`
        detector_radiometric_gain: :attr:`detector_radiometric_gain`
        detector_radiometric_decay: :attr:`detector_radiometric_decay`
        enable_cfar: :attr:`enable_cfar`
        cfar_type: :attr:`cfar_type`
        cfar_guard_cell: :attr:`cfar_guard_cell`
        cfar_neighbor_cell: :attr:`cfar_neighbor_cell`
        cfar_threshold_scale: :attr:`cfar_threshold_scale`
    Attributes:
        detector_type: Default: CONSTANT_DETECTOR
        detector_constant_gain: Default: 30.0
        detector_radiometric_gain: Default: 100.0
        detector_radiometric_decay: Default: 4.0
        enable_cfar: Default: False
        cfar_type: Default: CACFAR
        cfar_guard_cell: Default: 2
        cfar_neighbor_cell: Default: 5
        cfar_threshold_scale: Default: 0.5"""

    _proto_message = pd_sensor_pb2.RadarDetectorParameters

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.RadarDetectorParameters] = None,
        detector_type: str = None,
        detector_constant_gain: float = None,
        detector_radiometric_gain: float = None,
        detector_radiometric_decay: float = None,
        enable_cfar: bool = None,
        cfar_type: str = None,
        cfar_guard_cell: int = None,
        cfar_neighbor_cell: int = None,
        cfar_threshold_scale: float = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.RadarDetectorParameters()
        self.proto = proto
        if detector_type is not None:
            self.detector_type = detector_type
        if detector_constant_gain is not None:
            self.detector_constant_gain = detector_constant_gain
        if detector_radiometric_gain is not None:
            self.detector_radiometric_gain = detector_radiometric_gain
        if detector_radiometric_decay is not None:
            self.detector_radiometric_decay = detector_radiometric_decay
        if enable_cfar is not None:
            self.enable_cfar = enable_cfar
        if cfar_type is not None:
            self.cfar_type = cfar_type
        if cfar_guard_cell is not None:
            self.cfar_guard_cell = cfar_guard_cell
        if cfar_neighbor_cell is not None:
            self.cfar_neighbor_cell = cfar_neighbor_cell
        if cfar_threshold_scale is not None:
            self.cfar_threshold_scale = cfar_threshold_scale

    @property
    def detector_type(self) -> str:
        return self.proto.detector_type

    @detector_type.setter
    def detector_type(self, value: str):
        self.proto.detector_type = value

    @property
    def detector_constant_gain(self) -> float:
        return self.proto.detector_constant_gain

    @detector_constant_gain.setter
    def detector_constant_gain(self, value: float):
        self.proto.detector_constant_gain = value

    @property
    def detector_radiometric_gain(self) -> float:
        return self.proto.detector_radiometric_gain

    @detector_radiometric_gain.setter
    def detector_radiometric_gain(self, value: float):
        self.proto.detector_radiometric_gain = value

    @property
    def detector_radiometric_decay(self) -> float:
        return self.proto.detector_radiometric_decay

    @detector_radiometric_decay.setter
    def detector_radiometric_decay(self, value: float):
        self.proto.detector_radiometric_decay = value

    @property
    def enable_cfar(self) -> bool:
        return self.proto.enable_cfar

    @enable_cfar.setter
    def enable_cfar(self, value: bool):
        self.proto.enable_cfar = value

    @property
    def cfar_type(self) -> str:
        return self.proto.cfar_type

    @cfar_type.setter
    def cfar_type(self, value: str):
        self.proto.cfar_type = value

    @property
    def cfar_guard_cell(self) -> int:
        return self.proto.cfar_guard_cell

    @cfar_guard_cell.setter
    def cfar_guard_cell(self, value: int):
        self.proto.cfar_guard_cell = value

    @property
    def cfar_neighbor_cell(self) -> int:
        return self.proto.cfar_neighbor_cell

    @cfar_neighbor_cell.setter
    def cfar_neighbor_cell(self, value: int):
        self.proto.cfar_neighbor_cell = value

    @property
    def cfar_threshold_scale(self) -> float:
        return self.proto.cfar_threshold_scale

    @cfar_threshold_scale.setter
    def cfar_threshold_scale(self, value: float):
        self.proto.cfar_threshold_scale = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarDetectorParameters):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.RadarIntrinsic)
class RadarIntrinsic(ProtoMessageClass):
    """
    Args:
        basic_parameters: :attr:`basic_parameters`
        energy_parameters: :attr:`energy_parameters`
        noise_parameters: :attr:`noise_parameters`
        detector_parameters: :attr:`detector_parameters`
    Attributes:
        basic_parameters:
        energy_parameters:
        noise_parameters:
        detector_parameters:"""

    _proto_message = pd_sensor_pb2.RadarIntrinsic

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.RadarIntrinsic] = None,
        basic_parameters: RadarBasicParameters = None,
        energy_parameters: RadarEnergyParameters = None,
        noise_parameters: RadarNoiseParameters = None,
        detector_parameters: RadarDetectorParameters = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.RadarIntrinsic()
        self.proto = proto
        self._basic_parameters = get_wrapper(proto_type=proto.basic_parameters.__class__)(proto=proto.basic_parameters)
        self._energy_parameters = get_wrapper(proto_type=proto.energy_parameters.__class__)(
            proto=proto.energy_parameters
        )
        self._noise_parameters = get_wrapper(proto_type=proto.noise_parameters.__class__)(proto=proto.noise_parameters)
        self._detector_parameters = get_wrapper(proto_type=proto.detector_parameters.__class__)(
            proto=proto.detector_parameters
        )
        if basic_parameters is not None:
            self.basic_parameters = basic_parameters
        if energy_parameters is not None:
            self.energy_parameters = energy_parameters
        if noise_parameters is not None:
            self.noise_parameters = noise_parameters
        if detector_parameters is not None:
            self.detector_parameters = detector_parameters

    @property
    def basic_parameters(self) -> RadarBasicParameters:
        return self._basic_parameters

    @basic_parameters.setter
    def basic_parameters(self, value: RadarBasicParameters):
        self.proto.basic_parameters.CopyFrom(value.proto)

        self._basic_parameters = value
        self._basic_parameters._update_proto_references(self.proto.basic_parameters)

    @property
    def energy_parameters(self) -> RadarEnergyParameters:
        return self._energy_parameters

    @energy_parameters.setter
    def energy_parameters(self, value: RadarEnergyParameters):
        self.proto.energy_parameters.CopyFrom(value.proto)

        self._energy_parameters = value
        self._energy_parameters._update_proto_references(self.proto.energy_parameters)

    @property
    def noise_parameters(self) -> RadarNoiseParameters:
        return self._noise_parameters

    @noise_parameters.setter
    def noise_parameters(self, value: RadarNoiseParameters):
        self.proto.noise_parameters.CopyFrom(value.proto)

        self._noise_parameters = value
        self._noise_parameters._update_proto_references(self.proto.noise_parameters)

    @property
    def detector_parameters(self) -> RadarDetectorParameters:
        return self._detector_parameters

    @detector_parameters.setter
    def detector_parameters(self, value: RadarDetectorParameters):
        self.proto.detector_parameters.CopyFrom(value.proto)

        self._detector_parameters = value
        self._detector_parameters._update_proto_references(self.proto.detector_parameters)

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarIntrinsic):
        self.proto = proto
        self._basic_parameters._update_proto_references(proto.basic_parameters)
        self._energy_parameters._update_proto_references(proto.energy_parameters)
        self._noise_parameters._update_proto_references(proto.noise_parameters)
        self._detector_parameters._update_proto_references(proto.detector_parameters)


@register_wrapper(proto_type=pd_sensor_pb2.SensorExtrinsic)
class SensorExtrinsic(ProtoMessageClass):
    """
    Object to store extrinsic parameters of sensors. All extrinsics are stored in the RFU coordinate system relative to
    the agent to which the sensor is attached.

    Args:
        yaw: :attr:`yaw`
        pitch: :attr:`pitch`
        roll: :attr:`roll`
        x: :attr:`x`
        y: :attr:`y`
        z: :attr:`z`
        lock_to_yaw: :attr:`lock_to_yaw`
        attach_socket: :attr:`attach_socket`
        follow_rotation: :attr:`follow_rotation`
    Attributes:
        yaw: Yaw of the sensor in degrees.
        pitch: Pitch of the sensor in degrees.
        roll: Roll of the sensor in degrees.
        x: `x` position of the sensor in meters.
        y: `y` position of the sensor in meters.
        z: `z` position of the sensor in meters.
        lock_to_yaw: Setting this flag to true will cause the yaw value of the sensor orientation to be locked to the agent to which the
            sensor is attached, but leave the pitch and roll values as zero with respect to the world frame.
        attach_socket: Controls the socket on the agent to which the sensor should be attached.
        follow_rotation: Controls whether or not the sensor follows the rotation of the socket to which it is attached if
            :attr:`attach_socket` is `True`."""

    _proto_message = pd_sensor_pb2.SensorExtrinsic

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.SensorExtrinsic] = None,
        yaw: float = None,
        pitch: float = None,
        roll: float = None,
        x: float = None,
        y: float = None,
        z: float = None,
        lock_to_yaw: bool = None,
        attach_socket: str = None,
        follow_rotation: bool = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.SensorExtrinsic()
        self.proto = proto
        if yaw is not None:
            self.yaw = yaw
        if pitch is not None:
            self.pitch = pitch
        if roll is not None:
            self.roll = roll
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
        if lock_to_yaw is not None:
            self.lock_to_yaw = lock_to_yaw
        if attach_socket is not None:
            self.attach_socket = attach_socket
        if follow_rotation is not None:
            self.follow_rotation = follow_rotation

    @property
    def yaw(self) -> float:
        return self.proto.yaw

    @yaw.setter
    def yaw(self, value: float):
        self.proto.yaw = value

    @property
    def pitch(self) -> float:
        return self.proto.pitch

    @pitch.setter
    def pitch(self, value: float):
        self.proto.pitch = value

    @property
    def roll(self) -> float:
        return self.proto.roll

    @roll.setter
    def roll(self, value: float):
        self.proto.roll = value

    @property
    def x(self) -> float:
        return self.proto.x

    @x.setter
    def x(self, value: float):
        self.proto.x = value

    @property
    def y(self) -> float:
        return self.proto.y

    @y.setter
    def y(self, value: float):
        self.proto.y = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    @property
    def lock_to_yaw(self) -> bool:
        return self.proto.lock_to_yaw

    @lock_to_yaw.setter
    def lock_to_yaw(self, value: bool):
        self.proto.lock_to_yaw = value

    @property
    def attach_socket(self) -> str:
        return self.proto.attach_socket

    @attach_socket.setter
    def attach_socket(self, value: str):
        self.proto.attach_socket = value

    @property
    def follow_rotation(self) -> bool:
        return self.proto.follow_rotation

    @follow_rotation.setter
    def follow_rotation(self, value: bool):
        self.proto.follow_rotation = value

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorExtrinsic):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.SensorConfig)
class SensorConfig(ProtoMessageClass):
    """
    A configuration of one sensor.

    Args:
        display_name: :attr:`display_name`
        camera_intrinsic: :attr:`camera_intrinsic`
        lidar_intrinsic: :attr:`lidar_intrinsic`
        radar_intrinsic: :attr:`radar_intrinsic`
        sensor_extrinsic: :attr:`sensor_extrinsic`
    Attributes:
        display_name: The name of the sensor.
        camera_intrinsic: Instrinsics of a camera sensor.
        lidar_intrinsic: Instrinsics of a lidar sensor.
        radar_intrinsic: Instrinsics of a radar sensor.
        sensor_extrinsic: The extrinsics of the sensor."""

    _proto_message = pd_sensor_pb2.SensorConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.SensorConfig] = None,
        display_name: str = None,
        camera_intrinsic: CameraIntrinsic = None,
        lidar_intrinsic: LidarIntrinsic = None,
        radar_intrinsic: RadarIntrinsic = None,
        sensor_extrinsic: SensorExtrinsic = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.SensorConfig()
        self.proto = proto
        self._camera_intrinsic = get_wrapper(proto_type=proto.camera_intrinsic.__class__)(proto=proto.camera_intrinsic)
        self._lidar_intrinsic = get_wrapper(proto_type=proto.lidar_intrinsic.__class__)(proto=proto.lidar_intrinsic)
        self._radar_intrinsic = get_wrapper(proto_type=proto.radar_intrinsic.__class__)(proto=proto.radar_intrinsic)
        self._sensor_extrinsic = get_wrapper(proto_type=proto.sensor_extrinsic.__class__)(proto=proto.sensor_extrinsic)
        if display_name is not None:
            self.display_name = display_name
        if camera_intrinsic is not None:
            self.camera_intrinsic = camera_intrinsic
        if lidar_intrinsic is not None:
            self.lidar_intrinsic = lidar_intrinsic
        if radar_intrinsic is not None:
            self.radar_intrinsic = radar_intrinsic
        if sensor_extrinsic is not None:
            self.sensor_extrinsic = sensor_extrinsic

    @property
    def display_name(self) -> str:
        return self.proto.display_name

    @display_name.setter
    def display_name(self, value: str):
        self.proto.display_name = value

    @property
    def camera_intrinsic(self) -> CameraIntrinsic:
        return self._camera_intrinsic

    @camera_intrinsic.setter
    def camera_intrinsic(self, value: CameraIntrinsic):
        self.proto.camera_intrinsic.CopyFrom(value.proto)

        self._camera_intrinsic = value
        self._camera_intrinsic._update_proto_references(self.proto.camera_intrinsic)

    @property
    def lidar_intrinsic(self) -> LidarIntrinsic:
        return self._lidar_intrinsic

    @lidar_intrinsic.setter
    def lidar_intrinsic(self, value: LidarIntrinsic):
        self.proto.lidar_intrinsic.CopyFrom(value.proto)

        self._lidar_intrinsic = value
        self._lidar_intrinsic._update_proto_references(self.proto.lidar_intrinsic)

    @property
    def radar_intrinsic(self) -> RadarIntrinsic:
        return self._radar_intrinsic

    @radar_intrinsic.setter
    def radar_intrinsic(self, value: RadarIntrinsic):
        self.proto.radar_intrinsic.CopyFrom(value.proto)

        self._radar_intrinsic = value
        self._radar_intrinsic._update_proto_references(self.proto.radar_intrinsic)

    @property
    def sensor_extrinsic(self) -> SensorExtrinsic:
        return self._sensor_extrinsic

    @sensor_extrinsic.setter
    def sensor_extrinsic(self, value: SensorExtrinsic):
        self.proto.sensor_extrinsic.CopyFrom(value.proto)

        self._sensor_extrinsic = value
        self._sensor_extrinsic._update_proto_references(self.proto.sensor_extrinsic)

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorConfig):
        self.proto = proto
        self._camera_intrinsic._update_proto_references(proto.camera_intrinsic)
        self._lidar_intrinsic._update_proto_references(proto.lidar_intrinsic)
        self._radar_intrinsic._update_proto_references(proto.radar_intrinsic)
        self._sensor_extrinsic._update_proto_references(proto.sensor_extrinsic)


@register_wrapper(proto_type=pd_sensor_pb2.SensorList)
class SensorList(ProtoMessageClass):
    """
    A list of sensors.

    Args:
        sensors: :attr:`sensors`
    Attributes:
        sensors:"""

    _proto_message = pd_sensor_pb2.SensorList

    def __init__(self, *, proto: Optional[pd_sensor_pb2.SensorList] = None, sensors: List[str] = None):
        if proto is None:
            proto = pd_sensor_pb2.SensorList()
        self.proto = proto
        self._sensors = ProtoListWrapper(
            container=[str(v) for v in proto.sensors], attr_name="sensors", list_owner=self
        )
        if sensors is not None:
            self.sensors = sensors

    @property
    def sensors(self) -> List[str]:
        return self._sensors

    @sensors.setter
    def sensors(self, value: List[str]):
        self._sensors.clear()
        for v in value:
            self._sensors.append(v)

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorList):
        self.proto = proto


@register_wrapper(proto_type=pd_sensor_pb2.SensorRigConfig)
class SensorRigConfig(ProtoMessageClass):
    """
    A configuration of a rig of sensors containing one or more sensors.

    Args:
        sensor_configs: :attr:`sensor_configs`
        sensor_rig_artifact_uid: :attr:`sensor_rig_artifact_uid`
        default_sensor_splits_list: :attr:`default_sensor_splits_list`
    Attributes:
        sensor_configs: The configuration of sensors within a particular sensor rig.
        sensor_rig_artifact_uid: The s3 path to a sensor rig if it is not stored locally.
        default_sensor_splits_list: A list of sensor names to control which sensors are rendered in parallel."""

    _proto_message = pd_sensor_pb2.SensorRigConfig

    def __init__(
        self,
        *,
        proto: Optional[pd_sensor_pb2.SensorRigConfig] = None,
        sensor_configs: List[SensorConfig] = None,
        sensor_rig_artifact_uid: str = None,
        default_sensor_splits_list: List[SensorList] = None,
    ):
        if proto is None:
            proto = pd_sensor_pb2.SensorRigConfig()
        self.proto = proto
        self._sensor_configs = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensor_configs],
            attr_name="sensor_configs",
            list_owner=self,
        )
        self._default_sensor_splits_list = ProtoListWrapper(
            container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.default_sensor_splits_list],
            attr_name="default_sensor_splits_list",
            list_owner=self,
        )
        if sensor_configs is not None:
            self.sensor_configs = sensor_configs
        if sensor_rig_artifact_uid is not None:
            self.sensor_rig_artifact_uid = sensor_rig_artifact_uid
        if default_sensor_splits_list is not None:
            self.default_sensor_splits_list = default_sensor_splits_list

    @property
    def sensor_configs(self) -> List[SensorConfig]:
        return self._sensor_configs

    @sensor_configs.setter
    def sensor_configs(self, value: List[SensorConfig]):
        self._sensor_configs.clear()
        for v in value:
            self._sensor_configs.append(v)

    @property
    def sensor_rig_artifact_uid(self) -> str:
        return self.proto.sensor_rig_artifact_uid

    @sensor_rig_artifact_uid.setter
    def sensor_rig_artifact_uid(self, value: str):
        self.proto.sensor_rig_artifact_uid = value

    @property
    def default_sensor_splits_list(self) -> List[SensorList]:
        return self._default_sensor_splits_list

    @default_sensor_splits_list.setter
    def default_sensor_splits_list(self, value: List[SensorList]):
        self._default_sensor_splits_list.clear()
        for v in value:
            self._default_sensor_splits_list.append(v)

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorRigConfig):
        self.proto = proto
        for i, v in enumerate(self.sensor_configs):
            v._update_proto_references(self.proto.sensor_configs[i])
        for i, v in enumerate(self.default_sensor_splits_list):
            v._update_proto_references(self.proto.default_sensor_splits_list[i])
