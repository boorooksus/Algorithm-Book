import sys
from sys import stdin


def get_cost(x:int, y:int) -> int:
    return (y - x) * (1 + abs(a[x] - a[y]))


n, k = map(int, stdin.readline().split())
a = list(map(int, stdin.readline().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for end in range(1, n):
    for start in range(end):
        cost = sys.maxsize
        for stop in range(start, end):
            temp = dp[stop][start] + get_cost(stop, end)
            cost = min(cost, temp)
        dp[end][start] = cost

x = 1
print('YES') if dp[-1][0] <= k \
    else print('NO')
