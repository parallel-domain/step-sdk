# Copyright (c) 2023 Parallel Domain, Inc.
# All rights reserved.
#
# Use of this file is only permitted if you have entered into a
# separate written license agreement with Parallel Domain, Inc.
import abc
from typing import TypeVar

from pd.data_lab.sim_state import SimState

TSimState = TypeVar("TSimState", bound=SimState)


class StateCallback:
    @abc.abstractmethod
    def __call__(self, sim_state: TSimState):
        pass

    @abc.abstractmethod
    def clone(self) -> "StateCallback":
        pass
