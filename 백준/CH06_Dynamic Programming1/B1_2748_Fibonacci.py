from sys import stdin

dp = [0, 1]


def fibonacci(n: int) -> int:
    if len(dp) > n:
        return dp[n]
    dp.append(fibonacci(n - 2) + fibonacci(n - 1))
    return dp[n]


n = int(stdin.readline())
print(fibonacci(n))
