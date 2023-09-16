from src.domains.train_data.train_data_file_factory import TrainDataFileFactory
from src.domains.train_data.train_data_merge_factory import TrainDataMergeFactory

FILE_NAMES = map(lambda x: 'dump_{}'.format('0' * (3 - len(str(x)))  + str(x)), range(1, 3))

def merge():
    train_datas = list(map(lambda filename: TrainDataFileFactory(filename).create(), FILE_NAMES))
    merged_train_data = TrainDataMergeFactory(train_datas).create()
    merged_train_data.save('dump_merged_001')
