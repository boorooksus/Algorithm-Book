class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 0b1
        res = 0
        while n:
            if n & mask == 1:
                res += 1
            n >>= 1
        return res

sol = Solution()
print(sol.hammingWeight(11))

"""
leetcode: 191
비트연산자를 이용한 풀이
"""