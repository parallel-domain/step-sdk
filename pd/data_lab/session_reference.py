# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.

from typing import Optional, List, Union

from pd.data_lab.labeled_state_reference import StateReference
from pd.session import StepSession
from pd.state import State, CameraSensor, LiDARSensor


class TemporalSessionReference(StateReference):
    def __init__(
        self,
        session: StepSession,
        state: State,
        frame_id: str,
        sensor_rig: List[Union[CameraSensor, LiDARSensor]],
        ego_agent_id: int,
    ):
        super().__init__(state=state, frame_id=frame_id, ego_agent_id=ego_agent_id)
        self._session = session
        self.sensor_rig = sensor_rig

    @property
    def session(self) -> Optional[StepSession]:
        return self._session

    def on_session_state_changed(self):
        self._session = None
