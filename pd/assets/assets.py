# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Asset metadata and references

This module provides references and metadata information about all the available assets.
This is a lightweight wrapper around the underlying `asset_registry.db` SQLite database.

It uses the :mod:`peewee` package to provide an ORM layer.
For example, :class:`~pd.assets.ObjAssets` provides access to the table OBJ_assets.

This module also provides a few convenience functions to query the Asset Registry.

You will need to initialize the Asset Registry with one of these two functions
before using the ORM classes or convenience functions in this module.
  * :func:`init_asset_registry_version` if using a Step server
  * :func:`init_asset_registry_file` if using a local Ig

Before calling :func:`init_asset_registry_version`, make sure that you have
set the configuration required by :mod:`pd.management` for Step Management API.
"""
from pathlib import Path
from typing import Iterator, List, Tuple
from uuid import UUID

import pd.internal.assets.asset_registry as asset_registry
from pd.core import PdError
from pd.internal.assets.asset_registry import (
    DataVehicle,
    DataVehicleWheelOffset,
    DataWheel,
    ObjAssets,
    PairVehicleColor,
    PairVehicleWheel,
    PairVehicleWheelCombo,
    UtilAssetCategories,
    database,
)
from pd.management import IgVersion, fetch_ig_asset_registry
from pd.management.utils import is_uuid
from pd.state.pose6d import Pose6D


def init_asset_registry_file(path: Path):
    """
    Initialize the Asset Registry from a file

    Args:
        path: Path to asset registry file
    """
    asset_registry.database.init(str(path))


def init_asset_registry_version(ig_version: str):
    """
    Initialize the Asset Registry for a given :class:`~IgVersion`

    Note - this queries the Step Management API to fetch the Asset Registry.
    Configuration required by :mod:`pd.management` must be set before calling
    this function.

    Args:
        ig_version: Ig version name / IG artifact UUID
    """
    # Check for local copy of asset registry
    internal_asset_package_path = Path(asset_registry.__file__).resolve().parent
    registry_path = internal_asset_package_path / "downloaded" / ig_version / "asset_registry.db"
    if registry_path.is_file():
        asset_registry.database.init(str(registry_path))
        return

    # Need to download the asset registry
    # Validate that Ig version is available to us
    if not is_uuid(ig_version):
        try:
            internal_version = next(iv.internal_version for iv in IgVersion.list() if iv.name == ig_version)
        except StopIteration:
            raise PdError(
                f"Couldn't fetch Asset Registry for Ig version '{ig_version}'. This Ig version is not available."
            )
        version = internal_version or ig_version
    else:
        version = UUID(ig_version)
    registry_content = fetch_ig_asset_registry(version)
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    with registry_path.open("wb") as registry_file:
        registry_file.write(registry_content)
    asset_registry.database.init(str(registry_path))


def get_asset_registry_path() -> str:
    """
    Returns the path of the Asset Registry file currently in use

    Returns:
        Path to asset registry db
    """
    return database.database


def asset_coords_to_sim_coords(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """
    Converts coordinates from asset coordinate frame to Sim coordinate frame

    The asset registry stores coordinates in the asset coordinate frame. This function converts
    them to the Sim coordinate frame that is used in :class:`~pd.state.State`.

    Returns:
        A tuple of (x, y, z) coordinates in Sim coordinate frame
    """
    return -x, z, y


def asset_dimension_to_sim_dimension(x: float, y: float, z: float) -> Tuple[float, float, float]:
    """
    Converts dimensions from asset coordinate frame to Sim coordinate frame

    The asset registry stores coordinates in the asset coordinate frame. This function converts
    them to the Sim coordinate frame that is used in :class:`~pd.state.State`.

    Returns:
        A tuple of (x, y, z) coordinates in Sim coordinate frame
    """
    return x, z, y


def asset_pivot_point_to_asset_geometric_center_offset(
    min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float
) -> Tuple[float, float, float]:
    """
    Calculates the offset from the pivot point to the geometric center for an asset in its
    internal asset coordinate system.
    If asset has a rotation, it needs to be applied outside of this function.

    Returns:
        A tuple of (x, y, z) coordinates in asset coordinate frame
    """
    dim_x, dim_y, dim_z = (max_x - min_x), (max_y - min_y), (max_z - min_z)
    offset_x, offset_y, offset_z = max_x - dim_x / 2, max_y - dim_y / 2, max_z - dim_z / 2

    return offset_x, offset_y, offset_z


def asset_pivot_point_to_sim_geometric_center_offset(
    min_x: float, max_x: float, min_y: float, max_y: float, min_z: float, max_z: float
) -> Tuple[float, float, float]:
    """
    Calculates the offset from the pivot point to the geometric center for an asset in Sim coordinate system.
    If asset has a rotation, it needs to be applied outside of this function.

    Returns:
        A tuple of (x, y, z) coordinates in Sim coordinate frame
    """
    offset_x_asset, offset_y_asset, offset_z_asset = asset_pivot_point_to_asset_geometric_center_offset(
        min_x=min_x, max_x=max_x, min_y=min_y, max_y=max_y, min_z=min_z, max_z=max_z
    )

    offset_x, offset_y, offset_z = asset_coords_to_sim_coords(x=offset_x_asset, y=offset_y_asset, z=offset_z_asset)

    return offset_x, offset_y, offset_z


def get_vehicle_colors(vehicle_name) -> List[str]:
    """
    Returns names of colors available for a given vehicle

    Args:
        vehicle_name: Name of the vehicle

    Returns:
        List of colors
    """
    query = PairVehicleColor.select(PairVehicleColor.vehicle_color).where(PairVehicleColor.vehicle_name == vehicle_name)
    return [row.vehicle_color for row in query]


def get_vehicle_names() -> Iterator[str]:
    """
    Returns names of all vehicles

    Returns:
        Names of all vehicles
    """
    return get_asset_names_in_category("vehicle")


def get_vehicle_wheel_names(vehicle_name):
    """
    Returns name of wheels that belong to a given vehicle

    Args:
        vehicle_name: Name of the vehicle

    Returns:
        Wheel name
    """
    VehicleObjAssets = ObjAssets.alias()
    query = ObjAssets.select(ObjAssets.name)
    query = query.join(DataWheel).join(PairVehicleWheel).join(DataVehicle)
    query = query.join(VehicleObjAssets, on=(VehicleObjAssets.id == DataVehicle.asset))
    query = query.where(VehicleObjAssets.name == vehicle_name)
    return [row.name for row in query]


def get_vehicle_wheel_combos(vehicle_name):
    """
    Returns combos of wheels that belong to a given vehicle

    Args:
        vehicle_name: Name of the vehicle

    Returns:
        Wheel Combos
    """

    VehicleObjAssets = ObjAssets.alias()
    query = PairVehicleWheelCombo.select(PairVehicleWheelCombo.wheel_combo)
    query = query.join(VehicleObjAssets, on=(VehicleObjAssets.id == PairVehicleWheelCombo.vehicle))
    query = query.where(VehicleObjAssets.name == vehicle_name)
    return [row.wheel_combo.split(" ") if " " in row.wheel_combo else [row.wheel_combo] for row in query]


def get_vehicle_wheel_combo_styles(vehicle_name):
    """
    Returns style combo of wheels that belong to a given vehicle

    Args:
        vehicle_name: Name of the vehicle

    Returns:
        Wheel Combos style
    """

    VehicleObjAssets = ObjAssets.alias()
    query = PairVehicleWheelCombo.select(PairVehicleWheelCombo.style_combo)
    query = query.join(VehicleObjAssets, on=(VehicleObjAssets.id == PairVehicleWheelCombo.vehicle))
    query = query.where(VehicleObjAssets.name == vehicle_name)
    combo_styles = [row.style_combo.split(" ") if " " in row.style_combo else [row.style_combo] for row in query]
    return combo_styles


def get_wheel_radius(wheel_name: str) -> float:
    """
    Returns radius of a wheel

    Args:
        wheel_name: Name of the wheel

    Returns:
        Radius in metres
    """
    query = DataWheel.select().join(ObjAssets).where(ObjAssets.name == wheel_name)
    wheel_data = next(iter(query))
    return wheel_data.radius


def get_vehicle_wheel_poses(vehicle_name: str, wheel_name: str) -> List[Pose6D]:
    """
    Returns the wheel poses for a given vehicle and wheel combination

    Args:
        vehicle_name: Name of the vehicle
        wheel_name: Name of the wheel

    Returns:
        List of 4 Poses corresponding to wheels in back right, back left, front right, front left,
        in that order
    """
    # The y-offset is determined by the wheel_offsets and the bounding_box centers
    # The z-offset is determined by wheel radius
    query = DataVehicle.select().join(ObjAssets).where(ObjAssets.name == vehicle_name)
    vehicle_data = next(iter(query))
    (wheel_offset_front_left_s, wheel_offset_front_right_s, wheel_offset_back_left_s, wheel_offset_back_right_s) = (
        vehicle_data.wheel_offset_00,
        vehicle_data.wheel_offset_01,
        vehicle_data.wheel_offset_02,
        vehicle_data.wheel_offset_03,
    )
    if (
        not wheel_offset_front_left_s
        or not wheel_offset_front_right_s
        or not wheel_offset_back_left_s
        or not wheel_offset_back_right_s
    ):
        return []
    wheel_offset_front_left = tuple(map(float, wheel_offset_front_left_s.split(" ")))
    wheel_offset_front_right = tuple(map(float, wheel_offset_front_right_s.split(" ")))
    wheel_offset_back_left = tuple(map(float, wheel_offset_back_left_s.split(" ")))
    wheel_offset_back_right = tuple(map(float, wheel_offset_back_right_s.split(" ")))
    wheel_radius = get_wheel_radius(wheel_name)
    # Note: Z-axis in bbox corresponds to Y-axis in sim coordinates
    vehicle_asset = ObjAssets.get(ObjAssets.name == vehicle_name)
    bbox_min_z, bbox_max_z = vehicle_asset.bbox_min_z, vehicle_asset.bbox_max_z
    y_center_offset = (bbox_min_z + bbox_max_z) / 2.0
    wheels = [
        Pose6D.from_translation(
            x_metres=wheel_offset_back_right[0],
            y_metres=wheel_offset_back_right[1] + y_center_offset,
            z_metres=wheel_radius,
        ),
        Pose6D.from_translation(
            x_metres=wheel_offset_back_left[0],
            y_metres=wheel_offset_back_left[1] + y_center_offset,
            z_metres=wheel_radius,
        ),
        Pose6D.from_translation(
            x_metres=wheel_offset_front_right[0],
            y_metres=wheel_offset_front_right[1] + y_center_offset,
            z_metres=wheel_radius,
        ),
        Pose6D.from_translation(
            x_metres=wheel_offset_front_left[0],
            y_metres=wheel_offset_front_left[1] + y_center_offset,
            z_metres=wheel_radius,
        ),
    ]
    return wheels


def get_vehicle_wheel_combo_poses(vehicle_name: str, wheel_combo: List[str]) -> List[Pose6D]:
    """
    Returns the wheel poses for a given vehicle and wheel combo

    Args:
        vehicle_name: Name of the vehicle
        wheel_comb: list of pairs of wheels.

    Returns:
        List of multiple Poses corresponding to wheels from combo.
    """

    wheels = []
    i = 0
    for wheel_name in wheel_combo:
        right_wheel_pose = get_vehicle_wheel_pose(vehicle_name, wheel_name, i)
        i += 1
        left_wheel_pose = get_vehicle_wheel_pose(vehicle_name, wheel_name, i)

        if left_wheel_pose:
            wheels.append(left_wheel_pose)
        if right_wheel_pose:
            wheels.append(right_wheel_pose)
        i += 1

    # making sure that wheel offset from multi axle vehicle is removed
    # multi axle vehicle uses index 0,1,4,5
    if len(wheels) == 6:
        wheels.pop(3)
        wheels.pop(2)

    # making sure that poses are not too long
    return wheels[:4]


def get_vehicle_wheel_pose(vehicle_name: str, wheel_name: str, wheel_index: int) -> Pose6D:
    """
    Returns the wheel pose for a given vehicle and one wheel combination

    Args:
        vehicle_name: Name of the vehicle
        wheel_name: Name of the wheel
        wheel_index: Index of the wheel on the vehicle

    Returns:
        1 wheel pose
    """
    # The y-offset is determined by the wheel_offsets and the bounding_box centers
    # The z-offset is determined by wheel radius

    query = (
        DataVehicleWheelOffset.select()
        .join(ObjAssets)
        .where(ObjAssets.name == vehicle_name)
        .where(DataVehicleWheelOffset.wheel_index == wheel_index)
    )
    vehicle_data = next(iter(query))

    if not vehicle_data.wheel_offset:
        return None

    wheel_offset = tuple(map(float, vehicle_data.wheel_offset.split(" ")))
    wheel_radius = get_wheel_radius(wheel_name)
    # Note: Z-axis in bbox corresponds to Y-axis in sim coordinates
    vehicle_asset = ObjAssets.get(ObjAssets.name == vehicle_name)
    bbox_min_z, bbox_max_z = vehicle_asset.bbox_min_z, vehicle_asset.bbox_max_z
    y_center_offset = (bbox_min_z + bbox_max_z) / 2.0

    wheel = Pose6D.from_translation(
        x_metres=wheel_offset[0],
        y_metres=wheel_offset[1] + y_center_offset,
        z_metres=wheel_radius,
    )
    return wheel


def get_category_names() -> Iterator[str]:
    """
    Returns names of all asset categories

    Returns:
        Names of all asset categories
    """
    query = UtilAssetCategories.select(UtilAssetCategories.name)
    for obj in query:
        yield obj.name


def get_asset_names_in_category(category: str) -> Iterator[str]:
    """
    Returns names of all asset in a given category

    Returns:
        Names of assets
    """
    query = ObjAssets.select(ObjAssets.name).join(UtilAssetCategories).where(UtilAssetCategories.name == category)
    for obj in query:
        yield obj.name
