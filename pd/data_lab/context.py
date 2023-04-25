# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import pd.management
from pd.assets import init_asset_registry_version, init_asset_registry_file

from pd.core import PdError
from pd.management import IgVersion


@dataclass
class DataLabContext:
    is_mode_local: bool = False
    """
    Indicates local mode for DataLab scripts.
    In local mode, no cloud Step resources are used.
    All Step applications (Step IG, Step Sim, etc) must be available locally.
    Step Management API is not used.
    Local copies of resources such as Asset Registry and Umd files must be provided.
    """

    org: Optional[str] = None
    """
    Org name. Only valid when :attr:`is_mode_local` is :obj:`False`
    """

    version: Optional[str] = None
    """
    DataLab version. Only valid when :attr:`is_mode_local` is :obj:`False`
    """

    client_cert_file: Optional[str] = None
    """
    Path to client certificate
    """

    fail_on_version_mismatch: bool = True
    """
    Fail when the version of components (Sim, Ig, etc) does not match
    the selected DataLab version in :attr:`version`.
    Only valid when :attr:`is_mode_local` is :obj:`False`
    """


_GLOBAL_CONTEXT: Optional[DataLabContext] = None


def get_datalab_context() -> DataLabContext:
    if _GLOBAL_CONTEXT is not None:
        return _GLOBAL_CONTEXT
    else:
        raise PdError("Data Lab context is not set. Did you remember to call pd.data_lab.context.setup_datalab()?")


def setup_datalab(version: Optional[str], fail_on_version_mismatch: bool = True):
    """
    Set up global context for Data Lab

    This function should be called at the beginning of every Data Lab script.
    When using Data Lab in cloud mode, ensure that the following environment variables are set:
     * PD_CLIENT_ORG_ENV: Org name
     * PD_CLIENT_STEP_API_KEY_ENV: Step API Key
     * PD_CLIENT_CREDENTIALS_PATH_ENV: Path to Step credentials file (.pem file)
    When using Data Lab in local mode, clear out these environment variables.

    Args:
        version: Data Lab version
        fail_on_version_mismatch: Fail when version of components (Sim, Ig, etc) doesn't match Data Lab version
    """
    global _GLOBAL_CONTEXT
    needed_env_vars_for_cloud = ["PD_CLIENT_ORG_ENV", "PD_CLIENT_STEP_API_KEY_ENV", "PD_CLIENT_CREDENTIALS_PATH_ENV"]
    if all([n in os.environ for n in needed_env_vars_for_cloud]):
        # Cloud mode
        pd.management.api_key = os.environ["PD_CLIENT_STEP_API_KEY_ENV"]
        pd.management.org = os.environ["PD_CLIENT_ORG_ENV"]
        ig_versions = set(iv.name for iv in IgVersion.list())
        if version not in ig_versions:
            raise PdError(f"Data Lab version '{version}' is not available. Please choose a different version "
                          "when calling setup_datalab().")
        init_asset_registry_version(version)
        _GLOBAL_CONTEXT = DataLabContext(
            is_mode_local=False,
            org=pd.management.org,
            version=version,
            client_cert_file=os.environ["PD_CLIENT_CREDENTIALS_PATH_ENV"],
            fail_on_version_mismatch=fail_on_version_mismatch
        )
    elif any([n in os.environ for n in needed_env_vars_for_cloud]):
        raise PdError("Some of the required environment variables are not set. "
                      "Please ensure all of the following environment variables are set: "
                      + ", ".join(needed_env_vars_for_cloud))
    else:
        # Local mode
        _GLOBAL_CONTEXT = DataLabContext(
            is_mode_local=True
        )
        local_asset_registry_path = Path(os.environ.get("PD_ROOT", "")) / 'assets' / 'asset_registry.db'
        if not local_asset_registry_path.is_file():
            raise PdError(f"Couldn't find asset registry at {str(local_asset_registry_path)}. "
                          "Please make sure env var PD_ROOT is set and asset registry exists at "
                          "$PD_ROOT/assets/asset_registry.db")
        init_asset_registry_file(local_asset_registry_path)
