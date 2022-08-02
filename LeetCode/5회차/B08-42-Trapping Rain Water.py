from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
                max_left = max(height[left], max_left)
            else:
                res += max_right - height[right]
                right -= 1
                max_right = max(height[right], max_right)
        return res


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))