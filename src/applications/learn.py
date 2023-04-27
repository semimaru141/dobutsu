import random
from models.board import State
from consts.const import Finish
from utils.get_next_boards import get_next_boards
from utils.is_finish import is_finish

def run():
    pass

def a(state: State):
    state = State.create_initial()
    for i in range(100):
        if i % 2 == 0:
            print(state.getStr())
        else:
            print(state.turn().getStr())

        finish_flag, finish = is_finish(state)
        if finish_flag:
            print(f"finished in {i} times")
            add = 0 if finish == Finish.WIN else 1
            if (i + add) % 2 == 0:
                print("me win")
            else:
                print("op win")
            return
        nest_states = get_next_boards(state)
        next_state = nest_states[random.randint(0, len(nest_states) - 1)]
        state = next_state.turn()