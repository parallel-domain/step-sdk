# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
State flatbuffer serialization and deserialization

This set of classes serialize and deserialize between State objects and
their flatbuffer encodings
"""

from typing import Union, Tuple, List, Type, TypeVar, Optional
from dataclasses import dataclass
import logging

import flatbuffers
import numpy as np

from pd.state.sensor import (
    PostProcessMaterial, PostProcessParams, NoiseParams, DenoiseFilter, DistortionParams,
    CameraSensor, LiDARSensor, Sensor, LiDARBeam, LiDARIntensityParams, TonemapCurve
)
from pd.state.state import (
    VehicleAgent, ModelAgent, SensorAgent, WorldInfo, PerformanceMode, State,
    PhaseBulbValue, PhaseBulbLogicalState, SignalAgent, VehicleIndicatorState
)
from pd.state.pose6d import Pose6D

from pd.internal.fb.generated.python.pdPerformanceFeature import pdPerformanceFeature
from pd.internal.fb.generated.python import (
    float3_t, float4x4_t, TransformStateFB, SimpleVehicleStateFB, VehicleModelConfigFB, ModelConfigFB,
    SignalModuleOutputFB, ControlStateFB, SimpleControlStateFB, PedestrianStateFB,
    AgentStateFB, WorldInfoFB, SimStateFB, CameraConfigFB, DistortionParamsFB, NoiseParamsFB, pdDenoiseFilter,
    PostProcessParamsFB, PostProcessMatsFB,
    LiDARConfigFB, LiDARBeamFB, LiDARIntensityParamsFB,
    SensorExtrinsicConfigFB, SensorConfigFB, SensorRigConfigFB, StateObjectFB,
    PhaseBulbValuesFB, BulbValues, TonemapCurveFB
)
from pd.internal.fb.generated.python.SensorIntrinsicConfigFB import SensorIntrinsicConfigFB
from pd.internal.fb.generated.python.StateObject import StateObject

T = TypeVar('T')
logger = logging.getLogger(__name__)


def state_to_bytes(state: State) -> bytearray:
    builder = flatbuffers.Builder(65536)
    builder.Finish(SerializeState.serialize(builder, state))
    return builder.Output()


def bytes_to_state(bytes_: bytes) -> State:
    sim_state_fb = SimStateFB.SimStateFB.GetRootAsSimStateFB(bytes_, 0)
    return SerializeState.deserialize(sim_state_fb)


class SerializePostProcessMaterial:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: PostProcessMaterial):
        mat_fb = builder.CreateString(obj.material)
        PostProcessMatsFB.PostProcessMatsFBStart(builder)
        PostProcessMatsFB.PostProcessMatsFBAddMat(builder, mat_fb)
        PostProcessMatsFB.PostProcessMatsFBAddWeight(builder, obj.weight)
        return PostProcessMatsFB.PostProcessMatsFBEnd(builder)

    @staticmethod
    def deserialize(fb: PostProcessMatsFB.PostProcessMatsFB) -> PostProcessMaterial:
        return PostProcessMaterial(
            material=fb.Mat().decode() or None,
            weight=fb.Weight()
        )


class SerializeToneCurve:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: TonemapCurve):
        TonemapCurveFB.TonemapCurveFBStart(builder)
        TonemapCurveFB.TonemapCurveFBAddSlope(builder, obj.slope)
        TonemapCurveFB.TonemapCurveFBAddToe(builder, obj.toe)
        TonemapCurveFB.TonemapCurveFBAddShoulder(builder, obj.shoulder)
        TonemapCurveFB.TonemapCurveFBAddBlackClip(builder, obj.black_clip)
        TonemapCurveFB.TonemapCurveFBAddWhiteClip(builder, obj.white_clip)
        return TonemapCurveFB.TonemapCurveFBEnd(builder)

    @staticmethod
    def deserialize(fb: TonemapCurveFB.TonemapCurveFB) -> TonemapCurve:
        return TonemapCurve(
            slope=fb.Slope(),
            toe=fb.Toe(),
            shoulder=fb.Shoulder(),
            black_clip=fb.BlackClip(),
            white_clip=fb.WhiteClip()
        )


class SerializePostProcessParams:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: PostProcessParams):
        metering_mask_fb = builder.CreateString(obj.exposure_metering_mask) if obj.exposure_metering_mask else None
        exposure_compensation_curve_fb = builder.CreateString(obj.exposure_compensation_curve) if obj.exposure_compensation_curve else None
        tone_curve_fb = SerializeToneCurve.serialize(builder, obj.tone_curve) \
            if obj.tone_curve else None

        PostProcessParamsFB.PostProcessParamsFBStart(builder)
        PostProcessParamsFB.PostProcessParamsFBAddExposureCompensation(builder, obj.exposure_compensation)
        PostProcessParamsFB.PostProcessParamsFBAddExposureSpeedUp(builder, obj.exposure_speed_up)
        PostProcessParamsFB.PostProcessParamsFBAddExposureSpeedDown(builder, obj.exposure_speed_down)
        PostProcessParamsFB.PostProcessParamsFBAddExposureMinEv100(builder, obj.exposure_min_ev100)
        PostProcessParamsFB.PostProcessParamsFBAddExposureMaxEv100(builder, obj.exposure_max_ev100)
        if obj.exposure_compensation_curve:
            PostProcessParamsFB.PostProcessParamsFBAddExposureCompensationCurve(builder, exposure_compensation_curve_fb)
        if obj.exposure_metering_mask:
            PostProcessParamsFB.PostProcessParamsFBAddExposureMeteringMask(builder, metering_mask_fb)
        PostProcessParamsFB.PostProcessParamsFBAddMotionBlurAmount(builder, obj.motion_blur_amount)
        PostProcessParamsFB.PostProcessParamsFBAddMotionBlurMax(builder, obj.motion_blur_max)
        PostProcessParamsFB.PostProcessParamsFBAddDofFocalDistance(builder, obj.dof_focal_distance)
        PostProcessParamsFB.PostProcessParamsFBAddDofDepthBlurAmount(builder, obj.dof_depth_blur_amount)
        PostProcessParamsFB.PostProcessParamsFBAddDofDepthBlurRadius(builder, obj.dof_depth_blur_radius)
        PostProcessParamsFB.PostProcessParamsFBAddVignetteIntensity(builder, obj.vignette_intensity)
        if obj.tone_curve:
              PostProcessParamsFB.PostProcessParamsFBAddTonemapCurve(
                builder,
                tone_curve_fb
            )
        return PostProcessParamsFB.PostProcessParamsFBEnd(builder)

    @staticmethod
    def deserialize(fb: PostProcessParamsFB.PostProcessParamsFB) -> PostProcessParams:
        post_process_params = PostProcessParams(
            exposure_compensation=fb.ExposureCompensation(),
            exposure_speed_up=fb.ExposureSpeedUp(),
            exposure_speed_down=fb.ExposureSpeedDown(),
            exposure_min_ev100=fb.ExposureMinEv100(),
            exposure_max_ev100=fb.ExposureMaxEv100(),
            exposure_compensation_curve=fb.ExposureCompensationCurve().decode() or None,
            exposure_metering_mask=fb.ExposureMeteringMask().decode() or None,
            motion_blur_amount=fb.MotionBlurAmount(),
            motion_blur_max=fb.MotionBlurMax(),
            dof_focal_distance=fb.DofFocalDistance(),
            dof_depth_blur_amount=fb.DofDepthBlurAmount(),
            dof_depth_blur_radius=fb.DofDepthBlurRadius(),
            vignette_intensity=fb.VignetteIntensity()
        )
        tone_curve_fb = fb.TonemapCurve()
        if tone_curve_fb:
            post_process_params.tone_curve = SerializeToneCurve.deserialize(tone_curve_fb)
        return post_process_params


class SerializeNoiseParams:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: NoiseParams):
        denoise_filter_lookup = {
            DenoiseFilter.AverageFilter: pdDenoiseFilter.pdDenoiseFilter.AverageFilter,
            DenoiseFilter.MedianFilter: pdDenoiseFilter.pdDenoiseFilter.MedianFilter,
            DenoiseFilter.FastMedianFilter: pdDenoiseFilter.pdDenoiseFilter.FastMedianFilter,
            DenoiseFilter.BilateralFilter: pdDenoiseFilter.pdDenoiseFilter.BilateralFilter,
        }
        return NoiseParamsFB.CreateNoiseParamsFB(
            builder=builder,
            enableBayer=obj.enable_bayer,
            enableGaussNoise=obj.enable_gauss_noise,
            enablePoissonNoise=obj.enable_poisson_noise,
            enableDenoise=obj.enable_denoise,
            gaussNoiseSigma=obj.gauss_noise_sigma,
            poissonNoiseLambda=obj.poisson_noise_lambda,
            denoiseFilter=denoise_filter_lookup[obj.denoise_filter],
            denoiseFilterSize=obj.denoise_filter_size,
            bilateralSigmaD=obj.bilateral_sigma_d,
            bilateralSigmaR=obj.bilateral_sigma_r,
            enableAutoNoise=obj.enable_auto_noise,
            signalAmount=obj.signal_amount,
            preAmplifierNoise=obj.pre_amplifier_noise,
            postAmplifierNoise=obj.post_amplifier_noise,
            isUsingIso=obj.is_using_iso,
            isoLevel=obj.iso_level,
            enableAutoIso=obj.enable_auto_iso,
            fstop=obj.fstop,
            maxExposureTime=obj.max_exposure_time,
            quantumEfficiency=obj.quantum_efficiency
        )

    @staticmethod
    def deserialize(fb: NoiseParamsFB.NoiseParamsFB) -> NoiseParams:
        denoise_filter_lookup = {
            pdDenoiseFilter.pdDenoiseFilter.AverageFilter: DenoiseFilter.AverageFilter,
            pdDenoiseFilter.pdDenoiseFilter.MedianFilter: DenoiseFilter.MedianFilter,
            pdDenoiseFilter.pdDenoiseFilter.FastMedianFilter: DenoiseFilter.FastMedianFilter,
            pdDenoiseFilter.pdDenoiseFilter.BilateralFilter: DenoiseFilter.BilateralFilter,
        }
        return NoiseParams(
            enable_bayer=fb.EnableBayer(),
            enable_gauss_noise=fb.EnableGaussNoise(),
            enable_poisson_noise=fb.EnablePoissonNoise(),
            enable_denoise=fb.EnableDenoise(),
            gauss_noise_sigma=fb.GaussNoiseSigma(),
            poisson_noise_lambda=fb.PoissonNoiseLambda(),
            denoise_filter=denoise_filter_lookup[fb.DenoiseFilter()],
            denoise_filter_size=fb.DenoiseFilterSize(),
            bilateral_sigma_d=fb.BilateralSigmaD(),
            bilateral_sigma_r=fb.BilateralSigmaR(),
            enable_auto_noise=fb.EnableAutoNoise(),
            signal_amount=fb.SignalAmount(),
            pre_amplifier_noise=fb.PreAmplifierNoise(),
            post_amplifier_noise=fb.PostAmplifierNoise(),
            is_using_iso=fb.IsUsingIso(),
            iso_level=fb.IsoLevel(),
            enable_auto_iso=fb.EnableAutoIso(),
            fstop=fb.Fstop(),
            max_exposure_time=fb.MaxExposureTime(),
            quantum_efficiency=fb.QuantumEfficiency()
        )


class SerializeDistortionParams:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: DistortionParams):
        return DistortionParamsFB.CreateDistortionParamsFB(
            builder=builder,
            k1=obj.k1,
            k2=obj.k2,
            k3=obj.k3,
            k4=obj.k4,
            k5=obj.k5,
            k6=obj.k6,
            p1=obj.p1,
            p2=obj.p2,
            skew=obj.skew,
            isFisheye=obj.is_fisheye,
            fx=obj.fx,
            fy=obj.fy,
            cx=obj.cx,
            cy=obj.cy
        )

    @staticmethod
    def deserialize(fb: DistortionParamsFB.DistortionParamsFB) -> DistortionParams:
        return DistortionParams(
            k1=fb.K1(),
            k2=fb.K2(),
            k3=fb.K3(),
            k4=fb.K4(),
            k5=fb.K5(),
            k6=fb.K6(),
            p1=fb.P1(),
            p2=fb.P2(),
            skew=fb.Skew(),
            is_fisheye=fb.IsFisheye(),
            fx=fb.Fx(),
            fy=fb.Fy(),
            cx=fb.Cx(),
            cy=fb.Cy()
        )


class SerializeCameraSensor:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: CameraSensor):
        lut_fb = builder.CreateString(obj.lut) if obj.lut else None
        distortion_lookup_table_fb = builder.CreateString(obj.distortion_lookup_table) \
            if obj.distortion_lookup_table else None
        post_process_params_fb = SerializePostProcessParams.serialize(builder, obj.post_process_params) \
            if obj.post_process_params else None
        post_mats_vec_fb = None
        if obj.post_process_materials:
            post_mats_fb_list = []
            for material in obj.post_process_materials:
                post_mats_fb_list.append(SerializePostProcessMaterial.serialize(builder, material))
            CameraConfigFB.CameraConfigFBStartPostProcessMatsVector(builder, len(post_mats_fb_list))
            for post_mat_fb in reversed(post_mats_fb_list):
                builder.PrependUOffsetTRelative(post_mat_fb)
            post_mats_vec_fb = builder.EndVector(len(post_mats_fb_list))

        CameraConfigFB.CameraConfigFBStart(builder)

        CameraConfigFB.CameraConfigFBAddWidth(builder, obj.width)
        CameraConfigFB.CameraConfigFBAddHeight(builder, obj.height)
        CameraConfigFB.CameraConfigFBAddFov(builder, obj.field_of_view_degrees)
        CameraConfigFB.CameraConfigFBAddSupersample(builder, obj.supersample)
        CameraConfigFB.CameraConfigFBAddCaptureRgb(builder, obj.capture_rgb)
        CameraConfigFB.CameraConfigFBAddCaptureDepth(builder, obj.capture_depth)
        CameraConfigFB.CameraConfigFBAddCaptureNormals(builder, obj.capture_normals)
        CameraConfigFB.CameraConfigFBAddCaptureSegmentation(builder, obj.capture_segmentation)
        CameraConfigFB.CameraConfigFBAddCaptureInstances(builder, obj.capture_instances)
        CameraConfigFB.CameraConfigFBAddCaptureMotionvectors(builder, obj.capture_motionvectors)
        CameraConfigFB.CameraConfigFBAddCaptureBackwardmotionvectors(builder, obj.capture_backwardmotionvectors)
        CameraConfigFB.CameraConfigFBAddCaptureBasecolor(builder, obj.capture_basecolor)
        CameraConfigFB.CameraConfigFBAddCaptureProperties(builder, obj.capture_properties)
        CameraConfigFB.CameraConfigFBAddEnableStreaming(builder, obj.enable_streaming)
        CameraConfigFB.CameraConfigFBAddFisheyeModel(builder, obj.fisheye_model)
        if distortion_lookup_table_fb:
            CameraConfigFB.CameraConfigFBAddDistortionLookupTable(builder, distortion_lookup_table_fb)
        CameraConfigFB.CameraConfigFBAddTimeOffset(builder, obj.time_offset)
        if lut_fb:
            CameraConfigFB.CameraConfigFBAddLut(builder, lut_fb)
        CameraConfigFB.CameraConfigFBAddLutWeight(builder, obj.lut_weight)
        CameraConfigFB.CameraConfigFBAddTransmitGray(builder, obj.transmit_gray)

        if obj.distortion_params:
            CameraConfigFB.CameraConfigFBAddDistortionParams(
                builder,
                SerializeDistortionParams.serialize(builder, obj.distortion_params)
            )
        if obj.noise_params:
            CameraConfigFB.CameraConfigFBAddNoiseParams(
                builder,
                SerializeNoiseParams.serialize(builder, obj.noise_params)
            )
        if post_process_params_fb:
            CameraConfigFB.CameraConfigFBAddPostProcessParams(builder, post_process_params_fb)
        if post_mats_vec_fb:
            CameraConfigFB.CameraConfigFBAddPostProcessMats(builder, post_mats_vec_fb)

        return CameraConfigFB.CameraConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: CameraConfigFB.CameraConfigFB) -> CameraSensor:
        camera = CameraSensor(
            name='',  # filled in by SerializeSensor
            pose=np.empty((4, 4)),  # filled in by SerializeSensor
            width=fb.Width(),
            height=fb.Height(),
            field_of_view_degrees=fb.Fov(),
            supersample=fb.Supersample(),
            capture_rgb=bool(fb.CaptureRgb()),
            capture_depth=bool(fb.CaptureDepth()),
            capture_normals=bool(fb.CaptureNormals()),
            capture_segmentation=bool(fb.CaptureSegmentation()),
            capture_instances=bool(fb.CaptureInstances()),
            capture_motionvectors=bool(fb.CaptureMotionvectors()),
            capture_backwardmotionvectors=bool(fb.CaptureBackwardmotionvectors()),
            capture_basecolor=bool(fb.CaptureBasecolor()),
            capture_properties=bool(fb.CaptureProperties()),
            enable_streaming=bool(fb.EnableStreaming()),
            lut=fb.Lut().decode() or None,
            lut_weight=fb.LutWeight(),
            transmit_gray=fb.TransmitGray(),
            fisheye_model=fb.FisheyeModel(),
            distortion_lookup_table=fb.DistortionLookupTable().decode() or None,
            time_offset=fb.TimeOffset()
        )
        distortion_params_fb = fb.DistortionParams()
        if distortion_params_fb:
            camera.distortion_params = SerializeDistortionParams.deserialize(distortion_params_fb)
        noise_params_fb = fb.NoiseParams()
        if noise_params_fb:
            camera.noise_params = SerializeNoiseParams.deserialize(noise_params_fb)
        post_process_params_fb = fb.PostProcessParams()
        if post_process_params_fb:
            camera.post_process_params = SerializePostProcessParams.deserialize(post_process_params_fb)
        for i in range(fb.PostProcessMatsLength()):
            post_process_mat_fb = fb.PostProcessMats(i)
            camera.post_process_materials.append(SerializePostProcessMaterial.deserialize(post_process_mat_fb))
        return camera


class SerializeSensor:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: Sensor):
        if isinstance(obj, CameraSensor):
            intrinsic_fb = SerializeCameraSensor.serialize(builder, obj)
            intrinsic_type_fb = SensorIntrinsicConfigFB.CameraConfigFB
        elif isinstance(obj, LiDARSensor):
            intrinsic_fb = SerializeLiDARSensor.serialize(builder, obj)
            intrinsic_type_fb = SensorIntrinsicConfigFB.LiDARConfigFB
        else:
            raise TypeError("Unsupported sensor type: ", str(type(obj)))

        attach_socket_fb = builder.CreateString(obj.attach_socket) if obj.attach_socket else None

        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBStart(builder)
        sensor_to_vehicle_fb = SerializePose.serialize(builder, obj.pose)
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddSensorToVehicle(builder, sensor_to_vehicle_fb)
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddLockToYaw(builder, obj.lock_to_yaw)
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddFollowRotation(builder, obj.follow_rotation)
        if attach_socket_fb:
            SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddAttachSocket(builder, attach_socket_fb)
        extrinsic_fb = SensorExtrinsicConfigFB.SensorExtrinsicConfigFBEnd(builder)
        name_fb = builder.CreateString(obj.name)
        SensorConfigFB.SensorConfigFBStart(builder)
        SensorConfigFB.SensorConfigFBAddDisplayName(builder, name_fb)
        SensorConfigFB.SensorConfigFBAddSensorExtrinsic(builder, extrinsic_fb)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsicType(builder, intrinsic_type_fb)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsic(builder, intrinsic_fb)
        return SensorConfigFB.SensorConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: SensorConfigFB.SensorConfigFB) -> Sensor:
        if fb.SensorIntrinsicType() == SensorIntrinsicConfigFB.CameraConfigFB:
            camera_fb = CameraConfigFB.CameraConfigFB()
            camera_fb.Init(fb.SensorIntrinsic().Bytes, fb.SensorIntrinsic().Pos)
            sensor = SerializeCameraSensor.deserialize(camera_fb)
        elif fb.SensorIntrinsicType() == SensorIntrinsicConfigFB.LiDARConfigFB:
            lidar_fb = LiDARConfigFB.LiDARConfigFB()
            lidar_fb.Init(fb.SensorIntrinsic().Bytes, fb.SensorIntrinsic().Pos)
            sensor = SerializeLiDARSensor.deserialize(lidar_fb)
        else:
            raise TypeError("Unsupported sensor type: ", fb.SensorIntrinsicType())

        sensor.name = fb.DisplayName().decode() or None
        if fb.SensorExtrinsic():
            sensor.pose = SerializePose.deserialize(fb.SensorExtrinsic().SensorToVehicle())
            sensor.lock_to_yaw = fb.SensorExtrinsic().LockToYaw()
            sensor.follow_rotation = fb.SensorExtrinsic().FollowRotation()
            sensor.attach_socket = fb.SensorExtrinsic().AttachSocket().decode() or None
        return sensor


class SerializePose:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: Union[Pose6D, np.ndarray]):
        if isinstance(obj, Pose6D):
            mat = obj.as_transformation_matrix().T
        elif isinstance(obj, np.ndarray):
            if obj.shape != (4, 4):
                raise TypeError("Invalid pose matrix shape: must be 4x4 numpy array")
            mat = obj.T
        else:
            raise TypeError(f"Invalid pose type '{type(obj).__name__}': must be a Pose6D object or 4x4 numpy array")

        return float4x4_t.Createfloat4x4_t(
            builder,
            mat[0, 0], mat[0, 1], mat[0, 2], mat[0, 3],
            mat[1, 0], mat[1, 1], mat[1, 2], mat[1, 3],
            mat[2, 0], mat[2, 1], mat[2, 2], mat[2, 3],
            mat[3, 0], mat[3, 1], mat[3, 2], mat[3, 3]
        )

    @staticmethod
    def deserialize(fb: float4x4_t.float4x4_t) -> np.ndarray:
        # We purposefully deserialize to ndarray and not Pose6D
        # because there is no guarantee that the matrix obeys the
        # constraints of a valid transformation matrix.
        # In fact, due to floating point errors introduced by flatbuffers,
        # a valid transformation matrix deserializes to an invalid matrix
        mat = np.array([
            [fb.M00(), fb.M01(), fb.M02(), fb.M03()],
            [fb.M10(), fb.M11(), fb.M12(), fb.M13()],
            [fb.M20(), fb.M21(), fb.M22(), fb.M23()],
            [fb.M30(), fb.M31(), fb.M32(), fb.M33()],
        ], dtype=np.float32).T
        return mat


class SerializeLiDARBeam:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: LiDARBeam):
        LiDARBeamFB.LiDARBeamFBStart(builder)
        LiDARBeamFB.LiDARBeamFBAddId(builder, obj.id)
        LiDARBeamFB.LiDARBeamFBAddAzimuth(builder, obj.azimuth)
        LiDARBeamFB.LiDARBeamFBAddElevation(builder, obj.elevation)
        return LiDARBeamFB.LiDARBeamFBEnd(builder)

    @staticmethod
    def deserialize(fb: LiDARBeamFB.LiDARBeamFB) -> LiDARBeam:
        return LiDARBeam(
            id=fb.Id(),
            azimuth=fb.Azimuth(),
            elevation=fb.Elevation()
        )


class SerializeLiDARIntensityParams:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: LiDARIntensityParams):
        LiDARIntensityParamsFB.LiDARIntensityParamsFBStart(builder)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddRetroRangeNoiseStddev(builder, obj.retro_range_noise_stddev)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddRetroreflectionNoiseMean(builder, obj.retroreflection_noise_mean)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddRetroreflectionNoiseStddev(builder, obj.retroreflection_noise_stddev)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddMaxAttenuationDistance(builder, obj.max_attenuation_distance_metres)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddRetroIntensityEnhance(builder, obj.retro_intensity_enhance)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddIntensitySpecularScale(builder, obj.intensity_specular_scale)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddIntensityRoughnessScale(builder, obj.intensity_roughness_scale)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddBeamIntensity(builder, obj.beam_intensity)
        albedo_weights_fb = float3_t.Createfloat3_t(builder, *obj.albedo_weights)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddAlbedoWeights(builder, albedo_weights_fb)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddMaxAlbedo(builder, obj.max_albedo)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddStrongRetroIntensityEnhance(builder, obj.strong_retro_intensity_enhance)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddIntensityMetallicScale(builder, obj.intensity_metallic_scale)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddEmissiveGate(builder, obj.emissive_gate)
        LiDARIntensityParamsFB.LiDARIntensityParamsFBAddMaxEmissiveRate(builder, obj.max_emissive_rate)
        return LiDARIntensityParamsFB.LiDARIntensityParamsFBEnd(builder)

    @staticmethod
    def deserialize(fb: LiDARIntensityParamsFB.LiDARIntensityParamsFB) -> LiDARIntensityParams:
        albedo_weights = (fb.AlbedoWeights().X(), fb.AlbedoWeights().Y(), fb.AlbedoWeights().Z()) \
            if fb.AlbedoWeights() else (0., 0., 0.)
        return LiDARIntensityParams(
            retro_range_noise_stddev=fb.RetroRangeNoiseStddev(),
            retroreflection_noise_mean=fb.RetroreflectionNoiseMean(),
            retroreflection_noise_stddev=fb.RetroreflectionNoiseStddev(),
            max_attenuation_distance_metres=fb.MaxAttenuationDistance(),
            retro_intensity_enhance=fb.RetroIntensityEnhance(),
            intensity_specular_scale=fb.IntensitySpecularScale(),
            intensity_roughness_scale=fb.IntensityRoughnessScale(),
            beam_intensity=fb.BeamIntensity(),
            albedo_weights=albedo_weights,
            max_albedo=fb.MaxAlbedo(),
            strong_retro_intensity_enhance=fb.StrongRetroIntensityEnhance(),
            intensity_metallic_scale=fb.IntensityMetallicScale(),
            emissive_gate=fb.EmissiveGate(),
            max_emissive_rate=fb.MaxEmissiveRate()
        )


class SerializeLiDARSensor:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: LiDARSensor):
        beam_data_vec_fb = None
        if obj.beam_data:
            beam_data_fb_list = []
            for beam in obj.beam_data:
                beam_data_fb_list.append(SerializeLiDARBeam.serialize(builder, beam))
            LiDARConfigFB.LiDARConfigFBStartBeamDataVector(builder, len(beam_data_fb_list))
            for beam_data_fb in reversed(beam_data_fb_list):
                builder.PrependUOffsetTRelative(beam_data_fb)
            beam_data_vec_fb = builder.EndVector(len(beam_data_fb_list))
        intensity_params_fb = None
        if obj.intensity_params:
            intensity_params_fb = SerializeLiDARIntensityParams.serialize(builder, obj.intensity_params)
        pattern_fb = builder.CreateString(obj.pattern) if obj.pattern else None
        LiDARConfigFB.LiDARConfigFBStart(builder)
        LiDARConfigFB.LiDARConfigFBAddSampleRate(builder, obj.sample_rate)
        LiDARConfigFB.LiDARConfigFBAddRotationRate(builder, obj.rotation_rate)
        LiDARConfigFB.LiDARConfigFBAddAzimuthMin(builder, obj.azimuth_min)
        LiDARConfigFB.LiDARConfigFBAddAzimuthMax(builder, obj.azimuth_max)
        LiDARConfigFB.LiDARConfigFBAddElevationDelta(builder, obj.elevation_delta)
        LiDARConfigFB.LiDARConfigFBAddCaptureRgb(builder, obj.capture_rgb)
        LiDARConfigFB.LiDARConfigFBAddCaptureDepth(builder, obj.capture_depth)
        LiDARConfigFB.LiDARConfigFBAddCaptureNormals(builder, obj.capture_normals)
        LiDARConfigFB.LiDARConfigFBAddCaptureSegmentation(builder, obj.capture_segmentation)
        LiDARConfigFB.LiDARConfigFBAddCaptureInstances(builder, obj.capture_instances)
        LiDARConfigFB.LiDARConfigFBAddCaptureMotionvectors(builder, obj.capture_motionvectors)
        LiDARConfigFB.LiDARConfigFBAddMinimumRangeCutoff(builder, obj.minimum_range_cutoff)
        LiDARConfigFB.LiDARConfigFBAddMaximumRangeCutoff(builder, obj.maximum_range_cutoff)
        LiDARConfigFB.LiDARConfigFBAddMinimumCutoffProb(builder, obj.minimum_cutoff_prob)
        LiDARConfigFB.LiDARConfigFBAddMaximumCutoffProb(builder, obj.maximum_cutoff_prob)
        LiDARConfigFB.LiDARConfigFBAddMinimumOffset(builder, obj.minimum_offset)
        LiDARConfigFB.LiDARConfigFBAddMaximumOffset(builder, obj.maximum_offset)
        LiDARConfigFB.LiDARConfigFBAddMinimumNoise(builder, obj.minimum_noise)
        LiDARConfigFB.LiDARConfigFBAddRangeNoiseMean(builder, obj.range_noise_mean)
        LiDARConfigFB.LiDARConfigFBAddRangeNoiseStddev(builder, obj.range_noise_stddev)
        LiDARConfigFB.LiDARConfigFBAddTimeOffset(builder, obj.time_offset_ms)
        if beam_data_vec_fb:
            LiDARConfigFB.LiDARConfigFBAddBeamData(builder, beam_data_vec_fb)
        if intensity_params_fb:
            LiDARConfigFB.LiDARConfigFBAddIntensityParams(builder, intensity_params_fb)
        if pattern_fb:
            LiDARConfigFB.LiDARConfigFBAddPattern(builder, pattern_fb)

        return CameraConfigFB.CameraConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: LiDARConfigFB.LiDARConfigFB) -> LiDARSensor:
        lidar = LiDARSensor(
            name='',  # filled in by SerializeSensor
            pose=np.empty((4, 4)),  # filled in by SerializeSensor
            sample_rate=fb.SampleRate(),
            rotation_rate=fb.RotationRate(),
            azimuth_min=fb.AzimuthMin(),
            azimuth_max=fb.AzimuthMax(),
            elevation_delta=fb.ElevationDelta(),
            capture_rgb=bool(fb.CaptureRgb()),
            capture_depth=bool(fb.CaptureDepth()),
            capture_normals=bool(fb.CaptureNormals()),
            capture_segmentation=bool(fb.CaptureSegmentation()),
            capture_instances=bool(fb.CaptureInstances()),
            capture_motionvectors=bool(fb.CaptureMotionvectors()),
            minimum_range_cutoff=fb.MinimumRangeCutoff(),
            maximum_range_cutoff=fb.MaximumRangeCutoff(),
            minimum_cutoff_prob=fb.MinimumCutoffProb(),
            maximum_cutoff_prob=fb.MaximumCutoffProb(),
            minimum_offset=fb.MinimumOffset(),
            maximum_offset=fb.MaximumOffset(),
            minimum_noise=fb.MinimumNoise(),
            range_noise_mean=fb.RangeNoiseMean(),
            range_noise_stddev=fb.RangeNoiseStddev(),
            pattern=fb.Pattern().decode() or None,
            time_offset_ms=fb.TimeOffset(),
        )
        for i in range(fb.BeamDataLength()):
            beam_fb = fb.BeamData(i)
            lidar.beam_data.append(SerializeLiDARBeam.deserialize(beam_fb))
        if fb.IntensityParams():
            lidar.intensity_params = SerializeLiDARIntensityParams.deserialize(fb.IntensityParams())
        return lidar


class SerializePhaseBulbValue:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: PhaseBulbValue):
        PhaseBulbValuesFB.PhaseBulbValuesFBStart(builder)
        PhaseBulbValuesFB.PhaseBulbValuesFBAddPhase(builder, obj.phase)
        PhaseBulbValuesFB.PhaseBulbValuesFBAddValue(
            builder,
            BulbValues.CreateBulbValues(
                builder=builder,
                red=obj.red,
                yellow=obj.yellow,
                green=obj.green
            )
        )
        PhaseBulbValuesFB.PhaseBulbValuesFBAddLogicalState(builder, obj.logical_state.value)
        return PhaseBulbValuesFB.PhaseBulbValuesFBEnd(builder)

    @staticmethod
    def deserialize(fb: PhaseBulbValuesFB.PhaseBulbValuesFB) -> PhaseBulbValue:
        return PhaseBulbValue(
            phase=fb.Phase(),
            red=fb.Value().Red() if fb.Value() else 0.0,
            yellow=fb.Value().Yellow() if fb.Value() else 0.0,
            green=fb.Value().Green() if fb.Value() else 0.0,
            logical_state=PhaseBulbLogicalState(fb.LogicalState())
        )


class SerializeWorldInfo:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: WorldInfo):
        location_fb = builder.CreateString(obj.location) if obj.location else None
        tod_fb = builder.CreateString(obj.time_of_day) if obj.time_of_day else None
        performance_type = pdPerformanceFeature.PerformanceMode \
            if obj.performance_mode == PerformanceMode.Performance \
            else pdPerformanceFeature.HighFidelityMode

        WorldInfoFB.WorldInfoFBStart(builder)
        if location_fb:
            WorldInfoFB.WorldInfoFBAddName(builder, location_fb)
        if tod_fb:
            WorldInfoFB.WorldInfoFBAddTimeOfDay(builder, tod_fb)
        WorldInfoFB.WorldInfoFBAddWetness(builder, obj.wetness)
        WorldInfoFB.WorldInfoFBAddRainIntensity(builder, obj.rain_intensity)
        WorldInfoFB.WorldInfoFBAddStreetLights(builder, obj.street_lights)
        WorldInfoFB.WorldInfoFBAddFogIntensity(builder, obj.fog_intensity)
        WorldInfoFB.WorldInfoFBAddEnableHeadlights(builder, obj.enable_headlights)
        WorldInfoFB.WorldInfoFBAddPerformanceFeature(builder, performance_type)
        WorldInfoFB.WorldInfoFBAddAntiAliasing(builder, obj.anti_aliasing)
        return WorldInfoFB.WorldInfoFBEnd(builder)

    @staticmethod
    def deserialize(fb: WorldInfoFB.WorldInfoFB) -> WorldInfo:
        performance_mode = PerformanceMode.Performance \
            if fb.PerformanceFeature() == pdPerformanceFeature.PerformanceMode else PerformanceMode.HighFidelity
        return WorldInfo(
            location=fb.Name().decode() or None,
            time_of_day=fb.TimeOfDay().decode() or None,
            wetness=fb.Wetness(),
            rain_intensity=fb.RainIntensity(),
            street_lights=fb.StreetLights(),
            fog_intensity=fb.FogIntensity(),
            enable_headlights=fb.EnableHeadlights(),
            performance_mode=performance_mode,
            anti_aliasing=fb.AntiAliasing()
        )


class SerializeState:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: State):
        # Agents
        agents_fb = []
        for agent in obj.agents:
            if not isinstance(agent, (VehicleAgent, ModelAgent, SensorAgent, SignalAgent)):
                raise TypeError(f"Unsupported agent type: {type(agent).__name__}")
            agents_fb.append(SerializeAgent.serialize(builder, agent))
        SimStateFB.SimStateFBStartAgentsVector(builder, len(agents_fb))
        for agent_fb in reversed(agents_fb):
            builder.PrependUOffsetTRelative(agent_fb)
        agents_vec_fb = builder.EndVector(len(agents_fb))

        # World info
        world_info_fb = SerializeWorldInfo.serialize(builder, obj.world_info)

        SimStateFB.SimStateFBStart(builder)
        SimStateFB.SimStateFBAddWorldInfo(builder, world_info_fb)
        SimStateFB.SimStateFBAddAgents(builder, agents_vec_fb)
        SimStateFB.SimStateFBAddTime(builder, obj.simulation_time_sec)
        SimStateFB.SimStateFBAddCapture(builder, obj.capture)
        sim_state = SimStateFB.SimStateFBEnd(builder)
        return sim_state

    @staticmethod
    def deserialize(fb: SimStateFB.SimStateFB) -> State:
        agents = []
        for i in range(fb.AgentsLength()):
            deserialized_agent = SerializeAgent.deserialize(fb.Agents(i))
            if deserialized_agent:
                agents.append(deserialized_agent)
        world_info = SerializeWorldInfo.deserialize(fb.WorldInfo()) if fb.WorldInfo() else None
        return State(
            simulation_time_sec=fb.Time(),
            world_info=world_info,
            agents=agents,
            capture=fb.Capture()
        )


class SerializeAgent:
    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: Union[VehicleAgent, ModelAgent, SensorAgent, SignalAgent]):
        states_data = []

        if isinstance(obj, (VehicleAgent, ModelAgent, SensorAgent)):
            pose_matrix = obj.pose.as_transformation_matrix() if isinstance(obj.pose, Pose6D) else obj.pose
            states_data.append(
                SerializeTransformState.TransformStateData(
                    pose=pose_matrix,
                    velocity=obj.velocity,
                    angular_velocity=obj.angular_velocity
                )
            )

        if isinstance(obj, (VehicleAgent, ModelAgent, SensorAgent)) and obj.sensors:
            states_data.append(
                SerializeSensorRig.SensorRigData(obj.sensors)
            )

        if isinstance(obj, VehicleAgent):
            states_data.append(
                SerializeVehicleModelConfig.VehicleModelConfigData(
                    vehicle_type=obj.vehicle_type,
                    vehicle_color=obj.vehicle_color,
                    vehicle_accessory=obj.vehicle_accessory,
                    vehicle_wear=obj.vehicle_wear,
                    wheel_type=obj.wheel_type,
                    vehicle_actor=obj.vehicle_actor,
                    lock_to_ground=obj.lock_to_ground,
                    ground_offset=obj.ground_offset,
                    wheel_combo=list(obj.wheel_combo),
                    wheel_combo_style=list(obj.wheel_combo_style),
                    accessories=list(obj.accessories),
                    occupants=list(obj.occupants)
                )
            )
            states_data.append(
                SerializeControlState.ControlStateData(
                    indicator_state=obj.indicator_state
                )
            )
            wheels_to_world = []
            if obj.wheel_poses is not None:
                object_to_world = pose_matrix
                for wheel_pose in obj.wheel_poses:
                    wheel_to_object = wheel_pose.as_transformation_matrix() \
                        if isinstance(wheel_pose, Pose6D) else wheel_pose
                    wheels_to_world.append(np.matmul(object_to_world, wheel_to_object))
            states_data.append(
                SerializeSimpleVehicleState.SimpleVehicleStateData(
                    wheel_to_world=wheels_to_world,
                    emergency_lights_on=False,
                    brake_light_on=obj.brake_light_on
                )
            )
            if not obj.is_parked:
                states_data.append(
                    SerializeSimpleControlState.SimpleControlStateData()
                )
        elif isinstance(obj, SensorAgent):
            pass
        elif isinstance(obj, ModelAgent):
            states_data.append(
                SerializeModelConfig.ModelConfigData(
                    asset_name=obj.asset_name,
                    lock_to_ground=obj.lock_to_ground,
                    ground_offset=obj.ground_offset
                )
            )
            if obj.pedestrian_animation_data is not None:
                states_data.append(
                    SerializePedestrianState.PedestrianStateData(
                        animation_data=obj.pedestrian_animation_data
                    )
                )
        elif isinstance(obj, SignalAgent):
            states_data.append(
                SerializeSignalModuleOutput.SignalModuleOutputData(
                    elapsed_time=obj.elapsed_time,
                    phase_bulb_values=obj.phase_bulb_values
                )
            )
        else:
            raise TypeError(f"Unsupported agent type: {type(obj).__name__}")

        return SerializeAgentState.serialize(builder, SerializeAgentState.AgentStateData(
            id=obj.id,
            states_data=states_data
        ))

    @staticmethod
    def deserialize(fb: AgentStateFB.AgentStateFB) -> Optional[Union[VehicleAgent, ModelAgent, SensorAgent]]:
        agent_state_data = SerializeAgentState.deserialize(fb)

        def find_state_data(state_type: Type[T]) -> T:
            try:
                state_data = next(d for d in agent_state_data.states_data if isinstance(d, state_type))
                return state_data
            except StopIteration:
                return None

        sensor_rig_data = find_state_data(SerializeSensorRig.SensorRigData)
        transform_state_data = find_state_data(SerializeTransformState.TransformStateData)
        model_config_data = find_state_data(SerializeModelConfig.ModelConfigData)
        vehicle_model_config_data = find_state_data(SerializeVehicleModelConfig.VehicleModelConfigData)
        vehicle_state_data = find_state_data(SerializeSimpleVehicleState.SimpleVehicleStateData)
        control_state_data = find_state_data(SerializeControlState.ControlStateData)
        simple_control_state_data = find_state_data(SerializeSimpleControlState.SimpleControlStateData)
        signal_module_output_data = find_state_data(SerializeSignalModuleOutput.SignalModuleOutputData)
        pedestrian_state_data = find_state_data(SerializePedestrianState.PedestrianStateData)

        if vehicle_model_config_data and vehicle_state_data and transform_state_data:
            # This is a vehicle agent
            indicator_state = control_state_data.indicator_state if control_state_data \
                else VehicleIndicatorState.Inactive
            object_to_world = transform_state_data.pose
            wheel_to_object_matrices = []
            for wheel_to_world in vehicle_state_data.wheel_to_world:
                wheel_to_object_matrices.append(np.matmul(np.linalg.inv(object_to_world), wheel_to_world))
            agent = VehicleAgent(
                id=fb.Id(),
                pose=transform_state_data.pose,
                velocity=transform_state_data.velocity,
                vehicle_type=vehicle_model_config_data.vehicle_type,
                vehicle_color=vehicle_model_config_data.vehicle_color,
                vehicle_accessory=vehicle_model_config_data.vehicle_accessory,
                vehicle_wear=vehicle_model_config_data.vehicle_wear,
                vehicle_actor=vehicle_model_config_data.vehicle_actor,
                wheel_type=vehicle_model_config_data.wheel_type,
                wheel_poses=wheel_to_object_matrices,
                lock_to_ground=vehicle_model_config_data.lock_to_ground,
                ground_offset=vehicle_model_config_data.ground_offset,
                wheel_combo=vehicle_model_config_data.wheel_combo,
                wheel_combo_style=vehicle_model_config_data.wheel_combo_style,
                accessories=vehicle_model_config_data.accessories,
                occupants=vehicle_model_config_data.occupants,
                brake_light_on=vehicle_state_data.brake_light_on,
                indicator_state=indicator_state,
                is_parked=simple_control_state_data is None
            )
            agent.angular_velocity = transform_state_data.angular_velocity
        elif model_config_data and transform_state_data:
            # This is a model agent
            agent = ModelAgent(
                id=fb.Id(),
                pose=transform_state_data.pose,
                velocity=transform_state_data.velocity,
                asset_name=model_config_data.asset_name,
                lock_to_ground=model_config_data.lock_to_ground,
                ground_offset=model_config_data.ground_offset
            )
            agent.angular_velocity = transform_state_data.angular_velocity
            if pedestrian_state_data:
                agent.pedestrian_animation_data = pedestrian_state_data.animation_data
        elif transform_state_data:
            # This is a sensor agent
            # Sensors added later below for every agent type
            agent = SensorAgent(
                id=fb.Id(),
                pose=transform_state_data.pose,
                velocity=transform_state_data.velocity
            )
            agent.angular_velocity = transform_state_data.angular_velocity
        elif signal_module_output_data:
            # This is a signal agent
            agent = SignalAgent(
                id=fb.Id(),
                elapsed_time=signal_module_output_data.elapsed_time,
                phase_bulb_values=signal_module_output_data.phase_bulb_values
            )
        else:
            logger.warning(f"Failed to determine Agent type for deserialization: agent id = {fb.Id()}")
            return None

        if sensor_rig_data:
            agent.sensors = sensor_rig_data.sensors

        return agent


#############################
# Serialize StateObjects
#############################

class SerializeAgentState:
    state_object_ids = {
        StateObject.TransformStateFB: 12298431360834646861,
        StateObject.SimpleVehicleStateFB: 12476338340133291318,
        StateObject.VehicleModelConfigFB: 15482515385289015907,
        StateObject.ControlStateFB: 12600429034653655870,
        StateObject.ModelConfigFB: 3870787532367476188,
        StateObject.SensorRigConfigFB: 510337214252732030,
        StateObject.SignalModuleOutputFB: 10246967395465483304,
        StateObject.SimpleControlStateFB: 13564387674721412426,
        StateObject.PedestrianStateFB: 15712700117038221379,
    }

    @dataclass
    class AgentStateData:
        id: int
        states_data: List

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: AgentStateData):
        states_data_fb_list = []
        for state_data in obj.states_data:
            if isinstance(state_data, SerializeSensorRig.SensorRigData):
                states_data_fb_list.append(
                    (StateObject.SensorRigConfigFB, SerializeSensorRig.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeTransformState.TransformStateData):
                states_data_fb_list.append(
                    (StateObject.TransformStateFB, SerializeTransformState.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeModelConfig.ModelConfigData):
                states_data_fb_list.append(
                    (StateObject.ModelConfigFB, SerializeModelConfig.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeVehicleModelConfig.VehicleModelConfigData):
                states_data_fb_list.append(
                    (StateObject.VehicleModelConfigFB, SerializeVehicleModelConfig.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeSimpleVehicleState.SimpleVehicleStateData):
                states_data_fb_list.append(
                    (StateObject.SimpleVehicleStateFB, SerializeSimpleVehicleState.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeControlState.ControlStateData):
                states_data_fb_list.append(
                    (StateObject.ControlStateFB, SerializeControlState.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeSimpleControlState.SimpleControlStateData):
                states_data_fb_list.append(
                    (StateObject.SimpleControlStateFB, SerializeSimpleControlState.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializeSignalModuleOutput.SignalModuleOutputData):
                states_data_fb_list.append(
                    (StateObject.SignalModuleOutputFB, SerializeSignalModuleOutput.serialize(builder, state_data))
                )
            elif isinstance(state_data, SerializePedestrianState.PedestrianStateData):
                states_data_fb_list.append(
                    (StateObject.PedestrianStateFB, SerializePedestrianState.serialize(builder, state_data))
                )
            else:
                raise TypeError("Unknown state data type")

        sorted_states_data_fb_list = sorted(
            states_data_fb_list,
            key=lambda s: SerializeAgentState.state_object_ids[s[0]]
        )
        state_fb_list = []
        for state_type, state_data_fb in sorted_states_data_fb_list:
            state_object_id = SerializeAgentState.state_object_ids[state_type]
            StateObjectFB.StateObjectFBStart(builder)
            StateObjectFB.StateObjectFBAddId(builder, state_object_id)
            StateObjectFB.StateObjectFBAddStateType(builder, state_type)
            StateObjectFB.StateObjectFBAddState(builder, state_data_fb)
            state_fb_list.append(StateObjectFB.StateObjectFBEnd(builder))

        AgentStateFB.AgentStateFBStartStateVector(builder, len(state_fb_list))
        for state_fb in reversed(state_fb_list):
            builder.PrependUOffsetTRelative(state_fb)
        states_vec_fb = builder.EndVector(len(state_fb_list))

        AgentStateFB.AgentStateFBStart(builder)
        AgentStateFB.AgentStateFBAddId(builder, obj.id)
        AgentStateFB.AgentStateFBAddState(builder, states_vec_fb)
        return AgentStateFB.AgentStateFBEnd(builder)

    @staticmethod
    def deserialize(fb: AgentStateFB.AgentStateFB) -> AgentStateData:
        states_data = []
        for i in range(fb.StateLength()):
            state_fb = fb.State(i)
            state_type = state_fb.StateType()
            state_obj_fb = state_fb.State()
            if state_type == StateObject.SensorRigConfigFB:
                sensor_rig_fb = SensorRigConfigFB.SensorRigConfigFB()
                sensor_rig_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeSensorRig.deserialize(sensor_rig_fb))
            elif state_type == StateObject.TransformStateFB:
                transform_state_fb = TransformStateFB.TransformStateFB()
                transform_state_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeTransformState.deserialize(transform_state_fb))
            elif state_type == StateObject.ModelConfigFB:
                model_config_fb = ModelConfigFB.ModelConfigFB()
                model_config_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeModelConfig.deserialize(model_config_fb))
            elif state_type == StateObject.VehicleModelConfigFB:
                vehicle_model_config_fb = VehicleModelConfigFB.VehicleModelConfigFB()
                vehicle_model_config_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeVehicleModelConfig.deserialize(vehicle_model_config_fb))
            elif state_type == StateObject.ControlStateFB:
                simple_control_state_fb = ControlStateFB.ControlStateFB()
                simple_control_state_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeControlState.deserialize(simple_control_state_fb))
            elif state_type == StateObject.SimpleControlStateFB:
                simple_control_state_fb = SimpleControlStateFB.SimpleControlStateFB()
                simple_control_state_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeSimpleControlState.deserialize(simple_control_state_fb))
            elif state_type == StateObject.SimpleVehicleStateFB:
                vehicle_state_fb = SimpleVehicleStateFB.SimpleVehicleStateFB()
                vehicle_state_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeSimpleVehicleState.deserialize(vehicle_state_fb))
            elif state_type == StateObject.SignalModuleOutputFB:
                signal_module_output_fb = SignalModuleOutputFB.SignalModuleOutputFB()
                signal_module_output_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializeSignalModuleOutput.deserialize(signal_module_output_fb))
            elif state_type == StateObject.PedestrianStateFB:
                pedestrian_state_fb = PedestrianStateFB.PedestrianStateFB()
                pedestrian_state_fb.Init(state_obj_fb.Bytes, state_obj_fb.Pos)
                states_data.append(SerializePedestrianState.deserialize(pedestrian_state_fb))
            elif state_type in (
                StateObject.PathDeviationFB,
                StateObject.PlanningInputFB,
                StateObject.VehiclePhysicsConfigFB,
                StateObject.ControlConfigFB,
                StateObject.MotionPlanFB,
                StateObject.LinearMoverConfigFB,
                StateObject.SignalModuleConfigFB,
                StateObject.SignedIntersectionModuleOutputFB,
                StateObject.SignedIntersectionModuleConfigFB,
                StateObject.VehicleEventsFB,
                StateObject.AssetPlacementFB,
                StateObject.NavRouteOutputFB,
                StateObject.RoleOutputFB,
                StateObject.ParkingPlannerOutputFB,
                StateObject.VehicleTrafficControlOutputFB,
                StateObject.VehiclePlannerOutputFB,
                StateObject.TrajectoryOutputFB,
                StateObject.AgentEventsFB,
            ):
                state_type_name = next(k for k, v in StateObject.__dict__.items() if v == state_type)
                logger.warning(f"Skipping deserialization of StateObject not supported/relevant in Step API: "
                               f"'{state_type_name}' ({state_type})")
            else:
                state_type_name = next(k for k, v in StateObject.__dict__.items() if v == state_type)
                raise TypeError(f"Unsupported State type: '{state_type_name}' ({state_type}) for agent id {fb.Id()}")
        return SerializeAgentState.AgentStateData(
            id=fb.Id(),
            states_data=states_data
        )


class SerializeSensorRig:
    @dataclass
    class SensorRigData:
        sensors: List[Sensor]

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: SensorRigData):
        sensors_fb_list = []
        for sensor in obj.sensors:
            sensors_fb_list.append(SerializeSensor.serialize(builder, sensor))
        SensorRigConfigFB.SensorRigConfigFBStartSensorConfigsVector(builder, len(sensors_fb_list))
        for sensor_fb in reversed(sensors_fb_list):
            builder.PrependUOffsetTRelative(sensor_fb)
        sensors_fb = builder.EndVector(len(sensors_fb_list))

        SensorRigConfigFB.SensorRigConfigFBStart(builder)
        SensorRigConfigFB.SensorRigConfigFBAddSensorConfigs(builder, sensors_fb)
        return SensorRigConfigFB.SensorRigConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: SensorRigConfigFB.SensorRigConfigFB) -> SensorRigData:
        sensors = []
        for i in range(fb.SensorConfigsLength()):
            sensor_fb = fb.SensorConfigs(i)
            sensors.append(SerializeSensor.deserialize(sensor_fb))
        return SerializeSensorRig.SensorRigData(sensors=sensors)


class SerializeTransformState:
    @dataclass
    class TransformStateData:
        pose: np.ndarray
        velocity: Tuple[float, float, float]
        angular_velocity: Tuple[float, float, float]

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: TransformStateData):
        TransformStateFB.TransformStateFBStart(builder)
        TransformStateFB.TransformStateFBAddParent(builder, 0)
        object_to_world_fb = SerializePose.serialize(builder, obj.pose)
        TransformStateFB.TransformStateFBAddObjectToWorld(builder, object_to_world_fb)
        velocity_fb = float3_t.Createfloat3_t(builder, *obj.velocity)
        TransformStateFB.TransformStateFBAddVelocity(builder, velocity_fb)
        angular_velocity_fb = float3_t.Createfloat3_t(builder, *obj.angular_velocity)
        TransformStateFB.TransformStateFBAddAngularVelocity(builder, angular_velocity_fb)
        return TransformStateFB.TransformStateFBEnd(builder)

    @staticmethod
    def deserialize(fb: TransformStateFB.TransformStateFB) -> TransformStateData:
        velocity = (fb.Velocity().X(), fb.Velocity().Y(), fb.Velocity().Z()) \
            if fb.Velocity() else (0., 0., 0.)
        angular_velocity = (fb.AngularVelocity().X(), fb.AngularVelocity().Y(), fb.AngularVelocity().Z()) \
            if fb.AngularVelocity() else (0., 0., 0.)
        return SerializeTransformState.TransformStateData(
            pose=SerializePose.deserialize(fb.ObjectToWorld()) if fb.ObjectToWorld() else np.empty((4, 4)),
            velocity=velocity,
            angular_velocity=angular_velocity,
        )


class SerializeModelConfig:
    @dataclass
    class ModelConfigData:
        asset_name: str
        lock_to_ground: bool
        ground_offset: float

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: ModelConfigData):
        asset_name_fb = builder.CreateString(obj.asset_name) if obj.asset_name else None
        ModelConfigFB.ModelConfigFBStart(builder)
        if asset_name_fb:
            ModelConfigFB.ModelConfigFBAddAssetName(builder, asset_name_fb)
        ModelConfigFB.ModelConfigFBAddLockToGround(builder, obj.lock_to_ground)
        ModelConfigFB.ModelConfigFBAddGroundOffset(builder, obj.ground_offset)
        return ModelConfigFB.ModelConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: ModelConfigFB.ModelConfigFB) -> ModelConfigData:
        return SerializeModelConfig.ModelConfigData(
            asset_name=fb.AssetName().decode() or None,
            lock_to_ground=fb.LockToGround(),
            ground_offset=fb.GroundOffset()
        )


class SerializeVehicleModelConfig:
    @dataclass
    class VehicleModelConfigData:
        vehicle_type: str
        vehicle_color: str
        vehicle_accessory: str
        vehicle_wear: float
        wheel_type: str
        vehicle_actor: str
        lock_to_ground: bool
        ground_offset: float
        wheel_combo: List[str]
        wheel_combo_style: List[str]
        accessories: List[str]
        occupants: List[str]

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: VehicleModelConfigData):
        vehicle_type_fb = builder.CreateString(obj.vehicle_type) if obj.vehicle_type else None
        vehicle_color_fb = builder.CreateString(obj.vehicle_color) if obj.vehicle_color else None
        vehicle_accessory_fb = builder.CreateString(obj.vehicle_accessory) if obj.vehicle_accessory else None
        wheel_type_fb = builder.CreateString(obj.wheel_type) if obj.wheel_type else None
        vehicle_actor_fb = builder.CreateString(obj.vehicle_actor) if obj.vehicle_actor else None

        wheel_combo_fb_list = [builder.CreateString(s) for s in obj.wheel_combo]
        VehicleModelConfigFB.VehicleModelConfigFBStartWheelComboVector(builder, len(wheel_combo_fb_list))
        for wheel_combo_fb in reversed(wheel_combo_fb_list):
            builder.PrependUOffsetTRelative(wheel_combo_fb)
        wheel_combo_vec_fb = builder.EndVector(len(wheel_combo_fb_list))

        wheel_combo_style_fb_list = [builder.CreateString(s) for s in obj.wheel_combo_style]
        VehicleModelConfigFB.VehicleModelConfigFBStartWheelComboStyleVector(builder, len(wheel_combo_style_fb_list))
        for wheel_combo_style_fb in reversed(wheel_combo_style_fb_list):
            builder.PrependUOffsetTRelative(wheel_combo_style_fb)
        wheel_combo_style_vec_fb = builder.EndVector(len(wheel_combo_style_fb_list))

        accessories_fb_list = [builder.CreateString(s) for s in obj.accessories]
        VehicleModelConfigFB.VehicleModelConfigFBStartAccessoriesVector(builder, len(accessories_fb_list))
        for accessories_fb in reversed(accessories_fb_list):
            builder.PrependUOffsetTRelative(accessories_fb)
        accessories_vec_fb = builder.EndVector(len(accessories_fb_list))

        occupants_fb_list = [builder.CreateString(s) for s in obj.occupants]
        VehicleModelConfigFB.VehicleModelConfigFBStartOccupantsVector(builder, len(occupants_fb_list))
        for occupants_fb in reversed(occupants_fb_list):
            builder.PrependUOffsetTRelative(occupants_fb)
        occupants_vec_fb = builder.EndVector(len(occupants_fb_list))

        VehicleModelConfigFB.VehicleModelConfigFBStart(builder)
        if vehicle_type_fb:
            VehicleModelConfigFB.VehicleModelConfigFBAddVehicleType(builder, vehicle_type_fb)
        if vehicle_color_fb:
            VehicleModelConfigFB.VehicleModelConfigFBAddVehicleColor(builder, vehicle_color_fb)
        if wheel_type_fb:
            VehicleModelConfigFB.VehicleModelConfigFBAddWheelType(builder, wheel_type_fb)
        if vehicle_accessory_fb:
            VehicleModelConfigFB.VehicleModelConfigFBAddVehicleAccessory(builder, vehicle_accessory_fb)
        if vehicle_actor_fb:
            VehicleModelConfigFB.VehicleModelConfigFBAddVehicleActor(builder, vehicle_actor_fb)
        VehicleModelConfigFB.VehicleModelConfigFBAddVehicleWear(builder, obj.vehicle_wear)
        VehicleModelConfigFB.VehicleModelConfigFBAddLockToGround(builder, obj.lock_to_ground)
        VehicleModelConfigFB.VehicleModelConfigFBAddGroundOffset(builder, obj.ground_offset)
        VehicleModelConfigFB.VehicleModelConfigFBAddWheelCombo(builder, wheel_combo_vec_fb)
        VehicleModelConfigFB.VehicleModelConfigFBAddWheelComboStyle(builder, wheel_combo_style_vec_fb)
        VehicleModelConfigFB.VehicleModelConfigFBAddAccessories(builder, accessories_vec_fb)
        VehicleModelConfigFB.VehicleModelConfigFBAddOccupants(builder, occupants_vec_fb)
        return VehicleModelConfigFB.VehicleModelConfigFBEnd(builder)

    @staticmethod
    def deserialize(fb: VehicleModelConfigFB.VehicleModelConfigFB) -> VehicleModelConfigData:
        vehicle_model_config = SerializeVehicleModelConfig.VehicleModelConfigData(
            vehicle_type=fb.VehicleType().decode() or None,
            vehicle_color=fb.VehicleColor().decode() or None,
            vehicle_accessory=fb.VehicleAccessory().decode() or None,
            vehicle_wear=fb.VehicleWear(),
            wheel_type=fb.WheelType().decode() or None,
            vehicle_actor=fb.VehicleActor().decode() or None,
            lock_to_ground=fb.LockToGround(),
            ground_offset=fb.GroundOffset(),
            wheel_combo=[],
            wheel_combo_style=[],
            accessories=[],
            occupants=[],
        )
        for i in range(fb.WheelComboLength()):
            wheel_combo_fb = fb.WheelCombo(i)
            vehicle_model_config.wheel_combo.append(wheel_combo_fb.decode())
        for i in range(fb.WheelComboStyleLength()):
            wheel_combo_style_fb = fb.WheelComboStyle(i)
            vehicle_model_config.wheel_combo_style.append(wheel_combo_style_fb.decode())
        for i in range(fb.AccessoriesLength()):
            accessories_fb = fb.Accessories(i)
            vehicle_model_config.accessories.append(accessories_fb.decode())
        for i in range(fb.OccupantsLength()):
            occupants_fb = fb.Occupants(i)
            vehicle_model_config.occupants.append(occupants_fb.decode())
        return vehicle_model_config


class SerializeSimpleVehicleState:
    @dataclass
    class SimpleVehicleStateData:
        wheel_to_world: List[np.ndarray]
        emergency_lights_on: bool
        brake_light_on: bool

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: SimpleVehicleStateData):
        wheels_vec_fb = None
        if obj.wheel_to_world:
            SimpleVehicleStateFB.SimpleVehicleStateFBStartWheelToWorldVector(builder, len(obj.wheel_to_world))
            for wheel_to_world in reversed(obj.wheel_to_world):
                SerializePose.serialize(builder, wheel_to_world)
            wheels_vec_fb = builder.EndVector(len(obj.wheel_to_world))

        SimpleVehicleStateFB.SimpleVehicleStateFBStart(builder)
        SimpleVehicleStateFB.SimpleVehicleStateFBAddHasBrakeLightOn(builder, True)
        SimpleVehicleStateFB.SimpleVehicleStateFBAddBrakeLightOn(builder, obj.brake_light_on)
        SimpleVehicleStateFB.SimpleVehicleStateFBAddEmergencyLightsOn(builder, obj.emergency_lights_on)
        if wheels_vec_fb:
            SimpleVehicleStateFB.SimpleVehicleStateFBAddWheelToWorld(builder, wheels_vec_fb)
        state = SimpleVehicleStateFB.SimpleVehicleStateFBEnd(builder)
        return state

    @staticmethod
    def deserialize(fb: SimpleVehicleStateFB.SimpleVehicleStateFB) -> SimpleVehicleStateData:
        simple_vehicle_state = SerializeSimpleVehicleState.SimpleVehicleStateData(
            wheel_to_world=[],
            emergency_lights_on=bool(fb.EmergencyLightsOn()),
            brake_light_on=bool(fb.BrakeLightOn())
        )
        for i in range(fb.WheelToWorldLength()):
            wheel_to_world_element_fb = fb.WheelToWorld(i)
            simple_vehicle_state.wheel_to_world.append(SerializePose.deserialize(wheel_to_world_element_fb))
        return simple_vehicle_state


class SerializeControlState:
    @dataclass
    class ControlStateData:
        indicator_state: VehicleIndicatorState

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: ControlStateData):
        ControlStateFB.ControlStateFBStart(builder)
        ControlStateFB.ControlStateFBAddIndicatorState(builder, obj.indicator_state.value)
        state = ControlStateFB.ControlStateFBEnd(builder)
        return state

    @staticmethod
    def deserialize(fb: ControlStateFB.ControlStateFB) -> ControlStateData:
        control_state = SerializeControlState.ControlStateData(
            indicator_state=VehicleIndicatorState(fb.IndicatorState())
        )
        return control_state


class SerializeSimpleControlState:
    @dataclass
    class SimpleControlStateData:
        pass

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: SimpleControlStateData):
        SimpleControlStateFB.SimpleControlStateFBStart(builder)
        state = SimpleControlStateFB.SimpleControlStateFBEnd(builder)
        return state

    @staticmethod
    def deserialize(fb: SimpleControlStateFB.SimpleControlStateFB) -> SimpleControlStateData:
        simple_control_state = SerializeSimpleControlState.SimpleControlStateData()
        return simple_control_state


class SerializeSignalModuleOutput:
    @dataclass
    class SignalModuleOutputData:
        elapsed_time: float
        phase_bulb_values: List[PhaseBulbValue]

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: SignalModuleOutputData):
        phase_bulb_values_vec_fb = None
        if obj.phase_bulb_values:
            phase_bulb_values_fb_list = [
                SerializePhaseBulbValue.serialize(builder, phase_bulb_value)
                for phase_bulb_value in obj.phase_bulb_values
            ]
            SignalModuleOutputFB.SignalModuleOutputFBStartPhaseBulbValuesVector(builder, len(phase_bulb_values_fb_list))
            for phase_bulb_value_fb in reversed(phase_bulb_values_fb_list):
                builder.PrependUOffsetTRelative(phase_bulb_value_fb)
            phase_bulb_values_vec_fb = builder.EndVector(len(phase_bulb_values_fb_list))

        SignalModuleOutputFB.SignalModuleOutputFBStart(builder)
        SignalModuleOutputFB.SignalModuleOutputFBAddElapsedTime(builder, obj.elapsed_time)
        if phase_bulb_values_vec_fb:
            SignalModuleOutputFB.SignalModuleOutputFBAddPhaseBulbValues(builder, phase_bulb_values_vec_fb)
        state = SignalModuleOutputFB.SignalModuleOutputFBEnd(builder)
        return state

    @staticmethod
    def deserialize(fb: SignalModuleOutputFB.SignalModuleOutputFB) -> SignalModuleOutputData:
        signal_module_output = SerializeSignalModuleOutput.SignalModuleOutputData(
            elapsed_time=fb.ElapsedTime(),
            phase_bulb_values=[]
        )
        for i in range(fb.PhaseBulbValuesLength()):
            phase_bulb_value_fb = fb.PhaseBulbValues(i)
            signal_module_output.phase_bulb_values.append(SerializePhaseBulbValue.deserialize(phase_bulb_value_fb))
        return signal_module_output


class SerializePedestrianState:
    @dataclass
    class PedestrianStateData:
        animation_data: str

    @staticmethod
    def serialize(builder: flatbuffers.Builder, obj: PedestrianStateData):
        animation_data_fb = builder.CreateString(obj.animation_data) if obj.animation_data else None
        PedestrianStateFB.PedestrianStateFBStart(builder)
        if animation_data_fb:
            PedestrianStateFB.PedestrianStateFBAddAnimationData(builder, animation_data_fb)
        state = PedestrianStateFB.PedestrianStateFBEnd(builder)
        return state

    @staticmethod
    def deserialize(fb: PedestrianStateFB.PedestrianStateFB) -> PedestrianStateData:
        pedestrian_state = SerializePedestrianState.PedestrianStateData(
            animation_data=fb.AnimationData().decode() or None
        )
        return pedestrian_state
