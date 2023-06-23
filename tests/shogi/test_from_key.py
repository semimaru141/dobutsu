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

class TestFromKey:
    # 初期状態
    def test_initial_board(self):
        state = ShogiState.from_key('867090040213000000')
        assert StringVisualizer(state, False).visualize() == start_board
