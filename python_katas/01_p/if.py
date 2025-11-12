#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 条件判断

age = 20

if age >= 18:
    print("成年了")
else:
    print("未成年")


score = 85

if score >= 90:
    print("优秀")
elif score >= 75:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("可以进入电影院")
else:
    print("不允许进入")


age = 16
student = True

if age < 18:
    if student:
        print("学生票 5 元")
    else:
        print("未成年票 8 元")
else:
    print("成人票 12 元")
