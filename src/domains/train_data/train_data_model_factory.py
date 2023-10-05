from typing import Dict, List
import numpy as np

from src.consts.domain import *
from src.domains.abstract.state import State
from src.domains.model.model import Model
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.const import AppearanceCount, TrainDataDic

class TrainDataModelFactory():
    _data: Dict[Key, List[Score]]

    def __init__(self, model_evaluator: ModelEvaluator) -> None:
        self._data = {}
        self.model_evaluator = model_evaluator

    def data_add(self, state: State, score: Score) -> None:
        key = state.get_unique_key()
        if key in self._data:
            self._data[key].append(score)
        else:
            self._data[key] = [score]

    def pick_state(self, original_state: State, nexts_states: List[State]) -> State:
        scores = self._calc_score(original_state, nexts_states)
        probabilities = self._calc_probabilities(scores)
        selected_state = np.random.choice(nexts_states, p=probabilities)
        return selected_state
    
    # UCBによる補正を加えたスコアを算出
    def _calc_score(self, original_state: State, states: List[State]) -> Score:
        keys = np.array([state.get_unique_key() for state in states])
        get_appearance_count = np.vectorize(self._get_apearance_count)
        search_score = np.vectorize(self.model_evaluator.search_score)

        # モデルによる評価に、UCBによる補正を加える
        # UCB = 定数 * sqrt(log(親ノードの出現回数) / 子ノードの出現回数)
        original_log = np.log(self._get_apearance_count(original_state.get_unique_key()))
        counts = get_appearance_count(keys)
        ucb = UCB_COEFFICIENT * np.sqrt(original_log / counts)
        scores = search_score(keys) * -1.0 + ucb
        
        return scores
    
    # その局面が出現した回数を返す
    def _get_apearance_count(self, key: Key) -> AppearanceCount:
        found = self._data.get(key)
        if found == None:
            return 0
        else:
            return len(found)
    
    # スコアから選出される確率を算出
    def _calc_probabilities(self, scores: List[Score]) -> np.ndarray:
        # softmax関数で算出
        exp_scores = np.exp(np.array(scores) * SOFTMAX_TEMPERATURE)
        return exp_scores / np.sum(exp_scores)

    def create(self) -> TrainData:
        ret: TrainDataDic = {}
        for key, value in self._data.items():
            length = len(value)
            ret[key] = (sum(value) / length, length)
        return TrainData(ret)
