import random
from typing import List
from models.state import State

def pick_state_randomly(states: List[State]) -> State:
    return states[random.randint(0, len(states) - 1)]