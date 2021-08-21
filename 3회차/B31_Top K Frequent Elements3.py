from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(list(i) for i in zip(*Counter(nums).most_common(k)))[0]
