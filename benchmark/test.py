from src.domains.model.model import Model

from src.domains.benchmark.benchmark import Benchmark

def test():
    benchmark = Benchmark()
    result = benchmark.test()
    if result:
        print("ベンチマークは可能手のみ存在している")
    else:
        print("ベンチマークに不可能な手が存在している")

if __name__ == "__main__":
    test()
