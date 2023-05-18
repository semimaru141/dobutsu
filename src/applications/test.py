from typing import Tuple
from domains.shogi.shogi_state import ShogiState
from consts.domain import Finish
from consts.application import Winner, Step
from domains.shogi.history import History
from domains.shogi.visualizers.string_visualizer import StringVisualizer
from utils.check_winner import check_winner
from utils.pick_state_randomly import pick_state_randomly

LIMIT = 100

def test():
    winner, step, history = run(ShogiState.create_initial(), 0, History())
    for index, state in enumerate(history):
        print(StringVisualizer(state, index % 2 == 1).visualize())
    print(f"finished in {step} times")
    if winner == Winner.ME:
        print("me win")
    elif winner == Winner.OP:
        print("op win")
    else:
        print("draw")

def run(state: ShogiState, step: Step, history: History) -> Tuple[Winner, Step, History]:
    # historyに追加
    history.add_state(state)

    # ループからの離脱
    if step > LIMIT: return Winner.NO, step, history

    # 終了判定
    finish = state.get_finish()
    if finish != Finish.NOT: return check_winner(finish, step), step, history

    # 再帰
    next_states = state.get_next_states()
    next_state = pick_state_randomly(next_states)
    return run(next_state, step + 1, history)