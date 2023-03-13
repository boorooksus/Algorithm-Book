from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(k - coin + 1):
            dp[i + coin] += dp[i]

    print(dp[-1])
