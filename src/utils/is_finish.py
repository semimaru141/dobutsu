from models.board import State
from consts.model import *

def is_finish(state: State) -> Finish:
    # 自分のLが最終段に存在する または 相手に王手がかかっている場合に勝利となる
    # 自分のLが最終段に存在する(厳密な条件ではないものの、今回はこちらを条件とした)
    board = state.getBoard()
    for i in range(3):
        if board.getPiece(i) == MY_LION_NUM:
            return Finish.WIN
    
    # 自分の王がいない場合に敗北する
    for i in range(RANGE_OF_BOARD):
        if board.getPiece(i) == MY_LION_NUM:
            return Finish.NOT
    return Finish.LOSE
