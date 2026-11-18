"""小型回归、分类与聚类基线。"""

import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def regression() -> tuple[float, float]:
    """训练线性模型并返回测试 MAE 及新样本预测。"""
    features = np.arange(20).reshape(-1, 1)
    labels = 3 * features.ravel() + 2
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.25, random_state=42
    )
    model = LinearRegression().fit(x_train, y_train)
    error = mean_absolute_error(y_test, model.predict(x_test))
    return float(error), float(model.predict([[20]])[0])


def classification() -> tuple[int, float]:
    """使用分层拆分和训练内标准化预测鸢尾花类别。"""
    data = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, stratify=data.target, test_size=0.20, random_state=42
    )
    model = make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=300, solver="newton-cg", random_state=42)
    )
    model.fit(x_train, y_train)
    prediction = model.predict(x_test)
    return len(prediction), float(accuracy_score(y_test, prediction))


def cluster_sizes() -> list[int]:
    """无标签输入产生两个簇，返回与簇编号无关的大小。"""
    points = np.array([[0, 0], [0, 1], [8, 8], [9, 8]])
    model = KMeans(n_clusters=2, n_init=10, random_state=42).fit(points)
    return sorted(np.bincount(model.labels_).tolist())


if __name__ == "__main__":
    error, predicted = regression()
    count, accuracy = classification()
    print(f"回归 MAE={error:.6f}，预测={predicted:.1f}")
    print(f"分类样本={count}，准确率={accuracy:.4f}")
    print("聚类大小", cluster_sizes())
