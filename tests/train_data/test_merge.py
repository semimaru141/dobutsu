
from src.domains.train_data.train_data import TrainData
from src.domains.train_data.train_data_merge_factory import TrainDataMergeFactory


class TestMerge:
    # 初期状態
    def test_merge1(self):
        key = '867090040213000000'
        train_data1 = TrainData({
            key: [
                0.2,
                1
            ]
        })
        train_data2 = TrainData({
            key: [
                0.5,
                2
            ]
        })
        merged = TrainDataMergeFactory([train_data1, train_data2]).create()
        assert abs(merged.search_score(key) - 0.4) < 1e-9
        assert merged.search_appearance_count(key) == 3

    def test_merge2(self):
        key0 = '867090040213000000'
        key1 = '067890040213000000'
        key2 = '867090043210000000'
        train_data1 = TrainData({
            key0: [
                0.2,
                1
            ],
            key1: [
                0.5,
                1
            ]
        })
        train_data2 = TrainData({
            key0: [
                0.5,
                2
            ],
            key2: [
                0.2,
                3
            ]
        })
        merged = TrainDataMergeFactory([train_data1, train_data2]).create()
        assert len(merged.get_size()) == 3

