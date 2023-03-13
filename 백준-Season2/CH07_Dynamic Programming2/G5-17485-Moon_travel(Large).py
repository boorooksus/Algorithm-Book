from sys import stdin
input = lambda: stdin.readline().rstrip()


INF = 100001


if __name__ == "__main__":
    N, M = map(int, input().split())
    costs = [list(map(int, input().split())) for _ in range(N)]

    dp = [[[INF] * 3 for _ in range(M)] for _ in range(N)]

    for i in range(M):
        dp[0][i] = [costs[0][i]] * 3

    for i in range(1, N):
        for j in range(M):
            for k in range(-1, 2):
                if 0 <= j + k < M:
                    dp[i][j][k] = costs[i][j] + \
                                  min(dp[i - 1][j + k][(k + 1) % 3], dp[i - 1][j + k][(k + 2) % 3])

    ans = INF
    for li in dp[-1]:
        ans = min(ans, min(li))
    print(ans)