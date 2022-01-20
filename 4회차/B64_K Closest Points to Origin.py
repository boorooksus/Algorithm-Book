from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for x, y in points:
            heapq.heappush(hq, (x ** 2 + y ** 2, [x, y]))

        res = []
        for i in range(k):
            if hq:
                res.append(heapq.heappop(hq)[1])
        return res


print(Solution().kClosest([[1,3],[-2,2]],
1))