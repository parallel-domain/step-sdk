# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Utilities for scripting, such as handling common inputs.
"""

from functools import partial, wraps
from dataclasses import dataclass
from typing import Optional, Dict
from pathlib import Path
from requests import HTTPError

import click

from pd.session import is_server_url
import pd.management
from pd.management import Ig
from pd.assets import init_asset_registry_version, init_asset_registry_file, get_asset_registry_path


@dataclass
class StepScriptContext:
    internal_dev: bool
    """
    Indicates an internal dev workflow
    In internal dev workflow, Step Management API is not used.
    Addresses for any instances (Sim, IG, etc) must be explicitly provided.
    Path to all related artifacts (Umd, Asset Registry) must be explicitly provided. 
    """

    ig: str
    """
    Ig name, when :attr:`internal_dev` is :obj:`False`
    Address for Ig instance, when :attr:`internal_dev` is :obj:`True`
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

    asset_registry_path: Optional[Path] = None
    """
    Path to asset registry being used, if any.
    Always set when :attr:`internal_dev` is :obj:`False`.
    May not be set when :attr:`internal_dev` is :obj:`True`, 
    depending on if the script requires this path.
    """

    umd_path: Optional[Path] = None
    """
    Path to asset Umd file, if requested.
    Only valid when :attr:`internal_dev` is :obj:`True` (use :func:`load_umd_map` otherwise)
    """


def common_step_options(require_asset_registry=False, require_umd_path=False):
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

    This decorator additionally accepts parameters to enforce certain behaviours, like forcing
    certain options to be required.

    Args:
        require_asset_registry: Force asset registry path to be required (for internal dev workflow)
        require_umd_path: Force umd path to be required (for internal dev workflow)
    """
    # The following callback function is used to capture the unexposed option values
    def _callback(ctx, param, value):
        ctx.obj = ctx.obj or {}
        ctx.obj['step_option_values'] = ctx.obj.get('step_option_values', {})
        ctx.obj['step_option_values'][param.name] = value

    # The following decorator is used to trigger validation on the options
    # and expose the script-specific context object
    def _step_options_callback_decorator(_func):
        @click.pass_context
        @wraps(_func)
        def _step_options_callback(ctx, *args, **kwargs):
            update_dict = {'step_options': _validate_step_options(ctx.obj['step_option_values'])}
            ctx.params.update(update_dict)
            kwargs.update(update_dict)
            _func(*args, **kwargs)
        return _step_options_callback

    # The following function performs the validation on the step script options
    def _validate_step_options(option_values: Dict[str, str]) -> StepScriptContext:
        ig = option_values.get('ig', None)
        org = option_values.get('org', None)
        api_key = option_values.get('apikey', None)
        client_cert_file = option_values.get('client_cert_file', None)
        asset_registry = option_values.get('asset_registry', None)
        umd = option_values.get('umd', None)
        umd_path = None
        if is_server_url(ig):
            internal_dev = True
            if org:
                raise ValueError(
                    f"--org is not needed when using an Ig server address. "
                    f"Please remove it."
                )
            if api_key:
                raise ValueError(
                    f"--apikey is not needed when using an Ig server address. "
                    f"Please remove it."
                )
            if asset_registry:
                asset_registry_path = Path(asset_registry)
                init_asset_registry_file(asset_registry_path)
            elif require_asset_registry:
                raise ValueError(
                    f"--asset-registry parameter is required"
                )
            else:
                asset_registry_path = None
            if umd:
                umd_path = Path(umd)
            elif require_umd_path:
                raise ValueError(
                    f"--umd parameter is required"
                )
            ig_version = None
        else:
            internal_dev = False
            if not org:
                raise ValueError(
                    f"--org is required when connecting to a named Ig server"
                )
            if not api_key:
                raise ValueError(
                    f"--apikey is required when connecting to a named Ig server"
                )
            if asset_registry:
                raise ValueError(
                    f"--asset-registry is not needed when connecting to a named Ig server. "
                    f"Please remove it."
                )
            if umd:
                raise ValueError(
                    f"--umd is not needed when connecting to a named Ig server. "
                    f"Please remove it."
                )
            pd.management.org = org
            pd.management.api_key = api_key
            try:
                ig_instance = Ig.read(ig)
                ig_version = ig_instance.ig_version
                ig = ig_instance.ig_url
            except HTTPError:
                raise ValueError(
                    f"Couldn't find an Ig by the name '{ig}'. Please check the value passed in '--ig'"
                )
            init_asset_registry_version(ig_version)
            asset_registry_path = get_asset_registry_path()

        return StepScriptContext(
            internal_dev=internal_dev,
            ig=ig,
            org=org,
            api_key=api_key,
            ig_version=ig_version,
            client_cert_file=client_cert_file,
            asset_registry_path=asset_registry_path,
            umd_path=umd_path
        )

    unexposed_option = partial(click.option, expose_value=False, callback=_callback)
    _common_step_options = [
        unexposed_option(
            '--ig',
            default='tcp://127.0.0.1:9000',
            help="Name of the IG server or address of IG server's url",
            show_default=True,
            required=True
        ),
        unexposed_option('--client-cert-file', help="Path to .pem certificate file", type=click.Path(exists=True)),
        unexposed_option('--org', help="Step Management org name. Required with named IG server."),
        unexposed_option('--apikey', help="Step Management API key. Required with named IG server."),
    ]
    if require_asset_registry:
        _common_step_options += [
            unexposed_option(
                '--asset-registry',
                help="Path to asset registry. Required with IG url.",
                type=click.Path(exists=True)
            )
        ]
    if require_umd_path:
        _common_step_options += [
            unexposed_option(
                '--umd',
                help="Path to Umd file. Required with IG url.",
                type=click.Path(exists=True)
            )
        ]

    def inner_decorator(func):
        for option in reversed(_common_step_options):
            func = option(func)
        func = _step_options_callback_decorator(func)
        return func
    return inner_decorator
