from typing import List
import bisect


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)

        if idx < len(nums) and nums[idx] == target:
            return idx
        else:
            return -1


sol = Solution()
print(sol.search([-1,0,3,5,9,12], 2))


"""
leetcode: 704
bisect 이용 방식
"""