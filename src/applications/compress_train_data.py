from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def compress_train_data(read_filename: str = 'default', new_filename: str = 'default'):
    train_data = TrainDataFileFactory(read_filename).create()
    compressed_train_data =  train_data.compress()
    compressed_train_data.save(new_filename)
