#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 函数基础

def say_hello():
    print("你好，Python！")

say_hello()

def greet(name):
    print("你好，" + name + "！")

greet("小明")
greet("小红")



def add(a, b):
    return a + b

result = add(5, 3)
print("结果:", result)


def power(base, exp=2):
    return base ** exp

print(power(3))      # 默认指数是2 → 9
print(power(2, 3))   # 自定义指数 → 8

# ==========================================================
def show_info(*args, **kwargs):
    print("位置参数:", args)
    print("关键字参数:", kwargs)

show_info("Tom", 25, city="Beijing", job="Dev")
