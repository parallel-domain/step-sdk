# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: options.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\roptions.proto\x12\x07pd.data\x1a google/protobuf/descriptor.proto*\x8e\x02\n\x08\x44\x61taType\x12\t\n\x05\x65None\x10\x00\x12\n\n\x06\x65Image\x10\x01\x12\t\n\x05\x65Mesh\x10\x02\x12\x0c\n\x08\x65MeshMap\x10\x03\x12\t\n\x05\x65Null\x10\x04\x12\x11\n\reTransformMap\x10\x05\x12\x0b\n\x07\x65Sensor\x10\x06\x12\x0e\n\neMeshIDMap\x10\x07\x12\x0f\n\x0b\x65PointCloud\x10\x08\x12\x0f\n\x0b\x65\x41nnotation\x10\t\x12\x08\n\x04\x65UMD\x10\n\x12\r\n\teSimState\x10\x0b\x12 \n\x1c\x65\x43\x61meraDistortionCalibration\x10\x0c\x12\x12\n\x0e\x65\x43onfiguration\x10\r\x12\x0f\n\x0b\x65IGMetadata\x10\x0e\x12\x15\n\x11\x65SemanticLabelMap\x10\x0f*%\n\nStreamType\x12\n\n\x06\x65Input\x10\x00\x12\x0b\n\x07\x65Output\x10\x01*>\n\x10StreamDimensions\x12\x0b\n\x07\x65Single\x10\x00\x12\t\n\x05\x65Time\x10\x01\x12\x12\n\x0e\x65SensorAndTime\x10\x02*1\n\nSensorType\x12\x0b\n\x07\x65\x43\x61mera\x10\x00\x12\n\n\x06\x65LiDAR\x10\x01\x12\n\n\x06\x65Radar\x10\x02*1\n\x10MotionVectorMode\x12\r\n\teForwards\x10\x00\x12\x0e\n\neBackwards\x10\x01:@\n\x04type\x12\x1d.google.protobuf.FieldOptions\x18\xd0\x86\x03 \x01(\x0e\x32\x11.pd.data.DataType:D\n\x06stream\x12\x1d.google.protobuf.FieldOptions\x18\xd1\x86\x03 \x01(\x0e\x32\x13.pd.data.StreamTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'options_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(type)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stream)

  DESCRIPTOR._options = None
  _DATATYPE._serialized_start=61
  _DATATYPE._serialized_end=331
  _STREAMTYPE._serialized_start=333
  _STREAMTYPE._serialized_end=370
  _STREAMDIMENSIONS._serialized_start=372
  _STREAMDIMENSIONS._serialized_end=434
  _SENSORTYPE._serialized_start=436
  _SENSORTYPE._serialized_end=485
  _MOTIONVECTORMODE._serialized_start=487
  _MOTIONVECTORMODE._serialized_end=536
# @@protoc_insertion_point(module_scope)
