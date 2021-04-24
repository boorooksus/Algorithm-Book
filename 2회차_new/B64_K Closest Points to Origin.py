from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            dists.append((dist, point))
        dists.sort()
        res = []
        for i in range(k):
            res.append(dists[i][1])
        return res


print(Solution().kClosest([[1,3],[-2,2]],
1))