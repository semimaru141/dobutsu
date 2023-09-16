import itertools
from typing import List
import numpy as np
from src.consts.domain import *

def proccess_key(key: Key) -> List[int]:
    board_one_hots = map(lambda s: board_one_hot_encode(int(s) if s != 'a' else 10), key[:12])
    capture_one_hot = map(lambda c: capture_one_hot_encode(int(c)), key[12:])
    return list(itertools.chain.from_iterable(board_one_hots)) + list(itertools.chain.from_iterable(capture_one_hot))

'''
盤面の一つの値についてone-hotエンコードする
board_one_hot_encode(0) -> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
def board_one_hot_encode(value: int) -> List[int]:
    one_hot = np.zeros(SIZE_OF_BOARD_ONEHOT_VECTOR, dtype=np.float32)
    one_hot[value] = 1
    return one_hot

'''
持ち駒の一つの値についてone-hotエンコードする
capture_one_hot_encode(0) -> [1, 0, 0]
'''
def capture_one_hot_encode(value: int) -> List[int]:
    one_hot = np.zeros(SIZE_OF_CAPTURE_ONEHOT_VECTOR, dtype=np.float32)
    one_hot[value] = 1
    return one_hot

def key_to_state(key: Key) -> List[int]:
    return list(int(i) if i != 'a' else 10 for i in key)
