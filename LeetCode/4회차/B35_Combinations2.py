from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def dfs(comb: List, last: int) -> None:
            if len(comb) == k:
                res.append(comb)
                return

            for i in range(last + 1, n):
                dfs(comb + [nums[i]], i)

        nums = [i for i in range(1, n + 1)]
        res = []

        dfs([], -1)
        return res
