import numpy as np
from src.consts.domain import Score
from src.domains.model.model_evaluator import ModelEvaluator
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.shogi.shogi_state import ShogiState
from src.domains.shogi.visualizers.image_visualizer import ImageVisualizer
from src.domains.shogi.visualizers.string_visualizer import StringVisualizer

t = "5"
v = "221"
target_name = 'heatmap_hen3'
# f'060000000010000{v}',
keys = [
    [
        f'{t}06000000010000{v}',
        f'0{t}6000000010000{v}',
        None
    ],
    [
        f'006{t}00000010000{v}',
        f'0060{t}0000010000{v}',
        f'00600{t}000010000{v}',
    ],
    [
        f'006000{t}00010000{v}',
        f'0060000{t}0010000{v}',
        f'00600000{t}010000{v}',
    ],
    [   f'006000000{t}10000{v}',
        None,
        f'00600000001{t}000{v}',
    ]
]

def read_model(filename: str = 'default'):
    factory = ModelFileFactory(filename)
    model = factory.create()
    evaluator = ModelEvaluator(model)

    func = lambda key: evaluator.search_score(key) if key != None else np.nan
    f = np.vectorize(func)
    a = f(np.array(keys))
    np.save(target_name, a)
    print(a)
    