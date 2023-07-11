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

from .snapshot import get_asset_rotated_bbox, generate_camera_pose_for_rotated_bbox, get_location_for_asset_snap
from .scripting import common_step_options, StepScriptContext
