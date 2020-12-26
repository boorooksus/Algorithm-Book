from typing import List
from sys import setrecursionlimit
setrecursionlimit(10**9)


class Solution:
    def dfs(self, row, col, grid, visited):
        visited[row][col] = "1"

        dy = [1, -1, 0, 0]
        dx = [0, 0, 1, -1]

        for i in range(4):
            cy = row + dy[i]
            cx = col + dx[i]

            if 0 <= cy < len(visited) and 0 <= cx < len(visited[0]) and \
                    grid[cy][cx] == "1" and visited[cy][cx] == "0":
                self.dfs(cy, cx, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited: List[List[str]] = [["0" for _ in range(len(grid[0]))] for _ in range(len(grid))]
        cnt: int = 0

        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if grid[i][j] == "1" and visited[i][j] == "0":
                    cnt += 1
                    self.dfs(i, j, grid, visited)

        return cnt

sol = Solution()
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

# leetcode: 200
# grid 리스트의 자료형이 int가 아닌 str이라서 헤맴(조건문에서 visited == "0" 이렇게 써야함).
