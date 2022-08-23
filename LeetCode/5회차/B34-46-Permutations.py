"""
itertools 이용한 풀이
"""
from typing import List
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(list(pmt) for pmt in permutations(nums))
