"""
dfs 이용한 풀이
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visit = [False] * len(nums)
        ans = []

        def dfs(path: List[int]) -> None:
            if len(path) == len(nums):
                ans.append(path)

            for i, num in enumerate(nums):
                if not visit[i]:
                    visit[i] = True
                    dfs(path + [num])
                    visit[i] = False

        dfs([])
        return ans
