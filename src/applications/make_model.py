from src.domains.model.model_learn_factory import ModelLearnFactory
from src.domains.ready_data.ready_data import ReadyData

def make_model(read_filename: str = 'default', output_filename = 'default') -> None:
    ready_data = ReadyData.create_from_file(read_filename)
    factory = ModelLearnFactory(ready_data)
    model = factory.create()
    model.save(output_filename)
