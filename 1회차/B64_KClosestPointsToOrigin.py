from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = {}
        for a, b in points:
            dist[(a, b)] = a**2 + b**2

        return sorted(points, key=lambda x: dist[(x[0], x[1])])[:K]


sol = Solution()
print(sol.kClosest([[1,3],[-2,2]], 1))

"""
leetcode: 793
"""