from typing import Dict, List

from src.consts.domain import *
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.const import TrainDataDic

class TrainDataStrategyFactory():
    _data: Dict[Key, List[Score]]

    def __init__(self, strategy: PickStateStrategy) -> None:
        self._data = {}
        self.strategy = strategy

    def data_add(self, state: State, score: Score) -> None:
        key = state.get_unique_key()
        if key in self._data:
            self._data[key].append(score)
        else:
            self._data[key] = [score]

    def pick_state(self, original_state: State, next_states: List[State]) -> State:
        return self.strategy.pick_state(original_state, next_states, self._data)

    def create(self) -> TrainData:
        ret: TrainDataDic = {}
        for key, value in self._data.items():
            length = len(value)
            ret[key] = (sum(value) / length, length)
        return TrainData(ret)
