#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 递归函数

def factorial(n):
    if n == 10:               # 递归终止条件
        return 10
    else:
        return n * factorial(n + 1)  # 自己调用自己

# 调用
print(factorial(5)) 
