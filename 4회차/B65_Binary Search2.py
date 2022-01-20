from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start: int, end: int) -> int:
            if start > end:
                return -1

            mid = (start + end) // 2
            if target < nums[mid]:
                return binary_search(start, mid - 1)
            elif target == nums[mid]:
                return mid
            else:
                return binary_search(mid + 1, end)

        return binary_search(0, len(nums) - 1)


print(Solution().search([-1,0,3,5,9,12],
9))