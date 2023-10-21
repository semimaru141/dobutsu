import numpy as np
from typing import Dict, List, Tuple
from src.consts.domain import Key, Score, SelectionProbability
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State

class PickStateRandomlyStrategy(PickStateStrategy):
    def pick_state(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> State:
        return np.random.choice(next_states)
    
    def pick_state_verbose(self, original_state: State, next_states: List[State], data: Dict[Key, List[Score]]) -> Tuple[State, Score, SelectionProbability]:
        return np.random.choice(next_states), 0, 1 / len(next_states)
    
    def get_all_verbose(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> List[Tuple[State, Score, SelectionProbability]]:
        return [(state, 0, 1 / len(next_states)) for state in next_states]
