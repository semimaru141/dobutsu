from src.consts.domain import Key
from src.domains.abstract.evaluator import Evaluator
from src.domains.shogi.shogi_state import ShogiState


class BenchmarkData:
    def __init__(self, x: Key, y: Key):
        self.x = x
        self.y = y

    def check(self, evaluator: Evaluator) -> bool:
        states = ShogiState.from_key(self.x).get_next_states()
        state = max(states, key=lambda state: self.evaluate(state.get_unique_key(), evaluator))
        return state.get_unique_key() == self.y

    def evaluate(self, key: Key, evaluator: Evaluator):
        return evaluator.search_score(key)
