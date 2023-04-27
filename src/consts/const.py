from enum import Enum

# board
RANGE_OF_BOARD = 12

EMPTY = 0
MY_LION_NUM = 1
MY_ELE_NUM = 2
MY_GIR_NUM = 3
MY_CHICK_NUM = 4
MY_HEN_NUM = 5

OP_LION_NUM = 6
OP_ELE_NUM = 7
OP_GIR_NUM = 8
OP_CHICK_NUM = 9
OP_HEN_NUM = 10

# captured
RANGE_OF_CAPTURED = 6

MY_ELE_INDEX = 0
MY_GIR_INDEX = 1
MY_CHICK_INDEX = 2

OP_ELE_INDEX = 3
OP_GIR_INDEX = 4
OP_CHICK_INDEX = 5

class Finish(Enum):
    WIN = 1
    LOSE = 2

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0
