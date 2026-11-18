"""对教学实验进行确定性检查。"""

import runpy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    """加载受控示例的函数，不触发脚本入口。"""
    return runpy.run_path(ROOT / path)


def test_linear_algebra() -> None:
    results = load("examples/02-numpy-ai/main.py")["linear_algebra"]()
    assert results["dot"] == 13
    assert results["matvec"] == [8, 18]
    assert results["matmul"] == [[7, 10], [15, 22]]


def test_rule_probability_and_gradient() -> None:
    examples = load("examples/01-ai-basics/main.py")
    assert not examples["rule_alert"](99)
    assert examples["rule_alert"](100)
    assert examples["probability_summary"]()[:2] == (2.5, 1.25)
    assert examples["gradient_step"](3, 0.1) == pytest.approx(2.4)


def test_regression() -> None:
    error, prediction = load("examples/03-machine-learning/main.py")["regression"]()
    assert error < 1e-10
    assert prediction == pytest.approx(62)


def test_classification_and_clustering() -> None:
    examples = load("examples/03-machine-learning/main.py")
    count, accuracy = examples["classification"]()
    assert count == 30
    assert 0.85 <= accuracy <= 1
    assert examples["cluster_sizes"]() == [2, 2]


def test_regression_project() -> None:
    metrics = load("projects/linear-regression/main.py")["run"]()
    assert (metrics["train_rows"], metrics["test_rows"]) == (80, 20)
    assert metrics["mae"] < metrics["baseline_mae"]
    assert metrics["slope"] == pytest.approx(2.5, abs=0.1)


def test_pytorch_tensor() -> None:
    pytest.importorskip("torch")
    assert load("examples/04-pytorch/main.py")["tensor_demo"]() == [1, 4]


def test_pytorch_training() -> None:
    pytest.importorskip("torch")
    before, after = load("examples/04-pytorch/main.py")["train_network"]()
    assert 0 <= after < before / 10
