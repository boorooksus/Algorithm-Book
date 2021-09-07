from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) == 1:
                return i
        return 0

"""
leetcode: 136
"""