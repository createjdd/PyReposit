#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slots
演示slots的使用
@property装饰器：将一个方法转换为属性
"""

class Person:
    # 限制实例属性
    __slots__ = ('name', '_age')
    # 初始化实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # str作用：打印实例时，返回字符串
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

p = Person('John', 30)
print(p)

# 尝试添加一个slots中没有的属性
#p.gender = 'male'
print(p)

print(p.age)
p.age = 31
print(p.age)


"""
定制类
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

s = Student('John', 30)
print(s)

# __iter__：实现迭代器协议
class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.students):
            result = self.students[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

s = StudentIterator([Student('John', 30), Student('Jane', 25), Student('Jim', 35)])
for student in s:
    print(student)

# 使用场景：当需要限制实例属性时，可以使用slots
# 当需要实现迭代器协议时，可以使用__iter__和__next__
# 当需要实现序列协议时，可以使用__len__和__getitem__
# 当需要实现映射协议时，可以使用__getitem__和__setitem__
# 当需要实现上下文管理协议时，可以使用__enter__和__exit__
# 当需要实现描述符协议时，可以使用__get__和__set__
# 当需要实现属性协议时，可以使用__getattr__和__setattr__
# 当需要实现方法协议时，可以使用__call__
# 当需要实现运算符重载时，可以使用__add__和__sub__
# 当需要实现比较运算符重载时，可以使用__eq__和__ne__
# 当需要实现算术运算符重载时，可以使用__add__和__sub__

# 举例：实现一个简单的学生管理系统
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)

    def get_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def __iter__(self):
        return StudentIterator(self.students)

    def __len__(self):
        return len(self.students)
        
sm = StudentManager()
sm.add_student(Student('John', 30))
sm.add_student(Student('Jane', 25))
sm.add_student(Student('Jim', 35))
print('--------------------------------')
for student in sm:
    print(student)

print(len(sm))
print(sm.get_student('John'))
print(sm.get_student('Jane'))
print(sm.get_student('Jim'))


from enum import Enum
print('----------------=====----------------')
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print('============================')
class Weekday(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

for name, member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

day1 = Weekday.Monday
print('----------------=====----------------')
print(day1)
print(day1.value)
print(day1 == Weekday.Monday)
print(day1 == Weekday.Tuesday)
print(day1 == Weekday.Wednesday)
print(day1 == Weekday.Thursday)
print(day1 == Weekday.Friday)

print('++++++++++++++++++++++++++++++++++++')
# 模拟从接口接收到的数据
json_data = '{"status": "DONE"}'

# 解析字符串
import json
data = json.loads(json_data)
from enum import Enum

class Status(Enum):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

# 转成枚举
status_enum = Status[data['status']]
print(status_enum)        # Status.DONE
print(status_enum.value)  # 3

# 如果要再发回接口
resp = json.dumps({'status': status_enum.name})
print(resp)  # {"status": "DONE"}
