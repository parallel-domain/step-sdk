# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import annotation_pb2 as annotation__pb2
from . import bounding_box_2d_pb2 as bounding__box__2d__pb2
from . import bounding_box_3d_pb2 as bounding__box__3d__pb2
from . import camera_calibration_pb2 as camera__calibration__pb2
from . import ig_metadata_pb2 as ig__metadata__pb2
from . import motion_vectors_2d_pb2 as motion__vectors__2d__pb2
from . import dgp_pb2 as dgp__pb2
from . import geometry_pb2 as geometry__pb2
from . import instance_map_pb2 as instance__map__pb2
from . import mesh_map_pb2 as mesh__map__pb2
from . import transform_map_pb2 as transform__map__pb2
from . import options_pb2 as options__pb2
from . import python_engine_pb2 as python__engine__pb2
from . import telemetry_pb2 as telemetry__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\x12\x07pd.data\x1a\x19google/protobuf/any.proto\x1a\x10\x61nnotation.proto\x1a\x15\x62ounding_box_2d.proto\x1a\x15\x62ounding_box_3d.proto\x1a\x18\x63\x61mera_calibration.proto\x1a\x11ig_metadata.proto\x1a\x17motion_vectors_2d.proto\x1a\tdgp.proto\x1a\x0egeometry.proto\x1a\x12instance_map.proto\x1a\x0emesh_map.proto\x1a\x13transform_map.proto\x1a\roptions.proto\x1a\x13python_engine.proto\x1a\x0ftelemetry.proto\"v\n\x15TransformPipelineNode\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\ndepends_on\x18\x02 \x03(\t\x12$\n\x06\x63onfig\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x15\n\rfinalize_node\x18\x04 \x01(\x08\"B\n\x11TransformPipeline\x12-\n\x05nodes\x18\x01 \x03(\x0b\x32\x1e.pd.data.TransformPipelineNode\"1\n\x0e\x44\x61taTypeRecord\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.pd.data.DataTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'data_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TRANSFORMPIPELINENODE._serialized_start=321
  _TRANSFORMPIPELINENODE._serialized_end=439
  _TRANSFORMPIPELINE._serialized_start=441
  _TRANSFORMPIPELINE._serialized_end=507
  _DATATYPERECORD._serialized_start=509
  _DATATYPERECORD._serialized_end=558
# @@protoc_insertion_point(module_scope)
