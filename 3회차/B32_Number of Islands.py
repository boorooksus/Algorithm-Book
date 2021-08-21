from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        result = 0
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def dfs(island_id, row, col):
            if grid[row][col] != "1" or visit[row][col] != 0:
                return

            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            visit[row][col] = island_id

            for i in range(4):
                ny = row + dy[i]
                nx = col + dx[i]

                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                    dfs(island_id, ny, nx)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visit[i][j] == 0 and grid[i][j] == "1":
                    result += 1
                    dfs(result, i, j)

        return result

