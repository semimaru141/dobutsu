from src.consts.domain import *

class Model():
    def __init__(self, model):
        self.model = model

    def save(self, filename: str = 'default'):
        self.model.save('data/model/' + filename)

    def search_score(key: Key) -> Score:
        return 0
