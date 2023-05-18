from abc import ABC, abstractmethod
from domains.abstract.state import State

class Visualizer(ABC):
    @abstractmethod
    def __init__(self, state: State) -> None:
        pass

    @abstractmethod
    def visualize(self) -> str:
        pass
