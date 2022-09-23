from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 5_000_000_000


def get_cost(i: int, j: int) -> int:
    return (j - i) * (1 + abs(A[i] - A[j]))


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))

    dp = [0] + [INF] * (N - 1)

    for i in range(1, N):
        for j in range(i):
            dp[i] = min(dp[i], max(get_cost(j, i), dp[j]))

    print(dp[-1])
