from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        result = 0
        visit = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def bfs(island_id, row, col):
            dy = [1, -1, 0, 0]
            dx = [0, 0, 1, -1]

            dq = deque([(row, col)])

            while dq:
                cy, cx = dq.popleft()

                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]

                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) \
                            and grid[ny][nx] == "1" and visit[ny][nx] == 0:
                        visit[ny][nx] = island_id
                        dq.append((ny, nx))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visit[i][j] == 0 and grid[i][j] == "1":
                    result += 1
                    bfs(result, i, j)

        return result
