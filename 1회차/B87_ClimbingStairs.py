from collections import defaultdict

class Solution:
    d = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        if self.d[n]:
            return self.d[n]
        self.d[n] = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        return self.d[n]

print(Solution().climbStairs(3))