from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

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

board2 = '''[]
-------
| | | |
-------
| | | |
-------
| |C| |
-------
|L| | |
-------
[]

'''

start_board3 = '''[]
-------
| | | |
-------
| |c| |
-------
| |C| |
-------
| | | |
-------
[]

'''

next_board3 = '''[]
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

board4 = '''[]
-------
|G|C| |
-------
| | | |
-------
| |L| |
-------
| | |C|
-------
[]

'''

class TestGetNextBoards:
    # ひよこのみでの挙動を確認
    def test_only_chick(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == start_board
        assert len(next_boards) == 1
        assert StringVisualizer(next_boards[0], True).visualize() == next_board

    def test_board2(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == board2
        assert len(next_boards) == 3

    def test_board3(self):
        board = [0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == start_board3
        assert len(next_boards) == 1
        assert StringVisualizer(next_boards[0], True).visualize() == next_board3
    
    def test_board4(self):
        board = [3, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4]
        captured = [0, 0, 0, 0, 0, 0]
        state = ShogiState.create(board, captured)
        next_boards = state.get_next_states()
        assert StringVisualizer(state, False).visualize() == board4
        assert len(next_boards) == 9
