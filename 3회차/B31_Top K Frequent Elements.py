from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(i[0] for i in Counter(nums).most_common(k))
