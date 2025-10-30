#!/usr/bin/env python3
from __future__ import annotations

"""
主题: 异常处理
- try/except/else/finally
- 自定义异常
- raise
"""

class NegativeError(ValueError):
    pass


def sqrt_non_negative(x: float) -> float:
    if x < 0:
        raise NegativeError("x must be non-negative")
    return x ** 0.5


def parse_int_safe(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


def run_self_check():
    assert sqrt_non_negative(9) == 3
    try:
        sqrt_non_negative(-1)
    except NegativeError:
        pass
    else:
        raise AssertionError("NegativeError 未抛出")

    assert parse_int_safe("123") == 123
    assert parse_int_safe("abc") is None

    print("07_exceptions ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
