import tensorflow as tf
from tensorflow.keras import layers, models

class LearnModel:
    def __init__(self, input, output) -> None:
        self._input = input
        self._output = output
        self._model = self.learn()

    def learn(self):
        x_train = self._input
        y_train = self._output

        # モデルの定義
        model = models.Sequential()
        model.add(layers.Dense(132, activation='relu'))
        model.add(layers.Dense(128, activation='relu'))
        model.add(layers.Dense(1, activation='linear'))

        # モデルのコンパイル
        model.compile(optimizer='rmsprop',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        # モデルの学習
        model.fit(x_train, y_train, epochs=10, batch_size=len(x_train))

        return model
        
    def save(self):
        self._model.save_weights('model')
