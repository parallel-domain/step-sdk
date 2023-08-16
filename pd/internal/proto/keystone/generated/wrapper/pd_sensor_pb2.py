from __future__ import annotations
from typing import List, Dict, Optional, Union
from pd.internal.proto.keystone.generated.python import pd_sensor_pb2
from pd.internal.proto.keystone.generated.wrapper.utils import WRAPPER_REGISTRY, register_wrapper, get_wrapper, ProtoMessageClass, ProtoEnumClass, AtomicGeneratorMessage, ProtoListWrapper, ProtoDictWrapper
from pd.internal.proto.keystone.generated.wrapper import pd_distributions_pb2 as _pd_distributions_pb2, pd_environments_pb2 as _pd_environments_pb2, pd_keystone_pb2 as _pd_keystone_pb2, pd_levelcook_pb2 as _pd_levelcook_pb2, pd_package_maps_from_p4_pb2 as _pd_package_maps_from_p4_pb2, pd_post_process_pb2 as _pd_post_process_pb2, pd_recook_pb2 as _pd_recook_pb2, pd_render_pb2 as _pd_render_pb2, pd_scenario_pb2 as _pd_scenario_pb2, pd_sensor_pb2 as _pd_sensor_pb2, pd_sim_state_pb2 as _pd_sim_state_pb2, pd_source_maps_pb2 as _pd_source_maps_pb2, pd_spawn_pb2 as _pd_spawn_pb2, pd_types_pb2 as _pd_types_pb2, pd_unified_generator_pb2 as _pd_unified_generator_pb2, pd_world_cook_from_p4_pb2 as _pd_world_cook_from_p4_pb2, pd_worldbuild_pb2 as _pd_worldbuild_pb2, pd_worldgen_pb2 as _pd_worldgen_pb2

@register_wrapper(proto_type=pd_sensor_pb2.AlbedoWeights)
class AlbedoWeights(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.AlbedoWeights

    def __init__(self, *, proto: Optional[pd_sensor_pb2.AlbedoWeights]=None, x: Optional[float]=None, y: Optional[float]=None, z: Optional[float]=None):
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

@register_wrapper(proto_type=pd_sensor_pb2.AliceLidarModel)
class AliceLidarModel(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.AliceLidarModel

    def __init__(self, *, proto: Optional[pd_sensor_pb2.AliceLidarModel]=None, dense_radian_spacing: Optional[float]=None, horizontal_spacing: Optional[float]=None, max_azimuth_angle: Optional[float]=None, max_dense_elevation_angle: Optional[float]=None, max_elevation_angle: Optional[float]=None, min_azimuth_angle: Optional[float]=None, min_dense_elevation_angle: Optional[float]=None, min_elevation_angle: Optional[float]=None, number_points: Optional[int]=None, sparse_radian_spacing: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.AliceLidarModel()
        self.proto = proto
        if dense_radian_spacing is not None:
            self.dense_radian_spacing = dense_radian_spacing
        if horizontal_spacing is not None:
            self.horizontal_spacing = horizontal_spacing
        if max_azimuth_angle is not None:
            self.max_azimuth_angle = max_azimuth_angle
        if max_dense_elevation_angle is not None:
            self.max_dense_elevation_angle = max_dense_elevation_angle
        if max_elevation_angle is not None:
            self.max_elevation_angle = max_elevation_angle
        if min_azimuth_angle is not None:
            self.min_azimuth_angle = min_azimuth_angle
        if min_dense_elevation_angle is not None:
            self.min_dense_elevation_angle = min_dense_elevation_angle
        if min_elevation_angle is not None:
            self.min_elevation_angle = min_elevation_angle
        if number_points is not None:
            self.number_points = number_points
        if sparse_radian_spacing is not None:
            self.sparse_radian_spacing = sparse_radian_spacing

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

    @property
    def max_azimuth_angle(self) -> float:
        return self.proto.max_azimuth_angle

    @max_azimuth_angle.setter
    def max_azimuth_angle(self, value: float):
        self.proto.max_azimuth_angle = value

    @property
    def max_dense_elevation_angle(self) -> float:
        return self.proto.max_dense_elevation_angle

    @max_dense_elevation_angle.setter
    def max_dense_elevation_angle(self, value: float):
        self.proto.max_dense_elevation_angle = value

    @property
    def max_elevation_angle(self) -> float:
        return self.proto.max_elevation_angle

    @max_elevation_angle.setter
    def max_elevation_angle(self, value: float):
        self.proto.max_elevation_angle = value

    @property
    def min_azimuth_angle(self) -> float:
        return self.proto.min_azimuth_angle

    @min_azimuth_angle.setter
    def min_azimuth_angle(self, value: float):
        self.proto.min_azimuth_angle = value

    @property
    def min_dense_elevation_angle(self) -> float:
        return self.proto.min_dense_elevation_angle

    @min_dense_elevation_angle.setter
    def min_dense_elevation_angle(self, value: float):
        self.proto.min_dense_elevation_angle = value

    @property
    def min_elevation_angle(self) -> float:
        return self.proto.min_elevation_angle

    @min_elevation_angle.setter
    def min_elevation_angle(self, value: float):
        self.proto.min_elevation_angle = value

    @property
    def number_points(self) -> int:
        return self.proto.number_points

    @number_points.setter
    def number_points(self, value: int):
        self.proto.number_points = value

    @property
    def sparse_radian_spacing(self) -> float:
        return self.proto.sparse_radian_spacing

    @sparse_radian_spacing.setter
    def sparse_radian_spacing(self, value: float):
        self.proto.sparse_radian_spacing = value

    def _update_proto_references(self, proto: pd_sensor_pb2.AliceLidarModel):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.CameraIntrinsic)
class CameraIntrinsic(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.CameraIntrinsic

    def __init__(self, *, proto: Optional[pd_sensor_pb2.CameraIntrinsic]=None, capture_backwardmotionvectors: Optional[bool]=None, capture_basecolor: Optional[bool]=None, capture_depth: Optional[bool]=None, capture_detections: Optional[bool]=None, capture_instance: Optional[bool]=None, capture_motionvectors: Optional[bool]=None, capture_normals: Optional[bool]=None, capture_properties: Optional[bool]=None, capture_rgb: Optional[bool]=None, capture_segmentation: Optional[bool]=None, distortion_lookup_table: Optional[str]=None, distortion_params: Optional[DistortionParams]=None, enable_streaming: Optional[bool]=None, fov: Optional[float]=None, height: Optional[int]=None, lut: Optional[str]=None, lut_weight: Optional[float]=None, noise_params: Optional[NoiseParams]=None, post_process: Optional[List[PostProcessNode]]=None, post_process_params: Optional[PostProcessParams]=None, supersample: Optional[float]=None, time_offset: Optional[float]=None, transmit_gray: Optional[bool]=None, width: Optional[int]=None):
        if proto is None:
            proto = pd_sensor_pb2.CameraIntrinsic()
        self.proto = proto
        self._distortion_params = get_wrapper(proto_type=proto.distortion_params.__class__)(proto=proto.distortion_params)
        self._noise_params = get_wrapper(proto_type=proto.noise_params.__class__)(proto=proto.noise_params)
        self._post_process = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.post_process], attr_name='post_process', list_owner=self)
        self._post_process_params = get_wrapper(proto_type=proto.post_process_params.__class__)(proto=proto.post_process_params)
        if capture_backwardmotionvectors is not None:
            self.capture_backwardmotionvectors = capture_backwardmotionvectors
        if capture_basecolor is not None:
            self.capture_basecolor = capture_basecolor
        if capture_depth is not None:
            self.capture_depth = capture_depth
        if capture_detections is not None:
            self.capture_detections = capture_detections
        if capture_instance is not None:
            self.capture_instance = capture_instance
        if capture_motionvectors is not None:
            self.capture_motionvectors = capture_motionvectors
        if capture_normals is not None:
            self.capture_normals = capture_normals
        if capture_properties is not None:
            self.capture_properties = capture_properties
        if capture_rgb is not None:
            self.capture_rgb = capture_rgb
        if capture_segmentation is not None:
            self.capture_segmentation = capture_segmentation
        if distortion_lookup_table is not None:
            self.distortion_lookup_table = distortion_lookup_table
        if distortion_params is not None:
            self.distortion_params = distortion_params
        if enable_streaming is not None:
            self.enable_streaming = enable_streaming
        if fov is not None:
            self.fov = fov
        if height is not None:
            self.height = height
        if lut is not None:
            self.lut = lut
        if lut_weight is not None:
            self.lut_weight = lut_weight
        if noise_params is not None:
            self.noise_params = noise_params
        if post_process is not None:
            self.post_process = post_process
        if post_process_params is not None:
            self.post_process_params = post_process_params
        if supersample is not None:
            self.supersample = supersample
        if time_offset is not None:
            self.time_offset = time_offset
        if transmit_gray is not None:
            self.transmit_gray = transmit_gray
        if width is not None:
            self.width = width

    @property
    def capture_backwardmotionvectors(self) -> bool:
        return self.proto.capture_backwardmotionvectors

    @capture_backwardmotionvectors.setter
    def capture_backwardmotionvectors(self, value: bool):
        self.proto.capture_backwardmotionvectors = value

    @property
    def capture_basecolor(self) -> bool:
        return self.proto.capture_basecolor

    @capture_basecolor.setter
    def capture_basecolor(self, value: bool):
        self.proto.capture_basecolor = value

    @property
    def capture_depth(self) -> bool:
        return self.proto.capture_depth

    @capture_depth.setter
    def capture_depth(self, value: bool):
        self.proto.capture_depth = value

    @property
    def capture_detections(self) -> bool:
        return self.proto.capture_detections

    @capture_detections.setter
    def capture_detections(self, value: bool):
        self.proto.capture_detections = value

    @property
    def capture_instance(self) -> bool:
        return self.proto.capture_instance

    @capture_instance.setter
    def capture_instance(self, value: bool):
        self.proto.capture_instance = value

    @property
    def capture_motionvectors(self) -> bool:
        return self.proto.capture_motionvectors

    @capture_motionvectors.setter
    def capture_motionvectors(self, value: bool):
        self.proto.capture_motionvectors = value

    @property
    def capture_normals(self) -> bool:
        return self.proto.capture_normals

    @capture_normals.setter
    def capture_normals(self, value: bool):
        self.proto.capture_normals = value

    @property
    def capture_properties(self) -> bool:
        return self.proto.capture_properties

    @capture_properties.setter
    def capture_properties(self, value: bool):
        self.proto.capture_properties = value

    @property
    def capture_rgb(self) -> bool:
        return self.proto.capture_rgb

    @capture_rgb.setter
    def capture_rgb(self, value: bool):
        self.proto.capture_rgb = value

    @property
    def capture_segmentation(self) -> bool:
        return self.proto.capture_segmentation

    @capture_segmentation.setter
    def capture_segmentation(self, value: bool):
        self.proto.capture_segmentation = value

    @property
    def distortion_lookup_table(self) -> str:
        return self.proto.distortion_lookup_table

    @distortion_lookup_table.setter
    def distortion_lookup_table(self, value: str):
        self.proto.distortion_lookup_table = value

    @property
    def distortion_params(self) -> DistortionParams:
        return self._distortion_params

    @distortion_params.setter
    def distortion_params(self, value: DistortionParams):
        self.proto.distortion_params.CopyFrom(value.proto)
        
        self._distortion_params = value
        self._distortion_params._update_proto_references(self.proto.distortion_params)

    @property
    def enable_streaming(self) -> bool:
        return self.proto.enable_streaming

    @enable_streaming.setter
    def enable_streaming(self, value: bool):
        self.proto.enable_streaming = value

    @property
    def fov(self) -> float:
        return self.proto.fov

    @fov.setter
    def fov(self, value: float):
        self.proto.fov = value

    @property
    def height(self) -> int:
        return self.proto.height

    @height.setter
    def height(self, value: int):
        self.proto.height = value

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
    def noise_params(self) -> NoiseParams:
        return self._noise_params

    @noise_params.setter
    def noise_params(self, value: NoiseParams):
        self.proto.noise_params.CopyFrom(value.proto)
        
        self._noise_params = value
        self._noise_params._update_proto_references(self.proto.noise_params)

    @property
    def post_process(self) -> List[PostProcessNode]:
        return self._post_process

    @post_process.setter
    def post_process(self, value: List[PostProcessNode]):
        self._post_process.clear()
        for v in value:
            self._post_process.append(v)

    @property
    def post_process_params(self) -> PostProcessParams:
        return self._post_process_params

    @post_process_params.setter
    def post_process_params(self, value: PostProcessParams):
        self.proto.post_process_params.CopyFrom(value.proto)
        
        self._post_process_params = value
        self._post_process_params._update_proto_references(self.proto.post_process_params)

    @property
    def supersample(self) -> float:
        return self.proto.supersample

    @supersample.setter
    def supersample(self, value: float):
        self.proto.supersample = value

    @property
    def time_offset(self) -> float:
        return self.proto.time_offset

    @time_offset.setter
    def time_offset(self, value: float):
        self.proto.time_offset = value

    @property
    def transmit_gray(self) -> bool:
        return self.proto.transmit_gray

    @transmit_gray.setter
    def transmit_gray(self, value: bool):
        self.proto.transmit_gray = value

    @property
    def width(self) -> int:
        return self.proto.width

    @width.setter
    def width(self, value: int):
        self.proto.width = value

    def _update_proto_references(self, proto: pd_sensor_pb2.CameraIntrinsic):
        self.proto = proto
        self._distortion_params._update_proto_references(proto.distortion_params)
        self._noise_params._update_proto_references(proto.noise_params)
        for i, v in enumerate(self.post_process):
            v._update_proto_references(self.proto.post_process[i])
        self._post_process_params._update_proto_references(proto.post_process_params)

@register_wrapper(proto_type=pd_sensor_pb2.DistortionParams)
class DistortionParams(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.DistortionParams

    def __init__(self, *, proto: Optional[pd_sensor_pb2.DistortionParams]=None, cx: Optional[float]=None, cy: Optional[float]=None, fisheye_model: Optional[int]=None, fx: Optional[float]=None, fy: Optional[float]=None, is_fisheye: Optional[bool]=None, k1: Optional[float]=None, k2: Optional[float]=None, k3: Optional[float]=None, k4: Optional[float]=None, k5: Optional[float]=None, k6: Optional[float]=None, p1: Optional[float]=None, p2: Optional[float]=None, skew: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.DistortionParams()
        self.proto = proto
        if cx is not None:
            self.cx = cx
        if cy is not None:
            self.cy = cy
        if fisheye_model is not None:
            self.fisheye_model = fisheye_model
        if fx is not None:
            self.fx = fx
        if fy is not None:
            self.fy = fy
        if is_fisheye is not None:
            self.is_fisheye = is_fisheye
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
    def is_fisheye(self) -> bool:
        return self.proto.is_fisheye

    @is_fisheye.setter
    def is_fisheye(self, value: bool):
        self.proto.is_fisheye = value

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

    def _update_proto_references(self, proto: pd_sensor_pb2.DistortionParams):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.LidarBeam)
class LidarBeam(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.LidarBeam

    def __init__(self, *, proto: Optional[pd_sensor_pb2.LidarBeam]=None, azimuth: Optional[float]=None, elevation: Optional[float]=None, id: Optional[int]=None):
        if proto is None:
            proto = pd_sensor_pb2.LidarBeam()
        self.proto = proto
        if azimuth is not None:
            self.azimuth = azimuth
        if elevation is not None:
            self.elevation = elevation
        if id is not None:
            self.id = id

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

    @property
    def id(self) -> int:
        return self.proto.id

    @id.setter
    def id(self, value: int):
        self.proto.id = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarBeam):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.LidarIntensityParams)
class LidarIntensityParams(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.LidarIntensityParams

    def __init__(self, *, proto: Optional[pd_sensor_pb2.LidarIntensityParams]=None, albedo_weights: Optional[AlbedoWeights]=None, beam_intensity: Optional[float]=None, emissive_gate: Optional[float]=None, intensity_metallic_scale: Optional[float]=None, intensity_roughness_scale: Optional[float]=None, intensity_specular_scale: Optional[float]=None, max_albedo: Optional[float]=None, max_attenuation_distance: Optional[float]=None, max_emissive_rate: Optional[float]=None, retro_intensity_enhance: Optional[float]=None, retro_range_noise_stddev: Optional[float]=None, retroreflection_noise_mean: Optional[float]=None, retroreflection_noise_stddev: Optional[float]=None, strong_retro_intensity_enhance: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.LidarIntensityParams()
        self.proto = proto
        self._albedo_weights = get_wrapper(proto_type=proto.albedo_weights.__class__)(proto=proto.albedo_weights)
        if albedo_weights is not None:
            self.albedo_weights = albedo_weights
        if beam_intensity is not None:
            self.beam_intensity = beam_intensity
        if emissive_gate is not None:
            self.emissive_gate = emissive_gate
        if intensity_metallic_scale is not None:
            self.intensity_metallic_scale = intensity_metallic_scale
        if intensity_roughness_scale is not None:
            self.intensity_roughness_scale = intensity_roughness_scale
        if intensity_specular_scale is not None:
            self.intensity_specular_scale = intensity_specular_scale
        if max_albedo is not None:
            self.max_albedo = max_albedo
        if max_attenuation_distance is not None:
            self.max_attenuation_distance = max_attenuation_distance
        if max_emissive_rate is not None:
            self.max_emissive_rate = max_emissive_rate
        if retro_intensity_enhance is not None:
            self.retro_intensity_enhance = retro_intensity_enhance
        if retro_range_noise_stddev is not None:
            self.retro_range_noise_stddev = retro_range_noise_stddev
        if retroreflection_noise_mean is not None:
            self.retroreflection_noise_mean = retroreflection_noise_mean
        if retroreflection_noise_stddev is not None:
            self.retroreflection_noise_stddev = retroreflection_noise_stddev
        if strong_retro_intensity_enhance is not None:
            self.strong_retro_intensity_enhance = strong_retro_intensity_enhance

    @property
    def albedo_weights(self) -> AlbedoWeights:
        return self._albedo_weights

    @albedo_weights.setter
    def albedo_weights(self, value: AlbedoWeights):
        self.proto.albedo_weights.CopyFrom(value.proto)
        
        self._albedo_weights = value
        self._albedo_weights._update_proto_references(self.proto.albedo_weights)

    @property
    def beam_intensity(self) -> float:
        return self.proto.beam_intensity

    @beam_intensity.setter
    def beam_intensity(self, value: float):
        self.proto.beam_intensity = value

    @property
    def emissive_gate(self) -> float:
        return self.proto.emissive_gate

    @emissive_gate.setter
    def emissive_gate(self, value: float):
        self.proto.emissive_gate = value

    @property
    def intensity_metallic_scale(self) -> float:
        return self.proto.intensity_metallic_scale

    @intensity_metallic_scale.setter
    def intensity_metallic_scale(self, value: float):
        self.proto.intensity_metallic_scale = value

    @property
    def intensity_roughness_scale(self) -> float:
        return self.proto.intensity_roughness_scale

    @intensity_roughness_scale.setter
    def intensity_roughness_scale(self, value: float):
        self.proto.intensity_roughness_scale = value

    @property
    def intensity_specular_scale(self) -> float:
        return self.proto.intensity_specular_scale

    @intensity_specular_scale.setter
    def intensity_specular_scale(self, value: float):
        self.proto.intensity_specular_scale = value

    @property
    def max_albedo(self) -> float:
        return self.proto.max_albedo

    @max_albedo.setter
    def max_albedo(self, value: float):
        self.proto.max_albedo = value

    @property
    def max_attenuation_distance(self) -> float:
        return self.proto.max_attenuation_distance

    @max_attenuation_distance.setter
    def max_attenuation_distance(self, value: float):
        self.proto.max_attenuation_distance = value

    @property
    def max_emissive_rate(self) -> float:
        return self.proto.max_emissive_rate

    @max_emissive_rate.setter
    def max_emissive_rate(self, value: float):
        self.proto.max_emissive_rate = value

    @property
    def retro_intensity_enhance(self) -> float:
        return self.proto.retro_intensity_enhance

    @retro_intensity_enhance.setter
    def retro_intensity_enhance(self, value: float):
        self.proto.retro_intensity_enhance = value

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
    def strong_retro_intensity_enhance(self) -> float:
        return self.proto.strong_retro_intensity_enhance

    @strong_retro_intensity_enhance.setter
    def strong_retro_intensity_enhance(self, value: float):
        self.proto.strong_retro_intensity_enhance = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarIntensityParams):
        self.proto = proto
        self._albedo_weights._update_proto_references(proto.albedo_weights)

@register_wrapper(proto_type=pd_sensor_pb2.LidarIntrinsic)
class LidarIntrinsic(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.LidarIntrinsic

    def __init__(self, *, proto: Optional[pd_sensor_pb2.LidarIntrinsic]=None, alice_lidar_model: Optional[AliceLidarModel]=None, azimuth_max: Optional[float]=None, azimuth_min: Optional[float]=None, beam_data: Optional[List[LidarBeam]]=None, capture_backwardmotionvectors: Optional[bool]=None, capture_depth: Optional[bool]=None, capture_detections: Optional[bool]=None, capture_instance: Optional[bool]=None, capture_intensity: Optional[bool]=None, capture_motionvectors: Optional[bool]=None, capture_normals: Optional[bool]=None, capture_properties: Optional[bool]=None, capture_rgb: Optional[bool]=None, capture_segmentation: Optional[bool]=None, intensity_params: Optional[LidarIntensityParams]=None, maximum_cutoff_prob: Optional[float]=None, maximum_offset: Optional[float]=None, maximum_range_cutoff: Optional[float]=None, merge_returns: Optional[int]=None, minimum_cutoff_prob: Optional[float]=None, minimum_noise: Optional[float]=None, minimum_offset: Optional[float]=None, minimum_range_cutoff: Optional[float]=None, multi_returns: Optional[int]=None, pattern: Optional[str]=None, range_noise_mean: Optional[float]=None, range_noise_stddev: Optional[float]=None, rotation_rate: Optional[float]=None, sample_rate: Optional[float]=None, time_offset: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.LidarIntrinsic()
        self.proto = proto
        self._alice_lidar_model = get_wrapper(proto_type=proto.alice_lidar_model.__class__)(proto=proto.alice_lidar_model)
        self._beam_data = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.beam_data], attr_name='beam_data', list_owner=self)
        self._intensity_params = get_wrapper(proto_type=proto.intensity_params.__class__)(proto=proto.intensity_params)
        if alice_lidar_model is not None:
            self.alice_lidar_model = alice_lidar_model
        if azimuth_max is not None:
            self.azimuth_max = azimuth_max
        if azimuth_min is not None:
            self.azimuth_min = azimuth_min
        if beam_data is not None:
            self.beam_data = beam_data
        if capture_backwardmotionvectors is not None:
            self.capture_backwardmotionvectors = capture_backwardmotionvectors
        if capture_depth is not None:
            self.capture_depth = capture_depth
        if capture_detections is not None:
            self.capture_detections = capture_detections
        if capture_instance is not None:
            self.capture_instance = capture_instance
        if capture_intensity is not None:
            self.capture_intensity = capture_intensity
        if capture_motionvectors is not None:
            self.capture_motionvectors = capture_motionvectors
        if capture_normals is not None:
            self.capture_normals = capture_normals
        if capture_properties is not None:
            self.capture_properties = capture_properties
        if capture_rgb is not None:
            self.capture_rgb = capture_rgb
        if capture_segmentation is not None:
            self.capture_segmentation = capture_segmentation
        if intensity_params is not None:
            self.intensity_params = intensity_params
        if maximum_cutoff_prob is not None:
            self.maximum_cutoff_prob = maximum_cutoff_prob
        if maximum_offset is not None:
            self.maximum_offset = maximum_offset
        if maximum_range_cutoff is not None:
            self.maximum_range_cutoff = maximum_range_cutoff
        if merge_returns is not None:
            self.merge_returns = merge_returns
        if minimum_cutoff_prob is not None:
            self.minimum_cutoff_prob = minimum_cutoff_prob
        if minimum_noise is not None:
            self.minimum_noise = minimum_noise
        if minimum_offset is not None:
            self.minimum_offset = minimum_offset
        if minimum_range_cutoff is not None:
            self.minimum_range_cutoff = minimum_range_cutoff
        if multi_returns is not None:
            self.multi_returns = multi_returns
        if pattern is not None:
            self.pattern = pattern
        if range_noise_mean is not None:
            self.range_noise_mean = range_noise_mean
        if range_noise_stddev is not None:
            self.range_noise_stddev = range_noise_stddev
        if rotation_rate is not None:
            self.rotation_rate = rotation_rate
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if time_offset is not None:
            self.time_offset = time_offset

    @property
    def alice_lidar_model(self) -> AliceLidarModel:
        return self._alice_lidar_model

    @alice_lidar_model.setter
    def alice_lidar_model(self, value: AliceLidarModel):
        self.proto.alice_lidar_model.CopyFrom(value.proto)
        
        self._alice_lidar_model = value
        self._alice_lidar_model._update_proto_references(self.proto.alice_lidar_model)

    @property
    def azimuth_max(self) -> float:
        return self.proto.azimuth_max

    @azimuth_max.setter
    def azimuth_max(self, value: float):
        self.proto.azimuth_max = value

    @property
    def azimuth_min(self) -> float:
        return self.proto.azimuth_min

    @azimuth_min.setter
    def azimuth_min(self, value: float):
        self.proto.azimuth_min = value

    @property
    def beam_data(self) -> List[LidarBeam]:
        return self._beam_data

    @beam_data.setter
    def beam_data(self, value: List[LidarBeam]):
        self._beam_data.clear()
        for v in value:
            self._beam_data.append(v)

    @property
    def capture_backwardmotionvectors(self) -> bool:
        return self.proto.capture_backwardmotionvectors

    @capture_backwardmotionvectors.setter
    def capture_backwardmotionvectors(self, value: bool):
        self.proto.capture_backwardmotionvectors = value

    @property
    def capture_depth(self) -> bool:
        return self.proto.capture_depth

    @capture_depth.setter
    def capture_depth(self, value: bool):
        self.proto.capture_depth = value

    @property
    def capture_detections(self) -> bool:
        return self.proto.capture_detections

    @capture_detections.setter
    def capture_detections(self, value: bool):
        self.proto.capture_detections = value

    @property
    def capture_instance(self) -> bool:
        return self.proto.capture_instance

    @capture_instance.setter
    def capture_instance(self, value: bool):
        self.proto.capture_instance = value

    @property
    def capture_intensity(self) -> bool:
        return self.proto.capture_intensity

    @capture_intensity.setter
    def capture_intensity(self, value: bool):
        self.proto.capture_intensity = value

    @property
    def capture_motionvectors(self) -> bool:
        return self.proto.capture_motionvectors

    @capture_motionvectors.setter
    def capture_motionvectors(self, value: bool):
        self.proto.capture_motionvectors = value

    @property
    def capture_normals(self) -> bool:
        return self.proto.capture_normals

    @capture_normals.setter
    def capture_normals(self, value: bool):
        self.proto.capture_normals = value

    @property
    def capture_properties(self) -> bool:
        return self.proto.capture_properties

    @capture_properties.setter
    def capture_properties(self, value: bool):
        self.proto.capture_properties = value

    @property
    def capture_rgb(self) -> bool:
        return self.proto.capture_rgb

    @capture_rgb.setter
    def capture_rgb(self, value: bool):
        self.proto.capture_rgb = value

    @property
    def capture_segmentation(self) -> bool:
        return self.proto.capture_segmentation

    @capture_segmentation.setter
    def capture_segmentation(self, value: bool):
        self.proto.capture_segmentation = value

    @property
    def intensity_params(self) -> LidarIntensityParams:
        return self._intensity_params

    @intensity_params.setter
    def intensity_params(self, value: LidarIntensityParams):
        self.proto.intensity_params.CopyFrom(value.proto)
        
        self._intensity_params = value
        self._intensity_params._update_proto_references(self.proto.intensity_params)

    @property
    def maximum_cutoff_prob(self) -> float:
        return self.proto.maximum_cutoff_prob

    @maximum_cutoff_prob.setter
    def maximum_cutoff_prob(self, value: float):
        self.proto.maximum_cutoff_prob = value

    @property
    def maximum_offset(self) -> float:
        return self.proto.maximum_offset

    @maximum_offset.setter
    def maximum_offset(self, value: float):
        self.proto.maximum_offset = value

    @property
    def maximum_range_cutoff(self) -> float:
        return self.proto.maximum_range_cutoff

    @maximum_range_cutoff.setter
    def maximum_range_cutoff(self, value: float):
        self.proto.maximum_range_cutoff = value

    @property
    def merge_returns(self) -> int:
        return self.proto.merge_returns

    @merge_returns.setter
    def merge_returns(self, value: int):
        self.proto.merge_returns = value

    @property
    def minimum_cutoff_prob(self) -> float:
        return self.proto.minimum_cutoff_prob

    @minimum_cutoff_prob.setter
    def minimum_cutoff_prob(self, value: float):
        self.proto.minimum_cutoff_prob = value

    @property
    def minimum_noise(self) -> float:
        return self.proto.minimum_noise

    @minimum_noise.setter
    def minimum_noise(self, value: float):
        self.proto.minimum_noise = value

    @property
    def minimum_offset(self) -> float:
        return self.proto.minimum_offset

    @minimum_offset.setter
    def minimum_offset(self, value: float):
        self.proto.minimum_offset = value

    @property
    def minimum_range_cutoff(self) -> float:
        return self.proto.minimum_range_cutoff

    @minimum_range_cutoff.setter
    def minimum_range_cutoff(self, value: float):
        self.proto.minimum_range_cutoff = value

    @property
    def multi_returns(self) -> int:
        return self.proto.multi_returns

    @multi_returns.setter
    def multi_returns(self, value: int):
        self.proto.multi_returns = value

    @property
    def pattern(self) -> str:
        return self.proto.pattern

    @pattern.setter
    def pattern(self, value: str):
        self.proto.pattern = value

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
    def rotation_rate(self) -> float:
        return self.proto.rotation_rate

    @rotation_rate.setter
    def rotation_rate(self, value: float):
        self.proto.rotation_rate = value

    @property
    def sample_rate(self) -> float:
        return self.proto.sample_rate

    @sample_rate.setter
    def sample_rate(self, value: float):
        self.proto.sample_rate = value

    @property
    def time_offset(self) -> float:
        return self.proto.time_offset

    @time_offset.setter
    def time_offset(self, value: float):
        self.proto.time_offset = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarIntrinsic):
        self.proto = proto
        self._alice_lidar_model._update_proto_references(proto.alice_lidar_model)
        for i, v in enumerate(self.beam_data):
            v._update_proto_references(self.proto.beam_data[i])
        self._intensity_params._update_proto_references(proto.intensity_params)

@register_wrapper(proto_type=pd_sensor_pb2.LidarNoiseParams)
class LidarNoiseParams(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.LidarNoiseParams

    def __init__(self, *, proto: Optional[pd_sensor_pb2.LidarNoiseParams]=None, max_dist: Optional[float]=None, max_offset: Optional[float]=None, max_prob: Optional[float]=None, min_dist: Optional[float]=None, min_noise: Optional[float]=None, min_offset: Optional[float]=None, min_prob: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.LidarNoiseParams()
        self.proto = proto
        if max_dist is not None:
            self.max_dist = max_dist
        if max_offset is not None:
            self.max_offset = max_offset
        if max_prob is not None:
            self.max_prob = max_prob
        if min_dist is not None:
            self.min_dist = min_dist
        if min_noise is not None:
            self.min_noise = min_noise
        if min_offset is not None:
            self.min_offset = min_offset
        if min_prob is not None:
            self.min_prob = min_prob

    @property
    def max_dist(self) -> float:
        return self.proto.max_dist

    @max_dist.setter
    def max_dist(self, value: float):
        self.proto.max_dist = value

    @property
    def max_offset(self) -> float:
        return self.proto.max_offset

    @max_offset.setter
    def max_offset(self, value: float):
        self.proto.max_offset = value

    @property
    def max_prob(self) -> float:
        return self.proto.max_prob

    @max_prob.setter
    def max_prob(self, value: float):
        self.proto.max_prob = value

    @property
    def min_dist(self) -> float:
        return self.proto.min_dist

    @min_dist.setter
    def min_dist(self, value: float):
        self.proto.min_dist = value

    @property
    def min_noise(self) -> float:
        return self.proto.min_noise

    @min_noise.setter
    def min_noise(self, value: float):
        self.proto.min_noise = value

    @property
    def min_offset(self) -> float:
        return self.proto.min_offset

    @min_offset.setter
    def min_offset(self, value: float):
        self.proto.min_offset = value

    @property
    def min_prob(self) -> float:
        return self.proto.min_prob

    @min_prob.setter
    def min_prob(self, value: float):
        self.proto.min_prob = value

    def _update_proto_references(self, proto: pd_sensor_pb2.LidarNoiseParams):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.NoiseParams)
class NoiseParams(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.NoiseParams

    def __init__(self, *, proto: Optional[pd_sensor_pb2.NoiseParams]=None, bilateral_sigma_d: Optional[float]=None, bilateral_sigma_r: Optional[float]=None, denoise_filter: Optional[DenoiseFilter]=None, denoise_filter_size: Optional[int]=None, enable_auto_iso: Optional[bool]=None, enable_auto_noise: Optional[bool]=None, enable_bayer: Optional[bool]=None, enable_denoise: Optional[bool]=None, enable_gauss_noise: Optional[bool]=None, enable_poisson_noise: Optional[bool]=None, fstop: Optional[float]=None, gauss_noise_sigma: Optional[float]=None, is_using_iso: Optional[bool]=None, iso_level: Optional[int]=None, max_exposure_time: Optional[float]=None, poisson_noise_lambda: Optional[float]=None, post_amplifier_noise: Optional[float]=None, pre_amplifier_noise: Optional[float]=None, quantum_efficiency: Optional[float]=None, signal_amount: Optional[int]=None):
        if proto is None:
            proto = pd_sensor_pb2.NoiseParams()
        self.proto = proto
        if bilateral_sigma_d is not None:
            self.bilateral_sigma_d = bilateral_sigma_d
        if bilateral_sigma_r is not None:
            self.bilateral_sigma_r = bilateral_sigma_r
        if denoise_filter is not None:
            self.denoise_filter = denoise_filter
        if denoise_filter_size is not None:
            self.denoise_filter_size = denoise_filter_size
        if enable_auto_iso is not None:
            self.enable_auto_iso = enable_auto_iso
        if enable_auto_noise is not None:
            self.enable_auto_noise = enable_auto_noise
        if enable_bayer is not None:
            self.enable_bayer = enable_bayer
        if enable_denoise is not None:
            self.enable_denoise = enable_denoise
        if enable_gauss_noise is not None:
            self.enable_gauss_noise = enable_gauss_noise
        if enable_poisson_noise is not None:
            self.enable_poisson_noise = enable_poisson_noise
        if fstop is not None:
            self.fstop = fstop
        if gauss_noise_sigma is not None:
            self.gauss_noise_sigma = gauss_noise_sigma
        if is_using_iso is not None:
            self.is_using_iso = is_using_iso
        if iso_level is not None:
            self.iso_level = iso_level
        if max_exposure_time is not None:
            self.max_exposure_time = max_exposure_time
        if poisson_noise_lambda is not None:
            self.poisson_noise_lambda = poisson_noise_lambda
        if post_amplifier_noise is not None:
            self.post_amplifier_noise = post_amplifier_noise
        if pre_amplifier_noise is not None:
            self.pre_amplifier_noise = pre_amplifier_noise
        if quantum_efficiency is not None:
            self.quantum_efficiency = quantum_efficiency
        if signal_amount is not None:
            self.signal_amount = signal_amount

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
    def denoise_filter(self) -> int:
        return self.proto.denoise_filter

    @denoise_filter.setter
    def denoise_filter(self, value: int):
        self.proto.denoise_filter = value

    @property
    def denoise_filter_size(self) -> int:
        return self.proto.denoise_filter_size

    @denoise_filter_size.setter
    def denoise_filter_size(self, value: int):
        self.proto.denoise_filter_size = value

    @property
    def enable_auto_iso(self) -> bool:
        return self.proto.enable_auto_iso

    @enable_auto_iso.setter
    def enable_auto_iso(self, value: bool):
        self.proto.enable_auto_iso = value

    @property
    def enable_auto_noise(self) -> bool:
        return self.proto.enable_auto_noise

    @enable_auto_noise.setter
    def enable_auto_noise(self, value: bool):
        self.proto.enable_auto_noise = value

    @property
    def enable_bayer(self) -> bool:
        return self.proto.enable_bayer

    @enable_bayer.setter
    def enable_bayer(self, value: bool):
        self.proto.enable_bayer = value

    @property
    def enable_denoise(self) -> bool:
        return self.proto.enable_denoise

    @enable_denoise.setter
    def enable_denoise(self, value: bool):
        self.proto.enable_denoise = value

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
    def fstop(self) -> float:
        return self.proto.fstop

    @fstop.setter
    def fstop(self, value: float):
        self.proto.fstop = value

    @property
    def gauss_noise_sigma(self) -> float:
        return self.proto.gauss_noise_sigma

    @gauss_noise_sigma.setter
    def gauss_noise_sigma(self, value: float):
        self.proto.gauss_noise_sigma = value

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
    def max_exposure_time(self) -> float:
        return self.proto.max_exposure_time

    @max_exposure_time.setter
    def max_exposure_time(self, value: float):
        self.proto.max_exposure_time = value

    @property
    def poisson_noise_lambda(self) -> float:
        return self.proto.poisson_noise_lambda

    @poisson_noise_lambda.setter
    def poisson_noise_lambda(self, value: float):
        self.proto.poisson_noise_lambda = value

    @property
    def post_amplifier_noise(self) -> float:
        return self.proto.post_amplifier_noise

    @post_amplifier_noise.setter
    def post_amplifier_noise(self, value: float):
        self.proto.post_amplifier_noise = value

    @property
    def pre_amplifier_noise(self) -> float:
        return self.proto.pre_amplifier_noise

    @pre_amplifier_noise.setter
    def pre_amplifier_noise(self, value: float):
        self.proto.pre_amplifier_noise = value

    @property
    def quantum_efficiency(self) -> float:
        return self.proto.quantum_efficiency

    @quantum_efficiency.setter
    def quantum_efficiency(self, value: float):
        self.proto.quantum_efficiency = value

    @property
    def signal_amount(self) -> int:
        return self.proto.signal_amount

    @signal_amount.setter
    def signal_amount(self, value: int):
        self.proto.signal_amount = value

    def _update_proto_references(self, proto: pd_sensor_pb2.NoiseParams):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.PostProcessNode)
class PostProcessNode(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.PostProcessNode

    def __init__(self, *, proto: Optional[pd_sensor_pb2.PostProcessNode]=None, material: Optional[str]=None, weight: Optional[float]=None):
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
    _proto_message = pd_sensor_pb2.PostProcessParams

    def __init__(self, *, proto: Optional[pd_sensor_pb2.PostProcessParams]=None, dof_depth_blur_amount: Optional[float]=None, dof_depth_blur_radius: Optional[float]=None, dof_focal_distance: Optional[float]=None, exposure_compensation: Optional[float]=None, exposure_max_ev100: Optional[float]=None, exposure_metering_mask: Optional[str]=None, exposure_min_ev100: Optional[float]=None, exposure_speed_down: Optional[float]=None, exposure_speed_up: Optional[float]=None, motion_blur_amount: Optional[float]=None, motion_blur_max: Optional[float]=None, vignette_intensity: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.PostProcessParams()
        self.proto = proto
        if dof_depth_blur_amount is not None:
            self.dof_depth_blur_amount = dof_depth_blur_amount
        if dof_depth_blur_radius is not None:
            self.dof_depth_blur_radius = dof_depth_blur_radius
        if dof_focal_distance is not None:
            self.dof_focal_distance = dof_focal_distance
        if exposure_compensation is not None:
            self.exposure_compensation = exposure_compensation
        if exposure_max_ev100 is not None:
            self.exposure_max_ev100 = exposure_max_ev100
        if exposure_metering_mask is not None:
            self.exposure_metering_mask = exposure_metering_mask
        if exposure_min_ev100 is not None:
            self.exposure_min_ev100 = exposure_min_ev100
        if exposure_speed_down is not None:
            self.exposure_speed_down = exposure_speed_down
        if exposure_speed_up is not None:
            self.exposure_speed_up = exposure_speed_up
        if motion_blur_amount is not None:
            self.motion_blur_amount = motion_blur_amount
        if motion_blur_max is not None:
            self.motion_blur_max = motion_blur_max
        if vignette_intensity is not None:
            self.vignette_intensity = vignette_intensity

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
    def dof_focal_distance(self) -> float:
        return self.proto.dof_focal_distance

    @dof_focal_distance.setter
    def dof_focal_distance(self, value: float):
        self.proto.dof_focal_distance = value

    @property
    def exposure_compensation(self) -> float:
        return self.proto.exposure_compensation

    @exposure_compensation.setter
    def exposure_compensation(self, value: float):
        self.proto.exposure_compensation = value

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
    def exposure_min_ev100(self) -> float:
        return self.proto.exposure_min_ev100

    @exposure_min_ev100.setter
    def exposure_min_ev100(self, value: float):
        self.proto.exposure_min_ev100 = value

    @property
    def exposure_speed_down(self) -> float:
        return self.proto.exposure_speed_down

    @exposure_speed_down.setter
    def exposure_speed_down(self, value: float):
        self.proto.exposure_speed_down = value

    @property
    def exposure_speed_up(self) -> float:
        return self.proto.exposure_speed_up

    @exposure_speed_up.setter
    def exposure_speed_up(self, value: float):
        self.proto.exposure_speed_up = value

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
    def vignette_intensity(self) -> float:
        return self.proto.vignette_intensity

    @vignette_intensity.setter
    def vignette_intensity(self, value: float):
        self.proto.vignette_intensity = value

    def _update_proto_references(self, proto: pd_sensor_pb2.PostProcessParams):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.RadarBasicParameters)
class RadarBasicParameters(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.RadarBasicParameters

    def __init__(self, *, proto: Optional[pd_sensor_pb2.RadarBasicParameters]=None, azimuth_accuracy: Optional[float]=None, azimuth_fov: Optional[float]=None, azimuth_resolution: Optional[float]=None, doppler_resolution: Optional[float]=None, elevation_accuracy: Optional[float]=None, elevation_fov: Optional[float]=None, elevation_resolution: Optional[float]=None, max_doppler: Optional[float]=None, max_range: Optional[float]=None, number_rays_per_frame: Optional[int]=None, prf_profile_file: Optional[str]=None, radar_output_2d: Optional[bool]=None, range_resolution: Optional[float]=None, use_random_raycast: Optional[bool]=None):
        if proto is None:
            proto = pd_sensor_pb2.RadarBasicParameters()
        self.proto = proto
        if azimuth_accuracy is not None:
            self.azimuth_accuracy = azimuth_accuracy
        if azimuth_fov is not None:
            self.azimuth_fov = azimuth_fov
        if azimuth_resolution is not None:
            self.azimuth_resolution = azimuth_resolution
        if doppler_resolution is not None:
            self.doppler_resolution = doppler_resolution
        if elevation_accuracy is not None:
            self.elevation_accuracy = elevation_accuracy
        if elevation_fov is not None:
            self.elevation_fov = elevation_fov
        if elevation_resolution is not None:
            self.elevation_resolution = elevation_resolution
        if max_doppler is not None:
            self.max_doppler = max_doppler
        if max_range is not None:
            self.max_range = max_range
        if number_rays_per_frame is not None:
            self.number_rays_per_frame = number_rays_per_frame
        if prf_profile_file is not None:
            self.prf_profile_file = prf_profile_file
        if radar_output_2d is not None:
            self.radar_output_2d = radar_output_2d
        if range_resolution is not None:
            self.range_resolution = range_resolution
        if use_random_raycast is not None:
            self.use_random_raycast = use_random_raycast

    @property
    def azimuth_accuracy(self) -> float:
        return self.proto.azimuth_accuracy

    @azimuth_accuracy.setter
    def azimuth_accuracy(self, value: float):
        self.proto.azimuth_accuracy = value

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
    def doppler_resolution(self) -> float:
        return self.proto.doppler_resolution

    @doppler_resolution.setter
    def doppler_resolution(self, value: float):
        self.proto.doppler_resolution = value

    @property
    def elevation_accuracy(self) -> float:
        return self.proto.elevation_accuracy

    @elevation_accuracy.setter
    def elevation_accuracy(self, value: float):
        self.proto.elevation_accuracy = value

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
    def max_doppler(self) -> float:
        return self.proto.max_doppler

    @max_doppler.setter
    def max_doppler(self, value: float):
        self.proto.max_doppler = value

    @property
    def max_range(self) -> float:
        return self.proto.max_range

    @max_range.setter
    def max_range(self, value: float):
        self.proto.max_range = value

    @property
    def number_rays_per_frame(self) -> int:
        return self.proto.number_rays_per_frame

    @number_rays_per_frame.setter
    def number_rays_per_frame(self, value: int):
        self.proto.number_rays_per_frame = value

    @property
    def prf_profile_file(self) -> str:
        return self.proto.prf_profile_file

    @prf_profile_file.setter
    def prf_profile_file(self, value: str):
        self.proto.prf_profile_file = value

    @property
    def radar_output_2d(self) -> bool:
        return self.proto.radar_output_2d

    @radar_output_2d.setter
    def radar_output_2d(self, value: bool):
        self.proto.radar_output_2d = value

    @property
    def range_resolution(self) -> float:
        return self.proto.range_resolution

    @range_resolution.setter
    def range_resolution(self, value: float):
        self.proto.range_resolution = value

    @property
    def use_random_raycast(self) -> bool:
        return self.proto.use_random_raycast

    @use_random_raycast.setter
    def use_random_raycast(self, value: bool):
        self.proto.use_random_raycast = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarBasicParameters):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.RadarDetectorParameters)
class RadarDetectorParameters(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.RadarDetectorParameters

    def __init__(self, *, proto: Optional[pd_sensor_pb2.RadarDetectorParameters]=None, cfar_guard_cell: Optional[int]=None, cfar_neighbor_cell: Optional[int]=None, cfar_threshold_scale: Optional[float]=None, cfar_type: Optional[str]=None, detector_constant_gain: Optional[float]=None, detector_radiometric_decay: Optional[float]=None, detector_radiometric_gain: Optional[float]=None, detector_type: Optional[str]=None, enable_cfar: Optional[bool]=None):
        if proto is None:
            proto = pd_sensor_pb2.RadarDetectorParameters()
        self.proto = proto
        if cfar_guard_cell is not None:
            self.cfar_guard_cell = cfar_guard_cell
        if cfar_neighbor_cell is not None:
            self.cfar_neighbor_cell = cfar_neighbor_cell
        if cfar_threshold_scale is not None:
            self.cfar_threshold_scale = cfar_threshold_scale
        if cfar_type is not None:
            self.cfar_type = cfar_type
        if detector_constant_gain is not None:
            self.detector_constant_gain = detector_constant_gain
        if detector_radiometric_decay is not None:
            self.detector_radiometric_decay = detector_radiometric_decay
        if detector_radiometric_gain is not None:
            self.detector_radiometric_gain = detector_radiometric_gain
        if detector_type is not None:
            self.detector_type = detector_type
        if enable_cfar is not None:
            self.enable_cfar = enable_cfar

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

    @property
    def cfar_type(self) -> str:
        return self.proto.cfar_type

    @cfar_type.setter
    def cfar_type(self, value: str):
        self.proto.cfar_type = value

    @property
    def detector_constant_gain(self) -> float:
        return self.proto.detector_constant_gain

    @detector_constant_gain.setter
    def detector_constant_gain(self, value: float):
        self.proto.detector_constant_gain = value

    @property
    def detector_radiometric_decay(self) -> float:
        return self.proto.detector_radiometric_decay

    @detector_radiometric_decay.setter
    def detector_radiometric_decay(self, value: float):
        self.proto.detector_radiometric_decay = value

    @property
    def detector_radiometric_gain(self) -> float:
        return self.proto.detector_radiometric_gain

    @detector_radiometric_gain.setter
    def detector_radiometric_gain(self, value: float):
        self.proto.detector_radiometric_gain = value

    @property
    def detector_type(self) -> str:
        return self.proto.detector_type

    @detector_type.setter
    def detector_type(self, value: str):
        self.proto.detector_type = value

    @property
    def enable_cfar(self) -> bool:
        return self.proto.enable_cfar

    @enable_cfar.setter
    def enable_cfar(self, value: bool):
        self.proto.enable_cfar = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarDetectorParameters):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.RadarEnergyParameters)
class RadarEnergyParameters(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.RadarEnergyParameters

    def __init__(self, *, proto: Optional[pd_sensor_pb2.RadarEnergyParameters]=None, beam_pattern_file: Optional[str]=None, enable_beam_pattern: Optional[bool]=None, gain_jitter_std: Optional[float]=None, nominal_gain: Optional[float]=None, radiometric_coefficient: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.RadarEnergyParameters()
        self.proto = proto
        if beam_pattern_file is not None:
            self.beam_pattern_file = beam_pattern_file
        if enable_beam_pattern is not None:
            self.enable_beam_pattern = enable_beam_pattern
        if gain_jitter_std is not None:
            self.gain_jitter_std = gain_jitter_std
        if nominal_gain is not None:
            self.nominal_gain = nominal_gain
        if radiometric_coefficient is not None:
            self.radiometric_coefficient = radiometric_coefficient

    @property
    def beam_pattern_file(self) -> str:
        return self.proto.beam_pattern_file

    @beam_pattern_file.setter
    def beam_pattern_file(self, value: str):
        self.proto.beam_pattern_file = value

    @property
    def enable_beam_pattern(self) -> bool:
        return self.proto.enable_beam_pattern

    @enable_beam_pattern.setter
    def enable_beam_pattern(self, value: bool):
        self.proto.enable_beam_pattern = value

    @property
    def gain_jitter_std(self) -> float:
        return self.proto.gain_jitter_std

    @gain_jitter_std.setter
    def gain_jitter_std(self, value: float):
        self.proto.gain_jitter_std = value

    @property
    def nominal_gain(self) -> float:
        return self.proto.nominal_gain

    @nominal_gain.setter
    def nominal_gain(self, value: float):
        self.proto.nominal_gain = value

    @property
    def radiometric_coefficient(self) -> float:
        return self.proto.radiometric_coefficient

    @radiometric_coefficient.setter
    def radiometric_coefficient(self, value: float):
        self.proto.radiometric_coefficient = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarEnergyParameters):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.RadarIntrinsic)
class RadarIntrinsic(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.RadarIntrinsic

    def __init__(self, *, proto: Optional[pd_sensor_pb2.RadarIntrinsic]=None, basic_parameters: Optional[RadarBasicParameters]=None, detector_parameters: Optional[RadarDetectorParameters]=None, energy_parameters: Optional[RadarEnergyParameters]=None, noise_parameters: Optional[RadarNoiseParameters]=None):
        if proto is None:
            proto = pd_sensor_pb2.RadarIntrinsic()
        self.proto = proto
        self._basic_parameters = get_wrapper(proto_type=proto.basic_parameters.__class__)(proto=proto.basic_parameters)
        self._detector_parameters = get_wrapper(proto_type=proto.detector_parameters.__class__)(proto=proto.detector_parameters)
        self._energy_parameters = get_wrapper(proto_type=proto.energy_parameters.__class__)(proto=proto.energy_parameters)
        self._noise_parameters = get_wrapper(proto_type=proto.noise_parameters.__class__)(proto=proto.noise_parameters)
        if basic_parameters is not None:
            self.basic_parameters = basic_parameters
        if detector_parameters is not None:
            self.detector_parameters = detector_parameters
        if energy_parameters is not None:
            self.energy_parameters = energy_parameters
        if noise_parameters is not None:
            self.noise_parameters = noise_parameters

    @property
    def basic_parameters(self) -> RadarBasicParameters:
        return self._basic_parameters

    @basic_parameters.setter
    def basic_parameters(self, value: RadarBasicParameters):
        self.proto.basic_parameters.CopyFrom(value.proto)
        
        self._basic_parameters = value
        self._basic_parameters._update_proto_references(self.proto.basic_parameters)

    @property
    def detector_parameters(self) -> RadarDetectorParameters:
        return self._detector_parameters

    @detector_parameters.setter
    def detector_parameters(self, value: RadarDetectorParameters):
        self.proto.detector_parameters.CopyFrom(value.proto)
        
        self._detector_parameters = value
        self._detector_parameters._update_proto_references(self.proto.detector_parameters)

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

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarIntrinsic):
        self.proto = proto
        self._basic_parameters._update_proto_references(proto.basic_parameters)
        self._detector_parameters._update_proto_references(proto.detector_parameters)
        self._energy_parameters._update_proto_references(proto.energy_parameters)
        self._noise_parameters._update_proto_references(proto.noise_parameters)

@register_wrapper(proto_type=pd_sensor_pb2.RadarNoiseParameters)
class RadarNoiseParameters(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.RadarNoiseParameters

    def __init__(self, *, proto: Optional[pd_sensor_pb2.RadarNoiseParameters]=None, enable_doa_noise: Optional[bool]=None, enable_thermal_noise: Optional[bool]=None, thermal_noise_mean: Optional[float]=None, thermal_noise_std: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.RadarNoiseParameters()
        self.proto = proto
        if enable_doa_noise is not None:
            self.enable_doa_noise = enable_doa_noise
        if enable_thermal_noise is not None:
            self.enable_thermal_noise = enable_thermal_noise
        if thermal_noise_mean is not None:
            self.thermal_noise_mean = thermal_noise_mean
        if thermal_noise_std is not None:
            self.thermal_noise_std = thermal_noise_std

    @property
    def enable_doa_noise(self) -> bool:
        return self.proto.enable_doa_noise

    @enable_doa_noise.setter
    def enable_doa_noise(self, value: bool):
        self.proto.enable_doa_noise = value

    @property
    def enable_thermal_noise(self) -> bool:
        return self.proto.enable_thermal_noise

    @enable_thermal_noise.setter
    def enable_thermal_noise(self, value: bool):
        self.proto.enable_thermal_noise = value

    @property
    def thermal_noise_mean(self) -> float:
        return self.proto.thermal_noise_mean

    @thermal_noise_mean.setter
    def thermal_noise_mean(self, value: float):
        self.proto.thermal_noise_mean = value

    @property
    def thermal_noise_std(self) -> float:
        return self.proto.thermal_noise_std

    @thermal_noise_std.setter
    def thermal_noise_std(self, value: float):
        self.proto.thermal_noise_std = value

    def _update_proto_references(self, proto: pd_sensor_pb2.RadarNoiseParameters):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.SensorConfig)
class SensorConfig(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.SensorConfig

    def __init__(self, *, proto: Optional[pd_sensor_pb2.SensorConfig]=None, camera_intrinsic: Optional[CameraIntrinsic]=None, display_name: Optional[str]=None, lidar_intrinsic: Optional[LidarIntrinsic]=None, radar_intrinsic: Optional[RadarIntrinsic]=None, sensor_extrinsic: Optional[SensorExtrinsic]=None):
        if proto is None:
            proto = pd_sensor_pb2.SensorConfig()
        self.proto = proto
        self._camera_intrinsic = get_wrapper(proto_type=proto.camera_intrinsic.__class__)(proto=proto.camera_intrinsic)
        self._lidar_intrinsic = get_wrapper(proto_type=proto.lidar_intrinsic.__class__)(proto=proto.lidar_intrinsic)
        self._radar_intrinsic = get_wrapper(proto_type=proto.radar_intrinsic.__class__)(proto=proto.radar_intrinsic)
        self._sensor_extrinsic = get_wrapper(proto_type=proto.sensor_extrinsic.__class__)(proto=proto.sensor_extrinsic)
        if camera_intrinsic is not None:
            self.camera_intrinsic = camera_intrinsic
        if display_name is not None:
            self.display_name = display_name
        if lidar_intrinsic is not None:
            self.lidar_intrinsic = lidar_intrinsic
        if radar_intrinsic is not None:
            self.radar_intrinsic = radar_intrinsic
        if sensor_extrinsic is not None:
            self.sensor_extrinsic = sensor_extrinsic

    @property
    def camera_intrinsic(self) -> CameraIntrinsic:
        return self._camera_intrinsic

    @camera_intrinsic.setter
    def camera_intrinsic(self, value: CameraIntrinsic):
        self.proto.camera_intrinsic.CopyFrom(value.proto)
        
        self._camera_intrinsic = value
        self._camera_intrinsic._update_proto_references(self.proto.camera_intrinsic)

    @property
    def display_name(self) -> str:
        return self.proto.display_name

    @display_name.setter
    def display_name(self, value: str):
        self.proto.display_name = value

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

@register_wrapper(proto_type=pd_sensor_pb2.SensorExtrinsic)
class SensorExtrinsic(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.SensorExtrinsic

    def __init__(self, *, proto: Optional[pd_sensor_pb2.SensorExtrinsic]=None, attach_socket: Optional[str]=None, follow_rotation: Optional[bool]=None, lock_to_yaw: Optional[bool]=None, pitch: Optional[float]=None, roll: Optional[float]=None, x: Optional[float]=None, y: Optional[float]=None, yaw: Optional[float]=None, z: Optional[float]=None):
        if proto is None:
            proto = pd_sensor_pb2.SensorExtrinsic()
        self.proto = proto
        if attach_socket is not None:
            self.attach_socket = attach_socket
        if follow_rotation is not None:
            self.follow_rotation = follow_rotation
        if lock_to_yaw is not None:
            self.lock_to_yaw = lock_to_yaw
        if pitch is not None:
            self.pitch = pitch
        if roll is not None:
            self.roll = roll
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if yaw is not None:
            self.yaw = yaw
        if z is not None:
            self.z = z

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

    @property
    def lock_to_yaw(self) -> bool:
        return self.proto.lock_to_yaw

    @lock_to_yaw.setter
    def lock_to_yaw(self, value: bool):
        self.proto.lock_to_yaw = value

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
    def yaw(self) -> float:
        return self.proto.yaw

    @yaw.setter
    def yaw(self, value: float):
        self.proto.yaw = value

    @property
    def z(self) -> float:
        return self.proto.z

    @z.setter
    def z(self, value: float):
        self.proto.z = value

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorExtrinsic):
        self.proto = proto

@register_wrapper(proto_type=pd_sensor_pb2.SensorList)
class SensorList(ProtoMessageClass):
    _proto_message = pd_sensor_pb2.SensorList

    def __init__(self, *, proto: Optional[pd_sensor_pb2.SensorList]=None, sensors: Optional[List[str]]=None):
        if proto is None:
            proto = pd_sensor_pb2.SensorList()
        self.proto = proto
        self._sensors = ProtoListWrapper(container=[str(v) for v in proto.sensors], attr_name='sensors', list_owner=self)
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
    _proto_message = pd_sensor_pb2.SensorRigConfig

    def __init__(self, *, proto: Optional[pd_sensor_pb2.SensorRigConfig]=None, default_sensor_splits_list: Optional[List[SensorList]]=None, sensor_configs: Optional[List[SensorConfig]]=None, sensor_rig_artifact_uid: Optional[str]=None):
        if proto is None:
            proto = pd_sensor_pb2.SensorRigConfig()
        self.proto = proto
        self._default_sensor_splits_list = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.default_sensor_splits_list], attr_name='default_sensor_splits_list', list_owner=self)
        self._sensor_configs = ProtoListWrapper(container=[get_wrapper(proto_type=v.__class__)(proto=v) for v in proto.sensor_configs], attr_name='sensor_configs', list_owner=self)
        if default_sensor_splits_list is not None:
            self.default_sensor_splits_list = default_sensor_splits_list
        if sensor_configs is not None:
            self.sensor_configs = sensor_configs
        if sensor_rig_artifact_uid is not None:
            self.sensor_rig_artifact_uid = sensor_rig_artifact_uid

    @property
    def default_sensor_splits_list(self) -> List[SensorList]:
        return self._default_sensor_splits_list

    @default_sensor_splits_list.setter
    def default_sensor_splits_list(self, value: List[SensorList]):
        self._default_sensor_splits_list.clear()
        for v in value:
            self._default_sensor_splits_list.append(v)

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

    def _update_proto_references(self, proto: pd_sensor_pb2.SensorRigConfig):
        self.proto = proto
        for i, v in enumerate(self.default_sensor_splits_list):
            v._update_proto_references(self.proto.default_sensor_splits_list[i])
        for i, v in enumerate(self.sensor_configs):
            v._update_proto_references(self.proto.sensor_configs[i])

@register_wrapper(proto_type=pd_sensor_pb2.DenoiseFilter)
class DenoiseFilter(ProtoEnumClass):
    _proto_message = pd_sensor_pb2.DenoiseFilter
    AVERAGE_FILTER: pd_sensor_pb2.DenoiseFilter = pd_sensor_pb2.DenoiseFilter.AVERAGE_FILTER
    BILATERAL_FILTER: pd_sensor_pb2.DenoiseFilter = pd_sensor_pb2.DenoiseFilter.BILATERAL_FILTER
    FAST_MEDIAN_FILTER: pd_sensor_pb2.DenoiseFilter = pd_sensor_pb2.DenoiseFilter.FAST_MEDIAN_FILTER
    MEDIAN_FILTER: pd_sensor_pb2.DenoiseFilter = pd_sensor_pb2.DenoiseFilter.MEDIAN_FILTER