from domains.shogi.shogi_state import ShogiState

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
        assert state.get.get_state_str() == start_board
        assert len(next_boards) == 1
        assert Visualizer(next_boards[0]).get_state_str() == next_board

    def test_board2(self):
        board = [0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = state.get_next_states()
        assert Visualizer(state).get_state_str() == board2
        assert len(next_boards) == 3

    def test_board3(self):
        board = [0, 0, 0, 0, 9, 0, 0, 4, 0, 0, 0, 0]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = state.get_next_states()
        assert Visualizer(state).get_state_str() == start_board3
        assert len(next_boards) == 1
        assert Visualizer(next_boards[0]).get_state_str() == next_board3
    
    def test_board4(self):
        board = [3, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 4]
        captured = [0, 0, 0, 0, 0, 0]
        state = State.create(board, captured)
        next_boards = state.get_next_states()
        assert Visualizer(state).get_state_str() == board4
        assert len(next_boards) == 9
