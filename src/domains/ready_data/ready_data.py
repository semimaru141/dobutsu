import numpy as np

from src.consts.domain import *
from src.domains.train_data.train_data import TrainData
from src.utils.key_handler import proccess_key

class ReadyData:
    def __init__(self, x: np.ndarray, y: np.ndarray):
        self.x = x
        self.y = y

    @staticmethod
    def create_from_train_data(data: TrainData) -> 'ReadyData':
        x = []
        y = []
        for key, value in data.dict.items():
            x.append(proccess_key(key))
            y.append(value[0])
        x = np.array(x, dtype=np.int8)
        y = np.array(y, dtype=np.float32)
        return ReadyData(x, y)

    @staticmethod
    def create_from_file(filename: str = 'default'):
        data = np.load('data/ready_data/' + filename + '.npz')
        x = data['arr_0']
        y = data['arr_1']
        return ReadyData(x, y)

    def save(self, filename: str = 'default'):
        np.savez_compressed('data/ready_data/' + filename + '.npz', self.x, self.y)

    def clone_with_rand_y(self) -> 'ReadyData':
        rand_y = np.random.random(len(self.y)) * 2.0 - 1.0
        return ReadyData(self.x, rand_y)
