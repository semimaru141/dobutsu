from models.board import State

RANGE_OF_BOARD = 12

EMPTY = 0
MY_LION_NUM = 1
MY_ELE_NUM = 2
MY_ZIR_NUM = 3
MY_CHICK_NUM = 4

def get_next_boards(state: State):
    res = []
    # 各場所ごとにピースを計算し、各自の動ける箇所から次の盤面を作り出す
    for place in range(RANGE_OF_BOARD):
        piece = state.getBoard().getPiece(place)
        if piece == 0:
            continue
        for move in get_move(piece, place):
            # ToDo 成りのアルゴリズムがない
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
            board.setPiece(place + move, piece)
            res.append(newState)
    
    # ToDo 持ち駒の場合の処理がない
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
    elif piece == MY_ZIR_NUM:
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
