from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1

        return sorted(set(nums), key=lambda x: cnt[x], reverse=True)[:k]
    