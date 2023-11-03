from typing import Literal
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def compress_train_data(read_filename: str = 'default', new_filename: str = 'default', key: Literal['score', 'appearance'] = 'appearance'):
    train_data = TrainDataFileFactory(read_filename).create()
    if key == 'appearance':
        compressed_train_data =  train_data.compress_by_appearance()
    else:
        compressed_train_data = train_data.compress_by_score_abs()
    
    print(f"圧縮後局面数: {compressed_train_data.get_size()}")
    compressed_train_data.save(new_filename)
