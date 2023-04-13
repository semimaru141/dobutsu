from models.board import State
from consts.const import *

def get_next_boards(state: State):
    res = []
    # 各場所ごとにピースを計算し、各自の動ける箇所から次の盤面を作り出す
    for place in range(RANGE_OF_BOARD):
        piece = state.getBoard().getPiece(place)
        if piece == 0:
            continue
        for move in get_move(piece, place):
            newState = state.copy()
            board, captured = newState.getState()
            dstPiece = board.getPiece(place + move)
            if dstPiece > 0 and dstPiece < 6:
                # 自分の駒がある場合は移動できない
                continue
            elif dstPiece > 5:
                # 相手のコマがある場合は取得する
                captured.takePiece(dstPiece)
            
            board.setPiece(place, EMPTY)
            # 成りのアルゴリズム
            if (piece == MY_CHICK_NUM and place + move in [0, 1, 2]):
                board.setPiece(place + move, MY_HEN_NUM)
            else:
                board.setPiece(place + move, piece)
            res.append(newState)
    
    # 駒を打つアルゴリズム
    emptyPlaces = state.getBoard().getEmptyPlaces()
    myPieces = state.getCaptured().getMyPieces()
    for (place, piece) in ((place, piece) for place in emptyPlaces for piece in myPieces):
        newState = state.copy()
        board, captured = newState.getState()
        board.setPiece(place, piece)
        captured.usePiece(piece)
        res.append(newState)
    return res

# 移動先を取得する
def get_move(piece: int, place: int):
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
