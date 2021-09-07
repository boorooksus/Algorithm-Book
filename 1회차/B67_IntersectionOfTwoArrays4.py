from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.add(nums1[i])
                i += 1
                j += 1

        return list(res)


sol = Solution()
print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))

"""
leetcode: 349
투포인터 이용 방식
"""
