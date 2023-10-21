from enum import Enum

Step = int
Deps = int
DRAW_LIMIT = 100

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0
