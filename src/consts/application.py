from enum import Enum
from typing import List
from models.state import State

Step = int
History = List[State]

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0
