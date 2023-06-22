from src.domains.model.model import Model
from tensorflow.python.keras.models import load_model

class ModelFileFactory():
    def __init__(self, filename = 'default'):
        model = self._read(filename)
        self.model = model
    
    def _read(self, filename: str) -> None:
        return load_model('data/model/' + filename)

    def create(self) -> Model:
        return Model(self.model)
