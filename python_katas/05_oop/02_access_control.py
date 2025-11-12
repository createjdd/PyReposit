#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
访问限制
演示 Python 中的私有属性和方法（使用下划线约定）
"""

# ==================== 1. 公开属性（无下划线） ====================
class PublicClass:
    """公开属性示例"""
    
    def __init__(self):
        self.public_attr = "这是公开属性"  # 可以从外部访问
    
    def public_method(self):
        """公开方法"""
        return "这是公开方法"


print("=== 公开属性和方法 ===")
obj1 = PublicClass()
print(obj1.public_attr)        # ✅ 可以访问
print(obj1.public_method())     # ✅ 可以调用


# ==================== 2. 受保护属性（单下划线） ====================
class ProtectedClass:
    """受保护属性示例（约定，非强制）"""
    
    def __init__(self):
        self._protected_attr = "这是受保护属性"  # 约定：不应该从外部访问
    
    def _protected_method(self):
        """受保护方法（约定）"""
        return "这是受保护方法"
    
    def get_protected(self):
        """通过公开方法访问受保护属性"""
        return self._protected_attr


print("\n=== 受保护属性和方法 ===")
obj2 = ProtectedClass()
# 技术上可以访问，但不推荐
print(obj2._protected_attr)     # ⚠️ 可以访问，但不推荐
print(obj2._protected_method()) # ⚠️ 可以调用，但不推荐
# 推荐方式
print(obj2.get_protected())      # ✅ 推荐：通过公开方法访问


# ==================== 3. 私有属性（双下划线） ====================
class PrivateClass:
    """私有属性示例（名称改写）"""
    
    def __init__(self):
        self.public_attr = "公开属性"
        self._protected_attr = "受保护属性"
        self.__private_attr = "私有属性"  # 会被改写为 _PrivateClass__private_attr
    
    def __private_method(self):
        """私有方法"""
        return "这是私有方法"
    
    def get_private(self):
        """通过公开方法访问私有属性"""
        return self.__private_attr
    
    def call_private_method(self):
        """通过公开方法调用私有方法"""
        return self.__private_method()


print("\n=== 私有属性和方法 ===")
obj3 = PrivateClass()
print(obj3.public_attr)                    # ✅ 可以访问
print(obj3._protected_attr)                # ⚠️ 可以访问（不推荐）
# print(obj3.__private_attr)               # ❌ 直接访问会报错
print(obj3.get_private())                  # ✅ 通过方法访问
print(obj3.call_private_method())          # ✅ 通过方法调用

# 注意：Python 的"私有"是通过名称改写实现的
# 实际上可以通过改写后的名称访问（但不推荐）
print(obj3._PrivateClass__private_attr)     # ⚠️ 可以访问，但不推荐


# ==================== 4. 实际应用示例 ====================
class BankAccount:
    """银行账户类 - 使用访问限制保护数据"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number  # 公开属性
        self.owner = owner                    # 公开属性
        self.__balance = initial_balance      # 私有属性：余额不能直接修改
        self.__transaction_history = []       # 私有属性：交易历史
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"存款: +{amount}")
            return f"存款成功，当前余额: {self.__balance}"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"取款: -{amount}")
            return f"取款成功，当前余额: {self.__balance}"
        return "余额不足或金额无效"
    
    def get_balance(self):
        """查询余额（只读）"""
        return self.__balance
    
    def get_history(self):
        """获取交易历史（只读）"""
        return self.__history.copy()  # 返回副本，防止外部修改
    
    @property
    def balance(self):
        """使用 @property 装饰器，使余额可以像属性一样访问"""
        return self.__balance
    
    @property
    def history(self):
        """交易历史（只读）"""
        return tuple(self.__transaction_history)  # 返回元组，不可修改


print("\n=== 实际应用：银行账户 ===")
account = BankAccount("123456", "张三", 1000)
print(f"账户号: {account.account_number}")  # ✅ 公开属性
print(f"户主: {account.owner}")              # ✅ 公开属性

# 只能通过方法修改余额
print(account.deposit(500))
print(account.withdraw(200))

# 使用 @property 访问余额
print(f"当前余额: {account.balance}")       # ✅ 像属性一样访问
print(f"交易历史: {account.history}")

# 尝试直接访问私有属性（会报错）
# print(account.__balance)                  # ❌ AttributeError


# ==================== 5. 使用 @property 和 @setter ====================
class Temperature:
    """温度类 - 演示 @property 和 @setter"""
    
    def __init__(self, celsius=0):
        self.__celsius = celsius
    
    @property
    def celsius(self):
        """获取摄氏温度"""
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        """设置摄氏温度（带验证）"""
        if value < -273.15:
            raise ValueError("温度不能低于绝对零度")
        self.__celsius = value
    
    @property
    def fahrenheit(self):
        """获取华氏温度（只读）"""
        return self.__celsius * 9/5 + 32


print("\n=== @property 和 @setter ===")
temp = Temperature(25)
print(f"摄氏温度: {temp.celsius}°C")
print(f"华氏温度: {temp.fahrenheit}°F")

# 使用 setter
temp.celsius = 30
print(f"修改后摄氏温度: {temp.celsius}°C")
print(f"修改后华氏温度: {temp.fahrenheit}°F")

# 尝试设置无效值
try:
    temp.celsius = -300
except ValueError as e:
    print(f"错误: {e}")

