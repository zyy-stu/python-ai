# AI-003 Python AI 开发环境

## 学习目标与前置知识

读完能用小实验解释Python AI 开发环境。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../01-ai-fundamentals/02-ai-ml-dl.md)。

## 概念与原理

虚拟环境将解释器和依赖与其他项目分离。Jupyter 用于探索，NumPy 处理矩阵，Pandas 处理表格，Matplotlib 绘图，Scikit-learn 训练传统模型，PyTorch 支持张量与自动求导。本仓库基础示例只安装 NumPy 与 Scikit-learn，其他工具按任务单独安装。

线性算子可在 CPU 和 GPU 上求值。小实验使用 CPU；GPU 需匹配驱动和 PyTorch 构建，不能仅凭机器有显卡推断 CUDA 可用。Notebook 用当前虚拟环境作为内核。

$$
Y=XW+b
$$

## 创建环境

```bash
python -m venv .venv
```

Windows PowerShell 使用 `.\.venv\Scripts\Activate.ps1`，Linux/macOS 使用 `source .venv/bin/activate`。激活后执行 `python --version` 和 `python -m pip --version`，确认解释器及安装目录对应当前环境。Jupyter 是可选工具，使用时选中这个虚拟环境对应的内核。PyTorch 安装见 [CPU 示例](../../examples/04-pytorch/README.md)。

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../examples/02-numpy-ai/main.py)，运行：

```bash
python examples/02-numpy-ai/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
{'sum': [[2, 4], [6, 8]], 'transpose': [[1, 3], [2, 4]], 'dot': 13, 'matvec': [8, 18], 'matmul': [[7, 10], [15, 22]]}
```

## 实际应用与易错点

用 pip show 确认证据来自正在运行的解释器。 将本课作为后续实验的环境或规则基线。

## 常见问题

有 GPU 就必须使用吗？小教学实验使用 CPU 更容易复现。

## 练习及参考答案

执行 python -m pip show numpy scikit-learn，确认目录与版本。

**答案** 在激活的环境中应显示 NumPy 2.2.6 和 Scikit-learn 1.6.1。若位置不对，检查解释器。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

用 pip show 确认证据来自正在运行的解释器。 接下来学习[线性代数入门](../02-mathematics/01-linear-algebra.md)。

[官方参考资料](https://docs.python.org/3/library/venv.html)
