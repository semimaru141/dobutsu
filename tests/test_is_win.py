from models.board import State
from utils.is_win import is_win

board1 = '''[]
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
board2 = '''[]
-------
|g| |e|
-------
| |c| |
-------
| |C| |
-------
|E|L|G|
-------
[]

'''
board3 = '''[]
-------
|g| |e|
-------
| |c| |
-------
| |C| |
-------
|E|L|G|
-------
[]

'''
board3 = '''[]
-------
| |L| |
-------
| | | |
-------
| |l| |
-------
| | | |
-------
[]

'''



class TestIsWin:
    # 初期状態
    def test_board1(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        assert state.getStr() == board1
        assert is_win(state) == False

    # 手番が進んだ状態
    def test_board2(self):
        board = [8, 0, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        assert state.getStr() == board2
        assert is_win(state) == True

    def test_board3(self):
        board = [0, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        assert state.getStr() == board3
        assert is_win(state) == True