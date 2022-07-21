from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx = dict()
        for idx, num in enumerate(nums):
            val_idx[target - num] = idx
            
        for idx, num in enumerate(nums):
            if num in val_idx and val_idx[num] != idx:
                return [val_idx[num], idx]
