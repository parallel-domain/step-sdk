# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Everything to do with Assets
"""

from pd.internal.assets.asset_registry import (  # noqa
    DataSign,
    DataVehicle,
    DataVehicleTypeSpawnChance,
    DataWheel,
    InfoSegmentation,
    ObjAssets,
    ObjCountries,
    UtilAssetCategories,
    UtilSegmentationCategoriesPanoptic,
    UtilVehicleTypes,
)

from .assets import (
    asset_coords_to_sim_coords,
    get_asset_names_in_category,
    get_asset_registry_path,
    get_category_names,
    get_vehicle_colors,
    get_vehicle_names,
    get_vehicle_wheel_names,
    get_vehicle_wheel_poses,
    get_wheel_radius,
    init_asset_registry_file,
    init_asset_registry_version,
)
