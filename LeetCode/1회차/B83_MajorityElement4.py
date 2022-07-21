from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


print(Solution().majorityElement([3,2,3]))

"""
leetcode: 169
파이썬 다운 풀이
"""