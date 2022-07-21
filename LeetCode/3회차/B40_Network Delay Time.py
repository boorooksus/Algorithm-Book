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

        while hq:
            time, node = heapq.heappop(hq)
            visit.add(node)
            if len(visit) == n:
                return time

            for v, w in graph[node]:
                if time + w < weight[v]:
                    weight[v] = time + w
                    heapq.heappush(hq, (time + w, v))

        return -1
