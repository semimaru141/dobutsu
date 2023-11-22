from typing import Union
from src.consts.domain import MODEL_BATCH_SIZE, MODEL_EPOCHS
from src.domains.model.model import Model
from src.domains.model.model_layers import compile_model, create_tanh
from src.domains.ready_data.ready_data import ReadyData

class ModelLearnFactory:
    # modelは新規モデル生成時に副作用が発生してしまう(処理の効率化のための対応)
    def __init__(self, ready_data: ReadyData, model: Union[None, Model] = None) -> None:
        self.ready_data = ready_data
        self.model = model

    def create(self) -> 'Model':
        if self.model == None:
            return self._create_from_scratch()
        else:
            return self._create_from_model()

    def _create_from_scratch(self) -> 'Model':
        x = self.ready_data.x
        y = self.ready_data.y

        model = create_tanh()
        compile_model(model)

        # モデルの学習
        model.fit(x, y, epochs=MODEL_EPOCHS, batch_size=MODEL_BATCH_SIZE)

        return Model(model)
    
    def _create_from_model(self) -> 'Model':
        x = self.ready_data.x
        y = self.ready_data.y

        self.model.model.fit(x, y, epochs=MODEL_EPOCHS, batch_size=MODEL_BATCH_SIZE)

        return Model(self.model)

