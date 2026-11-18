# AI-004 线性代数入门

## 学习目标与前置知识

读完能用小实验解释线性代数入门。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../01-ai-fundamentals/05-ai-development-environment.md)。

## 概念与原理

标量为单个数，向量是一组数，矩阵以行列组织。转置交换轴；逐元素相加需形状兼容；点积加总元素乘积。矩阵乘法要求前一矩阵列数等于后一矩阵行数。

矩阵乘向量可把特征映射到得分。示例中首行与 [2,3] 点积为 8。NumPy 的 * 表示逐元素乘法，@ 表示矩阵乘法或向量点积。

$$
(AB)_{ij}=\sum_{k=1}^{n}A_{ik}B_{kj}
$$

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

先写出参与计算的两个形状。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

为什么向量点积是标量？维度对齐后所有乘积求和。

## 练习及参考答案

手算第二行的矩阵向量乘积。

**答案** 3×2 + 4×3 = 18。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

先写出参与计算的两个形状。 接下来学习[概率统计入门](../02-mathematics/03-probability.md)。

[官方参考资料](https://numpy.org/doc/2.2/user/quickstart.html)
