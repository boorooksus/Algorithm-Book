from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hq = []
        for person in people:
            heapq.heappush(hq, [-person[0], person[1]])

        res = []
        while hq:
            person = heapq.heappop(hq)
            res.insert(person[1], [-person[1], person[1]])

        return res