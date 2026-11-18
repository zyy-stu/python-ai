# AI-006 导数与梯度入门

## 学习目标与前置知识

读完能用小实验解释导数与梯度入门。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../02-mathematics/03-probability.md)。

## 概念与原理

导数描述局部变化率；偏导对一个变量求导并固定其余变量。梯度是偏导组成的向量，链式法则将复合函数的局部变化率相乘。

以 L(x)=x² 为例，梯度是 2x。x=3、学习率 0.1 时更新为 2.4。步长过大可越过最优点甚至发散。

$$
\frac{d(f\circ g)}{dx}=f'(g(x))g'(x),\quad \theta_{t+1}=\theta_t-\eta\nabla L(\theta_t)
$$

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../examples/01-ai-basics/main.py)，运行：

```bash
python examples/01-ai-basics/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
更新后参数 2.4
```

## 实际应用与易错点

把更新前后的平方损失都算一遍。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

学习率越大越快吗？超出稳定范围会来回振荡或发散。

## 练习及参考答案

从 2.4 继续做同一步长的一次更新。

**答案** 2.4 − 0.1×4.8 = 1.92。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

把更新前后的平方损失都算一遍。 接下来学习[机器学习是什么](../03-machine-learning/01-ml-introduction.md)。

[官方参考资料](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
