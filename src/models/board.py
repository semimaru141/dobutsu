class Board:
    def __init__(self, board: list[int], captured: list[int]):
        self.board = board
        self.captured = captured

    def getStatus(self): 
        return self.board, self.captured
