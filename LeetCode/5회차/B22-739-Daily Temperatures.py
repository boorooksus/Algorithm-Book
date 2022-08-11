from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                temperatures[prev] = i - prev
            stack.append(i)

        while stack:
            temperatures[stack.pop()] = 0

        return temperatures
