import random
import string

TARGET_FILE = "train_multi.sh"

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def write_file():
    with open(TARGET_FILE, "w") as file:
        for i in range(1, 11):
            seed = generate_random_string(10)
            filename = '0' * (3 - len(str(i)))  + str(i)
            file.write(f"python -m src.train_multi 100 {seed} dump_{filename}.pkl\n")

if __name__ == "__main__":
    write_file()
