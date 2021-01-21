from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        intervals.sort()
        start, end = intervals[0][0], intervals[0][1]
        res = []
        for a, b in intervals[1:]:
            if end < a:
                res.append([start, end])
                start = a
            if end < b:  # ========== 1 =======================
                end = b
        res.append([start, end])
        return res


"""
leetcode: 56
1: 범위가 이전 범위 안에 포함되는 경우 고려
"""
