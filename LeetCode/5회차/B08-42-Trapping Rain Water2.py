from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()

                if not stack:
                    break

                water = min(height[i] - height[top], height[stack[-1]] - height[top])
                res += water * (i - stack[-1] - 1)

            stack.append(i)

        return res


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))