👍 好的～那我来帮你准备一个最实用的

# 🧭 `pathlib` 常用方法速查表 + 示例（超简洁版）

---

## 🏁 一、导入与创建路径

```python
from pathlib import Path

p = Path('/Users/xincheng/Desktop')   # 绝对路径
q = Path('notes.txt')                 # 相对路径
```

---

## 📁 二、路径拼接与信息获取

| 操作             | 写法             | 说明                |
| ---------------- | ---------------- | ------------------- |
| 拼接路径         | `p / 'file.txt'` | 使用 `/` 拼接子路径 |
| 获取上级目录     | `p.parent`       | 返回父路径          |
| 获取文件名       | `p.name`         | 含扩展名            |
| 获取文件后缀     | `p.suffix`       | 如 `.txt`           |
| 去掉后缀的文件名 | `p.stem`         | 文件名不含扩展名    |
| 判断是否存在     | `p.exists()`     | 返回 True/False     |
| 是否是文件       | `p.is_file()`    |                     |
| 是否是目录       | `p.is_dir()`     |                     |

📘 示例：

```python
f = Path('/Users/xincheng/Desktop/demo.txt')
print(f.parent)   # /Users/xincheng/Desktop
print(f.stem)     # demo
print(f.suffix)   # .txt
```

---

## 🧱 三、目录操作

| 操作         | 写法                                   | 说明           |
| ------------ | -------------------------------------- | -------------- |
| 创建单层目录 | `p.mkdir()`                            | 若已存在会报错 |
| 递归创建多层 | `p.mkdir(parents=True, exist_ok=True)` | 推荐           |
| 删除空目录   | `p.rmdir()`                            | 仅删除空文件夹 |
| 遍历目录     | `for f in p.iterdir(): ...`            | 返回 Path 对象 |

📘 示例：

```python
(p / 'test_folder').mkdir(parents=True, exist_ok=True)
for f in p.iterdir():
    print(f)
```

---

## 📜 四、文件操作

| 操作       | 写法                     | 说明       |
| ---------- | ------------------------ | ---------- |
| 写入文本   | `p.write_text("hello")`  | 自动覆盖   |
| 读取文本   | `p.read_text()`          | 返回字符串 |
| 写入二进制 | `p.write_bytes(b'data')` |            |
| 读取二进制 | `p.read_bytes()`         |            |

📘 示例：

```python
file = p / 'hello.txt'
file.write_text('Hello World!')
print(file.read_text())
```

---

## 🧭 五、路径遍历与过滤

```python
# 遍历当前文件夹所有文件
for f in p.iterdir():
    print(f)

# 递归查找特定类型文件
for f in p.rglob('*.py'):
    print(f)
```

---

## 🚀 六、结合 `shutil` 的高级操作

```python
import shutil

src = Path('data.txt')
dst = Path('backup.txt')

shutil.copy(src, dst)     # 复制
shutil.move(dst, 'temp/') # 移动
shutil.rmtree('old_dir')  # 删除整个目录
```

---

## 🧩 七、实战例子：批量重命名 `.txt` 文件

```python
from pathlib import Path

p = Path('.')
for f in p.glob('*.txt'):
    new_name = f.with_stem('new_' + f.stem)
    f.rename(new_name)
```

---

## ✅ 八、总结对比

| 功能              | 方法                                      | 示例 |
| ----------------- | ----------------------------------------- | ---- |
| 判断文件/目录存在 | `.exists()`                               |      |
| 创建目录          | `.mkdir(parents=True)`                    |      |
| 读取/写入文本     | `.read_text()` / `.write_text()`          |      |
| 拼接路径          | `/` 运算符                                |      |
| 遍历文件          | `.iterdir()` / `.rglob()`                 |      |
| 重命名            | `.rename()`                               |      |
| 删除              | `.unlink()`（文件）/ `.rmdir()`（空目录） |      |

---

是否希望我下一步帮你整理一份
👉 **「`shutil` 文件复制/压缩/移动操作速查表」**
配合 `pathlib` 一起使用的实战参考？
