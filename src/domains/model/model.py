from typing import List
import numpy as np
from src.consts.domain import *
from src.utils.key_handler import proccess_key
from tensorflow.python.keras import Sequential, Model as KerasModel
import matplotlib.pyplot as plt

class Model():
    def __init__(self, model: Sequential):
        self.model = model

    def save(self, filename: str = 'default'):
        self.model.save('data/model/' + filename)

    def search_score(self, key: Key) -> Score:
        x = np.array([proccess_key(key)], dtype=np.float32)
        t = self.model(x, training=False)
        return t[0][0]
    
    def show_wight_distribution(self):
        # 重みの分布をヒストグラムとしてプロット
        for i, layer in enumerate(self.model.layers):
            weights, _biases = layer.get_weights()
            plt.hist(weights.flatten(), bins=50, alpha=0.6, label=f"Layer {i+1}")
            
        plt.legend()
        plt.xlabel('Weight values')
        plt.ylabel('Number of weights')
        plt.title('Distribution of Weights')
        plt.show()

    def show_activation(self, key: Key):
        # 中間層の出力を取得するモデルの作成
        layer_outputs = [layer.output for layer in self.model.layers]
        activation_model = KerasModel(inputs=self.model.input, outputs=layer_outputs)

        x = np.array([proccess_key(key)], dtype=np.float32)
        # 入力データを使って活性化の出力を取得
        activations = activation_model.predict(x)

        # 活性化の出力を可視化
        for i, activation in enumerate(activations):
            plt.figure(i)
            plt.title(f"Layer {i + 1}")
            plt.hist(activation[0], bins=50)
            plt.xlabel('Activation Value')
            plt.ylabel('Number of Neurons')

        plt.show()

    def show_heat_map(self, keys: List[Key]):
        # 中間層の出力を取得するモデルの作成
        layer_outputs = [layer.output for layer in self.model.layers]
        activation_model = KerasModel(inputs=self.model.input, outputs=layer_outputs)

        for key in keys:
            x = np.array([proccess_key(key)], dtype=np.float32)
            # 入力データを使って活性化の出力を取得
            activations = activation_model.predict(x)

            # ヒートマップを描画
            for i, activation in enumerate(activations):
                if i == 0:
                    plt.matshow(activation, cmap='viridis')
                    plt.title(f"Layer {i + 1}")

        plt.show()

    def show(self, key: Key, node_rank: int):
        # 中間層の出力を取得するモデルの作成
        layer_outputs = [layer.output for layer in self.model.layers]
        activation_model = KerasModel(inputs=self.model.input, outputs=layer_outputs)

        x = np.array([proccess_key(key)], dtype=np.float32)
        # 入力データを使って活性化の出力を取得
        activations = activation_model.predict(x)

        # 第一レイヤーを対象にする
        activation = activations[0][0]

        # 要素を昇順にソートした際のインデックスを取得
        sorted_indices = np.argsort(activation)

        # n番目に大きい要素のインデックス番号を取得
        node_index = sorted_indices[-1 * node_rank]

        # 重みを取得
        weights = self.model.layers[0].get_weights()[0]
        node_weights = weights[:, node_index]

        # 重みの合計を計算
        total = node_weights.sum()

        # 重みの割合を計算
        percentages = (node_weights / total) * 100

        # インデックスを取得
        indices = np.argsort(np.abs(node_weights))[::-1]

        # 結果をリストとして収集
        result = [(idx, percentages[idx]) for idx in indices]

        ps = list(map(lambda x: f"{x[0] // 11} * 11 + {x[0] % 11}, percentage: {x[1]}", result))[:10]

        for p in ps:
            print(p)

