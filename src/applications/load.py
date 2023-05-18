from domains.train_data.train_data_file_factory import TrainDataFileFactory


def load():
    train_data = TrainDataFileFactory()
    print(train_data._data)