from models.board import State

Score = float

class Evaluator:
    _evaluator = []

    def __init__(self) -> None:
        pass

    @staticmethod
    def create_rand() -> 'Evaluator':
        return Evaluator()
    
    @staticmethod
    def create_from_arg() -> 'Evaluator':
        return Evaluator()

    def learn(self, state: State, score: Score) -> None:
        self._evaluator[state] += score

    # stateの評価値を計算する
    def evaluate(self, state: State) -> int:
        return self._evaluator[state]
