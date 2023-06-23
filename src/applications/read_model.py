from src.consts.domain import Score
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

base_key = '067890040213000000'

def read_model(filename: str = 'default'):
    factory = ModelFileFactory(filename)
    model = factory.create()
    evaluator = ModelEvaluator(model)

    initial_state = ShogiState.from_key(base_key)
    key = initial_state.get_unique_key()
    score = evaluator.search_score(key)
    show_score(score, initial_state, False)

    states = initial_state.get_next_states()
    for state in states:
        key = state.get_unique_key()
        score = evaluator.search_score(key)
        show_score(score, state, False)

def show_score(score: Score, state: ShogiState, should_turn: bool):
    print(StringVisualizer(state, should_turn).visualize())
    print(f'score: {score}')
