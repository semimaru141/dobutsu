import itertools
from typing import List
import numpy as np
from src.consts.domain import *

def proccess_key(key: Key) -> List[int]:
    one_hots = map(lambda s: one_hot_encode(int(s) if s != 'a' else 10), key[:12])
    return list(itertools.chain.from_iterable(one_hots))

def one_hot_encode(value: int) -> List[int]:
    one_hot = np.zeros(SIZE_OF_ONEHOT_VECTOR, dtype=np.float32)
    one_hot[value] = 1
    return one_hot

def key_to_state(key: Key) -> List[int]:
    return list(int(i) if i != 'a' else 10 for i in key)
