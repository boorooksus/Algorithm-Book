from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = Counter(nums)
        res = []
        for num, cnt in cnts.most_common(k):
            res.append(num)
        return res
