from domains.state import State
from domains.learner import Learner
from consts.domain import Finish, Score
from consts.application import Winner, Step
from utils.pick_state_randomly import pick_state_randomly
from utils.check_winner import check_winner

TRIAL = 1000
LIMIT = 100

def learn():
    learner = Learner()
    for _ in range(TRIAL):
        run(learner, State.create_initial(), 0)
    model = learner.make_model()
    model.save()

def run(learner: Learner, state: State, step: Step) -> Score:
    # ループからの離脱
    if step > LIMIT: return 0

    # 終了判定
    finish = state.get_finish()
    if finish != Finish.NOT: 
        winner = check_winner(finish, step)
        if winner == Winner.ME: return 1
        else: return -1

    # 再帰
    next_states = state.get_next_boards()
    next_state = pick_state_randomly(next_states)
    score = run(learner, next_state.turn(), step + 1)

    # フィードバック
    learner.data_add(state, score)
    return score * -0.9
