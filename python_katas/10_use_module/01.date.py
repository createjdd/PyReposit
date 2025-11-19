#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datetime 模块使用示例
演示日期和时间的常用操作
"""

from datetime import datetime, timedelta, timezone

# 1. 获取当前日期和时间
now = datetime.now()
print(f"当前时间: {now}")

# 2. 格式化日期和时间
formatted = now.strftime('%Y-%m-%d %H:%M:%S')
print(f"格式化后: {formatted}")

# 3. 解析日期和时间字符串
date_str = '2025-11-18 10:00:00'
parsed_date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
print(f"解析后的日期: {parsed_date}")

# 4. 计算日期和时间（加天数）
tomorrow = now + timedelta(days=1)
print(f"明天: {tomorrow}")

# 5. 计算日期和时间差（减天数）
yesterday = now - timedelta(days=1)
print(f"昨天: {yesterday}")

# 6. 本地时间转换为UTC时间
utc_now = now.astimezone(timezone.utc)
print(f"UTC时间: {utc_now}")

# 7. 计算日期和时间差（加小时）
future_time = now + timedelta(hours=2)
print(f"2小时后: {future_time}")

# 8. 计算日期和时间差（加周数）
next_week = now + timedelta(weeks=1)
print(f"一周后: {next_week}")

# 9. 计算两个日期之间的差值
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 12, 31)
diff = date2 - date1
print(f"日期差: {diff.days} 天")

# 10. 创建指定时区的时间
beijing_tz = timezone(timedelta(hours=8))  # 东八区（北京时间）
beijing_time = datetime.now(beijing_tz)
print(f"北京时间: {beijing_time}")