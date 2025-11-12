#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 闭包和装饰器

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,2,3,4,5,6)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

# “装饰器（Decorator）” 是 Python 的一个进阶又非常实用的语法糖，
# 它让我们能在不修改原函数代码的前提下，
# 为函数添加额外功能（例如日志、权限校验、耗时统计等）。

def decorator(func):
    def wrapper():
        print("执行前")
        func()
        print("执行后")
    return wrapper


@decorator
def say_hello():
    print("Hello!")

say_hello()




def logger(func):
    def wrapper(*args, **kwargs):
        print(f"开始执行: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"执行完毕: {func.__name__}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(3, 5))


# | 场景       | 示例        |
# | -------- | --------- |
# | **日志记录** | 打印函数调用信息  |
# | **性能统计** | 统计函数运行时间  |
# | **权限验证** | 判断用户是否登录  |
# | **缓存结果** | 减少重复计算    |
# | **输入校验** | 检查参数类型或格式 |


import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行耗时: {end - start:.4f} 秒")
        return result
    return wrapper

@timer
def slow_func():
    time.sleep(1)
    print("运行完毕")

slow_func()


# 带参数的装饰器
def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] 开始执行 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{level}] 执行结束 {func.__name__}")
            return result
        return wrapper
    return decorator

@log("INFO")
def work():
    print("正在工作...")

work()

