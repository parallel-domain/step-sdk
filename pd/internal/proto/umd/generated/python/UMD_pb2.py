# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: UMD.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tUMD.proto\x12\x03umd\"2\n\tPoint_LLA\x12\x0b\n\x03lat\x18\x01 \x02(\x01\x12\x0b\n\x03lon\x18\x02 \x02(\x01\x12\x0b\n\x03\x61lt\x18\x03 \x02(\x01\"-\n\nPoint_ECEF\x12\t\n\x01x\x18\x01 \x02(\x01\x12\t\n\x01y\x18\x02 \x02(\x01\x12\t\n\x01z\x18\x03 \x02(\x01\",\n\tPoint_ENU\x12\t\n\x01x\x18\x01 \x02(\x02\x12\t\n\x01y\x18\x02 \x02(\x02\x12\t\n\x01z\x18\x03 \x02(\x02\"8\n\nQuaternion\x12\t\n\x01w\x18\x01 \x02(\x02\x12\t\n\x01x\x18\x02 \x02(\x02\x12\t\n\x01y\x18\x03 \x02(\x02\x12\t\n\x01z\x18\x04 \x02(\x02\"@\n\x04\x41\x41\x42\x42\x12\x1b\n\x03min\x18\x01 \x02(\x0b\x32\x0e.umd.Point_ENU\x12\x1b\n\x03max\x18\x02 \x02(\x0b\x32\x0e.umd.Point_ENU\"S\n\x04\x45\x64ge\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04open\x18\x02 \x02(\x08\x12\x1e\n\x06points\x18\x03 \x03(\x0b\x32\x0e.umd.Point_ENU\x12\x11\n\tuser_data\x18\x04 \x01(\t\"C\n\x04Info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1e\n\x06origin\x18\x02 \x02(\x0b\x32\x0e.umd.Point_LLA\x12\r\n\x05\x61udit\x18\x03 \x01(\t\"\xea\x05\n\x0bLaneSegment\x12\n\n\x02id\x18\x01 \x02(\x04\x12\'\n\x04type\x18\x02 \x02(\x0e\x32\x19.umd.LaneSegment.LaneType\x12-\n\tdirection\x18\x03 \x02(\x0e\x32\x1a.umd.LaneSegment.Direction\x12\x0c\n\x04road\x18\x04 \x02(\x04\x12\x11\n\tleft_edge\x18\x05 \x02(\x04\x12\x12\n\nright_edge\x18\x06 \x02(\x04\x12\x16\n\x0ereference_line\x18\x07 \x02(\x04\x12\x14\n\x0cpredecessors\x18\x08 \x03(\x04\x12\x12\n\nsuccessors\x18\t \x03(\x04\x12\x15\n\rleft_neighbor\x18\n \x01(\x04\x12\x16\n\x0eright_neighbor\x18\x0b \x01(\x04\x12\x15\n\rcompass_angle\x18\x0c \x01(\x01\x12\x12\n\nturn_angle\x18\r \x01(\x01\x12,\n\tturn_type\x18\x0f \x01(\x0e\x32\x19.umd.LaneSegment.TurnType\x12\x11\n\tuser_data\x18\x0e \x01(\t\"\xb8\x01\n\x08LaneType\x12\x12\n\x0eUNDEFINED_LANE\x10\x00\x12\x0c\n\x08\x44RIVABLE\x10\x01\x12\x10\n\x0cNON_DRIVABLE\x10\x02\x12\x0b\n\x07PARKING\x10\x03\x12\x0c\n\x08SHOULDER\x10\x04\x12\n\n\x06\x42IKING\x10\x05\x12\r\n\tCROSSWALK\x10\x06\x12\x0e\n\nRESTRICTED\x10\x07\x12\x11\n\rPARKING_AISLE\x10\x08\x12\x11\n\rPARKING_SPACE\x10\t\x12\x0c\n\x08SIDEWALK\x10\n\"L\n\tDirection\x12\x11\n\rUNDEFINED_DIR\x10\x00\x12\x0b\n\x07\x46ORWARD\x10\x01\x12\x0c\n\x08\x42\x41\x43KWARD\x10\x02\x12\x11\n\rBIDIRECTIONAL\x10\x03\"\\\n\x08TurnType\x12\x0c\n\x08STRAIGHT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02\x12\x0f\n\x0bSLIGHT_LEFT\x10\x03\x12\x10\n\x0cSLIGHT_RIGHT\x10\x04\x12\n\n\x06U_TURN\x10\x05\"\xf4\x04\n\x0bRoadSegment\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x14\n\x0cpredecessors\x18\x03 \x03(\x04\x12\x12\n\nsuccessors\x18\x04 \x03(\x04\x12\x15\n\rlane_segments\x18\x05 \x03(\x04\x12\x16\n\x0ereference_line\x18\x06 \x01(\x04\x12\'\n\x04type\x18\x08 \x01(\x0e\x32\x19.umd.RoadSegment.RoadType\x12\x30\n\x0bground_type\x18\x0b \x01(\x0e\x32\x1b.umd.RoadSegment.GroundType\x12$\n\x0bspeed_limit\x18\n \x01(\x0b\x32\x0f.umd.SpeedLimit\x12\x13\n\x0bjunction_id\x18\t \x01(\x04\x12\x11\n\tuser_data\x18\x07 \x01(\t\"\x96\x02\n\x08RoadType\x12\x0c\n\x08MOTORWAY\x10\x00\x12\t\n\x05TRUNK\x10\x01\x12\x0b\n\x07PRIMARY\x10\x02\x12\r\n\tSECONDARY\x10\x03\x12\x0c\n\x08TERTIARY\x10\x04\x12\x10\n\x0cUNCLASSIFIED\x10\x05\x12\x0f\n\x0bRESIDENTIAL\x10\x06\x12\x11\n\rMOTORWAY_LINK\x10\x07\x12\x0e\n\nTRUNK_LINK\x10\x08\x12\x10\n\x0cPRIMARY_LINK\x10\t\x12\x12\n\x0eSECONDARY_LINK\x10\n\x12\x11\n\rTERTIARY_LINK\x10\x0b\x12\x0b\n\x07SERVICE\x10\x0c\x12\x0c\n\x08\x44RIVEWAY\x10\r\x12\x11\n\rPARKING_AISLE\x10\x0e\x12\x1a\n\x16\x44RIVEWAY_PARKING_ENTRY\x10\x0f\"0\n\nGroundType\x12\n\n\x06GROUND\x10\x00\x12\n\n\x06\x42RIDGE\x10\x01\x12\n\n\x06TUNNEL\x10\x02\"\x81\x01\n\nSpeedLimit\x12\r\n\x05speed\x18\x01 \x02(\r\x12)\n\x05units\x18\x02 \x02(\x0e\x32\x1a.umd.SpeedLimit.SpeedUnits\"9\n\nSpeedUnits\x12\x12\n\x0eMILES_PER_HOUR\x10\x00\x12\x17\n\x13KILOMETERS_PER_HOUR\x10\x01\"\xd3\x05\n\x04\x41rea\x12\n\n\x02id\x18\x01 \x02(\x04\x12 \n\x04type\x18\x02 \x02(\x0e\x32\x12.umd.Area.AreaType\x12\r\n\x05\x65\x64ges\x18\x03 \x03(\x04\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x0e\n\x06\x66loors\x18\x06 \x01(\r\x12\x11\n\tuser_data\x18\x05 \x01(\t\"\xda\x04\n\x08\x41reaType\x12\x17\n\x13\x42UILDING_COMMERCIAL\x10\x00\x12\x18\n\x14\x42UILDING_RESIDENTIAL\x10\x01\x12\x17\n\x13\x42UILDING_INDUSTRIAL\x10\x02\x12\x12\n\x0e\x42UILDING_HOUSE\x10\x03\x12\x16\n\x12\x42UILDING_APARTMENT\x10\x08\x12\x13\n\x0f\x42UILDING_GARAGE\x10\t\x12\x10\n\x0c\x42UILDING_GAS\x10\n\x12\x14\n\x10\x42UILDING_PARKING\x10\x0b\x12\x13\n\x0f\x42UILDING_OFFICE\x10\x0c\x12\x13\n\x0f\x42UILDING_RETAIL\x10\r\x12\x13\n\x0f\x42UILDING_SCHOOL\x10\x0e\x12\x16\n\x12\x42UILDING_WAREHOUSE\x10\x0f\x12\x19\n\x15\x42UILDING_UNCLASSIFIED\x10\x1d\x12\r\n\tEMPTY_LOT\x10\x07\x12\x0f\n\x0bPARKING_LOT\x10\x04\x12\x11\n\rPARKING_SPACE\x10\x05\x12\x08\n\x04PARK\x10\x06\x12\t\n\x05POWER\x10\x12\x12\x08\n\x04RAIL\x10\x13\x12\x0c\n\x08SIDEWALK\x10\x11\x12\x10\n\x0cUNCLASSIFIED\x10\x10\x12\t\n\x05WATER\x10\x14\x12\x0e\n\nZONE_BROWN\x10\x15\x12\x13\n\x0fZONE_COMMERCIAL\x10\x16\x12\x0e\n\nZONE_GREEN\x10\x17\x12\x13\n\x0fZONE_INDUSTRIAL\x10\x18\x12\x14\n\x10ZONE_RESIDENTIAL\x10\x19\x12\x0f\n\x0bZONE_RETAIL\x10\x1a\x12\x0e\n\nZONE_WATER\x10\x1b\x12\r\n\tSPEEDBUMP\x10\x1c\x12\x10\n\x0c\x43ONSTRUCTION\x10\x1e\x12\x08\n\x04YARD\x10\x1f\"\xaa\x02\n\x08ZoneGrid\x12 \n\x08\x62ound_NE\x18\x01 \x02(\x0b\x32\x0e.umd.Point_ENU\x12 \n\x08\x62ound_SW\x18\x02 \x02(\x0b\x32\x0e.umd.Point_ENU\x12\x13\n\x0blat_samples\x18\x03 \x02(\r\x12\x13\n\x0blon_samples\x18\x04 \x02(\r\x12&\n\x06points\x18\x05 \x03(\x0e\x32\x16.umd.ZoneGrid.ZoneType\"\x87\x01\n\x08ZoneType\x12\x0e\n\nCOMMERCIAL\x10\x00\x12\n\n\x06RETAIL\x10\x01\x12\x0e\n\nINDUSTRIAL\x10\x02\x12\x0f\n\x0bRESIDENTIAL\x10\x03\x12\x0b\n\x07PARKING\x10\x04\x12\t\n\x05WATER\x10\x05\x12\t\n\x05GREEN\x10\x06\x12\t\n\x05\x42ROWN\x10\x07\x12\x10\n\x0cUNCLASSIFIED\x10\x08\"\xf7\x13\n\x0fTrafficSignData\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1d.umd.TrafficSignData.SignTypeH\x00\x12\x13\n\tsign_code\x18\x02 \x01(\tH\x00\x12\x14\n\nface_value\x18\x03 \x01(\rH\x00\x12\x13\n\tface_text\x18\x04 \x01(\tH\x00\x12\x14\n\nasset_name\x18\x05 \x01(\tH\x00\"\xd6\x12\n\x08SignType\x12-\n)REGULATORY_STOP_YIELD_PEDESTRIAN_CROSSING\x10\x00\x12\x1f\n\x1bREGULATORY_SPEED_REGULATION\x10\x01\x12 \n\x1cREGULATORY_TURN_AND_LANE_USE\x10\x02\x12\"\n\x1eREGULATORY_MOVEMENT_REGULATION\x10\x03\x12\"\n\x1eREGULATORY_SELECTIVE_EXCLUSION\x10\x04\x12\x31\n-REGULATORY_ONE_WAY_DIVIDED_HIGHWAY_ROUNDABOUT\x10\x05\x12!\n\x1dREGULATORY_PARKING_REGULATION\x10\x06\x12=\n9REGULATORY_PARKING_PROHIBITION_EMERGENCY_RESTRICTION_RAIL\x10\x07\x12,\n(REGULATORY_PEDESTRIAN_BICYCLE_EQUESTRIAN\x10\x08\x12\x1d\n\x19REGULATORY_TRAFFIC_SIGNAL\x10\t\x12\x1b\n\x17REGULATORY_ROAD_CLOSURE\x10\n\x12\x1b\n\x17REGULATORY_WEIGHT_LIMIT\x10\x0b\x12\x1c\n\x18REGULATORY_WEIGH_STATION\x10\x0c\x12\x1a\n\x16REGULATORY_TRUCK_ROUTE\x10\r\x12&\n\"REGULATORY_RAILROAD_AND_LIGHT_RAIL\x10\x0e\x12\x35\n1REGULATORY_SEATBELT_CRASH_CLEARANCE_HEADLIGHT_USE\x10\x0f\x12\x1a\n\x16WARNING_TURN_AND_CURVE\x10\x10\x12\x18\n\x14WARNING_INTERSECTION\x10\x11\x12#\n\x1fWARNING_ADVANCE_TRAFFIC_CONTROL\x10\x12\x12%\n!WARNING_MERGE_AND_LANE_TRANSITION\x10\x13\x12\x1d\n\x19WARNING_WIDTH_RESTRICTION\x10\x14\x12\x1b\n\x17WARNING_DIVIDED_HIGHWAY\x10\x15\x12\x10\n\x0cWARNING_HILL\x10\x16\x12\x1e\n\x1aWARNING_PAVEMENT_CONDITION\x10\x17\x12\x1b\n\x17WARNING_LANE_TRANSITION\x10\x18\x12#\n\x1fWARNING_RAILROAD_AND_LIGHT_RAIL\x10\x19\x12$\n WARNING_ADVANCE_WARNING_CROSSING\x10\x1a\x12\x19\n\x15WARNING_LOW_CLEARANCE\x10\x1b\x12\x1a\n\x16WARNING_ADVISORY_SPEED\x10\x1c\x12)\n%WARNING_DEAD_END_NO_OUTLET_NO_PASSING\x10\x1d\x12\x16\n\x12WARNING_PLAYGROUND\x10\x1e\x12 \n\x1cWARNING_SUPPLEMENTAL_PLAQUES\x10\x1f\x12\x16\n\x12WARNING_SPEED_HUMP\x10 \x12\x1c\n\x18WARNING_NO_TRAFFIC_SIGNS\x10!\x12\x15\n\x11WARNING_WORK_ZONE\x10\"\x12\x15\n\x11WARNING_ROAD_WORK\x10#\x12\x14\n\x10WARNING_BLASTING\x10$\x12\x18\n\x14WARNING_SLOW_TRAFFIC\x10%\x12 \n\x1cWARNING_DOUBLE_REVERSE_CURVE\x10&\x12\x17\n\x13WARNING_YELLOW_TRAP\x10\'\x12\x18\n\x14MARKER_ROUTE_MARKERS\x10(\x12\x19\n\x15MARKER_JUNCTION_SIGNS\x10)\x12+\n\'MARKER_CARDINAL_DIRECTIONAL_AUXILLARIES\x10*\x12\"\n\x1eMARKER_ALTERNATIVE_ROUTE_SIGNS\x10+\x12#\n\x1fMARKER_ADVANCE_TURN_AUXILLARIES\x10,\x12(\n$MARKER_DIRECTIONAL_ARROW_AUXILLARIES\x10-\x12\x30\n,MARKER_DIRECTIONAL_ARROW_AUXILLARIES_BICYCLE\x10.\x12\x15\n\x11GUIDE_DESTINATION\x10/\x12\x12\n\x0eGUIDE_DISTANCE\x10\x30\x12\x15\n\x11GUIDE_STREET_NAME\x10\x31\x12\x11\n\rGUIDE_PARKING\x10\x32\x12\x13\n\x0fGUIDE_REST_AREA\x10\x33\x12\x10\n\x0cGUIDE_SCENIC\x10\x34\x12\x16\n\x12GUIDE_RECREATIONAL\x10\x35\x12\x17\n\x13GUIDE_WEIGH_STATION\x10\x36\x12\x1a\n\x16GUIDE_GENERAL_SERVICES\x10\x37\x12&\n\"GUIDE_REFERENCE_LOCATION_MILEPOSTS\x10\x38\x12\x11\n\rGUIDE_BICYCLE\x10\x39\x12\x1d\n\x19GUIDE_GENERAL_INFORMATION\x10:\x12$\n GUIDE_CROSSOVER_FREEWAY_ENTRANCE\x10;\x12 \n\x1cGUIDE_EXPRESSWAY_AND_FREEWAY\x10<\x12\x1f\n\x1bGUIDE_WORK_ZONE_INFORMATION\x10=\x12,\n(GUIDE_RECREATIONAL_AND_CULTURAL_INTEREST\x10>\x12)\n%CULTURAL_INTEREST_GENERAL_INFORMATION\x10?\x12\'\n#CULTURAL_INTEREST_TRAVELER_SERVICES\x10@\x12,\n(CULTURAL_INTEREST_ACCOMMODATION_SERVICES\x10\x41\x12%\n!CULTURAL_INTEREST_LAND_RECREATION\x10\x42\x12&\n\"CULTURAL_INTEREST_WATER_RECREATION\x10\x43\x12\'\n#CULTURAL_INTEREST_WINTER_RECREATION\x10\x44\x12\x11\n\rOBJECT_MARKER\x10\x45\x12\x16\n\x12\x42ICYCLE_FACILITIES\x10\x46\x12\n\n\x06SCHOOL\x10G\x12&\n\"EMERGENCY_MANAGEMENT_CIVIL_DEFENSE\x10HB\x06\n\x04\x64\x61ta\"n\n\x10TrafficLightData\x12 \n\x18signaled_intersection_id\x18\x01 \x02(\x04\x12$\n\x05\x62ulbs\x18\x02 \x03(\x0b\x32\x15.umd.TrafficLightBulb\x12\x12\n\nasset_name\x18\x03 \x01(\t\"\x80\x03\n\x10TrafficLightBulb\x12*\n\x05shape\x18\x01 \x02(\x0e\x32\x1b.umd.TrafficLightBulb.Shape\x12*\n\x05\x63olor\x18\x02 \x02(\x0e\x32\x1b.umd.TrafficLightBulb.Color\x12\x10\n\x08phase_id\x18\x03 \x02(\x04\x12\x13\n\x0bis_flashing\x18\x04 \x01(\x08\"\xc3\x01\n\x05Shape\x12\n\n\x06\x43IRCLE\x10\x00\x12\x0e\n\nARROW_LEFT\x10\x01\x12\x17\n\x13\x41RROW_LEFT_DIAGONAL\x10\x02\x12\x0f\n\x0b\x41RROW_RIGHT\x10\x03\x12\x18\n\x14\x41RROW_RIGHT_DIAGONAL\x10\x04\x12\x0c\n\x08\x41RROW_UP\x10\x06\x12\x0e\n\nARROW_DOWN\x10\x07\x12\n\n\x06U_TURN\x10\x05\x12\x0b\n\x07\x42ICYCLE\x10\x08\x12\x08\n\x04WALK\x10\t\x12\r\n\tDONT_WALK\x10\n\x12\n\n\x06NUMBER\x10\x0b\"\'\n\x05\x43olor\x12\x07\n\x03RED\x10\x00\x12\n\n\x06YELLOW\x10\x01\x12\t\n\x05GREEN\x10\x02\"\xe7\x01\n\x08PropData\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x16.umd.PropData.PropTypeH\x00\x12\x14\n\nasset_name\x18\x02 \x01(\tH\x00\"\x94\x01\n\x08PropType\x12\x0b\n\x07VEHICLE\x10\x00\x12\x13\n\x0fTERRAIN_NATURAL\x10\x01\x12\x13\n\x0fVEGETATION_HIGH\x10\x02\x12\x12\n\x0eVEGETATION_LOW\x10\x03\x12\x0c\n\x08\x42UILDING\x10\x04\x12\r\n\tHARDSCAPE\x10\x05\x12\x0b\n\x07\x42\x41RRIER\x10\x06\x12\x08\n\x04POLE\x10\x07\x12\t\n\x05OTHER\x10\x08\x42\x06\n\x04\x64\x61ta\"\xd1\x02\n\x06Object\x12\n\n\x02id\x18\x01 \x02(\x04\x12$\n\x0borientation\x18\x03 \x02(\x0b\x32\x0f.umd.Quaternion\x12 \n\x06origin\x18\x02 \x01(\x0b\x32\x0e.umd.Point_ENUH\x00\x12!\n\x0c\x62ounding_box\x18\x04 \x01(\x0b\x32\t.umd.AABBH\x00\x12\x31\n\x11traffic_sign_data\x18\x05 \x01(\x0b\x32\x14.umd.TrafficSignDataH\x01\x12\x33\n\x12traffic_light_data\x18\x06 \x01(\x0b\x32\x15.umd.TrafficLightDataH\x01\x12\"\n\tprop_data\x18\x07 \x01(\x0b\x32\r.umd.PropDataH\x01\x12\x1c\n\x10\x65xclusion_radius\x18\x08 \x01(\x02:\x02-1\x12\x11\n\tuser_data\x18\t \x01(\tB\x0b\n\tplacementB\x06\n\x04\x64\x61ta\"\xbd\x01\n\x08Junction\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x15\n\rlane_segments\x18\x02 \x03(\x04\x12\x15\n\rroad_segments\x18\x03 \x03(\x04\x12\x1d\n\x15signaled_intersection\x18\x06 \x01(\x04\x12\x11\n\tuser_data\x18\x07 \x01(\t\x12\x0f\n\x07\x63orners\x18\x08 \x03(\x04\x12\x17\n\x0f\x63rosswalk_lanes\x18\t \x03(\x04\x12\x1b\n\x13signed_intersection\x18\n \x01(\x04\"\x8c\x03\n\x0bRoadMarking\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0f\n\x07\x65\x64ge_id\x18\x02 \x02(\x04\x12\r\n\x05width\x18\x03 \x02(\x02\x12#\n\x04type\x18\x04 \x01(\x0e\x32\x15.umd.RoadMarking.Type\x12%\n\x05\x63olor\x18\x05 \x01(\x0e\x32\x16.umd.RoadMarking.Color\x12\x13\n\x0b\x64\x61sh_length\x18\x07 \x01(\x02\x12\x17\n\x0f\x64\x61sh_separation\x18\x08 \x01(\x02\x12\x13\n\x0bis_stopline\x18\t \x01(\x08\"\x83\x01\n\x04Type\x12\t\n\x05SOLID\x10\x00\x12\n\n\x06\x44\x41SHED\x10\x01\x12\x0f\n\x0bSOLID_SOLID\x10\x02\x12\x10\n\x0cSOLID_DASHED\x10\x03\x12\x10\n\x0c\x44\x41SHED_SOLID\x10\x04\x12\x11\n\rDASHED_DASHED\x10\x05\x12\x0e\n\nBOTTS_DOTS\x10\x06\x12\x0c\n\x08NO_PAINT\x10\x07\"<\n\x05\x43olor\x12\t\n\x05WHITE\x10\x00\x12\x08\n\x04\x42LUE\x10\x01\x12\t\n\x05GREEN\x10\x02\x12\x07\n\x03RED\x10\x03\x12\n\n\x06YELLOW\x10\x04\"\xc1\x02\n\x0bSignalOnset\x12\r\n\x05onset\x18\x01 \x02(\x01\x12\x32\n\x0csignal_state\x18\x02 \x02(\x0e\x32\x1c.umd.SignalOnset.SignalState\x12\x34\n\rlogical_state\x18\x03 \x01(\x0e\x32\x1d.umd.SignalOnset.LogicalState\"-\n\x0bSignalState\x12\x07\n\x03red\x10\x00\x12\n\n\x06yellow\x10\x01\x12\t\n\x05green\x10\x02\"\x89\x01\n\x0cLogicalState\x12\x0c\n\x08inactive\x10\x00\x12\r\n\tred_solid\x10\x01\x12\x10\n\x0cred_flashing\x10\x02\x12\x10\n\x0cyellow_solid\x10\x03\x12\x13\n\x0fyellow_flashing\x10\x04\x12\x0f\n\x0bgreen_solid\x10\x05\x12\x12\n\x0egreen_flashing\x10\x06\"U\n\x05Phase\x12\n\n\x02id\x18\x01 \x02(\x04\x12&\n\x0cphase_timing\x18\x02 \x03(\x0b\x32\x10.umd.SignalOnset\x12\x18\n\x10\x63ontrolled_lanes\x18\x03 \x03(\x04\"k\n\x14SignaledIntersection\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x10\n\x08junction\x18\x02 \x02(\x04\x12!\n\rphase_timings\x18\x03 \x03(\x0b\x32\n.umd.Phase\x12\x12\n\ncycle_time\x18\x04 \x02(\x01\"k\n\x12SignedIntersection\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x10\n\x08junction\x18\x02 \x02(\x04\x12\x1a\n\x12stop_sign_lane_ids\x18\x03 \x03(\x04\x12\x1b\n\x13yield_sign_lane_ids\x18\x04 \x03(\x04\"\xc8\t\n\x0cUniversalMap\x12\x17\n\x04info\x18\x01 \x02(\x0b\x32\t.umd.Info\x12:\n\rroad_segments\x18\x02 \x03(\x0b\x32#.umd.UniversalMap.RoadSegmentsEntry\x12:\n\rlane_segments\x18\x03 \x03(\x0b\x32#.umd.UniversalMap.LaneSegmentsEntry\x12+\n\x05\x61reas\x18\x04 \x03(\x0b\x32\x1c.umd.UniversalMap.AreasEntry\x12/\n\x07objects\x18\x05 \x03(\x0b\x32\x1e.umd.UniversalMap.ObjectsEntry\x12+\n\x05\x65\x64ges\x18\x06 \x03(\x0b\x32\x1c.umd.UniversalMap.EdgesEntry\x12\x33\n\tjunctions\x18\x07 \x03(\x0b\x32 .umd.UniversalMap.JunctionsEntry\x12:\n\rroad_markings\x18\t \x03(\x0b\x32#.umd.UniversalMap.RoadMarkingsEntry\x12L\n\x16signaled_intersections\x18\n \x03(\x0b\x32,.umd.UniversalMap.SignaledIntersectionsEntry\x12H\n\x14signed_intersections\x18\x0c \x03(\x0b\x32*.umd.UniversalMap.SignedIntersectionsEntry\x12 \n\tzone_grid\x18\x0b \x01(\x0b\x32\r.umd.ZoneGrid\x1a\x45\n\x11RoadSegmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.umd.RoadSegment:\x02\x38\x01\x1a\x45\n\x11LaneSegmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.umd.LaneSegment:\x02\x38\x01\x1a\x37\n\nAreasEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.umd.Area:\x02\x38\x01\x1a;\n\x0cObjectsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.umd.Object:\x02\x38\x01\x1a\x37\n\nEdgesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.umd.Edge:\x02\x38\x01\x1a?\n\x0eJunctionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1c\n\x05value\x18\x02 \x01(\x0b\x32\r.umd.Junction:\x02\x38\x01\x1a\x45\n\x11RoadMarkingsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.umd.RoadMarking:\x02\x38\x01\x1aW\n\x1aSignaledIntersectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x19.umd.SignaledIntersection:\x02\x38\x01\x1aS\n\x18SignedIntersectionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.umd.SignedIntersection:\x02\x38\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UMD_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _UNIVERSALMAP_ROADSEGMENTSENTRY._options = None
  _UNIVERSALMAP_ROADSEGMENTSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_LANESEGMENTSENTRY._options = None
  _UNIVERSALMAP_LANESEGMENTSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_AREASENTRY._options = None
  _UNIVERSALMAP_AREASENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_OBJECTSENTRY._options = None
  _UNIVERSALMAP_OBJECTSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_EDGESENTRY._options = None
  _UNIVERSALMAP_EDGESENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_JUNCTIONSENTRY._options = None
  _UNIVERSALMAP_JUNCTIONSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_ROADMARKINGSENTRY._options = None
  _UNIVERSALMAP_ROADMARKINGSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_SIGNALEDINTERSECTIONSENTRY._options = None
  _UNIVERSALMAP_SIGNALEDINTERSECTIONSENTRY._serialized_options = b'8\001'
  _UNIVERSALMAP_SIGNEDINTERSECTIONSENTRY._options = None
  _UNIVERSALMAP_SIGNEDINTERSECTIONSENTRY._serialized_options = b'8\001'
  _POINT_LLA._serialized_start=18
  _POINT_LLA._serialized_end=68
  _POINT_ECEF._serialized_start=70
  _POINT_ECEF._serialized_end=115
  _POINT_ENU._serialized_start=117
  _POINT_ENU._serialized_end=161
  _QUATERNION._serialized_start=163
  _QUATERNION._serialized_end=219
  _AABB._serialized_start=221
  _AABB._serialized_end=285
  _EDGE._serialized_start=287
  _EDGE._serialized_end=370
  _INFO._serialized_start=372
  _INFO._serialized_end=439
  _LANESEGMENT._serialized_start=442
  _LANESEGMENT._serialized_end=1188
  _LANESEGMENT_LANETYPE._serialized_start=832
  _LANESEGMENT_LANETYPE._serialized_end=1016
  _LANESEGMENT_DIRECTION._serialized_start=1018
  _LANESEGMENT_DIRECTION._serialized_end=1094
  _LANESEGMENT_TURNTYPE._serialized_start=1096
  _LANESEGMENT_TURNTYPE._serialized_end=1188
  _ROADSEGMENT._serialized_start=1191
  _ROADSEGMENT._serialized_end=1819
  _ROADSEGMENT_ROADTYPE._serialized_start=1491
  _ROADSEGMENT_ROADTYPE._serialized_end=1769
  _ROADSEGMENT_GROUNDTYPE._serialized_start=1771
  _ROADSEGMENT_GROUNDTYPE._serialized_end=1819
  _SPEEDLIMIT._serialized_start=1822
  _SPEEDLIMIT._serialized_end=1951
  _SPEEDLIMIT_SPEEDUNITS._serialized_start=1894
  _SPEEDLIMIT_SPEEDUNITS._serialized_end=1951
  _AREA._serialized_start=1954
  _AREA._serialized_end=2677
  _AREA_AREATYPE._serialized_start=2075
  _AREA_AREATYPE._serialized_end=2677
  _ZONEGRID._serialized_start=2680
  _ZONEGRID._serialized_end=2978
  _ZONEGRID_ZONETYPE._serialized_start=2843
  _ZONEGRID_ZONETYPE._serialized_end=2978
  _TRAFFICSIGNDATA._serialized_start=2981
  _TRAFFICSIGNDATA._serialized_end=5532
  _TRAFFICSIGNDATA_SIGNTYPE._serialized_start=3134
  _TRAFFICSIGNDATA_SIGNTYPE._serialized_end=5524
  _TRAFFICLIGHTDATA._serialized_start=5534
  _TRAFFICLIGHTDATA._serialized_end=5644
  _TRAFFICLIGHTBULB._serialized_start=5647
  _TRAFFICLIGHTBULB._serialized_end=6031
  _TRAFFICLIGHTBULB_SHAPE._serialized_start=5795
  _TRAFFICLIGHTBULB_SHAPE._serialized_end=5990
  _TRAFFICLIGHTBULB_COLOR._serialized_start=5992
  _TRAFFICLIGHTBULB_COLOR._serialized_end=6031
  _PROPDATA._serialized_start=6034
  _PROPDATA._serialized_end=6265
  _PROPDATA_PROPTYPE._serialized_start=6109
  _PROPDATA_PROPTYPE._serialized_end=6257
  _OBJECT._serialized_start=6268
  _OBJECT._serialized_end=6605
  _JUNCTION._serialized_start=6608
  _JUNCTION._serialized_end=6797
  _ROADMARKING._serialized_start=6800
  _ROADMARKING._serialized_end=7196
  _ROADMARKING_TYPE._serialized_start=7003
  _ROADMARKING_TYPE._serialized_end=7134
  _ROADMARKING_COLOR._serialized_start=7136
  _ROADMARKING_COLOR._serialized_end=7196
  _SIGNALONSET._serialized_start=7199
  _SIGNALONSET._serialized_end=7520
  _SIGNALONSET_SIGNALSTATE._serialized_start=7335
  _SIGNALONSET_SIGNALSTATE._serialized_end=7380
  _SIGNALONSET_LOGICALSTATE._serialized_start=7383
  _SIGNALONSET_LOGICALSTATE._serialized_end=7520
  _PHASE._serialized_start=7522
  _PHASE._serialized_end=7607
  _SIGNALEDINTERSECTION._serialized_start=7609
  _SIGNALEDINTERSECTION._serialized_end=7716
  _SIGNEDINTERSECTION._serialized_start=7718
  _SIGNEDINTERSECTION._serialized_end=7825
  _UNIVERSALMAP._serialized_start=7828
  _UNIVERSALMAP._serialized_end=9052
  _UNIVERSALMAP_ROADSEGMENTSENTRY._serialized_start=8427
  _UNIVERSALMAP_ROADSEGMENTSENTRY._serialized_end=8496
  _UNIVERSALMAP_LANESEGMENTSENTRY._serialized_start=8498
  _UNIVERSALMAP_LANESEGMENTSENTRY._serialized_end=8567
  _UNIVERSALMAP_AREASENTRY._serialized_start=8569
  _UNIVERSALMAP_AREASENTRY._serialized_end=8624
  _UNIVERSALMAP_OBJECTSENTRY._serialized_start=8626
  _UNIVERSALMAP_OBJECTSENTRY._serialized_end=8685
  _UNIVERSALMAP_EDGESENTRY._serialized_start=8687
  _UNIVERSALMAP_EDGESENTRY._serialized_end=8742
  _UNIVERSALMAP_JUNCTIONSENTRY._serialized_start=8744
  _UNIVERSALMAP_JUNCTIONSENTRY._serialized_end=8807
  _UNIVERSALMAP_ROADMARKINGSENTRY._serialized_start=8809
  _UNIVERSALMAP_ROADMARKINGSENTRY._serialized_end=8878
  _UNIVERSALMAP_SIGNALEDINTERSECTIONSENTRY._serialized_start=8880
  _UNIVERSALMAP_SIGNALEDINTERSECTIONSENTRY._serialized_end=8967
  _UNIVERSALMAP_SIGNEDINTERSECTIONSENTRY._serialized_start=8969
  _UNIVERSALMAP_SIGNEDINTERSECTIONSENTRY._serialized_end=9052
# @@protoc_insertion_point(module_scope)
