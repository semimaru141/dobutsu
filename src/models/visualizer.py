from models.state import State
from consts.model import *
from models.board import Board
from models.captured import Captured

c_char = ["E", "G", "C", "e", "g", "c"]
b_char = [" ", "L", "E", "G", "C", "H", "l", "e", "g", "c", "h"]

class Visualizer:
    def __init__(self, state: State) -> None:
        self._state = state

    @property
    def state(self) -> State:
        return self._state
    
    @property
    def board(self) -> Board:
        return self.state.board
    
    @property
    def captured(self) -> Captured:
        return self.state.captured

    def get_state_str(self) -> str:
        str = ""

        # 相手持ち駒
        str += "["
        str += self._captured_str_op()
        str += "]\n"
        
        # 盤面
        for i in range(4):
            str += "-------\n"
            str += f"|{self._board_str(i*3)}|{self._board_str(i*3+1)}|{self._board_str(i*3+2)}|\n"
        str += "-------\n"

        # 自分持ち駒
        str += "["
        str += self._captured_str_me()
        str += "]\n\n"

        return str
    
        # 出力用
    def _captured_str_me(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i]*self.captured.get_count_by_index(i)
        return ret
    
    # 出力用
    def _captured_str_op(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i + 3]*self.captured.get_count_by_index(i + 3)
        return ret
    
        # 出力用
    def _board_str(self, place: Place) -> str:
        return b_char[self.board.get_piece(place)]
    