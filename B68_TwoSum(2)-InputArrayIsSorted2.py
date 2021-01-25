from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            if target - numbers[i] in numbers[i + 1:]:
                return [i + 1, i + 1 + numbers[i + 1:].index(target - numbers[i]) + 1]

        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
# print(sol.twoSum([0, 0], 0))

"""
leetcode: 167
"""