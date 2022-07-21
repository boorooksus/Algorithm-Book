from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def rotate_right(x: int, pivot: int) -> int:
            return (x + pivot) % len(nums)

        pivot, start, end = 0, 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        pivot = start

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            idx = rotate_right(mid, pivot)
            if target < nums[idx]:
                end = mid - 1
            elif target == nums[idx]:
                return idx
            else:
                start = mid + 1
        return -1


print(Solution().search([4,5,6,7,0,1,2],
0))