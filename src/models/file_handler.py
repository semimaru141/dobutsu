from models.evaluator import Evaluator
import numpy as np

class FileHandler:
    def __init__(self, evaluator: Evaluator) -> None:
        self._evaluator = evaluator

    def save_model(self, filename: str) -> None:
        np.save(filename, self._evaluator.model)

    @property
    def evaluator(self) -> Evaluator:
        return self.evaluator