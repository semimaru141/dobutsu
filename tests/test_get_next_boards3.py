from domains.state import State
from domains.visualizer import Visualizer

start_board = '''[]
-------
| | | |
-------
| |C| |
-------
| | | |
-------
| | | |
-------
[]

'''
next_board = '''[]
-------
| |H| |
-------
| | | |
-------
| | | |
-------
| | | |
-------
[]

'''

class TestGetNextBoards2:
    def test_only_chick(self):
        board = [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = state.get_next_states()
        assert Visualizer(state).get_state_str() == start_board
        assert len(next_boards) == 1
        assert Visualizer(next_boards[0]).get_state_str() == next_board

