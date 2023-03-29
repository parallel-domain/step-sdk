# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
IG and related objects
"""

from dataclasses import dataclass
from typing import TypeVar, Type, Optional, List, Dict
from enum import Enum
from datetime import datetime

from dacite import from_dict, Config

from pd.core import PdError
from pd.management.http_client import get_http_client


T = TypeVar('T')


class IgStatus(Enum):
    """
    Lifecycle status of a Step IG server instance
    """
    Starting = 'starting'
    Configuring = 'configuring'
    Running = 'running'
    Stopped = 'stopped'


class IgQuality(Enum):
    """
    Quality of a Step IG server instance
    """
    Low = 'low'
    High = 'high'


@dataclass
class Ig:
    """
    Managed Step IG server instance
    """

    self_url: str
    """Full URL for the Step server instance"""

    status: IgStatus
    """Status of the Step server instance"""

    step_url: Optional[str]
    """Deprecated: use occupants :attr:`ig_url` instead"""

    sim_url: Optional[str]
    """Address of the Step Sim server instance in the form ``protocol://host:port``"""

    ig_url: Optional[str]
    """Address of the Step IG server instance in the form ``protocol://host:port``"""

    sim_version: Optional[str]
    """Version of the Step Sim server instance"""

    ig_version: str
    """Version of the Step IG server instance"""

    created_at: datetime
    """Creation time for the Step server instance"""

    shutdown_time: Optional[datetime]
    """
    Time at which Step server instance will be shutdown.

    :obj:`None` if auto-shutdown was not requested or it was requested but
    Server instance isn't running yet.
    """

    levelpak: Dict[str, str]
    """
    Levelpak names and versions that are available in this Step server instance.

    Each key in this :obj:`dict` specifies the Levelpak name, and the value specifies the Levelpak
    version.
    Use the :class:`LevelpakVersion` object to retrieve additional Levelpak details.
    """

    @property
    def name(self) -> str:
        """Name of the Step IG server instance"""
        return self.self_url.split('/')[-1]

    _RESOURCE_NAME = 'ig'
    _DACITE_CONFIG = Config(type_hooks={datetime: datetime.fromisoformat}, cast=[IgStatus])

    @classmethod
    def create(cls: Type[T],
               sim_version: Optional[str] = None,
               ig_version: Optional[str] = None,
               quality: IgQuality = IgQuality.High,
               levelpaks: Optional[Dict[str, str]] = None,
               ttl: Optional[int] = None) -> T:
        """
        Create a Step IG server instance

        Args:
            sim_version: Sim version
            ig_version: Ig version
            quality: Ig quality
            levelpaks: :obj:`dict` specifying versions of Levelpaks that will be available in the Ig.
                       Only the Levelpaks specified will be available.
                       The dict key should contain the Levelpak name and the value should contain
                       the Levelpak version.
            ttl: Time-to-live in seconds. After this time the Ig will automatically be shutdown.
                 This time begins when Ig moves to the Running state.
                 If ttl is not specified, a ttl of 24-hours will be set by default.

        Returns:
            The created Ig
        """
        http_client = get_http_client()
        data = dict()
        data['quality'] = quality.value
        if sim_version:
            data['sim_version'] = sim_version
        if ig_version:
            data['ig_version'] = ig_version
        data['levelpak'] = levelpaks or {}
        if ttl:
            data['ttl'] = ttl
        url = cls._RESOURCE_NAME
        _, content = http_client.request('post', url, data=data)
        ig = from_dict(data_class=Ig, data=content, config=Ig._DACITE_CONFIG)
        # Backwards compatibility to step_url
        ig.ig_url = ig.ig_url or ig.step_url
        return ig

    @classmethod
    def read(cls: Type[T], name: str) -> T:
        if not name:
            raise PdError("Name cannot be empty")
        http_client = get_http_client()
        url = cls._RESOURCE_NAME + f'/{name}'
        _, content = http_client.request('get', url)
        ig = from_dict(data_class=Ig, data=content, config=Ig._DACITE_CONFIG)
        # Backwards compatibility to step_url
        ig.ig_url = ig.ig_url or ig.step_url
        return ig

    @classmethod
    def delete(cls: Type[T], name: str):
        if not name:
            raise PdError("Name cannot be empty")
        http_client = get_http_client()
        url = cls._RESOURCE_NAME + f'/{name}'
        http_client.request('delete', url)

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request('get', url)

        @dataclass
        class IgList:
            igs: List[Ig]

        ig_list = from_dict(data_class=IgList, data=content, config=Ig._DACITE_CONFIG)
        # Backwards compatibility to step_url
        for ig in ig_list.igs:
            ig.ig_url = ig.ig_url or ig.step_url
        return ig_list.igs


@dataclass
class IgVersion:
    """
    Available version of Step IG server
    """
    name: str
    """Ig version name"""

    _RESOURCE_NAME = 'ig_versions'

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        http_client = get_http_client()
        url = cls._RESOURCE_NAME
        _, content = http_client.request('get', url)
        ig_versions = [from_dict(data_class=IgVersion, data=v) for v in content]
        return ig_versions


def fetch_ig_asset_registry(ig_version: str) -> bytes:
    """
    Fetch the Asset Registry file associated with an :class:`IgVersion`

    Args:
        ig_version: :class:`IgVersion` name

    Returns:
        Bytes of the Asset Registry file
    """
    http_client = get_http_client()
    url = f'ig_versions/{ig_version}/asset_registry'
    _, content = http_client.request('get', url, raw_response=True)
    return content
