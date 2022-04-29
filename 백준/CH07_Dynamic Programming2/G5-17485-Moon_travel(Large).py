from sys import stdin


INF = 100001


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N, M = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(N)]

    dp = list(list([INF] * 3 for _ in range(M)) for _ in range(N))

    for i in range(M):
        for j in range(3):
            dp[0][i][j] = costs[0][i]

    for i in range(1, N):
        for j in range(M):
            if j > 0:
                dp[i][j][0] = min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2]) + costs[i][j]
            dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + costs[i][j]
            if j < M - 1:
                dp[i][j][2] = min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1]) + costs[i][j]

    ans = INF
    for i in range(M):
        ans = min(min(dp[-1][i]), ans)
    print(ans)
