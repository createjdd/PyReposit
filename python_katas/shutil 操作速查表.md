# 🧰 shutil 文件操作速查表

Python 的 `shutil` 模块提供了方便的文件、目录复制、移动、压缩等高级操作。

---

## 📦 一、复制相关

| 功能                                   | 方法                                                                         | 示例                                       |
| -------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------ |
| 复制文件（不带元数据）                 | `shutil.copy(src, dst)`                                                      | `shutil.copy('a.txt', 'backup/a.txt')`     |
| 复制文件（保留权限、修改时间等元数据） | `shutil.copy2(src, dst)`                                                     | `shutil.copy2('a.txt', 'backup/a.txt')`    |
| 复制整个目录（递归）                   | `shutil.copytree(src, dst)`                                                  | `shutil.copytree('mydir', 'backup/mydir')` |
| 忽略部分文件复制                       | `shutil.copytree(src, dst, ignore=shutil.ignore_patterns('*.tmp', '*.log'))` | 忽略临时文件                               |
| 复制文件权限（不复制内容）             | `shutil.copymode(src, dst)`                                                  | `shutil.copymode('a.txt', 'b.txt')`        |
| 复制文件状态信息（权限、时间戳）       | `shutil.copystat(src, dst)`                                                  | `shutil.copystat('a.txt', 'b.txt')`        |

---

## 🚚 二、移动与删除

| 功能                   | 方法                                      | 示例                            |
| ---------------------- | ----------------------------------------- | ------------------------------- |
| 移动文件或目录         | `shutil.move(src, dst)`                   | `shutil.move('a.txt', '/tmp/')` |
| 删除整个目录           | `shutil.rmtree(path)`                     | `shutil.rmtree('old_backup')`   |
| 安全删除（带错误忽略） | `shutil.rmtree(path, ignore_errors=True)` | 避免异常中断                    |

---

## 🗜️ 三、压缩与解压

| 功能                           | 方法                                               | 示例                                                     |
| ------------------------------ | -------------------------------------------------- | -------------------------------------------------------- |
| 创建压缩包（zip/tar/gztar 等） | `shutil.make_archive(base_name, format, root_dir)` | `shutil.make_archive('backup', 'zip', 'project_folder')` |
| 解压压缩包                     | `shutil.unpack_archive(filename, extract_dir)`     | `shutil.unpack_archive('backup.zip', 'output_folder')`   |
| 支持的压缩格式                 | `zip`, `tar`, `gztar`, `bztar`, `xztar`            | 多平台兼容                                               |

---

## 🧰 四、临时文件与目录（进阶）

| 功能               | 方法                                           | 示例         |
| ------------------ | ---------------------------------------------- | ------------ |
| 复制文件到临时目录 | `shutil.copy2('a.txt', tempfile.gettempdir())` | 临时处理文件 |
| 清空临时缓存目录   | `shutil.rmtree(tempfile.gettempdir())`         | 清理缓存     |

---

## 💡 小技巧

1. ✅ `copytree` 默认要求目标目录不存在，可以传 `dirs_exist_ok=True`（Python 3.8+）

   ```python
   shutil.copytree('src', 'dst', dirs_exist_ok=True)
   ```

2. ✅ 用于备份文件夹最方便的组合：

   ```python
   import shutil
   shutil.make_archive('backup/myproject', 'zip', 'myproject')
   ```

3. ✅ 用于同步文件夹（可写成简单的部署脚本）：
   ```python
   shutil.rmtree('dist', ignore_errors=True)
   shutil.copytree('src', 'dist')
   ```

---

> 🧩 **提示**：`shutil` 是文件管理脚本中最常用的模块之一，配合 `os`、`pathlib` 使用更强大。
