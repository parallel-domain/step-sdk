# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Simulator messages
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass
class Raycast:
    """
    A single raycast request
    """

    origin: Tuple[float, float, float]
    """
    Origin of the raycast request
    """

    direction: Tuple[float, float, float]
    """
    Direction of the raycast request
    """

    max_distance: float
    """
    Maximum distance of raycast request
    """


@dataclass
class RaycastHit:
    """
    A single hit from a raycast request
    """

    position: Tuple[float, float, float]
    """
    Impact point in world space where the ray hit
    """

    normal: Tuple[float, float, float]
    """
    Normal of the surface the ray hit
    """

    surface_flag: int
    """
    Surface flag of the surface the ray hit
    """
