# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Sim and related objects
"""

from dataclasses import dataclass
from typing import TypeVar, Type, List

from dacite import from_dict

from pd.core import PdError
from pd.management.http_client import get_http_client

T = TypeVar('T')


@dataclass
class SimVersion:
    """
    Available version of Step Sim server
    """
    name: str
    """Sim version name"""

    _RESOURCE_NAME = 'sim_versions'

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request('get', url)
        sim_versions = [from_dict(data_class=SimVersion, data=v) for v in content]
        return sim_versions
