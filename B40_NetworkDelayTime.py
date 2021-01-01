from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = defaultdict(list)
        for a, b, c in times:
            graph[a].append((b, c))

        Q = [(0, K)]
        dist = defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())
        return -1


# leetcode: 743
# 다익스트라
# 다시 풀어볼 것
