from functools import reduce
import itertools
import numpy as np

from src.consts.domain import *
from src.domains.ready_data.const import SIZE_OF_ONEHOT_VECTOR
from src.domains.train_data.train_data import TrainData

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

def proccess_key(key: Key) :
    one_hots = map(lambda s: one_hot_encode(int(s) if s != 'a' else 10), key[:12])
    return np.array(list(itertools.chain.from_iterable(one_hots)))

def one_hot_encode(value: int):
    one_hot = np.zeros(SIZE_OF_ONEHOT_VECTOR, dtype=np.float32)
    one_hot[value] = 1
    return one_hot
