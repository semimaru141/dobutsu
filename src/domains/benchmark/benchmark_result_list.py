from typing import List
from src.domains.benchmark.benchmark_result import BenchmarkResult

class BenchmarkResultList:
    def __init__(self, key: str, results: List[BenchmarkResult]) -> None:
        self.key = key
        self.results = results

    def print(self) -> None:
        succeed_count = 0
        failed_count = 0
        for result in self.results:
            if result.is_succeeded():
                succeed_count += 1
            else:
                failed_count += 1
        print(self.key)
        print('succeed: ' + str(succeed_count))
        print('failed: ' + str(failed_count))

    def show_failed(self) -> None:
        for result in self.results:
            if result.is_succeeded():
                continue
            else:
                result.show()
