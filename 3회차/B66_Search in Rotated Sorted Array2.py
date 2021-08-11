from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot, start, end = 0, 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[start] >= nums[mid]:
                end = mid
            else:
                start = mid

        pivot = start + 1

        left = bisect.bisect_left(nums, target, 0, pivot - 1)
        right = bisect.bisect_left(nums, target, pivot)

        if 0 <= left < pivot and nums[left] == target:
            return left
        elif pivot <= right < len(nums) and nums[right] == target:
            return right
        else:
            return -1


print(Solution().search([4,5,6,7,0,1,2],
0))