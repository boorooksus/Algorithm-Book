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

        nl = n
        leaves = []

        for node in connections.keys():
            if len(connections[node]) == 1:
                leaves.append(node)

        while nl > 2:
            nl -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                cur = connections[leaf].pop()
                connections[cur].remove(leaf)

                if len(connections[cur]) == 1:
                    new_leaves.append(cur)

            leaves = new_leaves

        return leaves


print(Solution().findMinHeightTrees(4,
[[1,0],[1,2],[1,3]]))