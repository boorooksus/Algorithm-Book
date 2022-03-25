from sys import stdin
from collections import defaultdict
from math import gcd


dp = defaultdict(int)


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    seq = list(map(int, input().split()))
    x = int(input())

    total, cnt = 0, 0
    for num in seq:
        if not dp[num]:
            dp[num] = gcd(x, num)
        if dp[num] == 1:
            total += num
            cnt += 1

    print(total / cnt)


if __name__ == "__main__":
    main()

