
import numpy as np

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
) -> (np.ndarray, float, list[float]):

    X = np.asarray(features, dtype=float)
    y = np.asarray(labels, dtype=float).reshape(-1)

    weights = np.asarray(initial_weights, dtype=float).copy()
    bias = float(initial_bias)

    m = len(y)
    mse_values = []

    for _ in range(epochs):
        z = X @ weights + bias

        # 修正 1：Sigmoid 分母使用 +
        predictions = 1 / (1 + np.exp(-z))

        error = predictions - y
        mse = np.mean(error ** 2)
        mse_values.append(round(float(mse), 4))

        delta = (2 / m) * error * predictions * (1 - predictions)

        dw = X.T @ delta
        db = np.sum(delta)

        # 修正 2：更新已经初始化的变量
        weights -= learning_rate * dw
        bias -= learning_rate * db

    # 修正 3：返回正确变量并保留四位小数
    return np.round(weights, 4), round(bias, 4), mse_values
