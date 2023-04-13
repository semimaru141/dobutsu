from models.board import State
from consts.const import *

def is_win(state: State) -> bool:
    # 自分のLが最終段に存在する または 相手に王手がかかっている場合に勝利となる
    # 自分のLが最終段に存在する(厳密な条件ではないものの、今回はこちらを条件とした)
    board = state.getBoard()
    for i in range(2):
        if board.getPiece(i) == MY_LION_NUM:
            return True
    
    # 相手の王がいない場合に勝利する
    for i in range(RANGE_OF_BOARD):
        if board.getPiece(i) == OP_LION_NUM:
            return False
    return True
