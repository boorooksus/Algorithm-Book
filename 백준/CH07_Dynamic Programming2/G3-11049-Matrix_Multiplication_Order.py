from sys import stdin


input = lambda: stdin.readline().rstrip()
INF = 2 ** 32


if __name__ == "__main__":
    N = int(input())
    matrix = list(list(map(int, input().split())) for _ in range(N))

    dp = list([INF] * N for _ in range(N))
    for i in range(N):
        dp[i][i] = 0

    for i in range(N - 1):
        dp[i][i + 1] = matrix[i][0] * matrix[i][1] * matrix[i + 1][1]

    for i in range(1, N):
        for j in range(N - i):
            for k in range(j, j + i):
                dp[j][j + i] = min(dp[j][j + i],
                                   dp[j][k] + dp[k + 1][j + i] +
                                   matrix[j][0] * matrix[k][1] * matrix[j+i][1])

    print(dp[0][N - 1])