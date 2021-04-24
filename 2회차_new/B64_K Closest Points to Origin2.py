from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(dists, (dist, point))
        res = []
        for i in range(k):
            res.append(heapq.heappop(dists)[1])
        return res


print(Solution().kClosest([[1,3],[-2,2]],
1))