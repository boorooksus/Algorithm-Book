from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    dp = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] += \
                dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

    for _ in range(m):
        ay, ax, by, bx = map(int, input().split())
        res = dp[by][bx] \
            - dp[ay - 1][bx] - dp[by][ax - 1] + dp[ay - 1][ax - 1]
        print(res)


if __name__ == "__main__":
    main()
