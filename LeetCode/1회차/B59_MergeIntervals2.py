from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals

        res = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res += i,  # ===== 1 ==================
        return res


"""
leetcode: 56
1: 맨 뒤에 콤마 - 리스트 형태로 추가. ('res += [i]' 와 같은 표현)
"""
