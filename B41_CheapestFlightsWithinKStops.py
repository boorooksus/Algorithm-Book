from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w, v))

        Q = [(0, src, -1)]
        dist = defaultdict(list)

        while Q:
            price, node, stops = heapq.heappop(Q)

            if node == dst:
                return price

            if stops < K:
                for w, v in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, stops + 1))

        return -1


sol = Solution()
# print(sol.findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1))
print(sol.findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1))


# leetcode 787
# 다익스트라
# 다시 풀어볼것
