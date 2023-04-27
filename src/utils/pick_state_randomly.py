import random
from models.state import State

def pick_state_randomly(states: list[State]) -> State:
    return states[random.randint(0, len(states) - 1)]