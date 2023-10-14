import json

import numpy as np
import pytest

from pd.state.pose6d import Pose6D
from pd.state.sensor import CameraSensor, DenoiseFilter, LiDARSensor, sensors_from_json


class TestCameraSensor:
    def test_default_instance(self):
        sensor = CameraSensor(name="test", pose=Pose6D(), width=1920, height=1080, field_of_view_degrees=90)
        assert sensor.name == "test"
        assert sensor.width == 1920
        assert sensor.height == 1080


class TestLiDARSensor:
    def test_default_instance(self):
        sensor = LiDARSensor(name="test", pose=Pose6D(), sample_rate=1.0, rotation_rate=2.0)
        assert sensor.name == "test"
        assert sensor.sample_rate == 1.0
        assert sensor.rotation_rate == 2.0


@pytest.fixture
def load_sensor_config(resources):
    """Returns a method to load sensor configs given the config file name"""

    def load(filename):
        with open(resources / "sensor_rigs" / filename) as file:
            return json.load(file)

    return load


def test_load_sensors_from_json_dict_1(load_sensor_config):
    json_dict = load_sensor_config("minimal.json")
    sensors = sensors_from_json(json_dict)
    assert len(sensors) == 1
    sensor = sensors[0]
    assert isinstance(sensor, CameraSensor)
    assert sensor.name == "Front"
    assert sensor.width == 1920
    assert sensor.height == 1080
    assert sensor.field_of_view_degrees == 65
    assert sensor.lut == "Texture2D'/Game/pd/Textures/LUT/LUT_PD_DashCamMedia.LUT_PD_DashCamMedia'"
    assert sensor.lut_weight == 0.5
    assert len(sensor.post_process_materials) == 1
    assert (
        sensor.post_process_materials[0].material
        == "MaterialInstanceConstant'/Game/pd/material/vfx/MI_lensDistortion_NoLens.MI_lensDistortion_NoLens'"
    )
    assert sensor.post_process_materials[0].weight == 1.0
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert sensor.capture_motionvectors
    assert sensor.noise_params.enable_bayer
    assert sensor.noise_params.enable_gauss_noise
    assert sensor.noise_params.enable_poisson_noise
    assert sensor.noise_params.enable_denoise
    assert np.array_equal(
        sensor.pose.as_transformation_matrix(),
        Pose6D.from_rpy_angles(
            yaw_degrees=0.0, pitch_degrees=0.0, roll_degrees=0.0, x_metres=0.0, y_metres=0.0, z_metres=2.0
        ).as_transformation_matrix(),
    )


def test_load_sensors_from_json_dict_2(load_sensor_config):
    json_dict = load_sensor_config("minimal_scanning.json")
    sensors = sensors_from_json(json_dict)
    assert len(sensors) == 2
    sensor = sensors[0]
    assert isinstance(sensor, CameraSensor)
    assert sensor.name == "Front"
    assert sensor.width == 1920
    assert sensor.height == 1080
    assert sensor.field_of_view_degrees == 65
    assert sensor.lut == "Texture2D'/Game/pd/Textures/LUT/T_LUT_PD_CameraEmulation.T_LUT_PD_CameraEmulation'"
    assert sensor.lut_weight == 0.1
    assert len(sensor.post_process_materials) == 1
    assert (
        sensor.post_process_materials[0].material
        == "MaterialInstanceConstant'/Game/pd/material/vfx/MI_lensDistortion_NoLens.MI_lensDistortion_NoLens'"
    )
    assert sensor.post_process_materials[0].weight == 1.0
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert sensor.capture_motionvectors
    sensor = sensors[1]
    assert isinstance(sensor, LiDARSensor)
    assert sensor.name == "Front_LiDAR"
    assert sensor.sample_rate == 18000
    assert sensor.rotation_rate == 10
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert sensor.capture_motionvectors
    beam_data = sensor.beam_data
    assert len(beam_data) == 32
    assert beam_data[0].id == 1
    assert beam_data[0].azimuth == -1.4
    assert beam_data[0].elevation == -25.0
    assert beam_data[31].id == 32
    assert beam_data[31].azimuth == 1.4
    assert beam_data[31].elevation == -1.333


def test_load_sensors_from_json_dict_3(load_sensor_config):
    json_dict = load_sensor_config("time_offset_test.json")
    sensors = sensors_from_json(json_dict)
    assert len(sensors) == 1
    sensor = sensors[0]
    assert isinstance(sensor, CameraSensor)
    assert sensor.name == "Front20"
    assert sensor.width == 960
    assert sensor.height == 540
    assert sensor.field_of_view_degrees == 65
    assert sensor.lut == "Texture2D'/Game/pd/Textures/LUT/LUT_PD_DashCamMedia.LUT_PD_DashCamMedia'"
    assert sensor.lut_weight == 0.5
    assert len(sensor.post_process_materials) == 1
    assert (
        sensor.post_process_materials[0].material
        == "MaterialInstanceConstant'/Game/pd/material/vfx/MI_lensDistortion_NoLens.MI_lensDistortion_NoLens'"
    )
    assert sensor.post_process_materials[0].weight == 1.0
    assert sensor.time_offset == 20
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert sensor.capture_motionvectors
    assert sensor.capture_basecolor
    assert sensor.capture_properties
    assert sensor.noise_params
    assert sensor.noise_params.enable_bayer
    assert sensor.noise_params.enable_gauss_noise
    assert sensor.noise_params.enable_poisson_noise
    assert sensor.noise_params.enable_denoise
    assert np.array_equal(
        sensor.pose.as_transformation_matrix(),
        Pose6D.from_rpy_angles(
            yaw_degrees=0.0, pitch_degrees=0.0, roll_degrees=0.0, x_metres=0.0, y_metres=0.0, z_metres=2.0
        ).as_transformation_matrix(),
    )


def test_load_sensors_from_json_dict_4(load_sensor_config, helpers):
    json_dict = load_sensor_config("demo_rig_v2_fisheye.json")
    sensors = sensors_from_json(json_dict)
    assert len(sensors) == 1
    sensor = sensors[0]
    assert isinstance(sensor, CameraSensor)
    assert sensor.name == "FisheyeLeft"
    assert np.array_equal(
        sensor.pose.as_transformation_matrix(),
        Pose6D.from_rpy_angles(
            yaw_degrees=90.0,
            pitch_degrees=-25.004856877359472,
            roll_degrees=-1.501989531760839e-17,
            x_metres=-1.1,
            y_metres=1.2,
            z_metres=1.2,
        ).as_transformation_matrix(),
    )
    assert sensor.width == 3000
    assert sensor.height == 2000
    assert sensor.distortion_params
    assert helpers.fisclose(sensor.distortion_params.fx, 866.0254037844389)
    assert helpers.fisclose(sensor.distortion_params.fy, 866.0254037844389)
    assert helpers.fisclose(sensor.distortion_params.cx, 1500)
    assert helpers.fisclose(sensor.distortion_params.cy, 1000)
    assert sensor.distortion_params.skew == 0
    assert sensor.fisheye_model == 3
    assert sensor.distortion_lookup_table == "customer\\Internal\\sensor_rigs\\fisheye_lookup.csv"
    assert sensor.noise_params
    assert sensor.noise_params.enable_bayer
    assert sensor.noise_params.enable_gauss_noise
    assert sensor.noise_params.enable_poisson_noise
    assert sensor.noise_params.enable_denoise
    assert sensor.noise_params.iso_level == 200
    assert len(sensor.post_process_materials) == 1
    assert (
        sensor.post_process_materials[0].material
        == "MaterialInstanceConstant'/Game/pd/material/vfx/MI_lensDistortion_NoLens.MI_lensDistortion_NoLens'"
    )
    assert sensor.post_process_materials[0].weight == 1.0
    assert sensor.lut == "Texture2D'/Game/pd/Textures/LUT/T_LUT_Aladdin_overcast_01.T_LUT_Aladdin_overcast_01'"
    assert sensor.lut_weight == 0.8
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert sensor.capture_motionvectors


def test_load_sensors_from_json_dict_5(load_sensor_config, helpers):
    json_dict = load_sensor_config("bev_1.json")
    sensors = sensors_from_json(json_dict)
    assert len(sensors) == 1
    sensor = sensors[0]
    assert isinstance(sensor, CameraSensor)
    assert sensor.name == "BEV"
    assert sensor.width == 2000
    assert sensor.height == 2000
    assert sensor.supersample == 1.0
    assert sensor.capture_rgb
    assert sensor.capture_depth
    assert not sensor.capture_normals
    assert sensor.capture_segmentation
    assert sensor.capture_instances
    assert not sensor.capture_motionvectors
    assert sensor.lut == "Texture2D'/Game/pd/Textures/LUT/T_LUT_Aladdin_overcast_01.T_LUT_Aladdin_overcast_01'"
    assert sensor.lut_weight == 0.0
    assert sensor.noise_params.denoise_filter == DenoiseFilter.MedianFilter
    assert len(sensor.post_process_materials) == 1
    assert (
        sensor.post_process_materials[0].material
        == "MaterialInstanceConstant'/Game/pd/material/vfx/MI_lensDistortion_NoLens.MI_lensDistortion_NoLens'"
    )
    assert sensor.post_process_materials[0].weight == 1.0
    assert sensor.distortion_params
    assert sensor.distortion_params.k1 == 0
    assert sensor.distortion_params.k2 == 0
    assert sensor.distortion_params.k3 == 0
    assert sensor.distortion_params.k4 == 0
    assert sensor.distortion_params.k5 == 0
    assert sensor.distortion_params.k6 == 0
    assert sensor.distortion_params.p1 == -200
    assert sensor.distortion_params.p2 == 30
    assert sensor.distortion_params.skew == 0
    assert sensor.distortion_params.fx == 20
    assert sensor.distortion_params.fy == 20
    assert sensor.distortion_params.cx == 1000
    assert sensor.distortion_params.cy == 1000
    assert sensor.distortion_params.is_fisheye is False
    assert sensor.fisheye_model == 6
    assert sensor.noise_params
    assert sensor.noise_params.enable_bayer is False
    assert sensor.noise_params.enable_gauss_noise is False
    assert sensor.noise_params.enable_poisson_noise is False
    assert sensor.noise_params.enable_denoise is False
    assert sensor.noise_params.iso_level == 200
    assert sensor.noise_params.gauss_noise_sigma == 0.025
    assert sensor.noise_params.poisson_noise_lambda == 1000
    assert sensor.noise_params.denoise_filter == DenoiseFilter.MedianFilter
    assert sensor.noise_params.denoise_filter_size == 3
    assert sensor.noise_params.bilateral_sigma_d == 3
    assert sensor.noise_params.bilateral_sigma_r == 20
    assert sensor.noise_params.enable_auto_noise is True
    assert sensor.noise_params.signal_amount == 5223
    assert helpers.fisclose(sensor.noise_params.pre_amplifier_noise, 7.63)
    assert helpers.fisclose(sensor.noise_params.post_amplifier_noise, 247.5)
    assert sensor.noise_params.is_using_iso is True
    assert sensor.noise_params.enable_auto_iso is False
    assert sensor.noise_params.fstop == 1
    assert helpers.fisclose(sensor.noise_params.max_exposure_time, 0.033)
    assert helpers.fisclose(sensor.noise_params.quantum_efficiency, 0.7)
    assert sensor.field_of_view_degrees == 0
    assert sensor.enable_streaming is False
    assert sensor.transmit_gray is False
    assert sensor.distortion_lookup_table is None
    assert sensor.capture_basecolor is False
    assert sensor.capture_properties is False
    assert sensor.time_offset == 0
    assert sensor.lock_to_yaw is False
    assert sensor.attach_socket is None
    assert sensor.follow_rotation is False
