from src.consts.domain import *
from src.domains.abstract.evaluator import Evaluator
from src.domains.model.model import Model

class ModelEvaluator(Evaluator):
    def __init__(self, model: Model):
        self.model = model

    def search_score(self, key: Key) -> Score:
        return self.model.search_score(key)
