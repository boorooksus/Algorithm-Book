class Solution:

    d = dict()
    d[0] = 0
    d[1] = 1

    def fib(self, n: int) -> int:
        if n in self.d:
            return self.d[n]

        self.d[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.d[n]

print(Solution().fib(3))


"""
leetcode: 509
다이나믹 프로그래밍
"""