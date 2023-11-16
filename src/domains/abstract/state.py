from abc import ABC, abstractmethod
from typing import List, Type

from src.consts.domain import *

class State(ABC):
    @abstractmethod
    def get_next_states(self) -> List[Type['State']]:
        pass

    @abstractmethod
    def get_all_possible_states(self) -> List[Type['State']]:
        pass

    @abstractmethod
    def get_unique_key(self) -> Key:
        pass

    @abstractmethod
    def get_finish(self) -> Finish:
        pass
