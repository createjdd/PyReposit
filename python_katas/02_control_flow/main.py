#!/usr/bin/env python3
from __future__ import annotations

"""
主题: 控制流
- if/elif/else, match(3.10+ 可用)
- for/while, break/continue
- range/enumerate/zip
"""

def fizz_buzz(n: int) -> list[str]:
    out: list[str] = []
    for i in range(1, n + 1):
        s = ""
        if i % 3 == 0:
            s += "Fizz"
        if i % 5 == 0:
            s += "Buzz"
        out.append(s or str(i))
    return out


def pair_sum(xs: list[int], ys: list[int]) -> list[int]:
    # TODO: 使用 zip 合并两个列表
    return [a + b for a, b in zip(xs, ys)]


def find_first_even(xs: list[int]) -> int | None:
    # TODO: 使用 for/else 结构，如果没有找到偶数，返回 None
    for v in xs:
        if v % 2 == 0:
            return v
    else:
        return None


def run_self_check():
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert pair_sum([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert find_first_even([1, 3, 5]) is None
    assert find_first_even([1, 4, 5]) == 4

    print("02_control_flow ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
