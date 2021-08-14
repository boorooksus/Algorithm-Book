from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        result = 0
        for i in range(k):
            result = -heapq.heappop(heap)
        return result

