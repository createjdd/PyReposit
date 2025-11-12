#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
继承和多态
演示类的继承、方法重写和多态性
"""

# ==================== 1. 基本继承 ====================
class Animal:
    """动物基类"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """说话方法（在子类中会被重写）"""
        return f"{self.name} 发出了声音"
    
    def move(self):
        """移动方法"""
        return f"{self.name} 在移动"


class Dog(Animal):
    """狗类 - 继承自 Animal"""
    
    def speak(self):
        """重写父类方法"""
        return f"{self.name} 汪汪叫"


class Cat(Animal):
    """猫类 - 继承自 Animal"""
    
    def speak(self):
        """重写父类方法"""
        return f"{self.name} 喵喵叫"


print("=== 基本继承 ===")
dog = Dog("旺财")
cat = Cat("小花")

print(dog.speak())      # 调用重写后的方法
print(cat.speak())      # 调用重写后的方法
print(dog.move())       # 调用继承的方法
print(cat.move())       # 调用继承的方法


# ==================== 2. 调用父类方法 ====================
class Bird(Animal):
    """鸟类"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name)  # 调用父类的 __init__
        self.can_fly = can_fly
    
    def speak(self):
        # 先调用父类方法，再添加自己的逻辑
        base_sound = super().speak()
        return f"{base_sound}，{self.name} 啾啾叫"
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} 在飞翔"
        return f"{self.name} 不会飞"


print("\n=== 调用父类方法 ===")
bird1 = Bird("鹦鹉", can_fly=True)
bird2 = Bird("企鹅", can_fly=False)

print(bird1.speak())
print(bird1.fly())
print(bird2.speak())
print(bird2.fly())


# ==================== 3. 多态性 ====================
def animal_speak(animal):
    """多态函数 - 可以接受任何 Animal 子类"""
    return animal.speak()


print("\n=== 多态性 ===")
animals = [Dog("旺财"), Cat("小花"), Bird("鹦鹉")]
for animal in animals:
    print(animal_speak(animal))  # 同一个函数，不同的行为


# ==================== 4. 多重继承 ====================
class Flyable:
    """可飞行接口"""
    
    def fly(self):
        return "正在飞行"


class Swimmable:
    """可游泳接口"""
    
    def swim(self):
        return "正在游泳"


class Duck(Animal, Flyable, Swimmable):
    """鸭子类 - 多重继承"""
    
    def speak(self):
        return f"{self.name} 嘎嘎叫"


print("\n=== 多重继承 ===")
duck = Duck("唐老鸭")
print(duck.speak())
print(duck.fly())
print(duck.swim())


# ==================== 5. 方法解析顺序（MRO） ====================
print("\n=== 方法解析顺序（MRO） ===")
print(f"Duck 的 MRO: {Duck.__mro__}")


# ==================== 6. 完整示例：图形类 ====================
class Shape:
    """图形基类"""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """计算面积（子类必须实现）"""
        raise NotImplementedError("子类必须实现 area 方法")
    
    def perimeter(self):
        """计算周长（子类必须实现）"""
        raise NotImplementedError("子类必须实现 perimeter 方法")
    
    def info(self):
        """显示信息"""
        return f"{self.name}: 面积={self.area():.2f}, 周长={self.perimeter():.2f}"


class Rectangle(Shape):
    """矩形类"""
    
    def __init__(self, width, height):
        super().__init__("矩形")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """圆形类"""
    
    def __init__(self, radius):
        super().__init__("圆形")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Square(Rectangle):
    """正方形类 - 继承自 Rectangle"""
    
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "正方形"


print("\n=== 完整示例：图形类 ===")
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Square(5)
]

for shape in shapes:
    print(shape.info())


# ==================== 7. isinstance 和 issubclass ====================
print("\n=== 类型检查 ===")
rect = Rectangle(5, 3)
print(f"rect 是 Rectangle 的实例: {isinstance(rect, Rectangle)}")
print(f"rect 是 Shape 的实例: {isinstance(rect, Shape)}")
print(f"Rectangle 是 Shape 的子类: {issubclass(Rectangle, Shape)}")
print(f"Square 是 Rectangle 的子类: {issubclass(Square, Rectangle)}")

