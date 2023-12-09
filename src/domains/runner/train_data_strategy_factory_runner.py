import numpy as np
from src.consts.application import DRAW_LIMIT, Step
from src.consts.domain import Finish, Score
from src.domains.abstract.calc_score_strategy import CalcScoreStrategy
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State
from src.domains.calc_score_strategy.sarsa_calc_score_strategy import SarsaCalcScoreStrategy
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.pick_state_strategy.pick_state_randomly_strategy import PickStateRandomlyStrategy
from src.domains.pick_state_strategy.pick_state_softmax_strategy import PickStateSoftmaxStrategy
from src.domains.train_data.train_data_strategy_factory import TrainDataStrategyFactory

# TrainDataのFactoryを保持しているRunner
class TrainDataStrategyFactoryRunner():
    # モデルを利用してSoftmax + UCBのRunnerを作成する
    @staticmethod
    def create_with_model(model_filename: str, use_ucb: bool = True) -> 'TrainDataStrategyFactoryRunner':
        model = ModelFileFactory(model_filename).create()
        pick_state_strategy = PickStateSoftmaxStrategy(ModelEvaluator(model), use_ucb)
        calc_score_strategy = SarsaCalcScoreStrategy()
        return TrainDataStrategyFactoryRunner(pick_state_strategy, calc_score_strategy)
    
    # MCTsによるランダム試行のRunnerを作成する
    @staticmethod
    def create_mcts() -> 'TrainDataStrategyFactoryRunner':
        pick_state_strategy = PickStateRandomlyStrategy()
        calc_score_strategy = SarsaCalcScoreStrategy()
        return TrainDataStrategyFactoryRunner(pick_state_strategy, calc_score_strategy)

    def __init__(self, pick_state_strategy: PickStateStrategy, calc_score_strategy: CalcScoreStrategy):
        self.factory = TrainDataStrategyFactory(pick_state_strategy)
        self.calc_score_strategy = calc_score_strategy

    def set_seed(self, seed: int) -> None:
        np.random.seed(seed)

    def run(self, state: State) -> None:
        self._run(state, 0)
    
    def _run(self, state: State, step: Step) -> Score:
            # ループからの離脱
        if step > DRAW_LIMIT: return 0

        # 終了判定
        finish = state.get_finish()
        if finish == Finish.WIN:
            score = 1
            self.factory.data_add(state, score)
            return score
        elif finish == Finish.LOSE:
            score = -1
            self.factory.data_add(state, score)
            return score

        # 再帰
        next_states = state.get_next_states()
        next_state = self.factory.pick_state(state, next_states)

        before_score = self._run(next_state, step + 1)
        score = self.calc_score_strategy.calc_score(state, before_score)

        # フィードバック
        self.factory.data_add(state, score)
        return score
    
    def get_factory(self) -> TrainDataStrategyFactory:
        return self.factory
