from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        cset: List[int] = []

        def dfs(idx: int):
            if idx == len(nums) and cset not in ans:
                ans.append(cset[:])

            for i in range(idx, len(nums)):
                dfs(i + 1)
                cset.append(nums[i])
                dfs(i + 1)
                cset.pop()

        dfs(0)
        return ans


sol = Solution()
print(sol.subsets([1,2,3]))


# leetcode: 78
# dfs, 백트래킹