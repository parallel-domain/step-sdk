# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Literal, Tuple

import pd.management
from pd.assets import init_asset_registry_file, init_asset_registry_version
from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.internal.proto.umd.generated.wrapper.UMD_pb2 import UniversalMap
from pd.management import IgVersion, Ig
from pd.umd import load_map_from_file, load_map as load_map_from_step


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


def datalab_context_exists() -> bool:
    if _GLOBAL_CONTEXT is not None:
        return True
    else:
        return False


def setup_datalab(
    version: str, environment: Literal["prod", "stage", "dev"] = "prod", fail_on_version_mismatch: bool = True
):
    """
    Set up global context for Data Lab

    This function should be called at the beginning of every Data Lab script.
    When using Data Lab in cloud mode, ensure that the following environment variables are set:
     * PD_CLIENT_ORG_ENV: Org name
     * PD_CLIENT_STEP_API_KEY_ENV: Step API Key
     * PD_CLIENT_CREDENTIALS_PATH_ENV: Path to Step credentials file (.pem file)
    When using Data Lab in local mode, call this function with the version set to "local".

    Args:
        version: Data Lab version for cloud workflow, or "local" for local workflow
        environment: Environment name, one of 'prod', 'stage' or 'dev'
        fail_on_version_mismatch: Fail when version of components (Sim, Ig, etc) doesn't match Data Lab version
    """
    global _GLOBAL_CONTEXT
    if version != "local":
        # Cloud mode
        needed_env_vars_for_cloud = [
            "PD_CLIENT_ORG_ENV",
            "PD_CLIENT_STEP_API_KEY_ENV",
            "PD_CLIENT_CREDENTIALS_PATH_ENV",
        ]
        if not all([n in os.environ for n in needed_env_vars_for_cloud]):
            raise PdError(
                "Some of the required environment variables are not set. "
                "Please ensure all of the following environment variables are set: "
                + ", ".join(needed_env_vars_for_cloud)
            )
        pd.management.api_key = os.environ["PD_CLIENT_STEP_API_KEY_ENV"]
        pd.management.org = os.environ["PD_CLIENT_ORG_ENV"]
        if environment == "stage":
            pd.management.api_url = pd.management._API_URL_STAGE
        elif environment == "dev":
            pd.management.api_url = pd.management._API_URL_DEV
        elif environment != "prod":
            raise PdError(f"Unknown environment name '{environment}' passed in setup_datalab().")
        ig_versions = {iv.name for iv in IgVersion.list()}
        if version not in ig_versions and fail_on_version_mismatch:
            raise PdError(
                f"Data Lab version '{version}' is not available. Please choose a different version "
                "when calling setup_datalab()."
            )
        init_asset_registry_version(version)
        _GLOBAL_CONTEXT = DataLabContext(
            is_mode_local=False,
            org=pd.management.org,
            version=version,
            client_cert_file=os.environ["PD_CLIENT_CREDENTIALS_PATH_ENV"],
            fail_on_version_mismatch=fail_on_version_mismatch,
        )
    else:
        # Local mode
        _GLOBAL_CONTEXT = DataLabContext(
            is_mode_local=True, client_cert_file=os.environ.get("PD_CLIENT_CREDENTIALS_PATH_ENV", None)
        )
        local_asset_registry_path = Path(os.environ.get("PD_ROOT", "")) / "assets" / "asset_registry.db"
        if not local_asset_registry_path.is_file():
            raise PdError(
                f"Couldn't find asset registry at {str(local_asset_registry_path)}. "
                "Please make sure env var PD_ROOT is set and asset registry exists at "
                "$PD_ROOT/assets/asset_registry.db"
            )
        init_asset_registry_file(local_asset_registry_path)


def validate_instance_address(
    instance_type: Literal["sim", "ig", "le"], name: Optional[str] = None, address: Optional[str] = None
) -> Tuple[str, str, str]:
    context = get_datalab_context()
    client_cert_file = context.client_cert_file
    default_port = dict(sim=9002, ig=9000, le=9004)[instance_type]
    url_field = dict(sim="sim_url", ig="ig_url", le="le_url")[instance_type]
    instance_name = dict(sim="simulation", ig="render", le="label engine")[instance_type]

    if name and address:
        return address, name, client_cert_file
    if not context.is_mode_local and not name:
        raise PdError(f"A 'name' is required in a {instance_name} instance when running in cloud mode.")

    if context.is_mode_local:
        # Local mode, use local address if none is provided
        address = address or f"tcp://localhost:{default_port}"
    else:
        # Cloud mode, resolve the address
        try:
            ig = next(ig for ig in Ig.list() if ig.name == name)
        except StopIteration:
            raise PdError(
                f"Couldn't find an instance with the name '{name}'. " "Please verify that the name is correct."
            )
        if context.fail_on_version_mismatch:
            if ig.ig_version != context.version:
                raise PdError(
                    f"There's a mismatch between the selected Data Lab version ({context.version}) "
                    f"and the version of the {instance_name} instance ({ig.ig_version}). "
                    "To disable this check, pass fail_on_version_mismatch=False to setup_datalab()."
                )
        address = getattr(ig, url_field)
        if address is None:
            raise PdError(f"{instance_name} instance doesn't have a server.")
    return address, name, client_cert_file


def load_map(location: Location) -> UniversalMap:
    """
    Load map using the appropriate Data Lab context mode.

    Cloud mode will load the map from Step Management API.
    Local mode will load the map on the local system.

    Args:
        location: Location info for the map to load

    Returns:
        The loaded map
    """
    context = get_datalab_context()
    if context.is_mode_local:
        map_file = (
            Path(os.environ.get("PD_ROOT", "")) / "generated" / "locations" / location.name / f"{location.name}.umd"
        )
        if not map_file.is_file():
            raise PdError(
                f"Couldn't find local map (Umd) for map {location.name} at {str(map_file)}. "
                "Please download the map artifact."
            )
        return load_map_from_file(path=map_file)
    else:
        location_name, location_version = location.name, location.version
        if not location_version:
            # No location version is provided, use the version from Data Lab context
            location_version = context.version
        else:
            # Location version is provided, verify that it matches Data Lab context
            if context.fail_on_version_mismatch and location_version != context.version:
                raise PdError(
                    f"There's a mismatch between the selected Data Lab version ({context.version}) "
                    f"and the version of the requested map ({location_name} {location_version}). "
                    "To disable this check, pass fail_on_version_mismatch=False to setup_datalab()."
                )
        try:
            return load_map_from_step(name=location_name, version=location_version)
        except PdError as e:
            raise PdError(f"Couldn't load map {location.name} {location.version} from management API. Error: {str(e)}")
