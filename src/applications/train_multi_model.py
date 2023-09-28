import numpy as np
from src.domains.abstract.state import State
from src.consts.domain import Finish, Score
from src.consts.application import Step
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.shogi.shogi_state import ShogiState
from src.domains.train_data.train_data_model_factory import TrainDataModelFactory

LIMIT = 100

def train_multi_model(trial: int, seed: str, filename: str, model_name: str):
    np.random.seed(seed)
    model = ModelFileFactory(model_name).create()
    factory = TrainDataModelFactory(model)
    for _ in range(trial):
        run(factory, ShogiState.create_initial(), 0)
    train_data = factory.create()
    print(train_data)
    train_data.save(filename)


def run(factory: TrainDataModelFactory, state: State, step: Step) -> Score:
    # ループからの離脱
    if step > LIMIT: return 0

    # 終了判定
    finish = state.get_finish()
    if finish == Finish.WIN:
        score = 1
        factory.data_add(state, score)
        return score
    elif finish == Finish.LOSE:
        score = -1
        factory.data_add(state, score)
        return score

    # 再帰
    next_states = state.get_next_states()
    next_state = factory.pick_state(next_states)
    score = run(factory, next_state, step + 1) * -0.95

    # フィードバック
    factory.data_add(state, score)
    return score
