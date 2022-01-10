from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                j, top = stack.pop()
                answer[j] = i - j
            stack.append((i, temp))

        return answer
    