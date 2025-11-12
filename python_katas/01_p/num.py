# 整数 int
a = 10

# 浮点数 float
b = 3.5

# 复数 complex
c = 2 + 3j

# 布尔值 bool
d = True  # 相当于数字 1


print("=== int + float ===")
print(a + b)   # 自动变成 float → 13.5

print("=== int // int ===")
print(7 // 3)  # 整除（向下取整）→ 2

print("=== int ** int ===")
print(2 ** 3)  # 幂运算 → 8

print("=== float 四舍五入 ===")
print(round(3.14159, 2))  # → 3.14

print("=== int + bool ===")
print(a + d)   # True 相当于 1 → 11

print("=== int + complex ===")
print(a + c)   # → (12 + 3j)

print("=== complex * complex ===")
print((1 + 2j) * (2 + 3j))  # → (-4 + 7j)
