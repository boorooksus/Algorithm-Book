from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            cur = matrix[row][col]
            if cur == target:
                return True
            elif cur > target:
                col -= 1
            elif cur < target:
                row += 1
        return False



print(Solution().searchMatrix([[-5]], -5))


