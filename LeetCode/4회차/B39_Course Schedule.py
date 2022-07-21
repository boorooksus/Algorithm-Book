from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced, visited = set(), set()

        def dfs(a: int) -> bool:
            if a in traced:
                return False
            if a in visited:
                return True

            traced.add(a)
            for num in graph[a]:
                if not dfs(num):
                    return False
            traced.remove(a)
            visited.add(a)
            return True

        for num in list(graph):
            if not dfs(num):
                return False
        return True
