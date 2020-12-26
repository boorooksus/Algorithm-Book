from typing import List
from sys import setrecursionlimit
setrecursionlimit(10**9)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col, grid):
            grid[row][col] = "0"

            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            for i in range(4):
                cy = row + dy[i]
                cx = col + dx[i]

                if 0 <= cy < len(grid) and 0 <= cx < len(grid[0]) and \
                        grid[cy][cx] == "1":
                    dfs(cy, cx, grid)

        cnt: int = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j, grid)

        return cnt



# leetcode: 200
# visited 행렬 없이 풀이(공간 복잡도 O(n) 감소)
# grid 행렬 매번 인자로 안넘겨도 됨(중첩함수 - 부모의 변수 자식에서도 사용 가능)
