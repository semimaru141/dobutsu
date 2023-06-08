from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

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

class TestGetBoardStr:
    # 初期状態
    def test_initial_board(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == start_board

    # 手番が進んだ状態
    def test_in_progress_board(self):
        board = [0, 5, 6, 0, 0, 0, 2, 0, 0, 0, 1, 0]
        captured = [0, 1, 1, 1, 1, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == in_progress_board
