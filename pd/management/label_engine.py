# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Label Engine and related objects
"""

from dataclasses import dataclass
from typing import List, Type, TypeVar

from dacite import from_dict

from pd.core import PdError
from pd.management.http_client import get_http_client

T = TypeVar("T")


@dataclass
class LabelEngineVersion:
    """
    Available version of Step Label Engine server
    """

    name: str
    """Label Engine version name"""

    _RESOURCE_NAME = "le_versions"

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request("get", url)
        le_versions = [from_dict(data_class=LabelEngineVersion, data=v) for v in content]
        return le_versions
