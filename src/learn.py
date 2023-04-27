from models.board import State
from models.evaluator import Evaluator
from models.trainer import Trainer

TRIAL = 100

if __name__ == "__main__":
    # 初期状態
    state = State.create_initial()
    evaluator = Evaluator.create_rand()

    trainer = Trainer()
    trainer.train(evaluator, TRIAL)

