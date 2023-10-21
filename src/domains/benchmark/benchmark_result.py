from typing import List
from src.consts.domain import Key
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.gif import Gif
from src.domains.shogi.visualizers.image import Image
from src.domains.shogi.visualizers.image_visualizer import ImageVisualizer

class BenchmarkResult:
    def __init__(self, x: Key, answer: Key, ys: List[Key], succeeded: bool) -> None:
        self.x = x
        self.answer = answer
        self.ys = ys
        self.succeeded = succeeded

    def is_succeeded(self) -> bool:
        return self.succeeded
    
    def show(self) -> None:
        images = [self._get_image(self.x), self._get_image(self.answer, True), self._get_image(self.ys[0], True)]
        gif = Gif(images)
        gif.show()

    def _get_image(self, key: Key, should_turn: bool = False) -> Image:
        state = ShogiState.from_key(key)
        return ImageVisualizer(state, should_turn).visualize()
