# AI-009 回归与分类

## 学习目标与前置知识

读完能用小实验解释回归与分类。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../03-machine-learning/02-supervised-learning.md)。

## 概念与原理

回归预测连续数值，分类预测标记或类别概率。线性回归在此拟合 y=wx+b；逻辑回归名称含回归，但示例用它做分类。

示例使用两种任务：连续产出和鸢尾花品种。回归误差带单位，分类准确率是比例，不能直接横向比较大小。

$$
\hat y=wx+b,\quad \hat c=\arg\max_c p(c\mid x)
$$

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../examples/03-machine-learning/main.py)，运行：

```bash
python examples/03-machine-learning/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
回归 MAE=0.000000，预测=62.0
分类样本=30，准确率=0.9333
```

## 实际应用与易错点

为连续目标标明单位，为类别标明可选集合。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

预测数字就是回归吗？若数字是类别编码，仍是分类。

## 练习及参考答案

预测 y=3x+2 在 x=20 时的结果。

**答案** 62。该示例无噪声，精度不能代表真实数据。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

为连续目标标明单位，为类别标明可选集合。 接下来学习[机器学习模型训练流程](../03-machine-learning/11-model-selection.md)。

[官方参考资料](https://scikit-learn.org/stable/modules/linear_model.html)
