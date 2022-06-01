"""
시간초과
"""
from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N, K = map(int, input().split())
    num = list(input())

    a = max(num[:K + 1])
    idx = num.index(a)
    num = num[idx:]
    K -= idx

    i = 1
    while K and i < len(num):
        while K and i + 1 < len(num) and num[i] < num[i + 1]:
            del num[i]
            K -= 1
        i += 1

    if K:
        num = num[:-K]

    print(''.join(num))
