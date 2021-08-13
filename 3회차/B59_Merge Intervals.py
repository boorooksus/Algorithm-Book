from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if end < intervals[i][0]:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif end < intervals[i][1]:
                end = intervals[i][1]

        result.append([start, end])
        return result


print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
