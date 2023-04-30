from typing import List
from consts.domain import *

class Board:
    def __init__(self, board: List[int]):
        self._board = board
    
    @staticmethod
    def create_initial() -> 'Board':
        return Board(INITIAL_BOARD)

    def copy(self) -> 'Board':
        return Board(self._board.copy())

    # 該当のPlaceについて、Pieceの情報を与える
    def get_piece(self, place: Place) -> Piece:
        return self._board[place]

    # 該当のPlaceにPieceを設置する
    def set_piece(self, place: Place, piece: Piece):
        self._board[place] = piece

    # 駒が配置可能なPlaceを取得する
    def get_empty_places(self) -> List[Place]:
        return [place for place in range(RANGE_OF_BOARD) if self._board[place] == EMPTY]
    
    # 先手後手入れ替える
    def turn(self):
        # 1. 配列を反転する
        # 2. OPとMYの駒を反転させる
        new_board = [turn_piece(piece) for piece in self._board[::-1]]
        return Board(new_board)

turn_piece_dic = {
    EMPTY: EMPTY,
    MY_ELE_NUM: OP_ELE_NUM,
    MY_GIR_NUM: OP_GIR_NUM,
    MY_CHICK_NUM: OP_CHICK_NUM,
    MY_HEN_NUM: OP_HEN_NUM,
    MY_LION_NUM: OP_LION_NUM,
    OP_ELE_NUM: MY_ELE_NUM,
    OP_GIR_NUM: MY_GIR_NUM,
    OP_CHICK_NUM: MY_CHICK_NUM,
    OP_HEN_NUM: MY_HEN_NUM,
    OP_LION_NUM: MY_LION_NUM
}

def turn_piece(piece: Piece) -> Piece:
    return turn_piece_dic[piece]
