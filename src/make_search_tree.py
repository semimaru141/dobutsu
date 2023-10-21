import argparse
from src.applications.make_search_tree import make_search_tree
from src.applications.test_with_model import test_with_model

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    return args.filename

if __name__ == "__main__":
    filename = get_args()
    make_search_tree(filename)
