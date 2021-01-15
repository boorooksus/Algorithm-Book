from typing import List
from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        leaves = []
        for i in graph:
            if len(graph[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            leaf = []
            for i in leaves:
                node = graph[i].pop()
                graph[node].remove(i)
                if len(graph[node]) == 1:
                    leaf.append(node)
            leaves = leaf

        return leaves


sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))


"""
leetcode: 310

"""