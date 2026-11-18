# AI-008 监督学习与无监督学习

## 学习目标与前置知识

读完能用小实验解释监督学习与无监督学习。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../03-machine-learning/01-ml-introduction.md)。

## 概念与原理

监督学习在带标签样本上学习预测。KMeans 只观察输入，交替分配到最近中心并重新计算中心，最小化簇内平方距离。簇编号本身不对应真实类别。

四个点构成两个明显的团，结果用簇大小检查。真实聚类应评估稳定性和用途，不能因为存在两簇就断言它们是决策标签。

$$
J=\sum_i\min_j\lVert x_i-\mu_j\rVert_2^2
$$

## Python 示例与实测输出

在仓库根目录使用 Python 3.11+。先运行 `python -m pip install -r requirements-dev.txt`。查看[完整 Python 代码](../../examples/03-machine-learning/main.py)，运行：

```bash
python examples/03-machine-learning/main.py
```

下方是本节对应的实际输出。共享脚本可能同时打印其他小节的结果。

```text
分类样本=30，准确率=0.9333
聚类大小 [2, 2]
```

## 实际应用与易错点

用簇大小检验可复现性，避免依赖整数簇编号。 保留输入与中间结果，方便定位手算和程序的差异。

## 常见问题

无监督没有评价方法吗？可用轮廓系数、稳定性或业务实验。

## 练习及参考答案

为什么示例对簇大小排序？

**答案** 聚类算法可以交换两个簇的编号，排序后仍能比较大小。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

用簇大小检验可复现性，避免依赖整数簇编号。 接下来学习[回归与分类](../03-machine-learning/04-regression.md)。

[官方参考资料](https://scikit-learn.org/stable/modules/clustering.html)
