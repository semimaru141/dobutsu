import argparse
from src.applications.compress_train_data import compress_train_data
from src.applications.format_data import format_data
from src.applications.make_model import make_model

from src.applications.merge_train_data import merge_train_data

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('basename', type=str)
    parser.add_argument('before_name', type=str)

    args = parser.parse_args()
    return args.basename, args.before_name

def run_model(basename: str, before_name: str):
    target_filenames = [f'{basename}_{str(i)}' for i in range(1, 21)]
    allin_filename = basename + '_allin'
    compressed_filename = basename + '_compressed'
    merged_filename = basename + '_merged'
    pre_merged_filaname = before_name + '_merged'

    merge_train_data(target_filenames, allin_filename)
    compress_train_data(allin_filename, compressed_filename)
    merge_train_data([compressed_filename, pre_merged_filaname], merged_filename)
    format_data(merged_filename, basename)
    make_model(basename, basename)

if __name__ == "__main__":
    basename, before_name = get_args()
    run_model(basename, before_name)
