# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_environments.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import pd_distributions_pb2 as pd__distributions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pd_environments.proto\x12\x08keystone\x1a\x16pd_distributions.proto\"\xa0\x02\n\x11\x45nvironmentPreset\x12\x36\n\x0btime_of_day\x18\x01 \x01(\x0b\x32!.keystone.CategoricalDistribution\x12.\n\x0e\x63loud_coverage\x18\x02 \x01(\x0b\x32\x16.keystone.Distribution\x12.\n\x0erain_intensity\x18\x03 \x01(\x0b\x32\x16.keystone.Distribution\x12-\n\rfog_intensity\x18\x04 \x01(\x0b\x32\x16.keystone.Distribution\x12\'\n\x07wetness\x18\x05 \x01(\x0b\x32\x16.keystone.Distribution\x12\x1b\n\x13independent_wetness\x18\x06 \x01(\x08\"\x85\x01\n\x15\x45nvironmentDefinition\x12>\n\x13preset_distribution\x18\x01 \x01(\x0b\x32!.keystone.CategoricalDistribution\x12,\n\x07presets\x18\x02 \x03(\x0b\x32\x1b.keystone.EnvironmentPresetb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_environments_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENVIRONMENTPRESET._serialized_start=60
  _ENVIRONMENTPRESET._serialized_end=348
  _ENVIRONMENTDEFINITION._serialized_start=351
  _ENVIRONMENTDEFINITION._serialized_end=484
# @@protoc_insertion_point(module_scope)
