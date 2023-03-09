import numpy as np

c_char = ["E", "G", "C", "e", "g", "c"]
b_char = [" ", "L", "E", "G", "C", "H", "l", "e", "g", "c", "l"]

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
    
class Captured:
    def __init__(self, captured: list[int]):
        self._captured = captured

    def copy(self) -> 'Captured':
        return Captured(self._captured.copy())
    
    def takePiece(self, piece: Piece):
        index = parsePiece(piece)
        self._captured[index] += 1

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



# 駒を与えると、相手の駒のインデックスを返す
pieceToCapIndexDic = {
    2: 3,
    3: 4,
    4: 5,
    5: 5,
    7: 0,
    8: 1,
    9: 2,
    10: 2
}

# * 0 空白
# * 1 ライオン(先手) L
# * 2 ぞう(先手) E
# * 3 きりん(先手) G
# * 4 ひよこ(先手) C
# * 5 にわとり(先手) H
# * 6 ライオン(後手) l
# * 7 ぞう(後手) e 
# * 8 きりん(後手) g
# * 9 ひよこ(後手) c
# * 10 にわとり(後手) l


# * 0 ぞう (先手の持ち駒)
# * 1 きりん (先手の持ち駒)
# * 2 ひよこ (先手の持ち駒)
# * 3 ぞう (後手の持ち駒)
# * 4 きりん (後手の持ち駒)
# * 5 ひよこ (後手の持ち駒)

def parsePiece(piece: Piece) -> CapturedIndex:
    return pieceToCapIndexDic[piece]
