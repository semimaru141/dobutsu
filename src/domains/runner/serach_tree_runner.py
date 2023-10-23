import numpy as np
from typing import Union
from src.consts.application import Deps
from src.consts.domain import Finish
from src.domains.abstract.pick_state_strategy import PickStateStrategy
from src.domains.abstract.state import State
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.shogi.search_tree_node import SearchTreeNode
from src.domains.strategy.pick_state_best_strategy import PickStateBestStrategy
from src.domains.strategy.pick_state_randomly_strategy import PickStateRandomlyStrategy
from src.domains.strategy.pick_state_softmax_strategy import PickStateSoftmaxStrategy

# 探索を行う木の作成
class SearchTreeRunner():
    # モデルを利用してSoftmax + (UCB)のRunnerを作成する
    @staticmethod
    def create_with_model(model_filename: str, use_ucb: bool = False) -> 'SearchTreeRunner':
        model = ModelFileFactory(model_filename).create()
        strategy = PickStateSoftmaxStrategy(ModelEvaluator(model), use_ucb)
        return SearchTreeRunner(strategy)
    
    # MCTsによるランダム試行のRunnerを作成する
    @staticmethod
    def create_mcts() -> 'SearchTreeRunner':
        strategy = PickStateRandomlyStrategy()
        return SearchTreeRunner(strategy)
    
    # 最善を選択する(実質的にmctsと同じになる)
    @staticmethod
    def create_best(model_filename: str) -> 'SearchTreeRunner':
        model = ModelFileFactory(model_filename).create()
        strategy = PickStateBestStrategy(ModelEvaluator(model))
        return SearchTreeRunner(strategy)
    
    def set_seed(self, seed: int) -> None:
        np.random.seed(seed)

    def __init__(self, strategy: PickStateStrategy):
        self.strategy = strategy
        self.node: Union[None, SearchTreeNode] = None

    def run(self, state: State, deps: Deps):
        node = SearchTreeNode(state, 0, 1)
        self._run(node, deps)
        self.node = node

    # 深さ優先探索
    def _run(self, node: SearchTreeNode, deps: Deps):
        # ループからの離脱
        if deps < 1:
            return

        state = node.get_state()
        # 終了判定
        finish = state.get_finish()
        if finish != Finish.NOT:
            return

        # 再帰
        next_states = state.get_next_states()
        datas = self.strategy.get_all_verbose(state, next_states, {})
        for (next_state, score, new_probability) in datas:
            node.data_add(next_state, score, new_probability)
        
        nodes = node.get_children()
        for new_node in nodes:
            self._run(new_node, deps - 1)

    def get_node(self) -> SearchTreeNode:
        return self.node
