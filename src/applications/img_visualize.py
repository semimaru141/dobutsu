from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.image_visualizer import ImageVisualizer

base_key = '067890040213012020'

def img_visualize():
    initial_state = ShogiState.from_key(base_key)
    ImageVisualizer(initial_state, False).visualize()
