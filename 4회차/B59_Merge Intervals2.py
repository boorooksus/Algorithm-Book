from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for a, b in sorted(intervals, key=lambda x: x[0]):
            if res and a <= res[-1][1]:
                res[-1][1] = max(res[-1][1], b)
            else:
                res += [a, b],

        return res
