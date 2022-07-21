from typing import List
from bisect import bisect_right


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            idx = bisect_right(g, s[i])
            if idx > res:
                res += 1

        return res
