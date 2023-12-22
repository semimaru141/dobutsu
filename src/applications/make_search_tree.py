from src.domains.runner.serach_tree_runner import SearchTreeRunner
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.graph import Graph

base_key = '760900021000010011'

def make_search_tree(model_filename: str):
    runner = SearchTreeRunner.create_with_model(model_filename)
    runner.run(ShogiState.from_key(base_key), 3)
    node = runner.get_node()

    Graph(node).save('test.dot')
