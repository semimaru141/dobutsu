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

a_board = '''[]
-------
|g|l|e|
-------
| |h| |
-------
| |C| |
-------
|E|L|G|
-------
[]

'''

class TestGetBoardStr:
    # 初期状態
    def test_initial_board(self):
        board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == start_board
        assert state.get_unique_key() == '867090040213000000'
    
    def test_a_board(self):
        board = [8, 6, 7, 0, 10, 0, 0, 4, 0, 2, 1, 3]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        assert StringVisualizer(state, False).visualize() == a_board
        assert state.get_unique_key() == '8670a0040213000000'
