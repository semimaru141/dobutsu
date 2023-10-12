import argparse
from typing import Tuple
from src.applications.train_multi import train_multi

def get_args() -> Tuple[int, int, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('trial', type=int)
    parser.add_argument('seed', type=int)
    parser.add_argument('filename', type=str)

    args = parser.parse_args() 
    return args.trial, args.seed, args.filename

if __name__ == "__main__":
    trial, seed, filename = get_args()
    train_multi(trial, seed, filename)
