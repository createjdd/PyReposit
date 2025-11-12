s = "Hello, Python!"

print(s[0])       # 取第一个字符 → 'H'
print(s[-1])      # 取最后一个字符 → '!'
print(s[0:5])     # 切片 → 'Hello'
print(s.lower())  # 全部小写
print(s.upper())  # 全部大写
print(len(s))     # 字符串长度 → 14
print("Python" in s)  # 是否包含子串 → True
print(s.replace("Python", "World"))  # 替换子串


text = "你好"
b = text.encode("utf-8")
print(b)  # 输出：b'\xe4\xbd\xa0\xe5\xa5\xbd'


s = b.decode("utf-8")
print(s)  # 输出：你好
