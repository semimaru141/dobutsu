import numpy as np
from models.state import State
from consts.model import *

class Evaluator:
    def __init__(self) -> None:
        self._model = np.zeros(tuple(11 for _ in range(12)), dtype=np.float32)

    @staticmethod
    def create_zeros() -> 'Evaluator':
        return Evaluator()
    
    @staticmethod
    def create_from_arg() -> 'Evaluator':
        return Evaluator()

    # とりあえずボードのみで評価する
    def learn(self, state: State, score: Score) -> None:
        target = self.model
        for place in range(RANGE_OF_BOARD - 1):
            piece = state.board.get_piece(place)
            target = target[piece]
        piece = state.board.get_piece(RANGE_OF_BOARD - 1)
        target[piece] += score

    # stateの評価値を計算する
    def evaluate(self, state: State) -> Score:
        target = self.model
        for place in range(RANGE_OF_BOARD):
            piece = state.board.get_piece(place)
            target = target[piece]
        return target
    
    @property
    def model(self) -> np.ndarray[np.float64]:
        return self._model
