from typing import List
import bisect


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        result = set()
        for num in nums1:
            idx = bisect.bisect_left(nums2, num)
            if 0 <= idx < len(nums2) and nums2[idx] == num:
                result.add(num)
        return list(result)


print(Solution().intersection([1,2],
[1,1]))