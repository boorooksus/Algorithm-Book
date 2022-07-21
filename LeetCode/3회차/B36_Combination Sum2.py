from typing import List
from sys import setrecursionlimit
setrecursionlimit(10 ** 9)


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def runner(index, path, csum):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)

            for i in range(index, len(candidates)):
                if candidates[i] != 0:
                    runner(i, path + [candidates[i]], csum - candidates[i])

        runner(0, [], target)
        return result


# print(Solution().combinationSum(
# [2,3,5],
# 8))