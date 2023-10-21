from src.domains.runner.serach_tree_runner import SearchTreeRunner
from src.domains.shogi.shogi_state import ShogiState

def make_search_tree(model_filename: str):
    runner = SearchTreeRunner.create_best(model_filename)
    runner.run(ShogiState.create_initial(), 3)
    node = runner.get_node()

    print(node)
