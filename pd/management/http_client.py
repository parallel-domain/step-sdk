# Copyright (c) 2022 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

"""
Client for making HTTP requests
"""
import threading

import requests

import pd.management
from pd.core import PdError

http_client_instance = None


class HTTPClient:
    def __init__(self):
        self._thread_local = threading.local()

    def _session(self) -> requests.Session:
        if getattr(self._thread_local, "session", None) is None:
            if not pd.management.api_key and not (pd.management.username and pd.management.password):
                if pd.management.username or pd.management.password:
                    raise PdError("Both username and password are required for Step Management API")
                raise PdError(
                    "An API Key is required for accessing Step Management API. E.g.: pd.management.api_key='<api key>'"
                )
            self._thread_local.session = requests.Session()
            if pd.management.api_key:
                self._thread_local.session.headers.update({"X-API-Key": pd.management.api_key})
            else:
                self._thread_local.session.auth = (pd.management.username, pd.management.password)
        return self._thread_local.session

    def request(self, method, url, params=None, data=None, raw_response=False):
        if not pd.management.org:
            raise PdError(
                "An Org name is required for accessing Step Management API. E.g.: pd.management.org='<my org>'"
            )
        session = self._session()
        url = pd.management.api_url + f"/{pd.management.org}/{url}"
        response = session.request(method, url, params=params, json=data)
        response.raise_for_status()
        if raw_response:
            content = response.content
        elif method == "delete":
            content = response.content.decode()
        else:
            content = response.json()
        status_code = response.status_code
        return status_code, content


def get_http_client() -> HTTPClient:
    """
    Returns a singleton copy of HTTPClient
    """
    global http_client_instance
    if not http_client_instance:
        http_client_instance = HTTPClient()
    return http_client_instance
