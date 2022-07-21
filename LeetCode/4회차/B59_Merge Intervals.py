from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        res = []
        start, end = intervals[0]
        for a, b in intervals[1:]:
            if end < a:
                res.append([start, end])
                start, end = a, b
            elif start <= a <= end < b:
                end = b

        res.append([start, end])

        return res
