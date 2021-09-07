from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        cset: List[int] = []

        def dfs(idx: int):
            ans.append(cset[:])

            for i in range(idx, len(nums)):
                cset.append(nums[i])
                dfs(i + 1)
                cset.pop()

        dfs(0)
        return ans


sol = Solution()
print(sol.subsets([1,2,3]))


# leetcode: 78
# dfs, 백트래킹
# 매번 결과를 추가하는 방법
