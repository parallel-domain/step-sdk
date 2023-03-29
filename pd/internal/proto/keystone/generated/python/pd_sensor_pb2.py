# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_sensor.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpd_sensor.proto\x12\x08keystone\";\n\tLidarBeam\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0f\n\x07\x61zimuth\x18\x02 \x02(\x02\x12\x11\n\televation\x18\x03 \x02(\x02\"\x95\x01\n\x10LidarNoiseParams\x12\x10\n\x08min_dist\x18\x01 \x01(\x02\x12\x10\n\x08max_dist\x18\x02 \x01(\x02\x12\x10\n\x08min_prob\x18\x03 \x01(\x02\x12\x10\n\x08max_prob\x18\x04 \x01(\x02\x12\x12\n\nmin_offset\x18\x05 \x01(\x02\x12\x12\n\nmax_offset\x18\x06 \x01(\x02\x12\x11\n\tmin_noise\x18\x07 \x01(\x02\"=\n\rAlbedoWeights\x12\x0c\n\x01x\x18\x01 \x01(\x02:\x01\x31\x12\x0e\n\x01y\x18\x02 \x01(\x02:\x03\x30.8\x12\x0e\n\x01z\x18\x03 \x01(\x02:\x03\x30.4\"\x9d\x04\n\x14LidarIntensityParams\x12%\n\x18retro_range_noise_stddev\x18\x01 \x01(\x02:\x03\x30.1\x12%\n\x1aretroreflection_noise_mean\x18\x02 \x01(\x02:\x01\x30\x12)\n\x1cretroreflection_noise_stddev\x18\x03 \x01(\x02:\x03\x30.1\x12%\n\x18max_attenuation_distance\x18\x04 \x01(\x02:\x03\x32\x32\x30\x12$\n\x17retro_intensity_enhance\x18\x05 \x01(\x02:\x03\x31.5\x12#\n\x18intensity_specular_scale\x18\x06 \x01(\x02:\x01\x32\x12&\n\x19intensity_roughness_scale\x18\x07 \x01(\x02:\x03\x31.5\x12\x19\n\x0e\x62\x65\x61m_intensity\x18\x08 \x01(\x02:\x01\x32\x12/\n\x0e\x61lbedo_weights\x18\t \x01(\x0b\x32\x17.keystone.AlbedoWeights\x12\x17\n\nmax_albedo\x18\n \x01(\x02:\x03\x32.2\x12+\n\x1estrong_retro_intensity_enhance\x18\x0b \x01(\x02:\x03\x31.5\x12%\n\x18intensity_metallic_scale\x18\x0c \x01(\x02:\x03\x31.5\x12\x1a\n\remissive_gate\x18\r \x01(\x02:\x03\x31\x30\x30\x12\x1d\n\x11max_emissive_rate\x18\x0e \x01(\x02:\x02\x31\x30\"\xb7\x02\n\x0f\x41liceLidarModel\x12\x15\n\rnumber_points\x18\x01 \x01(\x05\x12\x1b\n\x13min_elevation_angle\x18\x02 \x01(\x02\x12\x1b\n\x13max_elevation_angle\x18\x03 \x01(\x02\x12!\n\x19min_dense_elevation_angle\x18\x04 \x01(\x02\x12!\n\x19max_dense_elevation_angle\x18\x05 \x01(\x02\x12\x19\n\x11min_azimuth_angle\x18\x06 \x01(\x02\x12\x19\n\x11max_azimuth_angle\x18\x07 \x01(\x02\x12\x1d\n\x15sparse_radian_spacing\x18\x08 \x01(\x02\x12\x1c\n\x14\x64\x65nse_radian_spacing\x18\t \x01(\x02\x12\x1a\n\x12horizontal_spacing\x18\n \x01(\x02\"\x8b\x07\n\x0eLidarIntrinsic\x12\x13\n\x0bsample_rate\x18\x01 \x02(\x02\x12\x15\n\rrotation_rate\x18\x02 \x02(\x02\x12\x13\n\x0b\x61zimuth_min\x18\x03 \x01(\x02\x12\x13\n\x0b\x61zimuth_max\x18\x04 \x01(\x02\x12&\n\tbeam_data\x18\x05 \x03(\x0b\x32\x13.keystone.LidarBeam\x12\x13\n\x0b\x63\x61pture_rgb\x18\x06 \x01(\x08\x12\x19\n\x11\x63\x61pture_intensity\x18\x07 \x01(\x08\x12\x15\n\rcapture_depth\x18\x08 \x01(\x08\x12\x17\n\x0f\x63\x61pture_normals\x18\t \x01(\x08\x12\x1c\n\x14\x63\x61pture_segmentation\x18\n \x01(\x08\x12\x18\n\x10\x63\x61pture_instance\x18\x0b \x01(\x08\x12\x1a\n\x12\x63\x61pture_detections\x18\x0c \x01(\x08\x12\x1d\n\x15\x63\x61pture_motionvectors\x18\r \x01(\x08\x12 \n\x14minimum_range_cutoff\x18\x0e \x01(\x02:\x02\x36\x30\x12!\n\x14maximum_range_cutoff\x18\x0f \x01(\x02:\x03\x31\x35\x30\x12\x1e\n\x13minimum_cutoff_prob\x18\x15 \x01(\x02:\x01\x30\x12!\n\x13maximum_cutoff_prob\x18\x16 \x01(\x02:\x04\x30.95\x12\x1d\n\x0eminimum_offset\x18\x17 \x01(\x02:\x05\x30.002\x12\x1c\n\x0emaximum_offset\x18\x18 \x01(\x02:\x04\x30.02\x12\x1c\n\rminimum_noise\x18\x19 \x01(\x02:\x05\x30.001\x12\x1b\n\x10range_noise_mean\x18\x10 \x01(\x02:\x01\x30\x12!\n\x12range_noise_stddev\x18\x11 \x01(\x02:\x05\x30.005\x12\x38\n\x10intensity_params\x18\x12 \x01(\x0b\x32\x1e.keystone.LidarIntensityParams\x12\x34\n\x11\x61lice_lidar_model\x18\x13 \x01(\x0b\x32\x19.keystone.AliceLidarModel\x12\x0f\n\x07pattern\x18\x14 \x01(\t\x12\x13\n\x0btime_offset\x18\x1a \x01(\x02\x12\x15\n\rmulti_returns\x18\x1b \x01(\x05\x12\x15\n\rmerge_returns\x18\x1c \x01(\x05\x12\x1a\n\x12\x63\x61pture_properties\x18\x1d \x01(\x08\x12%\n\x1d\x63\x61pture_backwardmotionvectors\x18\x1e \x01(\x08\"\xdb\x01\n\x10\x44istortionParams\x12\n\n\x02k1\x18\x01 \x01(\x02\x12\n\n\x02k2\x18\x02 \x01(\x02\x12\n\n\x02k3\x18\x03 \x01(\x02\x12\n\n\x02k4\x18\x04 \x01(\x02\x12\n\n\x02k5\x18\x05 \x01(\x02\x12\n\n\x02k6\x18\x06 \x01(\x02\x12\n\n\x02p1\x18\x07 \x01(\x02\x12\n\n\x02p2\x18\x08 \x01(\x02\x12\x0c\n\x04skew\x18\t \x01(\x02\x12\x12\n\nis_fisheye\x18\n \x01(\x08\x12\n\n\x02\x66x\x18\x0b \x01(\x02\x12\n\n\x02\x66y\x18\x0c \x01(\x02\x12\n\n\x02\x63x\x18\r \x01(\x02\x12\n\n\x02\x63y\x18\x0e \x01(\x02\x12\x15\n\rfisheye_model\x18\x0f \x01(\x05\"3\n\x0fPostProcessNode\x12\x10\n\x08material\x18\x01 \x02(\t\x12\x0e\n\x06weight\x18\x02 \x02(\x02\"\x8f\x03\n\x11PostProcessParams\x12#\n\x15\x65xposure_compensation\x18\x01 \x01(\x02:\x04-100\x12\x19\n\x11\x65xposure_speed_up\x18\x02 \x01(\x02\x12\x1b\n\x13\x65xposure_speed_down\x18\x03 \x01(\x02\x12 \n\x12\x65xposure_min_ev100\x18\x04 \x01(\x02:\x04-100\x12 \n\x12\x65xposure_max_ev100\x18\x05 \x01(\x02:\x04-100\x12\x1e\n\x16\x65xposure_metering_mask\x18\x06 \x01(\t\x12\x1f\n\x12motion_blur_amount\x18\x07 \x01(\x02:\x03\x31.5\x12\x1a\n\x0fmotion_blur_max\x18\x08 \x01(\x02:\x01\x35\x12\x1e\n\x12\x64of_focal_distance\x18\t \x01(\x02:\x02-1\x12\x1d\n\x15\x64of_depth_blur_amount\x18\n \x01(\x02\x12!\n\x15\x64of_depth_blur_radius\x18\x0b \x01(\x02:\x02-1\x12\x1a\n\x12vignette_intensity\x18\x0c \x01(\x02\"\x98\x05\n\x0bNoiseParams\x12\x1a\n\x0c\x65nable_bayer\x18\x01 \x01(\x08:\x04true\x12 \n\x12\x65nable_gauss_noise\x18\x02 \x01(\x08:\x04true\x12\"\n\x14\x65nable_poisson_noise\x18\x03 \x01(\x08:\x04true\x12\x1c\n\x0e\x65nable_denoise\x18\x04 \x01(\x08:\x04true\x12 \n\x11gauss_noise_sigma\x18\x05 \x01(\x02:\x05\x30.025\x12\"\n\x14poisson_noise_lambda\x18\x06 \x01(\x02:\x04\x31\x30\x30\x30\x12>\n\x0e\x64\x65noise_filter\x18\x07 \x01(\x0e\x32\x17.keystone.DenoiseFilter:\rMEDIAN_FILTER\x12\x1e\n\x13\x64\x65noise_filter_size\x18\x08 \x01(\x05:\x01\x33\x12\x1c\n\x11\x62ilateral_sigma_d\x18\t \x01(\x02:\x01\x33\x12\x1d\n\x11\x62ilateral_sigma_r\x18\n \x01(\x02:\x02\x32\x30\x12\x1f\n\x11\x65nable_auto_noise\x18\x0b \x01(\x08:\x04true\x12\x1b\n\rsignal_amount\x18\x0c \x01(\x05:\x04\x35\x32\x32\x33\x12!\n\x13pre_amplifier_noise\x18\r \x01(\x02:\x04\x37.63\x12#\n\x14post_amplifier_noise\x18\x0e \x01(\x02:\x05\x32\x34\x37.5\x12\x1a\n\x0cis_using_iso\x18\x0f \x01(\x08:\x04true\x12\x16\n\tiso_level\x18\x10 \x01(\x05:\x03\x38\x30\x30\x12\x17\n\x0f\x65nable_auto_iso\x18\x11 \x01(\x08\x12\x10\n\x05\x66stop\x18\x12 \x01(\x02:\x01\x31\x12 \n\x11max_exposure_time\x18\x13 \x01(\x02:\x05\x30.033\x12\x1f\n\x12quantum_efficiency\x18\x14 \x01(\x02:\x03\x30.7\"\xc2\x05\n\x0f\x43\x61meraIntrinsic\x12\r\n\x05width\x18\x01 \x02(\x05\x12\x0e\n\x06height\x18\x02 \x02(\x05\x12\x0b\n\x03\x66ov\x18\x03 \x01(\x02\x12\x13\n\x0bsupersample\x18\x04 \x01(\x02\x12\x13\n\x0b\x63\x61pture_rgb\x18\x05 \x01(\x08\x12\x15\n\rcapture_depth\x18\x06 \x01(\x08\x12\x17\n\x0f\x63\x61pture_normals\x18\x07 \x01(\x08\x12\x1c\n\x14\x63\x61pture_segmentation\x18\x08 \x01(\x08\x12\x18\n\x10\x63\x61pture_instance\x18\t \x01(\x08\x12\x1a\n\x12\x63\x61pture_detections\x18\n \x01(\x08\x12\x1d\n\x15\x63\x61pture_motionvectors\x18\x0b \x01(\x08\x12\x0b\n\x03lut\x18\x0c \x01(\t\x12\x15\n\nlut_weight\x18\r \x01(\x02:\x01\x31\x12\x38\n\x13post_process_params\x18\x0e \x01(\x0b\x32\x1b.keystone.PostProcessParams\x12/\n\x0cpost_process\x18\x0f \x03(\x0b\x32\x19.keystone.PostProcessNode\x12\x35\n\x11\x64istortion_params\x18\x10 \x01(\x0b\x32\x1a.keystone.DistortionParams\x12+\n\x0cnoise_params\x18\x11 \x01(\x0b\x32\x15.keystone.NoiseParams\x12\x18\n\x10\x65nable_streaming\x18\x12 \x01(\x08\x12\x15\n\rtransmit_gray\x18\x13 \x01(\x08\x12\x1f\n\x17\x64istortion_lookup_table\x18\x14 \x01(\t\x12\x19\n\x11\x63\x61pture_basecolor\x18\x15 \x01(\x08\x12\x1a\n\x12\x63\x61pture_properties\x18\x16 \x01(\x08\x12\x13\n\x0btime_offset\x18\x17 \x01(\x02\x12%\n\x1d\x63\x61pture_backwardmotionvectors\x18\x18 \x01(\x08\"\xa4\x03\n\x14RadarBasicParameters\x12\x18\n\tmax_range\x18\x01 \x01(\x02:\x05\x32\x30\x34.8\x12\x1d\n\x10range_resolution\x18\x02 \x01(\x02:\x03\x30.8\x12\x17\n\x0bmax_doppler\x18\x03 \x01(\x02:\x02\x33\x30\x12\x1f\n\x12\x64oppler_resolution\x18\x04 \x01(\x02:\x03\x30.2\x12\x18\n\x0b\x61zimuth_fov\x18\x05 \x01(\x02:\x03\x31\x31\x30\x12\x1d\n\x12\x61zimuth_resolution\x18\x06 \x01(\x02:\x01\x31\x12\x19\n\relevation_fov\x18\x07 \x01(\x02:\x02\x33\x32\x12\x1f\n\x14\x65levation_resolution\x18\x08 \x01(\x02:\x01\x32\x12\x1e\n\x0fradar_output_2d\x18\t \x01(\x08:\x05\x66\x61lse\x12 \n\x12use_random_raycast\x18\n \x01(\x08:\x04true\x12$\n\x15number_rays_per_frame\x18\x0b \x01(\x05:\x05\x33\x30\x30\x30\x30\x12\x1d\n\x10\x61zimuth_accuracy\x18\x0c \x01(\x02:\x03\x30.5\x12\x1d\n\x12\x65levation_accuracy\x18\r \x01(\x02:\x01\x31\"\xde\x01\n\x15RadarEnergyParameters\x12\x19\n\x0cnominal_gain\x18\x01 \x01(\x02:\x03\x31\x32\x30\x12\x1a\n\x0fgain_jitter_std\x18\x02 \x01(\x02:\x01\x35\x12\"\n\x17radiometric_coefficient\x18\x03 \x01(\x02:\x01\x34\x12G\n\x16\x62\x65\x61m_pattern_file_path\x18\x04 \x01(\t:\'../tools/beam_pattern_77ghz_radians.csv\x12!\n\x13\x65nable_beam_pattern\x18\x05 \x01(\x08:\x04true\"\x98\x01\n\x14RadarNoiseParameters\x12\"\n\x14\x65nable_thermal_noise\x18\x01 \x01(\x08:\x04true\x12\x1c\n\x11thermal_noise_std\x18\x02 \x01(\x02:\x01\x33\x12\x1e\n\x12thermal_noise_mean\x18\x03 \x01(\x02:\x02\x31\x35\x12\x1e\n\x10\x65nable_doa_noise\x18\x04 \x01(\x08:\x04true\"\xb6\x01\n\x17RadarDetectorParameters\x12(\n\rdetector_type\x18\x01 \x01(\t:\x11\x43ONSTANT_DETECTOR\x12\"\n\x16\x64\x65tector_constant_gain\x18\x02 \x01(\x02:\x02\x33\x30\x12&\n\x19\x64\x65tector_radiometric_gain\x18\x03 \x01(\x02:\x03\x31\x30\x30\x12%\n\x1a\x64\x65tector_radiometric_decay\x18\x04 \x01(\x02:\x01\x34\"\x80\x02\n\x0eRadarIntrinsic\x12\x38\n\x10\x62\x61sic_parameters\x18\x01 \x01(\x0b\x32\x1e.keystone.RadarBasicParameters\x12:\n\x11\x65nergy_parameters\x18\x02 \x01(\x0b\x32\x1f.keystone.RadarEnergyParameters\x12\x38\n\x10noise_parameters\x18\x03 \x01(\x0b\x32\x1e.keystone.RadarNoiseParameters\x12>\n\x13\x64\x65tector_parameters\x18\x04 \x01(\x0b\x32!.keystone.RadarDetectorParameters\"\xa1\x01\n\x0fSensorExtrinsic\x12\x0b\n\x03yaw\x18\x01 \x02(\x02\x12\r\n\x05pitch\x18\x02 \x02(\x02\x12\x0c\n\x04roll\x18\x03 \x02(\x02\x12\t\n\x01x\x18\x04 \x02(\x02\x12\t\n\x01y\x18\x05 \x02(\x02\x12\t\n\x01z\x18\x06 \x02(\x02\x12\x13\n\x0block_to_yaw\x18\x07 \x01(\x08\x12\x15\n\rattach_socket\x18\x08 \x01(\t\x12\x17\n\x0f\x66ollow_rotation\x18\t \x01(\x08\"\x8e\x02\n\x0cSensorConfig\x12\x14\n\x0c\x64isplay_name\x18\x01 \x02(\t\x12\x35\n\x10\x63\x61mera_intrinsic\x18\x02 \x01(\x0b\x32\x19.keystone.CameraIntrinsicH\x00\x12\x33\n\x0flidar_intrinsic\x18\x03 \x01(\x0b\x32\x18.keystone.LidarIntrinsicH\x00\x12\x33\n\x0fradar_intrinsic\x18\x04 \x01(\x0b\x32\x18.keystone.RadarIntrinsicH\x00\x12\x33\n\x10sensor_extrinsic\x18\x05 \x02(\x0b\x32\x19.keystone.SensorExtrinsicB\x12\n\x10sensor_intrinsic\"\x1d\n\nSensorList\x12\x0f\n\x07sensors\x18\x01 \x03(\t\"\x9c\x01\n\x0fSensorRigConfig\x12.\n\x0esensor_configs\x18\x01 \x03(\x0b\x32\x16.keystone.SensorConfig\x12\x1f\n\x17sensor_rig_artifact_uid\x18\x02 \x01(\t\x12\x38\n\x1a\x64\x65\x66\x61ult_sensor_splits_list\x18\x03 \x03(\x0b\x32\x14.keystone.SensorList*d\n\rDenoiseFilter\x12\x12\n\x0e\x41VERAGE_FILTER\x10\x00\x12\x11\n\rMEDIAN_FILTER\x10\x01\x12\x16\n\x12\x46\x41ST_MEDIAN_FILTER\x10\x02\x12\x14\n\x10\x42ILATERAL_FILTER\x10\x03')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_sensor_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DENOISEFILTER._serialized_start=6000
  _DENOISEFILTER._serialized_end=6100
  _LIDARBEAM._serialized_start=29
  _LIDARBEAM._serialized_end=88
  _LIDARNOISEPARAMS._serialized_start=91
  _LIDARNOISEPARAMS._serialized_end=240
  _ALBEDOWEIGHTS._serialized_start=242
  _ALBEDOWEIGHTS._serialized_end=303
  _LIDARINTENSITYPARAMS._serialized_start=306
  _LIDARINTENSITYPARAMS._serialized_end=847
  _ALICELIDARMODEL._serialized_start=850
  _ALICELIDARMODEL._serialized_end=1161
  _LIDARINTRINSIC._serialized_start=1164
  _LIDARINTRINSIC._serialized_end=2071
  _DISTORTIONPARAMS._serialized_start=2074
  _DISTORTIONPARAMS._serialized_end=2293
  _POSTPROCESSNODE._serialized_start=2295
  _POSTPROCESSNODE._serialized_end=2346
  _POSTPROCESSPARAMS._serialized_start=2349
  _POSTPROCESSPARAMS._serialized_end=2748
  _NOISEPARAMS._serialized_start=2751
  _NOISEPARAMS._serialized_end=3415
  _CAMERAINTRINSIC._serialized_start=3418
  _CAMERAINTRINSIC._serialized_end=4124
  _RADARBASICPARAMETERS._serialized_start=4127
  _RADARBASICPARAMETERS._serialized_end=4547
  _RADARENERGYPARAMETERS._serialized_start=4550
  _RADARENERGYPARAMETERS._serialized_end=4772
  _RADARNOISEPARAMETERS._serialized_start=4775
  _RADARNOISEPARAMETERS._serialized_end=4927
  _RADARDETECTORPARAMETERS._serialized_start=4930
  _RADARDETECTORPARAMETERS._serialized_end=5112
  _RADARINTRINSIC._serialized_start=5115
  _RADARINTRINSIC._serialized_end=5371
  _SENSOREXTRINSIC._serialized_start=5374
  _SENSOREXTRINSIC._serialized_end=5535
  _SENSORCONFIG._serialized_start=5538
  _SENSORCONFIG._serialized_end=5808
  _SENSORLIST._serialized_start=5810
  _SENSORLIST._serialized_end=5839
  _SENSORRIGCONFIG._serialized_start=5842
  _SENSORRIGCONFIG._serialized_end=5998
# @@protoc_insertion_point(module_scope)