from typing import Generator
from consts.const import *

c_char = ["E", "G", "C", "e", "g", "c"]
b_char = [" ", "L", "E", "G", "C", "H", "l", "e", "g", "c", "h"]

Piece = int
Place = int
CapturedIndex = int

class State:
    def __init__(self, board: 'Board', captured: 'Captured'):
        self._board = board
        self._captured = captured

    @staticmethod
    def create(board: list[int], captured: list[int]) -> 'State':
        _board = Board(board)
        _captured = Captured(captured)
        return State(_board, _captured)

    def getState(self): 
        return self._board, self._captured
    
    def getBoard(self) -> 'Board': 
        return self._board
    
    def getCaptured(self) -> 'Captured': 
        return self._captured
    
    def copy(self) -> 'State':
        # 盤を複製する
        return State(self._board.copy(), self._captured.copy())
    
    def takePiece(self, place: Place):
        piece = self._board.getPiece(place)
        self._captured.takePiece(piece)

    def getStr(self) -> str:
        board, captured = self.getState()
        str = ""

        # 相手持ち駒
        str += "["
        str += captured.getOpponentStr()
        str += "]\n"
        
        # 盤面
        for i in range(4):
            str += "-------\n"
            str += f"|{board.getStr(i*3)}|{board.getStr(i*3+1)}|{board.getStr(i*3+2)}|\n"
        str += "-------\n"

        # 自分持ち駒
        str += "["
        str += captured.getMyStr()
        str += "]\n\n"

        return str


class Board:
    def __init__(self, board: list[int]):
        self._board = board
    
    def copy(self) -> 'Board':
        return Board(self._board.copy())

    def getPiece(self, place: Place) -> Piece:
        return self._board[place]

    def setPiece(self, place: Place, piece: Piece):
        self._board[place] = piece

    def getStr(self, place: Place) -> str:
        return b_char[self._board[place]]
    
    def getEmptyPlaces(self) -> list[Place]:
        return [place for place in range(RANGE_OF_BOARD) if self._board[place] == EMPTY]
    
class Captured:
    def __init__(self, captured: list[int]):
        self._captured = captured

    def copy(self) -> 'Captured':
        return Captured(self._captured.copy())
    
    def takePiece(self, piece: Piece):
        if(piece == OP_LION_NUM): return
        index = parsePiece(piece)
        self._captured[index] += 1
    
    def usePiece(self, piece: Piece):
        index = parsePiece(piece)
        self._captured[index] -= 1
        print (self._captured)

    def getMyStr(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i]*self._captured[i]
        return ret
    
    def getOpponentStr(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i+3]*self._captured[i+3]
        return ret
    
    def getMyPieces(self) -> list[Piece]:
        return [getPieceNum(capturedIndex) for capturedIndex in range(3) if self._captured[capturedIndex] != 0]

# 駒を与えると、自分の駒のインデックスを返す
# 駒取得時・駒使用時の双方から使用される
pieceToCapIndexDic = {
    MY_ELE_NUM: MY_ELE_INDEX,
    MY_GIR_NUM: MY_GIR_INDEX,
    MY_CHICK_NUM: MY_CHICK_INDEX,
    MY_HEN_NUM: MY_CHICK_INDEX,
    OP_ELE_NUM: MY_ELE_INDEX,
    OP_GIR_NUM: MY_GIR_INDEX,
    OP_CHICK_NUM: MY_CHICK_INDEX,
    OP_HEN_NUM: MY_CHICK_INDEX
}

def parsePiece(piece: Piece) -> CapturedIndex:
    return pieceToCapIndexDic[piece]

# 持ち駒のインデックスから打った後のPieceを返す
capIndexToPieceDic = {
    MY_ELE_INDEX: MY_ELE_NUM,
    MY_GIR_INDEX: MY_GIR_NUM,
    MY_CHICK_INDEX: MY_CHICK_NUM
}

def getPieceNum(index: CapturedIndex) -> Piece:
    return capIndexToPieceDic[index]
