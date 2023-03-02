from models.board import Board
from utils.get_board_str import get_board_str
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

class TestGetNextBoards:
    # ひよこのみでの挙動を確認
    def test_only_chick(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        boardClass = Board(board, captured)
        next_boards = get_next_boards(boardClass)
        assert get_board_str(boardClass) == start_board
        assert len(next_boards) == 1
        assert get_board_str(next_boards[0]) == next_board

