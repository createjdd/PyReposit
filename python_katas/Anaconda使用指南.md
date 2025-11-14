#!/usr/bin/env python3

# -_- coding: utf-8 -_-

"""
Mac 安装 Anaconda 指南

## 方法 1: 使用 Homebrew (推荐)

在终端执行以下命令：

# 安装 Anaconda

brew install --cask anaconda

# 或者安装 Miniconda (更轻量，只包含 conda 和 Python)

brew install --cask miniconda

安装完成后，需要初始化 conda：
conda init zsh # 如果使用 zsh (Mac 默认)

# 或

conda init bash # 如果使用 bash

然后重启终端或执行：
source ~/.zshrc

验证安装：
conda --version
conda info

## 方法 2: 从官网下载安装包

1. 访问官网：https://www.anaconda.com/download
2. 选择 macOS 版本下载
3. 双击 .pkg 文件安装
4. 按照安装向导完成安装

## 安装后的基本使用

# 创建新环境

conda create -n myenv python=3.9

# 激活环境

conda activate myenv

# 安装包

conda install numpy pandas

# 查看已安装的包

conda list

# 退出环境

conda deactivate

# 查看所有环境

conda env list

# 删除环境

conda env remove -n myenv

## 安装不同版本的 Python

# 方法 1: 创建新环境时指定 Python 版本（推荐）

conda create -n py39 python=3.9 # 创建 Python 3.9 环境
conda create -n py310 python=3.10 # 创建 Python 3.10 环境
conda create -n py311 python=3.11 # 创建 Python 3.11 环境
conda create -n py312 python=3.12 # 创建 Python 3.12 环境

# 方法 2: 在现有环境中安装/更新 Python 版本

conda activate myenv
conda install python=3.9 # 安装指定版本
conda update python # 更新到最新版本

# 方法 3: 查看可用的 Python 版本

conda search python # 查看所有可用版本

# 方法 4: 创建环境时指定精确版本

conda create -n myproject python=3.9.18 # 指定精确版本号

# 使用示例：

# 1. 创建 Python 3.9 环境并安装包

conda create -n project1 python=3.9 numpy pandas

# 2. 激活环境

conda activate project1

# 3. 验证 Python 版本

python --version

# 4. 查看环境中的 Python 路径

which python

# 5. 在不同环境间切换

conda activate project1 # 切换到 Python 3.9
conda activate project2 # 切换到 Python 3.10
conda deactivate # 退出当前环境

## 注意事项

- Anaconda 比较大（约 3GB），如果只需要基础功能，推荐安装 Miniconda
- 安装后会在 ~/.zshrc 或 ~/.bash_profile 中添加 conda 初始化代码
- 如果不想每次打开终端都激活 base 环境，可以执行：
  conda config --set auto_activate_base false
  """

if **name** == '**main**':
print("这是 Anaconda 安装指南，请查看文件内容获取详细步骤")
