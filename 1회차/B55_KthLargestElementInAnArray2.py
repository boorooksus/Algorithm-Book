from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in nums:
            heapq.heappush(pq, -i)
        ans = 0
        for i in range(k):
            ans = -heapq.heappop(pq)
        return ans

"""
leetcode: 215
"""