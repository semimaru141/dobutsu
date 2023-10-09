from typing import List
import json
from src.domains.abstract.evaluator import Evaluator
from src.domains.benchmark.benchmark_data import BenchmarkData
from src.domains.benchmark.benchmark_result import BenchmarkResult
from src.domains.shogi.shogi_state import ShogiState

DATA = "data"
CHECKMATE = "詰み"
ONE_STEP = "1手詰め"
BENCHMARK_KEYS = [CHECKMATE, ONE_STEP]
X = "x"
YS = "ys"

class Benchmark():
    def __init__(self, evaluator: Evaluator, filename: str = 'default'):
        self.evaluator = evaluator
        self.data = self._read(filename)

    def _read(self, filename: str) -> List[BenchmarkData]:
        with open('benchmark/' + filename + '.json') as f:
            datas = json.load(f)['data']

            benchmark_datas = []
            for key in BENCHMARK_KEYS:
                benchmark_datas += [BenchmarkData(data[X], data[YS]) for data in datas[key]]
            return benchmark_datas
        
    def run(self) -> BenchmarkResult:
        succeed: List[BenchmarkData] = []
        failed: List[BenchmarkData] = []
        for data in self.data:
            if data.check(self.evaluator):
                succeed.append(data)
            else:
                failed.append(data)
        return BenchmarkResult(succeed, failed)
