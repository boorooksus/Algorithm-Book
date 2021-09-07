from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        def dfs(cur: List[int]):
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for i in nums:
                if i not in cur:
                    cur.append(i)
                    dfs(cur)
                    cur.pop()

        dfs([])
        return ans


sol = Solution()
print(sol.permute([1,2,3]))

# leetcode: 46
# 백트래킹, dfs
# 리스트1을 리스트2에 넣은 후 리스트1을 수정하면 리스트2에 있는 것도 같이 수정됨
# dfs 후 pop하는 것 주의!
