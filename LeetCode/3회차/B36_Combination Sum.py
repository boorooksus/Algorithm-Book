from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def combinations(index, path, target):
            if target < 0:
                return
            if target == 0:
                result.append(path)

            for i in range(index, len(candidates)):
                combinations(i, path + [candidates[i]], target - candidates[i])

        combinations(0, [], target)
        return result


# print(Solution().combinationSum(
# [2,3,5],
# 8))