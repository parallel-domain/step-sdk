# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

import abc
import logging
import os
from abc import abstractmethod
from typing import Optional, Tuple

from pd.session import SimSession
from pd.state import State, bytes_to_state

from pd.data_lab.config.location import Location
from pd.data_lab.constants import PD_CLIENT_CREDENTIALS_PATH_ENV

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
        state_data = self.session.query_state_data()
        sim_state = bytes_to_state(state_data)
        return sim_state


class SimulationInstance(AbstractSimulationInstance):
    def __init__(
        self,
        address: Optional[str] = None,
    ):
        super().__init__()
        self._address = address
        self._client_cert_file = os.environ.get(PD_CLIENT_CREDENTIALS_PATH_ENV, None)
        self._temporal_session_reference = None

        self._session: Optional[SimSession] = None

    @property
    def session(self) -> SimSession:
        return self._session

    def create_session(self):
        if self._session is None:
            self._session = SimSession(request_addr=self._address, client_cert_file=self._client_cert_file)
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
