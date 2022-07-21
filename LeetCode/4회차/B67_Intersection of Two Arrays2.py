from typing import List
from bisect import bisect_left


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2.sort()
        res = []
        for num in nums1:
            idx = bisect_left(nums2, num)
            if 0 <= idx < len(nums2) and num == nums2[idx]:
                res.append(num)
        return res


print(Solution().intersection([4,9,5],
[9,4,9,8,4]))