from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1, -1, -1):
            num = nums.pop()
            if target - num in nums:
                return [nums.index(target - num), i]
