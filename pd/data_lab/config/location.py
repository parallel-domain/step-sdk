# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from dataclasses import dataclass


@dataclass
class Location:
    name: str
    version: str = None
    category: str = None
