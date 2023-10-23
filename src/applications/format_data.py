import time
from src.domains.ready_data.ready_data import ReadyData
from src.domains.train_data.train_data_file_factory import TrainDataFileFactory

def format_data(read_filename: str = 'default', output_filename = 'default') -> None:
    print(f"フォーマット開始 現在時刻: {time.time()}")
    train_data = TrainDataFileFactory(read_filename).create()
    ready_data = ReadyData.create_from_train_data(train_data)
    ready_data.save(output_filename)
    print(f"フォーマット終了 現在時刻: {time.time()}")
