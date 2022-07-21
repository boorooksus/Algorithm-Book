from typing import List
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        for satisfaction in s:
            idx = bisect.bisect_right(g, satisfaction)
            if idx > res:
                res += 1
        return res
