from typing import List
from collections import deque, defaultdict


class Solution:
    min_h = 100000 # 트리의 최소 높이

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set() # dfs 탐색할 대, 방문한 노드

        # 특정 노드를 root로 했을 때 트리의 높이를 탐색
        def dfs(cur: int) -> int:
            temp = set() # 자식 노드들의 높이들 저장 세트
            visit.add(cur)
            for i in graph[cur]:
                if i not in visit:
                    visit.add(i)
                    temp.add(dfs(i))

            if len(temp) == 0: # 자식 노드가 없는 경우
                return 0
            else: # 자식 노드들 중에서 가장 높은 높이 + 1 리턴
                return max(temp) + 1

        mht_set = set() # 최소 높이 트리가 되는 root 노드 세트

        for root in graph:
            height = dfs(root)
            if height < self.min_h: # 현재 발견된거 보다 최소 높이일 때
                self.min_h = height
                mht_set.clear()
                mht_set.add(root)

            elif self.min_h == height: # 최소 높이일 때
                mht_set.add(root)
            visit.clear()

        return list(mht_set)


sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))


"""
leetcode: 310
시간초과
"""