class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_val = 0x7FFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a > max_val:
            a = ~(mask ^ a)

        return a


sol = Solution()
print(sol.getSum(-12, -8))

"""
leetcode: 371
"""