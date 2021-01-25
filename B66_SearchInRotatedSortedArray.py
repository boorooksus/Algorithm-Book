from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(start, end):
            if start > end:
                return -1

            mid = start + (end - start) // 2
            if nums[mid] < target:
                return bs(mid + 1, end)
            elif nums[mid] > target:
                return bs(start, mid - 1)
            else:
                return mid

        tp = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                tp = i

        left = bs(0, tp - 1)
        right = bs(tp, len(nums) - 1)

        if left == right == -1:
            return -1
        elif left != -1:
            return left
        else:
            return right


"""
leetcode: 33
"""