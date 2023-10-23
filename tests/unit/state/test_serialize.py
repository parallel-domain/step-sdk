import flatbuffers
import numpy as np
import pytest

from pd.internal.fb.generated.python import (
    AgentStateFB,
    CameraConfigFB,
    ControlStateFB,
    EnvironmentConfigFB,
    LiDARBeamFB,
    LiDARConfigFB,
    LiDARIntensityParamsFB,
    ModelConfigFB,
    ObjectDecorationsInfoFB,
    PedestrianStateFB,
    PhaseBulbValuesFB,
    PostProcessMatsFB,
    PostProcessParamsFB,
    SensorConfigFB,
    SensorExtrinsicConfigFB,
    SensorRigConfigFB,
    SignalModuleOutputFB,
    SimpleControlStateFB,
    SimpleVehicleStateFB,
    SimStateFB,
    TonemapCurveFB,
    TransformStateFB,
    VehicleModelConfigFB,
    WorldInfoFB,
    VehiclePhysicsConfigFB
)
from pd.internal.fb.generated.python.SensorIntrinsicConfigFB import SensorIntrinsicConfigFB
from pd.state.pose6d import Pose6D
from pd.state.sensor import (
    CameraSensor,
    DenoiseFilter,
    DistortionParams,
    LiDARBeam,
    LiDARIntensityParams,
    LiDARSensor,
    NoiseParams,
    PostProcessMaterial,
    PostProcessParams,
    TonemapCurve,
)
from pd.state.serialize import (
    SerializeAgent,
    SerializeCameraSensor,
    SerializeControlState,
    SerializeDistortionParams,
    SerializeEnvironmentConfig,
    SerializeLiDARBeam,
    SerializeLiDARIntensityParams,
    SerializeLiDARSensor,
    SerializeModelConfig,
    SerializeNoiseParams,
    SerializeObjectDecorationsInfo,
    SerializePedestrianState,
    SerializePhaseBulbValue,
    SerializePose,
    SerializePostProcessMaterial,
    SerializePostProcessParams,
    SerializeSensor,
    SerializeSensorRig,
    SerializeSignalModuleOutput,
    SerializeSimpleControlState,
    SerializeSimpleVehicleState,
    SerializeState,
    SerializeToneCurve,
    SerializeTransformState,
    SerializeVehicleModelConfig,
    SerializeWorldInfo,
    SerializeVehiclePhysicsConfig,
    bytes_to_state,
    state_to_bytes,
)
from pd.state.state import (
    DecorationObjectType,
    DecorationPreset,
    LotParkingDelineationType,
    ModelAgent,
    ObjectDecorations,
    PaintTexture,
    ParkingConfig,
    ParkingSpaceDecal,
    ParkingSpaceMaterial,
    PerformanceMode,
    PhaseBulbLogicalState,
    PhaseBulbValue,
    SensorAgent,
    SignalAgent,
    State,
    StreetParkingAngleZeroOverride,
    StreetParkingDelineationType,
    VehicleAgent,
    VehicleIndicatorState,
    WorldAgent,
    WorldInfo,
)


@pytest.fixture
def builder():
    return flatbuffers.Builder(65536)


def test_deserialize_sample_states(resources):
    """Sample states can be deserialized without errors"""
    base_path = resources / "sample_states"
    sample_state_files_path = [
        base_path / "sunnyvale_1.pd",
        base_path / "kettman_1.pd",
        base_path / "20221113-SJ_237AndGreatAmerica_1.pd",
        base_path / "20221114-SJ_237AndGreatAmerica_1.pd",
        base_path / "20230322-SF_6thAndMission_medium_1.pd",
        base_path / "20230503-SJ_237AndZanker_1.pd",
        base_path / "20230604-SF_6thAndMission_medium_1.pd",
        base_path / "20230428-SF_GrantAndCalifornia_1.pd"
    ]
    for state_file_path in sample_state_files_path:
        with open(state_file_path, "rb") as f:
            state_data = f.read()
            state = bytes_to_state(state_data)
            assert state
            bytes = state_to_bytes(state)
            assert bytes


def test_state_to_bytes():
    state = State(
        simulation_time_sec=12.345,
        world_info=WorldInfo(location="test location", time_of_day="test tod"),
        agents=[
            SensorAgent(id=1, pose=Pose6D(), velocity=(0.0, 0.0, 0.0)),
            ModelAgent(id=2, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), asset_name="test asset"),
            VehicleAgent(id=3, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), vehicle_type="test vehicle type"),
        ],
        capture=False,
    )
    state_bytes = state_to_bytes(state)
    result = bytes_to_state(state_bytes)

    assert result and isinstance(result, State)
    assert isinstance(result, State)
    assert result.world_info.location == "test location"
    assert result.world_info.time_of_day == "test tod"
    assert len(result.agents) == 3
    assert isinstance(result.agents[0], SensorAgent)
    assert result.agents[0].id == 1
    assert isinstance(result.agents[1], ModelAgent)
    assert result.agents[1].id == 2
    assert isinstance(result.agents[2], VehicleAgent)
    assert result.agents[2].id == 3
    assert not result.capture


class TestSerializePostProcessMaterial:
    def test_serdes(self, builder, helpers):
        mat = PostProcessMaterial("mat 1", 0.1)
        builder.Finish(SerializePostProcessMaterial.serialize(builder, mat))
        fb = PostProcessMatsFB.PostProcessMatsFB.GetRootAsPostProcessMatsFB(builder.Output(), 0)
        result = SerializePostProcessMaterial.deserialize(fb)

        assert result
        assert isinstance(result, PostProcessMaterial)
        assert result.material == "mat 1"
        assert helpers.fisclose(result.weight, 0.1)

    def test_deserialize_default(self, builder):
        PostProcessMatsFB.PostProcessMatsFBStart(builder)
        builder.Finish(PostProcessMatsFB.PostProcessMatsFBEnd(builder))
        fb = PostProcessMatsFB.PostProcessMatsFB.GetRootAsPostProcessMatsFB(builder.Output(), 0)
        default = SerializePostProcessMaterial.deserialize(fb)

        assert default
        assert default.material is None
        assert default.weight == 0


class TestSerializeTonemapCurve:
    def test_serdes(self, builder, helpers):
        tone_curve = TonemapCurve(slope=0.12, toe=0.34, shoulder=0.56, black_clip=0.78, white_clip=0.91)
        builder.Finish(SerializeToneCurve.serialize(builder, tone_curve))
        fb = TonemapCurveFB.TonemapCurveFB.GetRootAsTonemapCurveFB(builder.Output(), 0)
        result = SerializeToneCurve.deserialize(fb)

        assert result
        assert helpers.fisclose(result.slope, 0.12)
        assert helpers.fisclose(result.toe, 0.34)
        assert helpers.fisclose(result.shoulder, 0.56)
        assert helpers.fisclose(result.black_clip, 0.78)
        assert helpers.fisclose(result.white_clip, 0.91)

    def test_deserialize_default(self, builder, helpers):
        TonemapCurveFB.TonemapCurveFBStart(builder)
        builder.Finish(TonemapCurveFB.TonemapCurveFBEnd(builder))
        fb = TonemapCurveFB.TonemapCurveFB.GetRootAsTonemapCurveFB(builder.Output(), 0)
        default = SerializeToneCurve.deserialize(fb)

        assert default
        assert helpers.fisclose(default.slope, 0.66)
        assert helpers.fisclose(default.toe, 0.52)
        assert helpers.fisclose(default.shoulder, 0.49)
        assert helpers.fisclose(default.black_clip, 0.0)
        assert helpers.fisclose(default.white_clip, 0.08)


class TestSerializePostProcessParams:
    def test_serdes(self, builder, helpers):
        mat = PostProcessParams(
            exposure_compensation=0.1,
            exposure_speed_up=0.2,
            exposure_speed_down=0.3,
            exposure_min_ev100=0.4,
            exposure_max_ev100=0.5,
            exposure_metering_mask="test mask",
            motion_blur_amount=0.6,
            motion_blur_max=0.7,
            dof_focal_distance=0.8,
            dof_depth_blur_amount=0.9,
            dof_depth_blur_radius=1.1,
            vignette_intensity=1.2,
            tone_curve=TonemapCurve(slope=0.123),
            exposure_compensation_curve="exposure-curve",
        )
        builder.Finish(SerializePostProcessParams.serialize(builder, mat))
        fb = PostProcessParamsFB.PostProcessParamsFB.GetRootAsPostProcessParamsFB(builder.Output(), 0)
        result = SerializePostProcessParams.deserialize(fb)

        assert result
        assert helpers.fisclose(result.exposure_compensation, 0.1)
        assert helpers.fisclose(result.exposure_speed_up, 0.2)
        assert helpers.fisclose(result.exposure_speed_down, 0.3)
        assert helpers.fisclose(result.exposure_min_ev100, 0.4)
        assert helpers.fisclose(result.exposure_max_ev100, 0.5)
        assert result.exposure_metering_mask == "test mask"
        assert helpers.fisclose(result.motion_blur_amount, 0.6)
        assert helpers.fisclose(result.motion_blur_max, 0.7)
        assert helpers.fisclose(result.dof_focal_distance, 0.8)
        assert helpers.fisclose(result.dof_depth_blur_amount, 0.9)
        assert helpers.fisclose(result.dof_depth_blur_radius, 1.1)
        assert helpers.fisclose(result.vignette_intensity, 1.2)
        assert result.tone_curve
        assert helpers.fisclose(result.tone_curve.slope, 0.123)
        assert result.exposure_compensation_curve == "exposure-curve"

    def test_deserialize_default(self, builder, helpers):
        PostProcessParamsFB.PostProcessParamsFBStart(builder)
        builder.Finish(PostProcessParamsFB.PostProcessParamsFBEnd(builder))
        fb = PostProcessParamsFB.PostProcessParamsFB.GetRootAsPostProcessParamsFB(builder.Output(), 0)
        default = SerializePostProcessParams.deserialize(fb)

        assert default
        assert helpers.fisclose(default.exposure_compensation, -100.0)
        assert helpers.fisclose(default.exposure_speed_up, 0.0)
        assert helpers.fisclose(default.exposure_speed_down, 0.0)
        assert helpers.fisclose(default.exposure_min_ev100, -100.0)
        assert helpers.fisclose(default.exposure_max_ev100, -100.0)
        assert default.exposure_metering_mask is None
        assert helpers.fisclose(default.motion_blur_amount, 1.5)
        assert helpers.fisclose(default.motion_blur_max, 5.0)
        assert helpers.fisclose(default.dof_focal_distance, -1.0)
        assert helpers.fisclose(default.dof_depth_blur_amount, 0.0)
        assert helpers.fisclose(default.dof_depth_blur_radius, -1.0)
        assert helpers.fisclose(default.vignette_intensity, 0.0)
        assert default.tone_curve is None
        assert default.exposure_compensation_curve is None


class TestSerializeNoiseParams:
    def test_serdes(self, builder, helpers):
        noise_params = NoiseParams(
            enable_bayer=True,
            enable_gauss_noise=True,
            enable_poisson_noise=True,
            enable_denoise=True,
            gauss_noise_sigma=0.21,
            poisson_noise_lambda=0.22,
            denoise_filter=DenoiseFilter.BilateralFilter,
            denoise_filter_size=31,
            bilateral_sigma_d=0.41,
            bilateral_sigma_r=0.42,
            enable_auto_noise=True,
            signal_amount=52,
            pre_amplifier_noise=0.61,
            post_amplifier_noise=0.62,
            is_using_iso=True,
            iso_level=73,
            enable_auto_iso=True,
            fstop=0.84,
            max_exposure_time=0.85,
            quantum_efficiency=0.86,
        )
        # FB struct must be part of parent table
        CameraConfigFB.CameraConfigFBStart(builder)
        CameraConfigFB.CameraConfigFBAddNoiseParams(builder, SerializeNoiseParams.serialize(builder, noise_params))
        builder.Finish(CameraConfigFB.CameraConfigFBEnd(builder))
        fb_camera = CameraConfigFB.CameraConfigFB.GetRootAsCameraConfigFB(builder.Output(), 0)
        fb = fb_camera.NoiseParams()
        result = SerializeNoiseParams.deserialize(fb)

        assert result
        assert result.enable_bayer
        assert result.enable_gauss_noise
        assert result.enable_poisson_noise
        assert result.enable_denoise
        assert result.gauss_noise_sigma
        assert result.poisson_noise_lambda
        assert helpers.fisclose(result.gauss_noise_sigma, 0.21)
        assert helpers.fisclose(result.poisson_noise_lambda, 0.22)
        assert result.denoise_filter == DenoiseFilter.BilateralFilter
        assert result.denoise_filter_size == 31
        assert helpers.fisclose(result.bilateral_sigma_d, 0.41)
        assert helpers.fisclose(result.bilateral_sigma_r, 0.42)
        assert result.enable_auto_noise
        assert result.signal_amount == 52
        assert helpers.fisclose(result.pre_amplifier_noise, 0.61)
        assert helpers.fisclose(result.post_amplifier_noise, 0.62)
        assert result.is_using_iso
        assert result.iso_level == 73
        assert result.enable_auto_noise
        assert helpers.fisclose(result.fstop, 0.84)
        assert helpers.fisclose(result.max_exposure_time, 0.85)
        assert helpers.fisclose(result.quantum_efficiency, 0.86)

    def test_serdes_enums_as_int(self, builder, helpers):
        noise_params = NoiseParams(
            denoise_filter=2,
        )

        # FB struct must be part of parent table
        CameraConfigFB.CameraConfigFBStart(builder)
        CameraConfigFB.CameraConfigFBAddNoiseParams(builder, SerializeNoiseParams.serialize(builder, noise_params))
        builder.Finish(CameraConfigFB.CameraConfigFBEnd(builder))
        fb_camera = CameraConfigFB.CameraConfigFB.GetRootAsCameraConfigFB(builder.Output(), 0)
        fb = fb_camera.NoiseParams()
        result = SerializeNoiseParams.deserialize(fb)

        assert result
        assert result.denoise_filter == DenoiseFilter.FastMedianFilter


class TestSerializeDistortionParams:
    def test_serdes(self, builder, helpers):
        distortion_params = DistortionParams(
            k1=0.1,
            k2=0.2,
            k3=0.3,
            k4=0.4,
            k5=0.5,
            k6=0.6,
            p1=0.11,
            p2=0.12,
            skew=0.2,
            is_fisheye=True,
            fx=0.31,
            fy=0.32,
            cx=0.41,
            cy=0.42,
        )
        # FB struct must be part of parent table
        CameraConfigFB.CameraConfigFBStart(builder)
        CameraConfigFB.CameraConfigFBAddDistortionParams(
            builder, SerializeDistortionParams.serialize(builder, distortion_params)
        )
        builder.Finish(CameraConfigFB.CameraConfigFBEnd(builder))
        fb_camera = CameraConfigFB.CameraConfigFB.GetRootAsCameraConfigFB(builder.Output(), 0)
        fb = fb_camera.DistortionParams()
        result = SerializeDistortionParams.deserialize(fb)

        assert result
        assert helpers.fisclose(result.k1, 0.1)
        assert helpers.fisclose(result.k2, 0.2)
        assert helpers.fisclose(result.k3, 0.3)
        assert helpers.fisclose(result.k4, 0.4)
        assert helpers.fisclose(result.k5, 0.5)
        assert helpers.fisclose(result.k6, 0.6)
        assert helpers.fisclose(result.p1, 0.11)
        assert helpers.fisclose(result.p2, 0.12)
        assert helpers.fisclose(result.skew, 0.2)
        assert result.is_fisheye
        assert helpers.fisclose(result.fx, 0.31)
        assert helpers.fisclose(result.fy, 0.32)
        assert helpers.fisclose(result.cx, 0.41)
        assert helpers.fisclose(result.cy, 0.42)


class TestSerializeCameraSensor:
    def test_serdes(self, builder, helpers):
        camera = CameraSensor(
            name="test camera",
            pose=Pose6D(),
            width=1024,
            height=960,
            field_of_view_degrees=0.5,
            supersample=0.11,
            capture_rgb=True,
            capture_depth=True,
            capture_normals=True,
            capture_segmentation=True,
            capture_instances=True,
            capture_motionvectors=True,
            capture_basecolor=True,
            capture_properties=True,
            enable_streaming=True,
            lut="test lut",
            lut_weight=0.22,
            distortion_params=DistortionParams(k1=3.14),
            noise_params=NoiseParams(max_exposure_time=1.23),
            post_process_params=PostProcessParams(exposure_compensation=123.4),
            post_process_materials=[
                PostProcessMaterial("mat 1", 0.1),
                PostProcessMaterial("mat 2", 0.2),
                PostProcessMaterial("mat 3", 0.3),
            ],
            transmit_gray=True,
            fisheye_model=3,
            distortion_lookup_table="test distortion lookup table",
            time_offset=0.35,
        )
        builder.Finish(SerializeCameraSensor.serialize(builder, camera))
        fb = CameraConfigFB.CameraConfigFB.GetRootAsCameraConfigFB(builder.Output(), 0)
        result = SerializeCameraSensor.deserialize(fb)

        assert result
        assert result.width == 1024
        assert result.height == 960
        assert result.field_of_view_degrees == 0.5
        assert helpers.fisclose(result.supersample, 0.11)
        assert result.capture_rgb
        assert result.capture_depth
        assert result.capture_normals
        assert result.capture_segmentation
        assert result.capture_instances
        assert result.capture_motionvectors
        assert result.capture_basecolor
        assert result.capture_properties
        assert result.enable_streaming
        assert result.lut == "test lut"
        assert helpers.fisclose(result.lut_weight, 0.22)
        assert result.transmit_gray
        assert result.fisheye_model == 3
        assert result.distortion_lookup_table == "test distortion lookup table"
        assert helpers.fisclose(result.time_offset, 0.35)
        assert result.distortion_params
        assert helpers.fisclose(result.distortion_params.k1, 3.14)
        assert result.noise_params
        assert helpers.fisclose(result.noise_params.max_exposure_time, 1.23)
        assert helpers.fisclose(result.post_process_params.exposure_compensation, 123.4)
        assert len(result.post_process_materials) == 3
        assert result.post_process_materials[0].material == "mat 1"
        assert helpers.fisclose(result.post_process_materials[0].weight, 0.1)
        assert result.post_process_materials[1].material == "mat 2"
        assert helpers.fisclose(result.post_process_materials[1].weight, 0.2)
        assert result.post_process_materials[2].material == "mat 3"
        assert helpers.fisclose(result.post_process_materials[2].weight, 0.3)

    def test_deserialize_default(self, builder, helpers):
        CameraConfigFB.CameraConfigFBStart(builder)
        builder.Finish(CameraConfigFB.CameraConfigFBEnd(builder))
        fb = CameraConfigFB.CameraConfigFB.GetRootAsCameraConfigFB(builder.Output(), 0)
        default = SerializeCameraSensor.deserialize(fb)

        assert default
        assert default.width == 0
        assert default.height == 0
        assert default.field_of_view_degrees == 0
        assert helpers.fisclose(default.supersample, 1.0)
        assert not default.capture_rgb
        assert not default.capture_depth
        assert not default.capture_normals
        assert not default.capture_segmentation
        assert not default.capture_instances
        assert not default.capture_motionvectors
        assert not default.capture_basecolor
        assert not default.capture_properties
        assert not default.enable_streaming
        assert default.fisheye_model == 0
        assert default.distortion_lookup_table is None
        assert default.time_offset == 0
        assert default.lut is None
        assert helpers.fisclose(default.lut_weight, 1.0)
        assert not default.transmit_gray
        assert default.distortion_params is None
        assert default.noise_params is None
        assert default.post_process_params is None
        assert isinstance(default.post_process_materials, list) and len(default.post_process_materials) == 0


class TestSerializeSensor:
    def test_serdes_camera(self, builder):
        camera = CameraSensor(name="test camera", pose=Pose6D.from_translation(1.0, 2.0, 3.0), width=1024, height=960)
        camera.lock_to_yaw = True
        camera.attach_socket = "test-socket"
        camera.follow_rotation = False
        camera.render_ego = True
        builder.Finish(SerializeSensor.serialize(builder, camera))
        fb = SensorConfigFB.SensorConfigFB.GetRootAsSensorConfigFB(builder.Output(), 0)
        result = SerializeSensor.deserialize(fb)

        assert result
        assert isinstance(result, CameraSensor)
        assert result.name == "test camera"
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(1.0, 2.0, 3.0).as_transformation_matrix())
        assert result.width == 1024
        assert result.height == 960
        assert result.lock_to_yaw
        assert result.attach_socket == "test-socket"
        assert result.follow_rotation is False
        assert result.render_ego

    def test_deserialize_default_camera(self, builder):
        CameraConfigFB.CameraConfigFBStart(builder)
        fb_camera = CameraConfigFB.CameraConfigFBEnd(builder)
        SensorConfigFB.SensorConfigFBStart(builder)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsicType(builder, SensorIntrinsicConfigFB.CameraConfigFB)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsic(builder, fb_camera)
        builder.Finish(SensorConfigFB.SensorConfigFBEnd(builder))
        fb = SensorConfigFB.SensorConfigFB.GetRootAsSensorConfigFB(builder.Output(), 0)
        default = SerializeSensor.deserialize(fb)

        assert default
        assert isinstance(default, CameraSensor)
        assert default.name is None
        assert isinstance(default.pose, np.ndarray)
        assert not default.lock_to_yaw
        assert default.attach_socket is None
        assert default.follow_rotation is True
        assert default.render_ego is False

    def test_serdes_lidar(self, builder, helpers):
        lidar = LiDARSensor(
            name="test lidar", pose=Pose6D.from_translation(1.0, 2.0, 3.0), sample_rate=1.2, rotation_rate=1.3
        )
        lidar.lock_to_yaw = True
        lidar.attach_socket = "test-socket"
        lidar.follow_rotation = False
        lidar.render_ego = True
        builder.Finish(SerializeSensor.serialize(builder, lidar))
        fb = SensorConfigFB.SensorConfigFB.GetRootAsSensorConfigFB(builder.Output(), 0)
        result = SerializeSensor.deserialize(fb)

        assert result
        assert isinstance(result, LiDARSensor)
        assert result.name == "test lidar"
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(1.0, 2.0, 3.0).as_transformation_matrix())
        assert helpers.fisclose(result.sample_rate, 1.2)
        assert helpers.fisclose(result.rotation_rate, 1.3)
        assert result.lock_to_yaw
        assert result.attach_socket == "test-socket"
        assert result.follow_rotation is False
        assert result.render_ego is True

    def test_deserialize_default_lidar(self, builder):
        LiDARConfigFB.LiDARConfigFBStart(builder)
        fb_lidar = LiDARConfigFB.LiDARConfigFBEnd(builder)
        SensorConfigFB.SensorConfigFBStart(builder)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsicType(builder, SensorIntrinsicConfigFB.LiDARConfigFB)
        SensorConfigFB.SensorConfigFBAddSensorIntrinsic(builder, fb_lidar)
        builder.Finish(SensorConfigFB.SensorConfigFBEnd(builder))
        fb = SensorConfigFB.SensorConfigFB.GetRootAsSensorConfigFB(builder.Output(), 0)
        default = SerializeSensor.deserialize(fb)

        assert default
        assert isinstance(default, LiDARSensor)
        assert default.name is None
        assert isinstance(default.pose, np.ndarray)
        assert not default.lock_to_yaw
        assert default.attach_socket is None
        assert default.follow_rotation is True
        assert default.render_ego is False

    def test_deserialize_default_raises_error_on_missing_sensor(self, builder):
        SensorConfigFB.SensorConfigFBStart(builder)
        builder.Finish(SensorConfigFB.SensorConfigFBEnd(builder))
        fb = SensorConfigFB.SensorConfigFB.GetRootAsSensorConfigFB(builder.Output(), 0)
        with pytest.raises(TypeError, match=r".*Unsupported sensor type.*"):
            SerializeSensor.deserialize(fb)


class TestSerializePose:
    def test_serdes_from_pose6d(self, builder):
        pose = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0, alpha_radians=1.0, beta_radians=2.0, gamma_radians=3.0
        )
        # FB struct must be part of parent table
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBStart(builder)
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddSensorToVehicle(
            builder, SerializePose.serialize(builder, pose)
        )
        builder.Finish(SensorExtrinsicConfigFB.SensorExtrinsicConfigFBEnd(builder))
        fb_extrinsic = SensorExtrinsicConfigFB.SensorExtrinsicConfigFB.GetRootAsSensorExtrinsicConfigFB(
            builder.Output(), 0
        )
        fb = fb_extrinsic.SensorToVehicle()
        result = SerializePose.deserialize(fb)

        assert result is not None
        assert isinstance(result, np.ndarray)
        assert np.allclose(result, pose.as_transformation_matrix())

    def test_serdes_from_ndarray(self, builder):
        mat = np.array(
            [
                [1.1, 1.2, 1.3, 1.4],
                [2.1, 2.2, 2.3, 2.4],
                [3.1, 3.2, 3.3, 3.4],
                [4.1, 4.2, 4.3, 4.4],
            ],
            dtype=np.float32,
        )
        # FB struct must be part of parent table
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBStart(builder)
        SensorExtrinsicConfigFB.SensorExtrinsicConfigFBAddSensorToVehicle(
            builder, SerializePose.serialize(builder, mat)
        )
        builder.Finish(SensorExtrinsicConfigFB.SensorExtrinsicConfigFBEnd(builder))
        fb_extrinsic = SensorExtrinsicConfigFB.SensorExtrinsicConfigFB.GetRootAsSensorExtrinsicConfigFB(
            builder.Output(), 0
        )
        fb = fb_extrinsic.SensorToVehicle()
        result = SerializePose.deserialize(fb)

        assert result is not None
        assert isinstance(result, np.ndarray)
        assert np.allclose(result, mat)


class TestSerializeLiDARBeam:
    def test_serdes(self, builder, helpers):
        beam = LiDARBeam(id=1, azimuth=0.1, elevation=1.1)
        builder.Finish(SerializeLiDARBeam.serialize(builder, beam))
        fb = LiDARBeamFB.LiDARBeamFB.GetRootAsLiDARBeamFB(builder.Output(), 0)
        result = SerializeLiDARBeam.deserialize(fb)

        assert result
        assert isinstance(result, LiDARBeam)
        assert result.id == 1
        assert helpers.fisclose(result.azimuth, 0.1)
        assert helpers.fisclose(result.elevation, 1.1)

    def test_deserialize_default(self, builder, helpers):
        LiDARBeamFB.LiDARBeamFBStart(builder)
        builder.Finish(LiDARBeamFB.LiDARBeamFBEnd(builder))
        fb = LiDARBeamFB.LiDARBeamFB.GetRootAsLiDARBeamFB(builder.Output(), 0)
        default = SerializeLiDARBeam.deserialize(fb)

        assert default
        assert isinstance(default, LiDARBeam)
        assert default.id == 0
        assert helpers.fisclose(default.azimuth, 0.0)
        assert helpers.fisclose(default.elevation, 0.0)


class TestSerializeLiDARIntensityParams:
    def test_serdes(self, builder, helpers):
        params = LiDARIntensityParams(
            retro_range_noise_stddev=1.0,
            retroreflection_noise_mean=2.0,
            retroreflection_noise_stddev=3.0,
            max_attenuation_distance_metres=4.0,
            retro_intensity_enhance=5.0,
            intensity_specular_scale=6.0,
            intensity_roughness_scale=7.0,
            beam_intensity=8.0,
            albedo_weights=(9.1, 9.2, 9.3),
            max_albedo=10.0,
            strong_retro_intensity_enhance=11.0,
            intensity_metallic_scale=12.0,
            emissive_gate=13.0,
            max_emissive_rate=14.0,
        )
        builder.Finish(SerializeLiDARIntensityParams.serialize(builder, params))
        fb = LiDARIntensityParamsFB.LiDARIntensityParamsFB.GetRootAsLiDARIntensityParamsFB(builder.Output(), 0)
        result = SerializeLiDARIntensityParams.deserialize(fb)

        assert result
        assert isinstance(result, LiDARIntensityParams)
        assert helpers.fisclose(result.retro_range_noise_stddev, 1.0)
        assert helpers.fisclose(result.retroreflection_noise_mean, 2.0)
        assert helpers.fisclose(result.retroreflection_noise_stddev, 3.0)
        assert helpers.fisclose(result.max_attenuation_distance_metres, 4.0)
        assert helpers.fisclose(result.retro_intensity_enhance, 5.0)
        assert helpers.fisclose(result.intensity_specular_scale, 6.0)
        assert helpers.fisclose(result.intensity_roughness_scale, 7.0)
        assert helpers.fisclose(result.beam_intensity, 8.0)
        assert helpers.fisclose(result.albedo_weights[0], 9.1)
        assert helpers.fisclose(result.albedo_weights[1], 9.2)
        assert helpers.fisclose(result.albedo_weights[2], 9.3)
        assert helpers.fisclose(result.max_albedo, 10.0)
        assert helpers.fisclose(result.strong_retro_intensity_enhance, 11.0)
        assert helpers.fisclose(result.intensity_metallic_scale, 12.0)
        assert helpers.fisclose(result.emissive_gate, 13.0)
        assert helpers.fisclose(result.max_emissive_rate, 14.0)

    def test_deserialize_default(self, builder, helpers):
        LiDARIntensityParamsFB.LiDARIntensityParamsFBStart(builder)
        builder.Finish(LiDARIntensityParamsFB.LiDARIntensityParamsFBEnd(builder))
        fb = LiDARIntensityParamsFB.LiDARIntensityParamsFB.GetRootAsLiDARIntensityParamsFB(builder.Output(), 0)
        default = SerializeLiDARIntensityParams.deserialize(fb)

        assert default
        assert isinstance(default, LiDARIntensityParams)
        assert helpers.fisclose(default.retro_range_noise_stddev, 0.1)
        assert helpers.fisclose(default.retroreflection_noise_mean, 0.0)
        assert helpers.fisclose(default.retroreflection_noise_stddev, 0.1)
        assert helpers.fisclose(default.max_attenuation_distance_metres, 220.0)
        assert helpers.fisclose(default.retro_intensity_enhance, 1.5)
        assert helpers.fisclose(default.intensity_specular_scale, 2.0)
        assert helpers.fisclose(default.intensity_roughness_scale, 1.5)
        assert helpers.fisclose(default.beam_intensity, 2.0)
        assert helpers.fisclose(default.albedo_weights[0], 0.0)
        assert helpers.fisclose(default.albedo_weights[1], 0.0)
        assert helpers.fisclose(default.albedo_weights[2], 0.0)
        assert helpers.fisclose(default.max_albedo, 2.2)
        assert helpers.fisclose(default.strong_retro_intensity_enhance, 0.9)
        assert helpers.fisclose(default.intensity_metallic_scale, 1.0)
        assert helpers.fisclose(default.emissive_gate, 100.0)
        assert helpers.fisclose(default.max_emissive_rate, 10.0)


class TestSerializeLiDARSensor:
    def test_serdes(self, builder, helpers):
        lidar = LiDARSensor(
            name="test lidar",
            pose=Pose6D(),
            sample_rate=0.1,
            rotation_rate=0.2,
            beam_data=[
                LiDARBeam(id=1, azimuth=0.1, elevation=1.1),
                LiDARBeam(id=2, azimuth=0.2, elevation=1.2),
                LiDARBeam(id=3, azimuth=0.3, elevation=1.3),
            ],
            azimuth_min=0.3,
            azimuth_max=0.4,
            elevation_delta=0.5,
            capture_rgb=True,
            capture_depth=True,
            capture_normals=True,
            capture_segmentation=True,
            capture_instances=True,
            capture_motionvectors=True,
            minimum_range_cutoff=0.6,
            maximum_range_cutoff=0.7,
            minimum_cutoff_prob=0.8,
            maximum_cutoff_prob=0.9,
            minimum_offset=1.1,
            maximum_offset=1.2,
            minimum_noise=1.3,
            range_noise_mean=1.4,
            range_noise_stddev=1.5,
            intensity_params=LiDARIntensityParams(
                retro_range_noise_stddev=3.1,
            ),
            pattern="lidar pattern",
            time_offset_ms=1.6,
        )
        builder.Finish(SerializeLiDARSensor.serialize(builder, lidar))
        fb = LiDARConfigFB.LiDARConfigFB.GetRootAsLiDARConfigFB(builder.Output(), 0)
        result = SerializeLiDARSensor.deserialize(fb)

        assert result
        assert isinstance(result, LiDARSensor)
        assert helpers.fisclose(result.sample_rate, 0.1)
        assert helpers.fisclose(result.rotation_rate, 0.2)
        assert helpers.fisclose(result.azimuth_min, 0.3)
        assert helpers.fisclose(result.azimuth_max, 0.4)
        assert helpers.fisclose(result.elevation_delta, 0.5)
        assert result.capture_rgb
        assert result.capture_depth
        assert result.capture_normals
        assert result.capture_segmentation
        assert result.capture_instances
        assert result.capture_motionvectors
        assert len(result.beam_data) == 3
        assert lidar.beam_data[0].id == 1
        assert helpers.fisclose(lidar.beam_data[0].azimuth, 0.1)
        assert helpers.fisclose(lidar.beam_data[0].elevation, 1.1)
        assert lidar.beam_data[1].id == 2
        assert helpers.fisclose(lidar.beam_data[1].azimuth, 0.2)
        assert helpers.fisclose(lidar.beam_data[1].elevation, 1.2)
        assert lidar.beam_data[2].id == 3
        assert helpers.fisclose(lidar.beam_data[2].azimuth, 0.3)
        assert helpers.fisclose(lidar.beam_data[2].elevation, 1.3)
        assert helpers.fisclose(lidar.minimum_range_cutoff, 0.6)
        assert helpers.fisclose(lidar.maximum_range_cutoff, 0.7)
        assert helpers.fisclose(lidar.minimum_cutoff_prob, 0.8)
        assert helpers.fisclose(lidar.maximum_cutoff_prob, 0.9)
        assert helpers.fisclose(lidar.minimum_offset, 1.1)
        assert helpers.fisclose(lidar.maximum_offset, 1.2)
        assert helpers.fisclose(lidar.minimum_noise, 1.3)
        assert helpers.fisclose(lidar.range_noise_mean, 1.4)
        assert helpers.fisclose(lidar.range_noise_stddev, 1.5)
        assert helpers.fisclose(lidar.intensity_params.retro_range_noise_stddev, 3.1)
        assert lidar.pattern == "lidar pattern"
        assert helpers.fisclose(lidar.time_offset_ms, 1.6)


class TestSerializePhaseBulbValue:
    def test_serdes(self, builder, helpers):
        bulb = PhaseBulbValue(phase=42, red=1.1, yellow=1.2, green=1.3, logical_state=PhaseBulbLogicalState.RedFlashing)
        builder.Finish(SerializePhaseBulbValue.serialize(builder, bulb))
        fb = PhaseBulbValuesFB.PhaseBulbValuesFB.GetRootAsPhaseBulbValuesFB(builder.Output(), 0)
        result = SerializePhaseBulbValue.deserialize(fb)

        assert result
        assert isinstance(result, PhaseBulbValue)
        assert result.phase == 42
        assert helpers.fisclose(result.red, 1.1)
        assert helpers.fisclose(result.yellow, 1.2)
        assert helpers.fisclose(result.green, 1.3)
        assert result.logical_state == PhaseBulbLogicalState.RedFlashing

    def test_serdes_enums_as_int(self, builder, helpers):
        bulb = PhaseBulbValue(logical_state=6)
        builder.Finish(SerializePhaseBulbValue.serialize(builder, bulb))
        fb = PhaseBulbValuesFB.PhaseBulbValuesFB.GetRootAsPhaseBulbValuesFB(builder.Output(), 0)
        result = SerializePhaseBulbValue.deserialize(fb)

        assert result
        assert result.logical_state == PhaseBulbLogicalState.GreenFlashing

    def test_deserialize_default(self, builder, helpers):
        PhaseBulbValuesFB.PhaseBulbValuesFBStart(builder)
        builder.Finish(PhaseBulbValuesFB.PhaseBulbValuesFBEnd(builder))
        fb = PhaseBulbValuesFB.PhaseBulbValuesFB.GetRootAsPhaseBulbValuesFB(builder.Output(), 0)
        default = SerializePhaseBulbValue.deserialize(fb)

        assert default
        assert isinstance(default, PhaseBulbValue)
        assert default.phase == 0
        assert helpers.fisclose(default.red, 0.0)
        assert helpers.fisclose(default.yellow, 0.0)
        assert helpers.fisclose(default.green, 0.0)
        assert default.logical_state == PhaseBulbLogicalState.Inactive


class TestSerializeWorldInfo:
    def test_serdes(self, builder, helpers):
        world_info = WorldInfo(
            location="test location",
            time_of_day="test time of day",
            wetness=0.1,
            rain_intensity=0.2,
            street_lights=0.3,
            fog_intensity=0.4,
            enable_headlights=True,
            performance_mode=PerformanceMode.Performance,
            anti_aliasing=42,
            scenario_seed=25487,
            agent_tags={1: ["aaa", "bbb"], 343: ["ccc"], 99: ["ddd", "eee", "fff"]},
        )
        builder.Finish(SerializeWorldInfo.serialize(builder, world_info))
        fb = WorldInfoFB.WorldInfoFB.GetRootAsWorldInfoFB(builder.Output(), 0)
        result = SerializeWorldInfo.deserialize(fb)

        assert result
        assert isinstance(result, WorldInfo)
        assert result.location == "test location"
        assert result.time_of_day == "test time of day"
        assert helpers.fisclose(result.wetness, 0.1)
        assert helpers.fisclose(result.rain_intensity, 0.2)
        assert helpers.fisclose(result.street_lights, 0.3)
        assert helpers.fisclose(result.fog_intensity, 0.4)
        assert result.enable_headlights
        assert result.performance_mode == PerformanceMode.Performance
        assert result.anti_aliasing == 42
        assert result.scenario_seed == 25487
        assert len(result.agent_tags.items()) == 3
        assert result.agent_tags[1] == ["aaa", "bbb"]
        assert result.agent_tags[343] == ["ccc"]
        assert result.agent_tags[99] == ["ddd", "eee", "fff"]

    def test_serdes_null_location(self, builder):
        world_info = WorldInfo()
        builder.Finish(SerializeWorldInfo.serialize(builder, world_info))
        fb = WorldInfoFB.WorldInfoFB.GetRootAsWorldInfoFB(builder.Output(), 0)
        result = SerializeWorldInfo.deserialize(fb)

        assert result
        assert isinstance(result, WorldInfo)
        assert result.location is None
        assert result.time_of_day is None

    def test_deserialize_default(self, builder, helpers):
        WorldInfoFB.WorldInfoFBStart(builder)
        builder.Finish(WorldInfoFB.WorldInfoFBEnd(builder))
        fb = WorldInfoFB.WorldInfoFB.GetRootAsWorldInfoFB(builder.Output(), 0)
        default = SerializeWorldInfo.deserialize(fb)

        assert default
        assert isinstance(default, WorldInfo)
        assert default.location is None
        assert default.time_of_day is None
        assert default.wetness == 0
        assert default.rain_intensity == 0
        assert default.street_lights == 0
        assert default.fog_intensity == 0
        assert not default.enable_headlights
        assert default.performance_mode == PerformanceMode.HighFidelity
        assert default.anti_aliasing == 4
        assert default.scenario_seed == 0
        assert default.agent_tags == {}


class TestSerializeState:
    def test_serdes(self, builder):
        state = State(
            simulation_time_sec=12.345,
            world_info=WorldInfo(location="test location", time_of_day="test tod"),
            agents=[
                SensorAgent(id=1, pose=Pose6D(), velocity=(0.0, 0.0, 0.0)),
                ModelAgent(id=2, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), asset_name="test asset"),
                VehicleAgent(id=3, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), vehicle_type="test vehicle type"),
                SignalAgent(id=4, elapsed_time=1.1, phase_bulb_values=[]),
            ],
            capture=False,
        )
        builder.Finish(SerializeState.serialize(builder, state))
        fb = SimStateFB.SimStateFB.GetRootAsSimStateFB(builder.Output(), 0)
        result = SerializeState.deserialize(fb)

        assert result
        assert isinstance(result, State)
        assert result.world_info.location == "test location"
        assert result.world_info.time_of_day == "test tod"
        assert len(result.agents) == 4
        assert isinstance(result.agents[0], SensorAgent)
        assert result.agents[0].id == 1
        assert isinstance(result.agents[1], ModelAgent)
        assert result.agents[1].id == 2
        assert isinstance(result.agents[2], VehicleAgent)
        assert result.agents[2].id == 3
        assert isinstance(result.agents[3], SignalAgent)
        assert result.agents[3].id == 4
        assert not result.capture

    def test_deserialize_default(self, builder):
        SimStateFB.SimStateFBStart(builder)
        builder.Finish(SimStateFB.SimStateFBEnd(builder))
        fb = SimStateFB.SimStateFB.GetRootAsSimStateFB(builder.Output(), 0)
        default = SerializeState.deserialize(fb)

        assert default
        assert isinstance(default, State)
        assert default.simulation_time_sec == 0
        assert len(default.agents) == 0
        assert default.world_info is None
        assert default.capture


class TestSerializeAgent:
    def test_serdes_vehicle_agent_pose_matrix(self, builder):
        pose_matrix = Pose6D.from_euler_angles(
            x_metres=1.0, y_metres=2.0, z_metres=3.0, alpha_radians=1.0, beta_radians=2.0, gamma_radians=3.0
        ).as_transformation_matrix()
        vehicle_agent = VehicleAgent(id=1, pose=pose_matrix, velocity=(0.0, 0.0, 0.0), vehicle_type="test vehicle")
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, VehicleAgent)
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, pose_matrix)

    def test_serdes_vehicle_agent_parked(self, builder):
        # Not parked
        vehicle_agent = VehicleAgent(
            id=1, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), vehicle_type="test vehicle", is_parked=False
        )
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, VehicleAgent)
        assert not result.is_parked

        # Parked
        vehicle_agent.is_parked = True
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, VehicleAgent)
        assert result.is_parked

    def test_serdes_vehicle_agent_connections(self, builder):
        mat1 = np.array(
            [
                [1.1, 1.2, 1.3, 1.4],
                [2.1, 2.2, 2.3, 2.4],
                [3.1, 3.2, 3.3, 3.4],
                [4.1, 4.2, 4.3, 4.4],
            ],
            dtype=np.float32,
        )
        mat2 = np.array(
            [
                [1.0, 2.0, 3.0, 4.0],
                [5.0, 6.0, 7.0, 8.0],
                [9.0, 10.0, 11.0, 12.0],
                [13.0, 14.0, 15.0, 16.0],
            ],
            dtype=np.float32,
        )
        vehicle_agent = VehicleAgent(
            id=1, pose=Pose6D(), velocity=(0.0, 0.0, 0.0), vehicle_type="test vehicle",
            connections=[(42, mat1), (1234, mat2)]
        )
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, VehicleAgent)
        assert len(result.connections) == 2
        assert result.connections[0][0] == 42
        assert isinstance(result.connections[0][1], np.ndarray)
        assert np.allclose(result.connections[0][1], mat1)
        assert result.connections[1][0] == 1234
        assert isinstance(result.connections[1][1], np.ndarray)
        assert np.allclose(result.connections[1][1], mat2)

    def test_serdes_vehicle_agent(self, builder, helpers):
        vehicle_agent = VehicleAgent(
            id=22,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
            vehicle_type="test vehicle",
            vehicle_color="test color",
            vehicle_accessory="test accessory",
            vehicle_wear=0.25,
            vehicle_actor="test actor",
            wheel_type="test wheel type",
            wheel_poses=[
                Pose6D.from_translation(1.1, 2.2, 3.3),
                Pose6D.from_translation(4.4, 5.5, 6.6),
                Pose6D.from_translation(7.7, 8.8, 9.9),
            ],
            lock_to_ground=True,
            ground_offset=0.58,
            wheel_combo=["wc1", "wc2"],
            wheel_combo_style=["wcs1", "wcs2"],
            accessories=["a1", "a2"],
            occupants=["o1", "o2"],
            brake_light_on=True,
            emergency_lights_on=True,
            indicator_state=VehicleIndicatorState.Hazards,
            sensors=[
                CameraSensor(name="camera1", pose=Pose6D(), width=1080, height=720),
                LiDARSensor(name="lidar", pose=Pose6D(), sample_rate=0.1, rotation_rate=0.2),
            ],
            is_parked=False,
            headlight_on=True,
        )
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, VehicleAgent)
        assert result.id == 22
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(0.1, 0.2, 0.3).as_transformation_matrix())
        assert helpers.fisclose(result.velocity[0], 3.1)
        assert helpers.fisclose(result.velocity[1], 3.2)
        assert helpers.fisclose(result.velocity[2], 3.3)
        assert result.vehicle_type == "test vehicle"
        assert result.vehicle_color == "test color"
        assert result.vehicle_accessory == "test accessory"
        assert helpers.fisclose(result.vehicle_wear, 0.25)
        assert result.vehicle_actor == "test actor"
        assert result.wheel_type == "test wheel type"
        assert result.lock_to_ground
        assert helpers.fisclose(result.ground_offset, 0.58)
        assert result.wheel_combo == ["wc1", "wc2"]
        assert len(result.sensors) == 2
        assert result.sensors[0].name == "camera1"
        assert result.sensors[1].name == "lidar"
        assert len(result.wheel_poses) == 3
        assert isinstance(result.wheel_poses[0], np.ndarray)
        assert np.allclose(result.wheel_poses[0], Pose6D.from_translation(1.1, 2.2, 3.3).as_transformation_matrix())
        assert isinstance(result.wheel_poses[1], np.ndarray)
        assert np.allclose(result.wheel_poses[1], Pose6D.from_translation(4.4, 5.5, 6.6).as_transformation_matrix())
        assert isinstance(result.wheel_poses[2], np.ndarray)
        assert np.allclose(result.wheel_poses[2], Pose6D.from_translation(7.7, 8.8, 9.9).as_transformation_matrix())
        assert result.brake_light_on
        assert result.emergency_lights_on
        assert result.indicator_state == VehicleIndicatorState.Hazards
        assert not result.is_parked
        assert result.headlight_on

    def test_serdes_vehicle_agent_enums_as_int(self, builder, helpers):
        vehicle_agent = VehicleAgent(
            id=22,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
            vehicle_type="test vehicle",
            indicator_state=2,
        )
        builder.Finish(SerializeAgent.serialize(builder, vehicle_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert result.indicator_state == VehicleIndicatorState.Right

    def test_serdes_sensor_agent(self, builder, helpers):
        sensor_agent = SensorAgent(
            id=33,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
            sensors=[
                CameraSensor(name="camera1", pose=Pose6D(), width=1080, height=720),
                LiDARSensor(name="lidar", pose=Pose6D(), sample_rate=0.1, rotation_rate=0.2),
            ],
        )
        builder.Finish(SerializeAgent.serialize(builder, sensor_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, SensorAgent)
        assert result.id == 33
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(0.1, 0.2, 0.3).as_transformation_matrix())
        assert helpers.fisclose(result.velocity[0], 3.1)
        assert helpers.fisclose(result.velocity[1], 3.2)
        assert helpers.fisclose(result.velocity[2], 3.3)
        assert len(result.sensors) == 2
        assert result.sensors[0].name == "camera1"
        assert result.sensors[1].name == "lidar"

    def test_serdes_model_agent(self, builder, helpers):
        model_agent = ModelAgent(
            id=44,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
            asset_name="test asset",
            lock_to_ground=True,
            ground_offset=0.57,
            sensors=[
                CameraSensor(name="camera1", pose=Pose6D(), width=1080, height=720),
                LiDARSensor(name="lidar", pose=Pose6D(), sample_rate=0.1, rotation_rate=0.2),
            ],
        )
        builder.Finish(SerializeAgent.serialize(builder, model_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, ModelAgent)
        assert result.id == 44
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(0.1, 0.2, 0.3).as_transformation_matrix())
        assert helpers.fisclose(result.velocity[0], 3.1)
        assert helpers.fisclose(result.velocity[1], 3.2)
        assert helpers.fisclose(result.velocity[2], 3.3)
        assert result.asset_name == "test asset"
        assert result.lock_to_ground
        assert helpers.fisclose(result.ground_offset, 0.57)
        assert len(result.sensors) == 2
        assert result.sensors[0].name == "camera1"
        assert result.sensors[1].name == "lidar"

    def test_serdes_model_agent_pedestrian(self, builder, helpers):
        model_agent = ModelAgent(
            id=44,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
            asset_name="test asset",
            pedestrian_animation_data="test pedestrian animation",
        )
        builder.Finish(SerializeAgent.serialize(builder, model_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, ModelAgent)
        assert result.id == 44
        assert result.pedestrian_animation_data == "test pedestrian animation"

    def test_serdes_signal_agent(self, builder, helpers):
        signal_agent = SignalAgent(
            id=55,
            elapsed_time=56.78,
            phase_bulb_values=[
                PhaseBulbValue(
                    phase=42, red=1.1, yellow=1.2, green=1.3, logical_state=PhaseBulbLogicalState.RedFlashing
                ),
                PhaseBulbValue(phase=43, red=2.1, yellow=2.2, green=2.3, logical_state=PhaseBulbLogicalState.Green),
            ],
        )
        builder.Finish(SerializeAgent.serialize(builder, signal_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, SignalAgent)
        assert result.id == 55
        assert helpers.fisclose(result.elapsed_time, 56.78)
        assert len(result.phase_bulb_values) == 2
        assert result.phase_bulb_values[0].phase == 42
        assert result.phase_bulb_values[1].phase == 43

    def test_serdes_agent_posed(self, builder, helpers):
        sensor_agent = SensorAgent(
            id=44,
            pose=Pose6D.from_translation(0.1, 0.2, 0.3),
            velocity=(3.1, 3.2, 3.3),
        )
        sensor_agent.angular_velocity = (4.1, 4.2, 4.3)
        builder.Finish(SerializeAgent.serialize(builder, sensor_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, SensorAgent)
        assert result.id == 44
        assert isinstance(result.pose, np.ndarray)
        assert np.allclose(result.pose, Pose6D.from_translation(0.1, 0.2, 0.3).as_transformation_matrix())
        assert helpers.fisclose(result.velocity[0], 3.1)
        assert helpers.fisclose(result.velocity[1], 3.2)
        assert helpers.fisclose(result.velocity[2], 3.3)
        assert helpers.fisclose(result.angular_velocity[0], 4.1)
        assert helpers.fisclose(result.angular_velocity[1], 4.2)
        assert helpers.fisclose(result.angular_velocity[2], 4.3)

    def test_serdes_world_agent(self, builder, helpers):
        world_agent = WorldAgent(
            id=1,
            parking_config=ParkingConfig(
                angle=42,
                delineation_color=(1.3, 4.5, 6.7),
                delineation_wear_amount=0.82,
                parking_space_tint=(0.1, 0.2, 0.3),
                parking_space_grunge_amount=0.123,
                lot_parking_delineation_type=LotParkingDelineationType.Random,
                street_parking_delineation_type=StreetParkingDelineationType.DoubleOpen,
                street_parking_angle_zero_override=StreetParkingAngleZeroOverride.Dashed,
                parking_space_material=ParkingSpaceMaterial.MI_ParkingTiles_CobbleStone_01,
                global_parking_decal_wear=0.456,
            ),
            object_decorations={
                10756: ObjectDecorations(
                    type=DecorationObjectType.Lane,
                    object_id=56,
                    decorations={
                        20: DecorationPreset(preset_name="test preset", variant=4567),
                        13: ParkingSpaceDecal(decal_preset="test decal preset"),
                    },
                )
            },
        )
        builder.Finish(SerializeAgent.serialize(builder, world_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, WorldAgent)
        assert result.id == 1
        assert result.parking_config
        assert result.parking_config.angle == 42
        assert helpers.fisclose(result.parking_config.delineation_color[0], 1.3)
        assert helpers.fisclose(result.parking_config.delineation_color[1], 4.5)
        assert helpers.fisclose(result.parking_config.delineation_color[2], 6.7)
        assert helpers.fisclose(result.parking_config.delineation_wear_amount, 0.82)
        assert helpers.fisclose(result.parking_config.parking_space_tint[0], 0.1)
        assert helpers.fisclose(result.parking_config.parking_space_tint[1], 0.2)
        assert helpers.fisclose(result.parking_config.parking_space_tint[2], 0.3)
        assert helpers.fisclose(result.parking_config.parking_space_grunge_amount, 0.123)
        assert result.parking_config.lot_parking_delineation_type == LotParkingDelineationType.Random
        assert result.parking_config.street_parking_delineation_type == StreetParkingDelineationType.DoubleOpen
        assert result.parking_config.street_parking_angle_zero_override == StreetParkingAngleZeroOverride.Dashed
        assert result.parking_config.parking_space_material == ParkingSpaceMaterial.MI_ParkingTiles_CobbleStone_01
        assert helpers.fisclose(result.parking_config.global_parking_decal_wear, 0.456)

        assert result.object_decorations
        assert len(result.object_decorations.items()) == 1
        object_decorations = result.object_decorations.get(10756, None)
        assert object_decorations
        assert object_decorations.type == DecorationObjectType.Lane
        assert object_decorations.object_id == 56
        assert object_decorations.decorations
        assert len(object_decorations.decorations.items()) == 2
        decorations = object_decorations.decorations.get(20, None)
        assert isinstance(decorations, DecorationPreset)
        assert decorations.preset_name == "test preset"
        assert decorations.variant == 4567
        decorations = object_decorations.decorations.get(13, None)
        assert isinstance(decorations, ParkingSpaceDecal)
        assert decorations.decal_preset == "test decal preset"

    def test_serdes_world_agent_enums_as_int(self, builder, helpers):
        world_agent = WorldAgent(
            id=1,
            parking_config=ParkingConfig(
                angle=0,
                delineation_color=(0, 0, 0),
                delineation_wear_amount=0,
                parking_space_tint=(0, 0, 0),
                parking_space_grunge_amount=0,
                lot_parking_delineation_type=4,
                street_parking_delineation_type=5,
                street_parking_angle_zero_override=5,
                parking_space_material=6,
            ),
        )
        builder.Finish(SerializeAgent.serialize(builder, world_agent))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        result = SerializeAgent.deserialize(fb)

        assert result
        assert isinstance(result, WorldAgent)
        assert result.parking_config.lot_parking_delineation_type == LotParkingDelineationType.DoubleRound
        assert result.parking_config.street_parking_delineation_type == StreetParkingDelineationType.DoubleRound
        assert result.parking_config.street_parking_angle_zero_override == StreetParkingAngleZeroOverride.DoubleRound
        assert result.parking_config.parking_space_material == ParkingSpaceMaterial.MI_ParkingTiles_CobbleStone_02

    def test_deserialize_default(self, builder):
        AgentStateFB.AgentStateFBStart(builder)
        builder.Finish(AgentStateFB.AgentStateFBEnd(builder))
        fb = AgentStateFB.AgentStateFB.GetRootAsAgentStateFB(builder.Output(), 0)
        assert SerializeAgent.deserialize(fb) is None


class TestSerializeSensorRig:
    def test_serdes(self, builder, helpers):
        sensors = [
            CameraSensor(name="test camera", pose=Pose6D(), width=1920, height=1080),
            LiDARSensor(name="test lidar", pose=Pose6D(), sample_rate=2.2, rotation_rate=2.3),
        ]
        builder.Finish(SerializeSensorRig.serialize(builder, SerializeSensorRig.SensorRigData(sensors)))
        fb = SensorRigConfigFB.SensorRigConfigFB.GetRootAsSensorRigConfigFB(builder.Output(), 0)
        result = SerializeSensorRig.deserialize(fb)

        assert result
        assert isinstance(result, SerializeSensorRig.SensorRigData)
        assert len(result.sensors) == 2
        assert isinstance(result.sensors[0], CameraSensor)
        assert result.sensors[0].name == "test camera"
        assert result.sensors[0].width == 1920
        assert result.sensors[0].height == 1080
        assert isinstance(result.sensors[1], LiDARSensor)
        assert result.sensors[1].name == "test lidar"
        assert helpers.fisclose(result.sensors[1].sample_rate, 2.2)
        assert helpers.fisclose(result.sensors[1].rotation_rate, 2.3)

    def test_deserialize_default(self, builder):
        SensorRigConfigFB.SensorRigConfigFBStart(builder)
        builder.Finish(SensorRigConfigFB.SensorRigConfigFBEnd(builder))
        fb = SensorRigConfigFB.SensorRigConfigFB.GetRootAsSensorRigConfigFB(builder.Output(), 0)
        default = SerializeSensorRig.deserialize(fb)

        assert isinstance(default, SerializeSensorRig.SensorRigData)
        assert len(default.sensors) == 0


class TestSerializeTransformState:
    def test_serdes(self, builder, helpers):
        transform_state = SerializeTransformState.TransformStateData(
            pose=Pose6D.from_translation(1.0, 2.0, 3.0).as_transformation_matrix(),
            velocity=(1.1, 1.2, 1.3),
            angular_velocity=(2.1, 2.2, 2.3),
        )
        builder.Finish(SerializeTransformState.serialize(builder, transform_state))
        fb = TransformStateFB.TransformStateFB.GetRootAsTransformStateFB(builder.Output(), 0)
        result = SerializeTransformState.deserialize(fb)

        assert result
        assert isinstance(result, SerializeTransformState.TransformStateData)
        assert np.allclose(result.pose, Pose6D.from_translation(1.0, 2.0, 3.0).as_transformation_matrix())
        assert helpers.fisclose(result.velocity[0], 1.1)
        assert helpers.fisclose(result.velocity[1], 1.2)
        assert helpers.fisclose(result.velocity[2], 1.3)
        assert helpers.fisclose(result.angular_velocity[0], 2.1)
        assert helpers.fisclose(result.angular_velocity[1], 2.2)
        assert helpers.fisclose(result.angular_velocity[2], 2.3)

    def test_deserialize_default(self, builder):
        TransformStateFB.TransformStateFBStart(builder)
        builder.Finish(TransformStateFB.TransformStateFBEnd(builder))
        fb = TransformStateFB.TransformStateFB.GetRootAsTransformStateFB(builder.Output(), 0)
        default = SerializeTransformState.deserialize(fb)

        assert default
        assert isinstance(default, SerializeTransformState.TransformStateData)
        assert isinstance(default.pose, np.ndarray)
        assert default.velocity == (0.0, 0.0, 0.0)
        assert default.angular_velocity == (0.0, 0.0, 0.0)


class TestSerializeModelConfig:
    def test_serdes(self, builder, helpers):
        model_config = SerializeModelConfig.ModelConfigData(
            asset_name="test asset", lock_to_ground=True, ground_offset=2.5
        )
        builder.Finish(SerializeModelConfig.serialize(builder, model_config))
        fb = ModelConfigFB.ModelConfigFB.GetRootAsModelConfigFB(builder.Output(), 0)
        result = SerializeModelConfig.deserialize(fb)

        assert result
        assert isinstance(result, SerializeModelConfig.ModelConfigData)
        assert result.asset_name == "test asset"
        assert result.lock_to_ground
        assert helpers.fisclose(result.ground_offset, 2.5)

    def test_deserialize_default(self, builder, helpers):
        ModelConfigFB.ModelConfigFBStart(builder)
        builder.Finish(ModelConfigFB.ModelConfigFBEnd(builder))
        fb = ModelConfigFB.ModelConfigFB.GetRootAsModelConfigFB(builder.Output(), 0)
        default = SerializeModelConfig.deserialize(fb)

        assert default
        assert isinstance(default, SerializeModelConfig.ModelConfigData)
        assert default.asset_name is None
        assert not default.lock_to_ground
        assert helpers.fisclose(default.ground_offset, 0.0)


class TestSerializeVehicleModelConfig:
    def test_serdes(self, builder, helpers):
        vehicle_model_config = SerializeVehicleModelConfig.VehicleModelConfigData(
            vehicle_type="type",
            vehicle_color="color",
            vehicle_accessory="accessory",
            vehicle_wear=0.5,
            wheel_type="wheel_type",
            vehicle_actor="actor",
            lock_to_ground=True,
            ground_offset=0.12,
            wheel_combo=["wc1", "wc2"],
            wheel_combo_style=["wcs1", "wcs2", "wcs3"],
            accessories=["a1", "a2", "a3", "a4"],
            occupants=["o1", "o2", "o3", "o4", "o5"],
        )
        builder.Finish(SerializeVehicleModelConfig.serialize(builder, vehicle_model_config))
        fb = VehicleModelConfigFB.VehicleModelConfigFB.GetRootAsVehicleModelConfigFB(builder.Output(), 0)
        result = SerializeVehicleModelConfig.deserialize(fb)

        assert result
        assert isinstance(result, SerializeVehicleModelConfig.VehicleModelConfigData)
        assert result.vehicle_type == "type"
        assert result.vehicle_color == "color"
        assert result.vehicle_accessory == "accessory"
        assert helpers.fisclose(result.vehicle_wear, 0.5)
        assert result.wheel_type == "wheel_type"
        assert result.vehicle_actor == "actor"
        assert result.lock_to_ground
        assert helpers.fisclose(result.ground_offset, 0.12)
        assert result.wheel_combo == ["wc1", "wc2"]
        assert result.wheel_combo_style == ["wcs1", "wcs2", "wcs3"]
        assert result.accessories == ["a1", "a2", "a3", "a4"]
        assert result.occupants == ["o1", "o2", "o3", "o4", "o5"]

    def test_deserialize_default(self, builder, helpers):
        VehicleModelConfigFB.VehicleModelConfigFBStart(builder)
        builder.Finish(VehicleModelConfigFB.VehicleModelConfigFBEnd(builder))
        fb = VehicleModelConfigFB.VehicleModelConfigFB.GetRootAsVehicleModelConfigFB(builder.Output(), 0)
        default = SerializeVehicleModelConfig.deserialize(fb)

        assert default
        assert isinstance(default, SerializeVehicleModelConfig.VehicleModelConfigData)
        assert default.vehicle_type is None
        assert default.vehicle_color is None
        assert default.vehicle_accessory is None
        assert default.vehicle_wear == 0.0
        assert default.wheel_type is None
        assert default.vehicle_actor is None
        assert not default.lock_to_ground
        assert default.ground_offset == 0.0
        assert default.wheel_combo == []
        assert default.wheel_combo_style == []
        assert default.accessories == []
        assert default.occupants == []


class TestSerializeSimpleVehicleState:
    def test_serdes(self, builder):
        simple_vehicle_state = SerializeSimpleVehicleState.SimpleVehicleStateData(
            wheel_to_world=[
                Pose6D.from_translation(1.1, 1.2, 1.3).as_transformation_matrix(),
                Pose6D.from_translation(2.1, 2.2, 2.3).as_transformation_matrix(),
                Pose6D.from_translation(3.1, 3.2, 3.3).as_transformation_matrix(),
            ],
            emergency_lights_on=True,
            brake_light_on=True,
            headlight_on=True,
        )
        builder.Finish(SerializeSimpleVehicleState.serialize(builder, simple_vehicle_state))
        fb = SimpleVehicleStateFB.SimpleVehicleStateFB.GetRootAsSimpleVehicleStateFB(builder.Output(), 0)
        result = SerializeSimpleVehicleState.deserialize(fb)

        assert result
        assert isinstance(result, SerializeSimpleVehicleState.SimpleVehicleStateData)
        assert len(result.wheel_to_world) == 3
        assert isinstance(result.wheel_to_world[0], np.ndarray)
        assert np.allclose(result.wheel_to_world[0], Pose6D.from_translation(1.1, 1.2, 1.3).as_transformation_matrix())
        assert isinstance(result.wheel_to_world[1], np.ndarray)
        assert np.allclose(result.wheel_to_world[1], Pose6D.from_translation(2.1, 2.2, 2.3).as_transformation_matrix())
        assert isinstance(result.wheel_to_world[2], np.ndarray)
        assert np.allclose(result.wheel_to_world[2], Pose6D.from_translation(3.1, 3.2, 3.3).as_transformation_matrix())
        assert result.emergency_lights_on
        assert result.brake_light_on
        assert result.headlight_on

    def test_deserialize_default(self, builder, helpers):
        SimpleVehicleStateFB.SimpleVehicleStateFBStart(builder)
        builder.Finish(SimpleVehicleStateFB.SimpleVehicleStateFBEnd(builder))
        fb = SimpleVehicleStateFB.SimpleVehicleStateFB.GetRootAsSimpleVehicleStateFB(builder.Output(), 0)
        default = SerializeSimpleVehicleState.deserialize(fb)

        assert default
        assert isinstance(default, SerializeSimpleVehicleState.SimpleVehicleStateData)
        assert len(default.wheel_to_world) == 0
        assert not default.emergency_lights_on
        assert not default.brake_light_on
        assert not default.headlight_on  # expect headlights to be off by default


class TestSerializeControlState:
    def test_serdes(self, builder):
        control_state = SerializeControlState.ControlStateData(indicator_state=VehicleIndicatorState.Left)
        builder.Finish(SerializeControlState.serialize(builder, control_state))
        fb = ControlStateFB.ControlStateFB.GetRootAsControlStateFB(builder.Output(), 0)
        result = SerializeControlState.deserialize(fb)

        assert result
        assert result.indicator_state == VehicleIndicatorState.Left

    def test_deserialize_default(self, builder, helpers):
        ControlStateFB.ControlStateFBStart(builder)
        builder.Finish(ControlStateFB.ControlStateFBEnd(builder))
        fb = ControlStateFB.ControlStateFB.GetRootAsControlStateFB(builder.Output(), 0)
        default = SerializeControlState.deserialize(fb)

        assert default
        assert isinstance(default, SerializeControlState.ControlStateData)
        assert default.indicator_state == VehicleIndicatorState.Inactive


class TestSerializeSimpleControlState:
    def test_serdes(self, builder):
        simple_control_state = SerializeSimpleControlState.SimpleControlStateData()
        builder.Finish(SerializeSimpleControlState.serialize(builder, simple_control_state))
        fb = SimpleControlStateFB.SimpleControlStateFB.GetRootAsSimpleControlStateFB(builder.Output(), 0)
        result = SerializeSimpleControlState.deserialize(fb)

        assert result

    def test_deserialize_default(self, builder, helpers):
        SimpleControlStateFB.SimpleControlStateFBStart(builder)
        builder.Finish(SimpleControlStateFB.SimpleControlStateFBEnd(builder))
        fb = SimpleControlStateFB.SimpleControlStateFB.GetRootAsSimpleControlStateFB(builder.Output(), 0)
        default = SerializeSimpleControlState.deserialize(fb)

        assert default
        assert isinstance(default, SerializeSimpleControlState.SimpleControlStateData)


class TestSerializeSignalModuleOutput:
    def test_serdes(self, builder, helpers):
        signal_module_output = SerializeSignalModuleOutput.SignalModuleOutputData(
            elapsed_time=123.45,
            phase_bulb_values=[
                PhaseBulbValue(
                    phase=42, red=1.1, yellow=1.2, green=1.3, logical_state=PhaseBulbLogicalState.RedFlashing
                ),
                PhaseBulbValue(phase=43, red=2.1, yellow=2.2, green=2.3, logical_state=PhaseBulbLogicalState.Green),
                PhaseBulbValue(phase=44, red=3.1, yellow=3.2, green=3.3, logical_state=PhaseBulbLogicalState.Red),
            ],
        )
        builder.Finish(SerializeSignalModuleOutput.serialize(builder, signal_module_output))
        fb = SignalModuleOutputFB.SignalModuleOutputFB.GetRootAsSignalModuleOutputFB(builder.Output(), 0)
        result = SerializeSignalModuleOutput.deserialize(fb)

        assert result
        assert isinstance(result, SerializeSignalModuleOutput.SignalModuleOutputData)
        assert helpers.fisclose(result.elapsed_time, 123.45)
        assert len(signal_module_output.phase_bulb_values) == 3
        assert signal_module_output.phase_bulb_values[0].phase == 42
        assert signal_module_output.phase_bulb_values[0].logical_state == PhaseBulbLogicalState.RedFlashing
        assert signal_module_output.phase_bulb_values[1].phase == 43
        assert signal_module_output.phase_bulb_values[1].logical_state == PhaseBulbLogicalState.Green
        assert signal_module_output.phase_bulb_values[2].phase == 44
        assert signal_module_output.phase_bulb_values[2].logical_state == PhaseBulbLogicalState.Red

    def test_deserialize_default(self, builder, helpers):
        SignalModuleOutputFB.SignalModuleOutputFBStart(builder)
        builder.Finish(SignalModuleOutputFB.SignalModuleOutputFBEnd(builder))
        fb = SignalModuleOutputFB.SignalModuleOutputFB.GetRootAsSignalModuleOutputFB(builder.Output(), 0)
        default = SerializeSignalModuleOutput.deserialize(fb)

        assert default
        assert isinstance(default, SerializeSignalModuleOutput.SignalModuleOutputData)
        assert helpers.fisclose(default.elapsed_time, 0.0)
        assert len(default.phase_bulb_values) == 0


class TestSerializePedestrianState:
    def test_serdes(self, builder):
        control_state = SerializePedestrianState.PedestrianStateData(animation_data="test animation data")
        builder.Finish(SerializePedestrianState.serialize(builder, control_state))
        fb = PedestrianStateFB.PedestrianStateFB.GetRootAsPedestrianStateFB(builder.Output(), 0)
        result = SerializePedestrianState.deserialize(fb)

        assert result
        assert result.animation_data == "test animation data"

    def test_deserialize_default(self, builder, helpers):
        PedestrianStateFB.PedestrianStateFBStart(builder)
        builder.Finish(PedestrianStateFB.PedestrianStateFBEnd(builder))
        fb = PedestrianStateFB.PedestrianStateFB.GetRootAsPedestrianStateFB(builder.Output(), 0)
        default = SerializePedestrianState.deserialize(fb)

        assert default
        assert isinstance(default, SerializePedestrianState.PedestrianStateData)
        assert default.animation_data is None


class TestSerializeEnvironmentConfig:
    def test_serdes(self, builder, helpers):
        environment_config = SerializeEnvironmentConfig.EnvironmentConfigData(
            parking_config=ParkingConfig(
                angle=42,
                delineation_color=(1.3, 4.5, 6.7),
                delineation_wear_amount=0.82,
                parking_space_tint=(0.1, 0.2, 0.3),
                parking_space_grunge_amount=0.123,
                lot_parking_delineation_type=LotParkingDelineationType.Random,
                street_parking_delineation_type=StreetParkingDelineationType.DoubleOpen,
                street_parking_angle_zero_override=StreetParkingAngleZeroOverride.Dashed,
                parking_space_material=ParkingSpaceMaterial.MI_ParkingTiles_CobbleStone_01,
                global_parking_decal_wear=0.456,
            )
        )
        builder.Finish(SerializeEnvironmentConfig.serialize(builder, environment_config))
        fb = EnvironmentConfigFB.EnvironmentConfigFB.GetRootAsEnvironmentConfigFB(builder.Output(), 0)
        result = SerializeEnvironmentConfig.deserialize(fb)

        assert result
        assert result.parking_config
        assert result.parking_config.angle == 42
        assert helpers.fisclose(result.parking_config.delineation_color[0], 1.3)
        assert helpers.fisclose(result.parking_config.delineation_color[1], 4.5)
        assert helpers.fisclose(result.parking_config.delineation_color[2], 6.7)
        assert helpers.fisclose(result.parking_config.delineation_wear_amount, 0.82)
        assert helpers.fisclose(result.parking_config.parking_space_tint[0], 0.1)
        assert helpers.fisclose(result.parking_config.parking_space_tint[1], 0.2)
        assert helpers.fisclose(result.parking_config.parking_space_tint[2], 0.3)
        assert helpers.fisclose(result.parking_config.parking_space_grunge_amount, 0.123)
        assert result.parking_config.lot_parking_delineation_type == LotParkingDelineationType.Random
        assert result.parking_config.street_parking_delineation_type == StreetParkingDelineationType.DoubleOpen
        assert result.parking_config.street_parking_angle_zero_override == StreetParkingAngleZeroOverride.Dashed
        assert result.parking_config.parking_space_material == ParkingSpaceMaterial.MI_ParkingTiles_CobbleStone_01
        assert helpers.fisclose(result.parking_config.global_parking_decal_wear, 0.456)

    def test_deserialize_default(self, builder, helpers):
        EnvironmentConfigFB.EnvironmentConfigFBStart(builder)
        builder.Finish(EnvironmentConfigFB.EnvironmentConfigFBEnd(builder))
        fb = EnvironmentConfigFB.EnvironmentConfigFB.GetRootAsEnvironmentConfigFB(builder.Output(), 0)
        default = SerializeEnvironmentConfig.deserialize(fb)

        assert default
        assert isinstance(default, SerializeEnvironmentConfig.EnvironmentConfigData)
        assert default.parking_config is None


class TestSerializeObjectDecorationsInfo:
    def test_serdes(self, builder, helpers):
        object_decorations_info = SerializeObjectDecorationsInfo.ObjectDecorationsInfoData(
            object_decorations={
                10756: ObjectDecorations(
                    type=DecorationObjectType.Lane,
                    object_id=56,
                    decorations={
                        20: DecorationPreset(preset_name="test preset", variant=4567),
                        13: ParkingSpaceDecal(decal_preset="test decal preset"),
                    },
                ),
                345: ObjectDecorations(
                    type=DecorationObjectType.Lane,
                    object_id=89,
                    decorations={
                        8374: PaintTexture(color_rgb=(4.5, 6.7, 7.8), wear=0.84),
                        3984: "test string decoration",
                    },
                ),
            }
        )
        builder.Finish(SerializeObjectDecorationsInfo.serialize(builder, object_decorations_info))
        fb = ObjectDecorationsInfoFB.ObjectDecorationsInfoFB.GetRootAsObjectDecorationsInfoFB(builder.Output(), 0)
        result = SerializeObjectDecorationsInfo.deserialize(fb)

        assert result
        assert result.object_decorations
        assert len(result.object_decorations.items()) == 2
        object_decorations = result.object_decorations.get(10756, None)
        assert object_decorations
        assert object_decorations.type == DecorationObjectType.Lane
        assert object_decorations.object_id == 56
        assert object_decorations.decorations
        assert len(object_decorations.decorations.items()) == 2
        decorations = object_decorations.decorations.get(20, None)
        assert isinstance(decorations, DecorationPreset)
        assert decorations.preset_name == "test preset"
        assert decorations.variant == 4567
        decorations = object_decorations.decorations.get(13, None)
        assert isinstance(decorations, ParkingSpaceDecal)
        assert decorations.decal_preset == "test decal preset"
        object_decorations = result.object_decorations.get(345, None)
        assert object_decorations
        assert object_decorations.type == DecorationObjectType.Lane
        assert object_decorations.object_id == 89
        assert object_decorations.decorations
        assert len(object_decorations.decorations.items()) == 2
        decorations = object_decorations.decorations.get(8374, None)
        assert isinstance(decorations, PaintTexture)
        assert helpers.fisclose(decorations.color_rgb[0], 4.5)
        assert helpers.fisclose(decorations.color_rgb[1], 6.7)
        assert helpers.fisclose(decorations.color_rgb[2], 7.8)
        assert helpers.fisclose(decorations.wear, 0.84)

    def test_serdes_enums_as_int(self, builder, helpers):
        object_decorations_info = SerializeObjectDecorationsInfo.ObjectDecorationsInfoData(
            object_decorations={
                10756: ObjectDecorations(type=0, object_id=56, decorations={}),
            }
        )
        builder.Finish(SerializeObjectDecorationsInfo.serialize(builder, object_decorations_info))
        fb = ObjectDecorationsInfoFB.ObjectDecorationsInfoFB.GetRootAsObjectDecorationsInfoFB(builder.Output(), 0)
        result = SerializeObjectDecorationsInfo.deserialize(fb)

        assert result
        assert result.object_decorations
        object_decorations = result.object_decorations.get(10756, None)
        assert object_decorations
        assert object_decorations.type == DecorationObjectType.Lane

    def test_deserialize_default(self, builder, helpers):
        ObjectDecorationsInfoFB.ObjectDecorationsInfoFBStart(builder)
        builder.Finish(ObjectDecorationsInfoFB.ObjectDecorationsInfoFBEnd(builder))
        fb = ObjectDecorationsInfoFB.ObjectDecorationsInfoFB.GetRootAsObjectDecorationsInfoFB(builder.Output(), 0)
        default = SerializeObjectDecorationsInfo.deserialize(fb)

        assert default
        assert isinstance(default, SerializeObjectDecorationsInfo.ObjectDecorationsInfoData)
        assert default.object_decorations == {}


class TestSerializeVehiclePhysicsConfig:
    def test_serdes(self, builder, helpers):
        mat1 = np.array(
            [
                [1.1, 1.2, 1.3, 1.4],
                [2.1, 2.2, 2.3, 2.4],
                [3.1, 3.2, 3.3, 3.4],
                [4.1, 4.2, 4.3, 4.4],
            ],
            dtype=np.float32,
        )
        mat2 = np.array(
            [
                [1.0, 2.0, 3.0, 4.0],
                [5.0, 6.0, 7.0, 8.0],
                [9.0, 10.0, 11.0, 12.0],
                [13.0, 14.0, 15.0, 16.0],
            ],
            dtype=np.float32,
        )
        vehicle_physics_config = SerializeVehiclePhysicsConfig.VehiclePhysicsConfigData(
            connections=[(42, mat1), (1234, mat2)]
        )
        builder.Finish(SerializeVehiclePhysicsConfig.serialize(builder, vehicle_physics_config))
        fb = VehiclePhysicsConfigFB.VehiclePhysicsConfigFB.GetRootAsVehiclePhysicsConfigFB(builder.Output(), 0)
        result = SerializeVehiclePhysicsConfig.deserialize(fb)

        assert result
        assert isinstance(result, SerializeVehiclePhysicsConfig.VehiclePhysicsConfigData)
        assert len(result.connections) == 2
        assert result.connections[0][0] == 42
        assert isinstance(result.connections[0][1], np.ndarray)
        assert np.allclose(result.connections[0][1], mat1)
        assert result.connections[1][0] == 1234
        assert isinstance(result.connections[1][1], np.ndarray)
        assert np.allclose(result.connections[1][1], mat2)

    def test_deserialize_default(self, builder, helpers):
        VehiclePhysicsConfigFB.VehiclePhysicsConfigFBStart(builder)
        builder.Finish(VehiclePhysicsConfigFB.VehiclePhysicsConfigFBEnd(builder))
        fb = VehiclePhysicsConfigFB.VehiclePhysicsConfigFB.GetRootAsVehiclePhysicsConfigFB(builder.Output(), 0)
        default = SerializeVehiclePhysicsConfig.deserialize(fb)

        assert default
        assert isinstance(default, SerializeVehiclePhysicsConfig.VehiclePhysicsConfigData)
        assert len(default.connections) == 0
