from typing import Tuple
from domains.state import State
from domains.visualizer import Visualizer
from consts.domain import Finish
from consts.application import History, Step, Winner
from utils.check_winner import check_winner
from utils.pick_state_randomly import pick_state_randomly

LIMIT = 100

def test():
    winner, step, history = run(State.create_initial(), 0, [])
    for state in history:
        visualizer = Visualizer(state)
        print(visualizer.get_state_str())
    print(f"finished in {step} times")
    if winner == Winner.ME:
        print("me win")
    elif winner == Winner.OP:
        print("op win")
    else:
        print("draw")

def run(state: State, step: Step, history: History) -> Tuple[Winner, Step, History]:
    # historyに追加
    if step % 2 == 0: history.append(state)
    else: history.append(state.turn())

    # ループからの離脱
    if step > LIMIT: return Winner.NO, step, history

    # 終了判定
    finish = state.get_finish()
    if finish != Finish.NOT: return check_winner(finish, step), step, history

    # 再帰
    next_states = state.get_next_boards()
    next_state = pick_state_randomly(next_states)
    return run(next_state.turn(), step + 1, history)