from sys import stdin
from typing import List
from math import factorial


def main():
    def input():
        return stdin.readline().rstrip()

    t = int(input())
    for _ in range(t):
        n = int(input())
        coins = list(map(int, input().split()))
        m = int(input())
        print(get_cnt(n, coins, m))


def get_cnt(n: int, coins: List[int], m: int) -> int:
    dp = [0] * (m + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, m + 1):
            dp[i] += dp[i - coin]

    return dp[m]


if __name__ == "__main__":
    main()
