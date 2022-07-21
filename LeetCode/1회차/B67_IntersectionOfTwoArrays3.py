from typing import List
from sys import setrecursionlimit
import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums2.sort()
        for i in nums1:
            idx = bisect.bisect_left(nums2, i)
            if idx < len(nums2) and nums2[idx] == i:
                res.add(i)

        return list(res)


sol = Solution()
print(sol.intersection([4,9,5], [9,4,9,8,4]))

"""
leetcode: 349
bisect 이용한 풀이
"""