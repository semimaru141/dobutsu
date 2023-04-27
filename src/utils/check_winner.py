from consts.application import Step, Winner
from consts.model import Finish

def check_winner(finish: Finish, step: Step) -> Winner:
    add = 0 if finish == Finish.WIN else 1
    if (step + add) % 2 == 0: return Winner.ME
    else: return Winner.OP