from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0

        g.sort()
        s.sort()

        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res

# print(Solution().findContentChildren([1, 2, 3], [1, 1]))
print(Solution().findContentChildren([10,9,8,7], [5,6,7,8]))

"""
leetcode: 455
그리디 알고리즘
"""