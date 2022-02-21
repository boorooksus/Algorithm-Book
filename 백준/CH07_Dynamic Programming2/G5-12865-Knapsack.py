from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    items = [list(map(int, stdin.readline().split())) for _ in range(n)]

    dp = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if items[i - 1][0] <= j:
                dp[i][j] = max(dp[i - 1][j - items[i - 1][0]] + items[i - 1][1],
                               dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][k])


if __name__ == "__main__":
    main()
