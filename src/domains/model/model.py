import numpy as np
from src.consts.domain import *
from src.utils.key_handler import proccess_key

class Model():
    def __init__(self, model):
        self.model = model

    def save(self, filename: str = 'default'):
        self.model.save('data/model/' + filename)

    def search_score(self, key: Key) -> Score:
        x = np.array([proccess_key(key)], dtype=np.float32)
        t = self.model(x, training=False)
        return t[0][0]
