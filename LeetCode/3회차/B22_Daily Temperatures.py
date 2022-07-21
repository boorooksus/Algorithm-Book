import sys
from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = deque([])
        cur_max = -sys.maxsize
        temp = deque([])

        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= cur_max:
                cur_max = temperatures[i]
                temp = deque([cur_max])
                result.appendleft(0)

            else:
                x = 0
                while temperatures[i] >= temp[x]:
                    x += result[x]

                result.appendleft(x + 1)

                temp.appendleft(temperatures[i])
        return list(result)


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))