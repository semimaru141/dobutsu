from tensorflow.python.keras import layers, models

# モデルのレイヤーのための関数
def create_tanh() -> models.Sequential:
    # モデルの定義
    model = models.Sequential()
    
    model.add(layers.Dense(132 + 18, activation='relu', input_shape=(150,)))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='tanh'))

    return model

def create_linear() -> models.Sequential:
     # モデルの定義
    model = models.Sequential()

    model.add(layers.Dense(132 + 18, activation='relu', input_shape=(150,)))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(256, activation='relu'))
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1, activation='linear'))

    return model

def compile_model(model: models.Sequential) -> None:
    # モデルのコンパイル
    model.compile(optimizer='adam',
                loss='mean_absolute_error',
                metrics=['accuracy'])
