from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res

sol = Solution()
print(sol.singleNumber([4, 1, 2, 1, 2]))


"""
leetcode: 136
XOR 이용한 방법
"""