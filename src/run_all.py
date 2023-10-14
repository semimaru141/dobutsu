import argparse
from typing import Tuple, Union
from src.applications.compress_train_data import compress_train_data
from src.applications.format_data import format_data
from src.applications.make_model import make_model
from src.applications.merge_train_data import merge_train_data
from src.applications.train_multi import train_multi
from src.applications.train_multi_model import train_multi_model

def get_args() -> Tuple[int, int, str, Union[str, None]]:
    parser = argparse.ArgumentParser()
    parser.add_argument('trial', type=int)
    parser.add_argument('seed', type=int)
    parser.add_argument('filename', type=str)
    parser.add_argument('--model_name', type=str, )

    args = parser.parse_args()
    return args.trial, args.seed, args.filename, args.model_name

def run_mcts(trial: int, seed: int, filename: str):
    compressed_filename = filename + '_merged'
    train_multi(trial, seed, filename)
    compress_train_data(filename, compressed_filename)
    format_data(compressed_filename, filename)
    make_model(filename, filename)

def run_model(trial: int, seed: int, filename: str, model_name: str):
    compressed_filename = filename + '_compressed'
    merged_filename = filename + '_merged'
    pre_merged_filaname = model_name + '_merged'

    train_multi_model(trial, seed, filename, model_name)
    compress_train_data(filename, compressed_filename)
    merge_train_data([compressed_filename, pre_merged_filaname], merged_filename)
    format_data(merged_filename, filename)
    make_model(filename, filename)

if __name__ == "__main__":
    trial, seed, filename, model_name = get_args()
    if model_name == None:
        run_mcts(trial, seed, filename)
    else:
        run_model(trial, seed, filename, model_name)
