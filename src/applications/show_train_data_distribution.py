from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def show_train_data_distribution(filename: str = 'default'):
    train_data = TrainDataFileFactory(filename).create()
    print(train_data.show_appearance_distribution())
