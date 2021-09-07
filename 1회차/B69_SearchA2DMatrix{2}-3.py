from typing import List
from bisect import bisect_left


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False

"""
leetcode: 240

"""