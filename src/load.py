import argparse
from src.applications.load import load

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    return args.filename

if __name__ == "__main__":
    filename = get_args()
    load(filename)
