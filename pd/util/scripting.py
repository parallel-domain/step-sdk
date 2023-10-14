# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utilities for scripting, such as handling common inputs.
"""
import os
from dataclasses import dataclass
from functools import partial, wraps
from pathlib import Path
from typing import Dict, Optional

import click
from requests import HTTPError

import pd.internal.umd.UMD_pb2 as schema
import pd.management
from pd.assets import init_asset_registry_file, init_asset_registry_version
from pd.core import PdError
from pd.internal.proto.umd.generated.wrapper.UMD_pb2 import UniversalMap
from pd.management import Ig
from pd.session import is_server_url
from pd.umd import load_umd_map, load_umd_map_from_file


@dataclass
class StepScriptContext:
    internal_dev: bool
    """
    Indicates an internal dev workflow
    In internal dev workflow, Step Management API is not used.
    Addresses for any instances (Sim, IG, etc) must be explicitly provided.
    """

    ig: str
    """
    Address for Ig instance
    """

    sim: Optional[str]
    """
    Address for Sim instance
    May not be set if the script doesn't require Sim
    """

    label_engine: Optional[str]
    """
    Address for Label Engine instance
    May not be set if the script doesn't require Label Engine
    """

    org: Optional[str] = None
    """
    Org name. Only valid when :attr:`internal_dev` is :obj:`False`
    """

    api_key: Optional[str] = None
    """
    API Key. Only valid when :attr:`internal_dev` is :obj:`False`
    """

    ig_version: Optional[str] = None
    """
    Ig version name. Only valid when :attr:`internal_dev` is :obj:`False`
    """

    client_cert_file: Optional[str] = None
    """
    Path to client certificate
    """

    def load_umd_map(self, location_name: str, location_version: str) -> schema.UniversalMap:
        """
        Load Umd map using the proper context information.

        I.e. Cloud workflow uses cloud Umd file and internal dev workflow uses local Umd file.

        Args:
            location_name: Location name
            location_version: Location version. Unused for internal dev workflow

        Returns:
            Umd map
        """
        if self.internal_dev:
            map_file = (
                Path(os.environ.get("PD_ROOT", "")) / "generated" / "locations" / location_name / f"{location_name}.umd"
            )
            if not map_file.is_file():
                raise PdError(
                    f"Couldn't find local map (Umd) for map {location_name} at {str(map_file)}. "
                    "Please download the map artifact."
                )
            return load_umd_map_from_file(path=map_file)
        else:
            try:
                return load_umd_map(name=location_name, version=location_version)
            except PdError as e:
                raise PdError(
                    f"Couldn't load map {location_name} {location_version} from management API. Error: {str(e)}"
                )

    def load_map(self, location_name: str, location_version: str) -> UniversalMap:
        """
        Load map using the proper context information.

        I.e. Cloud workflow uses cloud Umd file and internal dev workflow uses local Umd file.

        Args:
            location_name: Location name
            location_version: Location version. Unused for internal dev workflow

        Returns:
            Map object
        """
        return UniversalMap(proto=self.load_umd_map(location_name, location_version))


def common_step_options(require_sim=False, require_label_engine=False):
    """
    Decorator for click commands that adds common options for Step SDK scripts.

    Use this decorator with a :class:`click.command` to automatically add common Step options
    to the command.
    These options will handle the setup of Step Management API, if the workflow needs it.

    All options added by this decorator are unexposed, meaning they won't show up in the
    command function's arguments.
    Instead, the options are provided to the command function as a kwargs named `step_options` and of type
    :class:`StepScriptContext`.

    Example::

        @click.command()
        @common_step_options()
        @click.option('--test', is_flag=True)
        def cli(test, step_options: StepScriptContext = None)
            print(step_options.ig)

    This decorator additionally accepts parameters to enforce certain behaviors, like forcing
    certain options to be required.

    Args:
        require_sim: Adds an input for Sim name/address
        require_label_engine: Adds an input for Label Engine name/address
    """

    # The following callback function is used to capture the unexposed option values
    def _callback(ctx, param, value):
        ctx.obj = ctx.obj or {}
        ctx.obj["step_option_values"] = ctx.obj.get("step_option_values", {})
        ctx.obj["step_option_values"][param.name] = value

    # The following decorator is used to trigger validation on the options
    # and expose the script-specific context object
    def _step_options_callback_decorator(_func):
        @click.pass_context
        @wraps(_func)
        def _step_options_callback(ctx, *args, **kwargs):
            update_dict = {"step_options": _validate_step_options(ctx.obj["step_option_values"])}
            ctx.params.update(update_dict)
            kwargs.update(update_dict)
            _func(*args, **kwargs)

        return _step_options_callback

    # The following function performs the validation on the step script options
    def _validate_step_options(option_values: Dict[str, str]) -> StepScriptContext:
        ig = option_values.get("ig", None)
        sim = option_values.get("sim", None) if require_sim else None
        label_engine = option_values.get("label_engine", None) if require_label_engine else None
        org = option_values.get("org", None)
        api_key = option_values.get("apikey", None)
        env = option_values.get("env", None)
        client_cert_file = option_values.get("client_cert_file", None)
        if is_server_url(ig):
            internal_dev = True
            if sim and not is_server_url(sim):
                raise ValueError("Since --ig is a url, --sim must also be a url as well.")
            if label_engine and not is_server_url(label_engine):
                raise ValueError("Since --ig is a url, --label-engine must also be a url as well.")
            local_asset_registry_path = Path(os.environ.get("PD_ROOT", "")) / "assets" / "asset_registry.db"
            if not local_asset_registry_path.is_file():
                raise PdError(
                    f"Couldn't find asset registry at {str(local_asset_registry_path)}. "
                    "Please make sure env var PD_ROOT is set and asset registry exists at "
                    "$PD_ROOT/assets/asset_registry.db"
                )
            init_asset_registry_file(local_asset_registry_path)
            ig_version = None
        else:
            internal_dev = False
            if sim and sim != ig:
                raise ValueError("Since --ig is a cloud instance name, --sim must be the same instance name.")
            if label_engine and label_engine != ig:
                raise ValueError("Since --ig is a cloud instance name, --label-engine must be the same instance name.")
            if not org:
                raise ValueError("--org is required when connecting to a named Ig server")
            if not api_key:
                raise ValueError("--apikey is required when connecting to a named Ig server")
            pd.management.org = org
            pd.management.api_key = api_key
            if env:
                api_urls = {
                    "prod": pd.management._API_URL_PROD,
                    "stage": pd.management._API_URL_STAGE,
                    "dev": pd.management._API_URL_DEV,
                }
                pd.management.api_url = api_urls[env]
            try:
                ig_instance = Ig.read(ig)
                ig_version = ig_instance.ig_version
                ig = ig_instance.ig_url
                sim = ig_instance.sim_url
                if label_engine:
                    label_engine = ig_instance.le_url
            except HTTPError:
                raise ValueError(f"Couldn't find an Ig by the name '{ig}'. Please check the value passed in '--ig'")
            init_asset_registry_version(ig_version)

        return StepScriptContext(
            internal_dev=internal_dev,
            ig=ig,
            sim=sim,
            label_engine=label_engine,
            org=org,
            api_key=api_key,
            ig_version=ig_version,
            client_cert_file=client_cert_file,
        )

    unexposed_option = partial(click.option, expose_value=False, callback=_callback)
    _common_step_options = [
        unexposed_option(
            "--ig",
            default="tcp://127.0.0.1:9000",
            help="Name of the IG server or address of IG server's url",
            show_default=True,
        ),
        unexposed_option(
            "--client-cert-file",
            help="Path to .pem certificate file",
            type=click.Path(exists=True),
            envvar="PD_CLIENT_CREDENTIALS_PATH_ENV",
        ),
        unexposed_option(
            "--org", help="Step Management org name. Required with named IG server.", envvar="PD_CLIENT_ORG_ENV"
        ),
        unexposed_option(
            "--apikey",
            help="Step Management API key. Required with named IG server.",
            envvar="PD_CLIENT_STEP_API_KEY_ENV",
        ),
        unexposed_option("--env", help="Step Environment", type=click.Choice(["prod", "stage", "dev"])),
    ]
    if require_sim:
        _common_step_options.append(
            unexposed_option("--sim", help="Name of the Sim server or address of Sim server's url", show_default=True)
        )
    if require_label_engine:
        _common_step_options.append(
            unexposed_option(
                "--label-engine",
                help="Name of the Label Engine server or address of Label Engine server's url",
                show_default=True,
            )
        )

    def inner_decorator(func):
        for option in reversed(_common_step_options):
            func = option(func)
        func = _step_options_callback_decorator(func)
        return func

    return inner_decorator
