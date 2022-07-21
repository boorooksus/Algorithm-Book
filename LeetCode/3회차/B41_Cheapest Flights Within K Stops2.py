import sys
from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        if src == dst:
            return 0

        graph = defaultdict(list)
        weight = [(sys.maxsize, 0) for _ in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))

        hq = [(0, src, k)]
        while hq:
            price, node, dist = heapq.heappop(hq)
            if node == dst:
                return price
            if dist >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    if alt < weight[v][0] or dist - 1 >= weight[v][1]:
                        weight[v] = (alt, dist - 1)
                        heapq.heappush(hq, (alt, v, dist - 1))
        return -1


print(Solution().findCheapestPrice(3,
[[0,1,100],[1,2,100],[0,2,500]],
0,
2,
1))
