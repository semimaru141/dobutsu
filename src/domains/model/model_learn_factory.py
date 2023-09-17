from src.domains.model.model import Model
from src.domains.ready_data.ready_data import ReadyData
from tensorflow.python.keras import layers, models

class ModelLearnFactory:
    def __init__(self, ready_data: ReadyData) -> None:
        self.ready_data = ready_data

    def create(self) -> 'Model':
        x = self.ready_data.x
        y = self.ready_data.y

        # モデルの定義
        model = models.Sequential()
        model.add(layers.Dense(132 + 18, activation='relu'))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(1, activation='linear'))

        # モデルのコンパイル
        model.compile(optimizer='adam',
                    loss='mean_absolute_error',
                    metrics=['accuracy'])

        # モデルの学習
        model.fit(x, y, epochs=100, batch_size=1024)

        return Model(model)
