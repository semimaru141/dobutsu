from src.consts.domain import Score
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer
from src.domains.train_data.train_data_evaluator import TrainDataEvaluator
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory


def load(filename = 'default'):
    train_data = TrainDataFileFactory(filename).create()
    evaluator = TrainDataEvaluator(train_data)

    initial_state = get_initial()
    key = initial_state.get_unique_key()
    score = evaluator.search_score(key)
    show_score(score, initial_state, False)

    states = initial_state.get_next_states()
    for state in states:
        key = state.get_unique_key()
        score = evaluator.search_score(key)
        show_score(score, state, False)
    
def get_initial():
    board = [0, 0, 7, 8, 9, 6, 0, 4, 3, 2, 0, 1]
    captured = [0, 0, 0, 0, 0, 0]
    return ShogiState.create(board, captured)

def show_score(score: Score, state: ShogiState, should_turn: bool):
    print(StringVisualizer(state, should_turn).visualize())
    print(f'score: {score}')
