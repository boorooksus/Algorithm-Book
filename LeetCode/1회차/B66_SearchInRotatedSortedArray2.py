from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = nums.index(min(nums))
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2
            mid_pivot = (pivot + mid) % len(nums)

            if nums[mid_pivot] < target:
                start = mid + 1
            elif nums[mid_pivot] > target:
                end = mid - 1
            else:
                return mid_pivot

        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2], 0))

"""
leetcode: 33
"""