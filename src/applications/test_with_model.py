from src.domains.runner.history_runner import HistoryRunner
from src.domains.shogi.shogi_state import ShogiState
from src.consts.application import Winner

def test_with_model(model_filename: str):
    runner = HistoryRunner.create_best(model_filename)
    runner.run(ShogiState.create_initial())
    winner = runner.get_winner()
    history = runner.get_history()

    if winner == Winner.ME:
        print("me win")
    elif winner == Winner.OP:
        print("op win")
    else:
        print("draw")

    history.print()
