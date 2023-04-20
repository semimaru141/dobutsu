import random
from models.board import State
from utils.get_next_boards import get_next_boards
from utils.is_win import is_win

def exec_syogi(state: State):
    for i in range(100):
        if i % 2 == 0:
            print(state.getStr())
        else:
            print(state.turn().getStr())

        if is_win(state):
            print(f"finished in {i} times")
            return True
        nest_states = get_next_boards(state)
        next_state = nest_states[random.randint(0, len(nest_states) - 1)]
        state = next_state.turn()

if __name__ == "__main__":
    # 初期状態
    board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
    captured = [0, 0, 0, 0, 0, 0]
    state = State.create(board, captured)

    exec_syogi(state)
