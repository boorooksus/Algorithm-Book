from sys import stdin


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))
    J = list(map(int, input().split()))

    dp = list([0] * 101 for _ in range(N + 1))
    for i in range(1, N + 1):
        for j in range(1, 101):
            if j - L[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - L[i - 1]] + J[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[N][99])