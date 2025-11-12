#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取对象信息
演示如何获取对象的类型、属性、方法等信息
"""

# ==================== 1. type() - 获取对象类型 ====================
print("=== type() - 获取对象类型 ===")

num = 123
text = "hello"
lst = [1, 2, 3]

print(f"num 的类型: {type(num)}")
print(f"text 的类型: {type(text)}")
print(f"lst 的类型: {type(lst)}")

# 比较类型
print(f"num 是 int 类型: {type(num) == int}")
print(f"text 是 str 类型: {type(text) == str}")


# ==================== 2. isinstance() - 类型检查 ====================
class Animal:
    """动物基类"""
    pass


class Dog(Animal):
    """狗类"""
    pass


print("\n=== isinstance() - 类型检查 ===")
dog = Dog()
print(f"dog 是 Dog 的实例: {isinstance(dog, Dog)}")
print(f"dog 是 Animal 的实例: {isinstance(dog, Animal)}")
print(f"dog 是 object 的实例: {isinstance(dog, object)}")

# isinstance 可以检查多个类型
print(f"dog 是 Dog 或 Animal: {isinstance(dog, (Dog, Animal))}")


# ==================== 3. dir() - 获取对象的所有属性和方法 ====================
class Person:
    """人类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是{self.name}，{self.age}岁"


print("\n=== dir() - 获取对象的所有属性和方法 ===")
person = Person("张三", 25)
print("person 的所有属性和方法:")
for attr in dir(person):
    if not attr.startswith('__'):  # 过滤掉特殊方法
        print(f"  - {attr}")


# ==================== 4. hasattr() - 检查是否有属性 ====================
print("\n=== hasattr() - 检查是否有属性 ===")
print(f"person 有 name 属性: {hasattr(person, 'name')}")
print(f"person 有 age 属性: {hasattr(person, 'age')}")
print(f"person 有 introduce 方法: {hasattr(person, 'introduce')}")
print(f"person 有 gender 属性: {hasattr(person, 'gender')}")


# ==================== 5. getattr() - 获取属性值 ====================
print("\n=== getattr() - 获取属性值 ===")
print(f"person.name: {getattr(person, 'name')}")
print(f"person.age: {getattr(person, 'age')}")

# 如果属性不存在，可以设置默认值
print(f"person.gender (默认值): {getattr(person, 'gender', '未知')}")

# 获取方法并调用
introduce_method = getattr(person, 'introduce')
print(f"调用方法: {introduce_method()}")


# ==================== 6. setattr() - 设置属性 ====================
print("\n=== setattr() - 设置属性 ===")
setattr(person, 'gender', '男')
setattr(person, 'city', '北京')
print(f"person.gender: {person.gender}")
print(f"person.city: {person.city}")


# ==================== 7. __dict__ - 获取对象的属性字典 ====================
print("\n=== __dict__ - 获取对象的属性字典 ===")
print(f"person.__dict__: {person.__dict__}")


# ==================== 8. __class__ - 获取对象的类 ====================
print("\n=== __class__ - 获取对象的类 ===")
print(f"person 的类: {person.__class__}")
print(f"person 的类名: {person.__class__.__name__}")


# ==================== 9. __module__ - 获取模块名 ====================
print("\n=== __module__ - 获取模块名 ===")
print(f"Person 类的模块: {Person.__module__}")


# ==================== 10. __doc__ - 获取文档字符串 ====================
print("\n=== __doc__ - 获取文档字符串 ===")
print(f"Person 类的文档: {Person.__doc__}")


# ==================== 11. __name__ - 获取类名 ====================
print("\n=== __name__ - 获取类名 ===")
print(f"Person 类的名称: {Person.__name__}")


# ==================== 12. inspect 模块 - 更详细的检查 ====================
import inspect

print("\n=== inspect 模块 - 更详细的检查 ===")

# 获取类的所有方法
methods = inspect.getmembers(Person, predicate=inspect.ismethod)
print("Person 类的方法:")
for name, method in methods:
    print(f"  - {name}")

# 获取函数的参数信息
sig = inspect.signature(Person.__init__)
print(f"\nPerson.__init__ 的参数: {sig}")

# 获取源代码
print(f"\nPerson 类的源代码:")
print(inspect.getsource(Person))


# ==================== 13. 完整示例：对象信息查看器 ====================
def object_info(obj):
    """获取对象的详细信息"""
    info = {
        'type': type(obj).__name__,
        'class': obj.__class__.__name__,
        'module': obj.__class__.__module__,
        'attributes': {},
        'methods': []
    }
    
    # 获取实例属性
    if hasattr(obj, '__dict__'):
        info['attributes'] = obj.__dict__
    
    # 获取方法
    for name in dir(obj):
        if not name.startswith('__'):
            attr = getattr(obj, name)
            if callable(attr):
                info['methods'].append(name)
            elif name not in info['attributes']:
                info['attributes'][name] = attr
    
    return info


print("\n=== 完整示例：对象信息查看器 ===")
person_info = object_info(person)
print("person 的详细信息:")
for key, value in person_info.items():
    print(f"  {key}: {value}")

