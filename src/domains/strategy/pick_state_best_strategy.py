import numpy as np
from typing import Dict, List, Tuple
from src.consts.domain import SOFTMAX_TEMPERATURE, Key, Score, SelectionProbability
from src.domains.abstract.evaluator import Evaluator
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State

# 最善のみ出力してほしい場合
class PickStateBestStrategy(PickStateStrategy):
    def __init__(self, evaluator: Evaluator):
        self.evaluator = evaluator

    def pick_state(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> State:
        scores = [self._evaluate(state) for state in next_states]
        max_score = min(scores)
        for i, score in enumerate(scores):
            if score == max_score:
                return next_states[i]
        raise 'state not found error'
    
    def pick_state_verbose(self, original_state: State, next_states: List[State], data: Dict[Key, List[Score]]) -> Tuple[State, Score, SelectionProbability]:
        scores = [self._evaluate(state) for state in next_states]
        probabilities = self._calc_probabilities(scores)
        max_score = min(scores)
        for i, score in enumerate(scores):
            if score == max_score:
                return next_states[i], score, probabilities[i]
        raise 'state not found error'
    
        # スコアから選出される確率を算出
    def _calc_probabilities(self, scores: List[Score]) -> np.ndarray:
        # softmax関数で算出
        exp_scores = np.exp(-1 * np.array(scores) * SOFTMAX_TEMPERATURE)
        return exp_scores / np.sum(exp_scores)

    def _evaluate(self, state: State) -> Score:
        return self.evaluator.search_score(state.get_unique_key())
