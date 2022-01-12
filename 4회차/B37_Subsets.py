from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, last, k):
            if len(subset) == k:
                res.append(subset)
                return

            for i in range(last + 1, len(nums)):
                dfs(subset + [nums[i]], i, k)

        for i in range(len(nums) + 1):
            dfs([], -1, i)
        return res
    