#collections 模块是 Python 标准库中的一个模块，提供了很多有用的数据结构。

from collections import Counter, OrderedDict, defaultdict, namedtuple, deque

c = Counter('abcdeabcdabcaba')
print(c) # 统计字符串中每个字符出现的次数
print(c.most_common(3)) # 统计字符串中出现次数最多的3个字符
print(c.elements()) # 统计字符串中每个字符出现的次数

# OrderedDict 有序字典
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)

# defaultdict 默认字典
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
print(d)

# namedtuple 命名元组
d = namedtuple('d', ['a', 'b', 'c'])
d = d(1, 2, 3)
print(d)

# deque 双端队列
d = deque()
d.append(1)
d.appendleft(2)
print(d)