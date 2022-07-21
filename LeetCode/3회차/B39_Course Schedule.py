from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited, traced = set(), set()
        diagram = defaultdict(list)

        for prerequisite in prerequisites:
            diagram[prerequisite[0]].append(prerequisite[1])

        def dfs(i: int):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for j in diagram[i]:
                if not dfs(j):
                    return False

            traced.remove(i)
            visited.add(i)
            return True

        for i in list(diagram):
            if not dfs(i):
                return False
        return True
