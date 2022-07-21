from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            if target - num in indices.keys():
                return [i, indices[target - num]]

            indices[num] = i