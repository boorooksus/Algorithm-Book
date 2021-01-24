from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, mid, end = 0, len(nums) // 2, len(nums)

        while start < mid:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start, mid = mid, (mid + end) // 2
            else:
                mid, end = (start + mid) // 2, mid
        if nums[start] == target:
            return start
        return -1

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 2))