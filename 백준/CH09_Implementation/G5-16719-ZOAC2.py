"""
재귀 이용한 방법
"""
from sys import stdin
from typing import List


def show(arr: List[str], start: int) -> None:
    if not arr:
        return

    _min = min(arr)
    idx = arr.index(_min)
    res[start + idx] = _min
    print(''.join(res))

    show(arr[idx + 1:], start + idx + 1)
    show(arr[:idx], start)


if __name__ == "__main__":
    x = list(stdin.readline().rstrip())

    res = [''] * len(x)
    show(x, 0)