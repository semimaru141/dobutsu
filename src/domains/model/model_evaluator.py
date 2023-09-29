from typing import Dict
from src.consts.domain import *
from src.domains.abstract.evaluator import Evaluator
from src.domains.model.model import Model

class ModelEvaluator(Evaluator):
    def __init__(self, model: Model):
        self.model = model
        self.cache: Dict[Key, Score] = {}

    def search_score(self, key: Key) -> Score:
        if key in self.cache:
            return self.cache[key]
        else:
            score = self._search_score(key)
            self.cache[key] = score
            return score
    
    def _search_score(self, key: Key) -> Score:
        return self.model.search_score(key)
