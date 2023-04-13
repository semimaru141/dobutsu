from models.board import State
from utils.get_next_boards import get_next_boards

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
        next_boards = get_next_boards(state)
        assert state.getStr() == start_board
        assert len(next_boards) == 1
        assert next_boards[0].getStr() == next_board

