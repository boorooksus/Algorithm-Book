from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        for num in nums1:
            if num in nums2:
                result.add(num)
        return list(result)
    