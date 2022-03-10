"""
참고: https://suri78.tistory.com/11
"""
from sys import stdin


def main():
    a, b = (stdin.readline().rstrip() for _ in range(2))

    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[-1][-1])


if __name__ == "__main__":
    main()
