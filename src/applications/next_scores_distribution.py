from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.pick_state_strategy.pick_state_best_strategy import PickStateBestStrategy
from src.domains.shogi.shogi_state import ShogiState

base_key = '600702989010010000'

def next_scores_distribution(filename: str):
    evaluator = ModelEvaluator(ModelFileFactory(filename).create())
    state = ShogiState.from_key(base_key)
    next_states = state.get_next_states()
    datas = PickStateBestStrategy(evaluator).get_all_verbose(state, next_states, {})
    for _, score, _ in datas:
        print(f"{-1 * score}")