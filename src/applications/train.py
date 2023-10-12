from src.domains.runner.train_data_strategy_factory_runner import TrainDataStrategyFactoryRunner
from src.domains.shogi.shogi_state import ShogiState

TRIAL = 1000

def train():
    runner = TrainDataStrategyFactoryRunner.create_mcts()
    for _ in range(TRIAL):
        runner.run(ShogiState.create_initial(), 0)
    train_data = runner.get_factory().create()
    print(train_data)
    train_data.save()
