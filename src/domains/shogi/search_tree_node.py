from typing import List, Tuple
from src.consts.domain import Score, SelectionProbability
from src.domains.abstract.state import State
from src.domains.abstract.stockable import Stockable

class SearchTreeNode(Stockable):
    def __init__(self, state: State, score: Score, probability: SelectionProbability) -> None:
        self.state = state
        self.score = score
        self.probability = probability
        self.children: List[SearchTreeNode] = []

    def data_add(self, state: State, score: Score, probability: SelectionProbability) -> None:
        self.children.append(SearchTreeNode(state, score, probability))

    def get_children(self) -> List['SearchTreeNode']:
        return self.children
    
    def get_state(self) -> State:
        return self.state

    def get_all(self) -> Tuple[State, Score, SelectionProbability]:
        return self.state, self.score, self.probability
