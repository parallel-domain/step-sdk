# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: projection.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10projection.proto\x12\x07pd.data\x1a\roptions.proto\"\xb1\x01\n\x18GenerateProjectionConfig\x12%\n\x13input_annotation_3d\x18\x01 \x01(\tB\x08\x80\xb5\x18\t\x88\xb5\x18\x00\x12$\n\x12input_instance_map\x18\x02 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x03 \x01(\tB\x08\x80\xb5\x18\t\x88\xb5\x18\x01\x12)\n\x0csensor_types\x18\x04 \x03(\x0e\x32\x13.pd.data.SensorTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'projection_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENERATEPROJECTIONCONFIG.fields_by_name['input_annotation_3d']._options = None
  _GENERATEPROJECTIONCONFIG.fields_by_name['input_annotation_3d']._serialized_options = b'\200\265\030\t\210\265\030\000'
  _GENERATEPROJECTIONCONFIG.fields_by_name['input_instance_map']._options = None
  _GENERATEPROJECTIONCONFIG.fields_by_name['input_instance_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _GENERATEPROJECTIONCONFIG.fields_by_name['output_path']._options = None
  _GENERATEPROJECTIONCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\t\210\265\030\001'
  _GENERATEPROJECTIONCONFIG._serialized_start=45
  _GENERATEPROJECTIONCONFIG._serialized_end=222
# @@protoc_insertion_point(module_scope)