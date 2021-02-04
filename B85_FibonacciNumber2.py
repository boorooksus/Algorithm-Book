class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        x, y = 0, 1
        for i in range(2, n + 1):
            x, y = y, x + y
        return y

print(Solution().fib(3))


"""
leetcode: 509
두 변수만 이용한 풀이
"""