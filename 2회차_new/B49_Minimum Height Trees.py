from typing import List
from collections import defaultdict, deque
import sys


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        connections = defaultdict(list)

        for a, b in edges:
            connections[a].append(b)
            connections[b].append(a)

        res = []
        min_height = sys.maxsize
        for root in connections.keys():
            height = 0
            visit = [0 for _ in range(n)]
            dq = deque()
            dq.appendleft(root)
            while dq:
                degree = len(dq)
                height += 1
                for i in range(degree):
                    cur = dq.pop()
                    visit[cur] = 1
                    for child in connections[cur]:
                        if visit[child] == 0:
                            dq.appendleft(child)
            if height == min_height:
                res.append(root)
            elif height < min_height:
                min_height = height
                res = [root]

        return res


print(Solution().findMinHeightTrees(4,
[[1,0],[1,2],[1,3]]))