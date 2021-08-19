from typing import List
from collections import defaultdict
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        result = []
        diagram = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):
            diagram[u].append(v)

        def dfs(src):
            while diagram[src]:
                dfs(diagram[src].pop())
            result.append(src)

        dfs("JFK")
        return result[::-1]


print(Solution().findItinerary(
[["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]))
