from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                break
            if target in matrix[i]:
                return True
        return False



print(Solution().searchMatrix([[-5]], -5))


