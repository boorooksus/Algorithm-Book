from sys import stdin


INF = 10001


def main():
    n, k = map(int, stdin.readline().split())
    coins = set(int(stdin.readline()) for _ in range(n))

    dp = [0] + [INF] * k
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i - coin] + 1, dp[i])

    print(dp[k]) if dp[k] != INF else print(-1)


if __name__ == "__main__":
    main()
