from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 1000001

if __name__ == "__main__":
    N = int(input())
    e = list(list(map(int, input().split())) for _ in range(N - 1)) + [[0, 0]]
    k = int(input())

    if N == 1:
        print(e[0][0])
        exit(0)

    dp = [INF] * N
    dp[0], dp[1] = 0, e[0][0]
    for i in range(2, N):
        dp[i] = min(dp[i - 2] + e[i - 2][1], dp[i - 1] + e[i - 1][0])

    dp2 = [INF] * N
    dp2[-1], dp2[-2] = 0, e[-2][0]
    for i in range(-3, -N - 1, -1):
        dp2[i] = min(dp2[i + 1] + e[i][0], dp2[i + 2] + e[i][1])

    res = dp[-1]
    for i in range(3, N):
        res = min(res, dp[i - 3] + k + dp2[i])
    print(res)

"""
5
5000 5000
5000 5000
5000 5000
5000 5000
1
"""