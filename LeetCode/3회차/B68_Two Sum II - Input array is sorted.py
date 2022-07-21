from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            x = bisect.bisect_left(numbers, target - num, i + 1, len(numbers) - 1)
            if numbers[x] == target - num:
                return [i + 1, x + 1]
        return [-1]


print(Solution().twoSum([5,25,75],
100))