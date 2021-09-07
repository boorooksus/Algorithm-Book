from typing import List
import bisect


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0

        g.sort()
        s.sort()

        for i in s:
            idx = bisect.bisect_right(g, i)

            if res < idx:
                res += 1

        return res

print(Solution().findContentChildren([1, 2, 3], [1, 1]))
# print(Solution().findContentChildren([10,9,8,7], [5,6,7,8]))

"""
leetcode: 455
이진 탐색 이용 방법 
"""