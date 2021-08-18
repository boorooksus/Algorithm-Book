import sys
from typing import List
import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        weight = [sys.maxsize for _ in range(n + 1)]
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        hq = [(0, k)]
        weight[k] = 0
        weight[0] = 0

        while hq:
            time, node = heapq.heappop(hq)
            if node not in visit:
                visit.add(node)
                weight[node] = time
                for v, w in graph[node]:
                    heapq.heappush(hq, (time + w, v))

        if len(visit) == n:
            return max(weight)
        return -1


print(Solution().networkDelayTime(
[[1,2,1],[2,1,3]],
2,
2))