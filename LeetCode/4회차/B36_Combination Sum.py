from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(comb, start, left):
            if left < 0:
                return
            if left == 0:
                res.append(comb)
                return

            for i in range(start, len(candidates)):
                dfs(comb + [candidates[i]], i, left - candidates[i])

        dfs([], 0, target)
        return res
