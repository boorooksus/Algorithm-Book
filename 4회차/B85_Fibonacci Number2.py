class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]

        for i in range(n - 1):
            dp[i % 2] = dp[0] + dp[1]

        return dp[n % 2]
    