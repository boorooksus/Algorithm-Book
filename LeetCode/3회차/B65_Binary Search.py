from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if 0 <= idx < len(nums) and nums[idx] == target else -1
