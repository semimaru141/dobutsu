from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
from src.consts.domain import *
from src.domains.abstract.state import State

class PickStateStrategy(ABC):
    @abstractmethod
    def pick_state(self, original_state: State, next_states: List[State], data: Dict[Key, List[Score]]) -> State:
        pass

    # 冗長な出力の要請
    @abstractmethod
    def pick_state_verbose(self, original_state: State, next_states: List[State], data: Dict[Key, List[Score]]) -> Tuple[State, Score, SelectionProbability]:
        pass
