from abc import ABC, abstractmethod
from typing import List, Type

from consts.domain import *

class State(ABC):
    @abstractmethod
    def get_next_states(self) -> List[Type['State']]:
        pass

    @abstractmethod
    def get_unique_key(self) -> Key:
        pass

    @abstractmethod
    def get_finish(self) -> Finish:
        pass
