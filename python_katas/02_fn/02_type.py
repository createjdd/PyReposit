#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 数值类型之间的转换
a = 3.7
b = int(a)        # 浮点 -> 整数（去掉小数部分）
c = float(5)      # 整数 -> 浮点
print(b, c)       # 输出: 3 5.0

# 字符串和数字互转
s = "123"
num = int(s)      # 字符串 -> 整数
text = str(456)   # 整数 -> 字符串
print(num + 10)   # 输出: 133
print("结果是：" + text)  # 输出: 结果是：456

# 字符串转浮点
f = float("3.14")
print(f + 1)      # 输出: 4.14

# 列表、元组、集合互转
lst = [1, 2, 3, 3]
tup = tuple(lst)        # 列表 -> 元组
st = set(lst)           # 列表 -> 集合（去重）
new_list = list(st)     # 集合 -> 列表
print(tup, st, new_list)

# bool 转换
print(bool(0))          # False
print(bool(""))         # False
print(bool("Hello"))    # True
print(bool(123))        # True
