from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0

        child, cookie = 0, 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                res += 1
                cookie += 1
            child += 1

        return res
