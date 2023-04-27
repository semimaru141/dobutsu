from models.board import State
from models.evaluator import Evaluator
from applications.learn import learn

TRIAL = 100

if __name__ == "__main__":
    learn(TRIAL)
