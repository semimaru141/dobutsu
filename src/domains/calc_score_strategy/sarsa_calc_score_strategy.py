from src.consts.domain import DISCOUNT_RATE, Score
from src.domains.abstract.calc_score_strategy import CalcScoreStrategy
from src.domains.abstract.state import State

# Sarsaの計算式を実装したクラス
# 選択した行動に割引率をかけた値をその局面のスコアとする
class SarsaCalcScoreStrategy(CalcScoreStrategy):
    def __init__(self, gamma: float = DISCOUNT_RATE):
        super().__init__(gamma)

    def calc_score(self, _state: State, before_score: Score) -> Score:
        return before_score * self.gamma
