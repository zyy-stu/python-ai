"""使用规则与小型数值实验理解 AI 基础。"""

from math import exp, pi, sqrt
from statistics import mean, pstdev, pvariance


def rule_alert(amount: int) -> bool:
    """按人工设定的阈值标记异常。"""
    return amount >= 100


def probability_summary() -> tuple[float, float, float, float, float]:
    """计算总体统计量、条件频率和标准正态在零点的密度。"""
    values = [1, 2, 3, 4]
    conditional = sum(x % 2 == 0 for x in values if x > 2) / 2
    density = exp(-(0.0**2) / 2) / sqrt(2 * pi)
    return mean(values), pvariance(values), pstdev(values), conditional, density


def gradient_step(x: float, rate: float) -> float:
    """对平方函数执行一次梯度下降。"""
    return x - rate * 2 * x


if __name__ == "__main__":
    print("规则输出", [rule_alert(amount) for amount in (80, 120)])
    print("统计量", [round(x, 4) for x in probability_summary()])
    print("更新后参数", gradient_step(3, 0.1))
