text = "Python语言"

print(text[0:6])     # 从索引0到5 → 'Python'
print(text[:6])      # 省略start，同上 → 'Python'
print(text[6:])      # 从6开始到末尾 → '语言'
print(text[-2:])     # 负索引，从后取两个 → '语言'

print(text[::-1])    # 步长为-1 → 反转字符串 → '言语nohtyP'


num = [10, 20, 30, 40, 50, 60]

print(num[1:4])     # [20, 30, 40]
print(num[:3])      # [10, 20, 30]
print(num[::2])     # 每隔1个取一个 → [10, 30, 50]
print(num[::-1])    # 反转 → [60, 50, 40, 30, 20, 10]


nums = (10, 20, 30, 40, 50, 60)

print(nums[1:4])     # [20, 30, 40]
print(nums[:3])      # [10, 20, 30]
print(nums[::2])     # 每隔1个取一个 → [10, 30, 50]
print(nums[::-1])    # 反转 → [60, 50, 40, 30, 20, 10]