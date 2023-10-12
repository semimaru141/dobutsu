from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.image_visualizer import ImageVisualizer

# base_key = '000070673010012000'
base_key = '005800180206100001'

def img_visualize():
    initial_state = ShogiState.from_key(base_key)
    print(initial_state.get_unique_key())
    image = ImageVisualizer(initial_state, False).visualize()
    image.show()
