# Copyright (c) 2021 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
UMD schema utilities
"""

from pathlib import Path
from typing import Optional

import pd.internal.umd.UMD_pb2 as schema
from pd.core.errors import PdError
from pd.management import LevelpakVersion, Levelpak, fetch_level_umd


def load_umd_map_from_file(path: Path) -> schema.UniversalMap:
    """
    Load UMD map as a protobuf object

    Args:
        path: Path to the Umd file

    Returns:
        Map protobuf object
    """
    with path.open('rb') as umd_file:
        umd_map = schema.UniversalMap()
        umd_map.ParseFromString(umd_file.read())
    return umd_map



def load_umd_map(name: str, version: Optional[str] = None) -> schema.UniversalMap:
    """
    Load UMD map as a protobuf object for the given Level

    Note - this queries the Step Management API to fetch the Umd.
    Configuration required by :mod:`pd.management` must be set before calling
    this function.

    Args:
        name: Level name
        version: Level version. If no version is provided, the default version
                 will be selected

    Returns:
        Map protobuf object
    """
    import pd.internal.umd.maps as maps_package
    maps_package_path = Path(maps_package.__file__).resolve().parent

    # First try internal maps directory
    # These are the Umds for the test maps built into IG
    # These maps are versionless, so only try this if no version is provided
    if not version:
        umd_path = maps_package_path / f'{name}.umd'
        if umd_path.is_file():
            return load_umd_map_from_file(umd_path)

    # Next, see if the Umd already exists locally
    # We can only do this if a version is provided
    if version:
        umd_path = maps_package_path / 'downloaded' / f'{name}' / f'{version}' / f'{name}.umd'
        if umd_path.is_file():
            return load_umd_map_from_file(umd_path)

    # Fetch the map from Step Management API
    if not version:
        levels = Levelpak.list()
        try:
            version = next(l.default_version for l in levels if l.name == name)
        except StopIteration:
            raise PdError(f"Failed to fetch Umd for level named '{name}'. No such level exists.")
    level_versions = LevelpakVersion.list()
    try:
        level_internal_version = next(lv.internal_version for lv in level_versions
                                      if lv.levelpak == name and lv.version == version)
    except StopIteration:
        raise PdError(
            f"Failed to fetch Umd for level '{name}' with version '{version}'. "
            f"No such level and version combination exists."
        )
    umd_path = maps_package_path / 'downloaded' / f'{name}' / f'{version}' / f'{name}.umd'
    if not umd_path.is_file():
        umd_content = fetch_level_umd(level_internal_version)
        umd_path.parent.mkdir(parents=True, exist_ok=True)
        with umd_path.open('wb') as umd_file:
            umd_file.write(umd_content)
    return load_umd_map_from_file(umd_path)


def load_default_umd_map() -> schema.UniversalMap:
    """
    Load the default UMD map as a protobuf object

    Returns:
        Map protobuf object
    """
    return load_umd_map("Test_SF_6thAndMission_small_parking")
