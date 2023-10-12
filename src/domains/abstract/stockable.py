from abc import ABC, abstractmethod
from src.consts.domain import Score
from src.domains.abstract.state import State

class Stockable(ABC):
    @abstractmethod
    def data_add(self, state: State, score: Score) -> None:
        pass
