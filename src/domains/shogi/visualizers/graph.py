import uuid
import math
from graphviz import Digraph
from src.consts.domain import Key

from src.domains.shogi.search_tree_node import SearchTreeNode
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

target_keys = [
    '760900021000010011',
    '000600704012011010',
    '706902001000010011',
    '000600704182011000'
]

class Graph():
    def __init__(self, node: SearchTreeNode):
        self.node = node
        self.graph = self.append_child(node)

    def append_child(self, node: SearchTreeNode):
        # グラフの初期化
        graph = Digraph('G', filename='sample.gv')
        self.add_node(graph, node, False)
        return graph

    def show(self):
        # グラフのレンダリングと保存
        self.graph.render(view=True)

    def save(self, filename):
        self.graph.save(filename)

    def add_node(self, graph: Digraph, node: SearchTreeNode, turn: bool) -> Key:
        state, pre_score, probability = node.get_all()
        # 先後で反転させる
        score = pre_score * -1 if turn else pre_score
        node_key = state.get_unique_key() + str(uuid.uuid4())
        s = StringVisualizer(state, turn).visualize() + f'\nscore: {score:.2f}\nprobability: {probability:.2f}'
        graph.node(node_key, s)

        for child in node.get_children():
            child_key = self.add_node(graph, child, not turn)
            if self.contain(child_key):
                graph.edge(node_key, child_key, penwidth=str(math.ceil(child.probability * 20)), color="red")
            else:
                graph.edge(node_key, child_key, penwidth=str(math.ceil(child.probability * 20)))

        return node_key
    
    def contain(self, key: Key):
        for target_key in target_keys:
            if key.startswith(target_key):
                return True
        return False
