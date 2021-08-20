from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path):
            if len(path) == len(nums):
                result.append(path)

            for num in nums:
                if num not in path:
                    dfs(path + [num])

        dfs([])
        return result

