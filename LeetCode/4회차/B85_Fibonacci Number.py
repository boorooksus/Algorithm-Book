class Solution:
    dp = [0 for _ in range(31)]

    def fib(self, n: int) -> int:
        if n < 2:
            return n

        if self.dp[n] > 0:
            return self.dp[n]

        self.dp[n] = self.fib(n - 2) + self.fib(n - 1)
        return self.dp[n]