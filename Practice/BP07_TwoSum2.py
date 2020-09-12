from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = dict()
        for idx, num in enumerate(nums):
            if num in val_idx:
                return [val_idx[num], idx]
            val_idx[target - num] = idx
