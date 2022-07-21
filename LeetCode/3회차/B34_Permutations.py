from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(list(i) for i in itertools.permutations(nums))
