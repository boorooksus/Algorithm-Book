from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(idx, s, path: List[int]) -> None:
            if s == target:
                ans.append(path)

            if s > target or idx == len(candidates):
                return

            for next in range(idx, len(candidates)):
                dfs(next, s + candidates[next], path + [candidates[next]])

        ans = []
        dfs(0, 0, [])
        return ans
