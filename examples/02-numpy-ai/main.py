"""用 NumPy 表达向量和矩阵。"""

import numpy as np


def linear_algebra() -> dict[str, object]:
    """返回逐元素运算、转置、点积和矩阵乘法。"""
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([2, 3])
    return {
        "sum": (matrix + matrix).tolist(),
        "transpose": matrix.T.tolist(),
        "dot": int(vector @ vector),
        "matvec": (matrix @ vector).tolist(),
        "matmul": (matrix @ matrix).tolist(),
    }


if __name__ == "__main__":
    print(linear_algebra())
