# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: motion_vectors_3d.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17motion_vectors_3d.proto\x12\x07pd.data\x1a\roptions.proto\"\xca\x01\n\x1dGenerateMotionVectors3DConfig\x12-\n\x1binput_point_cloud_positions\x18\x01 \x01(\tB\x08\x80\xb5\x18\x08\x88\xb5\x18\x00\x12$\n\x12input_mesh_mask_3d\x18\x02 \x01(\tB\x08\x80\xb5\x18\x08\x88\xb5\x18\x00\x12\"\n\x1a\x65nable_child_mesh_rotation\x18\x03 \x01(\x08\x12\x11\n\tbackwards\x18\x04 \x01(\x08\x12\x1d\n\x0boutput_path\x18\x05 \x01(\tB\x08\x80\xb5\x18\x08\x88\xb5\x18\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'motion_vectors_3d_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['input_point_cloud_positions']._options = None
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['input_point_cloud_positions']._serialized_options = b'\200\265\030\010\210\265\030\000'
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['input_mesh_mask_3d']._options = None
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['input_mesh_mask_3d']._serialized_options = b'\200\265\030\010\210\265\030\000'
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['output_path']._options = None
  _GENERATEMOTIONVECTORS3DCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\010\210\265\030\001'
  _GENERATEMOTIONVECTORS3DCONFIG._serialized_start=52
  _GENERATEMOTIONVECTORS3DCONFIG._serialized_end=254
# @@protoc_insertion_point(module_scope)