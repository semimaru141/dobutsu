from models.board import Board
from utils.show_board import get_board_str

start_board = "[]\n-------\n|g|l|e|\n-------\n| |c| |\n-------\n| |C| |\n-------\n|E|L|G|\n-------\n[]\n\n"
in_progress_board = "[eg]\n-------\n| |H|l|\n-------\n| | | |\n-------\n|E| | |\n-------\n| |L| |\n-------\n[GC]\n\n"

class TestCreateXxx:
    # 初期状態
    def test__can_print_aaa(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        boardClass = Board(board, captured)
        assert get_board_str(boardClass) == start_board

    # 手番が進んだ状態
    def test__can_print_bbb(self):
        board = [0, 5, 6, 0, 0, 0, 2, 0, 0, 0, 1, 0]
        captured = [0, 1, 1, 1, 1, 0]
        boardClass = Board(board, captured)
        assert get_board_str(boardClass) == in_progress_board
