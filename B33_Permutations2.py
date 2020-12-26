import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, itertools.permutations(nums)))

# leetcode: 46
# itertools 이용
