from typing import List
from src.consts.domain import Key, Score
from src.domains.abstract.evaluator import Evaluator
from src.domains.shogi.shogi_state import ShogiState


class BenchmarkData:
    def __init__(self, x: Key, ys: List[Key]):
        self.x = x
        self.ys = ys

    def check(self, evaluator: Evaluator) -> bool:
        states = ShogiState.from_key(self.x).get_next_states()
        state = max(states, key=lambda state: -1 * self.evaluate(state.get_unique_key(), evaluator))
        for y in self.ys:
            if y == state.get_unique_key():
                return True
        return False

    def test(self) -> bool:
        keys = [state.get_unique_key() for state in ShogiState.from_key(self.x).get_next_states()]
        for y_key in self.ys:
            if y_key in keys:
                continue
            else:
                return False
        return True

    def evaluate(self, key: Key, evaluator: Evaluator) -> Score:
        return evaluator.search_score(key)
    
    def print(self) -> None:
        print(f"x_key: {self.x}")
