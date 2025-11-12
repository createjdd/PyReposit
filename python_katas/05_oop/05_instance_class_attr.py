#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实例属性和类属性
演示实例属性与类属性的区别和使用场景
"""

# ==================== 1. 类属性 vs 实例属性 ====================
class Student:
    """学生类"""
    school = "Python大学"  # 类属性：所有实例共享
    
    def __init__(self, name, age):
        self.name = name  # 实例属性：每个实例独有
        self.age = age    # 实例属性：每个实例独有


print("=== 类属性 vs 实例属性 ===")
student1 = Student("张三", 20)
student2 = Student("李四", 22)

# 访问类属性
print(f"student1 的学校: {student1.school}")  # 通过实例访问
print(f"student2 的学校: {student2.school}")  # 通过实例访问
print(f"Student 的学校: {Student.school}")    # 通过类访问

# 访问实例属性
print(f"student1 的姓名: {student1.name}")
print(f"student2 的姓名: {student2.name}")


# ==================== 2. 修改类属性 ====================
print("\n=== 修改类属性 ===")
# 通过类修改（影响所有实例）
Student.school = "新Python大学"
print(f"修改后 student1 的学校: {student1.school}")
print(f"修改后 student2 的学校: {student2.school}")

# 通过实例修改（只影响该实例，实际上是创建了实例属性）
student1.school = "个人学校"
print(f"student1 的学校: {student1.school}")  # 实例属性
print(f"student2 的学校: {student2.school}")  # 类属性
print(f"Student 的学校: {Student.school}")    # 类属性


# ==================== 3. 类属性的常见用途 ====================
class Counter:
    """计数器类 - 使用类属性统计实例数量"""
    count = 0  # 类属性：统计实例数量
    
    def __init__(self, name):
        self.name = name
        Counter.count += 1  # 每次创建实例时增加计数
        self.id = Counter.count  # 实例属性：实例ID


print("\n=== 类属性的常见用途：统计实例数量 ===")
c1 = Counter("计数器1")
c2 = Counter("计数器2")
c3 = Counter("计数器3")

print(f"创建的实例数量: {Counter.count}")
print(f"c1 的 ID: {c1.id}")
print(f"c2 的 ID: {c2.id}")
print(f"c3 的 ID: {c3.id}")


# ==================== 4. 类属性存储配置信息 ====================
class Database:
    """数据库类 - 使用类属性存储配置"""
    host = "localhost"
    port = 5432
    database = "mydb"
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    @classmethod
    def configure(cls, host, port, database):
        """类方法：配置数据库连接"""
        cls.host = host
        cls.port = port
        cls.database = database
    
    def connect(self):
        """连接数据库"""
        return f"连接到 {self.host}:{self.port}/{self.database} (用户: {self.user})"


print("\n=== 类属性存储配置信息 ===")
db1 = Database("user1", "pass1")
db2 = Database("user2", "pass2")

print(db1.connect())
print(db2.connect())

# 修改配置（影响所有实例）
Database.configure("192.168.1.100", 3306, "production")
print("\n修改配置后:")
print(db1.connect())
print(db2.connect())


# ==================== 5. 类方法和静态方法 ====================
class MathUtils:
    """数学工具类"""
    pi = 3.14159  # 类属性
    
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_string(cls, value_str):
        """类方法：从字符串创建实例"""
        return cls(float(value_str))
    
    @classmethod
    def get_pi(cls):
        """类方法：获取圆周率"""
        return cls.pi
    
    @staticmethod
    def add(a, b):
        """静态方法：不需要访问类或实例"""
        return a + b
    
    def multiply_by_pi(self):
        """实例方法：使用类属性"""
        return self.value * MathUtils.pi


print("\n=== 类方法和静态方法 ===")
# 使用类方法创建实例
math1 = MathUtils.from_string("10")
print(f"从字符串创建: {math1.value}")

# 调用类方法
print(f"圆周率: {MathUtils.get_pi()}")

# 调用静态方法
print(f"1 + 2 = {MathUtils.add(1, 2)}")

# 实例方法使用类属性
math2 = MathUtils(5)
print(f"5 * π = {math2.multiply_by_pi():.2f}")


# ==================== 6. 属性查找顺序 ====================
class Example:
    """示例类 - 演示属性查找顺序"""
    class_attr = "类属性"
    
    def __init__(self):
        self.instance_attr = "实例属性"
        self.class_attr = "实例属性（覆盖类属性）"  # 同名实例属性


print("\n=== 属性查找顺序 ===")
obj = Example()
print(f"obj.class_attr: {obj.class_attr}")  # 优先查找实例属性
print(f"obj.instance_attr: {obj.instance_attr}")
print(f"Example.class_attr: {Example.class_attr}")  # 类属性仍然存在

# 删除实例属性后，会使用类属性
del obj.class_attr
print(f"删除实例属性后 obj.class_attr: {obj.class_attr}")


# ==================== 7. 完整示例：银行账户 ====================
class BankAccount:
    """银行账户类"""
    bank_name = "Python银行"      # 类属性：银行名称
    interest_rate = 0.03          # 类属性：利率
    total_accounts = 0             # 类属性：账户总数
    
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number  # 实例属性
        self.owner = owner                    # 实例属性
        self.balance = balance                # 实例属性
        BankAccount.total_accounts += 1        # 增加账户总数
    
    @classmethod
    def set_interest_rate(cls, rate):
        """类方法：设置利率"""
        cls.interest_rate = rate
    
    @classmethod
    def get_total_accounts(cls):
        """类方法：获取账户总数"""
        return cls.total_accounts
    
    def calculate_interest(self):
        """计算利息"""
        return self.balance * BankAccount.interest_rate
    
    def deposit(self, amount):
        """存款"""
        self.balance += amount
        return self.balance
    
    def get_info(self):
        """获取账户信息"""
        return f"{BankAccount.bank_name} - 账户: {self.account_number}, 户主: {self.owner}, 余额: {self.balance}"


print("\n=== 完整示例：银行账户 ===")
account1 = BankAccount("001", "张三", 1000)
account2 = BankAccount("002", "李四", 2000)

print(account1.get_info())
print(account2.get_info())
print(f"总账户数: {BankAccount.get_total_accounts()}")
print(f"当前利率: {BankAccount.interest_rate}")

# 计算利息
print(f"\n张三的利息: {account1.calculate_interest()}")
print(f"李四的利息: {account2.calculate_interest()}")

# 修改利率（影响所有账户）
BankAccount.set_interest_rate(0.05)
print(f"\n新利率: {BankAccount.interest_rate}")
print(f"张三的新利息: {account1.calculate_interest()}")
print(f"李四的新利息: {account2.calculate_interest()}")

