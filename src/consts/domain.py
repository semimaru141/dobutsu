from enum import Enum

Score = float
Key = str
SelectionProbability = float

class Finish(Enum):
    NOT = 0
    WIN = 1
    LOSE = 2

SIZE_OF_BOARD_ONEHOT_VECTOR = 11
SIZE_OF_CAPTURE_ONEHOT_VECTOR = 3

COMPRESSION_THRESHOLD = 2
SOFTMAX_TEMPERATURE = 10
UCB_COEFFICIENT = 0.5

MODEL_EPOCHS = 150
MODEL_BATCH_SIZE = 1024
