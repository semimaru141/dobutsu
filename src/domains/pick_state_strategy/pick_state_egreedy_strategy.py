import numpy as np
from typing import Dict, List, Tuple
from src.consts.domain import *
from src.domains.abstract.evaluator import Evaluator
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State

DataDict = Dict[Key, List[Score]]

# ε-greedy法による選択を行う
class PickStateEgreedyStrategy(PickStateStrategy):
    def __init__(self, evaluator: Evaluator, use_ucb: bool = True) -> None:
        self.evaluator = evaluator
        self.use_ucb = use_ucb
        self.epsilon = GREEDY_EPSILON

    def set_epsilon(self, epsilon: float):
        self.epsilon = epsilon

    def pick_state(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> State:
        scores = [self._evaluate(state) for state in next_states]
        use_random = self.use_random()
        if use_random:
            return np.random.choice(next_states)
        max_score = min(scores)
        for i, score in enumerate(scores):
            if score == max_score:
                return next_states[i]
        raise 'state not found error'
    
    def pick_state_verbose(self, original_state: State, next_states: List[State], data: Dict[Key, List[Score]]) -> Tuple[State, Score, SelectionProbability]:
        scores = [self._evaluate(state) for state in next_states]
        use_random = self.use_random()
        if use_random:
            return np.random.choice(next_states), score, 1 / len(next_states)
        max_score = min(scores)
        for i, score in enumerate(scores):
            if score == max_score:
                return next_states[i], score, 1
        raise 'state not found error'

    def get_all_verbose(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> List[Tuple[State, Score, SelectionProbability]]:
        scores = [self._evaluate(state) for state in next_states]
        use_random = self.use_random()
        if use_random:
            return [(state, score, 1 / len(next_states)) for state, score in zip(next_states, scores)]
        max_score = min(scores)
        probabilities = [1 if score == max_score else 0 for score in scores]
        return zip(next_states, scores, probabilities)
    
    def use_random(self) -> bool:
        return np.random.rand() <= self.epsilon
    
    def _evaluate(self, key: Key) -> Score:
        return self.evaluator.search_score(key)
