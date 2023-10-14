# This file is auto-generated. Do not modify.
from pd.internal.assets.asset_registry_database import AssetRegistryDatabase
database = AssetRegistryDatabase(None)

from peewee import *



class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class UtilCharacterGenders(BaseModel):
    gender = TextField(null=True, unique=True)
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'UTIL_character_genders'

class UtilInstanceMethods(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_instance_methods'

class UtilAssetClasses(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_asset_classes'

class UtilAssetCategories(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_asset_categories'

class ObjAssets(BaseModel):
    asset_category = ForeignKeyField(column_name='asset_category_id', field='id', model=UtilAssetCategories, null=True)
    asset_class = ForeignKeyField(column_name='asset_class_id', field='id', model=UtilAssetClasses, null=True)
    asset_id = IntegerField()
    bbox_max_leaves_x = FloatField(null=True)
    bbox_max_leaves_y = FloatField(null=True)
    bbox_max_leaves_z = FloatField(null=True)
    bbox_max_x = FloatField(null=True)
    bbox_max_y = FloatField(null=True)
    bbox_max_z = FloatField(null=True)
    bbox_min_leaves_x = FloatField(null=True)
    bbox_min_leaves_y = FloatField(null=True)
    bbox_min_leaves_z = FloatField(null=True)
    bbox_min_x = FloatField(null=True)
    bbox_min_y = FloatField(null=True)
    bbox_min_z = FloatField(null=True)
    created = DateTimeField()
    height = FloatField(null=True)
    id = CharField(primary_key=True)
    instance_method = ForeignKeyField(column_name='instance_method_id', field='id', model=UtilInstanceMethods, null=True)
    is_obstacle = IntegerField(null=True)
    length = FloatField(null=True)
    name = TextField(null=True, unique=True)
    no_point_cache = IntegerField(null=True)
    updated = DateTimeField()
    width = FloatField(null=True)

    class Meta:
        table_name = 'OBJ_assets'

class UtilAnimalTypes(BaseModel):
    animal_type = TextField(null=True, unique=True)
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'UTIL_animal_types'

class DataCharacter(BaseModel):
    animal = ForeignKeyField(column_name='animal_id', field='id', model=UtilAnimalTypes, null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    child = IntegerField(null=True)
    construction_worker = IntegerField(null=True)
    gender = ForeignKeyField(column_name='gender_id', field='id', model=UtilCharacterGenders, null=True)
    id = CharField(primary_key=True)
    medical_worker = IntegerField(null=True)
    name = TextField(null=True)
    pk_id = IntegerField(null=True)
    police_officer = IntegerField(null=True)

    class Meta:
        table_name = 'DATA_character'

class UtilCharacterAccessoryAttachMethods(BaseModel):
    description = TextField(null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_character_accessory_attach_methods'

class UtilCharacterAccessoryClasses(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_character_accessory_classes'

class DataCharacterAccessories(BaseModel):
    accessory_class = ForeignKeyField(column_name='accessory_class_id', field='id', model=UtilCharacterAccessoryClasses, null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    attach_method = ForeignKeyField(column_name='attach_method_id', field='id', model=UtilCharacterAccessoryAttachMethods, null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)
    unique = IntegerField(null=True)

    class Meta:
        table_name = 'DATA_character_accessories'

class UtilTimeOfDayCategories(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)
    pk_id = IntegerField(null=True)

    class Meta:
        table_name = 'UTIL_time_of_day_categories'

class DataLightingSublevels(BaseModel):
    cloud_coverage = FloatField(null=True)
    fog_intensity_max = FloatField(null=True)
    fog_intensity_min = FloatField(null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)
    path = TextField(null=True)
    pk_id = IntegerField(null=True)
    rain_intensity_max = FloatField(null=True)
    rain_intensity_min = FloatField(null=True)
    source_note = TextField(null=True)
    street_lights = IntegerField(null=True)
    sun_azimuth = FloatField(null=True)
    sun_color_temperature = FloatField(null=True)
    sun_height = FloatField(null=True)
    sun_intensity = FloatField(null=True)
    time_of_day = IntegerField(null=True)
    time_of_day_category = ForeignKeyField(column_name='time_of_day_category_id', field='id', model=UtilTimeOfDayCategories, null=True)
    wetness_max = FloatField(null=True)
    wetness_min = FloatField(null=True)

    class Meta:
        table_name = 'DATA_lighting_sublevels'

class UtilRoadMarkingTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_road_marking_types'

class DataRoadMarkings(BaseModel):
    angle_01 = FloatField(null=True)
    angle_02 = FloatField(null=True)
    angle_03 = FloatField(null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    marking_type = ForeignKeyField(column_name='marking_type_id', field='id', model=UtilRoadMarkingTypes, null=True)
    purpose = TextField(null=True)
    text = TextField(null=True)

    class Meta:
        table_name = 'DATA_road_markings'

class ObjCountries(BaseModel):
    code = TextField(null=True)
    country_id = IntegerField(null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)

    class Meta:
        table_name = 'OBJ_countries'

class UtilSignTypes(BaseModel):
    id = CharField(primary_key=True)
    sign_type = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_sign_types'

class UtilSignShapes(BaseModel):
    id = CharField(primary_key=True)
    sign_shape = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_sign_shapes'

class UtilSignColors(BaseModel):
    id = CharField(primary_key=True)
    sign_color = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_sign_colors'

class DataSign(BaseModel):
    angle_01 = FloatField(null=True)
    angle_02 = FloatField(null=True)
    angle_03 = FloatField(null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    code = TextField(null=True)
    country = ForeignKeyField(column_name='country_id', field='id', model=ObjCountries, null=True)
    id = CharField(primary_key=True)
    implicitness = CharField(null=True)
    segment = CharField(null=True)
    sign_color = ForeignKeyField(column_name='sign_color_id', field='id', model=UtilSignColors, null=True)
    sign_height = FloatField(null=True)
    sign_shape = ForeignKeyField(column_name='sign_shape_id', field='id', model=UtilSignShapes, null=True)
    sign_type = ForeignKeyField(column_name='sign_type_id', field='id', model=UtilSignTypes, null=True)
    speed_limit = IntegerField(null=True)
    swappable = IntegerField(null=True)
    text = TextField(null=True)

    class Meta:
        table_name = 'DATA_sign'

class UtilSocketTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField()

    class Meta:
        table_name = 'UTIL_socket_types'

class DataSockets(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    m1 = FloatField(null=True)
    m10 = FloatField(null=True)
    m11 = FloatField(null=True)
    m12 = FloatField(null=True)
    m13 = FloatField(null=True)
    m14 = FloatField(null=True)
    m15 = FloatField(null=True)
    m16 = FloatField(null=True)
    m2 = FloatField(null=True)
    m3 = FloatField(null=True)
    m4 = FloatField(null=True)
    m5 = FloatField(null=True)
    m6 = FloatField(null=True)
    m7 = FloatField(null=True)
    m8 = FloatField(null=True)
    m9 = FloatField(null=True)
    socket_name = TextField(null=True)
    socket_type = ForeignKeyField(column_name='socket_type_id', field='id', model=UtilSocketTypes, null=True)

    class Meta:
        table_name = 'DATA_sockets'

class UtilTrafficSignalAxisAlignments(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_traffic_signal_axis_alignments'

class UtilTrafficSignalOrientations(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_traffic_signal_orientations'

class UtilTrafficSignalMountTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_traffic_signal_mount_types'

class UtilTrafficSignalMountOrientations(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_traffic_signal_mount_orientations'

class DataTrafficSignal(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    axis0_alignment = ForeignKeyField(column_name='axis0_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis0_diameter = FloatField(null=True)
    axis1_alignment = ForeignKeyField(backref='UTIL_traffic_signal_axis_alignments_axis1_alignment_set', column_name='axis1_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis1_diameter = FloatField(null=True)
    axis2_alignment = ForeignKeyField(backref='UTIL_traffic_signal_axis_alignments_axis2_alignment_set', column_name='axis2_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis2_diameter = FloatField(null=True)
    axis3_alignment = ForeignKeyField(backref='UTIL_traffic_signal_axis_alignments_axis3_alignment_set', column_name='axis3_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis3_diameter = FloatField(null=True)
    axis4_alignment = ForeignKeyField(backref='UTIL_traffic_signal_axis_alignments_axis4_alignment_set', column_name='axis4_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis4_diameter = FloatField(null=True)
    axis5_alignment = ForeignKeyField(backref='UTIL_traffic_signal_axis_alignments_axis5_alignment_set', column_name='axis5_alignment_id', field='id', model=UtilTrafficSignalAxisAlignments, null=True)
    axis5_diameter = FloatField(null=True)
    backplate = IntegerField(null=True)
    backplate_tape = IntegerField(null=True)
    bulb00 = IntegerField(null=True)
    bulb01 = IntegerField(null=True)
    bulb10 = IntegerField(null=True)
    bulb11 = IntegerField(null=True)
    bulb20 = IntegerField(null=True)
    bulb21 = IntegerField(null=True)
    bulb30 = IntegerField(null=True)
    bulb31 = IntegerField(null=True)
    bulb40 = IntegerField(null=True)
    bulb41 = IntegerField(null=True)
    bulb50 = IntegerField(null=True)
    bulb51 = IntegerField(null=True)
    id = CharField(primary_key=True)
    mount_alignment = ForeignKeyField(column_name='mount_alignment_id', field='id', model=UtilTrafficSignalMountOrientations, null=True)
    mount_orientation = ForeignKeyField(backref='UTIL_traffic_signal_mount_orientations_mount_orientation_set', column_name='mount_orientation_id', field='id', model=UtilTrafficSignalMountOrientations, null=True)
    mount_type = ForeignKeyField(column_name='mount_type_id', field='id', model=UtilTrafficSignalMountTypes, null=True)
    orientation = ForeignKeyField(column_name='orientation_id', field='id', model=UtilTrafficSignalOrientations, null=True)
    pedestrian = IntegerField(null=True)

    class Meta:
        table_name = 'DATA_traffic_signal'

class UtilVegetationTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vegetation_types'

class DataVegetation(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    enable_sidewalk = IntegerField(null=True)
    id = CharField(primary_key=True)
    vegetation_type = ForeignKeyField(column_name='vegetation_type_id', field='id', model=UtilVegetationTypes, null=True)

    class Meta:
        table_name = 'DATA_vegetation'

class UtilVehicleTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vehicle_types'

class UtilVehiclePhysicsGroups(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vehicle_physics_groups'

class DataVehicle(BaseModel):
    accessory_roof_chance = FloatField(null=True)
    accessory_trunk_chance = FloatField(null=True)
    anti_roll_stiffness = TextField(null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    center_of_mass = TextField()
    clearance = FloatField(null=True)
    default_wheel_radius = FloatField(null=True)
    dirt_level_max_default = FloatField(null=True)
    dirt_level_min_default = FloatField(null=True)
    distributable = IntegerField(null=True)
    engine_max_rotation_speed = FloatField(null=True)
    engine_max_torque = FloatField(null=True)
    front_left_x = FloatField(null=True)
    front_left_y = FloatField(null=True)
    front_left_z = FloatField(null=True)
    front_right_x = FloatField(null=True)
    front_right_y = FloatField(null=True)
    front_right_z = FloatField(null=True)
    front_track_width_half = FloatField(null=True)
    front_wheelbase_distance = FloatField(null=True)
    gears_count = IntegerField(null=True)
    gears_ratios = TextField(null=True)
    has_rear_hitch = IntegerField(null=True)
    id = CharField(primary_key=True)
    mass = FloatField(null=True)
    max_occupants = IntegerField(null=True)
    mud_level_max_default = FloatField(null=True)
    mud_level_min_default = FloatField(null=True)
    physics_group = ForeignKeyField(column_name='physics_group_id', field='id', model=UtilVehiclePhysicsGroups, null=True)
    pk_id = IntegerField(null=True)
    rear_left_x = FloatField(null=True)
    rear_left_y = FloatField(null=True)
    rear_left_z = FloatField(null=True)
    rear_right_x = FloatField(null=True)
    rear_right_y = FloatField(null=True)
    rear_right_z = FloatField(null=True)
    rear_track_width_half = FloatField(null=True)
    rear_wheelbase_distance = FloatField(null=True)
    rust_level_max_default = FloatField(null=True)
    rust_level_min_default = FloatField(null=True)
    scratch_level_max_default = FloatField(null=True)
    scratch_level_min_default = FloatField(null=True)
    spawn_chance = FloatField(null=True)
    speed_modifier = FloatField(null=True)
    suspension_damping_rate = FloatField(null=True)
    suspension_spring_rate = FloatField(null=True)
    top_speed = FloatField(null=True)
    vehicle_type = ForeignKeyField(column_name='vehicle_type_id', field='id', model=UtilVehicleTypes, null=True)
    wheel_count = IntegerField(null=True)
    wheel_offset_00 = TextField(null=True)
    wheel_offset_01 = TextField(null=True)
    wheel_offset_02 = TextField(null=True)
    wheel_offset_03 = TextField(null=True)
    wheels_included = IntegerField(null=True)

    class Meta:
        table_name = 'DATA_vehicle'

class UtilVehicleAccessoryTypes(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vehicle_accessory_types'

class DataVehicleAccessory(BaseModel):
    accessory_type = ForeignKeyField(column_name='accessory_type_id', field='id', model=UtilVehicleAccessoryTypes, null=True)
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    inherit_segmentation = IntegerField(null=True)
    is_license_plate = IntegerField(null=True)
    is_roof = IntegerField(null=True)
    is_trunk = IntegerField(null=True)
    needs_parent = IntegerField(null=True)
    pk_id = IntegerField(null=True)
    supported_child_tags = TextField(null=True)
    tag = TextField(null=True)

    class Meta:
        table_name = 'DATA_vehicle_accessory'

class DataVehicleTypeSpawnChance(BaseModel):
    id = CharField(primary_key=True)
    spawn_chance = FloatField(null=True)
    vehicle_type = ForeignKeyField(column_name='vehicle_type_id', field='id', model=UtilVehicleTypes, null=True)

    class Meta:
        table_name = 'DATA_vehicle_type_spawn_chance'

class DataVehicleWheelOffset(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)
    wheel_index = IntegerField(null=True)
    wheel_offset = TextField(null=True)

    class Meta:
        table_name = 'DATA_vehicle_wheel_offset'

class DataWheel(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    pk_id = IntegerField(null=True)
    radius = FloatField(null=True)

    class Meta:
        table_name = 'DATA_wheel'

class DataWindow(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    leg_height = FloatField(null=True)

    class Meta:
        table_name = 'DATA_window'

class InfoAssetCountries(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    country = ForeignKeyField(column_name='country_id', field='id', model=ObjCountries, null=True)
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'INFO_asset_countries'

class InfoMaterialClassification(BaseModel):
    classification_id = IntegerField(null=True, unique=True)
    classification_name = CharField(unique=True)
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'INFO_material_classification'

class InfoAssetMaterial(BaseModel):
    classification = ForeignKeyField(column_name='classification_id', field='id', model=InfoMaterialClassification)
    id = CharField(primary_key=True)
    path = TextField(null=True, unique=True)

    class Meta:
        table_name = 'INFO_asset_material'

class InfoAssetPathsSource(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    path = TextField(null=True)

    class Meta:
        table_name = 'INFO_asset_paths_source'

class InfoAssetPathsUnreal(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    combine_box = IntegerField(null=True)
    id = CharField(primary_key=True)
    path = TextField(null=True)
    pk_id = IntegerField(null=True)
    unreal_id = IntegerField(null=True)

    class Meta:
        table_name = 'INFO_asset_paths_unreal'

class UtilTags(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_tags'

class InfoAssetTagsSource(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    pk_id = IntegerField(null=True)
    tag = ForeignKeyField(column_name='tag_id', field='id', model=UtilTags, null=True)

    class Meta:
        table_name = 'INFO_asset_tags_source'

class InfoAssetTagsUnreal(BaseModel):
    id = CharField(primary_key=True)
    tag = ForeignKeyField(column_name='tag_id', field='id', model=UtilTags, null=True)
    unreal_id = IntegerField(null=True)
    unreal_path = ForeignKeyField(column_name='unreal_path_id', field='id', model=InfoAssetPathsUnreal, null=True)

    class Meta:
        table_name = 'INFO_asset_tags_unreal'

class InfoPointCachePathsUnreal(BaseModel):
    id = CharField(primary_key=True)
    path = TextField(null=True)
    pk_id = IntegerField(null=True)
    unreal = ForeignKeyField(column_name='unreal_id', field='id', model=InfoAssetPathsUnreal, null=True)

    class Meta:
        table_name = 'INFO_point_cache_paths_unreal'

class UtilSegmentationCategoriesPanoptic(BaseModel):
    id = CharField(primary_key=True)
    is_thing = IntegerField(null=True)
    name = TextField(null=True, unique=True)
    pk_id = IntegerField(null=True)

    class Meta:
        table_name = 'UTIL_segmentation_categories_panoptic'

class UtilSegmentationCategoriesCuboid3D(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)
    pk_id = IntegerField(null=True)

    class Meta:
        table_name = 'UTIL_segmentation_categories_cuboid_3d'

class InfoSegmentation(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    cuboid_3d_id = ForeignKeyField(column_name='cuboid_3d_id_id', field='id', model=UtilSegmentationCategoriesCuboid3D, null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)
    no_decals = IntegerField(null=True)
    no_segmentation = IntegerField(null=True)
    no_shadow = IntegerField(null=True)
    panoptic_id = ForeignKeyField(column_name='panoptic_id_id', field='id', model=UtilSegmentationCategoriesPanoptic, null=True)

    class Meta:
        table_name = 'INFO_segmentation'

class InfoSegmentationMaterials(BaseModel):
    force_opaque = IntegerField(null=True)
    id = CharField(primary_key=True)
    path = TextField(null=True)

    class Meta:
        table_name = 'INFO_segmentation_materials'

class InfoSegmentationNameMatch(BaseModel):
    deprecated = IntegerField(null=True)
    id = CharField(primary_key=True)
    no_decals = IntegerField(null=True)
    no_segmentation = IntegerField(null=True)
    no_shadow = IntegerField(null=True)
    notes = TextField(null=True)
    pattern = TextField(null=True)
    priority = IntegerField(null=True, unique=True)
    segmentation_category = ForeignKeyField(column_name='segmentation_category_id', field='id', model=UtilSegmentationCategoriesPanoptic, null=True)

    class Meta:
        table_name = 'INFO_segmentation_name_match'

class InfoTaxonomy(BaseModel):
    id = CharField(primary_key=True)
    name = TextField()
    parent = ForeignKeyField(column_name='parent_id', field='id', model='self', null=True)

    class Meta:
        table_name = 'INFO_taxonomy'

class InfoTaxonomyAssets(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True, unique=True)
    id = CharField(primary_key=True)
    taxonomy_node = ForeignKeyField(column_name='taxonomy_node_id', field='id', model=InfoTaxonomy, null=True)

    class Meta:
        table_name = 'INFO_taxonomy_assets'

class InfoTaxonomyAssetsNameMatch(BaseModel):
    id = CharField(primary_key=True)
    info_segmentation_name_match = ForeignKeyField(column_name='info_segmentation_name_match_id', field='id', model=InfoSegmentationNameMatch, unique=True)
    taxonomy_node = ForeignKeyField(column_name='taxonomy_node_id', field='id', model=InfoTaxonomy)

    class Meta:
        table_name = 'INFO_taxonomy_assets_name_match'

class InternalCustomer(BaseModel):
    code = TextField()
    id = CharField(primary_key=True)

    class Meta:
        table_name = 'INTERNAL_customer'

class InternalCustomerSpecificAssets(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets, null=True)
    customer = ForeignKeyField(column_name='customer_id', field='id', model=InternalCustomer, null=True)
    id = CharField(primary_key=True)
    name = TextField(null=True)

    class Meta:
        table_name = 'INTERNAL_customer_specific_assets'

class ObjAssetThumbnail(BaseModel):
    asset = ForeignKeyField(column_name='asset_id', field='id', model=ObjAssets)
    id = CharField(primary_key=True)
    tag = TextField()
    thumbnail = CharField()

    class Meta:
        table_name = 'OBJ_asset_thumbnail'

class PairAssetGrouping(BaseModel):
    child = ForeignKeyField(column_name='child_id', field='id', model=ObjAssets, null=True)
    id = CharField(primary_key=True)
    parent = ForeignKeyField(backref='OBJ_assets_parent_set', column_name='parent_id', field='id', model=ObjAssets, null=True)

    class Meta:
        table_name = 'PAIR_asset_grouping'

class PairSocketTypes(BaseModel):
    child = ForeignKeyField(column_name='child_id', field='id', model=UtilSocketTypes, null=True)
    id = CharField(primary_key=True)
    parent = ForeignKeyField(backref='UTIL_socket_types_parent_set', column_name='parent_id', field='id', model=UtilSocketTypes, null=True)

    class Meta:
        table_name = 'PAIR_socket_types'

class PairVehicleAccessory(BaseModel):
    accessory_class = TextField(null=True)
    accessory_name = TextField(null=True)
    id = CharField(primary_key=True)
    vehicle = ForeignKeyField(column_name='vehicle_id', field='id', model=ObjAssets, null=True)
    vehicle_name = TextField(null=True)

    class Meta:
        table_name = 'PAIR_vehicle_accessory'

class UtilVehicleAccessorySockets(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vehicle_accessory_sockets'

class PairVehicleAccessorySockets(BaseModel):
    accessory = ForeignKeyField(column_name='accessory_id', field='id', model=DataVehicleAccessory, null=True)
    id = CharField(primary_key=True)
    pk_id = IntegerField(null=True)
    probability = FloatField(null=True)
    socket = ForeignKeyField(column_name='socket_id', field='id', model=UtilVehicleAccessorySockets, null=True)

    class Meta:
        table_name = 'PAIR_vehicle_accessory_sockets'

class PairVehicleColor(BaseModel):
    chance = FloatField(null=True)
    id = CharField(primary_key=True)
    unreal = ForeignKeyField(column_name='unreal_id', field='id', model=InfoAssetPathsUnreal, null=True)
    vehicle_color = TextField(null=True)
    vehicle_id = IntegerField(null=True)
    vehicle_name = TextField(null=True)

    class Meta:
        table_name = 'PAIR_vehicle_color'

class PairVehicleRoofAccessory(BaseModel):
    accessory_id = ForeignKeyField(column_name='accessory_id_id', field='id', model=DataVehicleAccessory, null=True)
    accessory_name = ForeignKeyField(column_name='accessory_name_id', field='id', model=ObjAssets, null=True)
    chance = FloatField(null=True)
    id = CharField(primary_key=True)
    vehicle = ForeignKeyField(column_name='vehicle_id', field='id', model=DataVehicle, null=True)

    class Meta:
        table_name = 'PAIR_vehicle_roof_accessory'

class PairVehicleTrunkAccessory(BaseModel):
    accessory_id = ForeignKeyField(column_name='accessory_id_id', field='id', model=DataVehicleAccessory, null=True)
    accessory_name = ForeignKeyField(column_name='accessory_name_id', field='id', model=ObjAssets, null=True)
    chance = FloatField(null=True)
    id = CharField(primary_key=True)
    vehicle = ForeignKeyField(column_name='vehicle_id', field='id', model=DataVehicle, null=True)

    class Meta:
        table_name = 'PAIR_vehicle_trunk_accessory'

class PairVehicleWheel(BaseModel):
    id = CharField(primary_key=True)
    vehicle = ForeignKeyField(column_name='vehicle_id', field='id', model=DataVehicle, null=True)
    wheel = ForeignKeyField(column_name='wheel_id', field='id', model=DataWheel, null=True)

    class Meta:
        table_name = 'PAIR_vehicle_wheel'

class PairVehicleWheelCombo(BaseModel):
    chance = FloatField(null=True)
    id = CharField(primary_key=True)
    style_combo = TextField(null=True)
    vehicle = ForeignKeyField(column_name='vehicle_id', field='id', model=ObjAssets, null=True)
    vehicle_name = TextField(null=True)
    wheel_combo = TextField(null=True)

    class Meta:
        table_name = 'PAIR_vehicle_wheel_combo'

class UtilUnits(BaseModel):
    display_name = TextField(null=True, unique=True)
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_units'

class UtilVehicleAccessoryTags(BaseModel):
    id = CharField(primary_key=True)
    name = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_vehicle_accessory_tags'

class UtilVehiclePhysicsGroupsDefaultValues(BaseModel):
    field_name = CharField()
    id = CharField(primary_key=True)
    physics_group = ForeignKeyField(column_name='physics_group_id', field='id', model=UtilVehiclePhysicsGroups, null=True)
    value = TextField()

    class Meta:
        table_name = 'UTIL_vehicle_physics_groups_default_values'

class UtilWheelBpSuffix(BaseModel):
    id = CharField(primary_key=True)
    suffix = TextField(null=True, unique=True)

    class Meta:
        table_name = 'UTIL_wheel_bp_suffix'

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        table_name = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType)
    name = CharField()

    class Meta:
        table_name = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)

    class Meta:
        table_name = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = BooleanField()
    is_staff = BooleanField()
    is_superuser = BooleanField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        table_name = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(column_name='group_id', field='id', model=AuthGroup)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(column_name='permission_id', field='id', model=AuthPermission)
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class AuthenticationToken(BaseModel):
    id = CharField(primary_key=True)
    is_active = BooleanField()
    token = CharField()

    class Meta:
        table_name = 'authentication_token'

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(column_name='content_type_id', field='id', model=DjangoContentType, null=True)
    object_id = TextField(null=True)
    object_repr = CharField()
    user = ForeignKeyField(column_name='user_id', field='id', model=AuthUser)

    class Meta:
        table_name = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        table_name = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        table_name = 'django_session'

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

