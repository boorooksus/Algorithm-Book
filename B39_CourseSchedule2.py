from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced = set()
        visit = set()
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(cur):
            if cur in traced:
                return False
            if cur in visit:
                return True

            traced.add(cur)
            for i in graph[cur]:
                if not dfs(i):
                    return False
            traced.remove(cur)
            visit.add(cur)

            return True

        for i in list(graph):
            if not dfs(i):
                return False

        return True

# leetcode: 207
# 한 번 검증된 노드는 더이상 체크하지 않는 방식 -> 시간 절약
