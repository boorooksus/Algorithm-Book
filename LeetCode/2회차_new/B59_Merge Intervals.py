from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        res = []

        for a, b in intervals[1:]:
            if end < a:
                res.append([start, end])
                start, end = a, b
            else:
                end = max(end, b)
        res.append([start, end])
        return res