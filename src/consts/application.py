from enum import Enum

Step = int

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0
