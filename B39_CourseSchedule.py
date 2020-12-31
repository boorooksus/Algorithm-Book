from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        traced = set()
        dic = defaultdict(list)

        for a, b in prerequisites:
            dic[a].append(b)

        def dfs(cur: int):
            if cur in traced:
                return False

            traced.add(cur)
            for temp in dic[cur]:
                if not dfs(temp):
                    return False
            traced.remove(cur)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True


# leetcode: 207
# 한번에 모든 경로 돌 수 있는지 묻는 것이 아닌
# 그래프의 사이클 유무를 묻는 문제
