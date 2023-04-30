from typing import List, Type
from models.board import Board
from models.captured import Captured
from consts.model import *

class State:
    def __init__(self, board: 'Board', captured: 'Captured'):
        self._board = board
        self._captured = captured

    @staticmethod
    def create(board: List[int], captured: List[int]) -> 'State':
        _board = Board(board)
        _captured = Captured(captured)
        return State(_board, _captured)
    
    @staticmethod
    def create_initial() -> 'State':
        board = Board.create_initial()
        captured = Captured.create_initial()
        return State(board, captured)

    @property
    def state(self): 
        return self.board, self.captured
    
    @property
    def board(self) -> 'Board': 
        return self._board
    
    @property
    def captured(self) -> 'Captured': 
        return self._captured
    
    def copy(self) -> 'State':
        # 盤を複製する
        return State(self._board.copy(), self._captured.copy())
    
    def turn(self):
        board, captured = self.state
        return State(board.turn(), captured.turn())

    def get_finish(self) -> Finish:
        # 自分のLが最終段に存在する または 相手に王手がかかっている場合に勝利となる
        # 自分のLが最終段に存在する(厳密な条件ではないものの、今回はこちらを条件とした)
        board = self.board
        for i in range(3):
            if board.get_piece(i) == MY_LION_NUM:
                return Finish.WIN
        
        # 自分の王がいない場合に敗北する
        for i in range(RANGE_OF_BOARD):
            if board.get_piece(i) == MY_LION_NUM:
                return Finish.NOT
        return Finish.LOSE
    
    def get_next_boards(self) -> List[Type['State']]:
        res = []
        # 各場所ごとにピースを計算し、各自の動ける箇所から次の盤面を作り出す
        for place in range(RANGE_OF_BOARD):
            piece = self.board.get_piece(place)
            if piece == EMPTY:
                continue
            for move in get_move(piece, place):
                new_state = self.copy()
                board, captured = new_state.state
                dst_place = place + move
                dst_piece = board.get_piece(dst_place)
                if dst_piece > 0 and dst_piece < 6:
                    # 自分の駒がある場合は移動できない
                    continue
                elif dst_piece > 5:
                    # 相手のコマがある場合は取得する
                    captured.take_piece(dst_piece)
                
                board.set_piece(place, EMPTY)
                # 成りのアルゴリズム
                if (piece == MY_CHICK_NUM and dst_place in [0, 1, 2]):
                    board.set_piece(dst_place, MY_HEN_NUM)
                else:
                    board.set_piece(dst_place, piece)
                res.append(new_state)
        
        # 駒を打つアルゴリズム
        empty_places = self.board.get_empty_places()
        myPieces = self.captured.get_my_pieces()
        for (place, piece) in ((place, piece) for place in empty_places for piece in myPieces):
            new_state = self.copy()
            board, captured = new_state.state
            board.set_piece(place, piece)
            captured.use_piece(piece)
            res.append(new_state)
        return res

# 移動先を取得する
def get_move(piece: Piece, place: Place):
    if piece == MY_CHICK_NUM:
        if place > 2:
            return [-3]
        else: return []
    elif piece == MY_ELE_NUM:
        if place == 4 or place == 7:
            return [-4, -2, 2, 4]
        elif place == 0:
            return [4]
        elif place == 1:
            return [2, 4]
        elif place == 2:
            return [2]
        elif place == 3 or place == 6:
            return [-2, 4]
        elif place == 5 or place == 8:
            return [-4, 2]
        elif place == 9:
            return [-2]
        elif place == 10:
            return [-4, -2]
        elif place == 11:
            return [-4]
    elif piece == MY_GIR_NUM:
        if place == 4 or place == 7:
            return [-3, -1, 1, 3]
        elif place == 0:
            return [1, 3]
        elif place == 1:
            return [-1, 1, 3]
        elif place == 2:
            return [-1, 3]
        elif place == 3 or place == 6:
            return [-3, 1, 3]
        elif place == 5 or place == 8:
            return [-3, -1, 3]
        elif place == 9:
            return [-3, 1]
        elif place == 10:
            return [-3, -1, 1]
        elif place == 11:
            return [-3, -1]
    elif piece == MY_LION_NUM:
        if place == 4 or place == 7:
            return [-4, -3, -2, -1, 1, 2, 3, 4]
        elif place == 0:
            return [1, 3, 4]
        elif place == 1:
            return [-1, 1, 2, 3, 4]
        elif place == 2:
            return [-1, 2, 3]
        elif place == 3 or place == 6:
            return [-3, -2, 1, 3, 4]
        elif place == 5 or place == 8:
            return [-4, -3, -1, 2, 3]
        elif place == 9:
            return [-3, -2, 1]
        elif place == 10:
            return [-4, -3, -2, -1, 1]
        elif place == 11:
            return [-4, -3, -1]
    else: return []

