from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []

        for start, end in sorted(intervals, key=lambda x: x[0]):
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result += [start, end],
        return result



print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
