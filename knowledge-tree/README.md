# AI 知识树

## 01 人工智能基础

**范围与概念** 规则系统、机器学习、深度学习、生成式 AI 与环境。  
**先修与工具** Python 基础。使用 Python、Jupyter。  
**目标与应用** 能比较同一任务的规则和学习基线，保留复现输入和验证结果。  
**入口与进阶** [人工智能基础](../docs/01-ai-fundamentals/README.md)，进一步学习[数学基础](../docs/02-mathematics/README.md)。

## 02 数学基础

**范围与概念** 线性代数、概率统计、微积分与优化。  
**先修与工具** 中学代数。使用 NumPy、statistics。  
**目标与应用** 能向量投影与梯度实验，保留复现输入和验证结果。  
**入口与进阶** [数学基础](../docs/02-mathematics/README.md)，进一步学习[机器学习](../docs/03-machine-learning/README.md)。

## 03 机器学习

**范围与概念** 监督、无监督、回归、分类、聚类、评估、特征工程和选型。  
**先修与工具** 数学基础。使用 Scikit-learn。  
**目标与应用** 能建立训练、测试与基线流程，保留复现输入和验证结果。  
**入口与进阶** [机器学习](../docs/03-machine-learning/README.md)，进一步学习[深度学习](../docs/04-deep-learning/README.md)。

## 04 深度学习

**范围与概念** 感知机、网络、激活、损失、梯度下降、反向传播、优化、正则与训练。  
**先修与工具** 梯度与模型评估。使用 PyTorch。  
**目标与应用** 能完成小型神经网络基线，保留复现输入和验证结果。  
**入口与进阶** [深度学习](../docs/04-deep-learning/README.md)，进一步学习[PyTorch](../docs/05-pytorch/README.md)。

## 05 PyTorch

**范围与概念** Tensor、Autograd、nn.Module、Dataset、DataLoader、Loss、Optimizer、训练、保存、GPU。  
**先修与工具** 深度学习基础。使用 PyTorch。  
**目标与应用** 能训练与验证小网络，保留复现输入和验证结果。  
**入口与进阶** [PyTorch](../docs/05-pytorch/README.md)，进一步学习[计算机视觉](../docs/06-computer-vision/README.md)。

## 06 计算机视觉

**范围与概念** 图像、CNN、分类、检测、分割与视觉 Transformer。  
**先修与工具** 张量与网络。使用 PyTorch、TorchVision。  
**目标与应用** 能区分图像级与像素级预测，保留复现输入和验证结果。  
**入口与进阶** [计算机视觉](../docs/06-computer-vision/README.md)，进一步学习[自然语言处理](../docs/07-nlp/README.md)。

## 07 自然语言处理

**范围与概念** 文本处理、分词、词向量、Embedding、Attention、Transformer。  
**先修与工具** 线性代数与模型评估。使用 PyTorch、Transformers。  
**目标与应用** 能实现词袋和文本分类基线，保留复现输入和验证结果。  
**入口与进阶** [自然语言处理](../docs/07-nlp/README.md)，进一步学习[大语言模型](../docs/08-large-language-models/README.md)。

## 08 大语言模型

**范围与概念** Transformer、Tokenizer、Embedding、预训练、指令微调、微调、LoRA、量化、推理。  
**先修与工具** NLP 与注意力。使用 Transformers、PEFT。  
**目标与应用** 能比较推理延迟与质量，保留复现输入和验证结果。  
**入口与进阶** [大语言模型](../docs/08-large-language-models/README.md)，进一步学习[Prompt Engineering](../docs/09-prompt-engineering/README.md)。

## 09 Prompt Engineering

**范围与概念** 角色、上下文、少样本、结构化输出、评估与提示安全。  
**先修与工具** 模型输入输出。使用 JSON Schema、离线评估集。  
**目标与应用** 能验证模型输出满足结构约定，保留复现输入和验证结果。  
**入口与进阶** [Prompt Engineering](../docs/09-prompt-engineering/README.md)，进一步学习[RAG](../docs/10-rag/README.md)。

## 10 RAG

**范围与概念** 文档处理、切块、Embedding、向量库、检索、重排、生成、评估与优化。  
**先修与工具** 文本处理与基础模型调用。使用 向量索引、离线检索指标。  
**目标与应用** 能让回答引用可核对的文档，保留复现输入和验证结果。  
**入口与进阶** [RAG](../docs/10-rag/README.md)，进一步学习[AI Agent](../docs/11-ai-agents/README.md)。

## 11 AI Agent

**范围与概念** 工具调用、规划、记忆、多 Agent、工作流和评估。  
**先修与工具** 结构化输出和接口边界。使用 JSON Schema、模拟工具。  
**目标与应用** 能构建可审计的工具调用流程，保留复现输入和验证结果。  
**入口与进阶** [AI Agent](../docs/11-ai-agents/README.md)，进一步学习[模型部署](../docs/12-model-deployment/README.md)。

## 12 模型部署

**范围与概念** 服务、API、Docker、GPU 推理、监控。  
**先修与工具** 稳定的模型输入输出。使用 FastAPI、Docker。  
**目标与应用** 能验证健康检查与版本回滚，保留复现输入和验证结果。  
**入口与进阶** [模型部署](../docs/12-model-deployment/README.md)，进一步学习[AI 工程化](../docs/13-ai-engineering/README.md)。

## 13 AI 工程化

**范围与概念** 实验追踪、评估、数据治理、安全与应用。  
**先修与工具** 工程和评估基础。使用 pytest、GitHub Actions。  
**目标与应用** 能复现模型指标与安全边界，保留复现输入和验证结果。  
**入口与进阶** [AI 工程化](../docs/13-ai-engineering/README.md)，进一步按项目需求选择部署或安全评估。

[依赖关系](dependencies.md) · [学习地图](learning-map.md)
