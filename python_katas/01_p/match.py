#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 模式匹配（Python 3.10+）

command = "start"

match command:
    case "start":
        print("程序启动中...")
    case "stop":
        print("程序已停止。")
    case "restart":
        print("程序重新启动中...")
    case _:
        print("未知指令！")


color = "red"

match color:
    case "red" | "blue" | "green":
        print("这是一个基本颜色。")
    case "black" | "white":
        print("这是一个中性色。")
    case _:
        print("未知颜色。")

point = (10, 20)

match point:
    case (0, 0):
        print("原点")
    case (x, 0):
        print(f"在 X 轴上, x={x}")
    case (0, y):
        print(f"在 Y 轴上, y={y}")
    case (x, y):
        print(f"普通点 ({x}, {y})")



user = {"name": "Tom", "role": "admin"}

match user:
    case {"role": "admin"}:
        print("欢迎管理员登录")
    case {"role": "user"}:
        print("普通用户登录")
    case _:
        print("未知身份")
