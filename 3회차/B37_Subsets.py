from copy import copy
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        prev = set()

        def dfs(i):
            prev.add(i)
            temp = copy(sorted(list(prev)))
            if temp not in result:
                result.append(temp)
                for j in nums:
                    if j not in prev:
                        dfs(j)
            prev.remove(i)

        for num in nums:
            dfs(num)
        return result


print(Solution().subsets(
[1,2,3]))