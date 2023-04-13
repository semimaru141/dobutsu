from models.board import State
from utils.get_next_boards import get_next_boards

start_board = '''[]
-------
| | | |
-------
| |h| |
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
[C]

'''
board2 = '''[]
-------
| | | |
-------
| | | |
-------
| | | |
-------
| | | |
-------
[C]

'''
board3 = '''[]
-------
| | | |
-------
| | | |
-------
| |L| |
-------
| | | |
-------
[GC]

'''
start_board4 = '''[]
-------
| | | |
-------
| |h| |
-------
| |C| |
-------
| | | |
-------
[]

'''
next_board4 = '''[]
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

class TestGetNextBoards2:
    def test_only_chick(self):
        board = [0, 0, 0, 0, 10, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == start_board
        assert len(next_boards) == 1
        assert next_boards[0].getStr() == next_board

    def test_board2(self):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        captured = [0, 0, 1, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == board2
        assert len(next_boards) == 12

    def test_board3(self):
        board = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        captured = [0, 1, 1, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == board3
        assert len(next_boards) == 30
    
    def test_board4(self):
        board = [0, 0, 0, 0, 10, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = get_next_boards(state)
        assert state.getStr() == start_board4
        assert next_boards[0].getStr() == next_board4
