from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            idx = bisect_left(row, target)
            if 0 <= idx < len(row) and row[idx] == target:
                return True
        return False

"""
leetcode: 240
bisect 이용 풀이
"""