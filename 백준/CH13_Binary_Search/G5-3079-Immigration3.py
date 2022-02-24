"""
이진 탐색
"""
from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    t = [int(stdin.readline()) for _ in range(n)]

    left, right = 0, max(t) * m
    res = 0
    while left <= right:

        mid = left + (right - left) // 2
        passed = 0

        for time in t:
            passed += mid // time

        if passed < m:
            left = mid + 1
        else:
            res = mid
            right = mid - 1

    print(res)


if __name__ == "__main__":
    main()
