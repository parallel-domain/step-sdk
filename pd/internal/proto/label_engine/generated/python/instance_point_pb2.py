# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_point.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14instance_point.proto\x12\x07pd.data\x1a\roptions.proto\"e\n\x1eInstancePoint3DAnnotatorConfig\x12$\n\x12input_instance_map\x18\x01 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x02 \x01(\tB\x08\x80\xb5\x18\t\x88\xb5\x18\x01\"\xe3\x03\n\x17InstancePoint3DMetadata\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\x12\x37\n\x12trailer_point_data\x18\x02 \x01(\x0b\x32\x19.pd.data.TrailerPointDataH\x00\x12\x37\n\x12vehicle_point_data\x18\x03 \x01(\x0b\x32\x19.pd.data.VehiclePointDataH\x00\x12\x37\n\x12parking_point_data\x18\x04 \x01(\x0b\x32\x19.pd.data.ParkingPointDataH\x00\x12=\n\x15pedestrian_point_data\x18\x05 \x01(\x0b\x32\x1c.pd.data.PedestrianPointDataH\x00\x12\x33\n\x10wheel_point_data\x18\x06 \x01(\x0b\x32\x17.pd.data.WheelPointDataH\x00\x12H\n\x1b\x64rone_autoloader_point_data\x18\x07 \x01(\x0b\x32!.pd.data.DroneAutoLoaderPointDataH\x00\x12\x42\n\x18wheel_stopper_point_data\x18\x08 \x01(\x0b\x32\x1e.pd.data.WheelStopperPointDataH\x00\x42\x06\n\x04\x64\x61ta\"e\n\x1eInstancePoint2DAnnotatorConfig\x12$\n\x12input_instance_map\x18\x01 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x02 \x01(\tB\x08\x80\xb5\x18\t\x88\xb5\x18\x01\"\x92\x04\n\x17InstancePoint2DMetadata\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\x12\x37\n\x12trailer_point_data\x18\x02 \x01(\x0b\x32\x19.pd.data.TrailerPointDataH\x00\x12\x37\n\x12vehicle_point_data\x18\x03 \x01(\x0b\x32\x19.pd.data.VehiclePointDataH\x00\x12\x37\n\x12parking_point_data\x18\x04 \x01(\x0b\x32\x19.pd.data.ParkingPointDataH\x00\x12=\n\x15pedestrian_point_data\x18\x05 \x01(\x0b\x32\x1c.pd.data.PedestrianPointDataH\x00\x12\x33\n\x10wheel_point_data\x18\x06 \x01(\x0b\x32\x17.pd.data.WheelPointDataH\x00\x12H\n\x1b\x64rone_autoloader_point_data\x18\x07 \x01(\x0b\x32!.pd.data.DroneAutoLoaderPointDataH\x00\x12\x42\n\x18wheel_stopper_point_data\x18\x08 \x01(\x0b\x32\x1e.pd.data.WheelStopperPointDataH\x00\x12\x12\n\nvisibility\x18\t \x01(\x08\x12\x19\n\x11\x64istance_from_ego\x18\n \x01(\x02\x42\x06\n\x04\x64\x61ta\"\xc1\x02\n\x10TrailerPointData\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.pd.data.TrailerPointData.TrailerPointType\x12\x12\n\nother_name\x18\x02 \x01(\t\"\xde\x01\n\x10TrailerPointType\x12\x0e\n\nHITCH_BALL\x10\x00\x12\x0f\n\x0b\x42OTTOM_LEFT\x10\x01\x12\x11\n\rBOTTOM_CENTER\x10\x02\x12\x10\n\x0c\x42OTTOM_RIGHT\x10\x03\x12\x0c\n\x08TOP_LEFT\x10\x04\x12\r\n\tTOP_RIGHT\x10\x05\x12\x19\n\x15\x44RAWBAR_TRIANGLE_LEFT\x10\x06\x12\x1a\n\x16\x44RAWBAR_TRIANGLE_RIGHT\x10\x07\x12\x10\n\x0c\x44RAWBAR_NECK\x10\x08\x12\x0f\n\x0bTONGUE_JACK\x10\t\x12\r\n\tACCESSORY\x10\n\"\x98\x01\n\x10ParkingPointData\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.pd.data.ParkingPointData.ParkingPointType\"J\n\x10ParkingPointType\x12\x0c\n\x08\x43ORNER_1\x10\x00\x12\x0c\n\x08\x43ORNER_2\x10\x01\x12\x0c\n\x08\x43ORNER_3\x10\x02\x12\x0c\n\x08\x43ORNER_4\x10\x03\"\xcd\x01\n\x10VehiclePointData\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32*.pd.data.VehiclePointData.VehiclePointType\"\x7f\n\x10VehiclePointType\x12\x0e\n\nFRONT_LEFT\x10\x00\x12\x0f\n\x0b\x46RONT_RIGHT\x10\x01\x12\r\n\tREAR_LEFT\x10\x02\x12\x0e\n\nREAR_RIGHT\x10\x03\x12\x0e\n\nEGO_CENTER\x10\x04\x12\x0c\n\x08\x45GO_LEFT\x10\x05\x12\r\n\tEGO_RIGHT\x10\x06\"\xa3\x02\n\x18\x44roneAutoLoaderPointData\x12H\n\x04type\x18\x01 \x01(\x0e\x32:.pd.data.DroneAutoLoaderPointData.DroneAutoLoaderPointType\"\xbc\x01\n\x18\x44roneAutoLoaderPointType\x12\r\n\tARM_A_TIP\x10\x00\x12\x1a\n\x16\x41RM_A_SUPPORT_JUNCTION\x10\x01\x12\x14\n\x10\x41RM_A_REAR_MOUNT\x10\x02\x12\x0e\n\nARM_A_BASE\x10\x03\x12\r\n\tARM_B_TIP\x10\x04\x12\x1a\n\x16\x41RM_B_SUPPORT_JUNCTION\x10\x05\x12\x14\n\x10\x41RM_B_REAR_MOUNT\x10\x06\x12\x0e\n\nARM_B_BASE\x10\x07\"\xad\x01\n\x0eWheelPointData\x12\x34\n\x04type\x18\x01 \x01(\x0e\x32&.pd.data.WheelPointData.WheelPointType\"e\n\x0eWheelPointType\x12\x0e\n\nFRONT_LEFT\x10\x00\x12\x0f\n\x0b\x46RONT_RIGHT\x10\x01\x12\r\n\tREAR_LEFT\x10\x02\x12\x0e\n\nREAR_RIGHT\x10\x03\x12\t\n\x05\x46RONT\x10\x04\x12\x08\n\x04\x42\x41\x43K\x10\x05\"\x8b\x03\n\x13PedestrianPointData\x12>\n\x04type\x18\x01 \x01(\x0e\x32\x30.pd.data.PedestrianPointData.PedestrianPointType\"\xb3\x02\n\x13PedestrianPointType\x12\x08\n\x04ROOT\x10\x00\x12\x08\n\x04NECK\x10\x01\x12\x08\n\x04NOSE\x10\x02\x12\x0c\n\x08LEFT_EYE\x10\x03\x12\r\n\tRIGHT_EYE\x10\x04\x12\x0c\n\x08LEFT_EAR\x10\x05\x12\r\n\tRIGHT_EAR\x10\x06\x12\x11\n\rLEFT_SHOULDER\x10\x07\x12\x12\n\x0eRIGHT_SHOULDER\x10\x08\x12\x0e\n\nLEFT_ELBOW\x10\t\x12\x0f\n\x0bRIGHT_ELBOW\x10\n\x12\x0e\n\nLEFT_WRIST\x10\x0b\x12\x0f\n\x0bRIGHT_WRIST\x10\x0c\x12\x0c\n\x08LEFT_HIP\x10\r\x12\r\n\tRIGHT_HIP\x10\x0e\x12\r\n\tLEFT_KNEE\x10\x0f\x12\x0e\n\nRIGHT_KNEE\x10\x10\x12\x0e\n\nLEFT_ANKLE\x10\x11\x12\x0f\n\x0bRIGHT_ANKLE\x10\x12\"\x95\x01\n\x15WheelStopperPointData\x12\x42\n\x04type\x18\x01 \x01(\x0e\x32\x34.pd.data.WheelStopperPointData.WheelStopperPointType\"8\n\x15WheelStopperPointType\x12\x0e\n\nLEFT_POINT\x10\x00\x12\x0f\n\x0bRIGHT_POINT\x10\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'instance_point_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSTANCEPOINT3DANNOTATORCONFIG.fields_by_name['input_instance_map']._options = None
  _INSTANCEPOINT3DANNOTATORCONFIG.fields_by_name['input_instance_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _INSTANCEPOINT3DANNOTATORCONFIG.fields_by_name['output_path']._options = None
  _INSTANCEPOINT3DANNOTATORCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\t\210\265\030\001'
  _INSTANCEPOINT2DANNOTATORCONFIG.fields_by_name['input_instance_map']._options = None
  _INSTANCEPOINT2DANNOTATORCONFIG.fields_by_name['input_instance_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _INSTANCEPOINT2DANNOTATORCONFIG.fields_by_name['output_path']._options = None
  _INSTANCEPOINT2DANNOTATORCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\t\210\265\030\001'
  _INSTANCEPOINT3DANNOTATORCONFIG._serialized_start=48
  _INSTANCEPOINT3DANNOTATORCONFIG._serialized_end=149
  _INSTANCEPOINT3DMETADATA._serialized_start=152
  _INSTANCEPOINT3DMETADATA._serialized_end=635
  _INSTANCEPOINT2DANNOTATORCONFIG._serialized_start=637
  _INSTANCEPOINT2DANNOTATORCONFIG._serialized_end=738
  _INSTANCEPOINT2DMETADATA._serialized_start=741
  _INSTANCEPOINT2DMETADATA._serialized_end=1271
  _TRAILERPOINTDATA._serialized_start=1274
  _TRAILERPOINTDATA._serialized_end=1595
  _TRAILERPOINTDATA_TRAILERPOINTTYPE._serialized_start=1373
  _TRAILERPOINTDATA_TRAILERPOINTTYPE._serialized_end=1595
  _PARKINGPOINTDATA._serialized_start=1598
  _PARKINGPOINTDATA._serialized_end=1750
  _PARKINGPOINTDATA_PARKINGPOINTTYPE._serialized_start=1676
  _PARKINGPOINTDATA_PARKINGPOINTTYPE._serialized_end=1750
  _VEHICLEPOINTDATA._serialized_start=1753
  _VEHICLEPOINTDATA._serialized_end=1958
  _VEHICLEPOINTDATA_VEHICLEPOINTTYPE._serialized_start=1831
  _VEHICLEPOINTDATA_VEHICLEPOINTTYPE._serialized_end=1958
  _DRONEAUTOLOADERPOINTDATA._serialized_start=1961
  _DRONEAUTOLOADERPOINTDATA._serialized_end=2252
  _DRONEAUTOLOADERPOINTDATA_DRONEAUTOLOADERPOINTTYPE._serialized_start=2064
  _DRONEAUTOLOADERPOINTDATA_DRONEAUTOLOADERPOINTTYPE._serialized_end=2252
  _WHEELPOINTDATA._serialized_start=2255
  _WHEELPOINTDATA._serialized_end=2428
  _WHEELPOINTDATA_WHEELPOINTTYPE._serialized_start=2327
  _WHEELPOINTDATA_WHEELPOINTTYPE._serialized_end=2428
  _PEDESTRIANPOINTDATA._serialized_start=2431
  _PEDESTRIANPOINTDATA._serialized_end=2826
  _PEDESTRIANPOINTDATA_PEDESTRIANPOINTTYPE._serialized_start=2519
  _PEDESTRIANPOINTDATA_PEDESTRIANPOINTTYPE._serialized_end=2826
  _WHEELSTOPPERPOINTDATA._serialized_start=2829
  _WHEELSTOPPERPOINTDATA._serialized_end=2978
  _WHEELSTOPPERPOINTDATA_WHEELSTOPPERPOINTTYPE._serialized_start=2922
  _WHEELSTOPPERPOINTDATA_WHEELSTOPPERPOINTTYPE._serialized_end=2978
# @@protoc_insertion_point(module_scope)
