# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_recook.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0fpd_recook.proto\x12\x08keystone\"\xd7\x02\n\x06Recook\x12\x14\n\x0c\x61rtifact_key\x18\x01 \x01(\t\x12\x1b\n\x13output_artifact_uid\x18\x02 \x01(\t\x12\x1f\n\x17\x63ode_build_artifact_uid\x18\x03 \x01(\t\x12\x17\n\x0f\x62\x61se_changelist\x18\x04 \x01(\t\x12\x1b\n\x13unshelve_changelist\x18\x05 \x01(\t\x12\x1c\n\x14levelcook_batch_size\x18\x06 \x01(\x05\x12\x13\n\x0b\x64o_reimport\x18\x07 \x01(\x08\x12\x30\n\rlocation_list\x18\x08 \x03(\x0b\x32\x19.keystone.Recook.Location\x1a^\n\x08Location\x12$\n\x1clocation_output_artifact_uid\x18\x01 \x01(\t\x12\x15\n\rlocation_name\x18\x02 \x01(\t\x12\x15\n\rlocation_guid\x18\x03 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_recook_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RECOOK._serialized_start=30
  _RECOOK._serialized_end=373
  _RECOOK_LOCATION._serialized_start=279
  _RECOOK_LOCATION._serialized_end=373
# @@protoc_insertion_point(module_scope)
