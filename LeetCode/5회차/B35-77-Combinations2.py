"""
dfs 풀이
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, path) -> None:
            if len(path) == k:
                ans.append(path)
                return
            if i > n:
                return
            for j in range(i, n + 1):
                dfs(j + 1, path + [j])

        if n < 1 or k == 0:
            return []
        ans = []
        dfs(1, [])
        return ans

