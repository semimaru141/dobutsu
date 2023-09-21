from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def show_train_data_distribution(filename: str = 'default', show_score: bool = True):
    train_data = TrainDataFileFactory(filename).create()
    if show_score:
        print(train_data.show_score_distribution())
    else:
        print(train_data.show_appearance_distribution())
