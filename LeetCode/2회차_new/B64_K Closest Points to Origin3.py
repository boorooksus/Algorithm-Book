from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)


print(Solution().kClosest([[1,3],[-2,2]], 1))