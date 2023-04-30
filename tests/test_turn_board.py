from domains.state import State
from domains.visualizer import Visualizer

start_board = '''[]
-------
|g|l|e|
-------
| |c| |
-------
| |C| |
-------
|E|L|G|
-------
[]

'''
in_progress_board = '''[eg]
-------
| |H|l|
-------
| | | |
-------
|E| | |
-------
| |L| |
-------
[GC]

'''
in_progress_board_t = '''[gc]
-------
| |l| |
-------
| | |e|
-------
| | | |
-------
|L|h| |
-------
[EG]

'''

class TestTurnBoard:
    # 初期状態
    def test_initial_board(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        turn = state.turn()
        assert Visualizer(state).get_state_str() == start_board
        assert Visualizer(turn).get_state_str() == start_board

    # 手番が進んだ状態
    def test_in_progress_board(self):
        board = [0, 5, 6, 0, 0, 0, 2, 0, 0, 0, 1, 0]
        captured = [0, 1, 1, 1, 1, 0]
        state = State.create(board, captured)
        turn = state.turn()
        assert Visualizer(state).get_state_str() == in_progress_board
        assert Visualizer(turn).get_state_str() == in_progress_board_t
