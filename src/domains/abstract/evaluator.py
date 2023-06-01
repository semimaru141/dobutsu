from abc import ABC, abstractmethod
from src.consts.domain import *

class Evaluator(ABC):
    @abstractmethod
    def search_score(self, key: Key) -> Score:
        pass
