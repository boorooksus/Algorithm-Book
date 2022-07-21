import sys
from typing import List
from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def get_height(root: int):
            dq = deque([root])
            visit = []
            result = 0
            while dq:
                result += 1
                for _ in range(len(dq)):
                    cur = dq.popleft()
                    visit.append(cur)
                    for neighbor in graph[cur]:
                        if neighbor not in visit:
                            dq.append(neighbor)
            return result

        if not edges:
            return [0]

        vertices = set()
        graph = defaultdict(list)
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        min_height = sys.maxsize
        ans = []
        for vertex in vertices:
            height = get_height(vertex)
            if height < min_height:
                min_height = height
                ans = [vertex]
            elif height == min_height:
                ans.append(vertex)

        return ans


print(Solution().findMinHeightTrees(4,
[[1,0],[1,2],[1,3]]))
