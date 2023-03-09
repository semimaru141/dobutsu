from models.board import State
from utils.get_next_boards import get_next_boards

start_board = '''[]
-------
| | | |
-------
| | | |
-------
| |C| |
-------
| | | |
-------
[]

'''
next_board = '''[]
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

board2 = '''[]
-------
| | | |
-------
| | | |
-------
| |C| |
-------
|L| | |
-------
[]

'''

start_board3 = '''[]
-------
| | | |
-------
| |c| |
-------
| |C| |
-------
| | | |
-------
[]

'''

next_board3 = '''[]
-------
| | | |
-------
| |C| |
-------
| | | |
-------
| | | |
-------
[C]

'''

board4 = '''[]
-------
|G|C| |
-------
| | | |
-------
| |L| |
-------
| | |C|
-------
[]

'''

class TestGetNextBoards:
    # ひよこのみでの挙動を確認
    def test_only_chick(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == start_board
        assert len(next_boards) == 1
        assert next_boards[0].getStr() == next_board

    def test_board2(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == board2
        assert len(next_boards) == 3

    def test_board3(self):
        board = [0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == start_board3
        assert len(next_boards) == 1
        assert next_boards[0].getStr() == next_board3
    
    def test_board4(self):
        board = [3, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == board4
        assert len(next_boards) == 9
