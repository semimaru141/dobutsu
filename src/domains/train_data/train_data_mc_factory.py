from typing import Dict, List

from consts.domain import *
from domains.abstract.state import State
from domains.train_data.train_data import TrainData
from domains.train_data.const import TrainDataDic


class TrainDataMCFactory():
    _data: Dict[Key, List[Score]]

    def __init__(self) -> None:
        self._data = {}

    def data_add(self, state: State, score: Score) -> None:
        key = state.get_unique_key()
        if key in self._data:
            self._data[key].append(score)
        else:
            self._data[key] = [score]

    def create(self) -> TrainData:
        ret: TrainDataDic = {}
        for key, value in self._data.items():
            length = len(value)
            ret[key] = (sum(value) / length, length)
        return TrainData(ret)
