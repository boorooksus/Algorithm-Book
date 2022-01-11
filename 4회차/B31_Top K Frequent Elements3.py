from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        hq = []

        for num in cnts:
            heapq.heappush(hq, (-cnts[num], num))

        res = []
        for i in range(k):
            res.append(heapq.heappop(hq)[1])
        return res
    