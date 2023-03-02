import numpy as np

class Board:
    def __init__(self, board: list[int], captured: list[int]):
        self.board = board
        self.captured = captured

    def getStatus(self): 
        return self.board, self.captured
    
    def copyBoard(self):
        return Board(self.board.copy(), self.captured.copy())
