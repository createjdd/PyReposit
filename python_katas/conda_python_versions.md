# Conda 安装不同版本 Python 完整指南

## 前置步骤：接受服务条款（首次使用需要）

如果遇到 "Terms of Service have not been accepted" 错误，需要先接受：

```bash
# 方法 1: 交互式接受（推荐）
conda tos accept

# 方法 2: 手动接受特定频道
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

---

## 方法 1: 创建新环境时指定 Python 版本（最推荐）

### 基本语法

```bash
conda create -n 环境名 python=版本号
```

### 实际示例

```bash
# 创建 Python 3.9 环境
conda create -n py39 python=3.9

# 创建 Python 3.10 环境
conda create -n py310 python=3.10

# 创建 Python 3.11 环境
conda create -n py311 python=3.11

# 创建 Python 3.12 环境
conda create -n py312 python=3.12

# 创建环境并同时安装包
conda create -n myproject python=3.9 numpy pandas jupyter

# 指定精确版本号
conda create -n myproject python=3.9.18
```

### 使用环境

```bash
# 激活环境
conda activate py39

# 验证 Python 版本
python --version

# 查看 Python 路径
which python

# 退出环境
conda deactivate
```

---

## 方法 2: 在现有环境中安装/更新 Python

```bash
# 激活现有环境
conda activate myenv

# 安装指定版本的 Python
conda install python=3.9

# 更新到最新版本
conda update python
```

**注意**：这种方法可能会影响已安装的包，建议使用方法 1 创建新环境。

---

## 方法 3: 查看可用的 Python 版本

```bash
# 查看所有可用的 Python 版本
conda search python

# 查看特定主版本的可用版本
conda search "python=3.9"

# 查看特定小版本的可用版本
conda search "python=3.9.18"
```

---

## 完整工作流程示例

### 场景：需要同时维护 Python 3.9 和 3.11 的项目

```bash
# 1. 创建 Python 3.9 环境
conda create -n project-old python=3.9 numpy pandas -y
conda activate project-old
python --version  # 应该显示 Python 3.9.x

# 2. 创建 Python 3.11 环境
conda deactivate
conda create -n project-new python=3.11 numpy pandas -y
conda activate project-new
python --version  # 应该显示 Python 3.11.x

# 3. 在不同环境间切换
conda activate project-old   # 切换到 3.9
conda activate project-new   # 切换到 3.11
conda deactivate            # 退出到 base

# 4. 查看所有环境
conda env list
```

---

## 常用命令速查

```bash
# 创建环境
conda create -n 环境名 python=版本号

# 激活环境
conda activate 环境名

# 退出环境
conda deactivate

# 查看所有环境
conda env list
# 或
conda info --envs

# 删除环境
conda env remove -n 环境名

# 查看当前环境的 Python 版本
python --version

# 查看当前环境的 Python 路径
which python

# 查看环境中安装的包
conda list

# 导出环境配置（类似 package.json）
conda env export > environment.yml

# 从配置文件创建环境
conda env create -f environment.yml
```

---

## 最佳实践

1. **为每个项目创建独立环境**：避免包冲突
2. **使用有意义的环境名**：如 `project-name-py39` 而不是 `env1`
3. **记录环境配置**：使用 `conda env export > environment.yml` 保存配置
4. **定期清理**：删除不再使用的环境 `conda env remove -n 环境名`

---

## 常见问题

### Q: 如何知道应该用哪个 Python 版本？

A: 查看项目要求，或使用 `conda search python` 查看可用版本。

### Q: 可以同时安装多个 Python 版本吗？

A: 可以！每个 conda 环境可以有独立的 Python 版本，互不干扰。

### Q: 如何切换不同版本的 Python？

A: 使用 `conda activate 环境名` 在不同环境间切换。

### Q: 安装 Python 版本需要多长时间？

A: 通常几分钟，取决于网络速度和版本大小。

### Q: 可以修改 base 环境的 Python 版本吗？

A: 可以但不推荐，建议创建新环境。
