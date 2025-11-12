# 生成 0~9 的平方列表
squares = [x**2 for x in range(10)]
print(squares)
# 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 只保留偶数的平方
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)
# 输出: [0, 4, 16, 36, 64]


words = ["apple", "banana", "cherry"]
upper_words = [w.upper() for w in words]
print(upper_words)
# 输出: ['APPLE', 'BANANA', 'CHERRY']


gen = (x**2 for x in range(10))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)
# 不能重复遍历  没有输出

def f(x):
 return x ** 2

r = map(f, [1,2,3,4,5,6,7,8,9])

li = []
for item in r:
 li.append(item)

print(li)


# ===============-=-====-=-=-====================reduce=======
from functools import reduce

nums = [1, 2, 3, 4, 5]

# 定义一个累加函数
def add(a, b):
    return a + b

result = reduce(add, nums)
print(result)   # 输出 15

results = reduce(lambda a, b: a + b, nums)
print(results)   # 输出 15


# ==================================================filter============
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)
# 结果: [1, 5, 9, 15]

print(sorted([9,7,5,4,6,4,3,76]))
