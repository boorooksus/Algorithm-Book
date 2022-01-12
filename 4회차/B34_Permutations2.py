from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm)
                return

            for num in nums:
                if num not in perm:
                    dfs(perm + [num])

        res = []
        dfs([])

        return res


print(Solution().permute([1,2,3]))