from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(cy: int, cx: int):
            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            visit[cy][cx] = 1

            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]

                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) \
                        and visit[ny][nx] == 0 and grid[ny][nx] == '1':
                    dfs(ny, nx)

        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visit[i][j] == 0 and grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
