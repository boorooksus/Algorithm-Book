from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return sorted(nums)[len(nums) // 2]
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        left = self.majorityElement(nums[:len(nums) // 2])
        right = self.majorityElement(nums[len(nums) // 2:])

        return left if nums.count(left) > len(nums) // 2 else right
