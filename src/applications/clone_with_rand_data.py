from src.domains.ready_data.ready_data import ReadyData
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def clone_with_rand_data(filename: str = 'default') -> None:
    train_data = TrainDataFileFactory(filename).create()
    ready_data = ReadyData.create_from_train_data(train_data)
    rand_data = ready_data.clone_with_rand_y()
    rand_data.save('rand_' + filename)
