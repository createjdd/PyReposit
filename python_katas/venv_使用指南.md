# Python 虚拟环境（venv）使用指南

## 📚 什么是 venv？

`venv` 是 Python 3.3+ 内置的虚拟环境管理工具，用于创建独立的 Python 环境，避免不同项目之间的依赖冲突。

## 🎯 为什么使用 venv？

- ✅ **隔离依赖**：每个项目有独立的包环境
- ✅ **版本管理**：不同项目可以使用不同版本的包
- ✅ **避免冲突**：不会污染系统 Python 环境
- ✅ **易于部署**：可以导出依赖列表

---

## 🚀 快速开始

### 1. 创建虚拟环境

```bash
# 在项目根目录下创建虚拟环境
python3 -m venv venv

# 或者指定其他名称
python3 -m venv env
python3 -m venv .venv
```

**注意**：

- `venv` 是虚拟环境文件夹的名称，可以自定义
- 建议使用 `venv` 或 `.venv`（隐藏文件夹）

### 2. 激活虚拟环境

#### macOS / Linux:

```bash
# 如果创建的是 venv
source venv/bin/activate

# 如果创建的是 env
source env/bin/activate

# 如果创建的是 .venv
source .venv/bin/activate
```

**激活成功的标志**：

- 命令行前面会出现 `(venv)` 或 `(env)` 标识
- 例如：`(venv) ➜  python_katas git:(main) ✗`

#### Windows:

```bash
# 如果创建的是 venv
venv\Scripts\activate

# 如果创建的是 env
env\Scripts\activate
```

### 3. 验证虚拟环境

```bash
# 查看 Python 路径（应该指向虚拟环境）
which python    # macOS/Linux
where python    # Windows

# 查看 Python 版本
python --version

# 查看 pip 路径
which pip       # macOS/Linux
where pip       # Windows
```

### 4. 安装包

```bash
# 激活虚拟环境后，使用 pip 安装包
pip install requests
pip install pandas numpy

# 从 requirements.txt 安装
pip install -r requirements.txt
```

### 5. 退出虚拟环境

```bash
deactivate
```

退出后，命令行前面的 `(venv)` 标识会消失。

---

## 📝 完整工作流程示例

### 场景：为新项目设置虚拟环境

```bash
# 1. 进入项目目录
cd /Users/xincheng/_work/PyReposit/python_katas

# 2. 创建虚拟环境
python3 -m venv venv

# 3. 激活虚拟环境
source venv/bin/activate

# 4. 升级 pip（推荐）
pip install --upgrade pip

# 5. 安装项目依赖
pip install requests pandas numpy

# 6. 生成依赖列表（可选）
pip freeze > requirements.txt

# 7. 使用虚拟环境
python your_script.py

# 8. 退出虚拟环境（完成后）
deactivate
```

---

## 🔧 常用命令

### 查看已安装的包

```bash
pip list                    # 列出所有已安装的包
pip show package_name       # 查看特定包的详细信息
```

### 导出和导入依赖

```bash
# 导出依赖列表
pip freeze > requirements.txt

# 从依赖列表安装
pip install -r requirements.txt
```

### 卸载包

```bash
pip uninstall package_name
```

### 升级包

```bash
pip install --upgrade package_name
```

---

## ⚠️ 常见问题

### 问题 1：`source: no such file or directory: venv/bin/activate`

**原因**：

- 虚拟环境名称不匹配（创建的是 `env` 但尝试激活 `venv`）
- 虚拟环境未创建成功
- 路径不正确

**解决方法**：

```bash
# 检查当前目录下是否有虚拟环境文件夹
ls -la | grep venv
ls -la | grep env

# 如果创建的是 env，使用：
source env/bin/activate

# 如果创建的是 venv，使用：
source venv/bin/activate
```

### 问题 2：找不到 python3 命令

**解决方法**：

```bash
# macOS/Linux: 使用 python3
python3 -m venv venv

# 或者找到 Python 的完整路径
which python3
/usr/bin/python3 -m venv venv
```

### 问题 3：权限错误

**解决方法**：

```bash
# 确保有写入权限
chmod +w .

# 或者使用 sudo（不推荐，会创建系统级虚拟环境）
```

### 问题 4：虚拟环境已激活但 pip 安装到系统

**检查方法**：

```bash
# 查看 pip 路径
which pip

# 应该显示虚拟环境路径，例如：
# /Users/xincheng/_work/PyReposit/python_katas/venv/bin/pip
```

---

## 📂 项目结构示例

```
python_katas/
├── venv/                  # 虚拟环境（不要提交到 Git）
│   ├── bin/              # 可执行文件
│   ├── lib/              # Python 库
│   └── pyvenv.cfg        # 配置文件
├── requirements.txt      # 依赖列表（应该提交到 Git）
├── .gitignore           # 忽略 venv 文件夹
└── your_scripts.py      # 你的代码
```

---

## 🔒 Git 集成

### .gitignore 配置

在项目根目录创建或编辑 `.gitignore` 文件：

```gitignore
# 虚拟环境
venv/
env/
.venv/
ENV/
env.bak/
venv.bak/

# Python 缓存
__pycache__/
*.py[cod]
*$py.class
*.so

# 分发/打包
dist/
build/
*.egg-info/
```

### 提交依赖列表

```bash
# 生成 requirements.txt
pip freeze > requirements.txt

# 提交到 Git
git add requirements.txt
git commit -m "Add requirements.txt"
```

**注意**：只提交 `requirements.txt`，不要提交 `venv/` 文件夹！

---

## 💡 最佳实践

1. **每个项目一个虚拟环境**

   - 为每个项目创建独立的虚拟环境
   - 不要在不同项目间共享虚拟环境

2. **使用 requirements.txt**

   - 始终维护 `requirements.txt`
   - 团队成员可以通过它重建相同的环境

3. **激活虚拟环境后再工作**

   - 每次开始工作前先激活虚拟环境
   - 完成后记得退出

4. **定期更新依赖**

   ```bash
   pip install --upgrade pip
   pip list --outdated
   ```

5. **使用 .venv 作为隐藏文件夹**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

---

## 🔄 与其他工具对比

| 工具           | 特点                             | 适用场景              |
| -------------- | -------------------------------- | --------------------- |
| **venv**       | Python 内置，简单易用            | 标准 Python 项目      |
| **virtualenv** | 功能更强大，支持更多 Python 版本 | 需要兼容旧版本 Python |
| **conda**      | 包管理器 + 环境管理              | 数据科学、科学计算    |
| **poetry**     | 依赖管理 + 打包                  | 大型项目、库开发      |

---

## 📖 相关资源

- [Python venv 官方文档](https://docs.python.org/3/library/venv.html)
- [pip 官方文档](https://pip.pypa.io/)

---

## ✅ 快速检查清单

- [ ] 创建虚拟环境：`python3 -m venv venv`
- [ ] 激活虚拟环境：`source venv/bin/activate`
- [ ] 升级 pip：`pip install --upgrade pip`
- [ ] 安装依赖：`pip install package_name`
- [ ] 生成依赖列表：`pip freeze > requirements.txt`
- [ ] 添加到 .gitignore：`venv/`
- [ ] 退出虚拟环境：`deactivate`

---

**最后更新**：2025 年 1 月
