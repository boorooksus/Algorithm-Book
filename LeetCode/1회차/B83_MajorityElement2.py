from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        cnt = defaultdict(int)

        for num in nums:
            if cnt[num] == 0:
                cnt[num] = nums.count(num)

            elif cnt[num] > len(nums) // 2:
                return num


print(Solution().majorityElement([3,2,3]))

"""
leetcode: 169
다이나믹 프로그래밍
"""