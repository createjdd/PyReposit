from io import StringIO
from io import BytesIO

# 创建一个内存文件对象
f = StringIO()

# 写入文本
f.write('Hello, ')
f.write('World!')

# 移动到开头
f.seek(0)

# 读取内容
print(f.read())  # 输出：Hello, World!


# 直接初始化内存文件对象
f = StringIO('Hello, World!000')
print(f.read())  # 输出：Hello, World!

# 创建一个内存文件对象
f = BytesIO()

# 写入二进制数据
f.write('Hello, '.encode('utf-8'))
f.write('World!'.encode('utf-8'))

# 移动到开头
f.seek(0)

# 读取内容
print(f.read().decode('utf-8'))  # 输出：Hello, World!