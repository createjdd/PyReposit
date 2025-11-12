#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
类和实例
演示如何定义类、创建实例、访问属性和方法
"""

# ==================== 1. 定义类和创建实例 ====================
class Student:
    """学生类"""
    
    def __init__(self, name, age):
        """构造函数，初始化实例属性"""
        self.name = name
        self.age = age
    
    def introduce(self):
        """实例方法"""
        return f"我是{self.name}，今年{self.age}岁"


# 创建实例
student1 = Student("张三", 20)
student2 = Student("李四", 22)

print("=== 创建实例 ===")
print(student1.introduce())
print(student2.introduce())


# ==================== 2. 访问实例属性 ====================
print("\n=== 访问实例属性 ===")
print(f"学生1的姓名: {student1.name}")
print(f"学生1的年龄: {student1.age}")

# 修改实例属性
student1.age = 21
print(f"修改后学生1的年龄: {student1.age}")
print(f"修改后学生1-2的年龄: {student2.age}")

# ==================== 3. 类的方法 ====================
class Circle:
    """圆形类"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """计算面积"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """计算周长"""
        return 2 * 3.14159 * self.radius


print("\n=== 类的方法 ===")
circle = Circle(5)
print(f"圆的半径: {circle.radius}")
print(f"圆的面积: {circle.area():.2f}")
print(f"圆的周长: {circle.perimeter():.2f}")


# ==================== 4. 动态添加属性 ====================
print("\n=== 动态添加属性 ===")
student1.gender = "男"
print(f"学生1的性别: {student1.gender}")

# 注意：student2 没有 gender 属性
# print(student2.gender)  # 会报错


# ==================== 5. 类属性和实例属性 ====================
class Dog:
    """狗类"""
    species = "犬科"  # 类属性，所有实例共享
    
    def __init__(self, name, breed):
        self.name = name      # 实例属性
        self.breed = breed    # 实例属性


print("\n=== 类属性和实例属性 ===")
dog1 = Dog("旺财", "金毛")
dog2 = Dog("小黑", "拉布拉多")

print(f"dog1 的物种: {dog1.species}")  # 访问类属性
print(f"dog1 的名字: {dog1.name}")     # 访问实例属性
print(f"dog2 的物种: {dog2.species}")
print(f"dog2 的名字: {dog2.name}")

# 通过类名访问类属性
print(f"Dog 类的物种: {Dog.species}")


# ==================== 6. 完整示例 ====================
class BankAccount:
    """银行账户类"""
    
    bank_name = "Python银行"  # 类属性
    
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number # 银行卡号
        self.owner = owner # 户主
        self.balance = balance # 余额
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            return f"存款成功，当前余额: {self.balance}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"取款成功，当前余额: {self.balance}"
        return "余额不足或金额无效"
    
    def get_balance(self):
        """查询余额"""
        return f"账户 {self.account_number} 的余额: {self.balance}"


print("\n=== 完整示例：银行账户 ===")
account = BankAccount("123456", "张三", 1000)
print(f"银行名称: {BankAccount.bank_name}")
print(account.get_balance())
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

