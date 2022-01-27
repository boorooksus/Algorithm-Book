from sys import stdin, setrecursionlimit, maxsize
setrecursionlimit(10 ** 9)


n = int(stdin.readline())
a = [0] + list(map(int, stdin.readline().split()))
dp = [-1 for _ in range(n + 1)]  # 각 위치에서 징검다리를 건너는 최소 비용


def cost(i: int, j: int) -> int:
    return (j - i) * (1 + abs(a[i] - a[j]))


# x: 출발 위치
# return: 출발 위치에서 징검다리를 건너는 최소 비용
def jump(x: int) -> int:
    # 맨 마지막 징검다리에서 출발한 경우 비용은 0
    if x == n:
        return 0

    if dp[x] > -1:
        return dp[x]

    dp[x] = maxsize
    for stop in range(x + 1, n + 1):
        dp[x] = min(dp[x], max(cost(x, stop), jump(stop)))

    return dp[x]


print(jump(1))

