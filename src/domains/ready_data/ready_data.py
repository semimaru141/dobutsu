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
        x = np.array([])
        y = np.array([])
        for key, value in data.dict.items():
            x = np.append(x, proccess_key(key))
            y = np.append(y, value[0])
        return ReadyData(x, y)
    
    @staticmethod
    def create_from_file(filename: str = 'default'):
        x = np.load('data/ready_data/' + filename + '_x')
        y = np.load('data/ready_data/' + filename + '_x')
        return ReadyData(x, y)

    def save(self, filename: str = 'default'):
        np.savez('data/ready_data/' + filename + '_x', self.x)
        np.savez('data/ready_data/' + filename + '_y', self.y)
