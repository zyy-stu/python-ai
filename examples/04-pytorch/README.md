# PyTorch CPU 神经网络

使用 Python 3.11+。在仓库根目录运行 `python -m pip install -r examples/04-pytorch/requirements.txt` 安装 PyTorch 2.7.1 CPU 版。样本由程序合成，训练循环为 100 步，无需模型权重或 GPU。

运行 `python examples/04-pytorch/main.py`。测试执行 `python -m pytest -q -k pytorch`。

本地实测（PyTorch 2.7.1+cpu）张量平方为 `[1.0, 4.0]`，100 步 MSE 由 `2.9954` 降至 `0.0047`。浮点末位可能随平台变化，测试核验损失下降幅度。

[返回示例目录](../README.md)
