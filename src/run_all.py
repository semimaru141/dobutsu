import argparse
from typing import Tuple
from src.applications.compress_train_data import compress_train_data
from src.applications.format_data import format_data
from src.applications.make_model import make_model
from src.applications.train_multi_model import train_multi_model

def get_args() -> Tuple[int, int, str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('trial', type=int)
    parser.add_argument('seed', type=int)
    parser.add_argument('filename', type=str)
    parser.add_argument('model_name', type=str)

    args = parser.parse_args()
    return args.trial, args.seed, args.filename, args.model_name

if __name__ == "__main__":
    trial, seed, filename, model_name = get_args()
    compressed_filename = filename + '_compressed'
    train_multi_model(trial, seed, filename, model_name)
    compress_train_data(filename, compressed_filename)
    format_data(compressed_filename, filename)
    make_model(filename, filename, model_name)
