# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgpv1/remote.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x64gpv1/remote.proto\x12\tdgp.proto\"\x1b\n\nRemotePath\x12\r\n\x05value\x18\x01 \x01(\t\"Q\n\x0eRemoteArtifact\x12\"\n\x03url\x18\x01 \x01(\x0b\x32\x15.dgp.proto.RemotePath\x12\x0c\n\x04sha1\x18\x02 \x01(\t\x12\r\n\x05isdir\x18\x03 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dgpv1.remote_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REMOTEPATH._serialized_start=33
  _REMOTEPATH._serialized_end=60
  _REMOTEARTIFACT._serialized_start=62
  _REMOTEARTIFACT._serialized_end=143
# @@protoc_insertion_point(module_scope)
