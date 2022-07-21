from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans: List[str] = []
        dic = defaultdict(list)

        for dep, des in sorted(tickets, reverse=True):
            dic[dep].append(des)

        def dfs(cur: str):
            while dic[cur]:
                dfs(dic[cur].pop())
            ans.append(cur)

        dfs("JFK")
        return ans[::-1]


sol = Solution()
print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))


# leetcode: 332
# dfs
# 다시 풀어볼 것
