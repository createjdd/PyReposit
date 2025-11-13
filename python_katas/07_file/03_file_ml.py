import os

print(os.name) # 操作系统类型
print(os.environ) # 环境变量
print(os.environ.get('PATH')) # 路径
print(os.environ.get('HOME')) # 用户主目录
print(os.environ.get('USER')) # 用户名
print(os.getcwd()) # 当前工作目录

files = os.listdir('.')
print(files)

#判断路径类型
print(os.path.exists('test.txt'))   # 是否存在
print(os.path.isfile('test.txt'))   # 是否为文件
print(os.path.isdir('my_folder'))   # 是否为目录

# 创建和删除目录
# 先删除已存在的目录（如果存在）
if os.path.exists('demo'):
    os.rmdir('demo')      # 删除已存在的目录
if os.path.exists('a'):
    import shutil
    shutil.rmtree('a')    # 递归删除整个目录树

os.mkdir('demo')          # 创建单级目录
os.makedirs('a/b/c')      # 递归创建多级目录

print("\n创建目录后:")
print(f"demo 目录存在: {os.path.exists('demo')}")
print(f"a/b/c 目录存在: {os.path.exists('a/b/c')}")

os.rmdir('demo')          # 删除单级目录（必须为空）
os.removedirs('a/b/c')    # 递归删除多级空目录

print("\n删除目录后:")
print(f"demo 目录存在: {os.path.exists('demo')}")
print(f"a/b/c 目录存在: {os.path.exists('a/b/c')}")

# pathlib 库 组合使用 os比较适合老旧的系统接口
from pathlib import Path
import shutil

p = Path('/Users/xincheng/Desktop')

# 创建目录
(p / 'test_folder').mkdir(exist_ok=True)

# 写文件
(p / 'test_folder/file.txt').write_text('hello, world!')

# 读文件
print((p / 'test_folder/file.txt').read_text())

# 复制文件（shutil 辅助）
shutil.copy(p / 'test_folder/file.txt', p / 'file_copy.txt')

# 遍历文件夹
for f in p.iterdir():
    print(f)
