# AI-010 机器学习模型训练流程

## 学习目标与前置知识

读完能用小实验解释机器学习模型训练流程。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../03-machine-learning/04-regression.md)。

## 概念与原理

先定义问题和指标，再拆分数据。将预处理和模型放入 Pipeline，使拟合标准化的统计量来自训练数据。验证集或训练集内交叉验证用于选型，冻结配置后才报告测试结果。

流程：原始数据 → 分层拆分 → 训练内拟合变换 → 训练 → 测试预测。示例用预先确定的参数。若对同一个测试集反复挑选模型，相当于把测试信息用于训练决策。

$$
z_j=\frac{x_j-\mu_{j,\mathrm{train}}}{\sigma_{j,\mathrm{train}}}
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

确保测试集对预处理与选型不可见。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

交叉验证能替代最终测试吗？选型后仍可用预留测试集做独立评估。

## 练习及参考答案

把标准化提前到拆分之前会怎样？

**答案** 测试数据影响均值和标准差，构成数据泄漏。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

确保测试集对预处理与选型不可见。 接下来学习[模型评估基础](../03-machine-learning/09-model-evaluation.md)。

[官方参考资料](https://scikit-learn.org/stable/common_pitfalls.html)
