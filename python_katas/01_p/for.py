#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 循环语句

fruits = ["apple", "banana", "cherry"]

for item in fruits:
    print(item)

for item in range(5):
  print(item)

person = {"name": "Tom", "age": 25}

for key,val in person.items():
  print(key, val)

count = 0
while count < 4:
    print("计数:", count)
    count += 1

n = 1
while True:
    if n > 5:
        break  # 提前终止
    print("当前 n =", n)
    n += 1

for i in range(1, 6):
    if i == 3:
        continue  # 跳过 3
    print("数字:", i)
