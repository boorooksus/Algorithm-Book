from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())
    coins = [int(stdin.readline()) for _ in range(n)]

    dp = [1] + [0] * k

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]

    print(dp[k])


if __name__ == "__main__":
    main()
