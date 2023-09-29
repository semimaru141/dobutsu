import argparse
from src.applications.make_model import make_model

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('read_filename', type=str)
    parser.add_argument('output_filename', type=str)

    args = parser.parse_args()
    return args.read_filename, args.output_filename

if __name__ == "__main__":
    read_filename, output_filename = get_args()
    make_model(read_filename, output_filename)
