from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        result, left, right = 0, 0, len(height) - 1
        water = [0 for _ in range(len(height))]
        cur = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > cur:
                    for i in range(left + 1, right):
                        water[i] = height[left]
                    cur = height[left]
                left += 1
            else:
                if height[right] > cur:
                    for i in range(left + 1, right):
                        water[i] = height[right]
                    cur = height[right]
                right -= 1

        for i in range(len(water)):
            if water[i] - height[i] > 0:
                result += water[i] - height[i]

        return result


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
