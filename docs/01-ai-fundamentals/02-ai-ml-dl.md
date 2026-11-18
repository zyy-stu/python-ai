# AI-002 AI、机器学习与深度学习

## 学习目标与前置知识

读完能用小实验解释AI、机器学习与深度学习。需要会运行 Python 函数、阅读列表和数值输出。可先完成[上一课](../01-ai-fundamentals/01-what-is-ai.md)。

## 概念与原理

机器学习从经验数据拟合映射，是 AI 的一类方法。深度学习用多层神经网络表示映射，是机器学习的一类方法。逻辑回归可做表格分类，深度网络可处理语音和图像。生成式 AI 描述任务，概率语言模型只是其中一种实现。

固定报警规则和拟合得到的逻辑模型都可服务于同一目标，所需证据不同：前者验证规则覆盖，后者验证测试泛化。多层结构不自动保证准确。

$$
p(y=1\mid x)=\frac{1}{1+e^{-w^\top x-b}}
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

比较规则系统和分类模型可调的变量。 将本课作为后续实验的环境或规则基线。

## 常见问题

深度学习一定胜过传统方法吗？模型表现要在相同数据与指标下比较。

## 练习及参考答案

说明规则报警和鸢尾花模型的参数从哪里来。

**答案** 阈值由开发者指定，分类模型的权重由训练样本与优化方法确定。

[本阶段练习与答案索引](../../exercises/README.md)。

## 总结与下一课

比较规则系统和分类模型可调的变量。 接下来学习[Python AI 开发环境](../01-ai-fundamentals/05-ai-development-environment.md)。

[官方参考资料](https://scikit-learn.org/stable/supervised_learning.html)
