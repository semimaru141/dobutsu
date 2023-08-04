from typing import List
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.const import TrainDataDic
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

class TrainDataMergeFactory:
    def __init__(self) -> None:
        self.data: TrainDataDic = {}

    def merge(self, filenames: List[str]) -> None:
        for filename in filenames:
            self._append(filename)

    def _append(self, filename: str) -> None:
        train_data = TrainDataFileFactory(filename).create()
        for key, value in train_data.dict.items():
            if key in self.data:
                appearance_count = self.data[key][1] + value[1]
                score = (self.data[key][0] * self.data[key][1] + value[0] * value[1]) / appearance_count
                self.data[key] = [score, appearance_count]
            else: self.data[key] = value

    def create(self) -> TrainData:
        return TrainData(self.data)
