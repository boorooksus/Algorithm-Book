from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        hq = []
        for a, b in points:
            dist = a**2 + b**2
            heapq.heappush(hq, (dist, a, b))

        res = []
        for i in range(K):
            dist, a, b = heapq.heappop(hq)
            res.append([a, b])
        return res


sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))

"""
leetcode: 793
heapq 이용한 방식
"""