from typing import List
import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        nums2.sort()

        for i1, n1 in enumerate(nums1):
            i2 = bisect.bisect_left(nums2, n1)
            if i2 < len(nums2) and nums1[i1] == nums2[i2]:
                res.add(nums1[i1])
        return res



print(Solution().intersection(
[4,9,5],
[9,4,9,8,4]))