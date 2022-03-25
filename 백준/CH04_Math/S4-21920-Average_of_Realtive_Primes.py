"""
유클리드 호제법
"""
from sys import stdin
from collections import defaultdict


dp = defaultdict(int)


def get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    if a < b:
        a, b = b, a
    return get_gcd(b, a % b)


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())

    total, cnt = 0, 0
    for num in seq:
        if not dp[num]:
            dp[num] = get_gcd(x, num)
        if dp[num] == 1:
            total += num
            cnt += 1

    print(total / cnt)


if __name__ == "__main__":
    main()

