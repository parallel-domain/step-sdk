# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from datetime import datetime
from typing import Optional

from pd.session import StepSession
from pd.state import State


class TemporalSessionReference:
    def __init__(self, session: StepSession, state: State, date_time: datetime):
        self._session = session
        self._state = state
        self.date_time = date_time

    @property
    def session(self) -> Optional[StepSession]:
        return self._session

    @property
    def state(self) -> Optional[State]:
        return self._state

    def on_session_state_changed(self):
        self._session = None
