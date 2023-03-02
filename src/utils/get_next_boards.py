from models.board import Board

RANGE_OF_BOARD = 12

MY_LION_NUM = 1
MY_ELE_NUM = 2
MY_ZIR_NUM = 3
MY_CHICK_NUM = 4

def get_next_boards(board: Board):
    res = []
    # 各場所ごとにピースを計算し、各自の動ける箇所から次の盤面を作り出す
    for i in range(RANGE_OF_BOARD):
        piece = board.board[i]
        if piece == 0:
            continue
        for move in get_move(piece, i):
            # ToDo 駒の取得のアルゴリズムがない
            # ToDo 成りのアルゴリズムがない
            newBoard = board.copyBoard()
            newBoard.board[i] = 0
            newBoard.board[i + move] = piece
            res.append(newBoard)
    # ToDo 持ち駒の場合の処理がない
    return res

# 移動先を取得する
# ToDo マスの外に出ることを考えなくてはいけないが一旦省略
def get_move(piece: int, place: int):
    if piece == MY_CHICK_NUM:
        if place > 3:
            return [-3]
        else: return []
    elif piece == MY_ELE_NUM:
        return [-4, -2, 2, 4]
    elif piece == MY_ZIR_NUM:
        return [-3, -1, 1, 3]
    elif piece == MY_LION_NUM:
        return [-4, -3, -2, -1, 1, 2, 3, 4]
