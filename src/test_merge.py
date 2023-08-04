from src.domains.train_data.train_data_merge_factory import TrainDataMergeFactory

FILE_NAMES = list(map(lambda x: 'dump_{}.pkl'.format('0' * (3 - len(str(x)))  + str(x)), range(1, 3)))

if __name__ == '__main__':
    factory = TrainDataMergeFactory()
    factory.merge(FILE_NAMES)
