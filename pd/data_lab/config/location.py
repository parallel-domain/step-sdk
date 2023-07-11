# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
from typing import Optional

from dataclasses import dataclass


@dataclass
class Location:
    name: str
    version: Optional[str] = None
    category: Optional[str] = None


@dataclass
class LatLonLocation(Location):
    latitude: float = 37.78065  # San Francisco
    longitude: float = -122.416781  # San Francisco
