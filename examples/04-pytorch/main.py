"""在 CPU 上训练一个极小的神经网络。"""

import torch
from torch import nn


def tensor_demo() -> list[float]:
    """创建 CPU 张量并执行逐元素运算。"""
    values = torch.tensor([1.0, 2.0], device="cpu")
    return values.square().tolist()


def train_network() -> tuple[float, float]:
    """返回训练前后 MSE，使用合成数据与固定种子。"""
    torch.manual_seed(42)
    features = torch.linspace(-1, 1, 16, device="cpu").reshape(-1, 1)
    target = 2 * features + 1
    model = nn.Sequential(nn.Linear(1, 8), nn.Tanh(), nn.Linear(8, 1)).cpu()
    loss_fn = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    with torch.no_grad():
        initial = loss_fn(model(features), target).item()
    for _ in range(100):
        optimizer.zero_grad()
        loss = loss_fn(model(features), target)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        final = loss_fn(model(features), target).item()
    return initial, final


if __name__ == "__main__":
    print("张量平方", tensor_demo())
    before, after = train_network()
    print(f"训练前 MSE={before:.4f}，训练后 MSE={after:.4f}")
