from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []

        for h, o in people:
            heapq.heappush(hq, (-h, o))

        res = []
        while hq:
            h, o = heapq.heappop(hq)
            res.insert(o, [-h, o])
        return res
