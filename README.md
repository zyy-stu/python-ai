# Python 人工智能教程

Python Learning Roadmap 的中文 AI 专题。面向能编写 Python 函数的学习者，从概念、数学与算法走向框架、实验和应用工程。

## 从这里开始

[已发布的 12 篇教程](ROADMAP.md)覆盖 AI 基础、数学与机器学习。继续参阅[知识树](knowledge-tree/README.md)、[总目录](docs/README.md)、[四条学习路线](learning-path/README.md)、[可运行示例](examples/README.md)和[项目](projects/README.md)。深度学习与大模型等后续教程状态在路线图中逐项标明。

## 安装与验证

使用 Python 3.11+，在虚拟环境内安装并运行：

```bash
python -m pip install -r requirements-dev.txt
python -m ruff check .
python -m pytest
```

[PyTorch CPU 示例](examples/04-pytorch/README.md)单独安装。普通训练和 CI 不需要 GPU、API 密钥或模型权重。

## 仓库边界

本仓库负责机器学习、深度学习、NLP、LLM、RAG、Agent 与 AI 应用。学习前置知识时按需要查阅：

- [python-learning-roadmap](https://github.com/zyy-stu/python-learning-roadmap) · 总知识导航
- [python-basic](https://github.com/zyy-stu/python-basic) · Python 语法和数据结构
- [python-advanced](https://github.com/zyy-stu/python-advanced) · 高级机制、并发、内存和工程化
- [python-data-science](https://github.com/zyy-stu/python-data-science) · NumPy、Pandas、清洗、可视化与统计
- [python-web](https://github.com/zyy-stu/python-web) · FastAPI、Django、Flask 与 Web API
- [python-projects](https://github.com/zyy-stu/python-projects) · 跨专题综合项目

[贡献指南](CONTRIBUTING.md) · [规范](standards/README.md) · [模板](templates/README.md) · [MIT 许可证](LICENSE)
