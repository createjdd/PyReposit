#!/usr/bin/env python3
from __future__ import annotations
from collections import Counter, deque

"""
主题: 常用容器
- list/tuple/set/dict
- 推导式
- Counter, deque
"""

def top_k_words(text: str, k: int = 3) -> list[tuple[str, int]]:
    words = [w.strip('.,!?').lower() for w in text.split() if w.strip()]
    cnt = Counter(words)
    return cnt.most_common(k)


def unique_sorted(xs: list[int]) -> list[int]:
    # TODO: set 去重 + 排序
    return sorted(set(xs))


def rotate_queue(xs: list[int], steps: int) -> list[int]:
    dq = deque(xs)
    dq.rotate(steps)
    return list(dq)


def run_self_check():
    text = "a a A b, c c c"
    assert top_k_words(text, 2) == [("c", 3), ("a", 2)]
    assert unique_sorted([3, 1, 2, 3, 2]) == [1, 2, 3]
    assert rotate_queue([1, 2, 3, 4], 1) == [4, 1, 2, 3]

    print("04_collections ✅ 自检通过。")


if __name__ == "__main__":
    run_self_check()
