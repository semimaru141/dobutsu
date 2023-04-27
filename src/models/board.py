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
    
    def turn(self):
        board, captured = self.getState()
        return State(board.turn(), captured.turn())

class Board:
    def __init__(self, board: list[int]):
        self._board = board
    
    def copy(self) -> 'Board':
        return Board(self._board.copy())

    # 該当のPlaceについて、Pieceの情報を与える
    def getPiece(self, place: Place) -> Piece:
        return self._board[place]

    # 該当のPlaceにPieceを設置する
    def setPiece(self, place: Place, piece: Piece):
        self._board[place] = piece

    # 出力用
    def getStr(self, place: Place) -> str:
        return b_char[self._board[place]]
    
    # 駒が配置可能なPlaceを取得する
    def getEmptyPlaces(self) -> list[Place]:
        return [place for place in range(RANGE_OF_BOARD) if self._board[place] == EMPTY]
    
    # 先手後手入れ替える
    def turn(self):
        # 1. 配列を反転する
        # 2. OPとMYの駒を反転させる
        new_board = [turnPiece(piece) for piece in self._board[::-1]]
        return Board(new_board)
    
class Captured:
    def __init__(self, captured: list[int]):
        self._captured = captured

    def copy(self) -> 'Captured':
        return Captured(self._captured.copy())
    
    # Pieceを取得する。該当のPieceの個数を増やす
    def takePiece(self, piece: Piece):
        if(piece == OP_LION_NUM): return
        index = parsePiece(piece)
        self._captured[index] += 1

    # Pieceを使用する。該当するPieceの個数を減らす 
    def usePiece(self, piece: Piece):
        index = parsePiece(piece)
        self._captured[index] -= 1

    # 出力用
    def getMyStr(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i]*self._captured[i]
        return ret
    
    # 出力用
    def getOpponentStr(self) -> str:
        ret = ''
        for i in range(3):
            ret += c_char[i+3]*self._captured[i+3]
        return ret
    
    # 先手が使用可能なPieceを取得する
    def getMyPieces(self) -> list[Piece]:
        return [getPieceNum(capturedIndex) for capturedIndex in range(3) if self._captured[capturedIndex] != 0]
    
    # 先手後手を入れ替える
    def turn(self):
        new_captured = list(range(RANGE_OF_CAPTURED))
        for index in range(RANGE_OF_CAPTURED):
            new_captured[turnIndex(index)] = self._captured[index]
        return Captured(new_captured)

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

turnPieceDic = {
    EMPTY: EMPTY,
    MY_ELE_NUM: OP_ELE_NUM,
    MY_GIR_NUM: OP_GIR_NUM,
    MY_CHICK_NUM: OP_CHICK_NUM,
    MY_HEN_NUM: OP_HEN_NUM,
    MY_LION_NUM: OP_LION_NUM,
    OP_ELE_NUM: MY_ELE_NUM,
    OP_GIR_NUM: MY_GIR_NUM,
    OP_CHICK_NUM: MY_CHICK_NUM,
    OP_HEN_NUM: MY_HEN_NUM,
    OP_LION_NUM: MY_LION_NUM
}

def turnPiece(piece: Piece) -> Piece:
    return turnPieceDic[piece]

turnIndexDic = {
    MY_ELE_INDEX: OP_ELE_INDEX,
    MY_GIR_INDEX: OP_GIR_INDEX,
    MY_CHICK_INDEX: OP_CHICK_INDEX,
    OP_ELE_INDEX: MY_ELE_INDEX,
    OP_GIR_INDEX: MY_GIR_INDEX,
    OP_CHICK_INDEX: MY_CHICK_INDEX
}

def turnIndex(index: CapturedIndex) -> CapturedIndex:
    return turnIndexDic[index]
