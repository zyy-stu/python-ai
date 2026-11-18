# AI-011 模型评估基础

## 学习目标与前置知识

读完能用小实验解释模型评估基础。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../03-machine-learning/11-model-selection.md)。

## 概念与原理

回归可看 MAE、RMSE、R²。分类可看准确率、精确率、召回率与混淆矩阵。类别不均衡时应先比较简单基线，并报告具有业务意义的错误。

同一模型可因切分不同得到不同分数。项目用训练标签均值作测试基线，并对照线性模型的 MAE；随机种子帮助复现，不能消除抽样误差。

$$
\mathrm{MAE}=\frac1n\sum_i|y_i-\hat y_i|,\quad \mathrm{Accuracy}=\frac{\text{正确预测数}}n
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

用基线解释指标，再调查错误个例。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

R² 可以为负吗？可以，测试上可能不如常数均值比较基准。

## 练习及参考答案

若 95 个样本为负类，恒预测负类的准确率是多少？

**答案** 95%，但正类召回率为 0。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

用基线解释指标，再调查错误个例。 接下来学习[第一个机器学习项目](../03-machine-learning/12-first-project.md)。

[官方参考资料](https://scikit-learn.org/stable/modules/model_evaluation.html)
