from typing import List
from src.domains.benchmark.benchmark_data import BenchmarkData

class BenchmarkResult:
    def __init__(self, succeed_datas: List[BenchmarkData], failed_datas: List[BenchmarkData]) -> None:
        self.succeed_datas = succeed_datas
        self.failed_datas = failed_datas

    def print(self):
        print('succeed: ' + str(len(self.succeed_datas)))
        print('failed: ' + str(len(self.failed_datas)))
