from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        left, mid, right = 0, 1, 2
        window = nums[0] + nums[1] + nums[2]

        while left
