from typing import Union
from src.domains.model.model import Model
from src.domains.model.model_file_factory import ModelFileFactory
from src.domains.model.model_learn_factory import ModelLearnFactory
from src.domains.ready_data.ready_data import ReadyData

def make_model(read_filename: str = 'default', output_filename = 'default', base_model_name: Union[str, None] = None) -> None:
    if base_model_name == None:
        new_model = _create_from_scratch(read_filename)
    else:
        new_model = _create_from_model(read_filename, base_model_name)
    new_model.save(output_filename)

def _create_from_scratch(read_filename: str) -> Model:
    ready_data = ReadyData.create_from_file(read_filename)
    return ModelLearnFactory(ready_data).create()

def _create_from_model(read_filename: str, base_model_name: str) -> Model:
    ready_data = ReadyData.create_from_file(read_filename)
    model = ModelFileFactory(base_model_name).create()
    return ModelLearnFactory(ready_data, model).create()
