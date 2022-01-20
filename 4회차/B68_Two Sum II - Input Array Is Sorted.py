from typing import List
from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            idx = bisect_left(numbers, target - num, i + 1)

            if 0 <= idx < len(numbers) and num + numbers[idx] == target:
                return [i + 1, idx + 1]

        return []
