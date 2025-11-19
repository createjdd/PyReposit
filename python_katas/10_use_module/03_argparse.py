# argparse 模块是 Python 标准库中的一个模块，用于解析命令行参数。

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, default='world')
parser.add_argument('--age', type=int, default=18)
args = parser.parse_args()

print(f'Hello, {args.name}! You are {args.age} years old.')

# 运行方式：python 03_argparse.py --name Tom --age 20