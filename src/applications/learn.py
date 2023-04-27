from typing import Tuple
from models.state import State
from models.evaluator import Evaluator
from applications.test import History, Step, pick_state_randomly
from consts.model import Finish, Score
from consts.application import Winner
from models.file_handler import FileHandler
from utils.check_winner import check_winner

TRIAL = 1
LIMIT = 100

def learn():
    evaluator = Evaluator.create_zeros()
    for _ in range(TRIAL):
        run(evaluator, State.create_initial(), 0)
    
    FileHandler(evaluator).save_model('model')
    

def run(evaluator: Evaluator, state: State, step: Step) -> Score:

    # ループからの離脱
    if step > LIMIT: return Winner.NO, step

    # 終了判定
    finish = state.get_finish()
    if finish != Finish.NOT: 
        winner = check_winner(finish, step)
        if winner == Winner.ME: return 1
        else: return -1

    # 再帰
    next_states = state.get_next_boards()
    next_state = pick_state_randomly(next_states)
    score = run(evaluator, next_state.turn(), step + 1)

    # フィードバック
    evaluator.learn(state, score)
    return score * -0.9
