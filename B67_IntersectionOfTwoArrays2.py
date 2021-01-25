from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def bs(nums: List[int], start: int, end: int, target: int) -> int:
            if start > end:
                return -1
            mid = start + (end - start) // 2
            if nums[mid] < target:
                return bs(nums, mid + 1, end, target)
            elif nums[mid] > target:
                return bs(nums, start, mid - 1, target)
            else:
                return mid

        res = set()
        for i in nums1:
            if bs(sorted(nums2), 0, len(nums2) - 1, i) != -1:
                res.add(i)

        return list(res)


"""
leetcode: 349
binary search 이용한 풀이
"""