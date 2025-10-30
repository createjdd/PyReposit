#!/usr/bin/env python3
from __future__ import annotations
from typing import Callable, Any

"""
主题: 函数
- 参数/返回值/注解
- 可变参数 *args/**kwargs
- 闭包
- 高阶函数(map/filter/reduce 思想)
"""

def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}!"


def apply_twice(f: Callable[[int], int], x: int) -> int:
    return f(f(x))


def make_adder(delta: int) -> Callable[[int], int]:
    def _inner(x: int) -> int:
        return x + delta
    return _inner


def use_kwargs(**kwargs: Any) -> list[tuple[str, Any]]:
    # TODO: 返回按 key 排序后的 (k, v) 列表
    return sorted(kwargs.items(), key=lambda kv: kv[0])


def run_self_check():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", prefix="Hi") == "Hi, Bob!"

    inc = lambda x: x + 1
    assert apply_twice(inc, 3) == 5

    add5 = make_adder(5)
    assert add5(10) == 15

    kv = use_kwargs(b=2, a=1, c=3)
    assert kv == [("a", 1), ("b", 2), ("c", 3)]

    print("03_functions ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
