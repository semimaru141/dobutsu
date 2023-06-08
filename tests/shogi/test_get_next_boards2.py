from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer


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
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == start_board
        assert len(next_boards) == 1
        assert StringVisualizer(next_boards[0], True).visualize() == next_board

    def test_board2(self):
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        captured = [0, 0, 1, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == board2
        assert len(next_boards) == 12

    def test_board3(self):
        board = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        captured = [0, 1, 1, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == board3
        assert len(next_boards) == 30
    
    def test_board4(self):
        board = [0, 0, 0, 0, 10, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == start_board4
        assert StringVisualizer(next_boards[0], True).visualize() == next_board4
