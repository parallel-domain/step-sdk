# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: annotation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import geometry_pb2 as geometry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61nnotation.proto\x12\x07pd.data\x1a\x19google/protobuf/any.proto\x1a\x0egeometry.proto\"\x83\x04\n\x12GeometryAnnotation\x12$\n\x08point_2d\x18\x01 \x01(\x0b\x32\x10.pd.data.Vector2H\x00\x12\"\n\x07line_2d\x18\x02 \x01(\x0b\x32\x0f.pd.data.Line2DH\x00\x12+\n\x0cpoly_line_2d\x18\x03 \x01(\x0b\x32\x13.pd.data.PolyLine2DH\x00\x12(\n\npolygon_2d\x18\x04 \x01(\x0b\x32\x12.pd.data.Polygon2DH\x00\x12 \n\x06\x62ox_2d\x18\x05 \x01(\x0b\x32\x0e.pd.data.Box2DH\x00\x12$\n\x08point_3d\x18\x06 \x01(\x0b\x32\x10.pd.data.Vector3H\x00\x12\"\n\x07line_3d\x18\x07 \x01(\x0b\x32\x0f.pd.data.Line3DH\x00\x12+\n\x0cpoly_line_3d\x18\x08 \x01(\x0b\x32\x13.pd.data.PolyLine3DH\x00\x12(\n\npolygon_3d\x18\t \x01(\x0b\x32\x12.pd.data.Polygon3DH\x00\x12&\n\tcuboid_3d\x18\n \x01(\x0b\x32\x11.pd.data.Cuboid3DH\x00\x12\'\n\ttransform\x18\x0b \x01(\x0b\x32\x12.pd.data.TransformH\x00\x12&\n\x08metadata\x18\r \x01(\x0b\x32\x14.google.protobuf.AnyB\x10\n\x0egeometry_oneof\"E\n\x12GeometryCollection\x12/\n\nprimitives\x18\x01 \x03(\x0b\x32\x1b.pd.data.GeometryAnnotation\";\n\nAnnotation\x12-\n\x08geometry\x18\x01 \x01(\x0b\x32\x1b.pd.data.GeometryCollectionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'annotation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GEOMETRYANNOTATION._serialized_start=73
  _GEOMETRYANNOTATION._serialized_end=588
  _GEOMETRYCOLLECTION._serialized_start=590
  _GEOMETRYCOLLECTION._serialized_end=659
  _ANNOTATION._serialized_start=661
  _ANNOTATION._serialized_end=720
# @@protoc_insertion_point(module_scope)
