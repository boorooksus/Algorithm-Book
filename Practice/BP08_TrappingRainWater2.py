from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = height[stack.pop()]

                if not stack:
                    break

                distance = i - stack[-1] - 1
                volume += (min(height[stack[-1]], height[i]) - top) * distance

            stack.append(i)

        return volume
