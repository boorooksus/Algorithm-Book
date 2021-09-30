import sys
from sys import stdin


def get_cost(x:int, y:int) -> int:
    return (y - x) * (1 + abs(a[x] - a[y]))


n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

dp = [False for _ in range(n)]
dp[0] = True

for i in range(1, n):
    cost = sys.maxsize
    for j in range(0, i):
        if dp[j]:
            cost = min(cost, get_cost(j, i))

    if cost <= k:
        dp[i] = True

print('YES') if dp[-1] else print('NO')
