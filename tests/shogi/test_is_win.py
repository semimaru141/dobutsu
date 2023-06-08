from src.consts.domain import Finish
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer


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
|g|l|e|
-------
| |c| |
-------
| |C| |
-------
|E| |G|
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
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == board1
        assert state.get_finish() == Finish.NOT

    # 手番が進んだ状態
    def test_board2(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 0, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == board2
        assert state.get_finish() == Finish.LOSE

    def test_board3(self):
        board = [0, 1, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == board3
        assert state.get_finish() == Finish.WIN