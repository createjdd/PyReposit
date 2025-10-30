#!/usr/bin/env python3
from __future__ import annotations
from typing import Iterable, Iterator

"""
主题: 迭代器与生成器
- iter/next 协议
- 生成器函数与表达式
- 惰性处理
"""

def count_up(start: int, stop: int) -> Iterator[int]:
    cur = start
    while cur <= stop:
        yield cur
        cur += 1


def take(n: int, it: Iterable[int]) -> list[int]:
    out: list[int] = []
    for i, v in enumerate(it):
        if i >= n:
            break
        out.append(v)
    return out


def gen_squares(xs: Iterable[int]) -> Iterator[int]:
    # TODO: 生成每个元素的平方（生成器表达式也可）
    for x in xs:
        yield x * x


def run_self_check():
    assert list(count_up(3, 5)) == [3, 4, 5]
    assert take(3, range(10)) == [0, 1, 2]
    assert list(gen_squares([2, 3, 4])) == [4, 9, 16]

    print("08_iterators_generators ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
