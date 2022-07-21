from typing import List
from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        dist = [[-1 for _ in range(100)] for _ in range(100)]
        hq = [(0, -1, src)]
        while hq:
            total_price, stops, apt = heapq.heappop(hq)

            if stops <= k and dist[stops][apt] == -1:
                if apt == dst:
                    return total_price
                dist[stops][apt] = total_price
                for next, price in graph[apt]:
                    heapq.heappush(hq, (total_price + price, stops + 1, next))

        return -1


print(Solution().findCheapestPrice(4,
[[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
0,
3,
1))