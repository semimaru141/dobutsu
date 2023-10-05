from enum import Enum

Score = float
Key = str

class Finish(Enum):
    NOT = 0
    WIN = 1
    LOSE = 2

SIZE_OF_BOARD_ONEHOT_VECTOR = 11
SIZE_OF_CAPTURE_ONEHOT_VECTOR = 3

COMPRESSION_THRESHOLD = 2
