from enum import Enum
from models.board import State

Step = int
History = list[State]

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0