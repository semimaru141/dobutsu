import argparse

from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.benchmark.benchmark import Benchmark
from src.domains.model.model_file_factory import ModelFileFactory

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    return args.filename

def evaluate():
    filename = get_args()
    model = ModelFileFactory(filename).create()
    evaluator = ModelEvaluator(model)
    benchmark = Benchmark()
    result_lists = benchmark.run(evaluator)

    for result_list in result_lists:
        result_list.print()
        result_list.show_failed()

if __name__ == "__main__":
    evaluate()
