"""
itertools 이용 풀이
"""

from typing import List
from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(list(cb) for cb in combinations([i for i in range(1, n + 1)], k))
