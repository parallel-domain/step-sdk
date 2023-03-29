# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: instance_map.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import mesh_map_pb2 as mesh__map__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12instance_map.proto\x12\x07pd.data\x1a\roptions.proto\x1a\x0emesh_map.proto\"1\n\x08Instance\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\x12\x10\n\x08mesh_ids\x18\x02 \x03(\r\"\x85\x02\n\x0bInstanceMap\x12\x36\n\tinstances\x18\x01 \x03(\x0b\x32#.pd.data.InstanceMap.InstancesEntry\x12\x42\n\x10mesh_to_instance\x18\x02 \x03(\x0b\x32(.pd.data.InstanceMap.MeshToInstanceEntry\x1a\x43\n\x0eInstancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.pd.data.Instance:\x02\x38\x01\x1a\x35\n\x13MeshToInstanceEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"?\n\rMergeChildren\x12\x16\n\x0esemantic_label\x18\x01 \x01(\t\x12\x16\n\x0e\x65xclude_labels\x18\x02 \x03(\t\"\x81\x01\n\rInstanceMerge\x12\x33\n\x0bmesh_merges\x18\x01 \x03(\x0b\x32\x1e.pd.data.MeshSemanticMergeInfo\x12;\n\x13relationship_merges\x18\x02 \x03(\x0b\x32\x1e.pd.data.RelationshipMergeInfo\"9\n\x17InstancedSemanticFilter\x12\x1e\n\x16instanced_semantic_ids\x18\x01 \x03(\r\"\x8b\x01\n\x19GenerateInstanceMapConfig\x12)\n\x1bmerge_instance_map_filepath\x18\x01 \x01(\tB\x04\x80\xb5\x18\r\x12$\n\x12input_semantic_map\x18\x02 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x03 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x01\"\xaa\x01\n\x17\x46ilterInstanceMapConfig\x12$\n\x12input_instance_map\x18\x01 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12$\n\x16semantic_filter_config\x18\x02 \x01(\tB\x04\x80\xb5\x18\r\x12$\n\x12input_semantic_map\x18\x03 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x04 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x01\"a\n\x1aGenerateInstanceMaskConfig\x12$\n\x12input_instance_map\x18\x01 \x01(\tB\x08\x80\xb5\x18\x07\x88\xb5\x18\x00\x12\x1d\n\x0boutput_path\x18\x02 \x01(\tB\x08\x80\xb5\x18\x01\x88\xb5\x18\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'instance_map_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INSTANCEMAP_INSTANCESENTRY._options = None
  _INSTANCEMAP_INSTANCESENTRY._serialized_options = b'8\001'
  _INSTANCEMAP_MESHTOINSTANCEENTRY._options = None
  _INSTANCEMAP_MESHTOINSTANCEENTRY._serialized_options = b'8\001'
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['merge_instance_map_filepath']._options = None
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['merge_instance_map_filepath']._serialized_options = b'\200\265\030\r'
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['input_semantic_map']._options = None
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['input_semantic_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['output_path']._options = None
  _GENERATEINSTANCEMAPCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\007\210\265\030\001'
  _FILTERINSTANCEMAPCONFIG.fields_by_name['input_instance_map']._options = None
  _FILTERINSTANCEMAPCONFIG.fields_by_name['input_instance_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _FILTERINSTANCEMAPCONFIG.fields_by_name['semantic_filter_config']._options = None
  _FILTERINSTANCEMAPCONFIG.fields_by_name['semantic_filter_config']._serialized_options = b'\200\265\030\r'
  _FILTERINSTANCEMAPCONFIG.fields_by_name['input_semantic_map']._options = None
  _FILTERINSTANCEMAPCONFIG.fields_by_name['input_semantic_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _FILTERINSTANCEMAPCONFIG.fields_by_name['output_path']._options = None
  _FILTERINSTANCEMAPCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\007\210\265\030\001'
  _GENERATEINSTANCEMASKCONFIG.fields_by_name['input_instance_map']._options = None
  _GENERATEINSTANCEMASKCONFIG.fields_by_name['input_instance_map']._serialized_options = b'\200\265\030\007\210\265\030\000'
  _GENERATEINSTANCEMASKCONFIG.fields_by_name['output_path']._options = None
  _GENERATEINSTANCEMASKCONFIG.fields_by_name['output_path']._serialized_options = b'\200\265\030\001\210\265\030\001'
  _INSTANCE._serialized_start=62
  _INSTANCE._serialized_end=111
  _INSTANCEMAP._serialized_start=114
  _INSTANCEMAP._serialized_end=375
  _INSTANCEMAP_INSTANCESENTRY._serialized_start=253
  _INSTANCEMAP_INSTANCESENTRY._serialized_end=320
  _INSTANCEMAP_MESHTOINSTANCEENTRY._serialized_start=322
  _INSTANCEMAP_MESHTOINSTANCEENTRY._serialized_end=375
  _MERGECHILDREN._serialized_start=377
  _MERGECHILDREN._serialized_end=440
  _INSTANCEMERGE._serialized_start=443
  _INSTANCEMERGE._serialized_end=572
  _INSTANCEDSEMANTICFILTER._serialized_start=574
  _INSTANCEDSEMANTICFILTER._serialized_end=631
  _GENERATEINSTANCEMAPCONFIG._serialized_start=634
  _GENERATEINSTANCEMAPCONFIG._serialized_end=773
  _FILTERINSTANCEMAPCONFIG._serialized_start=776
  _FILTERINSTANCEMAPCONFIG._serialized_end=946
  _GENERATEINSTANCEMASKCONFIG._serialized_start=948
  _GENERATEINSTANCEMASKCONFIG._serialized_end=1045
# @@protoc_insertion_point(module_scope)