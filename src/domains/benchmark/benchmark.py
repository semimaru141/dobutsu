from typing import List
import json
from src.consts.domain import Key
from src.domains.abstract.evaluator import Evaluator
from src.domains.benchmark.benchmark_data import BenchmarkData
from src.domains.shogi.shogi_state import ShogiState

class Benchmark():
    def __init__(self, evaluator: Evaluator, filename: str = 'default'):
        self.evaluator = evaluator
        self.data = self._read(filename)

    def _read(self, filename: str) -> List[BenchmarkData]:
        with open('benchmark/' + filename + '.json') as f:
            datas = json.load(f)['data']
            return [BenchmarkData(data['x'], data['y'], self.evaluator) for data in datas]
        
    def run(self) -> None:
        succeed = []
        failed = []
        for data in self.data:
            if data.check(self.evaluator):
                succeed.append(data)
            else:
                failed.append(data)
        print('succeed: ' + str(len(succeed)))
        print('failed: ' + str(len(failed)))
