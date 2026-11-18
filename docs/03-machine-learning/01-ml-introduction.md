# AI-007 机器学习是什么

## 学习目标与前置知识

读完能用小实验解释机器学习是什么。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../02-mathematics/02-calculus.md)。

## 概念与原理

训练从观测特征学习模型参数。监督学习使用标签，无监督学习寻找数据结构；强化学习依据交互奖励优化策略。训练集更新参数，验证集选方案，测试集只用于最终评估。

分类示例的特征为花萼与花瓣测量，标签为品种。代码固定拆分，仅演示一个预设模型，有调参需求时应在训练部分内另设验证或交叉验证。

$$
\hat\theta=\arg\min_\theta\frac{1}{n}\sum_{i=1}^n \ell(f_\theta(x_i),y_i)
$$

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../examples/03-machine-learning/main.py)，运行：

```bash
python examples/03-machine-learning/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
分类样本=30，准确率=0.9333
```

## 实际应用与易错点

在流程图中明确哪些阶段能看标签。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

训练准确率能当最终指标吗？需要保留样本检验泛化。

## 练习及参考答案

指出分类示例的特征、标签和测试输出。

**答案** 4 个测量值为特征，品种为标签，测试输出为 30 个预测的准确率。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

在流程图中明确哪些阶段能看标签。 接下来学习[监督学习与无监督学习](../03-machine-learning/02-supervised-learning.md)。

[官方参考资料](https://scikit-learn.org/stable/model_selection.html)
