# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
from abc import abstractmethod
from typing import Optional, Tuple

from pd.session import SimSession
from pd.state import State

from pd.data_lab.context import get_datalab_context
from pd.data_lab.config.location import Location
from pd.management import Ig
from pd.core import PdError

logger = logging.getLogger(__name__)


class AbstractSimulationInstance(abc.ABC):
    @abc.abstractmethod
    def __enter__(self) -> SimSession:
        pass

    @abc.abstractmethod
    def __exit__(self):
        pass

    @property
    @abstractmethod
    def session(self) -> SimSession:
        ...

    def load_scenario_generation(self, scenario_gen: str) -> Tuple[Location, int]:
        loc_name, ego_id = self.session.load_scenario_generation(scenario_gen=scenario_gen)
        return Location(name=loc_name), ego_id

    def query_sim_state(self) -> State:
        sim_state = self.session.query_state_data()
        return sim_state


class SimulationInstance(AbstractSimulationInstance):
    def __init__(
        self,
        address: Optional[str] = None,
    ):
        super().__init__()
        self._address = address
        context = get_datalab_context()
        self._client_cert_file = context.client_cert_file
        self._temporal_session_reference = None

        self._session: Optional[SimSession] = None

        if not context.is_mode_local and context.fail_on_version_mismatch:
            try:
                ig_version = next(ig.ig_version for ig in Ig.list() if ig.sim_url == address)
            except StopIteration:
                raise PdError(f"Couldn't find a sim instance with the address '{address}'. "
                              "Please verify the sim instance address.")
            if ig_version != context.version:
                raise PdError(f"There's a mismatch between the selected Data Lab version ({context.version}) "
                              f"and the version of the sim instance ({ig_version}). "
                              "To disable this check, pass fail_on_version_mismatch=False to setup_datalab().")

    @property
    def session(self) -> SimSession:
        return self._session

    def create_session(self):
        if self._session is None:
            self._session = SimSession(request_addr=self._address, client_cert_file=self._client_cert_file)
            self._session.transport.timeout_recv_ms = 600_000
            self._session.__enter__()
            logger.info("Started Sim Session.")
        return self._session

    def end_session(self):
        if self._session is not None:
            self._session.__exit__()
            self._session = None
            logger.info("Ended Sim Session!")

    def __enter__(self) -> SimSession:
        return self.create_session()

    def __exit__(self, *args):
        self.end_session()


class ManagedSimulationInstance(SimulationInstance):
    pass
