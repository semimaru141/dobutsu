import random
from typing import Tuple
from src.domains.abstract.state import *
from src.domains.shogi.shogi_state import ShogiState
from src.consts.domain import Finish
from src.consts.application import Winner, Step
from src.domains.shogi.history import History
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer
from src.utils.check_winner import check_winner
from src.utils.pick_state_randomly import pick_state_randomly

LIMIT = 100

base_key = '060820021000000012'
seed = 'a'

def test():
    random.seed(seed)
    history = History()
    _, winner = run(history, ShogiState.from_key(base_key), 0)
    if winner == Winner.ME:
        print("me win")
    elif winner == Winner.OP:
        print("op win")
    else:
        print("draw")
    for state, _, score in history:
        print(StringVisualizer(state, False).visualize())
        print(f'score: {score}')

def run(history: History, state: State, step: Step) -> Tuple[Score, Winner]:
    # ループからの離脱
    if step > LIMIT: return 0

    # 終了判定
    finish = state.get_finish()
    if finish == Finish.WIN:
        score = 1
        history.data_add([state, step, score])
        return score, winner
    elif finish == Finish.LOSE:
        score = -1
        history.data_add([state, step, score])
        winner = check_winner(finish, step)
        return score, winner

    # 再帰
    next_states = state.get_next_states()
    next_state = pick_state_randomly(next_states)
    score, winner = run(history, next_state, step + 1)
    score = score * -0.95

    # フィードバック
    history.data_add([state, step, score])
    return score, winner
