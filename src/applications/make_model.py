from src.domains.model.model_learn_factory import ModelLearnFactory
from src.domains.ready_data.ready_data import ReadyData

def make_model(filename: str = 'default'):
    ready_data = ReadyData.create_from_file(filename)
    factory = ModelLearnFactory(ready_data)
    model = factory.learn()
    model.save()
