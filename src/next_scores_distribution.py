import argparse
from src.applications.next_scores_distribution import next_scores_distribution

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)
    args = parser.parse_args()
    return args.filename

if __name__ == "__main__":
    filename = get_args()
    next_scores_distribution(filename)
