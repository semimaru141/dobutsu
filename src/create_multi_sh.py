import argparse
import random

TARGET_FILE = "train_multi.sh"

def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('basename', type=str)
    parser.add_argument('model_name', type=str)
    parser.add_argument('param', type=float)
    parser.add_argument('algorithm', type=str)

    args = parser.parse_args()
    return args.basename, args.model_name, args.param, args.algorithm

def write_file(basename: str, model_name: str, param: float, algorithm: str):
    with open(TARGET_FILE, "w") as file:
        for i in range(1, 21):
            seed = random.randint(1, 1000000)
            index = '0' * (3 - len(str(i)))  + str(i)

            # 50000試合 = 2h
            file.write(f"python3 -m src.train_multi_model 15000 {seed} {basename}_{index} {model_name} {param} {algorithm}\n")

if __name__ == "__main__":
    basename, model_name, param, algorithm = get_args()
    write_file(basename, model_name, param, algorithm)
