from typing import List
from bisect import bisect_left


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect_left(nums, target)
        return idx if 0 <= idx < len(nums) and nums[idx] == target else -1
