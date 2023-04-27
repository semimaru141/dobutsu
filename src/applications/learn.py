from typing import Tuple
from models.board import State
from models.evaluator import Evaluator
from applications.test import History, Step, pick_state_randomly
from consts.model import Finish
from consts.application import Winner
from utils.check_winner import check_winner
from utils.get_next_boards import get_next_boards
from utils.is_finish import is_finish

def learn():
    # 初期状態
    state = State.create_initial()
    evaluator = Evaluator.create_rand()

def run(state: State, step: Step, history: History) -> Tuple[Winner, Step, History]:
    # historyに追加
    if step % 2 == 0: history.append(state)
    else: history.append(state.turn())

    # ループからの離脱
    if step > 100: return Winner.NO, step, history

    # 終了判定
    finish = is_finish(state)
    if finish != Finish.NOT: return check_winner(finish, step), step, history
        
    # 再帰
    next_states = get_next_boards(state)
    next_state = pick_state_randomly(next_states)
    return run(next_state.turn(), step + 1, history)