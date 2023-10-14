# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Useful utilities based on Step functionality

This subpackage provides helper classes and functions that use Step
API to provide useful functionality
"""

from .scripting import StepScriptContext, common_step_options
from .snapshot import generate_camera_pose_for_rotated_bbox, get_asset_rotated_bbox, get_location_for_asset_snap
