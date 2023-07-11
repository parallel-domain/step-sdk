# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Manage the lifecycle of Step instances

This subpackage is a wrapper around the Step Management REST API.
It provides class representations of REST API objects.
Each class supports the CRUD operations relevant to the REST API
object.
For example::

    from pd.management import Ig
    ig = Ig.create(org='myorg')

Additionally, you must provide an **API key** and an **Org name**.
Do this by setting the fields :data:`pd.management.org` and
:data:`pd.management.api_key`.

For example::

    import pd.management
    pd.management.org='<my org>'
    pd.management.api_key='<api key>'

You received the Org name in your onboarding email.
Please visit https://app.paralleldomain.com/settings/api-access to generate an API key.

You can configure the API environment by setting the field :data:`pd.management.api_url`.
For example::

    import pd.management
    pd.management.api_url = pd.management._API_URL_DEV
"""

from .ig import Ig, IgVersion, IgStatus, IgQuality, fetch_ig_asset_registry
from .level import Levelpak, LevelpakVersion, fetch_level_umd
from .sim import SimVersion
from .utils import create_ig_with_retry
from .label_engine import LabelEngineVersion


username = None
"""*Deprecated* use :data:`api_key` instead"""

password = None
"""*Deprecated* use :data:`api_key` instead"""

org = None
"""
Step Management Org Name
"""

api_key = None
"""
Step Management API Key

Please visit https://app.paralleldomain.com/settings/api-access to generate an API key
"""


_API_URL_PROD = 'https://step-api.paralleldomain.com/v1/step'
_API_URL_STAGE = 'https://step-api-stage.paralleldomain.com/v1/step'
_API_URL_DEV = 'https://step-api-dev.paralleldomain.com/v1/step'

api_url = _API_URL_PROD
"""Base url for Step Management API"""
