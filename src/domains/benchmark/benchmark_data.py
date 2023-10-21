from typing import List, Union
from src.consts.domain import Key, Score
from src.domains.abstract.evaluator import Evaluator
from src.domains.benchmark.benchmark_result import BenchmarkResult
from src.domains.shogi.shogi_state import ShogiState

class BenchmarkData:
    def __init__(self, x: Key, ys: List[Key]):
        self.x = x
        self.ys = ys
        self.answer: Union[Key, None] = None

    def check(self, evaluator: Evaluator) -> BenchmarkResult:
        states = ShogiState.from_key(self.x).get_next_states()
        answer = max(states, key=lambda state: -1 * self.evaluate(state.get_unique_key(), evaluator)).get_unique_key()
        return BenchmarkResult(self.x, answer, self.ys, answer in self.ys)

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
