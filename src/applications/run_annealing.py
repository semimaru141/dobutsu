from src.domains.runner.annealing_runner import AnnealingRunner
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

TRIAL = 5000
key = '807090040213000000'

def run_annealing(model_name: str):
    runner = AnnealingRunner.create_with_model(model_name)
    state = runner.run(ShogiState.from_key(key), TRIAL)

    str = StringVisualizer(state, False).visualize()
    print(str)

    scores = runner.get_scores()
    print(scores)
