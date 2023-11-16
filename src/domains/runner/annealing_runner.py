from typing import List
import numpy as np
from src.consts.domain import ANNEALING_SCALRE
from src.domains.abstract.state import State
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.strategy.pick_state_softmax_strategy import PickStateSoftmaxStrategy

class AnnealingRunner():
    def __init__(self, strategy: PickStateSoftmaxStrategy):
        self.strategy = strategy
        self.scores: List[float] = []

    # モデルを利用してSoftmax + (UCB)のRunnerを作成する
    @staticmethod
    def create_with_model(model_filename: str, use_ucb: bool = False) -> 'AnnealingRunner':
        model = ModelFileFactory(model_filename).create()
        strategy = PickStateSoftmaxStrategy(ModelEvaluator(model), use_ucb)
        return AnnealingRunner(strategy)
    
    def run(self, state: State, trial: int):
        initial_temperature_exp = 1.0
        return self._run(state, initial_temperature_exp, trial)

    def _run(self, state: State, temperature_exp: float, trial: int):
        if trial <= 0:
            return state
        
        temperature = np.log(temperature_exp)
        self.strategy.set_temperature(temperature)
        next_states = state.get_all_possible_states()
        next_state, score, _ = self.strategy.pick_state_verbose(state, next_states, {})
        
        self.scores.append(score)
        return self._run(next_state, temperature_exp + ANNEALING_SCALRE, trial - 1)
    
    def get_scores(self) -> List[float]:
        return self.scores
