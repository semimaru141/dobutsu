from typing import List
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.const import TrainDataDic

class TrainDataMergeFactory:
    def __init__(self, train_datas: List[TrainData]) -> None:
        self.train_datas = train_datas

    def create(self) -> TrainData:
        data: TrainDataDic = {}
        for train_data in self.train_datas:
            for key, value in train_data.dict.items():
                if key in data:
                    appearance_count = data[key][1] + value[1]
                    score = (data[key][0] * data[key][1] + value[0] * value[1]) / appearance_count
                    data[key] = [score, appearance_count]
                else: data[key] = value
        return TrainData(data)
