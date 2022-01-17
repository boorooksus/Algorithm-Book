from typing import List
from collections import defaultdict, deque
import sys


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)

        while n > 2:
            n -= len(leaves)
            new = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new.append(neighbor)

            leaves = new

        return leaves


