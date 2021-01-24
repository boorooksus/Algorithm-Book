from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        turning = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                turning = i
        start, end = 0, len(nums) - 1

        if target < nums[start]:
            start = turning
        elif target > nums[end]:
            end = turning - 1

        mid = (start + end) // 2

        while start <= mid:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start, mid = mid + 1, (mid + end) // 2
            else:
                end, mid = mid, (mid + start) // 2
        return -1

