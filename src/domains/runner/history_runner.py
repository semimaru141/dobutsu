import numpy as np
from typing import Union
from src.consts.application import DRAW_LIMIT, Step, Winner
from src.consts.domain import Finish, Score, SelectionProbability
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.shogi.history import History
from src.domains.strategy.pick_state_best_strategy import PickStateBestStrategy
from src.domains.strategy.pick_state_randomly_strategy import PickStateRandomlyStrategy
from src.domains.strategy.pick_state_softmax_strategy import PickStateSoftmaxStrategy

# 経由した盤面や経路等を把握しているRunner
class HistoryRunner():
    # モデルを利用してSoftmax + (UCB)のRunnerを作成する
    @staticmethod
    def create_with_model(model_filename: str, use_ucb: bool = False) -> 'HistoryRunner':
        model = ModelFileFactory(model_filename).create()
        strategy = PickStateSoftmaxStrategy(ModelEvaluator(model), use_ucb)
        return HistoryRunner(strategy)
    
    # MCTsによるランダム試行のRunnerを作成する
    @staticmethod
    def create_mcts() -> 'HistoryRunner':
        strategy = PickStateRandomlyStrategy()
        return HistoryRunner(strategy)
    
    # 最善を選択する
    @staticmethod
    def create_best(model_filename: str) -> 'HistoryRunner':
        model = ModelFileFactory(model_filename).create()
        strategy = PickStateBestStrategy(ModelEvaluator(model))
        return HistoryRunner(strategy)
    
    def set_seed(self, seed: int) -> None:
        np.random.seed(seed)

    def __init__(self, strategy: PickStateStrategy):
        self.history = History()
        self.strategy = strategy
        self.winner: Union[None, Winner] = None

    def run(self, state: State) -> None:
        self._run(state, 0, 1)
    
    def _run(self, state: State, step: Step, probability: SelectionProbability):
        # ループからの離脱
        if step > DRAW_LIMIT: return 0

        # 終了判定
        finish = state.get_finish()
        if finish == Finish.WIN:
            score = 1
            self.history.data_add(state, score, probability)
            winner = self.check_winner(finish, step)
            self.set_winner(winner)
            return score
        elif finish == Finish.LOSE:
            score = -1
            self.history.data_add(state, score, probability)
            winner = self.check_winner(finish, step)
            self.set_winner(winner)
            return score

        # 再帰
        next_states = state.get_next_states()
        next_state, score, new_probability = self.strategy.pick_state_verbose(state, next_states, {})
        self._run(next_state, step + 1, new_probability)

        # フィードバック
        self.history.data_add(state, score * -1, probability)
        return score
    
    def check_winner(self, finish: Finish, step: Step) -> Winner:
        add = 0 if finish == Finish.WIN else 1
        if (step + add) % 2 == 0: return Winner.ME
        else: return Winner.OP
        
    def get_history(self) -> History:
        return self.history
    
    def get_winner(self) -> Union[None, Winner]:
        return self.winner
    
    def set_winner(self, winner: Winner) -> None:
        self.winner = winner
