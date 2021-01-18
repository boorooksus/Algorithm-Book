from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        for i in range(k):
            ans = nums.pop()
        return ans


"""
leetcode: 215
"""