from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

            if left_max < right_max:
                result += left_max - height[left]
                left += 1
            else:
                result += right_max - height[right]
                right -= 1

        return result


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
