#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Anaconda 常用库快速示例
演示最常用的库和函数
"""

# ==================== 1. NumPy - 数值计算 ====================
print("=" * 50)
print("1. NumPy 示例")
print("=" * 50)

import numpy as np

# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(f"数组: {arr}")
print(f"数组形状: {arr.shape}")
print(f"数组求和: {arr.sum()}")
print(f"数组平均值: {arr.mean()}")

# 创建矩阵
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(f"矩阵:\n{matrix}")

print("\n")


# ==================== 2. Pandas - 数据分析 ====================
print("=" * 50)
print("2. Pandas 示例")
print("=" * 50)

import pandas as pd

# 创建 DataFrame
data = {
    '姓名': ['张三', '李四', '王五'],
    '年龄': [25, 30, 35],
    '城市': ['北京', '上海', '广州']
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print(f"\n数据形状: {df.shape}")
print(f"列名: {df.columns.tolist()}")
print(f"平均年龄: {df['年龄'].mean()}")

print("\n")


# ==================== 3. Matplotlib - 数据可视化 ====================
print("=" * 50)
print("3. Matplotlib 示例")
print("=" * 50)

import matplotlib.pyplot as plt

# 创建示例数据
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 绘制图表（注释掉，避免在非交互式环境中出错）
# plt.figure(figsize=(8, 6))
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('X轴')
# plt.ylabel('Y轴')
# plt.title('正弦函数图像')
# plt.legend()
# plt.grid(True)
# plt.savefig('sin_plot.png')
# print("图表已保存为 sin_plot.png")
print("Matplotlib 可用于绘制各种图表")
print("常用函数: plt.plot(), plt.scatter(), plt.bar(), plt.hist()")

print("\n")


# ==================== 4. Requests - HTTP 请求 ====================
print("=" * 50)
print("4. Requests 示例")
print("=" * 50)

import requests

# 示例：发送 GET 请求（注释掉，避免实际请求）
# response = requests.get('https://api.github.com')
# print(f"状态码: {response.status_code}")
# print(f"响应内容类型: {response.headers['Content-Type']}")
print("Requests 用于发送 HTTP 请求")
print("常用函数: requests.get(), requests.post()")

print("\n")


# ==================== 5. 常用库列表 ====================
print("=" * 50)
print("Anaconda 预装的主要库列表")
print("=" * 50)

libraries = {
    "NumPy": "数值计算、数组操作",
    "Pandas": "数据分析、数据处理",
    "Matplotlib": "数据可视化、绘图",
    "SciPy": "科学计算、统计、优化",
    "Scikit-learn": "机器学习",
    "Jupyter": "交互式笔记本",
    "IPython": "增强的交互式 shell",
    "Requests": "HTTP 请求库",
    "BeautifulSoup4": "HTML/XML 解析",
    "Pillow": "图像处理",
    "Seaborn": "统计可视化",
    "Plotly": "交互式可视化",
}

for lib, desc in libraries.items():
    print(f"  • {lib:20s} - {desc}")

print("\n")


# ==================== 6. 查看已安装的库 ====================
print("=" * 50)
print("查看当前环境中的库")
print("=" * 50)
print("在终端运行: conda list")
print("或使用 Python: import sys; print(sys.modules.keys())")

print("\n")


# ==================== 7. 常用函数速查 ====================
print("=" * 50)
print("常用函数速查")
print("=" * 50)

print("""
NumPy:
  - np.array()         创建数组
  - np.zeros()         创建全零数组
  - np.ones()          创建全一数组
  - np.arange()        创建序列数组
  - arr.sum()          求和
  - arr.mean()         平均值

Pandas:
  - pd.read_csv()      读取 CSV
  - df.head()          查看前几行
  - df.describe()      统计描述
  - df.groupby()       分组
  - df.merge()         合并数据

Matplotlib:
  - plt.plot()         折线图
  - plt.scatter()      散点图
  - plt.bar()          柱状图
  - plt.show()         显示图表
  - plt.savefig()      保存图表
""")

if __name__ == '__main__':
    print("\n✅ 示例运行完成！")
    print("📚 更多详细信息请查看: anaconda_常用库指南.md")

