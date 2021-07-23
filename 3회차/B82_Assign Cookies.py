from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res, cur = 0, 0
        g.sort()
        s.sort()

        for i in range(len(s)):
            if cur < len(g) and s[i] >= g[cur]:
                res += 1
                cur += 1

        return res
