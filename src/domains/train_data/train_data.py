import pickle
from typing import Dict
from src.consts.domain import *
from src.domains.train_data.const import AppearanceCount, TrainDataDic

class TrainData:
    def __init__(self, dict: TrainDataDic):
        self.dict = dict

    def search_score(self, key: Key) -> Score:
        found = self.dict.get(key)
        if found == None:
            return 0
        else:
            return found[0]
    
    def search_appearance_count(self, key: Key) -> AppearanceCount:
        found = self.dict.get(key)
        if found == None:
            return 0
        else:
            return found[1]
    
    def get_size(self) -> int:
        return len(self.dict)

    # このtrain_dataを生成するのに到達した局面数
    def get_predicted_count(self) -> int:
        count = 0
        for value in self.dict.values():
            count += value[1]
        return count
    
    def get_except_one_appearance_size(self) -> int:
        return len([value for value in self.dict.values() if value[1] > 1])
    
    def compress(self) -> 'TrainData':
        ret: TrainDataDic = {}
        for key, value in self.dict.items():
            if value[1] > COMPRESSION_THRESHOLD:
                ret[key] = value
        return TrainData(ret)
    
    # 出現回数の分布を返す
    def show_appearance_distribution(self) -> Dict[AppearanceCount, int]:
        distribution = {}
        for value in self.dict.values():
            if value[1] in distribution:
                distribution[value[1]] += 1
            else:
                distribution[value[1]] = 1
        return distribution
    
    '''
    スコアの分布を返す
    interval: 区間の大きさ
    '''
    def show_score_distribution(self, interval = 0.1) -> Dict[str, int]:
        scores = [value[0] for value in self.dict.values()]
        # 区間の初期化
        bins = [-1 + i * interval for i in range(int(2/interval) + 2)]
        distribution = {f"{bins[i]:.2f} to {bins[i+1]:.2f}": 0 for i in range(len(bins) - 1)}
        
        # スコアの数を数える
        for score in scores:
            for i in range(len(bins) - 1):
                if bins[i] <= score < bins[i + 1]:
                    distribution[f"{bins[i]:.2f} to {bins[i+1]:.2f}"] += 1
                    break
        return distribution

    def save(self, filename: str = 'test') -> None:
        with open(f"data/train_data/{filename}.pkl", "wb") as file:
            pickle.dump(self.dict, file)
