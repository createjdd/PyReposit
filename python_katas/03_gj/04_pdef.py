#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 偏函数

from functools import partial

def power(base, exp):
    return base ** exp

# 创建一个新的函数，固定 base=2
square = partial(power, 2)

print(square(3))  # 相当于 power(2, 3) → 8
print(square(5))  # 相当于 power(2, 5) → 32

print(int("10", base=2))  # 结果是 2
print(int("10", base=8))  # 结果是 8

# 偏函数使用场景
# 1. 当一个函数有很多参数时，我们只想固定其中的一部分参数，可以使用偏函数
