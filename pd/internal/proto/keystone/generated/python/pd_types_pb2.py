# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_types.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0epd_types.proto\x12\x08keystone\")\n\x06\x46loat3\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"d\n\x08\x46loat3x3\x12\x1c\n\x02r0\x18\x01 \x01(\x0b\x32\x10.keystone.Float3\x12\x1c\n\x02r1\x18\x02 \x01(\x0b\x32\x10.keystone.Float3\x12\x1c\n\x02r2\x18\x03 \x01(\x0b\x32\x10.keystone.Float3\"S\n\x04Pose\x12\"\n\x08position\x18\x01 \x01(\x0b\x32\x10.keystone.Float3\x12\'\n\x0borientation\x18\x02 \x01(\x0b\x32\x12.keystone.Float3x3b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_types_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FLOAT3._serialized_start=28
  _FLOAT3._serialized_end=69
  _FLOAT3X3._serialized_start=71
  _FLOAT3X3._serialized_end=171
  _POSE._serialized_start=173
  _POSE._serialized_end=256
# @@protoc_insertion_point(module_scope)
