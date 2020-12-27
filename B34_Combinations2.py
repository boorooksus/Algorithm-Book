from typing import List
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #pool = list(i for i in range(1, n + 1))
        #return list(map(list, itertools.combinations(pool, k)))
        return list(itertools.combinations(range(1, n + 1), k))


# leetcode: 77
# 조합, 백트래킹, dfs
# itertools 활용
