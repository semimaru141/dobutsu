import argparse
from typing import Tuple
from src.applications.format_data import format_data

def get_args() -> Tuple[str, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('read_filename', type=str)
    parser.add_argument('output_filename', type=str)

    args = parser.parse_args()
    return args.read_filename, args.output_filename

if __name__ == "__main__":
    read_filename, output_filename = get_args()
    format_data(read_filename, output_filename)
