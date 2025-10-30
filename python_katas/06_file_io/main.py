#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

"""
主题: 文件与Pathlib
- 读写文本
- 上下文管理器 with
- 路径拼接/遍历
"""

def write_lines(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path: Path) -> list[str]:
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def list_py_files(root: Path) -> list[Path]:
    # TODO: 使用 rglob 查找所有 .py 文件
    return sorted(root.rglob("*.py"))


def run_self_check():
    tmp = Path(__file__).parent / "_tmp" / "demo.txt"
    data = ["hello", "world"]
    write_lines(tmp, data)
    assert read_lines(tmp) == data

    py_files = list_py_files(Path(__file__).parents[2])  # 项目根
    assert any(p.name == "main.py" for p in py_files)

    print("06_file_io ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
