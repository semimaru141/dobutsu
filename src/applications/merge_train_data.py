import time
from typing import List
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory
from src.domains.train_data.train_data_merge_factory import TrainDataMergeFactory

def merge_train_data(target_filenames: List[str], output_filename):
    print(f"データ結合開始 現在時刻: {time.time()}")
    train_datas = list(map(lambda filename: TrainDataFileFactory(filename).create(), target_filenames))
    merged_train_data = TrainDataMergeFactory(train_datas).create()
    print(f"結合後局面数: {merged_train_data.get_size()}")
    merged_train_data.save(output_filename)
    print(f"データ結合終了 現在時刻: {time.time()}")
