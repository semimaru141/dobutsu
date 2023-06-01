import numpy as np
from typing import List, Tuple
from src.consts.domain import *
from src.domains.model.learn_model import LearnModel
from src.domains.abstract.state import State
from src.domains.shogi.const import *

class Learner:
    _data: List[Tuple[State, Score]]

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
        return LearnModel(np.array(input), np.array(output))
    
    def board_processer(self, board_array: List[Piece]):
        input: List[np.ndarray[np.float32]] = []
        for piece in board_array:
            one_hot = np.zeros(RANGE_OR_PIECE, dtype=np.float32)
            one_hot[piece] = 1
            input.append(one_hot)
        return np.concatenate(input)
        
