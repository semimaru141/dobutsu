from typing import List, Tuple
from src.consts.domain import Score
from src.domains.shogi.const import Step
from src.domains.shogi.shogi_state import ShogiState

class History:
    def __init__(self) -> None:
        self.list: List[Tuple[ShogiState, Step, Score]] = []

    def data_add(self, data: Tuple[ShogiState, Step, Score]) -> None:
        self.list.append(data)

    def __iter__(self) -> 'History':
        return self
    
    def __next__(self) -> Tuple[ShogiState, Step, Score]:
        if len(self.list) > 0:
            return self.list.pop(0)
        else:
            raise StopIteration
