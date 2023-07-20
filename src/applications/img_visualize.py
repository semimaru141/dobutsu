from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.image_visualizer import ImageVisualizer

base_key = '060820021000000011'

def img_visualize():
    initial_state = ShogiState.from_key(base_key)
    image = ImageVisualizer(initial_state, False).visualize()
    image.show()
