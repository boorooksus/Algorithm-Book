import sys
from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaves = []
        for vertex in graph:
            if len(graph[vertex]) == 1:
                leaves.append(vertex)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves


print(Solution().findMinHeightTrees(4,
[[1,0],[1,2],[1,3]]))
