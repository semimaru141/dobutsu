from typing import Any, Dict, List
import numpy as np

from src.consts.domain import *
from src.domains.abstract.state import State
from src.domains.model.model import Model
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.const import TrainDataDic


class TrainDataModelFactory():
    _data: Dict[Key, List[Score]]

    def __init__(self, model: Model) -> None:
        self._data = {}
        self.model = model

    def data_add(self, state: State, score: Score) -> None:
        key = state.get_unique_key()
        if key in self._data:
            self._data[key].append(score)
        else:
            self._data[key] = [score]

    def pick_state(self, states: List[State]) -> State:
        scores = [self.model.search_score(state.get_unique_key()) for state in states]
        probabilities = self._calc_probabilities(scores)
        selected_state = np.random.choice(states, p=probabilities)
        return selected_state
    
    def _calc_probabilities(self, scores: List[Score]) -> np.ndarray:
        # softmax関数で算出
        exp_scores = np.exp(scores)
        return exp_scores / np.sum(exp_scores)

    def create(self) -> TrainData:
        ret: TrainDataDic = {}
        for key, value in self._data.items():
            length = len(value)
            ret[key] = (sum(value) / length, length)
        return TrainData(ret)
