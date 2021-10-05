from sys import stdin


n, m = map(int, stdin.readline().split())
dp = [[0 for _ in range(m + 1)]]
for i in range(1, n + 1):
    dp.append([0] + list(map(int, stdin.readline().split())))
    for j in range(1, m + 1):
        dp[i][j] += dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

k = int(stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    print(dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1])

