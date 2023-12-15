from abc import ABC, abstractmethod
from src.consts.domain import *
from src.domains.abstract.state import State

class CalcScoreStrategy(ABC):
    def __init__(self, gamma: float):
        self.gamma = gamma

    def set_gamma(self, gamma: float):
        self.gamma = gamma

    @abstractmethod
    def calc_score(self, state: State, before_score: Score) -> Score:
        pass
