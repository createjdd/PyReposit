#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件操作
# 读取所有内容
f = open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'r')
print(f.read())
f.close()

# 读取所有行
with open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'r') as f:
    print(f.read())

# 读取所有行
with open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'r') as f:
    for line in f:
        print(line)

# 读取所有行
with open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'r') as f:
    print(f.readlines())

# 四种读取方式的区别
# 1. read() 读取所有内容
# 2. readlines() 读取所有行
# 3. readline() 读取一行
# 4. for line in f: 读取所有行

# 写入文件
with open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'w') as f:
    f.write('Hello, World!')


# 追加写入文件
with open('/Users/xincheng/_work/PyReposit/python_katas/00_完整学习指南.md', 'a') as f:
    f.write('Hello, World!')

# with 的作用是自动关闭文件