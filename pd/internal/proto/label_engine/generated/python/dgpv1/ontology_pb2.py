# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dgpv1/ontology.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64gpv1/ontology.proto\x12\x0c\x64gp.proto.v2\"\xab\x01\n\x0cOntologyItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12/\n\x05\x63olor\x18\x03 \x01(\x0b\x32 .dgp.proto.v2.OntologyItem.Color\x12\x0f\n\x07isthing\x18\x04 \x01(\x08\x12\x15\n\rsupercategory\x18\x05 \x01(\t\x1a(\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\r\x12\t\n\x01g\x18\x02 \x01(\r\x12\t\n\x01\x62\x18\x03 \x01(\r\"5\n\x08Ontology\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.dgp.proto.v2.OntologyItem\"K\n\x13\x46\x65\x61tureOntologyItem\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\r\x12\x1a\n\x12\x66\x65\x61ture_value_type\x18\x03 \x01(\r\"C\n\x0f\x46\x65\x61tureOntology\x12\x30\n\x05items\x18\x01 \x03(\x0b\x32!.dgp.proto.v2.FeatureOntologyItemb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dgpv1.ontology_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ONTOLOGYITEM._serialized_start=39
  _ONTOLOGYITEM._serialized_end=210
  _ONTOLOGYITEM_COLOR._serialized_start=170
  _ONTOLOGYITEM_COLOR._serialized_end=210
  _ONTOLOGY._serialized_start=212
  _ONTOLOGY._serialized_end=265
  _FEATUREONTOLOGYITEM._serialized_start=267
  _FEATUREONTOLOGYITEM._serialized_end=342
  _FEATUREONTOLOGY._serialized_start=344
  _FEATUREONTOLOGY._serialized_end=411
# @@protoc_insertion_point(module_scope)