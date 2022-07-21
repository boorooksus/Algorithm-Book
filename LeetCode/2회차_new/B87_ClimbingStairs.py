from collections import OrderedDict

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp = OrderedDict()
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp.pop(n)


print(Solution().climbStairs(10))