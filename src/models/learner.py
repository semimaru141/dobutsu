import numpy as np
from models.learn_model import LearnModel
from typing import Tuple
from models.state import State
from consts.model import *

class Learner:
    _data: list[Tuple[State, Score]]

    def __init__(self) -> None:
        self._data = []

    def data_add(self, state: State, score: Score) -> None:
        self._data.append((state, score))

    # とりあえずボードのみで評価する
    def make_model(self) -> LearnModel:
        input = []
        output = []
        for data in self._data:
            input.append(self.board_processer(data[0].board._board))
            output.append(data[1])
        return LearnModel(input, output)
    
    def board_processer(self, board_array: list[Piece]):
        input: list[np.ndarray[np.float32]] = []
        for piece in board_array:
            one_hot = np.zeros(RANGE_OR_PIECE, dtype=np.float32)
            one_hot[piece] = 1
            input.append(one_hot)
        return np.concatenate(input)
        
