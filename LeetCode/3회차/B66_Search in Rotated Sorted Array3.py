from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot, start, end = 0, 0, len(nums) - 1
        while start < end:
            mid = start + (end - start) // 2
            if nums[end] >= nums[mid]:
                end = mid
            else:
                start = mid + 1

        pivot = start

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if target < nums[mid_pivot]:
                right = mid - 1
            elif target > nums[mid_pivot]:
                left = mid + 1
            else:
                return mid_pivot
        return -1


print(Solution().search([4,5,6,7,0,1,2],
0))