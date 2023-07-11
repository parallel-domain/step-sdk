from pd.internal.proto.keystone.generated.wrapper.pd_sensor_pb2 import SensorConfig, CameraIntrinsic, DistortionParams


class TestSensorConfig:
    def test_instantiating_intrinsics_with_distortion_parameters_work(self) -> None:
        # This effectively tests nested proto wrapper access and assignment works
        sensor_config = SensorConfig(
            display_name="name",
            camera_intrinsic=CameraIntrinsic(width=1920, distortion_params=DistortionParams(cx=420)),
        )

        assert sensor_config.display_name == "name"
        assert sensor_config.camera_intrinsic.width == 1920
        assert sensor_config.camera_intrinsic.distortion_params.cx == 420

    def test_reassigning_intrinsics_works(self) -> None:
        sensor_config = SensorConfig(
            display_name="name",
            camera_intrinsic=CameraIntrinsic(width=1920, distortion_params=DistortionParams(cx=420)),
        )
        sensor_config.camera_intrinsic = CameraIntrinsic(width=400, distortion_params=DistortionParams(cx=10))

        assert sensor_config.camera_intrinsic.width == 400
        assert sensor_config.camera_intrinsic.distortion_params.cx == 10
        assert sensor_config.proto.camera_intrinsic is sensor_config.camera_intrinsic.proto
        assert (
            sensor_config.proto.camera_intrinsic.distortion_params
            is sensor_config.camera_intrinsic.distortion_params.proto
        )

    def test_it_references_assigned_object_after_setter(self) -> None:
        sensor_config = SensorConfig(
            display_name="name",
            camera_intrinsic=CameraIntrinsic(width=1920, distortion_params=DistortionParams(cx=420)),
        )
        old_intrinsic = sensor_config.camera_intrinsic
        new_intrinsic = CameraIntrinsic(width=400, distortion_params=DistortionParams(cx=10))
        sensor_config.camera_intrinsic = new_intrinsic

        assert sensor_config.camera_intrinsic is not old_intrinsic
        assert sensor_config.camera_intrinsic is new_intrinsic
