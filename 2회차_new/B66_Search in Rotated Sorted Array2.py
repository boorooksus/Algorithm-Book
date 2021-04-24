from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))

        idx = bisect.bisect_left(nums, target, pivot)
        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            idx = bisect.bisect_left(nums, target, 0, pivot - 1)
            if idx < pivot and nums[idx] == target:
                return idx

            return -1


print(Solution().search([4,5,6,7,0,1,2], 0))