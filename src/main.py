from utils.show_board import show_board
from models.board import Board

if __name__ == "__main__":
    # 初期状態
    board = [8, 6, 7, 0, 9, 0, 0, 4, 0, 2, 1, 3]
    captured = [0, 0, 0, 0, 0, 0]
    boardClass = Board(board, captured)
    show_board(boardClass)

    # 手番が進んだ状態
    board = [0, 5, 6, 0, 0, 0, 2, 0, 0, 0, 1, 0]
    captured = [0, 1, 1, 1, 1, 0]
    boardClass = Board(board, captured)
    show_board(boardClass)

