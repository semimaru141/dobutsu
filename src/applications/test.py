import random
from typing import Tuple
from models.board import State
from consts.const import Finish
from consts.const import Winner
from utils.get_next_boards import get_next_boards
from utils.is_finish import is_finish

Step = int
History = list[State]

def test():
    winner, step, history = run(State.create_initial(), 0, [])
    for state in history:
        print(state.getStr())
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
    if step > 100: return Winner.NO, step, history

    # 終了判定
    finish_flag, finish = is_finish(state)
    if finish_flag: return check_winner(finish, step), step, history
        
    # 再帰
    next_states = get_next_boards(state)
    next_state = pick_state_randomly(next_states)
    return run(next_state.turn(), step + 1, history)

def pick_state_randomly(states: State) -> State:
    return states[random.randint(0, len(states) - 1)]

def check_winner(finish: Finish, step: Step) -> Winner:
    add = 0 if finish == Finish.WIN else 1
    if (step + add) % 2 == 0: return Winner.ME
    else: return Winner.OP
