from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any(target in row for row in matrix)

"""
leetcode: 240
파이썬 다운 풀이
any() 와 all()
"""