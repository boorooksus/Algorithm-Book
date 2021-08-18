from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        flights_d = defaultdict(list)
        for start, end, price in flights:
            flights_d[start].append((end, price))

        hq = [(0, src, 0)]
        while hq:
            cp, cn, cd = heapq.heappop(hq)
            if cn == dst:
                return cp
            if cd > k:
                continue
            for nn, p in flights_d[cn]:
                np = cp + p
                heapq.heappush(hq, (np, nn, cd + 1))

        return -1


print(Solution().findCheapestPrice(3,
[[0,1,100],[1,2,100],[0,2,500]],
0,
2,
1))
