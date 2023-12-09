import time
from typing import Literal, Union
from src.consts.domain import DISCOUNT_RATE
from src.domains.runner.train_data_strategy_factory_runner import TrainDataStrategyFactoryRunner
from src.domains.shogi.shogi_state import ShogiState

def train_multi_model(trial: int, seed: int, filename: str, model_name: str, gamma: float = DISCOUNT_RATE, algorithm: Literal["q", "sarsa"] = "sarsa"):
    print(f"トレーニング開始 現在時刻: {time.time()}")
    print(f"モデル名: {model_name}")
    print(f"割引率: {gamma}")
    print(f"アルゴリズム: {algorithm}")
    if algorithm == "q":
        runner = TrainDataStrategyFactoryRunner.create_q_learning(model_name, gamma)
    else:
        runner = TrainDataStrategyFactoryRunner.create_with_model(model_name, False, gamma)
    runner.set_seed(seed)
    for _ in range(trial):
        runner.run(ShogiState.create_initial())
    train_data = runner.get_factory().create()
    print(f"試合回数: {trial}")
    print(f"総出現局面数: {train_data.get_size()}")
    print(f"2回以上出現した局面数: {train_data.get_except_one_appearance_size()}")
    print(f"予測回数: {train_data.get_predicted_count()}")
    print(f"トレーニング終了 現在時刻: {time.time()}")
    # print(f"正解局面到達数: {train_data.search_appearance_count(target_key)}")
    train_data.save(filename)
