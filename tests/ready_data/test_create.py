import numpy as np
from src.domains.ready_data.ready_data import ReadyData
from src.domains.train_data.train_data import TrainData
from src.utils.key_handler import board_one_hot_encode, capture_one_hot_encode, proccess_key

key = '867090040213100020'
answer = [
    0,0,0,0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,1,0,
    1,0,0,0,0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,1,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,1,0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,0,0,0,0,
    0,1,0,
    1,0,0,
    1,0,0,
    1,0,0,
    0,0,1,
    1,0,0,
]

a_key = '8670a0040213000000'
a_answer = [
    0,0,0,0,0,0,0,0,1,0,0,
    0,0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,0,0,0,1,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,1,0,0,0,0,0,0,
    1,0,0,0,0,0,0,0,0,0,0,
    0,0,1,0,0,0,0,0,0,0,0,
    0,1,0,0,0,0,0,0,0,0,0,
    0,0,0,1,0,0,0,0,0,0,0,
    1,0,0,
    1,0,0,
    1,0,0,
    1,0,0,
    1,0,0,
    1,0,0,
]

class TestCreate:
    def test_board_one_hot(self):
        assert np.allclose(board_one_hot_encode(4), [0,0,0,0,1,0,0,0,0,0,0])

    def test_capture_one_hot(self):
        assert np.allclose(capture_one_hot_encode(2), [0,0,1])

    def test_proccess_key(self):
        one_hot_chain = proccess_key(key)
        assert np.allclose(one_hot_chain, answer)

    def test_create_ready(self):
        train_data = TrainData({
            a_key: [0.5, 3]
        })
        ready_data = ReadyData.create_from_train_data(train_data)
        assert np.allclose(ready_data.x, [a_answer])
        assert np.allclose(ready_data.y, [0.5])
