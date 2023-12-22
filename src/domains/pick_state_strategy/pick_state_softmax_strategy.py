import numpy as np
from typing import Dict, List, Tuple
from src.consts.domain import *
from src.domains.abstract.evaluator import Evaluator
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State
from src.domains.train_data.const import AppearanceCount

DataDict = Dict[Key, List[Score]]

class PickStateSoftmaxStrategy(PickStateStrategy):
    def __init__(self, evaluator: Evaluator, use_ucb: bool = True) -> None:
        self.evaluator = evaluator
        self.use_ucb = use_ucb
        self.temperature = SOFTMAX_TEMPERATURE

    def set_temperature(self, temperature):
        self.temperature = temperature

    def pick_state(self, original_state: State, next_states: List[State], data: DataDict) -> State:
        scores = self._calc_score(original_state, next_states, data)
        probabilities = self._calc_probabilities(scores)
        selected_state = np.random.choice(next_states, p=probabilities)
        return selected_state
    
    def pick_state_verbose(self, original_state: State, next_states: List[State], data: DataDict) -> Tuple[State, Score, SelectionProbability]:
        scores = self._calc_score(original_state, next_states, data)
        probabilities = self._calc_probabilities(scores)
        selected_state = np.random.choice(next_states, p=probabilities)
        for i, state in enumerate(next_states):
            if selected_state == state:
                probability = probabilities[i]
                score = scores[i]

        return selected_state, score, probability

    def get_all_verbose(self, _original_state: State, next_states: List[State], _data: Dict[Key, List[Score]]) -> List[Tuple[State, Score, SelectionProbability]]:
        scores = [self._search_score(state.get_unique_key()) for state in next_states]
        probabilities = self._calc_probabilities(scores)
        result = sorted(zip(next_states, scores, probabilities), key=lambda x: x[0].get_unique_key())
        return result

    # UCBによる補正を加えたスコアを算出
    def _calc_score(self, original_state: State, states: List[State], data: DataDict) -> Score:
        keys = np.array([state.get_unique_key() for state in states])
        search_score = np.vectorize(lambda key: self._search_score(key))

        if self.use_ucb:
            get_appearance_count = np.vectorize(lambda key: self._get_apearance_count(key, data))

            # モデルによる評価に、UCBによる補正を加える
            # UCB = 定数 * sqrt(log(親ノードの出現回数) / 子ノードの出現回数)
            original_log = np.log(self._get_apearance_count(original_state.get_unique_key(), data))
            counts = get_appearance_count(keys)
            ucb = UCB_COEFFICIENT * np.sqrt(original_log / counts)
        else: 
            ucb = np.zeros(len(states))

        # 後手の盤面のため、評価値が反転している。
        # 後に反転するため、ucbはマイナスにしている
        scores = search_score(keys) - ucb
        return scores
    
    # その局面が出現した回数を返す (現在の探索回数も含むため、+1している)
    def _get_apearance_count(self, key: Key, data: DataDict) -> AppearanceCount:
        found = data.get(key)
        if found == None:
            return 1
        else:
            return len(found) + 1
    
    # スコアから選出される確率を算出
    def _calc_probabilities(self, scores: List[Score]) -> np.ndarray:
        # softmax関数で算出(後手目線のため、評価値を反転している)
        exp_scores = np.exp(-1 * np.array(scores) * self.temperature)
        return exp_scores / np.sum(exp_scores)
    
    def _search_score(self, key: Key) -> Score:
        return self.evaluator.search_score(key)
