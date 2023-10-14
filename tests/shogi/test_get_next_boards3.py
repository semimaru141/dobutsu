from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer


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
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == start_board
        assert len(next_boards) == 1
        assert StringVisualizer(next_boards[0], True).visualize() == next_board

    def test_hen(self):
        board = [0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == next_board
        assert len(next_boards) == 3

