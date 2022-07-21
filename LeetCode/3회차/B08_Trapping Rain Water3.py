from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()

                if not stack:
                    break

                result += (i - stack[-1] - 1) * (min(height[stack[-1]], height[i]) - height[top])

            stack.append(i)

        return result


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
