# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgpv1/image.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import geometry_pb2 as dgpv1_dot_geometry__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x64gpv1/image.proto\x12\tdgp.proto\x1a\x14\x64gpv1/geometry.proto\x1a\x19google/protobuf/any.proto\"\xce\x02\n\x05Image\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\x12\x10\n\x08\x63hannels\x18\x04 \x01(\x05\x12\x36\n\x0b\x61nnotations\x18\x05 \x03(\x0b\x32!.dgp.proto.Image.AnnotationsEntry\x12\x30\n\x08metadata\x18\x06 \x03(\x0b\x32\x1e.dgp.proto.Image.MetadataEntry\x12\x1d\n\x04pose\x18\x07 \x01(\x0b\x32\x0f.dgp.proto.Pose\x1a\x32\n\x10\x41nnotationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x45\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dgpv1.image_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IMAGE_ANNOTATIONSENTRY._options = None
  _IMAGE_ANNOTATIONSENTRY._serialized_options = b'8\001'
  _IMAGE_METADATAENTRY._options = None
  _IMAGE_METADATAENTRY._serialized_options = b'8\001'
  _IMAGE._serialized_start=82
  _IMAGE._serialized_end=416
  _IMAGE_ANNOTATIONSENTRY._serialized_start=295
  _IMAGE_ANNOTATIONSENTRY._serialized_end=345
  _IMAGE_METADATAENTRY._serialized_start=347
  _IMAGE_METADATAENTRY._serialized_end=416
# @@protoc_insertion_point(module_scope)
