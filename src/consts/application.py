from enum import Enum
from typing import List, Tuple
from domains.abstract.state import State

Step = int

class Winner(Enum):
    ME = 1
    OP = -1
    # draw
    NO = 0
