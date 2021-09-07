from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []
        for i, j in people:
            heapq.heappush(hq, [-i, j])
        res = []
        while hq:
            person = heapq.heappop(hq)
            res.insert(person[1], [-person[0], person[1]])
        return res

sol = Solution()
print(sol.reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))

"""
leetcode: 406
시간초과
"""