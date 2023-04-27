from models.evaluator import Evaluator
import numpy as np

class FileHandler:
    def __init__(self, evaluator: Evaluator) -> None:
        self._evaluator = evaluator

    def save_model(self) -> None:
        np.savetxt('model', self._evaluator.model, fmt='%d')

    @property
    def evaluator(self) -> Evaluator:
        return self.evaluator