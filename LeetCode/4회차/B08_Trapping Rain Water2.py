from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                top = stack.pop()

                if not stack:
                    break

                dist = i - stack[-1] - 1
                volume += (min(height[stack[-1]], h) - height[top]) * dist

            stack.append(i)

        return volume
