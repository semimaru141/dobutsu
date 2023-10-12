from typing import List
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory
from src.domains.train_data.train_data_merge_factory import TrainDataMergeFactory

def merge_train_data(target_filenames: List[str], output_filename):
    train_datas = list(map(lambda filename: TrainDataFileFactory(filename).create(), target_filenames))
    merged_train_data = TrainDataMergeFactory(train_datas).create()
    merged_train_data.save(output_filename)
