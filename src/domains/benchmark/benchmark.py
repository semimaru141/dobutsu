from typing import Dict, List
import json
from src.domains.abstract.evaluator import Evaluator
from src.domains.benchmark.benchmark_data import BenchmarkData
from src.domains.benchmark.benchmark_result import BenchmarkResult
from src.domains.shogi.shogi_state import ShogiState

DATA = "data"
CHECKMATE = "詰み"
ONE_STEP = "1手詰め"
THREE_STEP = "3手詰め"
FIVE_STEP = "5手詰め"
BENCHMARK_KEYS = [CHECKMATE, ONE_STEP, THREE_STEP, FIVE_STEP]
X = "x"
YS = "ys"

BenchDic = Dict[str, List[BenchmarkData]]

class Benchmark():
    def __init__(self, filename: str = 'default'):
        self.data = self._read(filename)

    def _read(self, filename: str) -> BenchDic:
        with open('benchmark/' + filename + '.json') as f:
            datas = json.load(f)['data']

            benchmark_datas: BenchDic = {}
            for key in BENCHMARK_KEYS:
                benchmark_datas[key] = [BenchmarkData(data[X], data[YS]) for data in datas[key]]
            return benchmark_datas
    
    def test(self) -> bool:
        for key, datas in self.data.items():
            for data in datas:
                if data.test():
                    continue
                else:
                    print(f"「{key}」にて、以下の回答に誤りがある")
                    data.print()
                    return False
        return True
        
    def run(self, evaluator: Evaluator) -> Dict[str, BenchmarkResult]:
        dic: Dict[str, BenchmarkResult] = {}
        for key, datas in self.data.items():
            succeed: List[BenchmarkData] = []
            failed: List[BenchmarkData] = []
            for data in datas:
                if data.check(evaluator):
                    succeed.append(data)
                else:
                    failed.append(data)
            dic[key] = BenchmarkResult(succeed, failed)
        return dic
