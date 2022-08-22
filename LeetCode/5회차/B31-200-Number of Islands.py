from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(y: int, x: int) -> int:
            dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

            if grid[y][x] != "1":
                return 0

            dq = deque([(y, x)])
            grid[y][x] = "2"
            while dq:
                cy, cx = dq.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) \
                            and grid[ny][nx] == "1":
                        dq.append((ny, nx))
                        grid[ny][nx] = "2"
            return 1

        if not grid:
            return 0

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cnt += bfs(i, j)
        return cnt

