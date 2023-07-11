# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
import os
from datetime import datetime
from time import sleep
from typing import List, Literal, Optional

import pd.state
from pd.core import PdError
from pd.data_lab.sim_state import SimState
from pd.management.ig import Ig, IgQuality, IgStatus
from pd.session import StepSession

from pd.data_lab.config.location import Location
from pd.data_lab.context import get_datalab_context
from pd.data_lab.session_reference import TemporalSessionReference

logger = logging.getLogger(__name__)


class AbstractRenderInstance(abc.ABC):
    def __init__(self):
        super().__init__()

        self._temporal_session_reference = None

        self.session: Optional[StepSession] = None
        self._location_is_set: bool = False
        self._loaded_location: Optional[Location] = None
        self._loaded_time_of_day: Optional[str] = None

    @abc.abstractmethod
    def __enter__(self) -> StepSession:
        pass

    @abc.abstractmethod
    def __exit__(self):
        pass

    @property
    @abc.abstractmethod
    def loaded_location(self) -> Optional[Location]:
        pass

    def load_environment(self, location: Location, time_of_day: str):
        if self.session is not None:
            logger.info(f"Start loading location {location.name} with time of day: {time_of_day}")
            if (
                self._loaded_location is None
                or self._loaded_location.name != location.name
                or self._loaded_location.version != location.version
                or self._loaded_time_of_day != time_of_day
            ):
                # For merge batches we don't want to reload an already loaded map
                self.session.load_location(location_name=location.name, time_of_day=time_of_day)
            self._location_is_set = True
            self._loaded_location = location
            self._loaded_time_of_day = time_of_day
            logger.info(f"Loaded location {location.name} with time of day: {time_of_day}")
        else:
            logger.warning("No active session! Wont update location.")

    @property
    def location_is_set(self) -> bool:
        return self._location_is_set

    @property
    def temporal_session_reference(self) -> Optional[TemporalSessionReference]:
        return self._temporal_session_reference


    def render_frame(self, sim_state: SimState) -> TemporalSessionReference:
        if self.session is not None:

            # invalidate previous frame session ref
            if self._temporal_session_reference is not None:
                self._temporal_session_reference.on_session_state_changed()

            # step_state.simulation_time_sec += time_delta
            self.session.update_state(state=sim_state.current_state)

            # create new frames session ref
            self._temporal_session_reference = TemporalSessionReference(
                session=self.session,
                state=sim_state.current_state,
                date_time=sim_state.current_sim_date_time,
            )
        return self.temporal_session_reference

    @property
    def loaded_location(self) -> Optional[Location]:
        return self._loaded_location


class ManagedRenderInstance(AbstractRenderInstance):
    def __init__(
        self,
        locations: List[Location] = None,
        ig_version: Optional[str] = None,
        address: Optional[str] = None,
        time_to_live: Optional[int] = None,
        quality: Literal["high", "low"] = "high",
        keep_instance_running: bool = False,
    ):
        super().__init__()

        context = get_datalab_context()
        if context.is_mode_local:
            raise PdError(
                "ManagedRenderInstance does not support local mode in Data Lab. "
                "Please specify cloud credentials to use a ManagedRenderInstance."
            )
        self._client_cert_file = context.client_cert_file
        self._ig_version = context.version
        self._time_to_live = time_to_live
        self._quality = IgQuality(quality)
        self._keep_instance_running = keep_instance_running or (address is not None)
        self.locations = locations

        self._ig: Optional[Ig] = None
        self._address = address

    def get_status(self) -> Optional[IgStatus]:
        if self._ig is not None:
            self._ig = Ig.read(name=self._ig.name)
            return self._ig.status
        return None

    def start_instance(self):
        if self._ig is None:
            # logger.info(f"No locations where passed so {self.locations} where randomly picked")
            if self._address is None:
                if self.locations is None:
                    raise ValueError(
                        "No locations have been passed to the Render Instance! "
                        "Those need to be known if you want ot start an instance!"
                    )

                logger.info(f"Using locations: {self.locations}")
                logger.info(f"Using IG version {self._ig_version}")
                # Start new instance
                self._ig = Ig.create(
                    ig_version=self._ig_version,
                    quality=self._quality,
                    levelpaks={ll.name: ll.version for ll in self.locations},
                    ttl=self._time_to_live,
                )

                self._wait_until_instance_started()
            else:
                # use running instance if credentials are set to check if its actually running
                # otherwise we just assume the url is correct as requested for better user experience
                igs = Ig.list()
                ig = next(iter([i for i in igs if i.step_url == self._address]), None)
                if ig is None:
                    raise ValueError(f"The step instance {self._address} is not running anymore!")
                self._ig = ig

    def _wait_until_instance_started(self, max_wait_time: int = 1800):
        started = False
        tries = 0
        wait_time = 0
        status = IgStatus.Starting
        status_changed = False
        while not started:
            tries += 1
            try:
                current_status = self.get_status()
                status_changed = status != current_status
                status = current_status
                started = status == IgStatus.Running
            except Exception as e:
                logger.exception(e)
            if not started:
                logger.info(f"Waiting for instance {self._ig.self_url} to start.. {status.name}")
                wait_for = min(30, 5 * tries)
                if status_changed:
                    wait_for = 0
                    status_changed = False
                sleep(wait_for)
                wait_time += wait_time

            if wait_time >= max_wait_time:
                raise ConnectionError(
                    f"Instance {self._ig.self_url} seems to have problems starting up! "
                    f"Please consult with the PD Step team!"
                )
        # sleep(10)
        logger.info(f"Instance {self._ig.self_url} is running")

    def stop_instance(self):
        if self._ig is not None:
            Ig.delete(name=self._ig.name)
            ig = next(iter([i for i in Ig.list() if i.step_url == self._ig.step_url]), None)
            if ig is None:
                logger.info("Successfully shut down step instance")
                self._ig = None
            else:
                logger.error(f"Step instance could not be shut down. Please shut {self._ig.step_url} down manually!")
        else:
            logger.info("Step instance could not be shut down because it does not exist (anymore)")

    def create_session(self):
        if self.session is None:
            if self._ig is None:
                if self._address is not None:
                    self.session = StepSession(request_addr=self._address, client_cert_file=self._client_cert_file)
                else:
                    raise RuntimeError("You need to start an instance before you can create a session!")
            else:
                self.session = StepSession(request_addr=self._ig.step_url, client_cert_file=self._client_cert_file)
            self.session.transport.timeout_recv_ms = 600_000
            self.session.__enter__()
            version = self.session.system_info.version
            logger.info(
                f"Started Session with Server version: {version.major}.{version.minor}.{version.patch}-{version.build}"
            )
        return self.session

    def end_session(self):
        if self.session is not None:
            self.session.__exit__()
            self.session = None
            self._temporal_session_reference = None
            self._location_is_set = False
            logger.info("Ended Render Session!")

    def __enter__(self) -> StepSession:
        self.start_instance()
        return self.create_session()

    def __exit__(self):
        try:
            self.end_session()
        except Exception as e:
            raise e
        finally:
            if not self._keep_instance_running:
                self.stop_instance()


class RenderInstance(AbstractRenderInstance):
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
        super().__init__()
        self._address = address
        context = get_datalab_context()
        self._client_cert_file = context.client_cert_file

        if name and address:
            raise PdError("Only one of 'name' or 'address' can be specified for RenderInstance.")
        if not context.is_mode_local and not name:
            raise PdError("A 'name' is required in RenderInstance when running in cloud mode.")

        if context.is_mode_local:
            # Local mode, use local address if none is provided
            self._address = self._address or "tcp://localhost:9000"
        else:
            # Cloud mode, resolve the address
            try:
                ig = next(ig for ig in Ig.list() if ig.name == name)
            except StopIteration:
                raise PdError(
                    f"Couldn't find a render instance with the name '{name}'. "
                    "Please verify that the name is correct."
                )
            if context.fail_on_version_mismatch:
                if ig.ig_version != context.version:
                    raise PdError(
                        f"There's a mismatch between the selected Data Lab version ({context.version}) "
                        f"and the version of the render instance ({ig.ig_version}). "
                        "To disable this check, pass fail_on_version_mismatch=False to setup_datalab()."
                    )
            self._address = ig.ig_url

    def create_session(self):
        if self.session is None:
            self.session = StepSession(request_addr=self._address, client_cert_file=self._client_cert_file)
            self.session.transport.timeout_recv_ms = 600_000
            self.session.__enter__()
            version = self.session.system_info.version
            logger.info(
                f"Started Session with Server version: {version.major}.{version.minor}.{version.patch}-{version.build}"
            )
        return self.session

    def end_session(self):
        if self.session is not None:
            self.session.__exit__()
            self.session = None
            self._temporal_session_reference = None
            self._location_is_set = False
            self._loaded_location = None
            self._loaded_time_of_day = None
            logger.info("Ended Render Session!")

    def __enter__(self) -> StepSession:
        return self.create_session()

    def __exit__(self, *args):
        self.end_session()
