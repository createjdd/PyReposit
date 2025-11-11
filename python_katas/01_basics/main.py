#!/usr/bin/env python3
from __future__ import annotations

"""
主题: 基础语法与内置类型
练习目标:
- 变量与类型
- 数字/字符串/布尔/None
- f-string 与格式化
- 基本运算与比较
- 序列切片
- Truthy/Falsy
使用: 直接运行本文件: python 01_basics/main.py
建议: 按 TODO 提示尝试修改并观察输出
"""


def demo_numbers_strings():
    x = 7 # 整数
    y = 3 # 浮点数
    add = x + y # 加法
    div = x / y # 除法
    floor_div = x // y # 整除
    mod = x % y # 取余
    power = x ** y # 幂
    s = "hello"
    t = "world"
    join = s + " " + t
    f = f"{s.capitalize()}, {t.upper()}! add={add} div={div:.2f}"
    return add, div, floor_div, mod, power, join, f


def demo_truthy_falsy():
    cases = [0, 1, "", "hi", [], [1], None, {}, {"a": 1}]
    return [bool(c) for c in cases]


def slice_examples(seq: list[int]) -> tuple[list[int], list[int], list[int]]:
    # TODO: 调整切片，体会步长含义
    first_three = seq[:3]
    last_two = seq[-2:]
    odds = seq[::2]
    return first_three, last_two, odds


def comparisons(a: int, b: int) -> dict[str, bool]:
    return {
        "eq": a == b,
        "ne": a != b,
        "gt": a > b,
        "ge": a >= b,
        "lt": a < b,
        "le": a <= b,
    }


def demo_data_types():
    """
    演示常见内置数据类型及其类型名。
    返回:
      - data: 各类型的示例值
      - types: 各示例值对应的类型名（字符串）
    """
    data = {
        "int": 42,
        "float": 3.14,
        "bool_true": True,
        "bool_false": False,
        "none": None,
        "str": "hello",
        "list": [1, 2, 3],
        "tuple": (1, 2, 3),
        "set": {1, 2, 3},
        "dict": {"a": 1, "b": 2},
        "bytes": b"hi",
    }
    types = {k: type(v).__name__ for k, v in data.items()}
    return data, types


def run_self_check():
    add, div, floor_div, mod, power, join, f = demo_numbers_strings()
    assert add == 10
    assert floor_div == 2 and mod == 1 and power == 343
    assert join.startswith("hello world") and "add=10" in f

    truth = demo_truthy_falsy()
    assert truth == [False, True, False, True, False, True, False, False, True]

    s1, s2, s3 = slice_examples([0, 1, 2, 3, 4, 5])
    assert s1 == [0, 1, 2] and s2 == [4, 5] and s3 == [0, 2, 4]

    comp = comparisons(3, 5)
    assert comp["lt"] and not comp["gt"] and comp["ne"]

    data, types = demo_data_types()
    # 简单校验类型名存在
    for key in ["int", "float", "bool_true", "none", "str", "list", "tuple", "set", "dict", "bytes"]:
        assert key in data and key in types

    print("01_basics ✅ 自检通过。你可以修改 TODO 再运行观察差异。")


if __name__ == "__main__":
    run_self_check()
