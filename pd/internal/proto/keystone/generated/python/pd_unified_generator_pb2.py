# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_unified_generator.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pd_types_pb2 as pd__types__pb2
from . import pd_distributions_pb2 as pd__distributions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1apd_unified_generator.proto\x12\x08keystone\x1a\x0epd_types.proto\x1a\x16pd_distributions.proto\"\xf5\x01\n\x1aUnifiedGeneratorParameters\x12\x34\n\x07\x61tomics\x18\x01 \x03(\x0b\x32#.keystone.AtomicGeneratorParameters\x12 \n\x11use_merge_batches\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x42\n\x0e\x64\x65\x66\x61ult_params\x18\x03 \x01(\x0b\x32*.keystone.DefaultAtomicGeneratorParameters\x12;\n\x12\x65nvironment_params\x18\x04 \x01(\x0b\x32\x1f.keystone.EnvironmentParameters\"\xd7\x04\n\x19\x41tomicGeneratorParameters\x12:\n\tego_agent\x18\x01 \x01(\x0b\x32%.keystone.EgoAgentGeneratorParametersH\x00\x12\x37\n\x07vehicle\x18\x02 \x01(\x0b\x32$.keystone.VehicleGeneratorParametersH\x00\x12\x37\n\x07traffic\x18\x03 \x01(\x0b\x32$.keystone.TrafficGeneratorParametersH\x00\x12\x45\n\x0fparked_vehicles\x18\x04 \x01(\x0b\x32*.keystone.ParkedVehicleGeneratorParametersH\x00\x12@\n\x0cstatic_agent\x18\x05 \x01(\x0b\x32(.keystone.StaticAgentGeneratorParametersH\x00\x12\x35\n\x06\x64\x65\x62ris\x18\x06 \x01(\x0b\x32#.keystone.DebrisGeneratorParametersH\x00\x12=\n\npedestrian\x18\x07 \x01(\x0b\x32\'.keystone.PedestrianGeneratorParametersH\x00\x12J\n\x11random_pedestrian\x18\x08 \x01(\x0b\x32-.keystone.RandomPedestrianGeneratorParametersH\x00\x12\x33\n\x05\x64rone\x18\t \x01(\x0b\x32\".keystone.DroneGeneratorParametersH\x00\x42\x0c\n\nparameters\"\xe2\x01\n DefaultAtomicGeneratorParameters\x12\x61\n\x14vehicle_distribution\x18\x01 \x03(\x0b\x32\x43.keystone.DefaultAtomicGeneratorParameters.VehicleDistributionEntry\x1a[\n\x18VehicleDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.keystone.VehicleCategoryWeight:\x02\x38\x01\"\x9f\x03\n\x15\x45nvironmentParameters\x12<\n\x16sign_spawn_probability\x18\x01 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x46\n crosswalk_sign_spawn_probability\x18\x02 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12K\n\x0fmarker_data_map\x18\x03 \x03(\x0b\x32\x32.keystone.EnvironmentParameters.MarkerDataMapEntry\x12*\n\x06region\x18\x04 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12\x36\n\x12parking_space_data\x18\x05 \x01(\x0b\x32\x1a.keystone.ParkingSpaceData\x1aO\n\x12MarkerDataMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.keystone.RoadMarkingData:\x02\x38\x01\"\xc4\x05\n\x10ParkingSpaceData\x12M\n\x12\x61ngle_distribution\x18\x01 \x03(\x0b\x32\x31.keystone.ParkingSpaceData.AngleDistributionEntry\x12@\n\x1clot_parking_delineation_type\x18\x02 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12\x43\n\x1fstreet_parking_delineation_type\x18\x03 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12\x46\n\"street_parking_angle_zero_override\x18\x04 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12+\n\x11\x64\x65lineation_color\x18\x05 \x03(\x0b\x32\x10.keystone.Float3\x12=\n\x17\x64\x65lineation_wear_amount\x18\x06 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12:\n\x16parking_space_material\x18\x07 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12,\n\x12parking_space_tint\x18\x08 \x03(\x0b\x32\x10.keystone.Float3\x12\x41\n\x1bparking_space_grunge_amount\x18\t \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12?\n\x19global_parking_decal_wear\x18\n \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x1a\x38\n\x16\x41ngleDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\xb4\x01\n\x0fRoadMarkingData\x12\x19\n\nuse_preset\x18\x01 \x01(\x08:\x05\x66\x61lse\x12-\n\x0foverride_colors\x18\x02 \x03(\x0b\x32\x14.keystone.FloatArray\x12\x15\n\rpreset_colors\x18\x03 \x03(\t\x12\x14\n\x0cmarker_types\x18\x04 \x03(\t\x12*\n\x04wear\x18\x05 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\";\n\x10\x44\x65\x63orationPreset\x12\x13\n\x0bpreset_name\x18\x01 \x02(\t\x12\x12\n\x07variant\x18\x02 \x01(\r:\x01\x30\"\\\n\x0e\x44\x65\x63orationData\x12\x37\n\x11\x64\x65\x63oration_preset\x18\x01 \x01(\x0b\x32\x1a.keystone.DecorationPresetH\x00\x42\x11\n\x0f\x64\x65\x63oration_data\"Y\n\x11ObjectDecorations\x12\x11\n\tobject_id\x18\x01 \x02(\r\x12\x31\n\x0f\x64\x65\x63oration_data\x18\x02 \x02(\x0b\x32\x18.keystone.DecorationData\"o\n\x16ObjectDecorationParams\x12\x1c\n\x0f\x64\x65\x63orate_chance\x18\x01 \x01(\x02:\x03\x30.1\x12\x37\n\x13preset_distribution\x18\x02 \x01(\x0b\x32\x1a.keystone.EnumDistribution\"\x1a\n\nFloatArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\xd0\x02\n\x1b\x45goAgentGeneratorParameters\x12\x30\n\nagent_type\x18\x01 \x01(\x0e\x32\x13.keystone.AgentType:\x07VEHICLE\x12 \n\tego_model\x18\x02 \x01(\t:\rsuv_medium_02\x12\x33\n\x10position_request\x18\x03 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x36\n\x12vehicle_spawn_data\x18\x04 \x01(\x0b\x32\x1a.keystone.VehicleSpawnData\x12<\n\x15pedestrian_spawn_data\x18\x05 \x01(\x0b\x32\x1d.keystone.PedestrianSpawnData\x12\x32\n\x10\x64rone_spawn_data\x18\x06 \x01(\x0b\x32\x18.keystone.DroneSpawnData\"\x98\x01\n\x1aVehicleGeneratorParameters\x12\r\n\x05model\x18\x01 \x01(\t\x12\x33\n\x10position_request\x18\x02 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x36\n\x12vehicle_spawn_data\x18\x03 \x01(\x0b\x32\x1a.keystone.VehicleSpawnData\"\xfe\x05\n\x1aTrafficGeneratorParameters\x12\x33\n\x10position_request\x18\x01 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x1e\n\x11spawn_probability\x18\x02 \x01(\x02:\x03\x30.8\x12\x36\n\x12vehicle_spawn_data\x18\x03 \x01(\x0b\x32\x1a.keystone.VehicleSpawnData\x12[\n\x14vehicle_distribution\x18\x04 \x03(\x0b\x32=.keystone.TrafficGeneratorParameters.VehicleDistributionEntry\x12\x63\n\x19start_separation_time_map\x18\x05 \x03(\x0b\x32@.keystone.TrafficGeneratorParameters.StartSeparationTimeMapEntry\x12\x65\n\x1atarget_separation_time_map\x18\x06 \x03(\x0b\x32\x41.keystone.TrafficGeneratorParameters.TargetSeparationTimeMapEntry\x1a[\n\x18VehicleDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.keystone.VehicleCategoryWeight:\x02\x38\x01\x1a\x65\n\x1bStartSeparationTimeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.keystone.ContinousUniformDistribution:\x02\x38\x01\x1a\x66\n\x1cTargetSeparationTimeMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.keystone.ContinousUniformDistribution:\x02\x38\x01\"\xd0\x02\n ParkedVehicleGeneratorParameters\x12\x33\n\x10position_request\x18\x01 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x37\n\x11spawn_probability\x18\x02 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x61\n\x14vehicle_distribution\x18\x03 \x03(\x0b\x32\x43.keystone.ParkedVehicleGeneratorParameters.VehicleDistributionEntry\x1a[\n\x18VehicleDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0b\x32\x1f.keystone.VehicleCategoryWeight:\x02\x38\x01\"d\n\x1eStaticAgentGeneratorParameters\x12\x33\n\x10position_request\x18\x01 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\r\n\x05model\x18\x02 \x01(\t\"\xae\x03\n\x19\x44\x65\x62risGeneratorParameters\x12\x1f\n\x11spawn_probability\x18\x01 \x01(\x02:\x04\x30.01\x12\x1a\n\x12\x64\x65\x62ris_center_bias\x18\x02 \x01(\x02\x12\x1b\n\x13min_debris_distance\x18\x03 \x01(\x02\x12\x1f\n\x13max_debris_distance\x18\x04 \x01(\x02:\x02\x35\x30\x12.\n\x10\x64\x65\x62ris_asset_tag\x18\x05 \x01(\t:\x14trash_bottle_tall_01\x12\x1f\n\x17\x64\x65\x62ris_asset_remove_tag\x18\x06 \x01(\t\x12\x33\n\x10position_request\x18\x07 \x01(\x0b\x32\x19.keystone.PositionRequest\x12V\n\x12\x61sset_distribution\x18\x08 \x03(\x0b\x32:.keystone.DebrisGeneratorParameters.AssetDistributionEntry\x1a\x38\n\x16\x41ssetDistributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"\x8b\x01\n\x1dPedestrianGeneratorParameters\x12\x33\n\x10position_request\x18\x01 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x35\n\x0eped_spawn_data\x18\x02 \x01(\x0b\x32\x1d.keystone.PedestrianSpawnData\"\xad\x02\n#RandomPedestrianGeneratorParameters\x12\x30\n\x0bspeed_range\x18\x01 \x01(\x0b\x32\x1b.keystone.MinMaxConfigFloat\x12\x33\n\x10position_request\x18\x02 \x01(\x0b\x32\x19.keystone.PositionRequest\x12;\n\x18num_of_pedestrians_range\x18\x03 \x01(\x0b\x32\x19.keystone.MinMaxConfigInt\x12+\n\x1emin_radius_between_pedestrians\x18\x04 \x01(\x02:\x03\x32.4\x12\x35\n\x0eped_spawn_data\x18\x05 \x01(\x0b\x32\x1d.keystone.PedestrianSpawnData\"\x83\x01\n\x18\x44roneGeneratorParameters\x12\x33\n\x10position_request\x18\x01 \x01(\x0b\x32\x19.keystone.PositionRequest\x12\x32\n\x10\x64rone_spawn_data\x18\x02 \x01(\x0b\x32\x18.keystone.DroneSpawnData\"\xc3\x04\n\x0fPositionRequest\x12\x39\n\x13longitudinal_offset\x18\x01 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x34\n\x0elateral_offset\x18\x02 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x30\n\nyaw_offset\x18\x03 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x46\n\x19\x61\x62solute_position_request\x18\x04 \x01(\x0b\x32!.keystone.AbsolutePositionRequestH\x00\x12X\n#path_time_relative_position_request\x18\x05 \x01(\x0b\x32).keystone.PathTimeRelativePositionRequestH\x00\x12W\n\"location_relative_position_request\x18\x06 \x01(\x0b\x32).keystone.LocationRelativePositionRequestH\x00\x12\x36\n\x11lane_spawn_policy\x18\x07 \x01(\x0b\x32\x19.keystone.LaneSpawnPolicyH\x00\x12I\n\x1broad_pitch_position_request\x18\x08 \x01(\x0b\x32\".keystone.RoadPitchPositionRequestH\x00\x42\x0f\n\rposition_type\"m\n\x18LaneCurvatureSpawnPolicy\x12\x35\n\x10\x63urvature_bounds\x18\x01 \x01(\x0b\x32\x1b.keystone.MinMaxConfigFloat\x12\x1a\n\x12min_section_length\x18\x02 \x01(\x02\"[\n\x13JunctionSpawnPolicy\x12\x44\n\x14\x64istance_to_junction\x18\x01 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\"\xbf\x01\n\x18PositionOfInterestPolicy\x12I\n\x1blane_curvature_spawn_policy\x18\x01 \x01(\x0b\x32\".keystone.LaneCurvatureSpawnPolicyH\x00\x12>\n\x15junction_spawn_policy\x18\x02 \x01(\x0b\x32\x1d.keystone.JunctionSpawnPolicyH\x00\x42\x18\n\x16PositionOfInterestType\"\x87\x01\n\x17\x41\x62solutePositionRequest\x12\"\n\x08position\x18\x01 \x01(\x0b\x32\x10.keystone.Float3\x12$\n\x08rotation\x18\x02 \x01(\x0b\x32\x12.keystone.Float3x3\x12\x0f\n\x07lane_id\x18\x03 \x01(\x04\x12\x11\n\tresolve_z\x18\x04 \x01(\x08\"\x8f\x02\n\x1fPathTimeRelativePositionRequest\x12-\n\nagent_tags\x18\x01 \x03(\x0e\x32\x19.keystone.SpecialAgentTag\x12<\n\x0ctime_to_path\x18\x02 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12?\n\x0ftime_along_path\x18\x03 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12>\n\x0eincident_angle\x18\x04 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\"\xa5\x01\n\x1fLocationRelativePositionRequest\x12-\n\nagent_tags\x18\x01 \x03(\x0e\x32\x19.keystone.SpecialAgentTag\x12\x1d\n\x10max_spawn_radius\x18\x02 \x01(\x02:\x03\x31\x35\x30\x12\x34\n\x11lane_spawn_policy\x18\x03 \x01(\x0b\x32\x19.keystone.LaneSpawnPolicy\"\x9c\x04\n\x0fLaneSpawnPolicy\x12\'\n\x1fmin_num_lanes_in_same_direction\x18\x01 \x01(\x05\x12-\n\tlane_type\x18\x02 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12.\n#min_num_lanes_in_opposite_direction\x18\x03 \x01(\x05:\x01\x30\x12\x34\n\x0elateral_offset\x18\x04 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12)\n\x1b\x62icycles_only_in_bike_lanes\x18\x05 \x01(\x08:\x04true\x12\x38\n\x13nearby_asset_policy\x18\x06 \x01(\x0b\x32\x1b.keystone.NearbyAssetPolicy\x12-\n\troad_type\x18\x07 \x01(\x0b\x32\x1a.keystone.EnumDistribution\x12G\n\x1bposition_of_interest_policy\x18\x08 \x03(\x0b\x32\".keystone.PositionOfInterestPolicy\x12\x35\n\x0fmin_path_length\x18\t \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x37\n\x11min_length_behind\x18\n \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\"\xc7\x01\n\x18RoadPitchPositionRequest\x12:\n\nroad_pitch\x18\x01 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x34\n\x11lane_spawn_policy\x18\x02 \x01(\x0b\x32\x19.keystone.LaneSpawnPolicy\x12\x1e\n\x10\x62in_pitch_points\x18\x03 \x01(\x08:\x04true\x12\x19\n\tbin_width\x18\x04 \x01(\x02:\x06\x30.0087\"\x8b\x01\n\x11NearbyAssetPolicy\x12\x33\n\rsearch_radius\x18\x01 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12-\n\nnum_assets\x18\x02 \x01(\x0b\x32\x19.keystone.MinMaxConfigInt\x12\x12\n\nasset_tags\x18\x03 \x03(\t\"\xb4\x01\n\x10VehicleSpawnData\x12\x33\n\x10vehicle_behavior\x18\x01 \x01(\x0b\x32\x19.keystone.VehicleBehavior\x12\x37\n\x12vehicle_peripheral\x18\x02 \x01(\x0b\x32\x1b.keystone.VehiclePeripheral\x12\x32\n\x10\x61gent_spawn_data\x18\x03 \x01(\x0b\x32\x18.keystone.AgentSpawnData\"\xe6\x06\n\x0fVehicleBehavior\x12;\n\x0bstart_speed\x18\x01 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12<\n\x0ctarget_speed\x18\x02 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12!\n\x12ignore_speed_limit\x18\x03 \x01(\x08:\x05\x66\x61lse\x12;\n\x0blane_offset\x18\x04 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12@\n\x10lane_drift_scale\x18\x05 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x44\n\x14lane_drift_amplitude\x18\x06 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12G\n\x17lane_change_probability\x18\x07 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x44\n\x14lane_change_cooldown\x18\x08 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12,\n\x1d\x65nable_dynamic_lane_selection\x18\t \x01(\x08:\x05\x66\x61lse\x12)\n\nstart_gear\x18\n \x01(\x0e\x32\x0e.keystone.Gear:\x05\x44RIVE\x12\x45\n\x15start_separation_time\x18\x0b \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x46\n\x16target_separation_time\x18\x0c \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x42\n\x12vehicle_aggression\x18\r \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12\x35\n\x15ignore_obstacle_types\x18\x0e \x03(\x0e\x32\x16.keystone.ObstacleType\"\x95\x02\n\x11VehiclePeripheral\x12$\n\x19spawn_trailer_probability\x18\x01 \x01(\x02:\x01\x30\x12\x43\n\x13trailer_initial_yaw\x18\x02 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12 \n\x11\x64isable_occupants\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\"\n\x13\x64isable_accessories\x18\x04 \x01(\x08:\x05\x66\x61lse\x12%\n\x17randomize_vehicle_parts\x18\x05 \x01(\x08:\x04true\x12(\n\x1b\x65mergency_light_probability\x18\x06 \x01(\x02:\x03\x30.5\"\xd0\x03\n\x13PedestrianSpawnData\x12K\n%pedestrian_color_override_probability\x18\x01 \x01(\x0b\x32\x1c.keystone.CenterSpreadConfig\x12\x37\n\x1dpedestrian_color_override_rgb\x18\x02 \x01(\x0b\x32\x10.keystone.Float3\x12-\n\x1bpedestrians_dynamic_pathing\x18\x03 \x01(\x08:\x04trueB\x02\x18\x01\x12 \n\x12orient_to_velocity\x18\x04 \x01(\x08:\x04true\x12\x1d\n\x0f\x63heck_occupancy\x18\x05 \x01(\x08:\x04true\x12$\n\x18jaywalker_ego_fwd_offset\x18\x06 \x01(\x02:\x02\x32\x30\x12\x32\n\x10\x61gent_spawn_data\x18\x07 \x01(\x0b\x32\x18.keystone.AgentSpawnData\x12\x32\n\x0cped_behavior\x18\x08 \x01(\x0e\x32\x1c.keystone.PedestrianBehavior\x12#\n\nasset_name\x18\t \x01(\t:\x0f\x63har_hannah_001\x12\x10\n\x05speed\x18\n \x01(\x02:\x01\x31\"\xc7\x02\n\x0e\x44roneSpawnData\x12\x1f\n\x12\x61scend_probability\x18\x01 \x01(\x02:\x03\x30.5\x12%\n\x18ground_asset_probability\x18\x02 \x01(\x02:\x03\x30.5\x12\x15\n\rground_assets\x18\x03 \x03(\t\x12\x17\n\x0f\x66light_path_dir\x18\x04 \x01(\t\x12\x32\n\x10\x61gent_spawn_data\x18\x05 \x01(\x0b\x32\x18.keystone.AgentSpawnData\x12=\n\rheight_offset\x18\x06 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\x12J\n\x1aground_asset_height_offset\x18\x07 \x01(\x0b\x32&.keystone.ContinousUniformDistribution\"9\n\x0e\x41gentSpawnData\x12\'\n\x04tags\x18\x01 \x03(\x0e\x32\x19.keystone.SpecialAgentTag\"]\n\x17SignalLightDistribution\x12\x15\n\x05green\x18\x01 \x01(\x02:\x06\x30.3333\x12\x13\n\x03red\x18\x02 \x01(\x02:\x06\x30.3333\x12\x16\n\x06yellow\x18\x03 \x01(\x02:\x06\x30.3333\"]\n\x14TurnTypeDistribution\x12\x18\n\x08straight\x18\x01 \x01(\x02:\x06\x30.3333\x12\x14\n\x04left\x18\x02 \x01(\x02:\x06\x30.3333\x12\x15\n\x05right\x18\x03 \x01(\x02:\x06\x30.3333\"Z\n\x17ParkingTypeDistribution\x12\x14\n\x07\x66orward\x18\x01 \x01(\x02:\x03\x30.5\x12\x14\n\x07reverse\x18\x02 \x01(\x02:\x03\x30.5\x12\x13\n\x08parallel\x18\x03 \x01(\x02:\x01\x30\"]\n\x1d\x43\x65nterSpreadProbabilityConfig\x12\x16\n\x0bprobability\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06\x63\x65nter\x18\x02 \x01(\x02:\x01\x30\x12\x11\n\x06spread\x18\x03 \x01(\x02:\x01\x30\":\n\x12\x43\x65nterSpreadConfig\x12\x11\n\x06\x63\x65nter\x18\x01 \x01(\x02:\x01\x30\x12\x11\n\x06spread\x18\x02 \x01(\x02:\x01\x30\"=\n\x15\x43\x65nterSpreadConfigInt\x12\x11\n\x06\x63\x65nter\x18\x01 \x01(\x05:\x01\x30\x12\x11\n\x06spread\x18\x02 \x01(\x05:\x01\x30\"3\n\x11MinMaxConfigFloat\x12\x0e\n\x03min\x18\x01 \x01(\x02:\x01\x30\x12\x0e\n\x03max\x18\x02 \x01(\x02:\x01\x30\"1\n\x0fMinMaxConfigInt\x12\x0e\n\x03min\x18\x01 \x01(\x05:\x01\x30\x12\x0e\n\x03max\x18\x02 \x01(\x05:\x01\x30*\x8c\x01\n\tAgentType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07VEHICLE\x10\x01\x12\x12\n\x0ePARKED_VEHICLE\x10\x02\x12\x13\n\x0fTRAILER_VEHICLE\x10\x03\x12\x0e\n\nPEDESTRIAN\x10\x04\x12\x11\n\rSTATIC_OBJECT\x10\x05\x12\t\n\x05\x44RONE\x10\x06\x12\n\n\x06\x41NIMAL\x10\x07*\xde\x01\n\x0cObstacleType\x12\x10\n\x0cROUTE_LENGTH\x10\x00\x12\x14\n\x10REVERSE_DISTANCE\x10\x01\x12\x0c\n\x08PATH_END\x10\x02\x12\x11\n\rFORWARD_AGENT\x10\x03\x12\x12\n\x0eONCOMING_AGENT\x10\x04\x12\x0f\n\x0b\x45ND_OF_LANE\x10\x05\x12\x10\n\x0c\x42LOCKED_LANE\x10\x06\x12\t\n\x05MERGE\x10\x07\x12\x10\n\x0cLINEAR_MOVER\x10\x08\x12\x10\n\x0cLANE_CLOSURE\x10\t\x12\x10\n\x0c\x43ROSSTRAFFIC\x10\n\x12\r\n\tSTOP_LINE\x10\x0b*7\n\x04Gear\x12\n\n\x06PARKED\x10\x01\x12\x0b\n\x07REVERSE\x10\x02\x12\x0b\n\x07NEUTRAL\x10\x03\x12\t\n\x05\x44RIVE\x10\x04*L\n\x12PedestrianBehavior\x12\n\n\x06NORMAL\x10\x01\x12\n\n\x06STATIC\x10\x02\x12\r\n\tJAYWALKER\x10\x03\x12\x0f\n\x0b\x45\x44GESTOPPER\x10\x04*$\n\x0fSpecialAgentTag\x12\x07\n\x03\x45GO\x10\x00\x12\x08\n\x04STAR\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_unified_generator_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DEFAULTATOMICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._options = None
  _DEFAULTATOMICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_options = b'8\001'
  _ENVIRONMENTPARAMETERS_MARKERDATAMAPENTRY._options = None
  _ENVIRONMENTPARAMETERS_MARKERDATAMAPENTRY._serialized_options = b'8\001'
  _PARKINGSPACEDATA_ANGLEDISTRIBUTIONENTRY._options = None
  _PARKINGSPACEDATA_ANGLEDISTRIBUTIONENTRY._serialized_options = b'8\001'
  _TRAFFICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._options = None
  _TRAFFICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_options = b'8\001'
  _TRAFFICGENERATORPARAMETERS_STARTSEPARATIONTIMEMAPENTRY._options = None
  _TRAFFICGENERATORPARAMETERS_STARTSEPARATIONTIMEMAPENTRY._serialized_options = b'8\001'
  _TRAFFICGENERATORPARAMETERS_TARGETSEPARATIONTIMEMAPENTRY._options = None
  _TRAFFICGENERATORPARAMETERS_TARGETSEPARATIONTIMEMAPENTRY._serialized_options = b'8\001'
  _PARKEDVEHICLEGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._options = None
  _PARKEDVEHICLEGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_options = b'8\001'
  _DEBRISGENERATORPARAMETERS_ASSETDISTRIBUTIONENTRY._options = None
  _DEBRISGENERATORPARAMETERS_ASSETDISTRIBUTIONENTRY._serialized_options = b'8\001'
  _PEDESTRIANSPAWNDATA.fields_by_name['pedestrians_dynamic_pathing']._options = None
  _PEDESTRIANSPAWNDATA.fields_by_name['pedestrians_dynamic_pathing']._serialized_options = b'\030\001'
  _AGENTTYPE._serialized_start=10819
  _AGENTTYPE._serialized_end=10959
  _OBSTACLETYPE._serialized_start=10962
  _OBSTACLETYPE._serialized_end=11184
  _GEAR._serialized_start=11186
  _GEAR._serialized_end=11241
  _PEDESTRIANBEHAVIOR._serialized_start=11243
  _PEDESTRIANBEHAVIOR._serialized_end=11319
  _SPECIALAGENTTAG._serialized_start=11321
  _SPECIALAGENTTAG._serialized_end=11357
  _UNIFIEDGENERATORPARAMETERS._serialized_start=81
  _UNIFIEDGENERATORPARAMETERS._serialized_end=326
  _ATOMICGENERATORPARAMETERS._serialized_start=329
  _ATOMICGENERATORPARAMETERS._serialized_end=928
  _DEFAULTATOMICGENERATORPARAMETERS._serialized_start=931
  _DEFAULTATOMICGENERATORPARAMETERS._serialized_end=1157
  _DEFAULTATOMICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_start=1066
  _DEFAULTATOMICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_end=1157
  _ENVIRONMENTPARAMETERS._serialized_start=1160
  _ENVIRONMENTPARAMETERS._serialized_end=1575
  _ENVIRONMENTPARAMETERS_MARKERDATAMAPENTRY._serialized_start=1496
  _ENVIRONMENTPARAMETERS_MARKERDATAMAPENTRY._serialized_end=1575
  _PARKINGSPACEDATA._serialized_start=1578
  _PARKINGSPACEDATA._serialized_end=2286
  _PARKINGSPACEDATA_ANGLEDISTRIBUTIONENTRY._serialized_start=2230
  _PARKINGSPACEDATA_ANGLEDISTRIBUTIONENTRY._serialized_end=2286
  _ROADMARKINGDATA._serialized_start=2289
  _ROADMARKINGDATA._serialized_end=2469
  _DECORATIONPRESET._serialized_start=2471
  _DECORATIONPRESET._serialized_end=2530
  _DECORATIONDATA._serialized_start=2532
  _DECORATIONDATA._serialized_end=2624
  _OBJECTDECORATIONS._serialized_start=2626
  _OBJECTDECORATIONS._serialized_end=2715
  _OBJECTDECORATIONPARAMS._serialized_start=2717
  _OBJECTDECORATIONPARAMS._serialized_end=2828
  _FLOATARRAY._serialized_start=2830
  _FLOATARRAY._serialized_end=2856
  _EGOAGENTGENERATORPARAMETERS._serialized_start=2859
  _EGOAGENTGENERATORPARAMETERS._serialized_end=3195
  _VEHICLEGENERATORPARAMETERS._serialized_start=3198
  _VEHICLEGENERATORPARAMETERS._serialized_end=3350
  _TRAFFICGENERATORPARAMETERS._serialized_start=3353
  _TRAFFICGENERATORPARAMETERS._serialized_end=4119
  _TRAFFICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_start=1066
  _TRAFFICGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_end=1157
  _TRAFFICGENERATORPARAMETERS_STARTSEPARATIONTIMEMAPENTRY._serialized_start=3914
  _TRAFFICGENERATORPARAMETERS_STARTSEPARATIONTIMEMAPENTRY._serialized_end=4015
  _TRAFFICGENERATORPARAMETERS_TARGETSEPARATIONTIMEMAPENTRY._serialized_start=4017
  _TRAFFICGENERATORPARAMETERS_TARGETSEPARATIONTIMEMAPENTRY._serialized_end=4119
  _PARKEDVEHICLEGENERATORPARAMETERS._serialized_start=4122
  _PARKEDVEHICLEGENERATORPARAMETERS._serialized_end=4458
  _PARKEDVEHICLEGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_start=1066
  _PARKEDVEHICLEGENERATORPARAMETERS_VEHICLEDISTRIBUTIONENTRY._serialized_end=1157
  _STATICAGENTGENERATORPARAMETERS._serialized_start=4460
  _STATICAGENTGENERATORPARAMETERS._serialized_end=4560
  _DEBRISGENERATORPARAMETERS._serialized_start=4563
  _DEBRISGENERATORPARAMETERS._serialized_end=4993
  _DEBRISGENERATORPARAMETERS_ASSETDISTRIBUTIONENTRY._serialized_start=4937
  _DEBRISGENERATORPARAMETERS_ASSETDISTRIBUTIONENTRY._serialized_end=4993
  _PEDESTRIANGENERATORPARAMETERS._serialized_start=4996
  _PEDESTRIANGENERATORPARAMETERS._serialized_end=5135
  _RANDOMPEDESTRIANGENERATORPARAMETERS._serialized_start=5138
  _RANDOMPEDESTRIANGENERATORPARAMETERS._serialized_end=5439
  _DRONEGENERATORPARAMETERS._serialized_start=5442
  _DRONEGENERATORPARAMETERS._serialized_end=5573
  _POSITIONREQUEST._serialized_start=5576
  _POSITIONREQUEST._serialized_end=6155
  _LANECURVATURESPAWNPOLICY._serialized_start=6157
  _LANECURVATURESPAWNPOLICY._serialized_end=6266
  _JUNCTIONSPAWNPOLICY._serialized_start=6268
  _JUNCTIONSPAWNPOLICY._serialized_end=6359
  _POSITIONOFINTERESTPOLICY._serialized_start=6362
  _POSITIONOFINTERESTPOLICY._serialized_end=6553
  _ABSOLUTEPOSITIONREQUEST._serialized_start=6556
  _ABSOLUTEPOSITIONREQUEST._serialized_end=6691
  _PATHTIMERELATIVEPOSITIONREQUEST._serialized_start=6694
  _PATHTIMERELATIVEPOSITIONREQUEST._serialized_end=6965
  _LOCATIONRELATIVEPOSITIONREQUEST._serialized_start=6968
  _LOCATIONRELATIVEPOSITIONREQUEST._serialized_end=7133
  _LANESPAWNPOLICY._serialized_start=7136
  _LANESPAWNPOLICY._serialized_end=7676
  _ROADPITCHPOSITIONREQUEST._serialized_start=7679
  _ROADPITCHPOSITIONREQUEST._serialized_end=7878
  _NEARBYASSETPOLICY._serialized_start=7881
  _NEARBYASSETPOLICY._serialized_end=8020
  _VEHICLESPAWNDATA._serialized_start=8023
  _VEHICLESPAWNDATA._serialized_end=8203
  _VEHICLEBEHAVIOR._serialized_start=8206
  _VEHICLEBEHAVIOR._serialized_end=9076
  _VEHICLEPERIPHERAL._serialized_start=9079
  _VEHICLEPERIPHERAL._serialized_end=9356
  _PEDESTRIANSPAWNDATA._serialized_start=9359
  _PEDESTRIANSPAWNDATA._serialized_end=9823
  _DRONESPAWNDATA._serialized_start=9826
  _DRONESPAWNDATA._serialized_end=10153
  _AGENTSPAWNDATA._serialized_start=10155
  _AGENTSPAWNDATA._serialized_end=10212
  _SIGNALLIGHTDISTRIBUTION._serialized_start=10214
  _SIGNALLIGHTDISTRIBUTION._serialized_end=10307
  _TURNTYPEDISTRIBUTION._serialized_start=10309
  _TURNTYPEDISTRIBUTION._serialized_end=10402
  _PARKINGTYPEDISTRIBUTION._serialized_start=10404
  _PARKINGTYPEDISTRIBUTION._serialized_end=10494
  _CENTERSPREADPROBABILITYCONFIG._serialized_start=10496
  _CENTERSPREADPROBABILITYCONFIG._serialized_end=10589
  _CENTERSPREADCONFIG._serialized_start=10591
  _CENTERSPREADCONFIG._serialized_end=10649
  _CENTERSPREADCONFIGINT._serialized_start=10651
  _CENTERSPREADCONFIGINT._serialized_end=10712
  _MINMAXCONFIGFLOAT._serialized_start=10714
  _MINMAXCONFIGFLOAT._serialized_end=10765
  _MINMAXCONFIGINT._serialized_start=10767
  _MINMAXCONFIGINT._serialized_end=10816
# @@protoc_insertion_point(module_scope)
