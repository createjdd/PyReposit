# Python 常见数据类型示例

# 1. 数字类型（Number）
a_int = 10               # 整数 int
b_float = 3.14           # 浮点数 float
c_complex = 2 + 3j       # 复数 complex
print(a_int, b_float, c_complex)

# 2. 字符串（String）
s = "Hello, Python!"
print(s, s[0], s[-1])    # 字符串支持索引和切片

# 3. 布尔值（Boolean）
is_active = True
print(is_active, not is_active)

# 4. 列表（List）——可变序列
lst = [1, 2, 3, "apple"]
lst.append("banana")
print(lst)

# 5. 元组（Tuple）——不可变序列
tup = (10, 20, 30)
print(tup)

# 6. 集合（Set）——无序、不重复
st = {1, 2, 2, 3}
st.add(4)
print(st)

# 7. 字典（Dict）——键值对
person = {"name": "Tom", "age": 25}
print(person["name"], person.get("age"))

# 8. None 类型——空值
x = None
print(x)
