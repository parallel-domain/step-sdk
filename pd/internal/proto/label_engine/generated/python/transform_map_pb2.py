# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transform_map.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13transform_map.proto\x12\x07pd.data\x1a\x0egeometry.proto\"\x9a\x01\n\x12SocketTransformMap\x12>\n\nsocket_map\x18\x01 \x03(\x0b\x32*.pd.data.SocketTransformMap.SocketMapEntry\x1a\x44\n\x0eSocketMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.pd.data.Transform:\x02\x38\x01\"\x9b\x01\n\x05Value\x12\x14\n\nbool_value\x18\x01 \x01(\x08H\x00\x12\x15\n\x0bint32_value\x18\x02 \x01(\x05H\x00\x12\x15\n\x0bint64_value\x18\x03 \x01(\x03H\x00\x12\x15\n\x0b\x66loat_value\x18\x04 \x01(\x02H\x00\x12\x16\n\x0c\x64ouble_value\x18\x05 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x06 \x01(\tH\x00\x42\x07\n\x05value\"\x7f\n\x08ValueMap\x12\x32\n\tvalue_map\x18\x01 \x03(\x0b\x32\x1f.pd.data.ValueMap.ValueMapEntry\x1a?\n\rValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1d\n\x05value\x18\x02 \x01(\x0b\x32\x0e.pd.data.Value:\x02\x38\x01\"\xd1\x04\n\x0cTransformMap\x12>\n\rtransform_map\x18\x01 \x03(\x0b\x32\'.pd.data.TransformMap.TransformMapEntry\x12K\n\x14socket_transform_map\x18\x02 \x03(\x0b\x32-.pd.data.TransformMap.SocketTransformMapEntry\x12\x36\n\tvalue_map\x18\x03 \x03(\x0b\x32#.pd.data.TransformMap.ValueMapEntry\x12I\n\x13\x61\x63tor_transform_map\x18\x04 \x03(\x0b\x32,.pd.data.TransformMap.ActorTransformMapEntry\x1aG\n\x11TransformMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.pd.data.Transform:\x02\x38\x01\x1aV\n\x17SocketTransformMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.pd.data.SocketTransformMap:\x02\x38\x01\x1a\x42\n\rValueMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.pd.data.ValueMap:\x02\x38\x01\x1aL\n\x16\x41\x63torTransformMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.pd.data.Transform:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transform_map_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOCKETTRANSFORMMAP_SOCKETMAPENTRY._options = None
  _SOCKETTRANSFORMMAP_SOCKETMAPENTRY._serialized_options = b'8\001'
  _VALUEMAP_VALUEMAPENTRY._options = None
  _VALUEMAP_VALUEMAPENTRY._serialized_options = b'8\001'
  _TRANSFORMMAP_TRANSFORMMAPENTRY._options = None
  _TRANSFORMMAP_TRANSFORMMAPENTRY._serialized_options = b'8\001'
  _TRANSFORMMAP_SOCKETTRANSFORMMAPENTRY._options = None
  _TRANSFORMMAP_SOCKETTRANSFORMMAPENTRY._serialized_options = b'8\001'
  _TRANSFORMMAP_VALUEMAPENTRY._options = None
  _TRANSFORMMAP_VALUEMAPENTRY._serialized_options = b'8\001'
  _TRANSFORMMAP_ACTORTRANSFORMMAPENTRY._options = None
  _TRANSFORMMAP_ACTORTRANSFORMMAPENTRY._serialized_options = b'8\001'
  _SOCKETTRANSFORMMAP._serialized_start=49
  _SOCKETTRANSFORMMAP._serialized_end=203
  _SOCKETTRANSFORMMAP_SOCKETMAPENTRY._serialized_start=135
  _SOCKETTRANSFORMMAP_SOCKETMAPENTRY._serialized_end=203
  _VALUE._serialized_start=206
  _VALUE._serialized_end=361
  _VALUEMAP._serialized_start=363
  _VALUEMAP._serialized_end=490
  _VALUEMAP_VALUEMAPENTRY._serialized_start=427
  _VALUEMAP_VALUEMAPENTRY._serialized_end=490
  _TRANSFORMMAP._serialized_start=493
  _TRANSFORMMAP._serialized_end=1086
  _TRANSFORMMAP_TRANSFORMMAPENTRY._serialized_start=781
  _TRANSFORMMAP_TRANSFORMMAPENTRY._serialized_end=852
  _TRANSFORMMAP_SOCKETTRANSFORMMAPENTRY._serialized_start=854
  _TRANSFORMMAP_SOCKETTRANSFORMMAPENTRY._serialized_end=940
  _TRANSFORMMAP_VALUEMAPENTRY._serialized_start=942
  _TRANSFORMMAP_VALUEMAPENTRY._serialized_end=1008
  _TRANSFORMMAP_ACTORTRANSFORMMAPENTRY._serialized_start=1010
  _TRANSFORMMAP_ACTORTRANSFORMMAPENTRY._serialized_end=1086
# @@protoc_insertion_point(module_scope)
