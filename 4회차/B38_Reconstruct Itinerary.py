from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []

        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        return route[::-1]


print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"], ["SFO", "JFK"]]))
# print(Solution().findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))