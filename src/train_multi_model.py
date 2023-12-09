import argparse
from typing import Tuple
from src.applications.train_multi_model import train_multi_model

def get_args() -> Tuple[int, int, str, str, float, str]:
    parser = argparse.ArgumentParser()
    parser.add_argument('trial', type=int)
    parser.add_argument('seed', type=int)
    parser.add_argument('filename', type=str)
    parser.add_argument('model_name', type=str)
    parser.add_argument('param', type=float)
    parser.add_argument('algorithm', type=str)

    args = parser.parse_args() 
    return args.trial, args.seed, args.filename, args.model_name, args.param, args.algorithm

if __name__ == "__main__":
    trial, seed, filename, model_name, param, algorithm = get_args()
    train_multi_model(trial, seed, filename, model_name, param, algorithm)
