from sys import stdin, maxsize


def main():
    def input():
        return stdin.readline().rstrip()

    c, n = map(int, input().split())
    promotions = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] + [1000000] * (c + 100)
    res = maxsize
    for i in range(c + 101):
        for cost, client in promotions:
            if i >= client:
                dp[i] = min(dp[i - client] + cost, dp[i])
            if i >= c:
                res = min(dp[i], res)
    print(res)


if __name__ == "__main__":
    main()
