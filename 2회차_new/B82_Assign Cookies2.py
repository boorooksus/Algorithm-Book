from typing import List
from bisect import bisect_right


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0

        for i in s:
            idx = bisect_right(g, i)
            if idx > res:
                res += 1

        return res


print(Solution().findContentChildren([1,2], [1,2,3]))