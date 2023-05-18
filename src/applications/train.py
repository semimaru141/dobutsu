from domains.abstract.state import State
from consts.domain import Finish, Score
from consts.application import Winner, Step
from domains.shogi.shogi_state import ShogiState
from domains.train_data.train_data_mc_factory import TrainDataMCFactory
from utils.pick_state_randomly import pick_state_randomly
from utils.check_winner import check_winner

TRIAL = 1000
LIMIT = 100

def train():
    factory = TrainDataMCFactory()
    for _ in range(TRIAL):
        run(factory, ShogiState.create_initial(), 0)
    train_data = factory.create()
    print(train_data)
    train_data.save()


def run(factory: TrainDataMCFactory, state: State, step: Step) -> Score:
    # ループからの離脱
    if step > LIMIT: return 0

    # 終了判定
    finish = state.get_finish()
    if finish != Finish.NOT: 
        winner = check_winner(finish, step)
        if winner == Winner.ME: return 1
        else: return -1

    # 再帰
    next_states = state.get_next_states()
    next_state = pick_state_randomly(next_states)
    score = run(factory, next_state, step + 1)

    # フィードバック
    factory.data_add(state, score)
    return score * -0.9
