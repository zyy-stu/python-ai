# AI-012 第一个机器学习项目

## 学习目标与前置知识

读完能用小实验解释第一个机器学习项目。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../03-machine-learning/09-model-evaluation.md)。

## 概念与原理

使用合成工件数量预测用时。由线性关系与零均值噪声生成 100 条样本，保留 20 条测试记录。单特征为工件数量，目标为秒。

用训练集拟合直线与常数基线，以同一个测试集比较 MAE，再预测 60 件。外推、真实工况变化和遗漏变量都会影响生产可用性。

$$
y=12+2.5x+\varepsilon,\quad\varepsilon\sim\mathcal N(0,2^2)
$$

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../projects/linear-regression/main.py)，运行：

```bash
python projects/linear-regression/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
train_rows: 80
test_rows: 20
slope: 2.49115
mae: 1.39219
baseline_mae: 64.1931
r2: 0.999348
prediction_60: 161.814
```

## 实际应用与易错点

检查噪声、样本量和目标范围对结果的影响。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

项目 MAE 能代表生产误差吗？合成数据的结果只验证这套实验。

## 练习及参考答案

把常数基线定义为测试集均值是否合理？

**答案** 不合理。预测时不能先知道测试标签，基线只能从训练集计算。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

检查噪声、样本量和目标范围对结果的影响。 接下来阅读[深度学习导读](../04-deep-learning/README.md)。

[官方参考资料](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
