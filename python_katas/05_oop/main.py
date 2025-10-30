#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass

"""
主题: 面向对象
- 类/实例属性
- 实例方法/类方法/静态方法
- dataclass
"""

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = float(celsius)

    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, f: float) -> "Temperature":
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def is_valid(t: float) -> bool:
        return -273.15 <= t <= 1e6

    def __repr__(self) -> str:
        return f"Temperature(celsius={self.celsius:.2f})"


@dataclass
class Point:
    x: float
    y: float

    def dist2(self) -> float:
        return self.x * self.x + self.y * self.y


def run_self_check():
    t = Temperature(0)
    assert round(t.fahrenheit, 2) == 32.00
    t2 = Temperature.from_fahrenheit(212)
    assert round(t2.celsius, 2) == 100.00
    assert Temperature.is_valid(-100) and not Temperature.is_valid(-1000)

    p = Point(3, 4)
    assert p.dist2() == 25

    print("05_oop ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
