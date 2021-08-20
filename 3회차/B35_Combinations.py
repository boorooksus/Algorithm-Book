from typing import List
import itertools

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        return list(list(i) for i in itertools.combinations(nums, k))


print(Solution().combine(4, 2))