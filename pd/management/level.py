# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Level and related objects
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional, Type, TypeVar
from uuid import UUID

from dacite import Config, from_dict

from pd.management.http_client import get_http_client

T = TypeVar("T")


@dataclass
class Levelpak:
    """
    Available Levelpak
    """

    name: str
    """Levelpak name"""

    default_version: Optional[str]
    """Default version selected when no version is specified"""

    versions: List[str]
    """List of versions available"""

    _RESOURCE_NAME = "levelpaks"

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request("get", url)
        levelpaks = [from_dict(data_class=Levelpak, data=v) for v in content]
        return levelpaks


@dataclass
class LevelpakVersion:
    """
    Available Levelpak versions
    """

    levelpak: str
    """Levelpak name"""

    version: str
    """Levelpak version"""

    internal_version: UUID
    """Levelpak internal version"""

    _RESOURCE_NAME = "levelpaks/versions"
    _DACITE_CONFIG = Config(cast=[UUID])

    @classmethod
    def list(cls) -> List[LevelpakVersion]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request("get", url)
        levelpak_versions = [from_dict(data_class=LevelpakVersion, data=v, config=cls._DACITE_CONFIG) for v in content]
        return levelpak_versions


def fetch_level_umd(internal_version: str) -> bytes:
    """
    Fetch the Umd file associated with a Levelpak version

    Args:
        internal_version: Levelpak internal version

    Returns:
        Bytes of the Umd file
    """
    http_client = get_http_client()
    url = f"levelpaks/umd/{internal_version}"
    _, content = http_client.request("get", url, raw_response=True)
    return content
