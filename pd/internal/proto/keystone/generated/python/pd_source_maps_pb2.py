# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pd_source_maps.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pd_source_maps.proto\x12\x08keystone\"\xc3\x03\n\nSourceMaps\x12\x14\n\x0c\x61rtifact_key\x18\x01 \x01(\t\x12\x1b\n\x13output_artifact_uid\x18\x02 \x01(\t\x12\x32\n\nmap_sector\x18\x03 \x01(\x0b\x32\x1e.keystone.SourceMaps.MapSector\x12\x1f\n\x17\x63ode_build_artifact_uid\x18\x04 \x01(\t\x12\x12\n\nosm_branch\x18\x05 \x01(\t\x12\x1a\n\x12osm_feature_search\x18\x06 \x01(\t\x12\x12\n\nzoom_level\x18\x07 \x01(\x05\x12\x12\n\ntotal_maps\x18\x08 \x01(\x05\x12\x15\n\rparent_region\x18\t \x01(\t\x12*\n\"avoid_overlap_production_locations\x18\n \x01(\x08\x12\"\n\x1arestrict_to_elevation_data\x18\x0b \x01(\x08\x12\x1c\n\x14source_location_seed\x18\x0c \x01(\x05\x12\x13\n\x0bosmcell_uid\x18\r \x01(\t\x1a;\n\tMapSector\x12\x16\n\x0emap_sector_key\x18\x01 \x01(\t\x12\x16\n\x0emap_sector_uid\x18\x02 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pd_source_maps_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SOURCEMAPS._serialized_start=35
  _SOURCEMAPS._serialized_end=486
  _SOURCEMAPS_MAPSECTOR._serialized_start=427
  _SOURCEMAPS_MAPSECTOR._serialized_end=486
# @@protoc_insertion_point(module_scope)
