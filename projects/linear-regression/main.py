"""使用合成用时与工件数完成回归实验。"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


def run() -> dict[str, float | int]:
    """用保留测试集评估线性模型和常数基线。"""
    rng = np.random.default_rng(42)
    count = np.arange(10, 110)
    elapsed = 12 + 2.5 * count + rng.normal(0, 2, count.size)
    features = count.reshape(-1, 1)
    x_train, x_test, y_train, y_test = train_test_split(
        features, elapsed, test_size=0.20, random_state=42
    )
    model = LinearRegression().fit(x_train, y_train)
    predictions = model.predict(x_test)
    baseline = np.full(y_test.shape, np.mean(y_train))
    return {
        "train_rows": len(x_train),
        "test_rows": len(x_test),
        "slope": float(model.coef_[0]),
        "mae": float(mean_absolute_error(y_test, predictions)),
        "baseline_mae": float(mean_absolute_error(y_test, baseline)),
        "r2": float(r2_score(y_test, predictions)),
        "prediction_60": float(model.predict([[60]])[0]),
    }


if __name__ == "__main__":
    for name, value in run().items():
        print(f"{name}: {value:.6g}")
