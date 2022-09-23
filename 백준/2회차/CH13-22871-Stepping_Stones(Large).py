from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = lambda: stdin.readline().rstrip()
INF = 5_000_000_000


def get_cost(i: int, j: int) -> int:
    return (j - i) * (1 + abs(A[i] - A[j]))


def jump(start: int) -> int:
    if start == N:
        return 0

    if dp[start] < INF:
        return dp[start]

    for stop in range(start + 1, N + 1):
        a = get_cost(start, stop)
        dp[start] = min(dp[start], max(get_cost(start, stop), jump(stop)))

    return dp[start]


if __name__ == "__main__":
    N = int(input())
    A = [0] + list(map(int, input().split()))

    dp = [INF] * (N + 1)
    print(jump(1))
