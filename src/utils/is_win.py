from models.board import State
from consts.const import *

def is_win(state: State) -> bool:
    # 自分のLが最終段に存在する または 相手に王手がかかっている場合に勝利となる
    # 自分のLが最終段に存在する
    board = state.getBoard()
    for i in range(2):
        if board.getPiece(i) == MY_LION_NUM:
            return True
    
    # 相手に王手がかかっている
    opLionPlace = 0
    for i in range(RANGE_OF_BOARD):
        if board.getPiece(i) == OP_LION_NUM:
            opLionPlace = i
            break
    get_catchable_place(opLionPlace)
    
    return False

def get_catchable_place(opLionPalce):
    if opLionPalce == 7 or opLionPalce == 4:
        return [[], [], []]

# 移動先を取得する
def get_move(piece: int, place: int):
    if piece == MY_CHICK_NUM:
        if place > 2:
            return [-3]
        else: return []
    elif piece == MY_ELE_NUM:
        if place == 4 or place == 7:
            return [-4, -2, 2, 4]
        elif place == 0:
            return [4]
        elif place == 1:
            return [2, 4]
        elif place == 2:
            return [2]
        elif place == 3 or place == 6:
            return [-2, 4]
        elif place == 5 or place == 8:
            return [-4, 2]
        elif place == 9:
            return [-2]
        elif place == 10:
            return [-4, -2]
        elif place == 11:
            return [-4]
    elif piece == MY_ZIR_NUM:
        if place == 4 or place == 7:
            return [-3, -1, 1, 3]
        elif place == 0:
            return [1, 3]
        elif place == 1:
            return [-1, 1, 3]
        elif place == 2:
            return [-1, 3]
        elif place == 3 or place == 6:
            return [-3, 1, 3]
        elif place == 5 or place == 8:
            return [-3, -1, 3]
        elif place == 9:
            return [-3, 1]
        elif place == 10:
            return [-3, -1, 1]
        elif place == 11:
            return [-3, -1]
    elif piece == MY_LION_NUM:
        if place == 4 or place == 7:
            return [-4, -3, -2, -1, 1, 2, 3, 4]
        elif place == 0:
            return [1, 3, 4]
        elif place == 1:
            return [-1, 1, 2, 3, 4]
        elif place == 2:
            return [-1, 2, 3]
        elif place == 3 or place == 6:
            return [-3, -2, 1, 3, 4]
        elif place == 5 or place == 8:
            return [-4, -3, -1, 2, 3]
        elif place == 9:
            return [-3, -2, 1]
        elif place == 10:
            return [-4, -3, -2, -1, 1]
        elif place == 11:
            return [-4, -3, -1]
    else: return []
