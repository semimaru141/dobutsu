from typing import List, Tuple
from src.consts.domain import Score, SelectionProbability
from src.domains.abstract.state import State
from src.domains.abstract.stockable import Stockable
from src.domains.shogi.const import Step
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

class History(Stockable):
    def __init__(self) -> None:
        self.list: List[Tuple[State, Score, SelectionProbability]] = []

    def data_add(self, state: State, score: Score, probability: SelectionProbability) -> None:
        self.list.append([state, score, probability])

    def __iter__(self) -> 'History':
        return self
    
    def __next__(self) -> Tuple[State, Score, SelectionProbability]:
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            raise StopIteration
        
    def print(self) -> None:
        for i, (state, score, probability) in enumerate(self):
            print(StringVisualizer(state, i % 2 == 1).visualize())
            print(f'probability: {probability}')
            print(f'score: {score}')
