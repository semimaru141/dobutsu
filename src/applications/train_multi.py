from src.domains.runner.train_data_strategy_factory_runner import TrainDataStrategyFactoryRunner
from src.domains.shogi.shogi_state import ShogiState

def train_multi(trial: int, seed: int, filename: str):
    runner = TrainDataStrategyFactoryRunner.create_mcts()
    runner.set_seed(seed)
    for _ in range(trial):
        runner.run(ShogiState.create_initial(), 0)
    train_data = runner.get_factory().create()
    print(train_data)
    train_data.save(filename)
