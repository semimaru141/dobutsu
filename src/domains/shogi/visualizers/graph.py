import uuid
from graphviz import Digraph
from src.consts.domain import Key

from src.domains.shogi.search_tree_node import SearchTreeNode
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

class Graph():
    def __init__(self, node: SearchTreeNode):
        self.node = node

    def show(self):
        # グラフの初期化
        graph = Digraph('G', filename='sample.gv')
        self.add_node(graph, self.node, False)

        # グラフのレンダリングと保存
        graph.render(view=True)

    def add_node(self, graph: Digraph, node: SearchTreeNode, turn: bool) -> Key:
        state, pre_score, probability = node.get_all()
        # 先後で反転させる
        score = pre_score * -1 if turn else pre_score
        node_key = state.get_unique_key() + str(uuid.uuid4())
        s = StringVisualizer(state, turn).visualize() + f'\nscore: {score:.2f}\nprobability: {probability:.2f}'
        graph.node(node_key, s)

        for child in node.get_children():
            child_key = self.add_node(graph, child, not turn)
            graph.edge(node_key, child_key)

        return node_key

