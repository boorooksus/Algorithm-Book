from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] > nums[i]:
                pivot = i
                break
        left = bisect.bisect_left(nums, target, 0, pivot - 1)
        right = bisect.bisect_left(nums, target, pivot)

        if 0 <= left < pivot and nums[left] == target:
            return left
        elif pivot <= right < len(nums) and nums[right] == target:
            return right
        else:
            return -1


