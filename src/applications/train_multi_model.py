from src.domains.runner.train_data_strategy_factory_runner import TrainDataStrategyFactoryRunner
from src.domains.shogi.shogi_state import ShogiState

LIMIT = 100
base_key = '060820021000000012'
target_key = '000600773010012000'

def train_multi_model(trial: int, seed: int, filename: str, model_name: str):
    runner = TrainDataStrategyFactoryRunner.create_with_model(model_name)
    runner.set_seed(seed)
    for _ in range(trial):
        runner.run(ShogiState.from_key(base_key), 0)
    train_data = runner.get_factory().create()
    print(f"試合回数: {trial}")
    print(f"総出現局面数: {train_data.get_size()}")
    print(f"2回以上出現した局面数: {train_data.get_except_one_appearance_size()}")
    print(f"予測回数: {train_data.get_predicted_count()}")
    print(f"正解局面到達数: {train_data.search_appearance_count(target_key)}")
    train_data.save(filename)
