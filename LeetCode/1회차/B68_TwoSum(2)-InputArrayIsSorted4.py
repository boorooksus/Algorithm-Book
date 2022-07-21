from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
투포인터 방식
"""