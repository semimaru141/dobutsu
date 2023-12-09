from src.consts.domain import DISCOUNT_RATE, Score
from src.domains.abstract.calc_score_strategy import CalcScoreStrategy
from src.domains.abstract.evaluator import Evaluator
from src.domains.abstract.state import State

# Q学習の計算式を実装したクラス
# 次の局面の最大のスコアに割引率をかけた値をその局面のスコアとする
class QCalcScoreStrategy(CalcScoreStrategy):
    # 検索の効率化のため、runnerと同じevaluatorを使用することを推奨
    def __init__(self, evaluator: Evaluator, gamma: float = DISCOUNT_RATE):
        self.evaluator = evaluator
        super().__init__(gamma)

    def calc_score(self, state: State, _before_score: Score) -> Score:
        next_states = state.get_next_states()
        # 反転させているため、最大値を最小値として扱う
        min_score = min([self.evaluator.search_score(state.get_unique_key()) for state in next_states])
        return min_score * self.gamma
