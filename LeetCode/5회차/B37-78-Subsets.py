from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(idx, path) -> None:
            ans.append(path)

            for j in range(idx + 1, len(nums)):
                dfs(j, path + [nums[j]])

        ans = []
        dfs(-1, [])
        return ans
