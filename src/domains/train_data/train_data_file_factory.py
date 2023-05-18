from consts.domains.train_data import *
from domains.train_data.train_data import TrainData


class TrainDataFileFactory():
    def __init__(self, filename) -> None:
        self._read(filename)

    def _read(self, filename: str) -> None:
        pass

    def create(self) -> TrainData:
        ret: TrainDataDic = {}
        for key, value in self._data.items():
            length = len(value)
            ret[key] = (sum(value) / length, length)
        return TrainData(ret)
