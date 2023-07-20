from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.benchmark.benchmark import Benchmark

def evaluate():
    evaluator = ModelEvaluator()
    benchmark = Benchmark(evaluator)
    benchmark.run()
