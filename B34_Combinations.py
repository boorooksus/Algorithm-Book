from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans: List[List[int]] = []
        cur: List[int] = []

        def dfs(idx: int):
            if len(cur) == k:
                ans.append(cur[:])
                return

            for i in range(idx, n + 1):
                cur.append(i)
                dfs(i + 1)
                cur.pop()

        dfs(1)
        return ans


# leetcode: 77
# 조합, 백트래킹, dfs
