# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
from typing import Optional

from pd.core import PdError
from pd.data_lab.config.location import Location
from pd.data_lab.context import get_datalab_context, validate_instance_address
from pd.data_lab.scenario import Lighting
from pd.management.ig import Ig
from pd.session import StepSession
from pd.state import State

logger = logging.getLogger(__name__)


class RenderInstance:
    def __init__(
        self,
        name: Optional[str] = None,
        address: Optional[str] = None,
    ):
        """
        Create a render instance for an existing remote IG server

        Args:
            name: Instance name. Required for cloud mode
            address: Instance address. Used in local mode
        """

        self.session: Optional[StepSession] = None
        self._location_is_set: bool = False
        self._loaded_location: Optional[Location] = None
        self._loaded_lighting: Optional[str] = None
        self.address = address
        self.name = name
        self._client_cert_file = None

    def load_environment(self, location: Location, lighting: Lighting, unique_scene_name: str):
        if self.session is not None:
            logger.info(f"Renderer loading location {location.name} with lighting: {lighting}")
            if (
                self._loaded_location is None
                or self._loaded_location.name != location.name
                or self._loaded_location.version != location.version
                or self._loaded_lighting != lighting
            ):
                # For merge batches we don't want to reload an already loaded map
                self.session.load_location(
                    location_name=location.name, time_of_day=lighting, scene_name=unique_scene_name
                )
            self._location_is_set = True
            self._loaded_location = location
            self._loaded_lighting = lighting
            logger.info(f"Renderer loaded location")
        else:
            logger.warning("No active render session! Wont update location.")

    @property
    def location_is_set(self) -> bool:
        return self._location_is_set

    def update_state(self, sim_state: State) -> None:
        if self.session is None:
            raise ValueError("Need to create session before calling update_state!")
        self.session.update_state(state=sim_state)

    @property
    def loaded_location(self) -> Optional[Location]:
        return self._loaded_location

    def create_session(self):
        if self.session is None:
            self.session = StepSession(request_addr=self.address, client_cert_file=self._client_cert_file)
            self.session.transport.timeout_recv_ms = 600_000
            self.session.__enter__()
            logger.info(f"Created render session")
        return self.session

    def end_session(self):
        if self.session is not None:
            self.session.__exit__()
            self.session = None
            self._temporal_session_reference = None
            self._location_is_set = False
            self._loaded_location = None
            self._loaded_lighting = None
            logger.info("Ended render session!")

    def setup(self, unique_scene_name: str, location: Location, lighting: Lighting):
        self.address, self.name, self._client_cert_file = validate_instance_address(
            instance_type="ig", address=self.address, name=self.name
        )
        self.create_session()
        self.load_environment(location=location, lighting=lighting, unique_scene_name=unique_scene_name)

    def cleanup(self):
        self.end_session()
