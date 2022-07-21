import heapq
from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        dist = {}
        for u, v, w in times:
            graph[u].append((v, w))

        hq = [(0, k)]
        while hq:
            w, v = heapq.heappop(hq)

            if v not in dist.keys():
                dist[v] = w

                for node, time in graph[v]:
                    heapq.heappush(hq, (w + time, node))

        if len(dist) != n:
            return -1
        return max(dist.values())


print(Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]],
3,
1))